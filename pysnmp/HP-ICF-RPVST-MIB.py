# SNMP MIB module (HP-ICF-RPVST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-RPVST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:07 2024
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

(BridgeId,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId")

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(StpPortRole,) = mibBuilder.importSymbols(
    "HP-ICF-TC",
    "StpPortRole")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfRpvstMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88)
)
hpicfRpvstMIB.setRevisions(
        ("2017-08-08 00:00",
         "2013-03-21 00:28",
         "2011-08-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PointToPoint(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("forceFalse", 2),
          ("forceTrue", 1))
    )



# MIB Managed Objects in the order of their OIDs

_HpicfRpvstNotifications_ObjectIdentity = ObjectIdentity
hpicfRpvstNotifications = _HpicfRpvstNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 0)
)


class _HpicfRpvstErrantBpduDetector_Type(Integer32):
    """Custom type hpicfRpvstErrantBpduDetector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bpduFilter", 1),
          ("bpduProtection", 2))
    )


_HpicfRpvstErrantBpduDetector_Type.__name__ = "Integer32"
_HpicfRpvstErrantBpduDetector_Object = MibScalar
hpicfRpvstErrantBpduDetector = _HpicfRpvstErrantBpduDetector_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 0, 1),
    _HpicfRpvstErrantBpduDetector_Type()
)
hpicfRpvstErrantBpduDetector.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfRpvstErrantBpduDetector.setStatus("current")
_HpicfRpvstErrantBpduSrcMac_Type = MacAddress
_HpicfRpvstErrantBpduSrcMac_Object = MibScalar
hpicfRpvstErrantBpduSrcMac = _HpicfRpvstErrantBpduSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 0, 2),
    _HpicfRpvstErrantBpduSrcMac_Type()
)
hpicfRpvstErrantBpduSrcMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfRpvstErrantBpduSrcMac.setStatus("current")
_HpicfRpvstNewRootBridgeId_Type = BridgeId
_HpicfRpvstNewRootBridgeId_Object = MibScalar
hpicfRpvstNewRootBridgeId = _HpicfRpvstNewRootBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 0, 3),
    _HpicfRpvstNewRootBridgeId_Type()
)
hpicfRpvstNewRootBridgeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfRpvstNewRootBridgeId.setStatus("current")
_HpicfRpvstPreviousRootBridgeId_Type = BridgeId
_HpicfRpvstPreviousRootBridgeId_Object = MibScalar
hpicfRpvstPreviousRootBridgeId = _HpicfRpvstPreviousRootBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 0, 4),
    _HpicfRpvstPreviousRootBridgeId_Type()
)
hpicfRpvstPreviousRootBridgeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfRpvstPreviousRootBridgeId.setStatus("current")
_HpicfRpvstDesignatedPort_Type = DisplayString
_HpicfRpvstDesignatedPort_Object = MibScalar
hpicfRpvstDesignatedPort = _HpicfRpvstDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 0, 5),
    _HpicfRpvstDesignatedPort_Type()
)
hpicfRpvstDesignatedPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfRpvstDesignatedPort.setStatus("current")
_HpicfRpvstVlanIndex_Type = VlanIndex
_HpicfRpvstVlanIndex_Object = MibScalar
hpicfRpvstVlanIndex = _HpicfRpvstVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 0, 6),
    _HpicfRpvstVlanIndex_Type()
)
hpicfRpvstVlanIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfRpvstVlanIndex.setStatus("current")


class _HpicfRpvstPortNumber_Type(Integer32):
    """Custom type hpicfRpvstPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfRpvstPortNumber_Type.__name__ = "Integer32"
_HpicfRpvstPortNumber_Object = MibScalar
hpicfRpvstPortNumber = _HpicfRpvstPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 0, 7),
    _HpicfRpvstPortNumber_Type()
)
hpicfRpvstPortNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfRpvstPortNumber.setStatus("current")
_HpicfRpvstRootBridgeChangeTimeStamp_Type = DateAndTime
_HpicfRpvstRootBridgeChangeTimeStamp_Object = MibScalar
hpicfRpvstRootBridgeChangeTimeStamp = _HpicfRpvstRootBridgeChangeTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 0, 8),
    _HpicfRpvstRootBridgeChangeTimeStamp_Type()
)
hpicfRpvstRootBridgeChangeTimeStamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfRpvstRootBridgeChangeTimeStamp.setStatus("current")
_HpicfRpvstSuperiorBpduSrcMac_Type = MacAddress
_HpicfRpvstSuperiorBpduSrcMac_Object = MibScalar
hpicfRpvstSuperiorBpduSrcMac = _HpicfRpvstSuperiorBpduSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 0, 9),
    _HpicfRpvstSuperiorBpduSrcMac_Type()
)
hpicfRpvstSuperiorBpduSrcMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfRpvstSuperiorBpduSrcMac.setStatus("current")


class _HpicfRpvstSuperiorBpduSrcPort_Type(Integer32):
    """Custom type hpicfRpvstSuperiorBpduSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfRpvstSuperiorBpduSrcPort_Type.__name__ = "Integer32"
_HpicfRpvstSuperiorBpduSrcPort_Object = MibScalar
hpicfRpvstSuperiorBpduSrcPort = _HpicfRpvstSuperiorBpduSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 0, 10),
    _HpicfRpvstSuperiorBpduSrcPort_Type()
)
hpicfRpvstSuperiorBpduSrcPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfRpvstSuperiorBpduSrcPort.setStatus("current")


class _HpicfRpvstOldPortRole_Type(Integer32):
    """Custom type hpicfRpvstOldPortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfRpvstOldPortRole_Type.__name__ = "Integer32"
_HpicfRpvstOldPortRole_Object = MibScalar
hpicfRpvstOldPortRole = _HpicfRpvstOldPortRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 0, 15),
    _HpicfRpvstOldPortRole_Type()
)
hpicfRpvstOldPortRole.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfRpvstOldPortRole.setStatus("current")


class _HpicfRpvstNewPortRole_Type(Integer32):
    """Custom type hpicfRpvstNewPortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfRpvstNewPortRole_Type.__name__ = "Integer32"
_HpicfRpvstNewPortRole_Object = MibScalar
hpicfRpvstNewPortRole = _HpicfRpvstNewPortRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 0, 16),
    _HpicfRpvstNewPortRole_Type()
)
hpicfRpvstNewPortRole.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfRpvstNewPortRole.setStatus("current")
_HpicfRpvstTopoChangeTime_Type = DateAndTime
_HpicfRpvstTopoChangeTime_Object = MibScalar
hpicfRpvstTopoChangeTime = _HpicfRpvstTopoChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 0, 17),
    _HpicfRpvstTopoChangeTime_Type()
)
hpicfRpvstTopoChangeTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfRpvstTopoChangeTime.setStatus("current")
_HpicfRpvstObjects_ObjectIdentity = ObjectIdentity
hpicfRpvstObjects = _HpicfRpvstObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1)
)
_HpicfRpvstGeneralGroup_ObjectIdentity = ObjectIdentity
hpicfRpvstGeneralGroup = _HpicfRpvstGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 1)
)


class _HpicfRpvstResetCounters_Type(TruthValue):
    """Custom type hpicfRpvstResetCounters based on TruthValue"""


_HpicfRpvstResetCounters_Object = MibScalar
hpicfRpvstResetCounters = _HpicfRpvstResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 1, 1),
    _HpicfRpvstResetCounters_Type()
)
hpicfRpvstResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRpvstResetCounters.setStatus("current")


class _HpicfRpvstExtendedSystemID_Type(TruthValue):
    """Custom type hpicfRpvstExtendedSystemID based on TruthValue"""


_HpicfRpvstExtendedSystemID_Object = MibScalar
hpicfRpvstExtendedSystemID = _HpicfRpvstExtendedSystemID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 1, 2),
    _HpicfRpvstExtendedSystemID_Type()
)
hpicfRpvstExtendedSystemID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRpvstExtendedSystemID.setStatus("current")


class _HpicfRpvstIgnorePVIDInconsistency_Type(TruthValue):
    """Custom type hpicfRpvstIgnorePVIDInconsistency based on TruthValue"""


_HpicfRpvstIgnorePVIDInconsistency_Object = MibScalar
hpicfRpvstIgnorePVIDInconsistency = _HpicfRpvstIgnorePVIDInconsistency_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 1, 3),
    _HpicfRpvstIgnorePVIDInconsistency_Type()
)
hpicfRpvstIgnorePVIDInconsistency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRpvstIgnorePVIDInconsistency.setStatus("current")


class _HpicfRpvstPathCostMode_Type(Integer32):
    """Custom type hpicfRpvstPathCostMode based on Integer32"""
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
        *(("pathCost8021d", 1),
          ("pathCost8021t", 2),
          ("proprietary", 3))
    )


_HpicfRpvstPathCostMode_Type.__name__ = "Integer32"
_HpicfRpvstPathCostMode_Object = MibScalar
hpicfRpvstPathCostMode = _HpicfRpvstPathCostMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 1, 5),
    _HpicfRpvstPathCostMode_Type()
)
hpicfRpvstPathCostMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRpvstPathCostMode.setStatus("current")
_HpicfRpvstVlanTable_Object = MibTable
hpicfRpvstVlanTable = _HpicfRpvstVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfRpvstVlanTable.setStatus("current")
_HpicfRpvstVlanEntry_Object = MibTableRow
hpicfRpvstVlanEntry = _HpicfRpvstVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 2, 1)
)
hpicfRpvstVlanEntry.setIndexNames(
    (0, "HP-ICF-RPVST-MIB", "hpicfRpvstVlanId"),
)
if mibBuilder.loadTexts:
    hpicfRpvstVlanEntry.setStatus("current")
_HpicfRpvstVlanId_Type = VlanIndex
_HpicfRpvstVlanId_Object = MibTableColumn
hpicfRpvstVlanId = _HpicfRpvstVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 2, 1, 1),
    _HpicfRpvstVlanId_Type()
)
hpicfRpvstVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfRpvstVlanId.setStatus("current")


class _HpicfRpvstVlanHelloTime_Type(Integer32):
    """Custom type hpicfRpvstVlanHelloTime based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HpicfRpvstVlanHelloTime_Type.__name__ = "Integer32"
_HpicfRpvstVlanHelloTime_Object = MibTableColumn
hpicfRpvstVlanHelloTime = _HpicfRpvstVlanHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 2, 1, 2),
    _HpicfRpvstVlanHelloTime_Type()
)
hpicfRpvstVlanHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRpvstVlanHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    hpicfRpvstVlanHelloTime.setUnits("seconds")


class _HpicfRpvstVlanForwardDelay_Type(Integer32):
    """Custom type hpicfRpvstVlanForwardDelay based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_HpicfRpvstVlanForwardDelay_Type.__name__ = "Integer32"
_HpicfRpvstVlanForwardDelay_Object = MibTableColumn
hpicfRpvstVlanForwardDelay = _HpicfRpvstVlanForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 2, 1, 3),
    _HpicfRpvstVlanForwardDelay_Type()
)
hpicfRpvstVlanForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRpvstVlanForwardDelay.setStatus("current")
if mibBuilder.loadTexts:
    hpicfRpvstVlanForwardDelay.setUnits("seconds")


class _HpicfRpvstVlanMaxAge_Type(Integer32):
    """Custom type hpicfRpvstVlanMaxAge based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_HpicfRpvstVlanMaxAge_Type.__name__ = "Integer32"
