# SNMP MIB module (ALCATEL-IND1-CONFIG-MGR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-CONFIG-MGR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:46 2024
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

(softentIND1Confmgr,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1Confmgr")

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


# MODULE-IDENTITY

alcatelIND1ConfigMgrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1)
)
alcatelIND1ConfigMgrMIB.setRevisions(
        ("2007-04-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1ConfigMgrMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1ConfigMgrMIBObjects = _AlcatelIND1ConfigMgrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1ConfigMgrMIBObjects.setStatus("current")
_ConfigManager_ObjectIdentity = ObjectIdentity
configManager = _ConfigManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1)
)


class _ConfigFileName_Type(DisplayString):
    """Custom type configFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_ConfigFileName_Type.__name__ = "DisplayString"
_ConfigFileName_Object = MibScalar
configFileName = _ConfigFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 1),
    _ConfigFileName_Type()
)
configFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFileName.setStatus("current")


class _ConfigFileAction_Type(Integer32):
    """Custom type configFileAction based on Integer32"""
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
        *(("apply", 3),
          ("checkSyntaxOnly", 2),
          ("none", 1))
    )


_ConfigFileAction_Type.__name__ = "Integer32"
_ConfigFileAction_Object = MibScalar
configFileAction = _ConfigFileAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 2),
    _ConfigFileAction_Type()
)
configFileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFileAction.setStatus("current")


class _ConfigErrorFileName_Type(DisplayString):
    """Custom type configErrorFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ConfigErrorFileName_Type.__name__ = "DisplayString"
_ConfigErrorFileName_Object = MibScalar
configErrorFileName = _ConfigErrorFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 3),
    _ConfigErrorFileName_Type()
)
configErrorFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configErrorFileName.setStatus("current")


class _ConfigFileStatus_Type(Integer32):
    """Custom type configFileStatus based on Integer32"""
    defaultValue = 1

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
        *(("completeErrors", 4),
          ("completeNoErrors", 3),
          ("inProgress", 2),
          ("noneAvail", 1))
    )


_ConfigFileStatus_Type.__name__ = "Integer32"
_ConfigFileStatus_Object = MibScalar
configFileStatus = _ConfigFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 4),
    _ConfigFileStatus_Type()
)
configFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configFileStatus.setStatus("current")


class _ConfigFileMode_Type(Integer32):
    """Custom type configFileMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("verbose", 2))
    )


_ConfigFileMode_Type.__name__ = "Integer32"
_ConfigFileMode_Object = MibScalar
configFileMode = _ConfigFileMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 5),
    _ConfigFileMode_Type()
)
configFileMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFileMode.setStatus("current")


class _ConfigTimerFileName_Type(DisplayString):
    """Custom type configTimerFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_ConfigTimerFileName_Type.__name__ = "DisplayString"
_ConfigTimerFileName_Object = MibScalar
configTimerFileName = _ConfigTimerFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 6),
    _ConfigTimerFileName_Type()
)
configTimerFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configTimerFileName.setStatus("current")


class _ConfigTimerFileTime_Type(DisplayString):
    """Custom type configTimerFileTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ConfigTimerFileTime_Type.__name__ = "DisplayString"
_ConfigTimerFileTime_Object = MibScalar
configTimerFileTime = _ConfigTimerFileTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 7),
    _ConfigTimerFileTime_Type()
)
configTimerFileTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configTimerFileTime.setStatus("current")


class _ConfigTimerFileStatus_Type(Integer32):
    """Custom type configTimerFileStatus based on Integer32"""
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
        *(("idle", 1),
          ("inProgress", 3),
          ("pending", 2))
    )


_ConfigTimerFileStatus_Type.__name__ = "Integer32"
_ConfigTimerFileStatus_Object = MibScalar
configTimerFileStatus = _ConfigTimerFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 8),
    _ConfigTimerFileStatus_Type()
)
configTimerFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configTimerFileStatus.setStatus("current")


class _ConfigTimerClear_Type(Integer32):
    """Custom type configTimerClear based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_ConfigTimerClear_Type.__name__ = "Integer32"
_ConfigTimerClear_Object = MibScalar
configTimerClear = _ConfigTimerClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 9),
    _ConfigTimerClear_Type()
)
configTimerClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configTimerClear.setStatus("current")


class _ConfigSnapshotFileName_Type(DisplayString):
    """Custom type configSnapshotFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_ConfigSnapshotFileName_Type.__name__ = "DisplayString"
_ConfigSnapshotFileName_Object = MibScalar
configSnapshotFileName = _ConfigSnapshotFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 10),
    _ConfigSnapshotFileName_Type()
)
configSnapshotFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotFileName.setStatus("current")


class _ConfigSnapshotAction_Type(Integer32):
    """Custom type configSnapshotAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_ConfigSnapshotAction_Type.__name__ = "Integer32"
_ConfigSnapshotAction_Object = MibScalar
configSnapshotAction = _ConfigSnapshotAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 11),
    _ConfigSnapshotAction_Type()
)
configSnapshotAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotAction.setStatus("current")


class _ConfigSnapshotAllSelect_Type(Integer32):
    """Custom type configSnapshotAllSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotAllSelect_Type.__name__ = "Integer32"
_ConfigSnapshotAllSelect_Object = MibScalar
configSnapshotAllSelect = _ConfigSnapshotAllSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 12),
    _ConfigSnapshotAllSelect_Type()
)
configSnapshotAllSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotAllSelect.setStatus("current")


class _ConfigSnapshotVlanSelect_Type(Integer32):
    """Custom type configSnapshotVlanSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotVlanSelect_Type.__name__ = "Integer32"
