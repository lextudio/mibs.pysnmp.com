# SNMP MIB module (HP-ICF-BRIDGE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-BRIDGE
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:09 2024
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

(dot1dBasePortEntry,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePortEntry")

(VidList,) = mibBuilder.importSymbols(
    "HP-ICF-FTRCO",
    "VidList")

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(ConfigStatus,) = mibBuilder.importSymbols(
    "HP-ICF-TC",
    "ConfigStatus")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(VlanId,
 VlanIndex,
 dot1qVlanStaticEntry) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId",
    "VlanIndex",
    "dot1qVlanStaticEntry")

(portCopyEntry,) = mibBuilder.importSymbols(
    "SMON-MIB",
    "portCopyEntry")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

hpicfBridge = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12)
)
hpicfBridge.setRevisions(
        ("2014-04-27 00:00",
         "2013-10-11 00:00",
         "2012-07-13 00:00",
         "2012-05-30 00:00",
         "2010-06-26 00:00",
         "2009-12-15 00:00",
         "2009-02-11 00:00",
         "2006-09-30 00:00",
         "2006-09-26 00:00",
         "2006-08-13 17:38",
         "2003-02-20 00:00",
         "2002-05-23 17:38",
         "2001-10-03 20:50",
         "2000-11-03 06:42")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class BridgeId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class LoopProtectReceiverAction(Integer32, TextualConvention):
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
        *(("disableTx", 1),
          ("disableTxRx", 3),
          ("noDisable", 2))
    )



# MIB Managed Objects in the order of their OIDs

_HpicfBridgeObjects_ObjectIdentity = ObjectIdentity
hpicfBridgeObjects = _HpicfBridgeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1)
)
_HpicfBridgeBase_ObjectIdentity = ObjectIdentity
hpicfBridgeBase = _HpicfBridgeBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 1)
)


class _HpicfBridgeMaxVlans_Type(Integer32):
    """Custom type hpicfBridgeMaxVlans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HpicfBridgeMaxVlans_Type.__name__ = "Integer32"
_HpicfBridgeMaxVlans_Object = MibScalar
hpicfBridgeMaxVlans = _HpicfBridgeMaxVlans_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 1, 1),
    _HpicfBridgeMaxVlans_Type()
)
hpicfBridgeMaxVlans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBridgeMaxVlans.setStatus("current")


class _HpicfBridgeVlanEnable_Type(Integer32):
    """Custom type hpicfBridgeVlanEnable based on Integer32"""
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


_HpicfBridgeVlanEnable_Type.__name__ = "Integer32"
_HpicfBridgeVlanEnable_Object = MibScalar
hpicfBridgeVlanEnable = _HpicfBridgeVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 1, 2),
    _HpicfBridgeVlanEnable_Type()
)
hpicfBridgeVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBridgeVlanEnable.setStatus("current")
_HpicfBridgePrimaryVlan_Type = VlanIndex
_HpicfBridgePrimaryVlan_Object = MibScalar
hpicfBridgePrimaryVlan = _HpicfBridgePrimaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 1, 3),
    _HpicfBridgePrimaryVlan_Type()
)
hpicfBridgePrimaryVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBridgePrimaryVlan.setStatus("current")
_HpicfBridgeVlanConfigStatus_Type = ConfigStatus
_HpicfBridgeVlanConfigStatus_Object = MibScalar
hpicfBridgeVlanConfigStatus = _HpicfBridgeVlanConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 1, 4),
    _HpicfBridgeVlanConfigStatus_Type()
)
hpicfBridgeVlanConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfBridgeVlanConfigStatus.setStatus("current")
_HpicfBridgeGvrp_ObjectIdentity = ObjectIdentity
hpicfBridgeGvrp = _HpicfBridgeGvrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 2)
)
_HpicfBridgeGvrpPortTable_Object = MibTable
hpicfBridgeGvrpPortTable = _HpicfBridgeGvrpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfBridgeGvrpPortTable.setStatus("current")
_HpicfBridgeGvrpPortEntry_Object = MibTableRow
hpicfBridgeGvrpPortEntry = _HpicfBridgeGvrpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfBridgeGvrpPortEntry.setStatus("current")
_HpicfBridgeGvrpRestrictedVlanReg_Type = TruthValue
_HpicfBridgeGvrpRestrictedVlanReg_Object = MibTableColumn
hpicfBridgeGvrpRestrictedVlanReg = _HpicfBridgeGvrpRestrictedVlanReg_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 2, 1, 1, 1),
    _HpicfBridgeGvrpRestrictedVlanReg_Type()
)
hpicfBridgeGvrpRestrictedVlanReg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBridgeGvrpRestrictedVlanReg.setStatus("current")
_HpicfBridgeGvrpStateMachineTable_Object = MibTable
hpicfBridgeGvrpStateMachineTable = _HpicfBridgeGvrpStateMachineTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hpicfBridgeGvrpStateMachineTable.setStatus("current")
_HpicfBridgeGvrpStateMachineEntry_Object = MibTableRow
hpicfBridgeGvrpStateMachineEntry = _HpicfBridgeGvrpStateMachineEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 2, 2, 1)
)
hpicfBridgeGvrpStateMachineEntry.setIndexNames(
    (0, "HP-ICF-BRIDGE", "hpicfGenericVlanId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpicfBridgeGvrpStateMachineEntry.setStatus("current")
_HpicfGenericVlanId_Type = VlanId
_HpicfGenericVlanId_Object = MibTableColumn
hpicfGenericVlanId = _HpicfGenericVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 2, 2, 1, 1),
    _HpicfGenericVlanId_Type()
)
hpicfGenericVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfGenericVlanId.setStatus("current")


class _HpicfApplicantStateMachine_Type(Integer32):
    """Custom type hpicfApplicantStateMachine based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("aa", 1),
          ("ao", 8),
          ("aon", 12),
          ("ap", 5),
          ("la", 3),
          ("lo", 10),
          ("qa", 2),
          ("qo", 9),
          ("qon", 13),
          ("qp", 6),
          ("va", 0),
          ("vo", 7),
          ("von", 11),
          ("vp", 4))
    )


_HpicfApplicantStateMachine_Type.__name__ = "Integer32"
_HpicfApplicantStateMachine_Object = MibTableColumn
hpicfApplicantStateMachine = _HpicfApplicantStateMachine_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 2, 2, 1, 2),
    _HpicfApplicantStateMachine_Type()
)
hpicfApplicantStateMachine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfApplicantStateMachine.setStatus("current")


class _HpicfRegistarStateMachine_Type(Integer32):
    """Custom type hpicfRegistarStateMachine based on Integer32"""
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
        *(("inf", 12),
          ("inn", 0),
          ("inr", 6),
          ("l1", 4),
          ("l1f", 16),
          ("l1r", 10),
          ("l2", 3),
          ("l2f", 15),
          ("l2r", 9),
          ("l3", 2),
          ("l3f", 14),
          ("l3r", 8),
          ("lv", 1),
          ("lvf", 13),
          ("lvr", 7),
          ("mt", 5),
          ("mtf", 17),
          ("mtr", 11))
    )


