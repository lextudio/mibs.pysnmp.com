# SNMP MIB module (ALCATEL-IND1-VLAN-STP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-VLAN-STP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:07 2024
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

(softentIND1VlanStp,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1VlanStp")

(BridgeId,
 Timeout) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "Timeout")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1VLANSTPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1)
)
alcatelIND1VLANSTPMIB.setRevisions(
        ("2010-05-13 00:00",)
)


# Types definitions



class DigestId(OctetString):
    """Custom type DigestId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )




# TEXTUAL-CONVENTIONS



class VlanBitmap(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_AlcatelIND1VLANSTPMIBNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1VLANSTPMIBNotifications = _AlcatelIND1VLANSTPMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 0)
)
if mibBuilder.loadTexts:
    alcatelIND1VLANSTPMIBNotifications.setStatus("current")
_AlcatelIND1VLANSTPMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1VLANSTPMIBObjects = _AlcatelIND1VLANSTPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1VLANSTPMIBObjects.setStatus("current")
_VStpInfo_ObjectIdentity = ObjectIdentity
vStpInfo = _VStpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1)
)
_VStpInsTable_Object = MibTable
vStpInsTable = _VStpInsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    vStpInsTable.setStatus("current")
_VStpInsEntry_Object = MibTableRow
vStpInsEntry = _VStpInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 1, 1)
)
vStpInsEntry.setIndexNames(
    (0, "ALCATEL-IND1-VLAN-STP-MIB", "vStpInsBridgeMode"),
    (0, "ALCATEL-IND1-VLAN-STP-MIB", "vStpInsNumber"),
)
if mibBuilder.loadTexts:
    vStpInsEntry.setStatus("current")


class _VStpInsBridgeMode_Type(Integer32):
    """Custom type vStpInsBridgeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flat", 1),
          ("onePerVlan", 2))
    )


_VStpInsBridgeMode_Type.__name__ = "Integer32"
_VStpInsBridgeMode_Object = MibTableColumn
vStpInsBridgeMode = _VStpInsBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 1, 1, 1),
    _VStpInsBridgeMode_Type()
)
vStpInsBridgeMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vStpInsBridgeMode.setStatus("current")


class _VStpInsNumber_Type(Integer32):
    """Custom type vStpInsNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_VStpInsNumber_Type.__name__ = "Integer32"
_VStpInsNumber_Object = MibTableColumn
vStpInsNumber = _VStpInsNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 1, 1, 2),
    _VStpInsNumber_Type()
)
vStpInsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpInsNumber.setStatus("current")


class _VStpInsProtocolSpecification_Type(Integer32):
    """Custom type vStpInsProtocolSpecification based on Integer32"""
    defaultValue = 3

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
        *(("decLb100", 2),
          ("ieeeMSTP", 5),
          ("ieeeRSTP", 4),
          ("ieeeSTP", 3),
          ("unknown", 1))
    )


_VStpInsProtocolSpecification_Type.__name__ = "Integer32"
_VStpInsProtocolSpecification_Object = MibTableColumn
vStpInsProtocolSpecification = _VStpInsProtocolSpecification_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 1, 1, 3),
    _VStpInsProtocolSpecification_Type()
)
vStpInsProtocolSpecification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpInsProtocolSpecification.setStatus("current")


class _VStpInsPriority_Type(Integer32):
    """Custom type vStpInsPriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VStpInsPriority_Type.__name__ = "Integer32"
_VStpInsPriority_Object = MibTableColumn
vStpInsPriority = _VStpInsPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 1, 1, 4),
    _VStpInsPriority_Type()
)
vStpInsPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpInsPriority.setStatus("current")
_VStpInsBridgeAddress_Type = BridgeId
_VStpInsBridgeAddress_Object = MibTableColumn
vStpInsBridgeAddress = _VStpInsBridgeAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 1, 1, 5),
    _VStpInsBridgeAddress_Type()
)
vStpInsBridgeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpInsBridgeAddress.setStatus("current")
_VStpInsTimeSinceTopologyChange_Type = TimeTicks
_VStpInsTimeSinceTopologyChange_Object = MibTableColumn
vStpInsTimeSinceTopologyChange = _VStpInsTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 1, 1, 6),
    _VStpInsTimeSinceTopologyChange_Type()
)
vStpInsTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpInsTimeSinceTopologyChange.setStatus("current")
_VStpInsTopChanges_Type = Counter32
_VStpInsTopChanges_Object = MibTableColumn
vStpInsTopChanges = _VStpInsTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 1, 1, 7),
    _VStpInsTopChanges_Type()
)
vStpInsTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpInsTopChanges.setStatus("current")
_VStpInsDesignatedRoot_Type = BridgeId
_VStpInsDesignatedRoot_Object = MibTableColumn
vStpInsDesignatedRoot = _VStpInsDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 1, 1, 8),
    _VStpInsDesignatedRoot_Type()
)
vStpInsDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpInsDesignatedRoot.setStatus("current")
_VStpInsRootCost_Type = Integer32
_VStpInsRootCost_Object = MibTableColumn
vStpInsRootCost = _VStpInsRootCost_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 1, 1, 9),
    _VStpInsRootCost_Type()
)
vStpInsRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpInsRootCost.setStatus("current")
_VStpInsRootPortNumber_Type = Integer32
_VStpInsRootPortNumber_Object = MibTableColumn
vStpInsRootPortNumber = _VStpInsRootPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 1, 1, 10),
    _VStpInsRootPortNumber_Type()
)
vStpInsRootPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpInsRootPortNumber.setStatus("current")
_VStpInsNextBestRootCost_Type = Integer32
_VStpInsNextBestRootCost_Object = MibTableColumn
vStpInsNextBestRootCost = _VStpInsNextBestRootCost_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 1, 1, 11),
    _VStpInsNextBestRootCost_Type()
)
vStpInsNextBestRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpInsNextBestRootCost.setStatus("current")
_VStpInsNextBestRootPortNumber_Type = Integer32
_VStpInsNextBestRootPortNumber_Object = MibTableColumn
vStpInsNextBestRootPortNumber = _VStpInsNextBestRootPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 1, 1, 12),
    _VStpInsNextBestRootPortNumber_Type()
)
vStpInsNextBestRootPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpInsNextBestRootPortNumber.setStatus("current")
_VStpInsMaxAge_Type = Timeout
_VStpInsMaxAge_Object = MibTableColumn
vStpInsMaxAge = _VStpInsMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 1, 1, 13),
    _VStpInsMaxAge_Type()
)
vStpInsMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpInsMaxAge.setStatus("current")
_VStpInsHelloTime_Type = Timeout
_VStpInsHelloTime_Object = MibTableColumn
vStpInsHelloTime = _VStpInsHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 1, 1, 14),
    _VStpInsHelloTime_Type()
)
vStpInsHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpInsHelloTime.setStatus("current")
_VStpInsHoldTime_Type = Integer32
_VStpInsHoldTime_Object = MibTableColumn
vStpInsHoldTime = _VStpInsHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 1, 1, 15),
    _VStpInsHoldTime_Type()
)
vStpInsHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpInsHoldTime.setStatus("current")
_VStpInsForwardDelay_Type = Integer32
_VStpInsForwardDelay_Object = MibTableColumn
vStpInsForwardDelay = _VStpInsForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 1, 1, 16),
    _VStpInsForwardDelay_Type()
)
vStpInsForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpInsForwardDelay.setStatus("current")


