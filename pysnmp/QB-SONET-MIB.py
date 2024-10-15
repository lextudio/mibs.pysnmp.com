# SNMP MIB module (QB-SONET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/QB-SONET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:40:46 2024
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

(qbMibs,) = mibBuilder.importSymbols(
    "QUANTUMBRIDGE-REG",
    "qbMibs")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(sonetMediumEntry,) = mibBuilder.importSymbols(
    "SONET-MIB",
    "sonetMediumEntry")


# MODULE-IDENTITY

qbSonetMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class QbSonetType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("sdhVC11", 3),
          ("sdhVC12", 2),
          ("sonetM13", 4),
          ("sonetVT15", 1),
          ("unknown", 5))
    )



# MIB Managed Objects in the order of their OIDs

_QbSonetObjects_ObjectIdentity = ObjectIdentity
qbSonetObjects = _QbSonetObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 6, 1)
)


class _QbSonetAlarmMode_Type(Integer32):
    """Custom type qbSonetAlarmMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_QbSonetAlarmMode_Type.__name__ = "Integer32"
_QbSonetAlarmMode_Object = MibScalar
qbSonetAlarmMode = _QbSonetAlarmMode_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 6, 1, 1),
    _QbSonetAlarmMode_Type()
)
qbSonetAlarmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSonetAlarmMode.setStatus("current")


class _QbSonetScramblingMode_Type(Integer32):
    """Custom type qbSonetScramblingMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 3))
    )


_QbSonetScramblingMode_Type.__name__ = "Integer32"
_QbSonetScramblingMode_Object = MibScalar
qbSonetScramblingMode = _QbSonetScramblingMode_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 6, 1, 2),
    _QbSonetScramblingMode_Type()
)
qbSonetScramblingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSonetScramblingMode.setStatus("current")


class _QbSonetMediumType_Type(QbSonetType):
    """Custom type qbSonetMediumType based on QbSonetType"""


_QbSonetMediumType_Object = MibScalar
qbSonetMediumType = _QbSonetMediumType_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 6, 1, 3),
    _QbSonetMediumType_Type()
)
qbSonetMediumType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSonetMediumType.setStatus("current")


class _QbSonetSlot_Type(Integer32):
    """Custom type qbSonetSlot based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_QbSonetSlot_Type.__name__ = "Integer32"
_QbSonetSlot_Object = MibScalar
qbSonetSlot = _QbSonetSlot_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 6, 1, 4),
    _QbSonetSlot_Type()
)
qbSonetSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSonetSlot.setStatus("current")
_QbSonetTables_ObjectIdentity = ObjectIdentity
qbSonetTables = _QbSonetTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 6, 2)
)
_QbSonetMediumTable_Object = MibTable
qbSonetMediumTable = _QbSonetMediumTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 6, 2, 1)
)
if mibBuilder.loadTexts:
    qbSonetMediumTable.setStatus("current")
_QbSonetMediumEntry_Object = MibTableRow
qbSonetMediumEntry = _QbSonetMediumEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 6, 2, 1, 1)
)
if mibBuilder.loadTexts:
    qbSonetMediumEntry.setStatus("current")


class _QbSonetPortTxClockSource_Type(Integer32):
    """Custom type qbSonetPortTxClockSource based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("recovered", 2))
    )


_QbSonetPortTxClockSource_Type.__name__ = "Integer32"
_QbSonetPortTxClockSource_Object = MibTableColumn
qbSonetPortTxClockSource = _QbSonetPortTxClockSource_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 6, 2, 1, 1, 1),
    _QbSonetPortTxClockSource_Type()
)
qbSonetPortTxClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSonetPortTxClockSource.setStatus("deprecated")


class _QbSonetPortScramblingMode_Type(Integer32):
    """Custom type qbSonetPortScramblingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_QbSonetPortScramblingMode_Type.__name__ = "Integer32"
_QbSonetPortScramblingMode_Object = MibTableColumn
qbSonetPortScramblingMode = _QbSonetPortScramblingMode_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 6, 2, 1, 1, 2),
    _QbSonetPortScramblingMode_Type()
)
qbSonetPortScramblingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSonetPortScramblingMode.setStatus("current")


class _QbSonetPortAlarmMode_Type(Integer32):
    """Custom type qbSonetPortAlarmMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_QbSonetPortAlarmMode_Type.__name__ = "Integer32"
_QbSonetPortAlarmMode_Object = MibTableColumn
qbSonetPortAlarmMode = _QbSonetPortAlarmMode_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 6, 2, 1, 1, 3),
    _QbSonetPortAlarmMode_Type()
)
qbSonetPortAlarmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSonetPortAlarmMode.setStatus("current")


class _QbSonetPortMediumType_Type(QbSonetType):
    """Custom type qbSonetPortMediumType based on QbSonetType"""