_HpicfRegistarStateMachine_Type.__name__ = "Integer32"
_HpicfRegistarStateMachine_Object = MibTableColumn
hpicfRegistarStateMachine = _HpicfRegistarStateMachine_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 2, 2, 1, 3),
    _HpicfRegistarStateMachine_Type()
)
hpicfRegistarStateMachine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRegistarStateMachine.setStatus("current")
_HpicfBridgeRstp_ObjectIdentity = ObjectIdentity
hpicfBridgeRstp = _HpicfBridgeRstp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 4)
)


class _HpicfBridgeRstpForceVersion_Type(Integer32):
    """Custom type hpicfBridgeRstpForceVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mstpOperation", 3),
          ("rstpOperation", 2),
          ("stpCompatibility", 0))
    )


_HpicfBridgeRstpForceVersion_Type.__name__ = "Integer32"
_HpicfBridgeRstpForceVersion_Object = MibScalar
hpicfBridgeRstpForceVersion = _HpicfBridgeRstpForceVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 4, 1),
    _HpicfBridgeRstpForceVersion_Type()
)
hpicfBridgeRstpForceVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBridgeRstpForceVersion.setStatus("current")
_HpicfBridgeRstpConfigStatus_Type = ConfigStatus
_HpicfBridgeRstpConfigStatus_Object = MibScalar
hpicfBridgeRstpConfigStatus = _HpicfBridgeRstpConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 4, 2),
    _HpicfBridgeRstpConfigStatus_Type()
)
hpicfBridgeRstpConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfBridgeRstpConfigStatus.setStatus("current")


class _HpicfBridgeRstpProtocolVersion_Type(Integer32):
    """Custom type hpicfBridgeRstpProtocolVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ieee8021d", 0),
          ("ieee8021s", 3),
          ("ieee8021w", 2))
    )


_HpicfBridgeRstpProtocolVersion_Type.__name__ = "Integer32"
_HpicfBridgeRstpProtocolVersion_Object = MibScalar
hpicfBridgeRstpProtocolVersion = _HpicfBridgeRstpProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 4, 3),
    _HpicfBridgeRstpProtocolVersion_Type()
)
hpicfBridgeRstpProtocolVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBridgeRstpProtocolVersion.setStatus("current")


class _HpicfBridgeRstpAdminStatus_Type(Integer32):
    """Custom type hpicfBridgeRstpAdminStatus based on Integer32"""
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


_HpicfBridgeRstpAdminStatus_Type.__name__ = "Integer32"
_HpicfBridgeRstpAdminStatus_Object = MibScalar
hpicfBridgeRstpAdminStatus = _HpicfBridgeRstpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 4, 4),
    _HpicfBridgeRstpAdminStatus_Type()
)
hpicfBridgeRstpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBridgeRstpAdminStatus.setStatus("current")
_HpicfBridgeRstpPortTable_Object = MibTable
hpicfBridgeRstpPortTable = _HpicfBridgeRstpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 4, 5)
)
if mibBuilder.loadTexts:
    hpicfBridgeRstpPortTable.setStatus("current")
_HpicfBridgeRstpPortEntry_Object = MibTableRow
hpicfBridgeRstpPortEntry = _HpicfBridgeRstpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 4, 5, 1)
)
hpicfBridgeRstpPortEntry.setIndexNames(
    (0, "HP-ICF-BRIDGE", "hpicfBridgeRstpPortIndex"),
)
if mibBuilder.loadTexts:
    hpicfBridgeRstpPortEntry.setStatus("current")


class _HpicfBridgeRstpPortIndex_Type(Integer32):
    """Custom type hpicfBridgeRstpPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfBridgeRstpPortIndex_Type.__name__ = "Integer32"
_HpicfBridgeRstpPortIndex_Object = MibTableColumn
hpicfBridgeRstpPortIndex = _HpicfBridgeRstpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 4, 5, 1, 1),
    _HpicfBridgeRstpPortIndex_Type()
)
hpicfBridgeRstpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfBridgeRstpPortIndex.setStatus("current")


class _HpicfBridgeRstpAdminEdgePort_Type(Integer32):
    """Custom type hpicfBridgeRstpAdminEdgePort based on Integer32"""
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


_HpicfBridgeRstpAdminEdgePort_Type.__name__ = "Integer32"
_HpicfBridgeRstpAdminEdgePort_Object = MibTableColumn
hpicfBridgeRstpAdminEdgePort = _HpicfBridgeRstpAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 4, 5, 1, 2),
    _HpicfBridgeRstpAdminEdgePort_Type()
)
hpicfBridgeRstpAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBridgeRstpAdminEdgePort.setStatus("current")


class _HpicfBridgeRstpOperEdgePort_Type(Integer32):
    """Custom type hpicfBridgeRstpOperEdgePort based on Integer32"""
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


_HpicfBridgeRstpOperEdgePort_Type.__name__ = "Integer32"
_HpicfBridgeRstpOperEdgePort_Object = MibTableColumn
hpicfBridgeRstpOperEdgePort = _HpicfBridgeRstpOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 4, 5, 1, 3),
    _HpicfBridgeRstpOperEdgePort_Type()
)
hpicfBridgeRstpOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfBridgeRstpOperEdgePort.setStatus("current")


class _HpicfBridgeRstpAdminPointToPointMac_Type(Integer32):
    """Custom type hpicfBridgeRstpAdminPointToPointMac based on Integer32"""
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


_HpicfBridgeRstpAdminPointToPointMac_Type.__name__ = "Integer32"
_HpicfBridgeRstpAdminPointToPointMac_Object = MibTableColumn
hpicfBridgeRstpAdminPointToPointMac = _HpicfBridgeRstpAdminPointToPointMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 4, 5, 1, 4),
    _HpicfBridgeRstpAdminPointToPointMac_Type()
)
hpicfBridgeRstpAdminPointToPointMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBridgeRstpAdminPointToPointMac.setStatus("current")
_HpicfBridgeRstpOperPointToPointMac_Type = TruthValue
_HpicfBridgeRstpOperPointToPointMac_Object = MibTableColumn
hpicfBridgeRstpOperPointToPointMac = _HpicfBridgeRstpOperPointToPointMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 4, 5, 1, 5),
    _HpicfBridgeRstpOperPointToPointMac_Type()
)
hpicfBridgeRstpOperPointToPointMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfBridgeRstpOperPointToPointMac.setStatus("current")


class _HpicfBridgeRstpPortPathCost_Type(Integer32):
    """Custom type hpicfBridgeRstpPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_HpicfBridgeRstpPortPathCost_Type.__name__ = "Integer32"