_ConfigSnapshotVlanSelect_Object = MibScalar
configSnapshotVlanSelect = _ConfigSnapshotVlanSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 13),
    _ConfigSnapshotVlanSelect_Type()
)
configSnapshotVlanSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotVlanSelect.setStatus("current")


class _ConfigSnapshotSpanningTreeSelect_Type(Integer32):
    """Custom type configSnapshotSpanningTreeSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotSpanningTreeSelect_Type.__name__ = "Integer32"
_ConfigSnapshotSpanningTreeSelect_Object = MibScalar
configSnapshotSpanningTreeSelect = _ConfigSnapshotSpanningTreeSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 14),
    _ConfigSnapshotSpanningTreeSelect_Type()
)
configSnapshotSpanningTreeSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotSpanningTreeSelect.setStatus("current")


class _ConfigSnapshotQOSSelect_Type(Integer32):
    """Custom type configSnapshotQOSSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotQOSSelect_Type.__name__ = "Integer32"
_ConfigSnapshotQOSSelect_Object = MibScalar
configSnapshotQOSSelect = _ConfigSnapshotQOSSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 15),
    _ConfigSnapshotQOSSelect_Type()
)
configSnapshotQOSSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotQOSSelect.setStatus("current")


class _ConfigSnapshotIPSelect_Type(Integer32):
    """Custom type configSnapshotIPSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotIPSelect_Type.__name__ = "Integer32"
_ConfigSnapshotIPSelect_Object = MibScalar
configSnapshotIPSelect = _ConfigSnapshotIPSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 16),
    _ConfigSnapshotIPSelect_Type()
)
configSnapshotIPSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotIPSelect.setStatus("current")


class _ConfigSnapshotIPXSelect_Type(Integer32):
    """Custom type configSnapshotIPXSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotIPXSelect_Type.__name__ = "Integer32"
_ConfigSnapshotIPXSelect_Object = MibScalar
configSnapshotIPXSelect = _ConfigSnapshotIPXSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 17),
    _ConfigSnapshotIPXSelect_Type()
)
configSnapshotIPXSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotIPXSelect.setStatus("current")


class _ConfigSnapshotIPMSSelect_Type(Integer32):
    """Custom type configSnapshotIPMSSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotIPMSSelect_Type.__name__ = "Integer32"
_ConfigSnapshotIPMSSelect_Object = MibScalar
configSnapshotIPMSSelect = _ConfigSnapshotIPMSSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 18),
    _ConfigSnapshotIPMSSelect_Type()
)
configSnapshotIPMSSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotIPMSSelect.setStatus("current")


class _ConfigSnapshotAAASelect_Type(Integer32):
    """Custom type configSnapshotAAASelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotAAASelect_Type.__name__ = "Integer32"
_ConfigSnapshotAAASelect_Object = MibScalar
configSnapshotAAASelect = _ConfigSnapshotAAASelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 19),
    _ConfigSnapshotAAASelect_Type()
)
configSnapshotAAASelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotAAASelect.setStatus("current")


class _ConfigSnapshotSNMPSelect_Type(Integer32):
    """Custom type configSnapshotSNMPSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotSNMPSelect_Type.__name__ = "Integer32"
_ConfigSnapshotSNMPSelect_Object = MibScalar
configSnapshotSNMPSelect = _ConfigSnapshotSNMPSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 20),
    _ConfigSnapshotSNMPSelect_Type()
)
configSnapshotSNMPSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotSNMPSelect.setStatus("current")


class _ConfigSnapshot8021QSelect_Type(Integer32):
    """Custom type configSnapshot8021QSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshot8021QSelect_Type.__name__ = "Integer32"
_ConfigSnapshot8021QSelect_Object = MibScalar
configSnapshot8021QSelect = _ConfigSnapshot8021QSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 21),
    _ConfigSnapshot8021QSelect_Type()
)
configSnapshot8021QSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshot8021QSelect.setStatus("current")


class _ConfigSnapshotLinkAggregateSelect_Type(Integer32):
    """Custom type configSnapshotLinkAggregateSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotLinkAggregateSelect_Type.__name__ = "Integer32"
_ConfigSnapshotLinkAggregateSelect_Object = MibScalar
configSnapshotLinkAggregateSelect = _ConfigSnapshotLinkAggregateSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 22),
    _ConfigSnapshotLinkAggregateSelect_Type()
)
configSnapshotLinkAggregateSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotLinkAggregateSelect.setStatus("current")


class _ConfigSnapshotPortMirrorSelect_Type(Integer32):
    """Custom type configSnapshotPortMirrorSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotPortMirrorSelect_Type.__name__ = "Integer32"
_ConfigSnapshotPortMirrorSelect_Object = MibScalar
configSnapshotPortMirrorSelect = _ConfigSnapshotPortMirrorSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 23),
    _ConfigSnapshotPortMirrorSelect_Type()
)
configSnapshotPortMirrorSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotPortMirrorSelect.setStatus("current")