class _VStpInsBridgeMaxAge_Type(Timeout):
    """Custom type vStpInsBridgeMaxAge based on Timeout"""
    defaultValue = 2000

    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_VStpInsBridgeMaxAge_Type.__name__ = "Timeout"
_VStpInsBridgeMaxAge_Object = MibTableColumn
vStpInsBridgeMaxAge = _VStpInsBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 1, 1, 17),
    _VStpInsBridgeMaxAge_Type()
)
vStpInsBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpInsBridgeMaxAge.setStatus("current")


class _VStpInsBridgeHelloTime_Type(Timeout):
    """Custom type vStpInsBridgeHelloTime based on Timeout"""
    defaultValue = 200

    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_VStpInsBridgeHelloTime_Type.__name__ = "Timeout"
_VStpInsBridgeHelloTime_Object = MibTableColumn
vStpInsBridgeHelloTime = _VStpInsBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 1, 1, 18),
    _VStpInsBridgeHelloTime_Type()
)
vStpInsBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpInsBridgeHelloTime.setStatus("current")


class _VStpInsBridgeForwardDelay_Type(Timeout):
    """Custom type vStpInsBridgeForwardDelay based on Timeout"""
    defaultValue = 1500

    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_VStpInsBridgeForwardDelay_Type.__name__ = "Timeout"
_VStpInsBridgeForwardDelay_Object = MibTableColumn
vStpInsBridgeForwardDelay = _VStpInsBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 1, 1, 19),
    _VStpInsBridgeForwardDelay_Type()
)
vStpInsBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpInsBridgeForwardDelay.setStatus("current")


class _VStpInsBpduSwitching_Type(Integer32):
    """Custom type vStpInsBpduSwitching based on Integer32"""
    defaultValue = 2

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


_VStpInsBpduSwitching_Type.__name__ = "Integer32"
_VStpInsBpduSwitching_Object = MibTableColumn
vStpInsBpduSwitching = _VStpInsBpduSwitching_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 1, 1, 20),
    _VStpInsBpduSwitching_Type()
)
vStpInsBpduSwitching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpInsBpduSwitching.setStatus("current")
_VStpInsCistRegionalRootId_Type = BridgeId
_VStpInsCistRegionalRootId_Object = MibTableColumn
vStpInsCistRegionalRootId = _VStpInsCistRegionalRootId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 1, 1, 21),
    _VStpInsCistRegionalRootId_Type()
)
vStpInsCistRegionalRootId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpInsCistRegionalRootId.setStatus("current")
_VStpInsCistPathCost_Type = Integer32
_VStpInsCistPathCost_Object = MibTableColumn
vStpInsCistPathCost = _VStpInsCistPathCost_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 1, 1, 22),
    _VStpInsCistPathCost_Type()
)
vStpInsCistPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpInsCistPathCost.setStatus("current")
_VStpIns1x1VlanNumber_Type = Integer32
_VStpIns1x1VlanNumber_Object = MibTableColumn
vStpIns1x1VlanNumber = _VStpIns1x1VlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 1, 1, 23),
    _VStpIns1x1VlanNumber_Type()
)
vStpIns1x1VlanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpIns1x1VlanNumber.setStatus("current")
_VStpInsMstiNumber_Type = Integer32
_VStpInsMstiNumber_Object = MibTableColumn
vStpInsMstiNumber = _VStpInsMstiNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 1, 1, 24),
    _VStpInsMstiNumber_Type()
)
vStpInsMstiNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpInsMstiNumber.setStatus("current")


class _VStpInsMode_Type(Integer32):
    """Custom type vStpInsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flat", 1),
          ("onePerVlan", 2))
    )


_VStpInsMode_Type.__name__ = "Integer32"
_VStpInsMode_Object = MibTableColumn
vStpInsMode = _VStpInsMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 1, 1, 25),
    _VStpInsMode_Type()
)
vStpInsMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpInsMode.setStatus("current")


class _VStpInsAutoVlanContainment_Type(Integer32):
    """Custom type vStpInsAutoVlanContainment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_VStpInsAutoVlanContainment_Type.__name__ = "Integer32"
_VStpInsAutoVlanContainment_Object = MibTableColumn
vStpInsAutoVlanContainment = _VStpInsAutoVlanContainment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 1, 1, 26),
    _VStpInsAutoVlanContainment_Type()
)
vStpInsAutoVlanContainment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpInsAutoVlanContainment.setStatus("current")


class _VStpInsBridgeTxHoldCount_Type(Integer32):
    """Custom type vStpInsBridgeTxHoldCount based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_VStpInsBridgeTxHoldCount_Type.__name__ = "Integer32"
_VStpInsBridgeTxHoldCount_Object = MibTableColumn
vStpInsBridgeTxHoldCount = _VStpInsBridgeTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 1, 1, 27),
    _VStpInsBridgeTxHoldCount_Type()
)
vStpInsBridgeTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpInsBridgeTxHoldCount.setStatus("current")


class _VStpInsAdminState_Type(Integer32):
    """Custom type vStpInsAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notapplicable", 0))
    )


_VStpInsAdminState_Type.__name__ = "Integer32"
_VStpInsAdminState_Object = MibTableColumn
vStpInsAdminState = _VStpInsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 1, 1, 28),
    _VStpInsAdminState_Type()
)
vStpInsAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpInsAdminState.setStatus("current")
_VStpInsPortTable_Object = MibTable
vStpInsPortTable = _VStpInsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    vStpInsPortTable.setStatus("current")
_VStpInsPortEntry_Object = MibTableRow
vStpInsPortEntry = _VStpInsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 2, 1)
)
vStpInsPortEntry.setIndexNames(
    (0, "ALCATEL-IND1-VLAN-STP-MIB", "vStpInsBridgeMode"),
    (0, "ALCATEL-IND1-VLAN-STP-MIB", "vStpInsNumber"),
    (0, "ALCATEL-IND1-VLAN-STP-MIB", "vStpInsPortNumber"),
)
if mibBuilder.loadTexts:
    vStpInsPortEntry.setStatus("current")


class _VStpInsPortNumber_Type(Integer32):
    """Custom type vStpInsPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VStpInsPortNumber_Type.__name__ = "Integer32"
_VStpInsPortNumber_Object = MibTableColumn
vStpInsPortNumber = _VStpInsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 2, 1, 1),
    _VStpInsPortNumber_Type()
)
vStpInsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpInsPortNumber.setStatus("current")


class _VStpInsPortPriority_Type(Integer32):
    """Custom type vStpInsPortPriority based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_VStpInsPortPriority_Type.__name__ = "Integer32"
_VStpInsPortPriority_Object = MibTableColumn
vStpInsPortPriority = _VStpInsPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 2, 1, 2),
    _VStpInsPortPriority_Type()
)
vStpInsPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpInsPortPriority.setStatus("current")


class _VStpInsPortState_Type(Integer32):
    """Custom type vStpInsPortState based on Integer32"""
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
        *(("blocking", 2),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_VStpInsPortState_Type.__name__ = "Integer32"
_VStpInsPortState_Object = MibTableColumn
vStpInsPortState = _VStpInsPortState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 2, 1, 3),
    _VStpInsPortState_Type()
)
vStpInsPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpInsPortState.setStatus("current")