_HpicfBridgeRstpPortPathCost_Object = MibTableColumn
hpicfBridgeRstpPortPathCost = _HpicfBridgeRstpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 4, 5, 1, 6),
    _HpicfBridgeRstpPortPathCost_Type()
)
hpicfBridgeRstpPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBridgeRstpPortPathCost.setStatus("current")
_HpicfBridgeRstpForceBpduMigrationCheck_Type = TruthValue
_HpicfBridgeRstpForceBpduMigrationCheck_Object = MibTableColumn
hpicfBridgeRstpForceBpduMigrationCheck = _HpicfBridgeRstpForceBpduMigrationCheck_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 4, 5, 1, 7),
    _HpicfBridgeRstpForceBpduMigrationCheck_Type()
)
hpicfBridgeRstpForceBpduMigrationCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBridgeRstpForceBpduMigrationCheck.setStatus("current")
_HpicfBridgeRstpAutoEdgePort_Type = TruthValue
_HpicfBridgeRstpAutoEdgePort_Object = MibTableColumn
hpicfBridgeRstpAutoEdgePort = _HpicfBridgeRstpAutoEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 4, 5, 1, 8),
    _HpicfBridgeRstpAutoEdgePort_Type()
)
hpicfBridgeRstpAutoEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBridgeRstpAutoEdgePort.setStatus("current")
_HpicfBridgeRstpPortBpduFiltering_Type = TruthValue
_HpicfBridgeRstpPortBpduFiltering_Object = MibTableColumn
hpicfBridgeRstpPortBpduFiltering = _HpicfBridgeRstpPortBpduFiltering_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 4, 5, 1, 9),
    _HpicfBridgeRstpPortBpduFiltering_Type()
)
hpicfBridgeRstpPortBpduFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBridgeRstpPortBpduFiltering.setStatus("current")
_HpicfBridgeStpBpduThrottleConfig_ObjectIdentity = ObjectIdentity
hpicfBridgeStpBpduThrottleConfig = _HpicfBridgeStpBpduThrottleConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 4, 6)
)


class _HpicfBridgeStpBpduThrottleStatus_Type(Integer32):
    """Custom type hpicfBridgeStpBpduThrottleStatus based on Integer32"""
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


_HpicfBridgeStpBpduThrottleStatus_Type.__name__ = "Integer32"
_HpicfBridgeStpBpduThrottleStatus_Object = MibScalar
hpicfBridgeStpBpduThrottleStatus = _HpicfBridgeStpBpduThrottleStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 4, 6, 1),
    _HpicfBridgeStpBpduThrottleStatus_Type()
)
hpicfBridgeStpBpduThrottleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBridgeStpBpduThrottleStatus.setStatus("current")


class _HpicfBridgeStpBpduThrottleValue_Type(Integer32):
    """Custom type hpicfBridgeStpBpduThrottleValue based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfBridgeStpBpduThrottleValue_Type.__name__ = "Integer32"
_HpicfBridgeStpBpduThrottleValue_Object = MibScalar
hpicfBridgeStpBpduThrottleValue = _HpicfBridgeStpBpduThrottleValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 4, 6, 2),
    _HpicfBridgeStpBpduThrottleValue_Type()
)
hpicfBridgeStpBpduThrottleValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBridgeStpBpduThrottleValue.setStatus("current")
_HpicfBridgeLoopProtect_ObjectIdentity = ObjectIdentity
hpicfBridgeLoopProtect = _HpicfBridgeLoopProtect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 5)
)
_HpicfBridgeLoopProtectNotifications_ObjectIdentity = ObjectIdentity
hpicfBridgeLoopProtectNotifications = _HpicfBridgeLoopProtectNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 5, 0)
)
_HpicfBridgeLoopProtectBase_ObjectIdentity = ObjectIdentity
hpicfBridgeLoopProtectBase = _HpicfBridgeLoopProtectBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 5, 1)
)


class _HpicfBridgeLoopProtectInterval_Type(Integer32):
    """Custom type hpicfBridgeLoopProtectInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HpicfBridgeLoopProtectInterval_Type.__name__ = "Integer32"
_HpicfBridgeLoopProtectInterval_Object = MibScalar
hpicfBridgeLoopProtectInterval = _HpicfBridgeLoopProtectInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 5, 1, 1),
    _HpicfBridgeLoopProtectInterval_Type()
)
hpicfBridgeLoopProtectInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBridgeLoopProtectInterval.setStatus("current")
_HpicfBridgeLoopProtectTrapLoopDetectEnable_Type = TruthValue
_HpicfBridgeLoopProtectTrapLoopDetectEnable_Object = MibScalar
hpicfBridgeLoopProtectTrapLoopDetectEnable = _HpicfBridgeLoopProtectTrapLoopDetectEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 5, 1, 2),
    _HpicfBridgeLoopProtectTrapLoopDetectEnable_Type()
)
hpicfBridgeLoopProtectTrapLoopDetectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBridgeLoopProtectTrapLoopDetectEnable.setStatus("current")


class _HpicfBridgeLoopProtectEnableTimer_Type(Integer32):
    """Custom type hpicfBridgeLoopProtectEnableTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpicfBridgeLoopProtectEnableTimer_Type.__name__ = "Integer32"
_HpicfBridgeLoopProtectEnableTimer_Object = MibScalar
hpicfBridgeLoopProtectEnableTimer = _HpicfBridgeLoopProtectEnableTimer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 5, 1, 3),
    _HpicfBridgeLoopProtectEnableTimer_Type()
)
hpicfBridgeLoopProtectEnableTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBridgeLoopProtectEnableTimer.setStatus("current")


class _HpicfBridgeLoopProtectMode_Type(Integer32):
    """Custom type hpicfBridgeLoopProtectMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port", 1),
          ("vlan", 2))
    )