class _ConfigSnapshotXIPSelect_Type(Integer32):
    """Custom type configSnapshotXIPSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotXIPSelect_Type.__name__ = "Integer32"
_ConfigSnapshotXIPSelect_Object = MibScalar
configSnapshotXIPSelect = _ConfigSnapshotXIPSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 24),
    _ConfigSnapshotXIPSelect_Type()
)
configSnapshotXIPSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotXIPSelect.setStatus("current")


class _ConfigSnapshotHealthMonitorSelect_Type(Integer32):
    """Custom type configSnapshotHealthMonitorSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotHealthMonitorSelect_Type.__name__ = "Integer32"
_ConfigSnapshotHealthMonitorSelect_Object = MibScalar
configSnapshotHealthMonitorSelect = _ConfigSnapshotHealthMonitorSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 25),
    _ConfigSnapshotHealthMonitorSelect_Type()
)
configSnapshotHealthMonitorSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotHealthMonitorSelect.setStatus("current")


class _ConfigSnapshotBootPSelect_Type(Integer32):
    """Custom type configSnapshotBootPSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotBootPSelect_Type.__name__ = "Integer32"
_ConfigSnapshotBootPSelect_Object = MibScalar
configSnapshotBootPSelect = _ConfigSnapshotBootPSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 26),
    _ConfigSnapshotBootPSelect_Type()
)
configSnapshotBootPSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotBootPSelect.setStatus("current")


class _ConfigSnapshotBridgeSelect_Type(Integer32):
    """Custom type configSnapshotBridgeSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotBridgeSelect_Type.__name__ = "Integer32"
_ConfigSnapshotBridgeSelect_Object = MibScalar
configSnapshotBridgeSelect = _ConfigSnapshotBridgeSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 27),
    _ConfigSnapshotBridgeSelect_Type()
)
configSnapshotBridgeSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotBridgeSelect.setStatus("current")


class _ConfigSnapshotChassisSelect_Type(Integer32):
    """Custom type configSnapshotChassisSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotChassisSelect_Type.__name__ = "Integer32"
_ConfigSnapshotChassisSelect_Object = MibScalar
configSnapshotChassisSelect = _ConfigSnapshotChassisSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 28),
    _ConfigSnapshotChassisSelect_Type()
)
configSnapshotChassisSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotChassisSelect.setStatus("current")


class _ConfigSnapshotInterfaceSelect_Type(Integer32):
    """Custom type configSnapshotInterfaceSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotInterfaceSelect_Type.__name__ = "Integer32"
_ConfigSnapshotInterfaceSelect_Object = MibScalar
configSnapshotInterfaceSelect = _ConfigSnapshotInterfaceSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 29),
    _ConfigSnapshotInterfaceSelect_Type()
)
configSnapshotInterfaceSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotInterfaceSelect.setStatus("current")


class _ConfigSnapshotPolicySelect_Type(Integer32):
    """Custom type configSnapshotPolicySelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotPolicySelect_Type.__name__ = "Integer32"
_ConfigSnapshotPolicySelect_Object = MibScalar
configSnapshotPolicySelect = _ConfigSnapshotPolicySelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 30),
    _ConfigSnapshotPolicySelect_Type()
)
configSnapshotPolicySelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotPolicySelect.setStatus("current")


class _ConfigSnapshotSessionSelect_Type(Integer32):
    """Custom type configSnapshotSessionSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotSessionSelect_Type.__name__ = "Integer32"
_ConfigSnapshotSessionSelect_Object = MibScalar
configSnapshotSessionSelect = _ConfigSnapshotSessionSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 31),
    _ConfigSnapshotSessionSelect_Type()
)
configSnapshotSessionSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotSessionSelect.setStatus("current")


class _ConfigSnapshotServerLoadBalanceSelect_Type(Integer32):
    """Custom type configSnapshotServerLoadBalanceSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotServerLoadBalanceSelect_Type.__name__ = "Integer32"
_ConfigSnapshotServerLoadBalanceSelect_Object = MibScalar
configSnapshotServerLoadBalanceSelect = _ConfigSnapshotServerLoadBalanceSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 32),
    _ConfigSnapshotServerLoadBalanceSelect_Type()
)
configSnapshotServerLoadBalanceSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotServerLoadBalanceSelect.setStatus("current")


class _ConfigSnapshotSystemServiceSelect_Type(Integer32):
    """Custom type configSnapshotSystemServiceSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotSystemServiceSelect_Type.__name__ = "Integer32"
_ConfigSnapshotSystemServiceSelect_Object = MibScalar
configSnapshotSystemServiceSelect = _ConfigSnapshotSystemServiceSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 33),
    _ConfigSnapshotSystemServiceSelect_Type()
)
configSnapshotSystemServiceSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotSystemServiceSelect.setStatus("current")


class _ConfigSnapshotVRRPSelect_Type(Integer32):
    """Custom type configSnapshotVRRPSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotVRRPSelect_Type.__name__ = "Integer32"
_ConfigSnapshotVRRPSelect_Object = MibScalar
configSnapshotVRRPSelect = _ConfigSnapshotVRRPSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 34),
    _ConfigSnapshotVRRPSelect_Type()
)
configSnapshotVRRPSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotVRRPSelect.setStatus("current")


class _ConfigSnapshotWebSelect_Type(Integer32):
    """Custom type configSnapshotWebSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotWebSelect_Type.__name__ = "Integer32"