class _VStpInsPortEnable_Type(Integer32):
    """Custom type vStpInsPortEnable based on Integer32"""
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


_VStpInsPortEnable_Type.__name__ = "Integer32"
_VStpInsPortEnable_Object = MibTableColumn
vStpInsPortEnable = _VStpInsPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 2, 1, 4),
    _VStpInsPortEnable_Type()
)
vStpInsPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpInsPortEnable.setStatus("current")


class _VStpInsPortPathCost_Type(Integer32):
    """Custom type vStpInsPortPathCost based on Integer32"""
    defaultValue = 0


_VStpInsPortPathCost_Object = MibTableColumn
vStpInsPortPathCost = _VStpInsPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 2, 1, 5),
    _VStpInsPortPathCost_Type()
)
vStpInsPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpInsPortPathCost.setStatus("current")
_VStpInsPortDesignatedRoot_Type = BridgeId
_VStpInsPortDesignatedRoot_Object = MibTableColumn
vStpInsPortDesignatedRoot = _VStpInsPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 2, 1, 6),
    _VStpInsPortDesignatedRoot_Type()
)
vStpInsPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpInsPortDesignatedRoot.setStatus("current")
_VStpInsPortDesignatedCost_Type = Integer32
_VStpInsPortDesignatedCost_Object = MibTableColumn
vStpInsPortDesignatedCost = _VStpInsPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 2, 1, 7),
    _VStpInsPortDesignatedCost_Type()
)
vStpInsPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpInsPortDesignatedCost.setStatus("current")
_VStpInsPortDesignatedBridge_Type = BridgeId
_VStpInsPortDesignatedBridge_Object = MibTableColumn
vStpInsPortDesignatedBridge = _VStpInsPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 2, 1, 8),
    _VStpInsPortDesignatedBridge_Type()
)
vStpInsPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpInsPortDesignatedBridge.setStatus("current")
_VStpInsPortDesignatedPtPrio_Type = Integer32
_VStpInsPortDesignatedPtPrio_Object = MibTableColumn
vStpInsPortDesignatedPtPrio = _VStpInsPortDesignatedPtPrio_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 2, 1, 9),
    _VStpInsPortDesignatedPtPrio_Type()
)
vStpInsPortDesignatedPtPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpInsPortDesignatedPtPrio.setStatus("current")
_VStpInsPortDesignatedPtNumber_Type = Integer32
_VStpInsPortDesignatedPtNumber_Object = MibTableColumn
vStpInsPortDesignatedPtNumber = _VStpInsPortDesignatedPtNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 2, 1, 10),
    _VStpInsPortDesignatedPtNumber_Type()
)
vStpInsPortDesignatedPtNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpInsPortDesignatedPtNumber.setStatus("current")
_VStpInsPortForwardTransitions_Type = Integer32
_VStpInsPortForwardTransitions_Object = MibTableColumn
vStpInsPortForwardTransitions = _VStpInsPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 2, 1, 11),
    _VStpInsPortForwardTransitions_Type()
)
vStpInsPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpInsPortForwardTransitions.setStatus("current")


class _VStpInsPortManualMode_Type(Integer32):
    """Custom type vStpInsPortManualMode based on Integer32"""
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
        *(("blocking", 2),
          ("forwarding", 3),
          ("no", 1))
    )


_VStpInsPortManualMode_Type.__name__ = "Integer32"
_VStpInsPortManualMode_Object = MibTableColumn
vStpInsPortManualMode = _VStpInsPortManualMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 2, 1, 12),
    _VStpInsPortManualMode_Type()
)
vStpInsPortManualMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpInsPortManualMode.setStatus("current")


class _VStpInsPortRole_Type(Integer32):
    """Custom type vStpInsPortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 3),
          ("backup", 4),
          ("designated", 2),
          ("disabled", 5),
          ("master", 6),
          ("root", 1))
    )


_VStpInsPortRole_Type.__name__ = "Integer32"
_VStpInsPortRole_Object = MibTableColumn
vStpInsPortRole = _VStpInsPortRole_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 2, 1, 13),
    _VStpInsPortRole_Type()
)
vStpInsPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpInsPortRole.setStatus("current")
_VStpInsPortPrimaryPortNumber_Type = Integer32
_VStpInsPortPrimaryPortNumber_Object = MibTableColumn
vStpInsPortPrimaryPortNumber = _VStpInsPortPrimaryPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 2, 1, 14),
    _VStpInsPortPrimaryPortNumber_Type()
)
vStpInsPortPrimaryPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpInsPortPrimaryPortNumber.setStatus("current")


class _VStpInsPortAdminConnectionType_Type(Integer32):
    """Custom type vStpInsPortAdminConnectionType based on Integer32"""
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
        *(("autopointtopoint", 3),
          ("edgeport", 4),
          ("nopointtopoint", 1),
          ("pointtopoint", 2))
    )


_VStpInsPortAdminConnectionType_Type.__name__ = "Integer32"
_VStpInsPortAdminConnectionType_Object = MibTableColumn
vStpInsPortAdminConnectionType = _VStpInsPortAdminConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 2, 1, 15),
    _VStpInsPortAdminConnectionType_Type()
)
vStpInsPortAdminConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpInsPortAdminConnectionType.setStatus("current")


class _VStpInsPortOperConnectionType_Type(Integer32):
    """Custom type vStpInsPortOperConnectionType based on Integer32"""
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
        *(("edgeport", 4),
          ("nonsignificant", 3),
          ("nopointtopoint", 1),
          ("pointtopoint", 2))
    )


_VStpInsPortOperConnectionType_Type.__name__ = "Integer32"
_VStpInsPortOperConnectionType_Object = MibTableColumn
vStpInsPortOperConnectionType = _VStpInsPortOperConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 2, 1, 16),
    _VStpInsPortOperConnectionType_Type()
)
vStpInsPortOperConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpInsPortOperConnectionType.setStatus("current")
_VStpInsPortCistRegionRootId_Type = BridgeId
_VStpInsPortCistRegionRootId_Object = MibTableColumn
vStpInsPortCistRegionRootId = _VStpInsPortCistRegionRootId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 2, 1, 17),
    _VStpInsPortCistRegionRootId_Type()
)
vStpInsPortCistRegionRootId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpInsPortCistRegionRootId.setStatus("current")
_VStpInsPortCistPathCost_Type = Integer32
_VStpInsPortCistPathCost_Object = MibTableColumn
vStpInsPortCistPathCost = _VStpInsPortCistPathCost_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 2, 1, 18),
    _VStpInsPortCistPathCost_Type()
)
vStpInsPortCistPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpInsPortCistPathCost.setStatus("current")


class _VStpInsPortHelloTime_Type(Timeout):
    """Custom type vStpInsPortHelloTime based on Timeout"""
    defaultValue = 200

    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_VStpInsPortHelloTime_Type.__name__ = "Timeout"
_VStpInsPortHelloTime_Object = MibTableColumn
vStpInsPortHelloTime = _VStpInsPortHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 2, 1, 19),
    _VStpInsPortHelloTime_Type()
)
vStpInsPortHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpInsPortHelloTime.setStatus("current")


class _VStpInsPortBridgeHelloTime_Type(Timeout):
    """Custom type vStpInsPortBridgeHelloTime based on Timeout"""
    defaultValue = 200

    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_VStpInsPortBridgeHelloTime_Type.__name__ = "Timeout"
_VStpInsPortBridgeHelloTime_Object = MibTableColumn
vStpInsPortBridgeHelloTime = _VStpInsPortBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 2, 1, 20),
    _VStpInsPortBridgeHelloTime_Type()
)
vStpInsPortBridgeHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpInsPortBridgeHelloTime.setStatus("current")


class _VstpInsPortRcvdInternal_Type(Integer32):
    """Custom type vstpInsPortRcvdInternal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("internal", 2),
          ("unkown", 3))
    )