_HpicfBridgeLoopProtectMode_Type.__name__ = "Integer32"
_HpicfBridgeLoopProtectMode_Object = MibScalar
hpicfBridgeLoopProtectMode = _HpicfBridgeLoopProtectMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 5, 1, 4),
    _HpicfBridgeLoopProtectMode_Type()
)
hpicfBridgeLoopProtectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBridgeLoopProtectMode.setStatus("current")
_HpicfBridgeLoopProtectVIDList_Type = VidList
_HpicfBridgeLoopProtectVIDList_Object = MibScalar
hpicfBridgeLoopProtectVIDList = _HpicfBridgeLoopProtectVIDList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 5, 1, 5),
    _HpicfBridgeLoopProtectVIDList_Type()
)
hpicfBridgeLoopProtectVIDList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBridgeLoopProtectVIDList.setStatus("current")
_HpicfBridgeLoopProtectPort_ObjectIdentity = ObjectIdentity
hpicfBridgeLoopProtectPort = _HpicfBridgeLoopProtectPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 5, 2)
)
_HpicfBridgeLoopProtectPortTable_Object = MibTable
hpicfBridgeLoopProtectPortTable = _HpicfBridgeLoopProtectPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfBridgeLoopProtectPortTable.setStatus("current")
_HpicfBridgeLoopProtectPortEntry_Object = MibTableRow
hpicfBridgeLoopProtectPortEntry = _HpicfBridgeLoopProtectPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 5, 2, 1, 1)
)
hpicfBridgeLoopProtectPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpicfBridgeLoopProtectPortEntry.setStatus("current")
_HpicfBridgeLoopProtectPortEnable_Type = TruthValue
_HpicfBridgeLoopProtectPortEnable_Object = MibTableColumn
hpicfBridgeLoopProtectPortEnable = _HpicfBridgeLoopProtectPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 5, 2, 1, 1, 1),
    _HpicfBridgeLoopProtectPortEnable_Type()
)
hpicfBridgeLoopProtectPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBridgeLoopProtectPortEnable.setStatus("current")
_HpicfBridgeLoopProtectPortLoopDetected_Type = TruthValue
_HpicfBridgeLoopProtectPortLoopDetected_Object = MibTableColumn
hpicfBridgeLoopProtectPortLoopDetected = _HpicfBridgeLoopProtectPortLoopDetected_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 5, 2, 1, 1, 2),
    _HpicfBridgeLoopProtectPortLoopDetected_Type()
)
hpicfBridgeLoopProtectPortLoopDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfBridgeLoopProtectPortLoopDetected.setStatus("current")
_HpicfBridgeLoopProtectPortLastLoopTime_Type = TimeStamp
_HpicfBridgeLoopProtectPortLastLoopTime_Object = MibTableColumn
hpicfBridgeLoopProtectPortLastLoopTime = _HpicfBridgeLoopProtectPortLastLoopTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 5, 2, 1, 1, 3),
    _HpicfBridgeLoopProtectPortLastLoopTime_Type()
)
hpicfBridgeLoopProtectPortLastLoopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfBridgeLoopProtectPortLastLoopTime.setStatus("current")
_HpicfBridgeLoopProtectPortLoopCount_Type = Counter32
_HpicfBridgeLoopProtectPortLoopCount_Object = MibTableColumn
hpicfBridgeLoopProtectPortLoopCount = _HpicfBridgeLoopProtectPortLoopCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 5, 2, 1, 1, 4),
    _HpicfBridgeLoopProtectPortLoopCount_Type()
)
hpicfBridgeLoopProtectPortLoopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfBridgeLoopProtectPortLoopCount.setStatus("current")
_HpicfBridgeLoopProtectPortReceiverAction_Type = LoopProtectReceiverAction
_HpicfBridgeLoopProtectPortReceiverAction_Object = MibTableColumn
hpicfBridgeLoopProtectPortReceiverAction = _HpicfBridgeLoopProtectPortReceiverAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 5, 2, 1, 1, 5),
    _HpicfBridgeLoopProtectPortReceiverAction_Type()
)
hpicfBridgeLoopProtectPortReceiverAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBridgeLoopProtectPortReceiverAction.setStatus("current")


class _HpicfBridgeLoopDetectedVlan_Type(Integer32):
    """Custom type hpicfBridgeLoopDetectedVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_HpicfBridgeLoopDetectedVlan_Type.__name__ = "Integer32"
_HpicfBridgeLoopDetectedVlan_Object = MibTableColumn
hpicfBridgeLoopDetectedVlan = _HpicfBridgeLoopDetectedVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 5, 2, 1, 1, 6),
    _HpicfBridgeLoopDetectedVlan_Type()
)
hpicfBridgeLoopDetectedVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfBridgeLoopDetectedVlan.setStatus("current")
_HpicfBridgeMirrorSession_ObjectIdentity = ObjectIdentity
hpicfBridgeMirrorSession = _HpicfBridgeMirrorSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 6)
)
_HpicfBridgeMirrorSessionBase_ObjectIdentity = ObjectIdentity
hpicfBridgeMirrorSessionBase = _HpicfBridgeMirrorSessionBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 6, 1)
)
_HpicfBridgeMirrorSessionDestination_ObjectIdentity = ObjectIdentity
hpicfBridgeMirrorSessionDestination = _HpicfBridgeMirrorSessionDestination_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 6, 2)
)
_HpicfBridgeMirrorSessionTable_Object = MibTable
hpicfBridgeMirrorSessionTable = _HpicfBridgeMirrorSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfBridgeMirrorSessionTable.setStatus("current")
_HpicfBridgeMirrorSessionEntry_Object = MibTableRow
hpicfBridgeMirrorSessionEntry = _HpicfBridgeMirrorSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 6, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfBridgeMirrorSessionEntry.setStatus("current")


class _HpicfBridgeMirrorSessionID_Type(Integer32):
    """Custom type hpicfBridgeMirrorSessionID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpicfBridgeMirrorSessionID_Type.__name__ = "Integer32"
_HpicfBridgeMirrorSessionID_Object = MibTableColumn
hpicfBridgeMirrorSessionID = _HpicfBridgeMirrorSessionID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 6, 2, 1, 1, 1),
    _HpicfBridgeMirrorSessionID_Type()
)
hpicfBridgeMirrorSessionID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBridgeMirrorSessionID.setStatus("current")


class _HpicfBridgeDontTagWithVlan_Type(Integer32):
    """Custom type hpicfBridgeDontTagWithVlan based on Integer32"""
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


_HpicfBridgeDontTagWithVlan_Type.__name__ = "Integer32"
_HpicfBridgeDontTagWithVlan_Object = MibTableColumn
hpicfBridgeDontTagWithVlan = _HpicfBridgeDontTagWithVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 6, 2, 1, 1, 2),
    _HpicfBridgeDontTagWithVlan_Type()
)
hpicfBridgeDontTagWithVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBridgeDontTagWithVlan.setStatus("current")


class _HpicfBridgeMirrorSessionType_Type(Integer32):
    """Custom type hpicfBridgeMirrorSessionType based on Integer32"""
    defaultValue = 1

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
        *(("mirrorAddresses", 2),
          ("mirrorPolicies", 3),
          ("mirrorPorts", 4),
          ("mirrorVlan", 5),
          ("noMirror", 1))
    )


_HpicfBridgeMirrorSessionType_Type.__name__ = "Integer32"
_HpicfBridgeMirrorSessionType_Object = MibTableColumn
hpicfBridgeMirrorSessionType = _HpicfBridgeMirrorSessionType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 6, 2, 1, 1, 3),
    _HpicfBridgeMirrorSessionType_Type()
)
hpicfBridgeMirrorSessionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBridgeMirrorSessionType.setStatus("current")
_HpicfBridgeVoiceVlanConfig_ObjectIdentity = ObjectIdentity
hpicfBridgeVoiceVlanConfig = _HpicfBridgeVoiceVlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 7)
)
_HpicfBridgeVoiceVlanConfigTable_Object = MibTable
hpicfBridgeVoiceVlanConfigTable = _HpicfBridgeVoiceVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 7, 1)
)
if mibBuilder.loadTexts:
    hpicfBridgeVoiceVlanConfigTable.setStatus("current")