_ConfigSnapshotWebSelect_Object = MibScalar
configSnapshotWebSelect = _ConfigSnapshotWebSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 35),
    _ConfigSnapshotWebSelect_Type()
)
configSnapshotWebSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotWebSelect.setStatus("current")


class _ConfigSnapshotRIPSelect_Type(Integer32):
    """Custom type configSnapshotRIPSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotRIPSelect_Type.__name__ = "Integer32"
_ConfigSnapshotRIPSelect_Object = MibScalar
configSnapshotRIPSelect = _ConfigSnapshotRIPSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 36),
    _ConfigSnapshotRIPSelect_Type()
)
configSnapshotRIPSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotRIPSelect.setStatus("current")


class _ConfigSnapshotOSPFSelect_Type(Integer32):
    """Custom type configSnapshotOSPFSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotOSPFSelect_Type.__name__ = "Integer32"
_ConfigSnapshotOSPFSelect_Object = MibScalar
configSnapshotOSPFSelect = _ConfigSnapshotOSPFSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 37),
    _ConfigSnapshotOSPFSelect_Type()
)
configSnapshotOSPFSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotOSPFSelect.setStatus("current")


class _ConfigSnapshotBGPSelect_Type(Integer32):
    """Custom type configSnapshotBGPSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotBGPSelect_Type.__name__ = "Integer32"
_ConfigSnapshotBGPSelect_Object = MibScalar
configSnapshotBGPSelect = _ConfigSnapshotBGPSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 38),
    _ConfigSnapshotBGPSelect_Type()
)
configSnapshotBGPSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotBGPSelect.setStatus("current")


class _ConfigSnapshotIPRMSelect_Type(Integer32):
    """Custom type configSnapshotIPRMSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotIPRMSelect_Type.__name__ = "Integer32"
_ConfigSnapshotIPRMSelect_Object = MibScalar
configSnapshotIPRMSelect = _ConfigSnapshotIPRMSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 39),
    _ConfigSnapshotIPRMSelect_Type()
)
configSnapshotIPRMSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotIPRMSelect.setStatus("current")


class _ConfigSnapshotIPMRSelect_Type(Integer32):
    """Custom type configSnapshotIPMRSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotIPMRSelect_Type.__name__ = "Integer32"
_ConfigSnapshotIPMRSelect_Object = MibScalar
configSnapshotIPMRSelect = _ConfigSnapshotIPMRSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 40),
    _ConfigSnapshotIPMRSelect_Type()
)
configSnapshotIPMRSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotIPMRSelect.setStatus("current")


class _ConfigSnapshotModuleSelect_Type(Integer32):
    """Custom type configSnapshotModuleSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotModuleSelect_Type.__name__ = "Integer32"
_ConfigSnapshotModuleSelect_Object = MibScalar
configSnapshotModuleSelect = _ConfigSnapshotModuleSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 41),
    _ConfigSnapshotModuleSelect_Type()
)
configSnapshotModuleSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotModuleSelect.setStatus("current")


class _ConfigTechSupportLogAction_Type(Integer32):
    """Custom type configTechSupportLogAction based on Integer32"""
    defaultValue = 1

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
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("notSiginificant", 0),
          ("techSupportBasic", 1),
          ("techSupportL2", 2),
          ("techSupportL3", 3),
          ("techSupportL3Bfd", 17),
          ("techSupportL3Bgp", 7),
          ("techSupportL3Dvmrp", 10),
          ("techSupportL3IPsec", 16),
          ("techSupportL3IPv6", 11),
          ("techSupportL3Ipx", 5),
          ("techSupportL3Isis", 14),
          ("techSupportL3Mroute", 9),
          ("techSupportL3OSPF3", 13),
          ("techSupportL3Ospf", 6),
          ("techSupportL3Pim6", 15),
          ("techSupportL3Pimsm", 8),
          ("techSupportL3RIPng", 12),
          ("techSupportL3Rip", 4))
    )


_ConfigTechSupportLogAction_Type.__name__ = "Integer32"
_ConfigTechSupportLogAction_Object = MibScalar
configTechSupportLogAction = _ConfigTechSupportLogAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 42),
    _ConfigTechSupportLogAction_Type()
)
configTechSupportLogAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configTechSupportLogAction.setStatus("current")


class _ConfigWriteMemory_Type(Integer32):
    """Custom type configWriteMemory based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigWriteMemory_Type.__name__ = "Integer32"
_ConfigWriteMemory_Object = MibScalar
configWriteMemory = _ConfigWriteMemory_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 43),
    _ConfigWriteMemory_Type()
)
configWriteMemory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configWriteMemory.setStatus("current")


class _ConfigErrorFileMaximum_Type(Integer32):
    """Custom type configErrorFileMaximum based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_ConfigErrorFileMaximum_Type.__name__ = "Integer32"
_ConfigErrorFileMaximum_Object = MibScalar
configErrorFileMaximum = _ConfigErrorFileMaximum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 44),
    _ConfigErrorFileMaximum_Type()
)
configErrorFileMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configErrorFileMaximum.setStatus("current")


class _ConfigChangeStatus_Type(Integer32):
    """Custom type configChangeStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("different", 2),
          ("identical", 1))
    )


_ConfigChangeStatus_Type.__name__ = "Integer32"
_ConfigChangeStatus_Object = MibScalar
configChangeStatus = _ConfigChangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 45),
    _ConfigChangeStatus_Type()
)
configChangeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configChangeStatus.setStatus("current")


class _ConfigSnapshotRDPSelect_Type(Integer32):
    """Custom type configSnapshotRDPSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotRDPSelect_Type.__name__ = "Integer32"