_VstpInsPortRcvdInternal_Type.__name__ = "Integer32"
_VstpInsPortRcvdInternal_Object = MibTableColumn
vstpInsPortRcvdInternal = _VstpInsPortRcvdInternal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 2, 1, 21),
    _VstpInsPortRcvdInternal_Type()
)
vstpInsPortRcvdInternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vstpInsPortRcvdInternal.setStatus("current")


class _VStpInsPortAdminEdge_Type(Integer32):
    """Custom type vStpInsPortAdminEdge based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_VStpInsPortAdminEdge_Type.__name__ = "Integer32"
_VStpInsPortAdminEdge_Object = MibTableColumn
vStpInsPortAdminEdge = _VStpInsPortAdminEdge_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 2, 1, 22),
    _VStpInsPortAdminEdge_Type()
)
vStpInsPortAdminEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpInsPortAdminEdge.setStatus("current")


class _VStpInsPortAutoEdge_Type(Integer32):
    """Custom type vStpInsPortAutoEdge based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_VStpInsPortAutoEdge_Type.__name__ = "Integer32"
_VStpInsPortAutoEdge_Object = MibTableColumn
vStpInsPortAutoEdge = _VStpInsPortAutoEdge_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 2, 1, 23),
    _VStpInsPortAutoEdge_Type()
)
vStpInsPortAutoEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpInsPortAutoEdge.setStatus("current")


class _VStpInsPortRestrictedRole_Type(Integer32):
    """Custom type vStpInsPortRestrictedRole based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_VStpInsPortRestrictedRole_Type.__name__ = "Integer32"
_VStpInsPortRestrictedRole_Object = MibTableColumn
vStpInsPortRestrictedRole = _VStpInsPortRestrictedRole_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 2, 1, 24),
    _VStpInsPortRestrictedRole_Type()
)
vStpInsPortRestrictedRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpInsPortRestrictedRole.setStatus("current")


class _VStpInsPortRestrictedTcn_Type(Integer32):
    """Custom type vStpInsPortRestrictedTcn based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_VStpInsPortRestrictedTcn_Type.__name__ = "Integer32"
_VStpInsPortRestrictedTcn_Object = MibTableColumn
vStpInsPortRestrictedTcn = _VStpInsPortRestrictedTcn_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 2, 1, 25),
    _VStpInsPortRestrictedTcn_Type()
)
vStpInsPortRestrictedTcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpInsPortRestrictedTcn.setStatus("current")
_VStpBridge_ObjectIdentity = ObjectIdentity
vStpBridge = _VStpBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 3)
)


class _VStpBridgeMode_Type(Integer32):
    """Custom type vStpBridgeMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flat", 1),
          ("onePerVlan", 2))
    )


_VStpBridgeMode_Type.__name__ = "Integer32"
_VStpBridgeMode_Object = MibScalar
vStpBridgeMode = _VStpBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 3, 1),
    _VStpBridgeMode_Type()
)
vStpBridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpBridgeMode.setStatus("current")
_VStpBridgeAddressId_Type = MacAddress
_VStpBridgeAddressId_Object = MibScalar
vStpBridgeAddressId = _VStpBridgeAddressId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 3, 2),
    _VStpBridgeAddressId_Type()
)
vStpBridgeAddressId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpBridgeAddressId.setStatus("current")
_VStpBridgeLastChanged_Type = TimeTicks
_VStpBridgeLastChanged_Object = MibScalar
vStpBridgeLastChanged = _VStpBridgeLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 3, 3),
    _VStpBridgeLastChanged_Type()
)
vStpBridgeLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpBridgeLastChanged.setStatus("current")


class _VStpBridgePathCostMode_Type(Integer32):
    """Custom type vStpBridgePathCostMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("thrityTwoBit", 1))
    )


_VStpBridgePathCostMode_Type.__name__ = "Integer32"
_VStpBridgePathCostMode_Object = MibScalar
vStpBridgePathCostMode = _VStpBridgePathCostMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 3, 4),
    _VStpBridgePathCostMode_Type()
)
vStpBridgePathCostMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpBridgePathCostMode.setStatus("current")


class _VStpBridgeAutoVlanContainment_Type(Integer32):
    """Custom type vStpBridgeAutoVlanContainment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_VStpBridgeAutoVlanContainment_Type.__name__ = "Integer32"
_VStpBridgeAutoVlanContainment_Object = MibScalar
vStpBridgeAutoVlanContainment = _VStpBridgeAutoVlanContainment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 3, 5),
    _VStpBridgeAutoVlanContainment_Type()
)
vStpBridgeAutoVlanContainment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpBridgeAutoVlanContainment.setStatus("current")


class _VStpBridgeModePVST_Type(Integer32):
    """Custom type vStpBridgeModePVST based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_VStpBridgeModePVST_Type.__name__ = "Integer32"
_VStpBridgeModePVST_Object = MibScalar
vStpBridgeModePVST = _VStpBridgeModePVST_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 3, 6),
    _VStpBridgeModePVST_Type()
)
vStpBridgeModePVST.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpBridgeModePVST.setStatus("current")
_VStpMstRegionTable_Object = MibTable
vStpMstRegionTable = _VStpMstRegionTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    vStpMstRegionTable.setStatus("current")
_VStpMstRegionEntry_Object = MibTableRow
vStpMstRegionEntry = _VStpMstRegionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 4, 1)
)
vStpMstRegionEntry.setIndexNames(
    (0, "ALCATEL-IND1-VLAN-STP-MIB", "vStpMstRegionNumber"),
)
if mibBuilder.loadTexts:
    vStpMstRegionEntry.setStatus("current")


class _VStpMstRegionNumber_Type(Integer32):
    """Custom type vStpMstRegionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_VStpMstRegionNumber_Type.__name__ = "Integer32"
_VStpMstRegionNumber_Object = MibTableColumn
vStpMstRegionNumber = _VStpMstRegionNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 4, 1, 1),
    _VStpMstRegionNumber_Type()
)
vStpMstRegionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpMstRegionNumber.setStatus("current")


class _VStpMstRegionConfigFormatSelector_Type(Integer32):
    """Custom type vStpMstRegionConfigFormatSelector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VStpMstRegionConfigFormatSelector_Type.__name__ = "Integer32"
_VStpMstRegionConfigFormatSelector_Object = MibTableColumn
vStpMstRegionConfigFormatSelector = _VStpMstRegionConfigFormatSelector_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 4, 1, 2),
    _VStpMstRegionConfigFormatSelector_Type()
)
vStpMstRegionConfigFormatSelector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpMstRegionConfigFormatSelector.setStatus("current")
_VStpMstRegionConfigDigest_Type = DigestId
_VStpMstRegionConfigDigest_Object = MibTableColumn
vStpMstRegionConfigDigest = _VStpMstRegionConfigDigest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 4, 1, 3),
    _VStpMstRegionConfigDigest_Type()
)
vStpMstRegionConfigDigest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpMstRegionConfigDigest.setStatus("current")