_HpicfBridgeVoiceVlanConfigEntry_Object = MibTableRow
hpicfBridgeVoiceVlanConfigEntry = _HpicfBridgeVoiceVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfBridgeVoiceVlanConfigEntry.setStatus("current")


class _HpicfBridgeVoiceVlanEnable_Type(TruthValue):
    """Custom type hpicfBridgeVoiceVlanEnable based on TruthValue"""


_HpicfBridgeVoiceVlanEnable_Object = MibTableColumn
hpicfBridgeVoiceVlanEnable = _HpicfBridgeVoiceVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 7, 1, 1, 1),
    _HpicfBridgeVoiceVlanEnable_Type()
)
hpicfBridgeVoiceVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBridgeVoiceVlanEnable.setStatus("current")
_HpicfBridgeJumboInterfaceConfig_ObjectIdentity = ObjectIdentity
hpicfBridgeJumboInterfaceConfig = _HpicfBridgeJumboInterfaceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 8)
)
_HpicfBridgeJumboInterfaceConfigTable_Object = MibTable
hpicfBridgeJumboInterfaceConfigTable = _HpicfBridgeJumboInterfaceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 8, 1)
)
if mibBuilder.loadTexts:
    hpicfBridgeJumboInterfaceConfigTable.setStatus("current")
_HpicfBridgeJumboInterfaceConfigEntry_Object = MibTableRow
hpicfBridgeJumboInterfaceConfigEntry = _HpicfBridgeJumboInterfaceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 8, 1, 1)
)
hpicfBridgeJumboInterfaceConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpicfBridgeJumboInterfaceConfigEntry.setStatus("current")


class _HpicfBridgeJumboInterfaceEnable_Type(TruthValue):
    """Custom type hpicfBridgeJumboInterfaceEnable based on TruthValue"""


_HpicfBridgeJumboInterfaceEnable_Object = MibTableColumn
hpicfBridgeJumboInterfaceEnable = _HpicfBridgeJumboInterfaceEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 8, 1, 1, 1),
    _HpicfBridgeJumboInterfaceEnable_Type()
)
hpicfBridgeJumboInterfaceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBridgeJumboInterfaceEnable.setStatus("current")
_HpicfBridgeManagementInterfaceConfig_ObjectIdentity = ObjectIdentity
hpicfBridgeManagementInterfaceConfig = _HpicfBridgeManagementInterfaceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 9)
)
_HpicfBridgeManagementInterfaceConfigTable_Object = MibTable
hpicfBridgeManagementInterfaceConfigTable = _HpicfBridgeManagementInterfaceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 9, 1)
)
if mibBuilder.loadTexts:
    hpicfBridgeManagementInterfaceConfigTable.setStatus("current")
_HpicfBridgeManagementInterfaceConfigEntry_Object = MibTableRow
hpicfBridgeManagementInterfaceConfigEntry = _HpicfBridgeManagementInterfaceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 9, 1, 1)
)
hpicfBridgeManagementInterfaceConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpicfBridgeManagementInterfaceConfigEntry.setStatus("current")


class _HpicfBridgeManagementInterfaceEnable_Type(TruthValue):
    """Custom type hpicfBridgeManagementInterfaceEnable based on TruthValue"""


_HpicfBridgeManagementInterfaceEnable_Object = MibTableColumn
hpicfBridgeManagementInterfaceEnable = _HpicfBridgeManagementInterfaceEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 9, 1, 1, 1),
    _HpicfBridgeManagementInterfaceEnable_Type()
)
hpicfBridgeManagementInterfaceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBridgeManagementInterfaceEnable.setStatus("current")
_HpicfBridgeConformance_ObjectIdentity = ObjectIdentity
hpicfBridgeConformance = _HpicfBridgeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 2)
)
_HpicfBridgeGroups_ObjectIdentity = ObjectIdentity
hpicfBridgeGroups = _HpicfBridgeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 2, 1)
)
_HpicfBridgeCompliances_ObjectIdentity = ObjectIdentity
hpicfBridgeCompliances = _HpicfBridgeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 2, 2)
)
_HpicfBridgeNotGroups_ObjectIdentity = ObjectIdentity
hpicfBridgeNotGroups = _HpicfBridgeNotGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 2, 3)
)
dot1dBasePortEntry.registerAugmentions(
    ("HP-ICF-BRIDGE",
     "hpicfBridgeGvrpPortEntry")
)
hpicfBridgeGvrpPortEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
portCopyEntry.registerAugmentions(
    ("HP-ICF-BRIDGE",
     "hpicfBridgeMirrorSessionEntry")
)
hpicfBridgeMirrorSessionEntry.setIndexNames(*portCopyEntry.getIndexNames())
dot1qVlanStaticEntry.registerAugmentions(
    ("HP-ICF-BRIDGE",
     "hpicfBridgeVoiceVlanConfigEntry")
)
hpicfBridgeVoiceVlanConfigEntry.setIndexNames(*dot1qVlanStaticEntry.getIndexNames())

# Managed Objects groups

hpicfBridgeVlanBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 2, 1, 1)
)
hpicfBridgeVlanBaseGroup.setObjects(
      *(("HP-ICF-BRIDGE", "hpicfBridgeMaxVlans"),
        ("HP-ICF-BRIDGE", "hpicfBridgeVlanEnable"),
        ("HP-ICF-BRIDGE", "hpicfBridgePrimaryVlan"),
        ("HP-ICF-BRIDGE", "hpicfBridgeVlanConfigStatus"))
)
if mibBuilder.loadTexts:
    hpicfBridgeVlanBaseGroup.setStatus("current")

hpicfBridgeGvrpPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 2, 1, 2)
)
hpicfBridgeGvrpPortGroup.setObjects(
    ("HP-ICF-BRIDGE", "hpicfBridgeGvrpRestrictedVlanReg")
)
if mibBuilder.loadTexts:
    hpicfBridgeGvrpPortGroup.setStatus("deprecated")

hpicfBridgeRstpBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 2, 1, 3)
)
hpicfBridgeRstpBaseGroup.setObjects(
      *(("HP-ICF-BRIDGE", "hpicfBridgeRstpForceVersion"),
        ("HP-ICF-BRIDGE", "hpicfBridgeRstpConfigStatus"),
        ("HP-ICF-BRIDGE", "hpicfBridgeRstpProtocolVersion"),
        ("HP-ICF-BRIDGE", "hpicfBridgeRstpAdminStatus"))
)
if mibBuilder.loadTexts:
    hpicfBridgeRstpBaseGroup.setStatus("current")

hpicfBridgeLoopProtectBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 2, 1, 4)
)
hpicfBridgeLoopProtectBaseGroup.setObjects(
      *(("HP-ICF-BRIDGE", "hpicfBridgeLoopProtectInterval"),
        ("HP-ICF-BRIDGE", "hpicfBridgeLoopProtectEnableTimer"),
        ("HP-ICF-BRIDGE", "hpicfBridgeLoopProtectTrapLoopDetectEnable"),
        ("HP-ICF-BRIDGE", "hpicfBridgeLoopProtectPortEnable"),
        ("HP-ICF-BRIDGE", "hpicfBridgeLoopProtectPortLoopDetected"),
        ("HP-ICF-BRIDGE", "hpicfBridgeLoopProtectPortLastLoopTime"),
        ("HP-ICF-BRIDGE", "hpicfBridgeLoopProtectPortLoopCount"),
        ("HP-ICF-BRIDGE", "hpicfBridgeLoopProtectPortReceiverAction"))
)
if mibBuilder.loadTexts:
    hpicfBridgeLoopProtectBaseGroup.setStatus("current")

hpicfBridgeMirrorSessionBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 2, 1, 5)
)
hpicfBridgeMirrorSessionBaseGroup.setObjects(
    ("HP-ICF-BRIDGE", "hpicfBridgeMirrorSessionID")
)
if mibBuilder.loadTexts:
    hpicfBridgeMirrorSessionBaseGroup.setStatus("current")

hpicfBridgeVoiceVlanConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 2, 1, 7)
)
hpicfBridgeVoiceVlanConfigGroup.setObjects(
    ("HP-ICF-BRIDGE", "hpicfBridgeVoiceVlanEnable")
)
if mibBuilder.loadTexts:
    hpicfBridgeVoiceVlanConfigGroup.setStatus("current")

hpicfBridgeJumboInterfaceConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 2, 1, 8)
)
hpicfBridgeJumboInterfaceConfigGroup.setObjects(
    ("HP-ICF-BRIDGE", "hpicfBridgeJumboInterfaceEnable")
)
if mibBuilder.loadTexts:
    hpicfBridgeJumboInterfaceConfigGroup.setStatus("current")

hpicfBridgeManagementInterfaceConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 2, 1, 9)
)
hpicfBridgeManagementInterfaceConfigGroup.setObjects(
    ("HP-ICF-BRIDGE", "hpicfBridgeManagementInterfaceEnable")
)
if mibBuilder.loadTexts:
    hpicfBridgeManagementInterfaceConfigGroup.setStatus("current")

hpicfBridgeLoopProtectVLANGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 2, 1, 10)
)
hpicfBridgeLoopProtectVLANGroup.setObjects(
      *(("HP-ICF-BRIDGE", "hpicfBridgeLoopProtectMode"),
        ("HP-ICF-BRIDGE", "hpicfBridgeLoopProtectVIDList"),
        ("HP-ICF-BRIDGE", "hpicfBridgeLoopDetectedVlan"))
)
if mibBuilder.loadTexts:
    hpicfBridgeLoopProtectVLANGroup.setStatus("current")

hpicfBridgeRstpPortEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 2, 1, 11)
)
hpicfBridgeRstpPortEntryGroup.setObjects(
      *(("HP-ICF-BRIDGE", "hpicfBridgeRstpAdminEdgePort"),
        ("HP-ICF-BRIDGE", "hpicfBridgeRstpOperEdgePort"),
        ("HP-ICF-BRIDGE", "hpicfBridgeRstpAdminPointToPointMac"),
        ("HP-ICF-BRIDGE", "hpicfBridgeRstpOperPointToPointMac"),
        ("HP-ICF-BRIDGE", "hpicfBridgeRstpPortPathCost"),
        ("HP-ICF-BRIDGE", "hpicfBridgeRstpForceBpduMigrationCheck"),
        ("HP-ICF-BRIDGE", "hpicfBridgeRstpAutoEdgePort"),
        ("HP-ICF-BRIDGE", "hpicfBridgeRstpPortBpduFiltering"))
)
if mibBuilder.loadTexts:
    hpicfBridgeRstpPortEntryGroup.setStatus("current")

hpicfBridgeMirrorSessionEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 2, 1, 12)
)
hpicfBridgeMirrorSessionEntryGroup.setObjects(
      *(("HP-ICF-BRIDGE", "hpicfBridgeDontTagWithVlan"),
        ("HP-ICF-BRIDGE", "hpicfBridgeMirrorSessionType"))
)
if mibBuilder.loadTexts:
    hpicfBridgeMirrorSessionEntryGroup.setStatus("current")

hpicfBridgeRstpPortEntryGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 2, 1, 13)
)
hpicfBridgeRstpPortEntryGroup1.setObjects(
    ("HP-ICF-BRIDGE", "hpicfBridgeRstpPortIndex")
)
if mibBuilder.loadTexts:
    hpicfBridgeRstpPortEntryGroup1.setStatus("current")

hpicfBridgeGvrpPortGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 2, 1, 14)
)
hpicfBridgeGvrpPortGroup1.setObjects(
      *(("HP-ICF-BRIDGE", "hpicfBridgeGvrpRestrictedVlanReg"),
        ("HP-ICF-BRIDGE", "hpicfApplicantStateMachine"),
        ("HP-ICF-BRIDGE", "hpicfRegistarStateMachine"))
)
if mibBuilder.loadTexts:
    hpicfBridgeGvrpPortGroup1.setStatus("current")

hpicfBridgeStpBpduThrottleConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 2, 1, 15)
)
hpicfBridgeStpBpduThrottleConfigGroup.setObjects(
      *(("HP-ICF-BRIDGE", "hpicfBridgeStpBpduThrottleStatus"),
        ("HP-ICF-BRIDGE", "hpicfBridgeStpBpduThrottleValue"))
)
if mibBuilder.loadTexts:
    hpicfBridgeStpBpduThrottleConfigGroup.setStatus("current")


# Notification objects

hpicfBridgeLoopProtectLoopDetectedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 5, 0, 1)
)
hpicfBridgeLoopProtectLoopDetectedNotification.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HP-ICF-BRIDGE", "hpicfBridgeLoopProtectPortLoopCount"),
        ("HP-ICF-BRIDGE", "hpicfBridgeLoopProtectPortReceiverAction"))
)
if mibBuilder.loadTexts:
    hpicfBridgeLoopProtectLoopDetectedNotification.setStatus(
        "current"
    )

hpicfBridgeVlanLoopProtectLoopDetectedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 1, 5, 0, 2)
)
hpicfBridgeVlanLoopProtectLoopDetectedNotification.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HP-ICF-BRIDGE", "hpicfBridgeLoopProtectPortLoopCount"),
        ("HP-ICF-BRIDGE", "hpicfBridgeLoopProtectPortReceiverAction"),
        ("HP-ICF-BRIDGE", "hpicfBridgeLoopDetectedVlan"))
)
if mibBuilder.loadTexts:
    hpicfBridgeVlanLoopProtectLoopDetectedNotification.setStatus(
        "current"
    )


# Notifications groups

hpicfBridgeLoopProtectNotGrp = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 2, 3, 1)
)
hpicfBridgeLoopProtectNotGrp.setObjects(
    ("HP-ICF-BRIDGE", "hpicfBridgeLoopProtectLoopDetectedNotification")
)
if mibBuilder.loadTexts:
    hpicfBridgeLoopProtectNotGrp.setStatus(
        "current"
    )