_HpicfRpvstVlanMaxAge_Object = MibTableColumn
hpicfRpvstVlanMaxAge = _HpicfRpvstVlanMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 2, 1, 4),
    _HpicfRpvstVlanMaxAge_Type()
)
hpicfRpvstVlanMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRpvstVlanMaxAge.setStatus("current")
if mibBuilder.loadTexts:
    hpicfRpvstVlanMaxAge.setUnits("seconds")


class _HpicfRpvstVlanPriority_Type(Integer32):
    """Custom type hpicfRpvstVlanPriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfRpvstVlanPriority_Type.__name__ = "Integer32"
_HpicfRpvstVlanPriority_Object = MibTableColumn
hpicfRpvstVlanPriority = _HpicfRpvstVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 2, 1, 5),
    _HpicfRpvstVlanPriority_Type()
)
hpicfRpvstVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRpvstVlanPriority.setStatus("current")


class _HpicfRpvstVlanRoot_Type(Integer32):
    """Custom type hpicfRpvstVlanRoot based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("primary", 1),
          ("secondary", 2))
    )


_HpicfRpvstVlanRoot_Type.__name__ = "Integer32"
_HpicfRpvstVlanRoot_Object = MibTableColumn
hpicfRpvstVlanRoot = _HpicfRpvstVlanRoot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 2, 1, 6),
    _HpicfRpvstVlanRoot_Type()
)
hpicfRpvstVlanRoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRpvstVlanRoot.setStatus("current")


class _HpicfRpvstVlanRpvstStatus_Type(Integer32):
    """Custom type hpicfRpvstVlanRpvstStatus based on Integer32"""
    defaultValue = 1

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


_HpicfRpvstVlanRpvstStatus_Type.__name__ = "Integer32"
_HpicfRpvstVlanRpvstStatus_Object = MibTableColumn
hpicfRpvstVlanRpvstStatus = _HpicfRpvstVlanRpvstStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 2, 1, 7),
    _HpicfRpvstVlanRpvstStatus_Type()
)
hpicfRpvstVlanRpvstStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRpvstVlanRpvstStatus.setStatus("current")


class _HpicfRpvstVlanResetCounters_Type(TruthValue):
    """Custom type hpicfRpvstVlanResetCounters based on TruthValue"""


_HpicfRpvstVlanResetCounters_Object = MibTableColumn
hpicfRpvstVlanResetCounters = _HpicfRpvstVlanResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 2, 1, 8),
    _HpicfRpvstVlanResetCounters_Type()
)
hpicfRpvstVlanResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRpvstVlanResetCounters.setStatus("current")


class _HpicfRpvstVlanOperHelloTime_Type(Integer32):
    """Custom type hpicfRpvstVlanOperHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HpicfRpvstVlanOperHelloTime_Type.__name__ = "Integer32"
_HpicfRpvstVlanOperHelloTime_Object = MibTableColumn
hpicfRpvstVlanOperHelloTime = _HpicfRpvstVlanOperHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 2, 1, 9),
    _HpicfRpvstVlanOperHelloTime_Type()
)
hpicfRpvstVlanOperHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstVlanOperHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    hpicfRpvstVlanOperHelloTime.setUnits("seconds")


class _HpicfRpvstVlanRootPriority_Type(Integer32):
    """Custom type hpicfRpvstVlanRootPriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfRpvstVlanRootPriority_Type.__name__ = "Integer32"
_HpicfRpvstVlanRootPriority_Object = MibTableColumn
hpicfRpvstVlanRootPriority = _HpicfRpvstVlanRootPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 2, 1, 10),
    _HpicfRpvstVlanRootPriority_Type()
)
hpicfRpvstVlanRootPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstVlanRootPriority.setStatus("current")


class _HpicfRpvstVlanRootPort_Type(Integer32):
    """Custom type hpicfRpvstVlanRootPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfRpvstVlanRootPort_Type.__name__ = "Integer32"
_HpicfRpvstVlanRootPort_Object = MibTableColumn
hpicfRpvstVlanRootPort = _HpicfRpvstVlanRootPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 2, 1, 11),
    _HpicfRpvstVlanRootPort_Type()
)
hpicfRpvstVlanRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstVlanRootPort.setStatus("current")


class _HpicfRpvstVlanRootPathCost_Type(Integer32):
    """Custom type hpicfRpvstVlanRootPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_HpicfRpvstVlanRootPathCost_Type.__name__ = "Integer32"
_HpicfRpvstVlanRootPathCost_Object = MibTableColumn
hpicfRpvstVlanRootPathCost = _HpicfRpvstVlanRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 2, 1, 12),
    _HpicfRpvstVlanRootPathCost_Type()
)
hpicfRpvstVlanRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstVlanRootPathCost.setStatus("current")
_HpicfRpvstVlanRootMacAddress_Type = MacAddress
_HpicfRpvstVlanRootMacAddress_Object = MibTableColumn
hpicfRpvstVlanRootMacAddress = _HpicfRpvstVlanRootMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 2, 1, 13),
    _HpicfRpvstVlanRootMacAddress_Type()
)
hpicfRpvstVlanRootMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstVlanRootMacAddress.setStatus("current")
_HpicfRpvstVlanRootChangeCounter_Type = Counter32
_HpicfRpvstVlanRootChangeCounter_Object = MibTableColumn
hpicfRpvstVlanRootChangeCounter = _HpicfRpvstVlanRootChangeCounter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 2, 1, 14),
    _HpicfRpvstVlanRootChangeCounter_Type()
)
hpicfRpvstVlanRootChangeCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstVlanRootChangeCounter.setStatus("current")
_HpicfRpvstVlanTimeSinceLastTopoChange_Type = TimeTicks
_HpicfRpvstVlanTimeSinceLastTopoChange_Object = MibTableColumn
hpicfRpvstVlanTimeSinceLastTopoChange = _HpicfRpvstVlanTimeSinceLastTopoChange_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 2, 1, 15),
    _HpicfRpvstVlanTimeSinceLastTopoChange_Type()
)
hpicfRpvstVlanTimeSinceLastTopoChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstVlanTimeSinceLastTopoChange.setStatus("current")
_HpicfVlanTopoChangeCount_Type = Counter32
_HpicfVlanTopoChangeCount_Object = MibTableColumn
hpicfVlanTopoChangeCount = _HpicfVlanTopoChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 2, 1, 16),
    _HpicfVlanTopoChangeCount_Type()
)
hpicfVlanTopoChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVlanTopoChangeCount.setStatus("current")


class _HpicfRpvstSendTopoChangeCtrl_Type(TruthValue):
    """Custom type hpicfRpvstSendTopoChangeCtrl based on TruthValue"""


_HpicfRpvstSendTopoChangeCtrl_Object = MibTableColumn
hpicfRpvstSendTopoChangeCtrl = _HpicfRpvstSendTopoChangeCtrl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 2, 1, 17),
    _HpicfRpvstSendTopoChangeCtrl_Type()
)
hpicfRpvstSendTopoChangeCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRpvstSendTopoChangeCtrl.setStatus("current")


class _HpicfRpvstLogPortStateTransitions_Type(TruthValue):
    """Custom type hpicfRpvstLogPortStateTransitions based on TruthValue"""


_HpicfRpvstLogPortStateTransitions_Object = MibTableColumn
hpicfRpvstLogPortStateTransitions = _HpicfRpvstLogPortStateTransitions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 2, 1, 18),
    _HpicfRpvstLogPortStateTransitions_Type()
)
hpicfRpvstLogPortStateTransitions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRpvstLogPortStateTransitions.setStatus("current")
_HpicfRpvstPortTable_Object = MibTable
hpicfRpvstPortTable = _HpicfRpvstPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfRpvstPortTable.setStatus("current")
_HpicfRpvstPortEntry_Object = MibTableRow
hpicfRpvstPortEntry = _HpicfRpvstPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 3, 1)
)
hpicfRpvstPortEntry.setIndexNames(
    (0, "HP-ICF-RPVST-MIB", "hpicfRpvstPortIndex"),
)
if mibBuilder.loadTexts:
    hpicfRpvstPortEntry.setStatus("current")


class _HpicfRpvstPortIndex_Type(Integer32):
    """Custom type hpicfRpvstPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfRpvstPortIndex_Type.__name__ = "Integer32"
_HpicfRpvstPortIndex_Object = MibTableColumn
hpicfRpvstPortIndex = _HpicfRpvstPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 3, 1, 1),
    _HpicfRpvstPortIndex_Type()
)
hpicfRpvstPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfRpvstPortIndex.setStatus("current")
_HpicfRpvstPortAdminEdge_Type = TruthValue
_HpicfRpvstPortAdminEdge_Object = MibTableColumn
hpicfRpvstPortAdminEdge = _HpicfRpvstPortAdminEdge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 3, 1, 2),
    _HpicfRpvstPortAdminEdge_Type()
)
hpicfRpvstPortAdminEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRpvstPortAdminEdge.setStatus("current")
_HpicfRpvstPortAdminPointToPoint_Type = PointToPoint
_HpicfRpvstPortAdminPointToPoint_Object = MibTableColumn
hpicfRpvstPortAdminPointToPoint = _HpicfRpvstPortAdminPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 3, 1, 3),
    _HpicfRpvstPortAdminPointToPoint_Type()
)
hpicfRpvstPortAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRpvstPortAdminPointToPoint.setStatus("current")
_HpicfRpvstPortAutoEdge_Type = TruthValue
_HpicfRpvstPortAutoEdge_Object = MibTableColumn
hpicfRpvstPortAutoEdge = _HpicfRpvstPortAutoEdge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 3, 1, 4),
    _HpicfRpvstPortAutoEdge_Type()
)
hpicfRpvstPortAutoEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRpvstPortAutoEdge.setStatus("current")
_HpicfRpvstPortBpduFiltering_Type = TruthValue
_HpicfRpvstPortBpduFiltering_Object = MibTableColumn
hpicfRpvstPortBpduFiltering = _HpicfRpvstPortBpduFiltering_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 3, 1, 5),
    _HpicfRpvstPortBpduFiltering_Type()
)
hpicfRpvstPortBpduFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRpvstPortBpduFiltering.setStatus("current")
_HpicfRpvstPortRestrictedTcn_Type = TruthValue
_HpicfRpvstPortRestrictedTcn_Object = MibTableColumn
hpicfRpvstPortRestrictedTcn = _HpicfRpvstPortRestrictedTcn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 3, 1, 6),
    _HpicfRpvstPortRestrictedTcn_Type()
)
hpicfRpvstPortRestrictedTcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRpvstPortRestrictedTcn.setStatus("current")


class _HpicfRpvstPortRootGuard_Type(TruthValue):
    """Custom type hpicfRpvstPortRootGuard based on TruthValue"""


_HpicfRpvstPortRootGuard_Object = MibTableColumn
hpicfRpvstPortRootGuard = _HpicfRpvstPortRootGuard_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 3, 1, 7),
    _HpicfRpvstPortRootGuard_Type()
)
hpicfRpvstPortRootGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRpvstPortRootGuard.setStatus("current")


class _HpicfRpvstPortLoopGuard_Type(TruthValue):
    """Custom type hpicfRpvstPortLoopGuard based on TruthValue"""


_HpicfRpvstPortLoopGuard_Object = MibTableColumn
hpicfRpvstPortLoopGuard = _HpicfRpvstPortLoopGuard_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 3, 1, 8),
    _HpicfRpvstPortLoopGuard_Type()
)
hpicfRpvstPortLoopGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRpvstPortLoopGuard.setStatus("current")


class _HpicfRpvstPortBpduProtection_Type(TruthValue):
    """Custom type hpicfRpvstPortBpduProtection based on TruthValue"""


_HpicfRpvstPortBpduProtection_Object = MibTableColumn
hpicfRpvstPortBpduProtection = _HpicfRpvstPortBpduProtection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 3, 1, 9),
    _HpicfRpvstPortBpduProtection_Type()
)
hpicfRpvstPortBpduProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRpvstPortBpduProtection.setStatus("current")


class _HpicfRpvstPortIeeeRstBpdu_Type(TruthValue):
    """Custom type hpicfRpvstPortIeeeRstBpdu based on TruthValue"""


_HpicfRpvstPortIeeeRstBpdu_Object = MibTableColumn
hpicfRpvstPortIeeeRstBpdu = _HpicfRpvstPortIeeeRstBpdu_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 3, 1, 10),
    _HpicfRpvstPortIeeeRstBpdu_Type()
)
hpicfRpvstPortIeeeRstBpdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRpvstPortIeeeRstBpdu.setStatus("current")
_HpicfRpvstPortVlanTable_Object = MibTable
hpicfRpvstPortVlanTable = _HpicfRpvstPortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanTable.setStatus("current")
_HpicfRpvstPortVlanEntry_Object = MibTableRow
hpicfRpvstPortVlanEntry = _HpicfRpvstPortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 4, 1)
)
hpicfRpvstPortVlanEntry.setIndexNames(
    (0, "HP-ICF-RPVST-MIB", "hpicfRpvstVlanId"),
    (0, "HP-ICF-RPVST-MIB", "hpicfRpvstPortIndex"),
)
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanEntry.setStatus("current")


class _HpicfRpvstPortVlanPathCost_Type(Integer32):
    """Custom type hpicfRpvstPortVlanPathCost based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_HpicfRpvstPortVlanPathCost_Type.__name__ = "Integer32"