class _VStpMstRegionConfigName_Type(SnmpAdminString):
    """Custom type vStpMstRegionConfigName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VStpMstRegionConfigName_Type.__name__ = "SnmpAdminString"
_VStpMstRegionConfigName_Object = MibTableColumn
vStpMstRegionConfigName = _VStpMstRegionConfigName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 4, 1, 4),
    _VStpMstRegionConfigName_Type()
)
vStpMstRegionConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpMstRegionConfigName.setStatus("current")


class _VStpMstRegionConfigRevisionLevel_Type(Integer32):
    """Custom type vStpMstRegionConfigRevisionLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VStpMstRegionConfigRevisionLevel_Type.__name__ = "Integer32"
_VStpMstRegionConfigRevisionLevel_Object = MibTableColumn
vStpMstRegionConfigRevisionLevel = _VStpMstRegionConfigRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 4, 1, 5),
    _VStpMstRegionConfigRevisionLevel_Type()
)
vStpMstRegionConfigRevisionLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpMstRegionConfigRevisionLevel.setStatus("current")


class _VStpMstRegionMstiList_Type(SnmpAdminString):
    """Custom type vStpMstRegionMstiList based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VStpMstRegionMstiList_Type.__name__ = "SnmpAdminString"
_VStpMstRegionMstiList_Object = MibTableColumn
vStpMstRegionMstiList = _VStpMstRegionMstiList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 4, 1, 6),
    _VStpMstRegionMstiList_Type()
)
vStpMstRegionMstiList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpMstRegionMstiList.setStatus("current")


class _VStpMstRegionCistInstanceNumber_Type(Integer32):
    """Custom type vStpMstRegionCistInstanceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_VStpMstRegionCistInstanceNumber_Type.__name__ = "Integer32"
_VStpMstRegionCistInstanceNumber_Object = MibTableColumn
vStpMstRegionCistInstanceNumber = _VStpMstRegionCistInstanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 4, 1, 7),
    _VStpMstRegionCistInstanceNumber_Type()
)
vStpMstRegionCistInstanceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpMstRegionCistInstanceNumber.setStatus("current")


class _VStpMstRegionMaxHops_Type(Integer32):
    """Custom type vStpMstRegionMaxHops based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_VStpMstRegionMaxHops_Type.__name__ = "Integer32"
_VStpMstRegionMaxHops_Object = MibTableColumn
vStpMstRegionMaxHops = _VStpMstRegionMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 4, 1, 8),
    _VStpMstRegionMaxHops_Type()
)
vStpMstRegionMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpMstRegionMaxHops.setStatus("current")
_VStpMstInstanceTable_Object = MibTable
vStpMstInstanceTable = _VStpMstInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    vStpMstInstanceTable.setStatus("current")
_VStpMstInstanceEntry_Object = MibTableRow
vStpMstInstanceEntry = _VStpMstInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 5, 1)
)
vStpMstInstanceEntry.setIndexNames(
    (0, "ALCATEL-IND1-VLAN-STP-MIB", "vStpMstInstanceNumber"),
)
if mibBuilder.loadTexts:
    vStpMstInstanceEntry.setStatus("current")


class _VStpMstInstanceNumber_Type(Integer32):
    """Custom type vStpMstInstanceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_VStpMstInstanceNumber_Type.__name__ = "Integer32"
_VStpMstInstanceNumber_Object = MibTableColumn
vStpMstInstanceNumber = _VStpMstInstanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 5, 1, 1),
    _VStpMstInstanceNumber_Type()
)
vStpMstInstanceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vStpMstInstanceNumber.setStatus("current")


class _VStpMstInstanceName_Type(SnmpAdminString):
    """Custom type vStpMstInstanceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VStpMstInstanceName_Type.__name__ = "SnmpAdminString"
_VStpMstInstanceName_Object = MibTableColumn
vStpMstInstanceName = _VStpMstInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 5, 1, 2),
    _VStpMstInstanceName_Type()
)
vStpMstInstanceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vStpMstInstanceName.setStatus("current")
_VStpMstInstanceVlanBitmapAddition_Type = VlanBitmap
_VStpMstInstanceVlanBitmapAddition_Object = MibTableColumn
vStpMstInstanceVlanBitmapAddition = _VStpMstInstanceVlanBitmapAddition_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 5, 1, 3),
    _VStpMstInstanceVlanBitmapAddition_Type()
)
vStpMstInstanceVlanBitmapAddition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vStpMstInstanceVlanBitmapAddition.setStatus("current")
_VStpMstInstanceVlanBitmapDeletion_Type = VlanBitmap
_VStpMstInstanceVlanBitmapDeletion_Object = MibTableColumn
vStpMstInstanceVlanBitmapDeletion = _VStpMstInstanceVlanBitmapDeletion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 5, 1, 4),
    _VStpMstInstanceVlanBitmapDeletion_Type()
)
vStpMstInstanceVlanBitmapDeletion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vStpMstInstanceVlanBitmapDeletion.setStatus("current")
_VStpMstInstanceVlanBitmapState_Type = VlanBitmap
_VStpMstInstanceVlanBitmapState_Object = MibTableColumn
vStpMstInstanceVlanBitmapState = _VStpMstInstanceVlanBitmapState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 5, 1, 5),
    _VStpMstInstanceVlanBitmapState_Type()
)
vStpMstInstanceVlanBitmapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpMstInstanceVlanBitmapState.setStatus("current")
_VStpMstInstanceRowStatus_Type = RowStatus
_VStpMstInstanceRowStatus_Object = MibTableColumn
vStpMstInstanceRowStatus = _VStpMstInstanceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 5, 1, 6),
    _VStpMstInstanceRowStatus_Type()
)
vStpMstInstanceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vStpMstInstanceRowStatus.setStatus("current")
_VStpMstVlanAssignmentTable_Object = MibTable
vStpMstVlanAssignmentTable = _VStpMstVlanAssignmentTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    vStpMstVlanAssignmentTable.setStatus("current")
_VStpMstVlanAssignmentEntry_Object = MibTableRow
vStpMstVlanAssignmentEntry = _VStpMstVlanAssignmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 6, 1)
)
vStpMstVlanAssignmentEntry.setIndexNames(
    (0, "ALCATEL-IND1-VLAN-STP-MIB", "vStpMstVlanAssignmentVlanNumber"),
)
if mibBuilder.loadTexts:
    vStpMstVlanAssignmentEntry.setStatus("current")


class _VStpMstVlanAssignmentVlanNumber_Type(Integer32):
    """Custom type vStpMstVlanAssignmentVlanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_VStpMstVlanAssignmentVlanNumber_Type.__name__ = "Integer32"
_VStpMstVlanAssignmentVlanNumber_Object = MibTableColumn
vStpMstVlanAssignmentVlanNumber = _VStpMstVlanAssignmentVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 6, 1, 1),
    _VStpMstVlanAssignmentVlanNumber_Type()
)
vStpMstVlanAssignmentVlanNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vStpMstVlanAssignmentVlanNumber.setStatus("current")