hpicfBridgeVlanLoopProtectNotGrp = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 2, 3, 2)
)
hpicfBridgeVlanLoopProtectNotGrp.setObjects(
    ("HP-ICF-BRIDGE", "hpicfBridgeVlanLoopProtectLoopDetectedNotification")
)
if mibBuilder.loadTexts:
    hpicfBridgeVlanLoopProtectNotGrp.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicfBridgeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfBridgeCompliance.setStatus(
        "deprecated"
    )

hpicfBridgeComplianceRevTwo = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hpicfBridgeComplianceRevTwo.setStatus(
        "deprecated"
    )

hpicfBridgeComplianceRevThree = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 2, 2, 3)
)
if mibBuilder.loadTexts:
    hpicfBridgeComplianceRevThree.setStatus(
        "deprecated"
    )

hpicfBridgeComplianceRevFour = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 2, 2, 4)
)
if mibBuilder.loadTexts:
    hpicfBridgeComplianceRevFour.setStatus(
        "deprecated"
    )

hpicfBridgeLoopProtectCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 2, 2, 5)
)
if mibBuilder.loadTexts:
    hpicfBridgeLoopProtectCompliance.setStatus(
        "current"
    )

hpicfBridgeVlanBaseConfigCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 2, 2, 6)
)
if mibBuilder.loadTexts:
    hpicfBridgeVlanBaseConfigCompliance.setStatus(
        "current"
    )

hpicfBridgeInterfaceConfigCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 2, 2, 7)
)
if mibBuilder.loadTexts:
    hpicfBridgeInterfaceConfigCompliance.setStatus(
        "current"
    )

hpicfBridgeVlanLoopProtConfigCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 2, 2, 8)
)
if mibBuilder.loadTexts:
    hpicfBridgeVlanLoopProtConfigCompliance.setStatus(
        "current"
    )

hpicfBridgeRstpPortEntryCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 2, 2, 9)
)
if mibBuilder.loadTexts:
    hpicfBridgeRstpPortEntryCompliance.setStatus(
        "current"
    )

hpicfBridgeMirrorSessionEntryCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 2, 2, 10)
)
if mibBuilder.loadTexts:
    hpicfBridgeMirrorSessionEntryCompliance.setStatus(
        "current"
    )

hpicfBridgeRstpPortEntryCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 2, 2, 11)
)
if mibBuilder.loadTexts:
    hpicfBridgeRstpPortEntryCompliance1.setStatus(
        "current"
    )

hpicfBridgeComplianceRevFour1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 2, 2, 12)
)
if mibBuilder.loadTexts:
    hpicfBridgeComplianceRevFour1.setStatus(
        "current"
    )

hpicfBridgeStpBpduThrottleConfigCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12, 2, 2, 13)
)
if mibBuilder.loadTexts:
    hpicfBridgeStpBpduThrottleConfigCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-BRIDGE",
    **{"BridgeId": BridgeId,
       "LoopProtectReceiverAction": LoopProtectReceiverAction,
       "hpicfBridge": hpicfBridge,
       "hpicfBridgeObjects": hpicfBridgeObjects,
       "hpicfBridgeBase": hpicfBridgeBase,
       "hpicfBridgeMaxVlans": hpicfBridgeMaxVlans,
       "hpicfBridgeVlanEnable": hpicfBridgeVlanEnable,
       "hpicfBridgePrimaryVlan": hpicfBridgePrimaryVlan,
       "hpicfBridgeVlanConfigStatus": hpicfBridgeVlanConfigStatus,
       "hpicfBridgeGvrp": hpicfBridgeGvrp,
       "hpicfBridgeGvrpPortTable": hpicfBridgeGvrpPortTable,
       "hpicfBridgeGvrpPortEntry": hpicfBridgeGvrpPortEntry,
       "hpicfBridgeGvrpRestrictedVlanReg": hpicfBridgeGvrpRestrictedVlanReg,
       "hpicfBridgeGvrpStateMachineTable": hpicfBridgeGvrpStateMachineTable,
       "hpicfBridgeGvrpStateMachineEntry": hpicfBridgeGvrpStateMachineEntry,
       "hpicfGenericVlanId": hpicfGenericVlanId,
       "hpicfApplicantStateMachine": hpicfApplicantStateMachine,
       "hpicfRegistarStateMachine": hpicfRegistarStateMachine,
       "hpicfBridgeRstp": hpicfBridgeRstp,
       "hpicfBridgeRstpForceVersion": hpicfBridgeRstpForceVersion,
       "hpicfBridgeRstpConfigStatus": hpicfBridgeRstpConfigStatus,
       "hpicfBridgeRstpProtocolVersion": hpicfBridgeRstpProtocolVersion,
       "hpicfBridgeRstpAdminStatus": hpicfBridgeRstpAdminStatus,
       "hpicfBridgeRstpPortTable": hpicfBridgeRstpPortTable,
       "hpicfBridgeRstpPortEntry": hpicfBridgeRstpPortEntry,
       "hpicfBridgeRstpPortIndex": hpicfBridgeRstpPortIndex,
       "hpicfBridgeRstpAdminEdgePort": hpicfBridgeRstpAdminEdgePort,
       "hpicfBridgeRstpOperEdgePort": hpicfBridgeRstpOperEdgePort,
       "hpicfBridgeRstpAdminPointToPointMac": hpicfBridgeRstpAdminPointToPointMac,
       "hpicfBridgeRstpOperPointToPointMac": hpicfBridgeRstpOperPointToPointMac,
       "hpicfBridgeRstpPortPathCost": hpicfBridgeRstpPortPathCost,
       "hpicfBridgeRstpForceBpduMigrationCheck": hpicfBridgeRstpForceBpduMigrationCheck,
       "hpicfBridgeRstpAutoEdgePort": hpicfBridgeRstpAutoEdgePort,
       "hpicfBridgeRstpPortBpduFiltering": hpicfBridgeRstpPortBpduFiltering,
       "hpicfBridgeStpBpduThrottleConfig": hpicfBridgeStpBpduThrottleConfig,
       "hpicfBridgeStpBpduThrottleStatus": hpicfBridgeStpBpduThrottleStatus,
       "hpicfBridgeStpBpduThrottleValue": hpicfBridgeStpBpduThrottleValue,
       "hpicfBridgeLoopProtect": hpicfBridgeLoopProtect,
       "hpicfBridgeLoopProtectNotifications": hpicfBridgeLoopProtectNotifications,
       "hpicfBridgeLoopProtectLoopDetectedNotification": hpicfBridgeLoopProtectLoopDetectedNotification,
       "hpicfBridgeVlanLoopProtectLoopDetectedNotification": hpicfBridgeVlanLoopProtectLoopDetectedNotification,
       "hpicfBridgeLoopProtectBase": hpicfBridgeLoopProtectBase,
       "hpicfBridgeLoopProtectInterval": hpicfBridgeLoopProtectInterval,
       "hpicfBridgeLoopProtectTrapLoopDetectEnable": hpicfBridgeLoopProtectTrapLoopDetectEnable,
       "hpicfBridgeLoopProtectEnableTimer": hpicfBridgeLoopProtectEnableTimer,
       "hpicfBridgeLoopProtectMode": hpicfBridgeLoopProtectMode,
       "hpicfBridgeLoopProtectVIDList": hpicfBridgeLoopProtectVIDList,
       "hpicfBridgeLoopProtectPort": hpicfBridgeLoopProtectPort,
       "hpicfBridgeLoopProtectPortTable": hpicfBridgeLoopProtectPortTable,
       "hpicfBridgeLoopProtectPortEntry": hpicfBridgeLoopProtectPortEntry,
       "hpicfBridgeLoopProtectPortEnable": hpicfBridgeLoopProtectPortEnable,
       "hpicfBridgeLoopProtectPortLoopDetected": hpicfBridgeLoopProtectPortLoopDetected,
       "hpicfBridgeLoopProtectPortLastLoopTime": hpicfBridgeLoopProtectPortLastLoopTime,
       "hpicfBridgeLoopProtectPortLoopCount": hpicfBridgeLoopProtectPortLoopCount,
       "hpicfBridgeLoopProtectPortReceiverAction": hpicfBridgeLoopProtectPortReceiverAction,
       "hpicfBridgeLoopDetectedVlan": hpicfBridgeLoopDetectedVlan,
       "hpicfBridgeMirrorSession": hpicfBridgeMirrorSession,
       "hpicfBridgeMirrorSessionBase": hpicfBridgeMirrorSessionBase,
       "hpicfBridgeMirrorSessionDestination": hpicfBridgeMirrorSessionDestination,
       "hpicfBridgeMirrorSessionTable": hpicfBridgeMirrorSessionTable,
       "hpicfBridgeMirrorSessionEntry": hpicfBridgeMirrorSessionEntry,
       "hpicfBridgeMirrorSessionID": hpicfBridgeMirrorSessionID,
       "hpicfBridgeDontTagWithVlan": hpicfBridgeDontTagWithVlan,
       "hpicfBridgeMirrorSessionType": hpicfBridgeMirrorSessionType,
       "hpicfBridgeVoiceVlanConfig": hpicfBridgeVoiceVlanConfig,
       "hpicfBridgeVoiceVlanConfigTable": hpicfBridgeVoiceVlanConfigTable,
       "hpicfBridgeVoiceVlanConfigEntry": hpicfBridgeVoiceVlanConfigEntry,
       "hpicfBridgeVoiceVlanEnable": hpicfBridgeVoiceVlanEnable,
       "hpicfBridgeJumboInterfaceConfig": hpicfBridgeJumboInterfaceConfig,
       "hpicfBridgeJumboInterfaceConfigTable": hpicfBridgeJumboInterfaceConfigTable,
       "hpicfBridgeJumboInterfaceConfigEntry": hpicfBridgeJumboInterfaceConfigEntry,
       "hpicfBridgeJumboInterfaceEnable": hpicfBridgeJumboInterfaceEnable,
       "hpicfBridgeManagementInterfaceConfig": hpicfBridgeManagementInterfaceConfig,
       "hpicfBridgeManagementInterfaceConfigTable": hpicfBridgeManagementInterfaceConfigTable,
       "hpicfBridgeManagementInterfaceConfigEntry": hpicfBridgeManagementInterfaceConfigEntry,
       "hpicfBridgeManagementInterfaceEnable": hpicfBridgeManagementInterfaceEnable,
       "hpicfBridgeConformance": hpicfBridgeConformance,
       "hpicfBridgeGroups": hpicfBridgeGroups,
       "hpicfBridgeVlanBaseGroup": hpicfBridgeVlanBaseGroup,
       "hpicfBridgeGvrpPortGroup": hpicfBridgeGvrpPortGroup,
       "hpicfBridgeRstpBaseGroup": hpicfBridgeRstpBaseGroup,
       "hpicfBridgeLoopProtectBaseGroup": hpicfBridgeLoopProtectBaseGroup,
       "hpicfBridgeMirrorSessionBaseGroup": hpicfBridgeMirrorSessionBaseGroup,
       "hpicfBridgeVoiceVlanConfigGroup": hpicfBridgeVoiceVlanConfigGroup,
       "hpicfBridgeJumboInterfaceConfigGroup": hpicfBridgeJumboInterfaceConfigGroup,
       "hpicfBridgeManagementInterfaceConfigGroup": hpicfBridgeManagementInterfaceConfigGroup,
       "hpicfBridgeLoopProtectVLANGroup": hpicfBridgeLoopProtectVLANGroup,
       "hpicfBridgeRstpPortEntryGroup": hpicfBridgeRstpPortEntryGroup,
       "hpicfBridgeMirrorSessionEntryGroup": hpicfBridgeMirrorSessionEntryGroup,
       "hpicfBridgeRstpPortEntryGroup1": hpicfBridgeRstpPortEntryGroup1,
       "hpicfBridgeGvrpPortGroup1": hpicfBridgeGvrpPortGroup1,
       "hpicfBridgeStpBpduThrottleConfigGroup": hpicfBridgeStpBpduThrottleConfigGroup,
       "hpicfBridgeCompliances": hpicfBridgeCompliances,
       "hpicfBridgeCompliance": hpicfBridgeCompliance,
       "hpicfBridgeComplianceRevTwo": hpicfBridgeComplianceRevTwo,
       "hpicfBridgeComplianceRevThree": hpicfBridgeComplianceRevThree,
       "hpicfBridgeComplianceRevFour": hpicfBridgeComplianceRevFour,
       "hpicfBridgeLoopProtectCompliance": hpicfBridgeLoopProtectCompliance,
       "hpicfBridgeVlanBaseConfigCompliance": hpicfBridgeVlanBaseConfigCompliance,
       "hpicfBridgeInterfaceConfigCompliance": hpicfBridgeInterfaceConfigCompliance,
       "hpicfBridgeVlanLoopProtConfigCompliance": hpicfBridgeVlanLoopProtConfigCompliance,
       "hpicfBridgeRstpPortEntryCompliance": hpicfBridgeRstpPortEntryCompliance,
       "hpicfBridgeMirrorSessionEntryCompliance": hpicfBridgeMirrorSessionEntryCompliance,
       "hpicfBridgeRstpPortEntryCompliance1": hpicfBridgeRstpPortEntryCompliance1,
       "hpicfBridgeComplianceRevFour1": hpicfBridgeComplianceRevFour1,
       "hpicfBridgeStpBpduThrottleConfigCompliance": hpicfBridgeStpBpduThrottleConfigCompliance,
       "hpicfBridgeNotGroups": hpicfBridgeNotGroups,
       "hpicfBridgeLoopProtectNotGrp": hpicfBridgeLoopProtectNotGrp,
       "hpicfBridgeVlanLoopProtectNotGrp": hpicfBridgeVlanLoopProtectNotGrp}
)
