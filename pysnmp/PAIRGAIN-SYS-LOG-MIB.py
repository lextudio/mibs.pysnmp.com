# SNMP MIB module (PAIRGAIN-SYS-LOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PAIRGAIN-SYS-LOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:26 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(pgainSysLog,) = mibBuilder.importSymbols(
    "PAIRGAIN-COMMON-HD-MIB",
    "pgainSysLog")

(TimeSeconds,) = mibBuilder.importSymbols(
    "PAIRGAIN-DSLAM-CHASSIS-MIB",
    "TimeSeconds")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class PgSysLogType(Integer32):
    """Custom type PgSysLogType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 3),
          ("bintrace", 7),
          ("clralarm", 4),
          ("debug", 9),
          ("error", 2),
          ("info", 6),
          ("trap", 5),
          ("txttrace", 8),
          ("unknown", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PgSystemLogTable_Object = MibTable
pgSystemLogTable = _PgSystemLogTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 10, 1)
)
if mibBuilder.loadTexts:
    pgSystemLogTable.setStatus("mandatory")
_PgSystemLogEntry_Object = MibTableRow
pgSystemLogEntry = _PgSystemLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 10, 1, 1)
)
pgSystemLogEntry.setIndexNames(
    (0, "PAIRGAIN-SYS-LOG-MIB", "pgSystemLogId"),
)
if mibBuilder.loadTexts:
    pgSystemLogEntry.setStatus("mandatory")
_PgSystemLogId_Type = Integer32
_PgSystemLogId_Object = MibTableColumn
pgSystemLogId = _PgSystemLogId_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 10, 1, 1, 1),
    _PgSystemLogId_Type()
)
pgSystemLogId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSystemLogId.setStatus("mandatory")
_PgSystemLogTimeStamp_Type = TimeSeconds
_PgSystemLogTimeStamp_Object = MibTableColumn
pgSystemLogTimeStamp = _PgSystemLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 10, 1, 1, 2),
    _PgSystemLogTimeStamp_Type()
)
pgSystemLogTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSystemLogTimeStamp.setStatus("mandatory")
_PgSystemLogType_Type = PgSysLogType
_PgSystemLogType_Object = MibTableColumn
pgSystemLogType = _PgSystemLogType_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 10, 1, 1, 3),
    _PgSystemLogType_Type()
)
pgSystemLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSystemLogType.setStatus("mandatory")
_PgSystemLogSlotId_Type = Integer32
_PgSystemLogSlotId_Object = MibTableColumn
pgSystemLogSlotId = _PgSystemLogSlotId_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 10, 1, 1, 4),
    _PgSystemLogSlotId_Type()
)
pgSystemLogSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSystemLogSlotId.setStatus("mandatory")
_PgSystemLogDescription_Type = DisplayString
_PgSystemLogDescription_Object = MibTableColumn
pgSystemLogDescription = _PgSystemLogDescription_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 10, 1, 1, 5),
    _PgSystemLogDescription_Type()
)
pgSystemLogDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSystemLogDescription.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PAIRGAIN-SYS-LOG-MIB",
    **{"DisplayString": DisplayString,
       "PgSysLogType": PgSysLogType,
       "pgSystemLogTable": pgSystemLogTable,
       "pgSystemLogEntry": pgSystemLogEntry,
       "pgSystemLogId": pgSystemLogId,
       "pgSystemLogTimeStamp": pgSystemLogTimeStamp,
       "pgSystemLogType": pgSystemLogType,
       "pgSystemLogSlotId": pgSystemLogSlotId,
       "pgSystemLogDescription": pgSystemLogDescription}
)