class _VStpMstVlanAssignmentMstiNumber_Type(Integer32):
    """Custom type vStpMstVlanAssignmentMstiNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_VStpMstVlanAssignmentMstiNumber_Type.__name__ = "Integer32"
_VStpMstVlanAssignmentMstiNumber_Object = MibTableColumn
vStpMstVlanAssignmentMstiNumber = _VStpMstVlanAssignmentMstiNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 6, 1, 2),
    _VStpMstVlanAssignmentMstiNumber_Type()
)
vStpMstVlanAssignmentMstiNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpMstVlanAssignmentMstiNumber.setStatus("current")
_VStpPortConfigTable_Object = MibTable
vStpPortConfigTable = _VStpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    vStpPortConfigTable.setStatus("current")
_VStpPortConfigEntry_Object = MibTableRow
vStpPortConfigEntry = _VStpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 7, 1)
)
vStpPortConfigEntry.setIndexNames(
    (0, "ALCATEL-IND1-VLAN-STP-MIB", "vStpPortConfigIfIndex"),
)
if mibBuilder.loadTexts:
    vStpPortConfigEntry.setStatus("current")
_VStpPortConfigIfIndex_Type = InterfaceIndex
_VStpPortConfigIfIndex_Object = MibTableColumn
vStpPortConfigIfIndex = _VStpPortConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 7, 1, 1),
    _VStpPortConfigIfIndex_Type()
)
vStpPortConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpPortConfigIfIndex.setStatus("current")


class _VStpPortConfigTenGigOs8800Opt_Type(Integer32):
    """Custom type vStpPortConfigTenGigOs8800Opt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_VStpPortConfigTenGigOs8800Opt_Type.__name__ = "Integer32"
_VStpPortConfigTenGigOs8800Opt_Object = MibTableColumn
vStpPortConfigTenGigOs8800Opt = _VStpPortConfigTenGigOs8800Opt_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 7, 1, 2),
    _VStpPortConfigTenGigOs8800Opt_Type()
)
vStpPortConfigTenGigOs8800Opt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpPortConfigTenGigOs8800Opt.setStatus("current")


class _VStpPortConfigPVST_Type(Integer32):
    """Custom type vStpPortConfigPVST based on Integer32"""
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
        *(("auto", 1),
          ("disable", 3),
          ("enable", 2))
    )


_VStpPortConfigPVST_Type.__name__ = "Integer32"
_VStpPortConfigPVST_Object = MibTableColumn
vStpPortConfigPVST = _VStpPortConfigPVST_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 7, 1, 3),
    _VStpPortConfigPVST_Type()
)
vStpPortConfigPVST.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpPortConfigPVST.setStatus("current")


class _VStpPortConfigStatePVST_Type(Integer32):
    """Custom type vStpPortConfigStatePVST based on Integer32"""
    defaultValue = 2

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


_VStpPortConfigStatePVST_Type.__name__ = "Integer32"
_VStpPortConfigStatePVST_Object = MibTableColumn
vStpPortConfigStatePVST = _VStpPortConfigStatePVST_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 7, 1, 4),
    _VStpPortConfigStatePVST_Type()
)
vStpPortConfigStatePVST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpPortConfigStatePVST.setStatus("current")


class _VStpRrstpGlobalState_Type(Integer32):
    """Custom type vStpRrstpGlobalState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_VStpRrstpGlobalState_Type.__name__ = "Integer32"
_VStpRrstpGlobalState_Object = MibScalar
vStpRrstpGlobalState = _VStpRrstpGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 8),
    _VStpRrstpGlobalState_Type()
)
vStpRrstpGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpRrstpGlobalState.setStatus("current")
_VStpRrstpRingConfigTable_Object = MibTable
vStpRrstpRingConfigTable = _VStpRrstpRingConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    vStpRrstpRingConfigTable.setStatus("current")
_VStpRrstpRingConfigEntry_Object = MibTableRow
vStpRrstpRingConfigEntry = _VStpRrstpRingConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 9, 1)
)
vStpRrstpRingConfigEntry.setIndexNames(
    (0, "ALCATEL-IND1-VLAN-STP-MIB", "vStpRrstpRingId"),
)
if mibBuilder.loadTexts:
    vStpRrstpRingConfigEntry.setStatus("current")


class _VStpRrstpRingId_Type(Integer32):
    """Custom type vStpRrstpRingId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_VStpRrstpRingId_Type.__name__ = "Integer32"
_VStpRrstpRingId_Object = MibTableColumn
vStpRrstpRingId = _VStpRrstpRingId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 9, 1, 1),
    _VStpRrstpRingId_Type()
)
vStpRrstpRingId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vStpRrstpRingId.setStatus("current")
_VStpRrstpRingPort1_Type = InterfaceIndex
_VStpRrstpRingPort1_Object = MibTableColumn
vStpRrstpRingPort1 = _VStpRrstpRingPort1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 9, 1, 2),
    _VStpRrstpRingPort1_Type()
)
vStpRrstpRingPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vStpRrstpRingPort1.setStatus("current")
_VStpRrstpRingPort2_Type = InterfaceIndex
_VStpRrstpRingPort2_Object = MibTableColumn
vStpRrstpRingPort2 = _VStpRrstpRingPort2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 9, 1, 3),
    _VStpRrstpRingPort2_Type()
)
vStpRrstpRingPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vStpRrstpRingPort2.setStatus("current")


class _VStpRrstpRingVlanTag_Type(Integer32):
    """Custom type vStpRrstpRingVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VStpRrstpRingVlanTag_Type.__name__ = "Integer32"
_VStpRrstpRingVlanTag_Object = MibTableColumn
vStpRrstpRingVlanTag = _VStpRrstpRingVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 9, 1, 4),
    _VStpRrstpRingVlanTag_Type()
)
vStpRrstpRingVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vStpRrstpRingVlanTag.setStatus("current")


class _VStpRrstpRingState_Type(Integer32):
    """Custom type vStpRrstpRingState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_VStpRrstpRingState_Type.__name__ = "Integer32"
_VStpRrstpRingState_Object = MibTableColumn
vStpRrstpRingState = _VStpRrstpRingState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 9, 1, 5),
    _VStpRrstpRingState_Type()
)
vStpRrstpRingState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vStpRrstpRingState.setStatus("current")
_VStpRrstpRingRowStatus_Type = RowStatus
_VStpRrstpRingRowStatus_Object = MibTableColumn
vStpRrstpRingRowStatus = _VStpRrstpRingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 1, 1, 9, 1, 6),
    _VStpRrstpRingRowStatus_Type()
)
vStpRrstpRingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vStpRrstpRingRowStatus.setStatus("current")
_AlcatelIND1VLANSTPMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1VLANSTPMIBConformance = _AlcatelIND1VLANSTPMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1VLANSTPMIBConformance.setStatus("current")
_AlcatelIND1VLANSTPMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1VLANSTPMIBGroups = _AlcatelIND1VLANSTPMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1VLANSTPMIBGroups.setStatus("current")
_AlcatelIND1VLANSTPMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1VLANSTPMIBCompliances = _AlcatelIND1VLANSTPMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1VLANSTPMIBCompliances.setStatus("current")

# Managed Objects groups

vStpInsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 2, 1, 1)
)
vStpInsGroup.setObjects(
      *(("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsNumber"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsProtocolSpecification"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsPriority"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsBridgeAddress"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsTimeSinceTopologyChange"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsTopChanges"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsDesignatedRoot"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsRootCost"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsRootPortNumber"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsNextBestRootCost"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsNextBestRootPortNumber"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsMaxAge"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsHelloTime"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsHoldTime"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsForwardDelay"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsBridgeMaxAge"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsBridgeHelloTime"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsBridgeForwardDelay"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsBpduSwitching"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsCistRegionalRootId"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsCistPathCost"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpIns1x1VlanNumber"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsMstiNumber"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsMode"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsAutoVlanContainment"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsBridgeTxHoldCount"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsAdminState"))
)
if mibBuilder.loadTexts:
    vStpInsGroup.setStatus("current")

vStpInsPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 2, 1, 2)
)
vStpInsPortGroup.setObjects(
      *(("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsPortNumber"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsPortPriority"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsPortState"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsPortEnable"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsPortPathCost"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsPortDesignatedRoot"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsPortDesignatedCost"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsPortDesignatedBridge"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsPortDesignatedPtPrio"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsPortDesignatedPtNumber"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsPortForwardTransitions"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsPortManualMode"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsPortRole"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsPortPrimaryPortNumber"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsPortAdminConnectionType"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsPortOperConnectionType"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsPortCistRegionRootId"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsPortCistPathCost"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsPortHelloTime"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsPortBridgeHelloTime"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vstpInsPortRcvdInternal"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsPortAdminEdge"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsPortAutoEdge"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsPortRestrictedRole"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsPortRestrictedTcn"))
)
if mibBuilder.loadTexts:
    vStpInsPortGroup.setStatus("current")

vStpMstInstanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 2, 1, 4)
)
vStpMstInstanceGroup.setObjects(
      *(("ALCATEL-IND1-VLAN-STP-MIB", "vStpMstInstanceName"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpMstInstanceVlanBitmapAddition"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpMstInstanceVlanBitmapDeletion"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpMstInstanceVlanBitmapState"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpMstInstanceRowStatus"))
)
if mibBuilder.loadTexts:
    vStpMstInstanceGroup.setStatus("current")

vStpMstVlanAssignmentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 2, 1, 5)
)
vStpMstVlanAssignmentGroup.setObjects(
    ("ALCATEL-IND1-VLAN-STP-MIB", "vStpMstVlanAssignmentMstiNumber")
)
if mibBuilder.loadTexts:
    vStpMstVlanAssignmentGroup.setStatus("current")

vStpMstRegionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 2, 1, 6)
)
vStpMstRegionGroup.setObjects(
      *(("ALCATEL-IND1-VLAN-STP-MIB", "vStpMstRegionNumber"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpMstRegionConfigFormatSelector"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpMstRegionConfigDigest"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpMstRegionConfigName"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpMstRegionConfigRevisionLevel"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpMstRegionMstiList"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpMstRegionCistInstanceNumber"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpMstRegionMaxHops"))
)
if mibBuilder.loadTexts:
    vStpMstRegionGroup.setStatus("current")

vStpPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 2, 1, 7)
)
vStpPortConfigGroup.setObjects(
      *(("ALCATEL-IND1-VLAN-STP-MIB", "vStpPortConfigIfIndex"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpPortConfigTenGigOs8800Opt"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpPortConfigPVST"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpPortConfigStatePVST"))
)
if mibBuilder.loadTexts:
    vStpPortConfigGroup.setStatus("current")

vStpRrstpRingConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 2, 1, 8)
)
vStpRrstpRingConfigGroup.setObjects(
      *(("ALCATEL-IND1-VLAN-STP-MIB", "vStpRrstpRingPort1"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpRrstpRingPort2"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpRrstpRingVlanTag"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpRrstpRingState"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpRrstpRingRowStatus"))
)
if mibBuilder.loadTexts:
    vStpRrstpRingConfigGroup.setStatus("current")

vStpRrstpRingBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 2, 1, 9)
)
vStpRrstpRingBaseGroup.setObjects(
    ("ALCATEL-IND1-VLAN-STP-MIB", "vStpRrstpGlobalState")
)
if mibBuilder.loadTexts:
    vStpRrstpRingBaseGroup.setStatus("current")

vStpBridgeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 2, 1, 10)
)
vStpBridgeGroup.setObjects(
      *(("ALCATEL-IND1-VLAN-STP-MIB", "vStpBridgeMode"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpBridgeAddressId"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpBridgeLastChanged"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpBridgePathCostMode"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpBridgeAutoVlanContainment"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpBridgeModePVST"))
)
if mibBuilder.loadTexts:
    vStpBridgeGroup.setStatus("current")


# Notification objects

stpNewRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 0, 1)
)
stpNewRoot.setObjects(
    ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsNumber")
)
if mibBuilder.loadTexts:
    stpNewRoot.setStatus(
        "current"
    )

stpRootPortChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 0, 2)
)
stpRootPortChange.setObjects(
      *(("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsNumber"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "vStpInsRootPortNumber"))
)
if mibBuilder.loadTexts:
    stpRootPortChange.setStatus(
        "current"
    )


# Notifications groups

vStpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 2, 1, 3)
)
vStpNotificationGroup.setObjects(
      *(("ALCATEL-IND1-VLAN-STP-MIB", "stpNewRoot"),
        ("ALCATEL-IND1-VLAN-STP-MIB", "stpRootPortChange"))
)
if mibBuilder.loadTexts:
    vStpNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1VLANSTPMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 12, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1VLANSTPMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-VLAN-STP-MIB",
    **{"VlanBitmap": VlanBitmap,
       "DigestId": DigestId,
       "alcatelIND1VLANSTPMIB": alcatelIND1VLANSTPMIB,
       "alcatelIND1VLANSTPMIBNotifications": alcatelIND1VLANSTPMIBNotifications,
       "stpNewRoot": stpNewRoot,
       "stpRootPortChange": stpRootPortChange,
       "alcatelIND1VLANSTPMIBObjects": alcatelIND1VLANSTPMIBObjects,
       "vStpInfo": vStpInfo,
       "vStpInsTable": vStpInsTable,
       "vStpInsEntry": vStpInsEntry,
       "vStpInsBridgeMode": vStpInsBridgeMode,
       "vStpInsNumber": vStpInsNumber,
       "vStpInsProtocolSpecification": vStpInsProtocolSpecification,
       "vStpInsPriority": vStpInsPriority,
       "vStpInsBridgeAddress": vStpInsBridgeAddress,
       "vStpInsTimeSinceTopologyChange": vStpInsTimeSinceTopologyChange,
       "vStpInsTopChanges": vStpInsTopChanges,
       "vStpInsDesignatedRoot": vStpInsDesignatedRoot,
       "vStpInsRootCost": vStpInsRootCost,
       "vStpInsRootPortNumber": vStpInsRootPortNumber,
       "vStpInsNextBestRootCost": vStpInsNextBestRootCost,
       "vStpInsNextBestRootPortNumber": vStpInsNextBestRootPortNumber,
       "vStpInsMaxAge": vStpInsMaxAge,
       "vStpInsHelloTime": vStpInsHelloTime,
       "vStpInsHoldTime": vStpInsHoldTime,
       "vStpInsForwardDelay": vStpInsForwardDelay,
       "vStpInsBridgeMaxAge": vStpInsBridgeMaxAge,
       "vStpInsBridgeHelloTime": vStpInsBridgeHelloTime,
       "vStpInsBridgeForwardDelay": vStpInsBridgeForwardDelay,
       "vStpInsBpduSwitching": vStpInsBpduSwitching,
       "vStpInsCistRegionalRootId": vStpInsCistRegionalRootId,
       "vStpInsCistPathCost": vStpInsCistPathCost,
       "vStpIns1x1VlanNumber": vStpIns1x1VlanNumber,
       "vStpInsMstiNumber": vStpInsMstiNumber,
       "vStpInsMode": vStpInsMode,
       "vStpInsAutoVlanContainment": vStpInsAutoVlanContainment,
       "vStpInsBridgeTxHoldCount": vStpInsBridgeTxHoldCount,
       "vStpInsAdminState": vStpInsAdminState,
       "vStpInsPortTable": vStpInsPortTable,
       "vStpInsPortEntry": vStpInsPortEntry,
       "vStpInsPortNumber": vStpInsPortNumber,
       "vStpInsPortPriority": vStpInsPortPriority,
       "vStpInsPortState": vStpInsPortState,
       "vStpInsPortEnable": vStpInsPortEnable,
       "vStpInsPortPathCost": vStpInsPortPathCost,
       "vStpInsPortDesignatedRoot": vStpInsPortDesignatedRoot,
       "vStpInsPortDesignatedCost": vStpInsPortDesignatedCost,
       "vStpInsPortDesignatedBridge": vStpInsPortDesignatedBridge,
       "vStpInsPortDesignatedPtPrio": vStpInsPortDesignatedPtPrio,
       "vStpInsPortDesignatedPtNumber": vStpInsPortDesignatedPtNumber,
       "vStpInsPortForwardTransitions": vStpInsPortForwardTransitions,
       "vStpInsPortManualMode": vStpInsPortManualMode,
       "vStpInsPortRole": vStpInsPortRole,
       "vStpInsPortPrimaryPortNumber": vStpInsPortPrimaryPortNumber,
       "vStpInsPortAdminConnectionType": vStpInsPortAdminConnectionType,
       "vStpInsPortOperConnectionType": vStpInsPortOperConnectionType,
       "vStpInsPortCistRegionRootId": vStpInsPortCistRegionRootId,
       "vStpInsPortCistPathCost": vStpInsPortCistPathCost,
       "vStpInsPortHelloTime": vStpInsPortHelloTime,
       "vStpInsPortBridgeHelloTime": vStpInsPortBridgeHelloTime,
       "vstpInsPortRcvdInternal": vstpInsPortRcvdInternal,
       "vStpInsPortAdminEdge": vStpInsPortAdminEdge,
       "vStpInsPortAutoEdge": vStpInsPortAutoEdge,
       "vStpInsPortRestrictedRole": vStpInsPortRestrictedRole,
       "vStpInsPortRestrictedTcn": vStpInsPortRestrictedTcn,
       "vStpBridge": vStpBridge,
       "vStpBridgeMode": vStpBridgeMode,
       "vStpBridgeAddressId": vStpBridgeAddressId,
       "vStpBridgeLastChanged": vStpBridgeLastChanged,
       "vStpBridgePathCostMode": vStpBridgePathCostMode,
       "vStpBridgeAutoVlanContainment": vStpBridgeAutoVlanContainment,
       "vStpBridgeModePVST": vStpBridgeModePVST,
       "vStpMstRegionTable": vStpMstRegionTable,
       "vStpMstRegionEntry": vStpMstRegionEntry,
       "vStpMstRegionNumber": vStpMstRegionNumber,
       "vStpMstRegionConfigFormatSelector": vStpMstRegionConfigFormatSelector,
       "vStpMstRegionConfigDigest": vStpMstRegionConfigDigest,
       "vStpMstRegionConfigName": vStpMstRegionConfigName,
       "vStpMstRegionConfigRevisionLevel": vStpMstRegionConfigRevisionLevel,
       "vStpMstRegionMstiList": vStpMstRegionMstiList,
       "vStpMstRegionCistInstanceNumber": vStpMstRegionCistInstanceNumber,
       "vStpMstRegionMaxHops": vStpMstRegionMaxHops,
       "vStpMstInstanceTable": vStpMstInstanceTable,
       "vStpMstInstanceEntry": vStpMstInstanceEntry,
       "vStpMstInstanceNumber": vStpMstInstanceNumber,
       "vStpMstInstanceName": vStpMstInstanceName,
       "vStpMstInstanceVlanBitmapAddition": vStpMstInstanceVlanBitmapAddition,
       "vStpMstInstanceVlanBitmapDeletion": vStpMstInstanceVlanBitmapDeletion,
       "vStpMstInstanceVlanBitmapState": vStpMstInstanceVlanBitmapState,
       "vStpMstInstanceRowStatus": vStpMstInstanceRowStatus,
       "vStpMstVlanAssignmentTable": vStpMstVlanAssignmentTable,
       "vStpMstVlanAssignmentEntry": vStpMstVlanAssignmentEntry,
       "vStpMstVlanAssignmentVlanNumber": vStpMstVlanAssignmentVlanNumber,
       "vStpMstVlanAssignmentMstiNumber": vStpMstVlanAssignmentMstiNumber,
       "vStpPortConfigTable": vStpPortConfigTable,
       "vStpPortConfigEntry": vStpPortConfigEntry,
       "vStpPortConfigIfIndex": vStpPortConfigIfIndex,
       "vStpPortConfigTenGigOs8800Opt": vStpPortConfigTenGigOs8800Opt,
       "vStpPortConfigPVST": vStpPortConfigPVST,
       "vStpPortConfigStatePVST": vStpPortConfigStatePVST,
       "vStpRrstpGlobalState": vStpRrstpGlobalState,
       "vStpRrstpRingConfigTable": vStpRrstpRingConfigTable,
       "vStpRrstpRingConfigEntry": vStpRrstpRingConfigEntry,
       "vStpRrstpRingId": vStpRrstpRingId,
       "vStpRrstpRingPort1": vStpRrstpRingPort1,
       "vStpRrstpRingPort2": vStpRrstpRingPort2,
       "vStpRrstpRingVlanTag": vStpRrstpRingVlanTag,
       "vStpRrstpRingState": vStpRrstpRingState,
       "vStpRrstpRingRowStatus": vStpRrstpRingRowStatus,
       "alcatelIND1VLANSTPMIBConformance": alcatelIND1VLANSTPMIBConformance,
       "alcatelIND1VLANSTPMIBGroups": alcatelIND1VLANSTPMIBGroups,
       "vStpInsGroup": vStpInsGroup,
       "vStpInsPortGroup": vStpInsPortGroup,
       "vStpNotificationGroup": vStpNotificationGroup,
       "vStpMstInstanceGroup": vStpMstInstanceGroup,
       "vStpMstVlanAssignmentGroup": vStpMstVlanAssignmentGroup,
       "vStpMstRegionGroup": vStpMstRegionGroup,
       "vStpPortConfigGroup": vStpPortConfigGroup,
       "vStpRrstpRingConfigGroup": vStpRrstpRingConfigGroup,
       "vStpRrstpRingBaseGroup": vStpRrstpRingBaseGroup,
       "vStpBridgeGroup": vStpBridgeGroup,
       "alcatelIND1VLANSTPMIBCompliances": alcatelIND1VLANSTPMIBCompliances,
       "alcatelIND1VLANSTPMIBCompliance": alcatelIND1VLANSTPMIBCompliance}
)
