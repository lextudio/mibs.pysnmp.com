# SNMP MIB module (WWP-LEOS-EXT-LAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-EXT-LAG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:51 2024
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

(wwpModulesLeos,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosExtLagMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 14)
)
wwpLeosExtLagMIB.setRevisions(
        ("2003-01-15 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpLeosExtLagMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosExtLagMIBObjects = _WwpLeosExtLagMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1)
)
_WwpLeosExtLag_ObjectIdentity = ObjectIdentity
wwpLeosExtLag = _WwpLeosExtLag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1)
)
_WwpLeosMaxLags_Type = Unsigned32
_WwpLeosMaxLags_Object = MibScalar
wwpLeosMaxLags = _WwpLeosMaxLags_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 1),
    _WwpLeosMaxLags_Type()
)
wwpLeosMaxLags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMaxLags.setStatus("current")
_WwpLeosNumLags_Type = Unsigned32
_WwpLeosNumLags_Object = MibScalar
wwpLeosNumLags = _WwpLeosNumLags_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 2),
    _WwpLeosNumLags_Type()
)
wwpLeosNumLags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosNumLags.setStatus("current")
_WwpLeosExtLagTable_Object = MibTable
wwpLeosExtLagTable = _WwpLeosExtLagTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 3)
)
if mibBuilder.loadTexts:
    wwpLeosExtLagTable.setStatus("current")
_WwpLeosExtLagEntry_Object = MibTableRow
wwpLeosExtLagEntry = _WwpLeosExtLagEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 3, 1)
)
wwpLeosExtLagEntry.setIndexNames(
    (0, "WWP-LEOS-EXT-LAG-MIB", "wwpLeosExtAggId"),
)
if mibBuilder.loadTexts:
    wwpLeosExtLagEntry.setStatus("current")


class _WwpLeosExtAggId_Type(Integer32):
    """Custom type wwpLeosExtAggId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WwpLeosExtAggId_Type.__name__ = "Integer32"
_WwpLeosExtAggId_Object = MibTableColumn
wwpLeosExtAggId = _WwpLeosExtAggId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 3, 1, 1),
    _WwpLeosExtAggId_Type()
)
wwpLeosExtAggId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosExtAggId.setStatus("current")


class _WwpLeosExtAggName_Type(DisplayString):
    """Custom type wwpLeosExtAggName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WwpLeosExtAggName_Type.__name__ = "DisplayString"
_WwpLeosExtAggName_Object = MibTableColumn
wwpLeosExtAggName = _WwpLeosExtAggName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 3, 1, 2),
    _WwpLeosExtAggName_Type()
)
wwpLeosExtAggName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosExtAggName.setStatus("current")


class _WwpLeosExtAggIndex_Type(Integer32):
    """Custom type wwpLeosExtAggIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WwpLeosExtAggIndex_Type.__name__ = "Integer32"
_WwpLeosExtAggIndex_Object = MibTableColumn
wwpLeosExtAggIndex = _WwpLeosExtAggIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 3, 1, 3),
    _WwpLeosExtAggIndex_Type()
)
wwpLeosExtAggIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosExtAggIndex.setStatus("current")
_WwpLeosExtAggStatus_Type = RowStatus
_WwpLeosExtAggStatus_Object = MibTableColumn
wwpLeosExtAggStatus = _WwpLeosExtAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 3, 1, 4),
    _WwpLeosExtAggStatus_Type()
)
wwpLeosExtAggStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosExtAggStatus.setStatus("current")


class _WwpLeosExtAggMode_Type(Integer32):
    """Custom type wwpLeosExtAggMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lacp", 1),
          ("manual", 2))
    )


_WwpLeosExtAggMode_Type.__name__ = "Integer32"
_WwpLeosExtAggMode_Object = MibTableColumn
wwpLeosExtAggMode = _WwpLeosExtAggMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 3, 1, 5),
    _WwpLeosExtAggMode_Type()
)
wwpLeosExtAggMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosExtAggMode.setStatus("current")


class _WwpLeosExtLagProtectionRevertState_Type(Integer32):
    """Custom type wwpLeosExtLagProtectionRevertState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WwpLeosExtLagProtectionRevertState_Type.__name__ = "Integer32"
_WwpLeosExtLagProtectionRevertState_Object = MibTableColumn
wwpLeosExtLagProtectionRevertState = _WwpLeosExtLagProtectionRevertState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 3, 1, 6),
    _WwpLeosExtLagProtectionRevertState_Type()
)
wwpLeosExtLagProtectionRevertState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosExtLagProtectionRevertState.setStatus("current")


class _WwpLeosExtLagProtectionRevertTimer_Type(Integer32):
    """Custom type wwpLeosExtLagProtectionRevertTimer based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_WwpLeosExtLagProtectionRevertTimer_Type.__name__ = "Integer32"