_ConfigSnapshotRDPSelect_Object = MibScalar
configSnapshotRDPSelect = _ConfigSnapshotRDPSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 46),
    _ConfigSnapshotRDPSelect_Type()
)
configSnapshotRDPSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotRDPSelect.setStatus("current")


class _ConfigSnapshotIPv6Select_Type(Integer32):
    """Custom type configSnapshotIPv6Select based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotIPv6Select_Type.__name__ = "Integer32"
_ConfigSnapshotIPv6Select_Object = MibScalar
configSnapshotIPv6Select = _ConfigSnapshotIPv6Select_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 47),
    _ConfigSnapshotIPv6Select_Type()
)
configSnapshotIPv6Select.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotIPv6Select.setStatus("current")


class _ConfigSnapshotRIPngSelect_Type(Integer32):
    """Custom type configSnapshotRIPngSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotRIPngSelect_Type.__name__ = "Integer32"
_ConfigSnapshotRIPngSelect_Object = MibScalar
configSnapshotRIPngSelect = _ConfigSnapshotRIPngSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 48),
    _ConfigSnapshotRIPngSelect_Type()
)
configSnapshotRIPngSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotRIPngSelect.setStatus("current")


class _ConfigSnapshotAtmSelect_Type(Integer32):
    """Custom type configSnapshotAtmSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotAtmSelect_Type.__name__ = "Integer32"
_ConfigSnapshotAtmSelect_Object = MibScalar
configSnapshotAtmSelect = _ConfigSnapshotAtmSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 49),
    _ConfigSnapshotAtmSelect_Type()
)
configSnapshotAtmSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotAtmSelect.setStatus("current")


class _ConfigSnapshotSonetSelect_Type(Integer32):
    """Custom type configSnapshotSonetSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotSonetSelect_Type.__name__ = "Integer32"
_ConfigSnapshotSonetSelect_Object = MibScalar
configSnapshotSonetSelect = _ConfigSnapshotSonetSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 50),
    _ConfigSnapshotSonetSelect_Type()
)
configSnapshotSonetSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotSonetSelect.setStatus("current")


class _ConfigSnapshotNTPSelect_Type(Integer32):
    """Custom type configSnapshotNTPSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotNTPSelect_Type.__name__ = "Integer32"
_ConfigSnapshotNTPSelect_Object = MibScalar
configSnapshotNTPSelect = _ConfigSnapshotNTPSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 51),
    _ConfigSnapshotNTPSelect_Type()
)
configSnapshotNTPSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotNTPSelect.setStatus("current")


class _ConfigSnapshotPortMappingSelect_Type(Integer32):
    """Custom type configSnapshotPortMappingSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotPortMappingSelect_Type.__name__ = "Integer32"
_ConfigSnapshotPortMappingSelect_Object = MibScalar
configSnapshotPortMappingSelect = _ConfigSnapshotPortMappingSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 52),
    _ConfigSnapshotPortMappingSelect_Type()
)
configSnapshotPortMappingSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotPortMappingSelect.setStatus("current")


class _ConfigSnapshotOSPF3Select_Type(Integer32):
    """Custom type configSnapshotOSPF3Select based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotOSPF3Select_Type.__name__ = "Integer32"
_ConfigSnapshotOSPF3Select_Object = MibScalar
configSnapshotOSPF3Select = _ConfigSnapshotOSPF3Select_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 53),
    _ConfigSnapshotOSPF3Select_Type()
)
configSnapshotOSPF3Select.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotOSPF3Select.setStatus("current")


class _ConfigWriteMemoryStatus_Type(Integer32):
    """Custom type configWriteMemoryStatus based on Integer32"""
    defaultValue = 1

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
        *(("completeErrors", 4),
          ("completeNoErrors", 3),
          ("inProgress", 2),
          ("noneAvail", 1))
    )


_ConfigWriteMemoryStatus_Type.__name__ = "Integer32"
_ConfigWriteMemoryStatus_Object = MibScalar
configWriteMemoryStatus = _ConfigWriteMemoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 54),
    _ConfigWriteMemoryStatus_Type()
)
configWriteMemoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configWriteMemoryStatus.setStatus("current")


class _ConfigSnapshotStackSelect_Type(Integer32):
    """Custom type configSnapshotStackSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotStackSelect_Type.__name__ = "Integer32"
_ConfigSnapshotStackSelect_Object = MibScalar
configSnapshotStackSelect = _ConfigSnapshotStackSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 55),
    _ConfigSnapshotStackSelect_Type()
)
configSnapshotStackSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotStackSelect.setStatus("current")


class _ConfigSnapshotISISSelect_Type(Integer32):
    """Custom type configSnapshotISISSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotISISSelect_Type.__name__ = "Integer32"
_ConfigSnapshotISISSelect_Object = MibScalar
configSnapshotISISSelect = _ConfigSnapshotISISSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 56),
    _ConfigSnapshotISISSelect_Type()
)
configSnapshotISISSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotISISSelect.setStatus("current")


class _ConfigSnapshotEOAMSelect_Type(Integer32):
    """Custom type configSnapshotEOAMSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotEOAMSelect_Type.__name__ = "Integer32"