_QbSonetPortMediumType_Object = MibTableColumn
qbSonetPortMediumType = _QbSonetPortMediumType_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 6, 2, 1, 1, 4),
    _QbSonetPortMediumType_Type()
)
qbSonetPortMediumType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSonetPortMediumType.setStatus("current")
_QbSonetStatTable_Object = MibTable
qbSonetStatTable = _QbSonetStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 6, 2, 2)
)
if mibBuilder.loadTexts:
    qbSonetStatTable.setStatus("current")
_QbSonetStatEntry_Object = MibTableRow
qbSonetStatEntry = _QbSonetStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 6, 2, 2, 1)
)
qbSonetStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    qbSonetStatEntry.setStatus("current")
_QbSonetSectionBIP_Type = Counter32
_QbSonetSectionBIP_Object = MibTableColumn
qbSonetSectionBIP = _QbSonetSectionBIP_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 6, 2, 2, 1, 1),
    _QbSonetSectionBIP_Type()
)
qbSonetSectionBIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSonetSectionBIP.setStatus("current")
_QbSonetLineBIP_Type = Counter32
_QbSonetLineBIP_Object = MibTableColumn
qbSonetLineBIP = _QbSonetLineBIP_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 6, 2, 2, 1, 2),
    _QbSonetLineBIP_Type()
)
qbSonetLineBIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSonetLineBIP.setStatus("current")
_QbSonetPathBIP_Type = Counter32
_QbSonetPathBIP_Object = MibTableColumn
qbSonetPathBIP = _QbSonetPathBIP_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 6, 2, 2, 1, 3),
    _QbSonetPathBIP_Type()
)
qbSonetPathBIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSonetPathBIP.setStatus("current")
_QbSonetConformance_ObjectIdentity = ObjectIdentity
qbSonetConformance = _QbSonetConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 6, 3)
)
_QbSonetCompliances_ObjectIdentity = ObjectIdentity
qbSonetCompliances = _QbSonetCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 6, 3, 1)
)
_QbSonetGroups_ObjectIdentity = ObjectIdentity
qbSonetGroups = _QbSonetGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 6, 3, 2)
)
sonetMediumEntry.registerAugmentions(
    ("QB-SONET-MIB",
     "qbSonetMediumEntry")
)
qbSonetMediumEntry.setIndexNames(*sonetMediumEntry.getIndexNames())

# Managed Objects groups

qbSonetAllGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 6, 3, 2, 1)
)
qbSonetAllGroup.setObjects(
      *(("QB-SONET-MIB", "qbSonetAlarmMode"),
        ("QB-SONET-MIB", "qbSonetScramblingMode"),
        ("QB-SONET-MIB", "qbSonetMediumType"),
        ("QB-SONET-MIB", "qbSonetSlot"),
        ("QB-SONET-MIB", "qbSonetPortTxClockSource"),
        ("QB-SONET-MIB", "qbSonetPortScramblingMode"),
        ("QB-SONET-MIB", "qbSonetPortAlarmMode"))
)
if mibBuilder.loadTexts:
    qbSonetAllGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qbSonetCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4323, 2, 6, 3, 1, 1)
)
if mibBuilder.loadTexts:
    qbSonetCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QB-SONET-MIB",
    **{"QbSonetType": QbSonetType,
       "qbSonetMIB": qbSonetMIB,
       "qbSonetObjects": qbSonetObjects,
       "qbSonetAlarmMode": qbSonetAlarmMode,
       "qbSonetScramblingMode": qbSonetScramblingMode,
       "qbSonetMediumType": qbSonetMediumType,
       "qbSonetSlot": qbSonetSlot,
       "qbSonetTables": qbSonetTables,
       "qbSonetMediumTable": qbSonetMediumTable,
       "qbSonetMediumEntry": qbSonetMediumEntry,
       "qbSonetPortTxClockSource": qbSonetPortTxClockSource,
       "qbSonetPortScramblingMode": qbSonetPortScramblingMode,
       "qbSonetPortAlarmMode": qbSonetPortAlarmMode,
       "qbSonetPortMediumType": qbSonetPortMediumType,
       "qbSonetStatTable": qbSonetStatTable,
       "qbSonetStatEntry": qbSonetStatEntry,
       "qbSonetSectionBIP": qbSonetSectionBIP,
       "qbSonetLineBIP": qbSonetLineBIP,
       "qbSonetPathBIP": qbSonetPathBIP,
       "qbSonetConformance": qbSonetConformance,
       "qbSonetCompliances": qbSonetCompliances,
       "qbSonetCompliance": qbSonetCompliance,
       "qbSonetGroups": qbSonetGroups,
       "qbSonetAllGroup": qbSonetAllGroup}
)