_WwpLeosExtLagProtectionRevertTimer_Object = MibTableColumn
wwpLeosExtLagProtectionRevertTimer = _WwpLeosExtLagProtectionRevertTimer_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 3, 1, 7),
    _WwpLeosExtLagProtectionRevertTimer_Type()
)
wwpLeosExtLagProtectionRevertTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosExtLagProtectionRevertTimer.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosExtLagProtectionRevertTimer.setUnits("msec")


class _WwpLeosExtAggHashMode_Type(Integer32):
    """Custom type wwpLeosExtAggHashMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enhanced", 3),
          ("ip-based", 2),
          ("mac-based", 1))
    )


_WwpLeosExtAggHashMode_Type.__name__ = "Integer32"
_WwpLeosExtAggHashMode_Object = MibTableColumn
wwpLeosExtAggHashMode = _WwpLeosExtAggHashMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 3, 1, 8),
    _WwpLeosExtAggHashMode_Type()
)
wwpLeosExtAggHashMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosExtAggHashMode.setStatus("current")


class _WwpLeosExtLagProtectionMode_Type(Integer32):
    """Custom type wwpLeosExtLagProtectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("proprietary", 1),
          ("standard", 2))
    )


_WwpLeosExtLagProtectionMode_Type.__name__ = "Integer32"
_WwpLeosExtLagProtectionMode_Object = MibTableColumn
wwpLeosExtLagProtectionMode = _WwpLeosExtLagProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 3, 1, 9),
    _WwpLeosExtLagProtectionMode_Type()
)
wwpLeosExtLagProtectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosExtLagProtectionMode.setStatus("current")
_WwpLeosLagModeTable_Object = MibTable
wwpLeosLagModeTable = _WwpLeosLagModeTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 4)
)
if mibBuilder.loadTexts:
    wwpLeosLagModeTable.setStatus("current")
_WwpLeosLagModeEntry_Object = MibTableRow
wwpLeosLagModeEntry = _WwpLeosLagModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 4, 1)
)
wwpLeosLagModeEntry.setIndexNames(
    (0, "WWP-LEOS-EXT-LAG-MIB", "wwpLeosLagPhyPortId"),
)
if mibBuilder.loadTexts:
    wwpLeosLagModeEntry.setStatus("current")


class _WwpLeosLagPhyPortId_Type(Integer32):
    """Custom type wwpLeosLagPhyPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosLagPhyPortId_Type.__name__ = "Integer32"
_WwpLeosLagPhyPortId_Object = MibTableColumn
wwpLeosLagPhyPortId = _WwpLeosLagPhyPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 4, 1, 1),
    _WwpLeosLagPhyPortId_Type()
)
wwpLeosLagPhyPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLagPhyPortId.setStatus("current")


class _WwpLeosLagAdminMode_Type(Integer32):
    """Custom type wwpLeosLagAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lacp", 1),
          ("manual", 2))
    )


_WwpLeosLagAdminMode_Type.__name__ = "Integer32"
_WwpLeosLagAdminMode_Object = MibTableColumn
wwpLeosLagAdminMode = _WwpLeosLagAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 4, 1, 2),
    _WwpLeosLagAdminMode_Type()
)
wwpLeosLagAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosLagAdminMode.setStatus("current")


class _WwpLeosLagOperMode_Type(Integer32):
    """Custom type wwpLeosLagOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lacp", 1),
          ("manual", 2))
    )


_WwpLeosLagOperMode_Type.__name__ = "Integer32"
_WwpLeosLagOperMode_Object = MibTableColumn
wwpLeosLagOperMode = _WwpLeosLagOperMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 4, 1, 3),
    _WwpLeosLagOperMode_Type()
)
wwpLeosLagOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLagOperMode.setStatus("current")
_WwpLeosLagProtectionTable_Object = MibTable
wwpLeosLagProtectionTable = _WwpLeosLagProtectionTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 5)
)
if mibBuilder.loadTexts:
    wwpLeosLagProtectionTable.setStatus("current")
_WwpLeosLagProtectionEntry_Object = MibTableRow
wwpLeosLagProtectionEntry = _WwpLeosLagProtectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 5, 1)
)
wwpLeosLagProtectionEntry.setIndexNames(
    (0, "WWP-LEOS-EXT-LAG-MIB", "wwpLeosExtAggId"),
    (0, "WWP-LEOS-EXT-LAG-MIB", "wwpLeosLagProtectionPort"),
)
if mibBuilder.loadTexts:
    wwpLeosLagProtectionEntry.setStatus("current")


class _WwpLeosLagProtectionPort_Type(Integer32):
    """Custom type wwpLeosLagProtectionPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosLagProtectionPort_Type.__name__ = "Integer32"