_ConfigSnapshotEOAMSelect_Object = MibScalar
configSnapshotEOAMSelect = _ConfigSnapshotEOAMSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 57),
    _ConfigSnapshotEOAMSelect_Type()
)
configSnapshotEOAMSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotEOAMSelect.setStatus("current")


class _ConfigSnapshotUDLDSelect_Type(Integer32):
    """Custom type configSnapshotUDLDSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotUDLDSelect_Type.__name__ = "Integer32"
_ConfigSnapshotUDLDSelect_Object = MibScalar
configSnapshotUDLDSelect = _ConfigSnapshotUDLDSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 58),
    _ConfigSnapshotUDLDSelect_Type()
)
configSnapshotUDLDSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotUDLDSelect.setStatus("current")


class _ConfigSnapshotNETSECSelect_Type(Integer32):
    """Custom type configSnapshotNETSECSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotNETSECSelect_Type.__name__ = "Integer32"
_ConfigSnapshotNETSECSelect_Object = MibScalar
configSnapshotNETSECSelect = _ConfigSnapshotNETSECSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 59),
    _ConfigSnapshotNETSECSelect_Type()
)
configSnapshotNETSECSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotNETSECSelect.setStatus("current")


class _ConfigSnapshotIPsecSelect_Type(Integer32):
    """Custom type configSnapshotIPsecSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotIPsecSelect_Type.__name__ = "Integer32"
_ConfigSnapshotIPsecSelect_Object = MibScalar
configSnapshotIPsecSelect = _ConfigSnapshotIPsecSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 60),
    _ConfigSnapshotIPsecSelect_Type()
)
configSnapshotIPsecSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotIPsecSelect.setStatus("current")


class _ConfigSnapshotBFDSelect_Type(Integer32):
    """Custom type configSnapshotBFDSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotBFDSelect_Type.__name__ = "Integer32"
_ConfigSnapshotBFDSelect_Object = MibScalar
configSnapshotBFDSelect = _ConfigSnapshotBFDSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 61),
    _ConfigSnapshotBFDSelect_Type()
)
configSnapshotBFDSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotBFDSelect.setStatus("current")


class _ConfigSnapshotErpSelect_Type(Integer32):
    """Custom type configSnapshotErpSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotErpSelect_Type.__name__ = "Integer32"
_ConfigSnapshotErpSelect_Object = MibScalar
configSnapshotErpSelect = _ConfigSnapshotErpSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 62),
    _ConfigSnapshotErpSelect_Type()
)
configSnapshotErpSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotErpSelect.setStatus("current")


class _ConfigSnapshotMPLSSelect_Type(Integer32):
    """Custom type configSnapshotMPLSSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotMPLSSelect_Type.__name__ = "Integer32"
_ConfigSnapshotMPLSSelect_Object = MibScalar
configSnapshotMPLSSelect = _ConfigSnapshotMPLSSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 63),
    _ConfigSnapshotMPLSSelect_Type()
)
configSnapshotMPLSSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotMPLSSelect.setStatus("current")


class _ConfigSnapshotEFMOAMSelect_Type(Integer32):
    """Custom type configSnapshotEFMOAMSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotEFMOAMSelect_Type.__name__ = "Integer32"
_ConfigSnapshotEFMOAMSelect_Object = MibScalar
configSnapshotEFMOAMSelect = _ConfigSnapshotEFMOAMSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 64),
    _ConfigSnapshotEFMOAMSelect_Type()
)
configSnapshotEFMOAMSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotEFMOAMSelect.setStatus("current")


class _ConfigSnapshotLBDSelect_Type(Integer32):
    """Custom type configSnapshotLBDSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotLBDSelect_Type.__name__ = "Integer32"
_ConfigSnapshotLBDSelect_Object = MibScalar
configSnapshotLBDSelect = _ConfigSnapshotLBDSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 65),
    _ConfigSnapshotLBDSelect_Type()
)
configSnapshotLBDSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotLBDSelect.setStatus("current")


class _ConfigSnapshotSAASelect_Type(Integer32):
    """Custom type configSnapshotSAASelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotSAASelect_Type.__name__ = "Integer32"
_ConfigSnapshotSAASelect_Object = MibScalar
configSnapshotSAASelect = _ConfigSnapshotSAASelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 66),
    _ConfigSnapshotSAASelect_Type()
)
configSnapshotSAASelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotSAASelect.setStatus("current")


class _ConfigSnapshotDhcpSrvSelect_Type(Integer32):
    """Custom type configSnapshotDhcpSrvSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotDhcpSrvSelect_Type.__name__ = "Integer32"
_ConfigSnapshotDhcpSrvSelect_Object = MibScalar
configSnapshotDhcpSrvSelect = _ConfigSnapshotDhcpSrvSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 67),
    _ConfigSnapshotDhcpSrvSelect_Type()
)
configSnapshotDhcpSrvSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotDhcpSrvSelect.setStatus("current")


class _ConfigSnapshotLLDPSelect_Type(Integer32):
    """Custom type configSnapshotLLDPSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotLLDPSelect_Type.__name__ = "Integer32"
_ConfigSnapshotLLDPSelect_Object = MibScalar
configSnapshotLLDPSelect = _ConfigSnapshotLLDPSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 68),
    _ConfigSnapshotLLDPSelect_Type()
)
configSnapshotLLDPSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotLLDPSelect.setStatus("current")


class _ConfigSnapshotLFPSelect_Type(Integer32):
    """Custom type configSnapshotLFPSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotLFPSelect_Type.__name__ = "Integer32"