_HpicfRpvstPortVlanPathCost_Object = MibTableColumn
hpicfRpvstPortVlanPathCost = _HpicfRpvstPortVlanPathCost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 4, 1, 1),
    _HpicfRpvstPortVlanPathCost_Type()
)
hpicfRpvstPortVlanPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanPathCost.setStatus("current")


class _HpicfRpvstPortVlanPriority_Type(Integer32):
    """Custom type hpicfRpvstPortVlanPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpicfRpvstPortVlanPriority_Type.__name__ = "Integer32"
_HpicfRpvstPortVlanPriority_Object = MibTableColumn
hpicfRpvstPortVlanPriority = _HpicfRpvstPortVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 4, 1, 2),
    _HpicfRpvstPortVlanPriority_Type()
)
hpicfRpvstPortVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanPriority.setStatus("current")


class _HpicfRpvstPortVlanResetCounters_Type(TruthValue):
    """Custom type hpicfRpvstPortVlanResetCounters based on TruthValue"""


_HpicfRpvstPortVlanResetCounters_Object = MibTableColumn
hpicfRpvstPortVlanResetCounters = _HpicfRpvstPortVlanResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 4, 1, 3),
    _HpicfRpvstPortVlanResetCounters_Type()
)
hpicfRpvstPortVlanResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanResetCounters.setStatus("current")
_HpicfRpvstPortVlanRole_Type = StpPortRole
_HpicfRpvstPortVlanRole_Object = MibTableColumn
hpicfRpvstPortVlanRole = _HpicfRpvstPortVlanRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 4, 1, 4),
    _HpicfRpvstPortVlanRole_Type()
)
hpicfRpvstPortVlanRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanRole.setStatus("current")


class _HpicfRpvstPortVlanState_Type(Integer32):
    """Custom type hpicfRpvstPortVlanState based on Integer32"""
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
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 2),
          ("bpduError", 7),
          ("broken", 6),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3),
          ("loopInconsistent", 8),
          ("pvidInconsistent", 9),
          ("rootGuard", 10))
    )


_HpicfRpvstPortVlanState_Type.__name__ = "Integer32"
_HpicfRpvstPortVlanState_Object = MibTableColumn
hpicfRpvstPortVlanState = _HpicfRpvstPortVlanState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 4, 1, 5),
    _HpicfRpvstPortVlanState_Type()
)
hpicfRpvstPortVlanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanState.setStatus("current")
_HpicfRpvstPortVlanDesigBridge_Type = MacAddress
_HpicfRpvstPortVlanDesigBridge_Object = MibTableColumn
hpicfRpvstPortVlanDesigBridge = _HpicfRpvstPortVlanDesigBridge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 4, 1, 6),
    _HpicfRpvstPortVlanDesigBridge_Type()
)
hpicfRpvstPortVlanDesigBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanDesigBridge.setStatus("current")
_HpicfRpvstPortVlanOperPointToPoint_Type = TruthValue
_HpicfRpvstPortVlanOperPointToPoint_Object = MibTableColumn
hpicfRpvstPortVlanOperPointToPoint = _HpicfRpvstPortVlanOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 4, 1, 7),
    _HpicfRpvstPortVlanOperPointToPoint_Type()
)
hpicfRpvstPortVlanOperPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanOperPointToPoint.setStatus("current")
_HpicfRpvstPortVlanOperEdge_Type = TruthValue
_HpicfRpvstPortVlanOperEdge_Object = MibTableColumn
hpicfRpvstPortVlanOperEdge = _HpicfRpvstPortVlanOperEdge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 4, 1, 8),
    _HpicfRpvstPortVlanOperEdge_Type()
)
hpicfRpvstPortVlanOperEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanOperEdge.setStatus("current")


class _HpicfRpvstPortVlanInconsistencyReason_Type(Integer32):
    """Custom type hpicfRpvstPortVlanInconsistencyReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inconsistentPvidprotected", 3),
          ("loopProtected", 2),
          ("rootProtected", 1))
    )


