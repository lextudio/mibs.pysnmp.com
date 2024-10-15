# SNMP MIB module (DSLAM-FLASH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DSLAM-FLASH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:39 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(pgainDSLAM,) = mibBuilder.importSymbols(
    "PAIRGAIN-COMMON-HD-MIB",
    "pgainDSLAM")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

pgDSLAMFlashMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PgDSLAMFlashObjects_ObjectIdentity = ObjectIdentity
pgDSLAMFlashObjects = _PgDSLAMFlashObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 5, 1)
)


class _PgDSLAMFlashOperStatus_Type(Integer32):
    """Custom type pgDSLAMFlashOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("failed", 4),
          ("inProgress", 3),
          ("none", 1),
          ("success", 2))
    )


_PgDSLAMFlashOperStatus_Type.__name__ = "Integer32"
_PgDSLAMFlashOperStatus_Object = MibScalar
pgDSLAMFlashOperStatus = _PgDSLAMFlashOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 5, 1, 1),
    _PgDSLAMFlashOperStatus_Type()
)
pgDSLAMFlashOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDSLAMFlashOperStatus.setStatus("mandatory")


class _PgDSLAMFlashDownLoad_Type(OctetString):
    """Custom type pgDSLAMFlashDownLoad based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PgDSLAMFlashDownLoad_Type.__name__ = "OctetString"
_PgDSLAMFlashDownLoad_Object = MibScalar
pgDSLAMFlashDownLoad = _PgDSLAMFlashDownLoad_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 5, 1, 2),
    _PgDSLAMFlashDownLoad_Type()
)
pgDSLAMFlashDownLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgDSLAMFlashDownLoad.setStatus("mandatory")


class _PgDSLAMFlashUpLoad_Type(OctetString):
    """Custom type pgDSLAMFlashUpLoad based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PgDSLAMFlashUpLoad_Type.__name__ = "OctetString"
_PgDSLAMFlashUpLoad_Object = MibScalar
pgDSLAMFlashUpLoad = _PgDSLAMFlashUpLoad_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 5, 1, 3),
    _PgDSLAMFlashUpLoad_Type()
)
pgDSLAMFlashUpLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgDSLAMFlashUpLoad.setStatus("mandatory")


class _PgDSLAMFlashCopyFile_Type(OctetString):
    """Custom type pgDSLAMFlashCopyFile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PgDSLAMFlashCopyFile_Type.__name__ = "OctetString"
_PgDSLAMFlashCopyFile_Object = MibScalar
pgDSLAMFlashCopyFile = _PgDSLAMFlashCopyFile_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 5, 1, 4),
    _PgDSLAMFlashCopyFile_Type()
)
pgDSLAMFlashCopyFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgDSLAMFlashCopyFile.setStatus("mandatory")
_PgModemXferTable_Object = MibTable
pgModemXferTable = _PgModemXferTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 5, 1, 5)
)
if mibBuilder.loadTexts:
    pgModemXferTable.setStatus("mandatory")
_PgModemXferEntry_Object = MibTableRow
pgModemXferEntry = _PgModemXferEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 5, 1, 5, 1)
)
pgModemXferEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pgModemXferEntry.setStatus("mandatory")


class _PgModemXferOperStatus_Type(Integer32):
    """Custom type pgModemXferOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("failed", 4),
          ("inProgress", 3),
          ("none", 1),
          ("success", 2))
    )


_PgModemXferOperStatus_Type.__name__ = "Integer32"
_PgModemXferOperStatus_Object = MibTableColumn
pgModemXferOperStatus = _PgModemXferOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 5, 1, 5, 1, 1),
    _PgModemXferOperStatus_Type()
)
pgModemXferOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgModemXferOperStatus.setStatus("mandatory")


class _PgModemXferSourceFilename_Type(OctetString):
    """Custom type pgModemXferSourceFilename based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PgModemXferSourceFilename_Type.__name__ = "OctetString"
_PgModemXferSourceFilename_Object = MibTableColumn
pgModemXferSourceFilename = _PgModemXferSourceFilename_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 5, 1, 5, 1, 2),
    _PgModemXferSourceFilename_Type()
)
pgModemXferSourceFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgModemXferSourceFilename.setStatus("mandatory")


class _PgModemXferDestinationFilename_Type(OctetString):
    """Custom type pgModemXferDestinationFilename based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PgModemXferDestinationFilename_Type.__name__ = "OctetString"
_PgModemXferDestinationFilename_Object = MibTableColumn
pgModemXferDestinationFilename = _PgModemXferDestinationFilename_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 5, 1, 5, 1, 3),
    _PgModemXferDestinationFilename_Type()
)
pgModemXferDestinationFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgModemXferDestinationFilename.setStatus("optional")


class _PgModemXferAction_Type(Integer32):
    """Custom type pgModemXferAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abort", 1),
          ("download", 2))
    )


_PgModemXferAction_Type.__name__ = "Integer32"
_PgModemXferAction_Object = MibTableColumn
pgModemXferAction = _PgModemXferAction_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 5, 1, 5, 1, 4),
    _PgModemXferAction_Type()
)
pgModemXferAction.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    pgModemXferAction.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DSLAM-FLASH-MIB",
    **{"pgDSLAMFlashMIB": pgDSLAMFlashMIB,
       "pgDSLAMFlashObjects": pgDSLAMFlashObjects,
       "pgDSLAMFlashOperStatus": pgDSLAMFlashOperStatus,
       "pgDSLAMFlashDownLoad": pgDSLAMFlashDownLoad,
       "pgDSLAMFlashUpLoad": pgDSLAMFlashUpLoad,
       "pgDSLAMFlashCopyFile": pgDSLAMFlashCopyFile,
       "pgModemXferTable": pgModemXferTable,
       "pgModemXferEntry": pgModemXferEntry,
       "pgModemXferOperStatus": pgModemXferOperStatus,
       "pgModemXferSourceFilename": pgModemXferSourceFilename,
       "pgModemXferDestinationFilename": pgModemXferDestinationFilename,
       "pgModemXferAction": pgModemXferAction}
)
