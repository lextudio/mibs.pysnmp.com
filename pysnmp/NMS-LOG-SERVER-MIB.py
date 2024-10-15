# SNMP MIB module (NMS-LOG-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NMS-LOG-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:01 2024
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

(nmslocal,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nmslocal")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LogServer_ObjectIdentity = ObjectIdentity
logServer = _LogServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 235)
)
_LogServerTable_Object = MibTable
logServerTable = _LogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 235, 1)
)
if mibBuilder.loadTexts:
    logServerTable.setStatus("mandatory")
_LogServerTableEntry_Object = MibTableRow
logServerTableEntry = _LogServerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 235, 1, 1)
)
logServerTableEntry.setIndexNames(
    (0, "NMS-LOG-SERVER-MIB", "logServerLevel"),
    (0, "NMS-LOG-SERVER-MIB", "logServerAddr"),
)
if mibBuilder.loadTexts:
    logServerTableEntry.setStatus("mandatory")


class _LogServerLevel_Type(Integer32):
    """Custom type logServerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("emerg", 0),
          ("error", 3),
          ("info", 6),
          ("notice", 5),
          ("warning", 4))
    )


_LogServerLevel_Type.__name__ = "Integer32"
_LogServerLevel_Object = MibTableColumn
logServerLevel = _LogServerLevel_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 235, 1, 1, 1),
    _LogServerLevel_Type()
)
logServerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logServerLevel.setStatus("mandatory")
_LogServerAddr_Type = IpAddress
_LogServerAddr_Object = MibTableColumn
logServerAddr = _LogServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 235, 1, 1, 2),
    _LogServerAddr_Type()
)
logServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logServerAddr.setStatus("mandatory")
_LogServerRowStatus_Type = RowStatus
_LogServerRowStatus_Object = MibTableColumn
logServerRowStatus = _LogServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 235, 1, 1, 3),
    _LogServerRowStatus_Type()
)
logServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    logServerRowStatus.setStatus("mandatory")


class _LogServerOff_Type(Integer32):
    """Custom type logServerOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 0))
    )


_LogServerOff_Type.__name__ = "Integer32"
_LogServerOff_Object = MibScalar
logServerOff = _LogServerOff_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 235, 2),
    _LogServerOff_Type()
)
logServerOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logServerOff.setStatus("mandatory")
_LogTrapTable_Object = MibTable
logTrapTable = _LogTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 235, 3)
)
if mibBuilder.loadTexts:
    logTrapTable.setStatus("mandatory")
_LogTrapTableEntry_Object = MibTableRow
logTrapTableEntry = _LogTrapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 235, 3, 1)
)
logTrapTableEntry.setIndexNames(
    (0, "NMS-LOG-SERVER-MIB", "logTrapLevel"),
    (0, "NMS-LOG-SERVER-MIB", "logTrapAddr"),
)
if mibBuilder.loadTexts:
    logTrapTableEntry.setStatus("mandatory")
_LogTrapAddr_Type = IpAddress
_LogTrapAddr_Object = MibTableColumn
logTrapAddr = _LogTrapAddr_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 235, 3, 1, 1),
    _LogTrapAddr_Type()
)
logTrapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logTrapAddr.setStatus("mandatory")
_LogTrapRowStatus_Type = RowStatus
_LogTrapRowStatus_Object = MibTableColumn
logTrapRowStatus = _LogTrapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 235, 3, 1, 2),
    _LogTrapRowStatus_Type()
)
logTrapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    logTrapRowStatus.setStatus("mandatory")


class _LogTrapRfcVer_Type(Integer32):
    """Custom type logTrapRfcVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("RFC3164", 0),
          ("RFC5424", 1))
    )


_LogTrapRfcVer_Type.__name__ = "Integer32"
_LogTrapRfcVer_Object = MibTableColumn
logTrapRfcVer = _LogTrapRfcVer_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 235, 3, 1, 3),
    _LogTrapRfcVer_Type()
)
logTrapRfcVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logTrapRfcVer.setStatus("mandatory")


class _LogTrap_Type(Integer32):
    """Custom type logTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("emerg", 0),
          ("error", 3),
          ("info", 6),
          ("notice", 5),
          ("warning", 4))
    )


_LogTrap_Type.__name__ = "Integer32"
_LogTrap_Object = MibScalar
logTrap = _LogTrap_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 235, 4),
    _LogTrap_Type()
)
logTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logTrap.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-LOG-SERVER-MIB",
    **{"logServer": logServer,
       "logServerTable": logServerTable,
       "logServerTableEntry": logServerTableEntry,
       "logServerLevel": logServerLevel,
       "logServerAddr": logServerAddr,
       "logServerRowStatus": logServerRowStatus,
       "logServerOff": logServerOff,
       "logTrapTable": logTrapTable,
       "logTrapTableEntry": logTrapTableEntry,
       "logTrapAddr": logTrapAddr,
       "logTrapRowStatus": logTrapRowStatus,
       "logTrapRfcVer": logTrapRfcVer,
       "logTrap": logTrap}
)