_WwpLeosLagProtectionPort_Object = MibTableColumn
wwpLeosLagProtectionPort = _WwpLeosLagProtectionPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 5, 1, 1),
    _WwpLeosLagProtectionPort_Type()
)
wwpLeosLagProtectionPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosLagProtectionPort.setStatus("current")
_WwpLeosLagProtectionRowStatus_Type = RowStatus
_WwpLeosLagProtectionRowStatus_Object = MibTableColumn
wwpLeosLagProtectionRowStatus = _WwpLeosLagProtectionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 5, 1, 2),
    _WwpLeosLagProtectionRowStatus_Type()
)
wwpLeosLagProtectionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosLagProtectionRowStatus.setStatus("current")


class _WwpLeosExtAggFloodHashMode_Type(Integer32):
    """Custom type wwpLeosExtAggFloodHashMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enhanced", 2),
          ("simplified", 1))
    )


_WwpLeosExtAggFloodHashMode_Type.__name__ = "Integer32"
_WwpLeosExtAggFloodHashMode_Object = MibScalar
wwpLeosExtAggFloodHashMode = _WwpLeosExtAggFloodHashMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 6),
    _WwpLeosExtAggFloodHashMode_Type()
)
wwpLeosExtAggFloodHashMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosExtAggFloodHashMode.setStatus("current")
_WwpLeosExtLagMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpLeosExtLagMIBNotificationPrefix = _WwpLeosExtLagMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 2)
)
_WwpLeosExtLagMIBNotifications_ObjectIdentity = ObjectIdentity
wwpLeosExtLagMIBNotifications = _WwpLeosExtLagMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 2, 0)
)
_WwpLeosExtLagMIBConformance_ObjectIdentity = ObjectIdentity
wwpLeosExtLagMIBConformance = _WwpLeosExtLagMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 3)
)
_WwpLeosExtLagMIBCompliances_ObjectIdentity = ObjectIdentity
wwpLeosExtLagMIBCompliances = _WwpLeosExtLagMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 3, 1)
)
_WwpLeosExtLagMIBGroups_ObjectIdentity = ObjectIdentity
wwpLeosExtLagMIBGroups = _WwpLeosExtLagMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-EXT-LAG-MIB",
    **{"wwpLeosExtLagMIB": wwpLeosExtLagMIB,
       "wwpLeosExtLagMIBObjects": wwpLeosExtLagMIBObjects,
       "wwpLeosExtLag": wwpLeosExtLag,
       "wwpLeosMaxLags": wwpLeosMaxLags,
       "wwpLeosNumLags": wwpLeosNumLags,
       "wwpLeosExtLagTable": wwpLeosExtLagTable,
       "wwpLeosExtLagEntry": wwpLeosExtLagEntry,
       "wwpLeosExtAggId": wwpLeosExtAggId,
       "wwpLeosExtAggName": wwpLeosExtAggName,
       "wwpLeosExtAggIndex": wwpLeosExtAggIndex,
       "wwpLeosExtAggStatus": wwpLeosExtAggStatus,
       "wwpLeosExtAggMode": wwpLeosExtAggMode,
       "wwpLeosExtLagProtectionRevertState": wwpLeosExtLagProtectionRevertState,
       "wwpLeosExtLagProtectionRevertTimer": wwpLeosExtLagProtectionRevertTimer,
       "wwpLeosExtAggHashMode": wwpLeosExtAggHashMode,
       "wwpLeosExtLagProtectionMode": wwpLeosExtLagProtectionMode,
       "wwpLeosLagModeTable": wwpLeosLagModeTable,
       "wwpLeosLagModeEntry": wwpLeosLagModeEntry,
       "wwpLeosLagPhyPortId": wwpLeosLagPhyPortId,
       "wwpLeosLagAdminMode": wwpLeosLagAdminMode,
       "wwpLeosLagOperMode": wwpLeosLagOperMode,
       "wwpLeosLagProtectionTable": wwpLeosLagProtectionTable,
       "wwpLeosLagProtectionEntry": wwpLeosLagProtectionEntry,
       "wwpLeosLagProtectionPort": wwpLeosLagProtectionPort,
       "wwpLeosLagProtectionRowStatus": wwpLeosLagProtectionRowStatus,
       "wwpLeosExtAggFloodHashMode": wwpLeosExtAggFloodHashMode,
       "wwpLeosExtLagMIBNotificationPrefix": wwpLeosExtLagMIBNotificationPrefix,
       "wwpLeosExtLagMIBNotifications": wwpLeosExtLagMIBNotifications,
       "wwpLeosExtLagMIBConformance": wwpLeosExtLagMIBConformance,
       "wwpLeosExtLagMIBCompliances": wwpLeosExtLagMIBCompliances,
       "wwpLeosExtLagMIBGroups": wwpLeosExtLagMIBGroups}
)