_HpicfRpvstPortVlanInconsistencyReason_Type.__name__ = "Integer32"
_HpicfRpvstPortVlanInconsistencyReason_Object = MibTableColumn
hpicfRpvstPortVlanInconsistencyReason = _HpicfRpvstPortVlanInconsistencyReason_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 4, 1, 9),
    _HpicfRpvstPortVlanInconsistencyReason_Type()
)
hpicfRpvstPortVlanInconsistencyReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanInconsistencyReason.setStatus("current")
_HpicfRpvstPortVlanRxCountersTable_Object = MibTable
hpicfRpvstPortVlanRxCountersTable = _HpicfRpvstPortVlanRxCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 5)
)
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanRxCountersTable.setStatus("current")
_HpicfRpvstPortVlanRxCountersEntry_Object = MibTableRow
hpicfRpvstPortVlanRxCountersEntry = _HpicfRpvstPortVlanRxCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 5, 1)
)
hpicfRpvstPortVlanRxCountersEntry.setIndexNames(
    (0, "HP-ICF-RPVST-MIB", "hpicfRpvstVlanId"),
    (0, "HP-ICF-RPVST-MIB", "hpicfRpvstPortIndex"),
)
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanRxCountersEntry.setStatus("current")
_HpicfRpvstPortVlanRpvstBpduRx_Type = Counter32
_HpicfRpvstPortVlanRpvstBpduRx_Object = MibTableColumn
hpicfRpvstPortVlanRpvstBpduRx = _HpicfRpvstPortVlanRpvstBpduRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 5, 1, 1),
    _HpicfRpvstPortVlanRpvstBpduRx_Type()
)
hpicfRpvstPortVlanRpvstBpduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanRpvstBpduRx.setStatus("current")
_HpicfRpvstPortVlanRpvstBpduRxLastUpdated_Type = DateAndTime
_HpicfRpvstPortVlanRpvstBpduRxLastUpdated_Object = MibTableColumn
hpicfRpvstPortVlanRpvstBpduRxLastUpdated = _HpicfRpvstPortVlanRpvstBpduRxLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 5, 1, 2),
    _HpicfRpvstPortVlanRpvstBpduRxLastUpdated_Type()
)
hpicfRpvstPortVlanRpvstBpduRxLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanRpvstBpduRxLastUpdated.setStatus("current")
_HpicfRpvstPortVlanRstBpduRx_Type = Counter32
_HpicfRpvstPortVlanRstBpduRx_Object = MibTableColumn
hpicfRpvstPortVlanRstBpduRx = _HpicfRpvstPortVlanRstBpduRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 5, 1, 3),
    _HpicfRpvstPortVlanRstBpduRx_Type()
)
hpicfRpvstPortVlanRstBpduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanRstBpduRx.setStatus("current")
_HpicfRpvstPortVlanRstBpduRxLastUpdated_Type = DateAndTime
_HpicfRpvstPortVlanRstBpduRxLastUpdated_Object = MibTableColumn
hpicfRpvstPortVlanRstBpduRxLastUpdated = _HpicfRpvstPortVlanRstBpduRxLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 5, 1, 4),
    _HpicfRpvstPortVlanRstBpduRxLastUpdated_Type()
)
hpicfRpvstPortVlanRstBpduRxLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanRstBpduRxLastUpdated.setStatus("current")
_HpicfRpvstPortVlanConfigBpduRx_Type = Counter32
_HpicfRpvstPortVlanConfigBpduRx_Object = MibTableColumn
hpicfRpvstPortVlanConfigBpduRx = _HpicfRpvstPortVlanConfigBpduRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 5, 1, 5),
    _HpicfRpvstPortVlanConfigBpduRx_Type()
)
hpicfRpvstPortVlanConfigBpduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanConfigBpduRx.setStatus("current")
_HpicfRpvstPortVlanConfigBpduRxLastUpdated_Type = DateAndTime
_HpicfRpvstPortVlanConfigBpduRxLastUpdated_Object = MibTableColumn
hpicfRpvstPortVlanConfigBpduRxLastUpdated = _HpicfRpvstPortVlanConfigBpduRxLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 5, 1, 6),
    _HpicfRpvstPortVlanConfigBpduRxLastUpdated_Type()
)
hpicfRpvstPortVlanConfigBpduRxLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanConfigBpduRxLastUpdated.setStatus("current")
_HpicfRpvstPortVlanTcnBpduRx_Type = Counter32
_HpicfRpvstPortVlanTcnBpduRx_Object = MibTableColumn
hpicfRpvstPortVlanTcnBpduRx = _HpicfRpvstPortVlanTcnBpduRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 5, 1, 7),
    _HpicfRpvstPortVlanTcnBpduRx_Type()
)
hpicfRpvstPortVlanTcnBpduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanTcnBpduRx.setStatus("current")
_HpicfRpvstPortVlanTcnBpduRxLastUpdated_Type = DateAndTime
_HpicfRpvstPortVlanTcnBpduRxLastUpdated_Object = MibTableColumn
hpicfRpvstPortVlanTcnBpduRxLastUpdated = _HpicfRpvstPortVlanTcnBpduRxLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 5, 1, 8),
    _HpicfRpvstPortVlanTcnBpduRxLastUpdated_Type()
)
hpicfRpvstPortVlanTcnBpduRxLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanTcnBpduRxLastUpdated.setStatus("current")
_HpicfRpvstPortVlanTcDetectCount_Type = Counter32
_HpicfRpvstPortVlanTcDetectCount_Object = MibTableColumn
hpicfRpvstPortVlanTcDetectCount = _HpicfRpvstPortVlanTcDetectCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 5, 1, 9),
    _HpicfRpvstPortVlanTcDetectCount_Type()
)
hpicfRpvstPortVlanTcDetectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanTcDetectCount.setStatus("current")
_HpicfRpvstPortVlanTcDetectCountLastUpdated_Type = DateAndTime
_HpicfRpvstPortVlanTcDetectCountLastUpdated_Object = MibTableColumn
hpicfRpvstPortVlanTcDetectCountLastUpdated = _HpicfRpvstPortVlanTcDetectCountLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 5, 1, 10),
    _HpicfRpvstPortVlanTcDetectCountLastUpdated_Type()
)
hpicfRpvstPortVlanTcDetectCountLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanTcDetectCountLastUpdated.setStatus("current")
_HpicfRpvstPortVlanTcFlagRx_Type = Counter32
_HpicfRpvstPortVlanTcFlagRx_Object = MibTableColumn
hpicfRpvstPortVlanTcFlagRx = _HpicfRpvstPortVlanTcFlagRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 5, 1, 11),
    _HpicfRpvstPortVlanTcFlagRx_Type()
)
hpicfRpvstPortVlanTcFlagRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanTcFlagRx.setStatus("current")
_HpicfRpvstPortVlanTcFlagRxLastUpdated_Type = DateAndTime
_HpicfRpvstPortVlanTcFlagRxLastUpdated_Object = MibTableColumn
hpicfRpvstPortVlanTcFlagRxLastUpdated = _HpicfRpvstPortVlanTcFlagRxLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 5, 1, 12),
    _HpicfRpvstPortVlanTcFlagRxLastUpdated_Type()
)
hpicfRpvstPortVlanTcFlagRxLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanTcFlagRxLastUpdated.setStatus("current")
_HpicfRpvstPortVlanTcAckFlagRx_Type = Counter32
_HpicfRpvstPortVlanTcAckFlagRx_Object = MibTableColumn
hpicfRpvstPortVlanTcAckFlagRx = _HpicfRpvstPortVlanTcAckFlagRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 5, 1, 13),
    _HpicfRpvstPortVlanTcAckFlagRx_Type()
)
hpicfRpvstPortVlanTcAckFlagRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanTcAckFlagRx.setStatus("current")
_HpicfRpvstPortVlanTcAckFlagRxLastUpdated_Type = DateAndTime
_HpicfRpvstPortVlanTcAckFlagRxLastUpdated_Object = MibTableColumn
hpicfRpvstPortVlanTcAckFlagRxLastUpdated = _HpicfRpvstPortVlanTcAckFlagRxLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 5, 1, 14),
    _HpicfRpvstPortVlanTcAckFlagRxLastUpdated_Type()
)
hpicfRpvstPortVlanTcAckFlagRxLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanTcAckFlagRxLastUpdated.setStatus("current")
_HpicfRpvstPortVlanStarvedBpduCount_Type = Counter32
_HpicfRpvstPortVlanStarvedBpduCount_Object = MibTableColumn
hpicfRpvstPortVlanStarvedBpduCount = _HpicfRpvstPortVlanStarvedBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 5, 1, 15),
    _HpicfRpvstPortVlanStarvedBpduCount_Type()
)
hpicfRpvstPortVlanStarvedBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanStarvedBpduCount.setStatus("current")
_HpicfRpvstPortVlanStarvedBpduCountLastUpdated_Type = DateAndTime
_HpicfRpvstPortVlanStarvedBpduCountLastUpdated_Object = MibTableColumn
hpicfRpvstPortVlanStarvedBpduCountLastUpdated = _HpicfRpvstPortVlanStarvedBpduCountLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 5, 1, 16),
    _HpicfRpvstPortVlanStarvedBpduCountLastUpdated_Type()
)
hpicfRpvstPortVlanStarvedBpduCountLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanStarvedBpduCountLastUpdated.setStatus("current")
_HpicfRpvstPortVlanInvalidBpduRx_Type = Counter32
_HpicfRpvstPortVlanInvalidBpduRx_Object = MibTableColumn
hpicfRpvstPortVlanInvalidBpduRx = _HpicfRpvstPortVlanInvalidBpduRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 5, 1, 17),
    _HpicfRpvstPortVlanInvalidBpduRx_Type()
)
hpicfRpvstPortVlanInvalidBpduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanInvalidBpduRx.setStatus("current")
_HpicfRpvstPortVlanInvalidBpduRxLastUpdated_Type = DateAndTime
_HpicfRpvstPortVlanInvalidBpduRxLastUpdated_Object = MibTableColumn
hpicfRpvstPortVlanInvalidBpduRxLastUpdated = _HpicfRpvstPortVlanInvalidBpduRxLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 5, 1, 18),
    _HpicfRpvstPortVlanInvalidBpduRxLastUpdated_Type()
)
hpicfRpvstPortVlanInvalidBpduRxLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanInvalidBpduRxLastUpdated.setStatus("current")
_HpicfRpvstPortVlanLoopedBackBpduRx_Type = Counter32
_HpicfRpvstPortVlanLoopedBackBpduRx_Object = MibTableColumn
hpicfRpvstPortVlanLoopedBackBpduRx = _HpicfRpvstPortVlanLoopedBackBpduRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 5, 1, 19),
    _HpicfRpvstPortVlanLoopedBackBpduRx_Type()
)
hpicfRpvstPortVlanLoopedBackBpduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanLoopedBackBpduRx.setStatus("current")
_HpicfRpvstPortVlanLoopedBackBpduRxLastUpdated_Type = DateAndTime
_HpicfRpvstPortVlanLoopedBackBpduRxLastUpdated_Object = MibTableColumn
hpicfRpvstPortVlanLoopedBackBpduRxLastUpdated = _HpicfRpvstPortVlanLoopedBackBpduRxLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 5, 1, 20),
    _HpicfRpvstPortVlanLoopedBackBpduRxLastUpdated_Type()
)
hpicfRpvstPortVlanLoopedBackBpduRxLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanLoopedBackBpduRxLastUpdated.setStatus("current")
_HpicfRpvstPortVlanErrantBpduRxCount_Type = Counter32
_HpicfRpvstPortVlanErrantBpduRxCount_Object = MibTableColumn
hpicfRpvstPortVlanErrantBpduRxCount = _HpicfRpvstPortVlanErrantBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 5, 1, 21),
    _HpicfRpvstPortVlanErrantBpduRxCount_Type()
)
hpicfRpvstPortVlanErrantBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanErrantBpduRxCount.setStatus("current")
_HpicfRpvstPortVlanErrantBpduRxCountLastUpdated_Type = DateAndTime
_HpicfRpvstPortVlanErrantBpduRxCountLastUpdated_Object = MibTableColumn
hpicfRpvstPortVlanErrantBpduRxCountLastUpdated = _HpicfRpvstPortVlanErrantBpduRxCountLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 5, 1, 22),
    _HpicfRpvstPortVlanErrantBpduRxCountLastUpdated_Type()
)
hpicfRpvstPortVlanErrantBpduRxCountLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanErrantBpduRxCountLastUpdated.setStatus("current")
_HpicfRpvstPortVlanAgedBpduRx_Type = Counter32
_HpicfRpvstPortVlanAgedBpduRx_Object = MibTableColumn
hpicfRpvstPortVlanAgedBpduRx = _HpicfRpvstPortVlanAgedBpduRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 5, 1, 23),
    _HpicfRpvstPortVlanAgedBpduRx_Type()
)
hpicfRpvstPortVlanAgedBpduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanAgedBpduRx.setStatus("current")
_HpicfRpvstPortVlanAgedBpduRxLastUpdated_Type = DateAndTime
_HpicfRpvstPortVlanAgedBpduRxLastUpdated_Object = MibTableColumn
hpicfRpvstPortVlanAgedBpduRxLastUpdated = _HpicfRpvstPortVlanAgedBpduRxLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 5, 1, 24),
    _HpicfRpvstPortVlanAgedBpduRxLastUpdated_Type()
)
hpicfRpvstPortVlanAgedBpduRxLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanAgedBpduRxLastUpdated.setStatus("current")
_HpicfRpvstPortVlanTxCountersTable_Object = MibTable
hpicfRpvstPortVlanTxCountersTable = _HpicfRpvstPortVlanTxCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 6)
)
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanTxCountersTable.setStatus("current")
_HpicfRpvstPortVlanTxCountersEntry_Object = MibTableRow
hpicfRpvstPortVlanTxCountersEntry = _HpicfRpvstPortVlanTxCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 6, 1)
)
hpicfRpvstPortVlanTxCountersEntry.setIndexNames(
    (0, "HP-ICF-RPVST-MIB", "hpicfRpvstVlanId"),
    (0, "HP-ICF-RPVST-MIB", "hpicfRpvstPortIndex"),
)
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanTxCountersEntry.setStatus("current")
_HpicfRpvstPortVlanRpvstBpduTx_Type = Counter32
_HpicfRpvstPortVlanRpvstBpduTx_Object = MibTableColumn
hpicfRpvstPortVlanRpvstBpduTx = _HpicfRpvstPortVlanRpvstBpduTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 6, 1, 1),
    _HpicfRpvstPortVlanRpvstBpduTx_Type()
)
hpicfRpvstPortVlanRpvstBpduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanRpvstBpduTx.setStatus("current")
_HpicfRpvstPortVlanRpvstBpduTxLastUpdated_Type = DateAndTime
_HpicfRpvstPortVlanRpvstBpduTxLastUpdated_Object = MibTableColumn
hpicfRpvstPortVlanRpvstBpduTxLastUpdated = _HpicfRpvstPortVlanRpvstBpduTxLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 6, 1, 2),
    _HpicfRpvstPortVlanRpvstBpduTxLastUpdated_Type()
)
hpicfRpvstPortVlanRpvstBpduTxLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanRpvstBpduTxLastUpdated.setStatus("current")
_HpicfRpvstPortVlanRstBpduTx_Type = Counter32
_HpicfRpvstPortVlanRstBpduTx_Object = MibTableColumn
hpicfRpvstPortVlanRstBpduTx = _HpicfRpvstPortVlanRstBpduTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 6, 1, 3),
    _HpicfRpvstPortVlanRstBpduTx_Type()
)
hpicfRpvstPortVlanRstBpduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanRstBpduTx.setStatus("current")
_HpicfRpvstPortVlanRstBpduTxLastUpdated_Type = DateAndTime
_HpicfRpvstPortVlanRstBpduTxLastUpdated_Object = MibTableColumn
hpicfRpvstPortVlanRstBpduTxLastUpdated = _HpicfRpvstPortVlanRstBpduTxLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 6, 1, 4),
    _HpicfRpvstPortVlanRstBpduTxLastUpdated_Type()
)
hpicfRpvstPortVlanRstBpduTxLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanRstBpduTxLastUpdated.setStatus("current")
_HpicfRpvstPortVlanConfigBpduTx_Type = Counter32
_HpicfRpvstPortVlanConfigBpduTx_Object = MibTableColumn
hpicfRpvstPortVlanConfigBpduTx = _HpicfRpvstPortVlanConfigBpduTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 6, 1, 5),
    _HpicfRpvstPortVlanConfigBpduTx_Type()
)
hpicfRpvstPortVlanConfigBpduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanConfigBpduTx.setStatus("current")
_HpicfRpvstPortVlanConfigBpduTxLastUpdated_Type = DateAndTime
_HpicfRpvstPortVlanConfigBpduTxLastUpdated_Object = MibTableColumn
hpicfRpvstPortVlanConfigBpduTxLastUpdated = _HpicfRpvstPortVlanConfigBpduTxLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 6, 1, 6),
    _HpicfRpvstPortVlanConfigBpduTxLastUpdated_Type()
)
hpicfRpvstPortVlanConfigBpduTxLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanConfigBpduTxLastUpdated.setStatus("current")
_HpicfRpvstPortVlanTcnBpduTx_Type = Counter32
_HpicfRpvstPortVlanTcnBpduTx_Object = MibTableColumn
hpicfRpvstPortVlanTcnBpduTx = _HpicfRpvstPortVlanTcnBpduTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 6, 1, 7),
    _HpicfRpvstPortVlanTcnBpduTx_Type()
)
hpicfRpvstPortVlanTcnBpduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanTcnBpduTx.setStatus("current")
_HpicfRpvstPortVlanTcnBpduTxLastUpdated_Type = DateAndTime
_HpicfRpvstPortVlanTcnBpduTxLastUpdated_Object = MibTableColumn
hpicfRpvstPortVlanTcnBpduTxLastUpdated = _HpicfRpvstPortVlanTcnBpduTxLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 6, 1, 8),
    _HpicfRpvstPortVlanTcnBpduTxLastUpdated_Type()
)
hpicfRpvstPortVlanTcnBpduTxLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanTcnBpduTxLastUpdated.setStatus("current")
_HpicfRpvstPortVlanTcFlagTx_Type = Counter32
_HpicfRpvstPortVlanTcFlagTx_Object = MibTableColumn
hpicfRpvstPortVlanTcFlagTx = _HpicfRpvstPortVlanTcFlagTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 6, 1, 9),
    _HpicfRpvstPortVlanTcFlagTx_Type()
)
hpicfRpvstPortVlanTcFlagTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanTcFlagTx.setStatus("current")
_HpicfRpvstPortVlanTcFlagTxLastUpdated_Type = DateAndTime
_HpicfRpvstPortVlanTcFlagTxLastUpdated_Object = MibTableColumn
hpicfRpvstPortVlanTcFlagTxLastUpdated = _HpicfRpvstPortVlanTcFlagTxLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 6, 1, 10),
    _HpicfRpvstPortVlanTcFlagTxLastUpdated_Type()
)
hpicfRpvstPortVlanTcFlagTxLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanTcFlagTxLastUpdated.setStatus("current")
_HpicfRpvstPortVlanTcAckFlagTx_Type = Counter32
_HpicfRpvstPortVlanTcAckFlagTx_Object = MibTableColumn
hpicfRpvstPortVlanTcAckFlagTx = _HpicfRpvstPortVlanTcAckFlagTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 6, 1, 11),
    _HpicfRpvstPortVlanTcAckFlagTx_Type()
)
hpicfRpvstPortVlanTcAckFlagTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanTcAckFlagTx.setStatus("current")
_HpicfRpvstPortVlanTcAckFlagTxLastUpdated_Type = DateAndTime
_HpicfRpvstPortVlanTcAckFlagTxLastUpdated_Object = MibTableColumn
hpicfRpvstPortVlanTcAckFlagTxLastUpdated = _HpicfRpvstPortVlanTcAckFlagTxLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 6, 1, 12),
    _HpicfRpvstPortVlanTcAckFlagTxLastUpdated_Type()
)
hpicfRpvstPortVlanTcAckFlagTxLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanTcAckFlagTxLastUpdated.setStatus("current")
_HpicfRpvstVlanRootHistoryTable_Object = MibTable
hpicfRpvstVlanRootHistoryTable = _HpicfRpvstVlanRootHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 7)
)
if mibBuilder.loadTexts:
    hpicfRpvstVlanRootHistoryTable.setStatus("current")