_ConfigSnapshotLFPSelect_Object = MibScalar
configSnapshotLFPSelect = _ConfigSnapshotLFPSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 69),
    _ConfigSnapshotLFPSelect_Type()
)
configSnapshotLFPSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotLFPSelect.setStatus("current")


class _ConfigSnapshotDHLSelect_Type(Integer32):
    """Custom type configSnapshotDHLSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotDHLSelect_Type.__name__ = "Integer32"
_ConfigSnapshotDHLSelect_Object = MibScalar
configSnapshotDHLSelect = _ConfigSnapshotDHLSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 70),
    _ConfigSnapshotDHLSelect_Type()
)
configSnapshotDHLSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotDHLSelect.setStatus("current")


class _ConfigSnapshotWccpSelect_Type(Integer32):
    """Custom type configSnapshotWccpSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotWccpSelect_Type.__name__ = "Integer32"
_ConfigSnapshotWccpSelect_Object = MibScalar
configSnapshotWccpSelect = _ConfigSnapshotWccpSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 71),
    _ConfigSnapshotWccpSelect_Type()
)
configSnapshotWccpSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotWccpSelect.setStatus("current")
_AlcatelIND1ConfigMgrMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1ConfigMgrMIBConformance = _AlcatelIND1ConfigMgrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1ConfigMgrMIBConformance.setStatus("current")
_AlcatelIND1ConfigMgrMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1ConfigMgrMIBGroups = _AlcatelIND1ConfigMgrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1ConfigMgrMIBGroups.setStatus("current")
_AlcatelIND1ConfigMgrMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1ConfigMgrMIBCompliances = _AlcatelIND1ConfigMgrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1ConfigMgrMIBCompliances.setStatus("current")

# Managed Objects groups

configFileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 2, 1, 1)
)
configFileGroup.setObjects(
      *(("ALCATEL-IND1-CONFIG-MGR-MIB", "configFileName"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configFileAction"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configErrorFileName"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configFileStatus"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configFileMode"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configErrorFileMaximum"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configChangeStatus"))
)
if mibBuilder.loadTexts:
    configFileGroup.setStatus("current")

configTimerFileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 2, 1, 2)
)
configTimerFileGroup.setObjects(
      *(("ALCATEL-IND1-CONFIG-MGR-MIB", "configTimerFileName"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configTimerFileTime"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configTimerFileStatus"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configTimerClear"))
)
if mibBuilder.loadTexts:
    configTimerFileGroup.setStatus("current")

configSnapshotGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 2, 1, 3)
)
configSnapshotGroup.setObjects(
      *(("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotAllSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotVlanSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotSpanningTreeSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotQOSSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotIPSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotIPXSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotIPMSSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotAAASelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotSNMPSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshot8021QSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotLinkAggregateSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotPortMirrorSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotXIPSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotHealthMonitorSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotBootPSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotBridgeSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotChassisSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotInterfaceSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotPolicySelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotSessionSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotServerLoadBalanceSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotSystemServiceSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotVRRPSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotWebSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotRIPSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotOSPFSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotBGPSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotIPRMSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotIPMRSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotModuleSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotRDPSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotIPv6Select"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotOSPF3Select"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotStackSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configWriteMemoryStatus"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotISISSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotEOAMSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotUDLDSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotNETSECSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotIPsecSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotBFDSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotErpSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotEFMOAMSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotLBDSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotSAASelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotLLDPSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotLFPSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotDHLSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotWccpSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotFileName"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotAction"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotAtmSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotDhcpSrvSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotMPLSSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotNTPSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotPortMappingSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotRIPngSelect"),
        ("ALCATEL-IND1-CONFIG-MGR-MIB", "configSnapshotSonetSelect"))
)
if mibBuilder.loadTexts:
    configSnapshotGroup.setStatus("current")

configTechSupportLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 2, 1, 4)
)
configTechSupportLogGroup.setObjects(
    ("ALCATEL-IND1-CONFIG-MGR-MIB", "configTechSupportLogAction")
)
if mibBuilder.loadTexts:
    configTechSupportLogGroup.setStatus("current")

configWriteMemoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 2, 1, 5)
)
configWriteMemoryGroup.setObjects(
    ("ALCATEL-IND1-CONFIG-MGR-MIB", "configWriteMemory")
)
if mibBuilder.loadTexts:
    configWriteMemoryGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1ConfigMgrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1ConfigMgrMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-CONFIG-MGR-MIB",
    **{"alcatelIND1ConfigMgrMIB": alcatelIND1ConfigMgrMIB,
       "alcatelIND1ConfigMgrMIBObjects": alcatelIND1ConfigMgrMIBObjects,
       "configManager": configManager,
       "configFileName": configFileName,
       "configFileAction": configFileAction,
       "configErrorFileName": configErrorFileName,
       "configFileStatus": configFileStatus,
       "configFileMode": configFileMode,
       "configTimerFileName": configTimerFileName,
       "configTimerFileTime": configTimerFileTime,
       "configTimerFileStatus": configTimerFileStatus,
       "configTimerClear": configTimerClear,
       "configSnapshotFileName": configSnapshotFileName,
       "configSnapshotAction": configSnapshotAction,
       "configSnapshotAllSelect": configSnapshotAllSelect,
       "configSnapshotVlanSelect": configSnapshotVlanSelect,
       "configSnapshotSpanningTreeSelect": configSnapshotSpanningTreeSelect,
       "configSnapshotQOSSelect": configSnapshotQOSSelect,
       "configSnapshotIPSelect": configSnapshotIPSelect,
       "configSnapshotIPXSelect": configSnapshotIPXSelect,
       "configSnapshotIPMSSelect": configSnapshotIPMSSelect,
       "configSnapshotAAASelect": configSnapshotAAASelect,
       "configSnapshotSNMPSelect": configSnapshotSNMPSelect,
       "configSnapshot8021QSelect": configSnapshot8021QSelect,
       "configSnapshotLinkAggregateSelect": configSnapshotLinkAggregateSelect,
       "configSnapshotPortMirrorSelect": configSnapshotPortMirrorSelect,
       "configSnapshotXIPSelect": configSnapshotXIPSelect,
       "configSnapshotHealthMonitorSelect": configSnapshotHealthMonitorSelect,
       "configSnapshotBootPSelect": configSnapshotBootPSelect,
       "configSnapshotBridgeSelect": configSnapshotBridgeSelect,
       "configSnapshotChassisSelect": configSnapshotChassisSelect,
       "configSnapshotInterfaceSelect": configSnapshotInterfaceSelect,
       "configSnapshotPolicySelect": configSnapshotPolicySelect,
       "configSnapshotSessionSelect": configSnapshotSessionSelect,
       "configSnapshotServerLoadBalanceSelect": configSnapshotServerLoadBalanceSelect,
       "configSnapshotSystemServiceSelect": configSnapshotSystemServiceSelect,
       "configSnapshotVRRPSelect": configSnapshotVRRPSelect,
       "configSnapshotWebSelect": configSnapshotWebSelect,
       "configSnapshotRIPSelect": configSnapshotRIPSelect,
       "configSnapshotOSPFSelect": configSnapshotOSPFSelect,
       "configSnapshotBGPSelect": configSnapshotBGPSelect,
       "configSnapshotIPRMSelect": configSnapshotIPRMSelect,
       "configSnapshotIPMRSelect": configSnapshotIPMRSelect,
       "configSnapshotModuleSelect": configSnapshotModuleSelect,
       "configTechSupportLogAction": configTechSupportLogAction,
       "configWriteMemory": configWriteMemory,
       "configErrorFileMaximum": configErrorFileMaximum,
       "configChangeStatus": configChangeStatus,
       "configSnapshotRDPSelect": configSnapshotRDPSelect,
       "configSnapshotIPv6Select": configSnapshotIPv6Select,
       "configSnapshotRIPngSelect": configSnapshotRIPngSelect,
       "configSnapshotAtmSelect": configSnapshotAtmSelect,
       "configSnapshotSonetSelect": configSnapshotSonetSelect,
       "configSnapshotNTPSelect": configSnapshotNTPSelect,
       "configSnapshotPortMappingSelect": configSnapshotPortMappingSelect,
       "configSnapshotOSPF3Select": configSnapshotOSPF3Select,
       "configWriteMemoryStatus": configWriteMemoryStatus,
       "configSnapshotStackSelect": configSnapshotStackSelect,
       "configSnapshotISISSelect": configSnapshotISISSelect,
       "configSnapshotEOAMSelect": configSnapshotEOAMSelect,
       "configSnapshotUDLDSelect": configSnapshotUDLDSelect,
       "configSnapshotNETSECSelect": configSnapshotNETSECSelect,
       "configSnapshotIPsecSelect": configSnapshotIPsecSelect,
       "configSnapshotBFDSelect": configSnapshotBFDSelect,
       "configSnapshotErpSelect": configSnapshotErpSelect,
       "configSnapshotMPLSSelect": configSnapshotMPLSSelect,
       "configSnapshotEFMOAMSelect": configSnapshotEFMOAMSelect,
       "configSnapshotLBDSelect": configSnapshotLBDSelect,
       "configSnapshotSAASelect": configSnapshotSAASelect,
       "configSnapshotDhcpSrvSelect": configSnapshotDhcpSrvSelect,
       "configSnapshotLLDPSelect": configSnapshotLLDPSelect,
       "configSnapshotLFPSelect": configSnapshotLFPSelect,
       "configSnapshotDHLSelect": configSnapshotDHLSelect,
       "configSnapshotWccpSelect": configSnapshotWccpSelect,
       "alcatelIND1ConfigMgrMIBConformance": alcatelIND1ConfigMgrMIBConformance,
       "alcatelIND1ConfigMgrMIBGroups": alcatelIND1ConfigMgrMIBGroups,
       "configFileGroup": configFileGroup,
       "configTimerFileGroup": configTimerFileGroup,
       "configSnapshotGroup": configSnapshotGroup,
       "configTechSupportLogGroup": configTechSupportLogGroup,
       "configWriteMemoryGroup": configWriteMemoryGroup,
       "alcatelIND1ConfigMgrMIBCompliances": alcatelIND1ConfigMgrMIBCompliances,
       "alcatelIND1ConfigMgrMIBCompliance": alcatelIND1ConfigMgrMIBCompliance}
)