_HpicfRpvstVlanRootHistoryEntry_Object = MibTableRow
hpicfRpvstVlanRootHistoryEntry = _HpicfRpvstVlanRootHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 7, 1)
)
hpicfRpvstVlanRootHistoryEntry.setIndexNames(
    (0, "HP-ICF-RPVST-MIB", "hpicfRpvstVlanId"),
    (0, "HP-ICF-RPVST-MIB", "hpicfRpvstVlanRootHistoryIndex"),
)
if mibBuilder.loadTexts:
    hpicfRpvstVlanRootHistoryEntry.setStatus("current")


class _HpicfRpvstVlanRootHistoryIndex_Type(Integer32):
    """Custom type hpicfRpvstVlanRootHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HpicfRpvstVlanRootHistoryIndex_Type.__name__ = "Integer32"
_HpicfRpvstVlanRootHistoryIndex_Object = MibTableColumn
hpicfRpvstVlanRootHistoryIndex = _HpicfRpvstVlanRootHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 7, 1, 1),
    _HpicfRpvstVlanRootHistoryIndex_Type()
)
hpicfRpvstVlanRootHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfRpvstVlanRootHistoryIndex.setStatus("current")
_HpicfRpvstVlanRootBridgeId_Type = BridgeId
_HpicfRpvstVlanRootBridgeId_Object = MibTableColumn
hpicfRpvstVlanRootBridgeId = _HpicfRpvstVlanRootBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 7, 1, 2),
    _HpicfRpvstVlanRootBridgeId_Type()
)
hpicfRpvstVlanRootBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstVlanRootBridgeId.setStatus("current")
_HpicfRpvstVlanRootHistoryTime_Type = DateAndTime
_HpicfRpvstVlanRootHistoryTime_Object = MibTableColumn
hpicfRpvstVlanRootHistoryTime = _HpicfRpvstVlanRootHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 7, 1, 3),
    _HpicfRpvstVlanRootHistoryTime_Type()
)
hpicfRpvstVlanRootHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstVlanRootHistoryTime.setStatus("current")
_HpicfRpvstVlanTopologyChangeRxTable_Object = MibTable
hpicfRpvstVlanTopologyChangeRxTable = _HpicfRpvstVlanTopologyChangeRxTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 8)
)
if mibBuilder.loadTexts:
    hpicfRpvstVlanTopologyChangeRxTable.setStatus("current")
_HpicfRpvstVlanTopologyChangeRxEntry_Object = MibTableRow
hpicfRpvstVlanTopologyChangeRxEntry = _HpicfRpvstVlanTopologyChangeRxEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 8, 1)
)
hpicfRpvstVlanTopologyChangeRxEntry.setIndexNames(
    (0, "HP-ICF-RPVST-MIB", "hpicfRpvstVlanId"),
    (0, "HP-ICF-RPVST-MIB", "hpicfRpvstVlanTopologyChangeRxIndex"),
)
if mibBuilder.loadTexts:
    hpicfRpvstVlanTopologyChangeRxEntry.setStatus("current")


class _HpicfRpvstVlanTopologyChangeRxIndex_Type(Integer32):
    """Custom type hpicfRpvstVlanTopologyChangeRxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfRpvstVlanTopologyChangeRxIndex_Type.__name__ = "Integer32"
_HpicfRpvstVlanTopologyChangeRxIndex_Object = MibTableColumn
hpicfRpvstVlanTopologyChangeRxIndex = _HpicfRpvstVlanTopologyChangeRxIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 8, 1, 1),
    _HpicfRpvstVlanTopologyChangeRxIndex_Type()
)
hpicfRpvstVlanTopologyChangeRxIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfRpvstVlanTopologyChangeRxIndex.setStatus("current")
_HpicfRpvstVlanTopologyChangeRxTime_Type = DateAndTime
_HpicfRpvstVlanTopologyChangeRxTime_Object = MibTableColumn
hpicfRpvstVlanTopologyChangeRxTime = _HpicfRpvstVlanTopologyChangeRxTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 8, 1, 2),
    _HpicfRpvstVlanTopologyChangeRxTime_Type()
)
hpicfRpvstVlanTopologyChangeRxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstVlanTopologyChangeRxTime.setStatus("current")
_HpicfRpvstVlanTopologyChangeRxMacAddress_Type = MacAddress
_HpicfRpvstVlanTopologyChangeRxMacAddress_Object = MibTableColumn
hpicfRpvstVlanTopologyChangeRxMacAddress = _HpicfRpvstVlanTopologyChangeRxMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 8, 1, 3),
    _HpicfRpvstVlanTopologyChangeRxMacAddress_Type()
)
hpicfRpvstVlanTopologyChangeRxMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstVlanTopologyChangeRxMacAddress.setStatus("current")
_HpicfRpvstVlanTopologyChangeRxPortId_Type = Integer32
_HpicfRpvstVlanTopologyChangeRxPortId_Object = MibTableColumn
hpicfRpvstVlanTopologyChangeRxPortId = _HpicfRpvstVlanTopologyChangeRxPortId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 8, 1, 4),
    _HpicfRpvstVlanTopologyChangeRxPortId_Type()
)
hpicfRpvstVlanTopologyChangeRxPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstVlanTopologyChangeRxPortId.setStatus("current")
_HpicfRpvstVlanTopologyChangeTxTable_Object = MibTable
hpicfRpvstVlanTopologyChangeTxTable = _HpicfRpvstVlanTopologyChangeTxTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 9)
)
if mibBuilder.loadTexts:
    hpicfRpvstVlanTopologyChangeTxTable.setStatus("current")
_HpicfRpvstVlanTopologyChangeTxEntry_Object = MibTableRow
hpicfRpvstVlanTopologyChangeTxEntry = _HpicfRpvstVlanTopologyChangeTxEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 9, 1)
)
hpicfRpvstVlanTopologyChangeTxEntry.setIndexNames(
    (0, "HP-ICF-RPVST-MIB", "hpicfRpvstVlanId"),
    (0, "HP-ICF-RPVST-MIB", "hpicfRpvstVlanTopologyChangeTxIndex"),
)
if mibBuilder.loadTexts:
    hpicfRpvstVlanTopologyChangeTxEntry.setStatus("current")


class _HpicfRpvstVlanTopologyChangeTxIndex_Type(Integer32):
    """Custom type hpicfRpvstVlanTopologyChangeTxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfRpvstVlanTopologyChangeTxIndex_Type.__name__ = "Integer32"
_HpicfRpvstVlanTopologyChangeTxIndex_Object = MibTableColumn
hpicfRpvstVlanTopologyChangeTxIndex = _HpicfRpvstVlanTopologyChangeTxIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 9, 1, 1),
    _HpicfRpvstVlanTopologyChangeTxIndex_Type()
)
hpicfRpvstVlanTopologyChangeTxIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfRpvstVlanTopologyChangeTxIndex.setStatus("current")
_HpicfRpvstVlanTopologyChangeTxCurrentPortRole_Type = StpPortRole
_HpicfRpvstVlanTopologyChangeTxCurrentPortRole_Object = MibTableColumn
hpicfRpvstVlanTopologyChangeTxCurrentPortRole = _HpicfRpvstVlanTopologyChangeTxCurrentPortRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 9, 1, 2),
    _HpicfRpvstVlanTopologyChangeTxCurrentPortRole_Type()
)
hpicfRpvstVlanTopologyChangeTxCurrentPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstVlanTopologyChangeTxCurrentPortRole.setStatus("current")
_HpicfRpvstVlanTopologyChangeTxPreviousPortRole_Type = StpPortRole
_HpicfRpvstVlanTopologyChangeTxPreviousPortRole_Object = MibTableColumn
hpicfRpvstVlanTopologyChangeTxPreviousPortRole = _HpicfRpvstVlanTopologyChangeTxPreviousPortRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 9, 1, 3),
    _HpicfRpvstVlanTopologyChangeTxPreviousPortRole_Type()
)
hpicfRpvstVlanTopologyChangeTxPreviousPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstVlanTopologyChangeTxPreviousPortRole.setStatus("current")
_HpicfRpvstVlanTopologyChangeTxTime_Type = DateAndTime
_HpicfRpvstVlanTopologyChangeTxTime_Object = MibTableColumn
hpicfRpvstVlanTopologyChangeTxTime = _HpicfRpvstVlanTopologyChangeTxTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 9, 1, 4),
    _HpicfRpvstVlanTopologyChangeTxTime_Type()
)
hpicfRpvstVlanTopologyChangeTxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstVlanTopologyChangeTxTime.setStatus("current")
_HpicfRpvstVlanTopologyChangeTxPortId_Type = Integer32
_HpicfRpvstVlanTopologyChangeTxPortId_Object = MibTableColumn
hpicfRpvstVlanTopologyChangeTxPortId = _HpicfRpvstVlanTopologyChangeTxPortId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 9, 1, 5),
    _HpicfRpvstVlanTopologyChangeTxPortId_Type()
)
hpicfRpvstVlanTopologyChangeTxPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstVlanTopologyChangeTxPortId.setStatus("current")
_HpicfRpvstPortRoleChangeTable_Object = MibTable
hpicfRpvstPortRoleChangeTable = _HpicfRpvstPortRoleChangeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 10)
)
if mibBuilder.loadTexts:
    hpicfRpvstPortRoleChangeTable.setStatus("current")
_HpicfRpvstPortRoleChangeEntry_Object = MibTableRow
hpicfRpvstPortRoleChangeEntry = _HpicfRpvstPortRoleChangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 10, 1)
)
hpicfRpvstPortRoleChangeEntry.setIndexNames(
    (0, "HP-ICF-RPVST-MIB", "hpicfRpvstVlanId"),
    (0, "HP-ICF-RPVST-MIB", "hpicfRpvstPortIndex"),
    (0, "HP-ICF-RPVST-MIB", "hpicfRpvstPortRoleChangeIndex"),
)
if mibBuilder.loadTexts:
    hpicfRpvstPortRoleChangeEntry.setStatus("current")


class _HpicfRpvstPortRoleChangeIndex_Type(Integer32):
    """Custom type hpicfRpvstPortRoleChangeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfRpvstPortRoleChangeIndex_Type.__name__ = "Integer32"
_HpicfRpvstPortRoleChangeIndex_Object = MibTableColumn
hpicfRpvstPortRoleChangeIndex = _HpicfRpvstPortRoleChangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 10, 1, 1),
    _HpicfRpvstPortRoleChangeIndex_Type()
)
hpicfRpvstPortRoleChangeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfRpvstPortRoleChangeIndex.setStatus("current")
_HpicfRpvstPortRoleChangeCurrentPortRole_Type = StpPortRole
_HpicfRpvstPortRoleChangeCurrentPortRole_Object = MibTableColumn
hpicfRpvstPortRoleChangeCurrentPortRole = _HpicfRpvstPortRoleChangeCurrentPortRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 10, 1, 2),
    _HpicfRpvstPortRoleChangeCurrentPortRole_Type()
)
hpicfRpvstPortRoleChangeCurrentPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortRoleChangeCurrentPortRole.setStatus("current")
_HpicfRpvstPortRoleChangePreviousPortRole_Type = StpPortRole
_HpicfRpvstPortRoleChangePreviousPortRole_Object = MibTableColumn
hpicfRpvstPortRoleChangePreviousPortRole = _HpicfRpvstPortRoleChangePreviousPortRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 10, 1, 3),
    _HpicfRpvstPortRoleChangePreviousPortRole_Type()
)
hpicfRpvstPortRoleChangePreviousPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortRoleChangePreviousPortRole.setStatus("current")
_HpicfRpvstPortRoleChangeTime_Type = DateAndTime
_HpicfRpvstPortRoleChangeTime_Object = MibTableColumn
hpicfRpvstPortRoleChangeTime = _HpicfRpvstPortRoleChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 1, 10, 1, 4),
    _HpicfRpvstPortRoleChangeTime_Type()
)
hpicfRpvstPortRoleChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRpvstPortRoleChangeTime.setStatus("current")
_HpicfRpvstConformance_ObjectIdentity = ObjectIdentity
hpicfRpvstConformance = _HpicfRpvstConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 2)
)
_HpicfRpvstGroups_ObjectIdentity = ObjectIdentity
hpicfRpvstGroups = _HpicfRpvstGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 2, 1)
)
_HpicfRpvstCompliances_ObjectIdentity = ObjectIdentity
hpicfRpvstCompliances = _HpicfRpvstCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 2, 2)
)

# Managed Objects groups

hpicfRpvstGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 2, 1, 1)
)
hpicfRpvstGroup.setObjects(
      *(("HP-ICF-RPVST-MIB", "hpicfRpvstResetCounters"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstExtendedSystemID"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstIgnorePVIDInconsistency"))
)
if mibBuilder.loadTexts:
    hpicfRpvstGroup.setStatus("current")

hpicfRpvstVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 2, 1, 2)
)
hpicfRpvstVlanGroup.setObjects(
      *(("HP-ICF-RPVST-MIB", "hpicfRpvstVlanHelloTime"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstVlanForwardDelay"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstVlanMaxAge"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstVlanPriority"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstVlanRoot"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstVlanRpvstStatus"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstVlanResetCounters"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstVlanOperHelloTime"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstVlanRootPriority"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstVlanRootPort"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstVlanRootPathCost"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstVlanRootMacAddress"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstVlanRootChangeCounter"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstVlanTimeSinceLastTopoChange"),
        ("HP-ICF-RPVST-MIB", "hpicfVlanTopoChangeCount"))
)
if mibBuilder.loadTexts:
    hpicfRpvstVlanGroup.setStatus("current")

hpicfRpvstPortVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 2, 1, 3)
)
hpicfRpvstPortVlanGroup.setObjects(
      *(("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanPathCost"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanPriority"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanResetCounters"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanRole"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanState"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanDesigBridge"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanOperPointToPoint"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanOperEdge"))
)
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanGroup.setStatus("current")

hpicfRpvstPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 2, 1, 4)
)
hpicfRpvstPortGroup.setObjects(
      *(("HP-ICF-RPVST-MIB", "hpicfRpvstPortAdminEdge"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortAdminPointToPoint"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortAutoEdge"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortBpduFiltering"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortRestrictedTcn"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortRootGuard"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortLoopGuard"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortBpduProtection"))
)
if mibBuilder.loadTexts:
    hpicfRpvstPortGroup.setStatus("deprecated")

hpicfRpvstPortVlanCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 2, 1, 5)
)
hpicfRpvstPortVlanCounterGroup.setObjects(
      *(("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanRpvstBpduRx"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanRpvstBpduRxLastUpdated"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanRpvstBpduTx"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanRpvstBpduTxLastUpdated"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanRstBpduRx"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanRstBpduRxLastUpdated"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanRstBpduTx"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanRstBpduTxLastUpdated"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanConfigBpduRx"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanConfigBpduRxLastUpdated"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanConfigBpduTx"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanConfigBpduTxLastUpdated"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanTcnBpduRx"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanTcnBpduRxLastUpdated"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanTcnBpduTx"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanTcnBpduTxLastUpdated"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanTcDetectCount"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanTcDetectCountLastUpdated"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanTcFlagRx"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanTcFlagRxLastUpdated"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanTcFlagTx"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanTcFlagTxLastUpdated"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanTcAckFlagRx"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanTcAckFlagRxLastUpdated"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanTcAckFlagTx"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanTcAckFlagTxLastUpdated"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanAgedBpduRx"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanAgedBpduRxLastUpdated"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanStarvedBpduCount"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanStarvedBpduCountLastUpdated"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanInvalidBpduRx"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanInvalidBpduRxLastUpdated"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanLoopedBackBpduRx"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanLoopedBackBpduRxLastUpdated"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanErrantBpduRxCount"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanErrantBpduRxCountLastUpdated"))
)
if mibBuilder.loadTexts:
    hpicfRpvstPortVlanCounterGroup.setStatus("current")

hpicfRpvstRootHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 2, 1, 6)
)
hpicfRpvstRootHistoryGroup.setObjects(
      *(("HP-ICF-RPVST-MIB", "hpicfRpvstVlanRootBridgeId"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstVlanRootHistoryTime"))
)
if mibBuilder.loadTexts:
    hpicfRpvstRootHistoryGroup.setStatus("current")

hpicfRpvstNotificationObjectGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 2, 1, 7)
)
hpicfRpvstNotificationObjectGrp.setObjects(
      *(("HP-ICF-RPVST-MIB", "hpicfRpvstErrantBpduDetector"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstErrantBpduSrcMac"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstVlanIndex"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortNumber"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstNewRootBridgeId"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPreviousRootBridgeId"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstDesignatedPort"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstRootBridgeChangeTimeStamp"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstSuperiorBpduSrcMac"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstSuperiorBpduSrcPort"))
)
if mibBuilder.loadTexts:
    hpicfRpvstNotificationObjectGrp.setStatus("current")

hpicfRpvstPvst1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 2, 1, 9)
)
hpicfRpvstPvst1.setObjects(
      *(("HP-ICF-RPVST-MIB", "hpicfRpvstPathCostMode"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstSendTopoChangeCtrl"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstLogPortStateTransitions"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanInconsistencyReason"))
)
if mibBuilder.loadTexts:
    hpicfRpvstPvst1.setStatus("current")

hpicfRpvstNotificationObjectGrpPvst1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 2, 1, 11)
)
hpicfRpvstNotificationObjectGrpPvst1.setObjects(
      *(("HP-ICF-RPVST-MIB", "hpicfRpvstOldPortRole"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstNewPortRole"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstTopoChangeTime"))
)
if mibBuilder.loadTexts:
    hpicfRpvstNotificationObjectGrpPvst1.setStatus("current")

hpicfRpvstTopologyRxGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 2, 1, 12)
)
hpicfRpvstTopologyRxGroup.setObjects(
      *(("HP-ICF-RPVST-MIB", "hpicfRpvstVlanTopologyChangeRxTime"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstVlanTopologyChangeRxMacAddress"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstVlanTopologyChangeRxPortId"))
)
if mibBuilder.loadTexts:
    hpicfRpvstTopologyRxGroup.setStatus("current")

hpicfRpvstTopologyTxGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 2, 1, 13)
)
hpicfRpvstTopologyTxGroup.setObjects(
      *(("HP-ICF-RPVST-MIB", "hpicfRpvstVlanTopologyChangeTxCurrentPortRole"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstVlanTopologyChangeTxPreviousPortRole"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstVlanTopologyChangeTxTime"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstVlanTopologyChangeTxPortId"))
)
if mibBuilder.loadTexts:
    hpicfRpvstTopologyTxGroup.setStatus("current")

hpicfRpvstPortRoleChangeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 2, 1, 14)
)
hpicfRpvstPortRoleChangeGroup.setObjects(
      *(("HP-ICF-RPVST-MIB", "hpicfRpvstPortRoleChangeCurrentPortRole"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortRoleChangePreviousPortRole"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortRoleChangeTime"))
)
if mibBuilder.loadTexts:
    hpicfRpvstPortRoleChangeGroup.setStatus("current")

hpicfRpvstPortGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 2, 1, 15)
)
hpicfRpvstPortGroup1.setObjects(
      *(("HP-ICF-RPVST-MIB", "hpicfRpvstPortAdminEdge"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortAdminPointToPoint"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortAutoEdge"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortBpduFiltering"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortRestrictedTcn"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortRootGuard"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortLoopGuard"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortBpduProtection"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortIeeeRstBpdu"))
)
if mibBuilder.loadTexts:
    hpicfRpvstPortGroup1.setStatus("current")


# Notification objects

hpicfRpvstErrantBpduReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 0, 11)
)
hpicfRpvstErrantBpduReceived.setObjects(
      *(("HP-ICF-RPVST-MIB", "hpicfRpvstVlanIndex"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortNumber"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanErrantBpduRxCount"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanState"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanDesigBridge"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstDesignatedPort"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstErrantBpduSrcMac"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstErrantBpduDetector"))
)
if mibBuilder.loadTexts:
    hpicfRpvstErrantBpduReceived.setStatus(
        "current"
    )

hpicfRpvstNewRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 0, 12)
)
hpicfRpvstNewRoot.setObjects(
      *(("HP-ICF-RPVST-MIB", "hpicfRpvstVlanIndex"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstNewRootBridgeId"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPreviousRootBridgeId"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstRootBridgeChangeTimeStamp"))
)
if mibBuilder.loadTexts:
    hpicfRpvstNewRoot.setStatus(
        "current"
    )

hpicfRpvstRootGuardInconsistency = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 0, 13)
)
hpicfRpvstRootGuardInconsistency.setObjects(
      *(("HP-ICF-RPVST-MIB", "hpicfRpvstVlanIndex"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortNumber"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstSuperiorBpduSrcMac"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstSuperiorBpduSrcPort"))
)
if mibBuilder.loadTexts:
    hpicfRpvstRootGuardInconsistency.setStatus(
        "current"
    )

hpicfRpvstLoopGuardInconsistency = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 0, 14)
)
hpicfRpvstLoopGuardInconsistency.setObjects(
      *(("HP-ICF-RPVST-MIB", "hpicfRpvstVlanIndex"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortNumber"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortVlanDesigBridge"))
)
if mibBuilder.loadTexts:
    hpicfRpvstLoopGuardInconsistency.setStatus(
        "current"
    )

hpicfRpvstTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 0, 18)
)
hpicfRpvstTopologyChange.setObjects(
      *(("HP-ICF-RPVST-MIB", "hpicfRpvstVlanIndex"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstPortNumber"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstOldPortRole"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstNewPortRole"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstTopoChangeTime"))
)
if mibBuilder.loadTexts:
    hpicfRpvstTopologyChange.setStatus(
        "current"
    )


# Notifications groups

hpicfRpvstNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 2, 1, 8)
)
hpicfRpvstNotificationGroup.setObjects(
      *(("HP-ICF-RPVST-MIB", "hpicfRpvstErrantBpduReceived"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstNewRoot"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstRootGuardInconsistency"),
        ("HP-ICF-RPVST-MIB", "hpicfRpvstLoopGuardInconsistency"))
)
if mibBuilder.loadTexts:
    hpicfRpvstNotificationGroup.setStatus(
        "current"
    )

hpicfRpvstNotificationGroupPvst1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 2, 1, 10)
)
hpicfRpvstNotificationGroupPvst1.setObjects(
    ("HP-ICF-RPVST-MIB", "hpicfRpvstTopologyChange")
)
if mibBuilder.loadTexts:
    hpicfRpvstNotificationGroupPvst1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicfRpvstCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfRpvstCompliance1.setStatus(
        "deprecated"
    )

hpicfRpvstCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hpicfRpvstCompliance2.setStatus(
        "current"
    )

hpicfRpvstCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88, 2, 2, 3)
)
if mibBuilder.loadTexts:
    hpicfRpvstCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-RPVST-MIB",
    **{"PointToPoint": PointToPoint,
       "hpicfRpvstMIB": hpicfRpvstMIB,
       "hpicfRpvstNotifications": hpicfRpvstNotifications,
       "hpicfRpvstErrantBpduDetector": hpicfRpvstErrantBpduDetector,
       "hpicfRpvstErrantBpduSrcMac": hpicfRpvstErrantBpduSrcMac,
       "hpicfRpvstNewRootBridgeId": hpicfRpvstNewRootBridgeId,
       "hpicfRpvstPreviousRootBridgeId": hpicfRpvstPreviousRootBridgeId,
       "hpicfRpvstDesignatedPort": hpicfRpvstDesignatedPort,
       "hpicfRpvstVlanIndex": hpicfRpvstVlanIndex,
       "hpicfRpvstPortNumber": hpicfRpvstPortNumber,
       "hpicfRpvstRootBridgeChangeTimeStamp": hpicfRpvstRootBridgeChangeTimeStamp,
       "hpicfRpvstSuperiorBpduSrcMac": hpicfRpvstSuperiorBpduSrcMac,
       "hpicfRpvstSuperiorBpduSrcPort": hpicfRpvstSuperiorBpduSrcPort,
       "hpicfRpvstErrantBpduReceived": hpicfRpvstErrantBpduReceived,
       "hpicfRpvstNewRoot": hpicfRpvstNewRoot,
       "hpicfRpvstRootGuardInconsistency": hpicfRpvstRootGuardInconsistency,
       "hpicfRpvstLoopGuardInconsistency": hpicfRpvstLoopGuardInconsistency,
       "hpicfRpvstOldPortRole": hpicfRpvstOldPortRole,
       "hpicfRpvstNewPortRole": hpicfRpvstNewPortRole,
       "hpicfRpvstTopoChangeTime": hpicfRpvstTopoChangeTime,
       "hpicfRpvstTopologyChange": hpicfRpvstTopologyChange,
       "hpicfRpvstObjects": hpicfRpvstObjects,
       "hpicfRpvstGeneralGroup": hpicfRpvstGeneralGroup,
       "hpicfRpvstResetCounters": hpicfRpvstResetCounters,
       "hpicfRpvstExtendedSystemID": hpicfRpvstExtendedSystemID,
       "hpicfRpvstIgnorePVIDInconsistency": hpicfRpvstIgnorePVIDInconsistency,
       "hpicfRpvstPathCostMode": hpicfRpvstPathCostMode,
       "hpicfRpvstVlanTable": hpicfRpvstVlanTable,
       "hpicfRpvstVlanEntry": hpicfRpvstVlanEntry,
       "hpicfRpvstVlanId": hpicfRpvstVlanId,
       "hpicfRpvstVlanHelloTime": hpicfRpvstVlanHelloTime,
       "hpicfRpvstVlanForwardDelay": hpicfRpvstVlanForwardDelay,
       "hpicfRpvstVlanMaxAge": hpicfRpvstVlanMaxAge,
       "hpicfRpvstVlanPriority": hpicfRpvstVlanPriority,
       "hpicfRpvstVlanRoot": hpicfRpvstVlanRoot,
       "hpicfRpvstVlanRpvstStatus": hpicfRpvstVlanRpvstStatus,
       "hpicfRpvstVlanResetCounters": hpicfRpvstVlanResetCounters,
       "hpicfRpvstVlanOperHelloTime": hpicfRpvstVlanOperHelloTime,
       "hpicfRpvstVlanRootPriority": hpicfRpvstVlanRootPriority,
       "hpicfRpvstVlanRootPort": hpicfRpvstVlanRootPort,
       "hpicfRpvstVlanRootPathCost": hpicfRpvstVlanRootPathCost,
       "hpicfRpvstVlanRootMacAddress": hpicfRpvstVlanRootMacAddress,
       "hpicfRpvstVlanRootChangeCounter": hpicfRpvstVlanRootChangeCounter,
       "hpicfRpvstVlanTimeSinceLastTopoChange": hpicfRpvstVlanTimeSinceLastTopoChange,
       "hpicfVlanTopoChangeCount": hpicfVlanTopoChangeCount,
       "hpicfRpvstSendTopoChangeCtrl": hpicfRpvstSendTopoChangeCtrl,
       "hpicfRpvstLogPortStateTransitions": hpicfRpvstLogPortStateTransitions,
       "hpicfRpvstPortTable": hpicfRpvstPortTable,
       "hpicfRpvstPortEntry": hpicfRpvstPortEntry,
       "hpicfRpvstPortIndex": hpicfRpvstPortIndex,
       "hpicfRpvstPortAdminEdge": hpicfRpvstPortAdminEdge,
       "hpicfRpvstPortAdminPointToPoint": hpicfRpvstPortAdminPointToPoint,
       "hpicfRpvstPortAutoEdge": hpicfRpvstPortAutoEdge,
       "hpicfRpvstPortBpduFiltering": hpicfRpvstPortBpduFiltering,
       "hpicfRpvstPortRestrictedTcn": hpicfRpvstPortRestrictedTcn,
       "hpicfRpvstPortRootGuard": hpicfRpvstPortRootGuard,
       "hpicfRpvstPortLoopGuard": hpicfRpvstPortLoopGuard,
       "hpicfRpvstPortBpduProtection": hpicfRpvstPortBpduProtection,
       "hpicfRpvstPortIeeeRstBpdu": hpicfRpvstPortIeeeRstBpdu,
       "hpicfRpvstPortVlanTable": hpicfRpvstPortVlanTable,
       "hpicfRpvstPortVlanEntry": hpicfRpvstPortVlanEntry,
       "hpicfRpvstPortVlanPathCost": hpicfRpvstPortVlanPathCost,
       "hpicfRpvstPortVlanPriority": hpicfRpvstPortVlanPriority,
       "hpicfRpvstPortVlanResetCounters": hpicfRpvstPortVlanResetCounters,
       "hpicfRpvstPortVlanRole": hpicfRpvstPortVlanRole,
       "hpicfRpvstPortVlanState": hpicfRpvstPortVlanState,
       "hpicfRpvstPortVlanDesigBridge": hpicfRpvstPortVlanDesigBridge,
       "hpicfRpvstPortVlanOperPointToPoint": hpicfRpvstPortVlanOperPointToPoint,
       "hpicfRpvstPortVlanOperEdge": hpicfRpvstPortVlanOperEdge,
       "hpicfRpvstPortVlanInconsistencyReason": hpicfRpvstPortVlanInconsistencyReason,
       "hpicfRpvstPortVlanRxCountersTable": hpicfRpvstPortVlanRxCountersTable,
       "hpicfRpvstPortVlanRxCountersEntry": hpicfRpvstPortVlanRxCountersEntry,
       "hpicfRpvstPortVlanRpvstBpduRx": hpicfRpvstPortVlanRpvstBpduRx,
       "hpicfRpvstPortVlanRpvstBpduRxLastUpdated": hpicfRpvstPortVlanRpvstBpduRxLastUpdated,
       "hpicfRpvstPortVlanRstBpduRx": hpicfRpvstPortVlanRstBpduRx,
       "hpicfRpvstPortVlanRstBpduRxLastUpdated": hpicfRpvstPortVlanRstBpduRxLastUpdated,
       "hpicfRpvstPortVlanConfigBpduRx": hpicfRpvstPortVlanConfigBpduRx,
       "hpicfRpvstPortVlanConfigBpduRxLastUpdated": hpicfRpvstPortVlanConfigBpduRxLastUpdated,
       "hpicfRpvstPortVlanTcnBpduRx": hpicfRpvstPortVlanTcnBpduRx,
       "hpicfRpvstPortVlanTcnBpduRxLastUpdated": hpicfRpvstPortVlanTcnBpduRxLastUpdated,
       "hpicfRpvstPortVlanTcDetectCount": hpicfRpvstPortVlanTcDetectCount,
       "hpicfRpvstPortVlanTcDetectCountLastUpdated": hpicfRpvstPortVlanTcDetectCountLastUpdated,
       "hpicfRpvstPortVlanTcFlagRx": hpicfRpvstPortVlanTcFlagRx,
       "hpicfRpvstPortVlanTcFlagRxLastUpdated": hpicfRpvstPortVlanTcFlagRxLastUpdated,
       "hpicfRpvstPortVlanTcAckFlagRx": hpicfRpvstPortVlanTcAckFlagRx,
       "hpicfRpvstPortVlanTcAckFlagRxLastUpdated": hpicfRpvstPortVlanTcAckFlagRxLastUpdated,
       "hpicfRpvstPortVlanStarvedBpduCount": hpicfRpvstPortVlanStarvedBpduCount,
       "hpicfRpvstPortVlanStarvedBpduCountLastUpdated": hpicfRpvstPortVlanStarvedBpduCountLastUpdated,
       "hpicfRpvstPortVlanInvalidBpduRx": hpicfRpvstPortVlanInvalidBpduRx,
       "hpicfRpvstPortVlanInvalidBpduRxLastUpdated": hpicfRpvstPortVlanInvalidBpduRxLastUpdated,
       "hpicfRpvstPortVlanLoopedBackBpduRx": hpicfRpvstPortVlanLoopedBackBpduRx,
       "hpicfRpvstPortVlanLoopedBackBpduRxLastUpdated": hpicfRpvstPortVlanLoopedBackBpduRxLastUpdated,
       "hpicfRpvstPortVlanErrantBpduRxCount": hpicfRpvstPortVlanErrantBpduRxCount,
       "hpicfRpvstPortVlanErrantBpduRxCountLastUpdated": hpicfRpvstPortVlanErrantBpduRxCountLastUpdated,
       "hpicfRpvstPortVlanAgedBpduRx": hpicfRpvstPortVlanAgedBpduRx,
       "hpicfRpvstPortVlanAgedBpduRxLastUpdated": hpicfRpvstPortVlanAgedBpduRxLastUpdated,
       "hpicfRpvstPortVlanTxCountersTable": hpicfRpvstPortVlanTxCountersTable,
       "hpicfRpvstPortVlanTxCountersEntry": hpicfRpvstPortVlanTxCountersEntry,
       "hpicfRpvstPortVlanRpvstBpduTx": hpicfRpvstPortVlanRpvstBpduTx,
       "hpicfRpvstPortVlanRpvstBpduTxLastUpdated": hpicfRpvstPortVlanRpvstBpduTxLastUpdated,
       "hpicfRpvstPortVlanRstBpduTx": hpicfRpvstPortVlanRstBpduTx,
       "hpicfRpvstPortVlanRstBpduTxLastUpdated": hpicfRpvstPortVlanRstBpduTxLastUpdated,
       "hpicfRpvstPortVlanConfigBpduTx": hpicfRpvstPortVlanConfigBpduTx,
       "hpicfRpvstPortVlanConfigBpduTxLastUpdated": hpicfRpvstPortVlanConfigBpduTxLastUpdated,
       "hpicfRpvstPortVlanTcnBpduTx": hpicfRpvstPortVlanTcnBpduTx,
       "hpicfRpvstPortVlanTcnBpduTxLastUpdated": hpicfRpvstPortVlanTcnBpduTxLastUpdated,
       "hpicfRpvstPortVlanTcFlagTx": hpicfRpvstPortVlanTcFlagTx,
       "hpicfRpvstPortVlanTcFlagTxLastUpdated": hpicfRpvstPortVlanTcFlagTxLastUpdated,
       "hpicfRpvstPortVlanTcAckFlagTx": hpicfRpvstPortVlanTcAckFlagTx,
       "hpicfRpvstPortVlanTcAckFlagTxLastUpdated": hpicfRpvstPortVlanTcAckFlagTxLastUpdated,
       "hpicfRpvstVlanRootHistoryTable": hpicfRpvstVlanRootHistoryTable,
       "hpicfRpvstVlanRootHistoryEntry": hpicfRpvstVlanRootHistoryEntry,
       "hpicfRpvstVlanRootHistoryIndex": hpicfRpvstVlanRootHistoryIndex,
       "hpicfRpvstVlanRootBridgeId": hpicfRpvstVlanRootBridgeId,
       "hpicfRpvstVlanRootHistoryTime": hpicfRpvstVlanRootHistoryTime,
       "hpicfRpvstVlanTopologyChangeRxTable": hpicfRpvstVlanTopologyChangeRxTable,
       "hpicfRpvstVlanTopologyChangeRxEntry": hpicfRpvstVlanTopologyChangeRxEntry,
       "hpicfRpvstVlanTopologyChangeRxIndex": hpicfRpvstVlanTopologyChangeRxIndex,
       "hpicfRpvstVlanTopologyChangeRxTime": hpicfRpvstVlanTopologyChangeRxTime,
       "hpicfRpvstVlanTopologyChangeRxMacAddress": hpicfRpvstVlanTopologyChangeRxMacAddress,
       "hpicfRpvstVlanTopologyChangeRxPortId": hpicfRpvstVlanTopologyChangeRxPortId,
       "hpicfRpvstVlanTopologyChangeTxTable": hpicfRpvstVlanTopologyChangeTxTable,
       "hpicfRpvstVlanTopologyChangeTxEntry": hpicfRpvstVlanTopologyChangeTxEntry,
       "hpicfRpvstVlanTopologyChangeTxIndex": hpicfRpvstVlanTopologyChangeTxIndex,
       "hpicfRpvstVlanTopologyChangeTxCurrentPortRole": hpicfRpvstVlanTopologyChangeTxCurrentPortRole,
       "hpicfRpvstVlanTopologyChangeTxPreviousPortRole": hpicfRpvstVlanTopologyChangeTxPreviousPortRole,
       "hpicfRpvstVlanTopologyChangeTxTime": hpicfRpvstVlanTopologyChangeTxTime,
       "hpicfRpvstVlanTopologyChangeTxPortId": hpicfRpvstVlanTopologyChangeTxPortId,
       "hpicfRpvstPortRoleChangeTable": hpicfRpvstPortRoleChangeTable,
       "hpicfRpvstPortRoleChangeEntry": hpicfRpvstPortRoleChangeEntry,
       "hpicfRpvstPortRoleChangeIndex": hpicfRpvstPortRoleChangeIndex,
       "hpicfRpvstPortRoleChangeCurrentPortRole": hpicfRpvstPortRoleChangeCurrentPortRole,
       "hpicfRpvstPortRoleChangePreviousPortRole": hpicfRpvstPortRoleChangePreviousPortRole,
       "hpicfRpvstPortRoleChangeTime": hpicfRpvstPortRoleChangeTime,
       "hpicfRpvstConformance": hpicfRpvstConformance,
       "hpicfRpvstGroups": hpicfRpvstGroups,
       "hpicfRpvstGroup": hpicfRpvstGroup,
       "hpicfRpvstVlanGroup": hpicfRpvstVlanGroup,
       "hpicfRpvstPortVlanGroup": hpicfRpvstPortVlanGroup,
       "hpicfRpvstPortGroup": hpicfRpvstPortGroup,
       "hpicfRpvstPortVlanCounterGroup": hpicfRpvstPortVlanCounterGroup,
       "hpicfRpvstRootHistoryGroup": hpicfRpvstRootHistoryGroup,
       "hpicfRpvstNotificationObjectGrp": hpicfRpvstNotificationObjectGrp,
       "hpicfRpvstNotificationGroup": hpicfRpvstNotificationGroup,
       "hpicfRpvstPvst1": hpicfRpvstPvst1,
       "hpicfRpvstNotificationGroupPvst1": hpicfRpvstNotificationGroupPvst1,
       "hpicfRpvstNotificationObjectGrpPvst1": hpicfRpvstNotificationObjectGrpPvst1,
       "hpicfRpvstTopologyRxGroup": hpicfRpvstTopologyRxGroup,
       "hpicfRpvstTopologyTxGroup": hpicfRpvstTopologyTxGroup,
       "hpicfRpvstPortRoleChangeGroup": hpicfRpvstPortRoleChangeGroup,
       "hpicfRpvstPortGroup1": hpicfRpvstPortGroup1,
       "hpicfRpvstCompliances": hpicfRpvstCompliances,
       "hpicfRpvstCompliance1": hpicfRpvstCompliance1,
       "hpicfRpvstCompliance2": hpicfRpvstCompliance2,
       "hpicfRpvstCompliance3": hpicfRpvstCompliance3}
)
