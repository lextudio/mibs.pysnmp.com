# SNMP MIB module (CISCO-EVC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-EVC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:03 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoCosList,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoCosList")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(VlanId,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId",
    "VlanIdOrNone")

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
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoEvcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 613)
)
ciscoEvcMIB.setRevisions(
        ("2012-05-21 00:00",
         "2008-05-01 00:00",
         "2007-12-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CevcMacSecurityViolationCauseType(Integer32, TextualConvention):
    status = "current"
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
        *(("blackListDeny", 4),
          ("exceedBdLimit", 2),
          ("exceedSILimit", 3),
          ("exceedSystemLimit", 1))
    )



class CiscoEvcIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class CiscoEvcIndexOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class CevcL2ControlProtocolType(Integer32, TextualConvention):
    status = "current"
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
        *(("cdp", 2),
          ("dot1x", 8),
          ("dtp", 3),
          ("lacp", 7),
          ("other", 1),
          ("pagp", 4),
          ("stp", 9),
          ("udld", 5),
          ("vtp", 6))
    )



class ServiceInstanceTarget(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )



class ServiceInstanceTargetType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interface", 2),
          ("other", 1))
    )



class ServiceInstanceInterface(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoEvcMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoEvcMIBNotifications = _CiscoEvcMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 0)
)
_CiscoEvcNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoEvcNotificationPrefix = _CiscoEvcNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 0, 0)
)
_CiscoEvcMIBObjects_ObjectIdentity = ObjectIdentity
ciscoEvcMIBObjects = _CiscoEvcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1)
)
_CevcSystem_ObjectIdentity = ObjectIdentity
cevcSystem = _CevcSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 1)
)
_CevcMaxNumEvcs_Type = Gauge32
_CevcMaxNumEvcs_Object = MibScalar
cevcMaxNumEvcs = _CevcMaxNumEvcs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 1, 1),
    _CevcMaxNumEvcs_Type()
)
cevcMaxNumEvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cevcMaxNumEvcs.setStatus("current")
_CevcNumCfgEvcs_Type = Gauge32
_CevcNumCfgEvcs_Object = MibScalar
cevcNumCfgEvcs = _CevcNumCfgEvcs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 1, 2),
    _CevcNumCfgEvcs_Type()
)
cevcNumCfgEvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cevcNumCfgEvcs.setStatus("current")
_CevcPort_ObjectIdentity = ObjectIdentity
cevcPort = _CevcPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 2)
)
_CevcPortTable_Object = MibTable
cevcPortTable = _CevcPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cevcPortTable.setStatus("current")
_CevcPortEntry_Object = MibTableRow
cevcPortEntry = _CevcPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 2, 1, 1)
)
cevcPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cevcPortEntry.setStatus("current")


class _CevcPortMode_Type(Integer32):
    """Custom type cevcPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nni", 2),
          ("uni", 1))
    )


_CevcPortMode_Type.__name__ = "Integer32"
_CevcPortMode_Object = MibTableColumn
cevcPortMode = _CevcPortMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 2, 1, 1, 1),
    _CevcPortMode_Type()
)
cevcPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cevcPortMode.setStatus("current")
_CevcPortMaxNumEVCs_Type = Gauge32
_CevcPortMaxNumEVCs_Object = MibTableColumn
cevcPortMaxNumEVCs = _CevcPortMaxNumEVCs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 2, 1, 1, 2),
    _CevcPortMaxNumEVCs_Type()
)
cevcPortMaxNumEVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cevcPortMaxNumEVCs.setStatus("current")
_CevcPortMaxNumServiceInstances_Type = Gauge32
_CevcPortMaxNumServiceInstances_Object = MibTableColumn
cevcPortMaxNumServiceInstances = _CevcPortMaxNumServiceInstances_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 2, 1, 1, 3),
    _CevcPortMaxNumServiceInstances_Type()
)
cevcPortMaxNumServiceInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cevcPortMaxNumServiceInstances.setStatus("current")
_CevcUniTable_Object = MibTable
cevcUniTable = _CevcUniTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cevcUniTable.setStatus("current")
_CevcUniEntry_Object = MibTableRow
cevcUniEntry = _CevcUniEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 2, 2, 1)
)
cevcUniEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cevcUniEntry.setStatus("current")


class _CevcUniIdentifier_Type(SnmpAdminString):
    """Custom type cevcUniIdentifier based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CevcUniIdentifier_Type.__name__ = "SnmpAdminString"
_CevcUniIdentifier_Object = MibTableColumn
cevcUniIdentifier = _CevcUniIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 2, 2, 1, 1),
    _CevcUniIdentifier_Type()
)
cevcUniIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcUniIdentifier.setStatus("current")


class _CevcUniPortType_Type(Integer32):
    """Custom type cevcUniPortType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot1ad", 2),
          ("dot1q", 1))
    )


_CevcUniPortType_Type.__name__ = "Integer32"
_CevcUniPortType_Object = MibTableColumn
cevcUniPortType = _CevcUniPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 2, 2, 1, 2),
    _CevcUniPortType_Type()
)
cevcUniPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcUniPortType.setStatus("current")


class _CevcUniServiceAttributes_Type(Bits):
    """Custom type cevcUniServiceAttributes based on Bits"""
    defaultBinValue = "11"

    namedValues = NamedValues(
        *(("allToOneBundling", 2),
          ("bundling", 1),
          ("serviceMultiplexing", 0))
    )

_CevcUniServiceAttributes_Type.__name__ = "Bits"
_CevcUniServiceAttributes_Object = MibTableColumn
cevcUniServiceAttributes = _CevcUniServiceAttributes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 2, 2, 1, 3),
    _CevcUniServiceAttributes_Type()
)
cevcUniServiceAttributes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcUniServiceAttributes.setStatus("current")
_CevcPortL2ControlProtocolTable_Object = MibTable
cevcPortL2ControlProtocolTable = _CevcPortL2ControlProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cevcPortL2ControlProtocolTable.setStatus("current")
_CevcPortL2ControlProtocolEntry_Object = MibTableRow
cevcPortL2ControlProtocolEntry = _CevcPortL2ControlProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 2, 3, 1)
)
cevcPortL2ControlProtocolEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-EVC-MIB", "cevcPortL2ControlProtocolType"),
)
if mibBuilder.loadTexts:
    cevcPortL2ControlProtocolEntry.setStatus("current")
_CevcPortL2ControlProtocolType_Type = CevcL2ControlProtocolType
_CevcPortL2ControlProtocolType_Object = MibTableColumn
cevcPortL2ControlProtocolType = _CevcPortL2ControlProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 2, 3, 1, 1),
    _CevcPortL2ControlProtocolType_Type()
)
cevcPortL2ControlProtocolType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cevcPortL2ControlProtocolType.setStatus("current")


class _CevcPortL2ControlProtocolAction_Type(Integer32):
    """Custom type cevcPortL2ControlProtocolAction based on Integer32"""
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
        *(("discard", 1),
          ("passToEvc", 3),
          ("peer", 2),
          ("peerAndPassToEvc", 4))
    )


_CevcPortL2ControlProtocolAction_Type.__name__ = "Integer32"
_CevcPortL2ControlProtocolAction_Object = MibTableColumn
cevcPortL2ControlProtocolAction = _CevcPortL2ControlProtocolAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 2, 3, 1, 2),
    _CevcPortL2ControlProtocolAction_Type()
)
cevcPortL2ControlProtocolAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcPortL2ControlProtocolAction.setStatus("current")
_CevcUniCEVlanEvcTable_Object = MibTable
cevcUniCEVlanEvcTable = _CevcUniCEVlanEvcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cevcUniCEVlanEvcTable.setStatus("current")
_CevcUniCEVlanEvcEntry_Object = MibTableRow
cevcUniCEVlanEvcEntry = _CevcUniCEVlanEvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 2, 4, 1)
)
cevcUniCEVlanEvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-EVC-MIB", "cevcUniEvcIndex"),
    (0, "CISCO-EVC-MIB", "cevcUniCEVlanEvcBeginningVlan"),
)
if mibBuilder.loadTexts:
    cevcUniCEVlanEvcEntry.setStatus("current")
_CevcUniEvcIndex_Type = CiscoEvcIndex
_CevcUniEvcIndex_Object = MibTableColumn
cevcUniEvcIndex = _CevcUniEvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 2, 4, 1, 1),
    _CevcUniEvcIndex_Type()
)
cevcUniEvcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cevcUniEvcIndex.setStatus("current")
_CevcUniCEVlanEvcBeginningVlan_Type = VlanId
_CevcUniCEVlanEvcBeginningVlan_Object = MibTableColumn
cevcUniCEVlanEvcBeginningVlan = _CevcUniCEVlanEvcBeginningVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 2, 4, 1, 2),
    _CevcUniCEVlanEvcBeginningVlan_Type()
)
cevcUniCEVlanEvcBeginningVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cevcUniCEVlanEvcBeginningVlan.setStatus("current")
_CevcUniCEVlanEvcEndingVlan_Type = VlanIdOrNone
_CevcUniCEVlanEvcEndingVlan_Object = MibTableColumn
cevcUniCEVlanEvcEndingVlan = _CevcUniCEVlanEvcEndingVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 2, 4, 1, 3),
    _CevcUniCEVlanEvcEndingVlan_Type()
)
cevcUniCEVlanEvcEndingVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cevcUniCEVlanEvcEndingVlan.setStatus("current")
_CevcEvc_ObjectIdentity = ObjectIdentity
cevcEvc = _CevcEvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 3)
)
_CevcEvcTable_Object = MibTable
cevcEvcTable = _CevcEvcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cevcEvcTable.setStatus("current")
_CevcEvcEntry_Object = MibTableRow
cevcEvcEntry = _CevcEvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 3, 1, 1)
)
cevcEvcEntry.setIndexNames(
    (0, "CISCO-EVC-MIB", "cevcEvcIndex"),
)
if mibBuilder.loadTexts:
    cevcEvcEntry.setStatus("current")
_CevcEvcIndex_Type = CiscoEvcIndex
_CevcEvcIndex_Object = MibTableColumn
cevcEvcIndex = _CevcEvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 3, 1, 1, 1),
    _CevcEvcIndex_Type()
)
cevcEvcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cevcEvcIndex.setStatus("current")
_CevcEvcRowStatus_Type = RowStatus
_CevcEvcRowStatus_Object = MibTableColumn
cevcEvcRowStatus = _CevcEvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 3, 1, 1, 2),
    _CevcEvcRowStatus_Type()
)
cevcEvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcEvcRowStatus.setStatus("current")


class _CevcEvcStorageType_Type(StorageType):
    """Custom type cevcEvcStorageType based on StorageType"""


_CevcEvcStorageType_Object = MibTableColumn
cevcEvcStorageType = _CevcEvcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 3, 1, 1, 3),
    _CevcEvcStorageType_Type()
)
cevcEvcStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcEvcStorageType.setStatus("current")


class _CevcEvcIdentifier_Type(SnmpAdminString):
    """Custom type cevcEvcIdentifier based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CevcEvcIdentifier_Type.__name__ = "SnmpAdminString"
_CevcEvcIdentifier_Object = MibTableColumn
cevcEvcIdentifier = _CevcEvcIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 3, 1, 1, 4),
    _CevcEvcIdentifier_Type()
)
cevcEvcIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcEvcIdentifier.setStatus("current")


class _CevcEvcType_Type(Integer32):
    """Custom type cevcEvcType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multipointToMultipoint", 2),
          ("pointToPoint", 1))
    )


_CevcEvcType_Type.__name__ = "Integer32"
_CevcEvcType_Object = MibTableColumn
cevcEvcType = _CevcEvcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 3, 1, 1, 5),
    _CevcEvcType_Type()
)
cevcEvcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcEvcType.setStatus("current")


class _CevcEvcCfgUnis_Type(Unsigned32):
    """Custom type cevcEvcCfgUnis based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4294967295),
    )


_CevcEvcCfgUnis_Type.__name__ = "Unsigned32"
_CevcEvcCfgUnis_Object = MibTableColumn
cevcEvcCfgUnis = _CevcEvcCfgUnis_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 3, 1, 1, 6),
    _CevcEvcCfgUnis_Type()
)
cevcEvcCfgUnis.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcEvcCfgUnis.setStatus("current")
_CevcEvcStateTable_Object = MibTable
cevcEvcStateTable = _CevcEvcStateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cevcEvcStateTable.setStatus("current")
_CevcEvcStateEntry_Object = MibTableRow
cevcEvcStateEntry = _CevcEvcStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 3, 2, 1)
)
cevcEvcStateEntry.setIndexNames(
    (0, "CISCO-EVC-MIB", "cevcEvcIndex"),
)
if mibBuilder.loadTexts:
    cevcEvcStateEntry.setStatus("current")


class _CevcEvcOperStatus_Type(Integer32):
    """Custom type cevcEvcOperStatus based on Integer32"""
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
        *(("active", 2),
          ("inactive", 4),
          ("partiallyActive", 3),
          ("unknown", 1))
    )


_CevcEvcOperStatus_Type.__name__ = "Integer32"
_CevcEvcOperStatus_Object = MibTableColumn
cevcEvcOperStatus = _CevcEvcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 3, 2, 1, 1),
    _CevcEvcOperStatus_Type()
)
cevcEvcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cevcEvcOperStatus.setStatus("current")
_CevcEvcActiveUnis_Type = Gauge32
_CevcEvcActiveUnis_Object = MibTableColumn
cevcEvcActiveUnis = _CevcEvcActiveUnis_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 3, 2, 1, 2),
    _CevcEvcActiveUnis_Type()
)
cevcEvcActiveUnis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cevcEvcActiveUnis.setStatus("current")
_CevcEvcUniTable_Object = MibTable
cevcEvcUniTable = _CevcEvcUniTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cevcEvcUniTable.setStatus("current")
_CevcEvcUniEntry_Object = MibTableRow
cevcEvcUniEntry = _CevcEvcUniEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 3, 3, 1)
)
cevcEvcUniEntry.setIndexNames(
    (0, "CISCO-EVC-MIB", "cevcEvcIndex"),
    (0, "CISCO-EVC-MIB", "cevcEvcUniIndex"),
)
if mibBuilder.loadTexts:
    cevcEvcUniEntry.setStatus("current")


class _CevcEvcUniIndex_Type(Unsigned32):
    """Custom type cevcEvcUniIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CevcEvcUniIndex_Type.__name__ = "Unsigned32"
_CevcEvcUniIndex_Object = MibTableColumn
cevcEvcUniIndex = _CevcEvcUniIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 3, 3, 1, 1),
    _CevcEvcUniIndex_Type()
)
cevcEvcUniIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cevcEvcUniIndex.setStatus("current")


class _CevcEvcUniId_Type(SnmpAdminString):
    """Custom type cevcEvcUniId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CevcEvcUniId_Type.__name__ = "SnmpAdminString"
_CevcEvcUniId_Object = MibTableColumn
cevcEvcUniId = _CevcEvcUniId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 3, 3, 1, 2),
    _CevcEvcUniId_Type()
)
cevcEvcUniId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cevcEvcUniId.setStatus("current")


class _CevcEvcUniOperStatus_Type(Integer32):
    """Custom type cevcEvcUniOperStatus based on Integer32"""
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
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("adminDown", 5),
          ("down", 4),
          ("localExcessiveError", 6),
          ("localInLoopback", 8),
          ("localOutLoopback", 10),
          ("notReachable", 2),
          ("remoteExcessiveError", 7),
          ("remoteInLoopback", 9),
          ("remoteOutLoopback", 11),
          ("unknown", 1),
          ("up", 3))
    )


_CevcEvcUniOperStatus_Type.__name__ = "Integer32"
_CevcEvcUniOperStatus_Object = MibTableColumn
cevcEvcUniOperStatus = _CevcEvcUniOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 3, 3, 1, 3),
    _CevcEvcUniOperStatus_Type()
)
cevcEvcUniOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cevcEvcUniOperStatus.setStatus("current")
_CevcEvcLocalUniIfIndex_Type = InterfaceIndexOrZero
_CevcEvcLocalUniIfIndex_Object = MibTableColumn
cevcEvcLocalUniIfIndex = _CevcEvcLocalUniIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 3, 3, 1, 4),
    _CevcEvcLocalUniIfIndex_Type()
)
cevcEvcLocalUniIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cevcEvcLocalUniIfIndex.setStatus("current")
_CevcServiceInstance_ObjectIdentity = ObjectIdentity
cevcServiceInstance = _CevcServiceInstance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4)
)
_CevcSITable_Object = MibTable
cevcSITable = _CevcSITable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cevcSITable.setStatus("current")
_CevcSIEntry_Object = MibTableRow
cevcSIEntry = _CevcSIEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 1, 1)
)
cevcSIEntry.setIndexNames(
    (0, "CISCO-EVC-MIB", "cevcSIIndex"),
)
if mibBuilder.loadTexts:
    cevcSIEntry.setStatus("current")


class _CevcSIIndex_Type(Unsigned32):
    """Custom type cevcSIIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CevcSIIndex_Type.__name__ = "Unsigned32"
_CevcSIIndex_Object = MibTableColumn
cevcSIIndex = _CevcSIIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 1, 1, 1),
    _CevcSIIndex_Type()
)
cevcSIIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cevcSIIndex.setStatus("current")
_CevcSIRowStatus_Type = RowStatus
_CevcSIRowStatus_Object = MibTableColumn
cevcSIRowStatus = _CevcSIRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 1, 1, 2),
    _CevcSIRowStatus_Type()
)
cevcSIRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIRowStatus.setStatus("current")


class _CevcSIStorageType_Type(StorageType):
    """Custom type cevcSIStorageType based on StorageType"""


_CevcSIStorageType_Object = MibTableColumn
cevcSIStorageType = _CevcSIStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 1, 1, 3),
    _CevcSIStorageType_Type()
)
cevcSIStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIStorageType.setStatus("current")
_CevcSITargetType_Type = ServiceInstanceTargetType
_CevcSITargetType_Object = MibTableColumn
cevcSITargetType = _CevcSITargetType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 1, 1, 4),
    _CevcSITargetType_Type()
)
cevcSITargetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSITargetType.setStatus("current")
_CevcSITarget_Type = ServiceInstanceTarget
_CevcSITarget_Object = MibTableColumn
cevcSITarget = _CevcSITarget_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 1, 1, 5),
    _CevcSITarget_Type()
)
cevcSITarget.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSITarget.setStatus("current")
_CevcSIName_Type = SnmpAdminString
_CevcSIName_Object = MibTableColumn
cevcSIName = _CevcSIName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 1, 1, 6),
    _CevcSIName_Type()
)
cevcSIName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIName.setStatus("current")


class _CevcSIEvcIndex_Type(CiscoEvcIndexOrZero):
    """Custom type cevcSIEvcIndex based on CiscoEvcIndexOrZero"""
    defaultValue = 0


_CevcSIEvcIndex_Object = MibTableColumn
cevcSIEvcIndex = _CevcSIEvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 1, 1, 7),
    _CevcSIEvcIndex_Type()
)
cevcSIEvcIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIEvcIndex.setStatus("current")


class _CevcSIAdminStatus_Type(Integer32):
    """Custom type cevcSIAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CevcSIAdminStatus_Type.__name__ = "Integer32"
_CevcSIAdminStatus_Object = MibTableColumn
cevcSIAdminStatus = _CevcSIAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 1, 1, 8),
    _CevcSIAdminStatus_Type()
)
cevcSIAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIAdminStatus.setStatus("current")


class _CevcSIForwardingType_Type(Integer32):
    """Custom type cevcSIForwardingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bridgeDomain", 1),
          ("other", 0))
    )


_CevcSIForwardingType_Type.__name__ = "Integer32"
_CevcSIForwardingType_Object = MibTableColumn
cevcSIForwardingType = _CevcSIForwardingType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 1, 1, 9),
    _CevcSIForwardingType_Type()
)
cevcSIForwardingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIForwardingType.setStatus("current")


class _CevcSICreationType_Type(Integer32):
    """Custom type cevcSICreationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_CevcSICreationType_Type.__name__ = "Integer32"
_CevcSICreationType_Object = MibTableColumn
cevcSICreationType = _CevcSICreationType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 1, 1, 10),
    _CevcSICreationType_Type()
)
cevcSICreationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cevcSICreationType.setStatus("current")


class _CevcSIType_Type(Integer32):
    """Custom type cevcSIType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("l2context", 3),
          ("regular", 1),
          ("trunk", 2))
    )


_CevcSIType_Type.__name__ = "Integer32"
_CevcSIType_Object = MibTableColumn
cevcSIType = _CevcSIType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 1, 1, 11),
    _CevcSIType_Type()
)
cevcSIType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIType.setStatus("current")
_CevcSIStateTable_Object = MibTable
cevcSIStateTable = _CevcSIStateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cevcSIStateTable.setStatus("current")
_CevcSIStateEntry_Object = MibTableRow
cevcSIStateEntry = _CevcSIStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 2, 1)
)
cevcSIStateEntry.setIndexNames(
    (0, "CISCO-EVC-MIB", "cevcSIIndex"),
)
if mibBuilder.loadTexts:
    cevcSIStateEntry.setStatus("current")


class _CevcSIOperStatus_Type(Integer32):
    """Custom type cevcSIOperStatus based on Integer32"""
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
        *(("adminDown", 3),
          ("deleted", 4),
          ("down", 2),
          ("errorDisabled", 5),
          ("unknown", 6),
          ("up", 1))
    )


_CevcSIOperStatus_Type.__name__ = "Integer32"
_CevcSIOperStatus_Object = MibTableColumn
cevcSIOperStatus = _CevcSIOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 2, 1, 1),
    _CevcSIOperStatus_Type()
)
cevcSIOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cevcSIOperStatus.setStatus("current")
_CevcSIVlanRewriteTable_Object = MibTable
cevcSIVlanRewriteTable = _CevcSIVlanRewriteTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 3)
)
if mibBuilder.loadTexts:
    cevcSIVlanRewriteTable.setStatus("current")
_CevcSIVlanRewriteEntry_Object = MibTableRow
cevcSIVlanRewriteEntry = _CevcSIVlanRewriteEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 3, 1)
)
cevcSIVlanRewriteEntry.setIndexNames(
    (0, "CISCO-EVC-MIB", "cevcSIIndex"),
    (0, "CISCO-EVC-MIB", "cevcSIVlanRewriteDirection"),
)
if mibBuilder.loadTexts:
    cevcSIVlanRewriteEntry.setStatus("current")


class _CevcSIVlanRewriteDirection_Type(Integer32):
    """Custom type cevcSIVlanRewriteDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("egress", 2),
          ("ingress", 1))
    )


_CevcSIVlanRewriteDirection_Type.__name__ = "Integer32"
_CevcSIVlanRewriteDirection_Object = MibTableColumn
cevcSIVlanRewriteDirection = _CevcSIVlanRewriteDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 3, 1, 1),
    _CevcSIVlanRewriteDirection_Type()
)
cevcSIVlanRewriteDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cevcSIVlanRewriteDirection.setStatus("current")
_CevcSIVlanRewriteRowStatus_Type = RowStatus
_CevcSIVlanRewriteRowStatus_Object = MibTableColumn
cevcSIVlanRewriteRowStatus = _CevcSIVlanRewriteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 3, 1, 2),
    _CevcSIVlanRewriteRowStatus_Type()
)
cevcSIVlanRewriteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIVlanRewriteRowStatus.setStatus("current")


class _CevcSIVlanRewriteStorageType_Type(StorageType):
    """Custom type cevcSIVlanRewriteStorageType based on StorageType"""


_CevcSIVlanRewriteStorageType_Object = MibTableColumn
cevcSIVlanRewriteStorageType = _CevcSIVlanRewriteStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 3, 1, 3),
    _CevcSIVlanRewriteStorageType_Type()
)
cevcSIVlanRewriteStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIVlanRewriteStorageType.setStatus("current")


class _CevcSIVlanRewriteAction_Type(Integer32):
    """Custom type cevcSIVlanRewriteAction based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("pop1", 3),
          ("pop2", 4),
          ("push1", 1),
          ("push2", 2),
          ("translate1To1", 5),
          ("translate1To2", 6),
          ("translate2To1", 7),
          ("translate2To2", 8))
    )


_CevcSIVlanRewriteAction_Type.__name__ = "Integer32"
_CevcSIVlanRewriteAction_Object = MibTableColumn
cevcSIVlanRewriteAction = _CevcSIVlanRewriteAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 3, 1, 4),
    _CevcSIVlanRewriteAction_Type()
)
cevcSIVlanRewriteAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIVlanRewriteAction.setStatus("current")


class _CevcSIVlanRewriteEncapsulation_Type(Integer32):
    """Custom type cevcSIVlanRewriteEncapsulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot1ad", 2),
          ("dot1q", 1))
    )


_CevcSIVlanRewriteEncapsulation_Type.__name__ = "Integer32"
_CevcSIVlanRewriteEncapsulation_Object = MibTableColumn
cevcSIVlanRewriteEncapsulation = _CevcSIVlanRewriteEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 3, 1, 5),
    _CevcSIVlanRewriteEncapsulation_Type()
)
cevcSIVlanRewriteEncapsulation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIVlanRewriteEncapsulation.setStatus("current")
_CevcSIVlanRewriteVlan1_Type = VlanId
_CevcSIVlanRewriteVlan1_Object = MibTableColumn
cevcSIVlanRewriteVlan1 = _CevcSIVlanRewriteVlan1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 3, 1, 6),
    _CevcSIVlanRewriteVlan1_Type()
)
cevcSIVlanRewriteVlan1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIVlanRewriteVlan1.setStatus("current")
_CevcSIVlanRewriteVlan2_Type = VlanId
_CevcSIVlanRewriteVlan2_Object = MibTableColumn
cevcSIVlanRewriteVlan2 = _CevcSIVlanRewriteVlan2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 3, 1, 7),
    _CevcSIVlanRewriteVlan2_Type()
)
cevcSIVlanRewriteVlan2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIVlanRewriteVlan2.setStatus("current")


class _CevcSIVlanRewriteSymmetric_Type(TruthValue):
    """Custom type cevcSIVlanRewriteSymmetric based on TruthValue"""


_CevcSIVlanRewriteSymmetric_Object = MibTableColumn
cevcSIVlanRewriteSymmetric = _CevcSIVlanRewriteSymmetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 3, 1, 8),
    _CevcSIVlanRewriteSymmetric_Type()
)
cevcSIVlanRewriteSymmetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIVlanRewriteSymmetric.setStatus("current")
_CevcSIL2ControlProtocolTable_Object = MibTable
cevcSIL2ControlProtocolTable = _CevcSIL2ControlProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 4)
)
if mibBuilder.loadTexts:
    cevcSIL2ControlProtocolTable.setStatus("current")
_CevcSIL2ControlProtocolEntry_Object = MibTableRow
cevcSIL2ControlProtocolEntry = _CevcSIL2ControlProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 4, 1)
)
cevcSIL2ControlProtocolEntry.setIndexNames(
    (0, "CISCO-EVC-MIB", "cevcSIIndex"),
    (0, "CISCO-EVC-MIB", "cevcSIL2ControlProtocolType"),
)
if mibBuilder.loadTexts:
    cevcSIL2ControlProtocolEntry.setStatus("current")
_CevcSIL2ControlProtocolType_Type = CevcL2ControlProtocolType
_CevcSIL2ControlProtocolType_Object = MibTableColumn
cevcSIL2ControlProtocolType = _CevcSIL2ControlProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 4, 1, 1),
    _CevcSIL2ControlProtocolType_Type()
)
cevcSIL2ControlProtocolType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cevcSIL2ControlProtocolType.setStatus("current")


class _CevcSIL2ControlProtocolAction_Type(Integer32):
    """Custom type cevcSIL2ControlProtocolAction based on Integer32"""
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
        *(("discard", 1),
          ("forward", 3),
          ("tunnel", 2))
    )


_CevcSIL2ControlProtocolAction_Type.__name__ = "Integer32"
_CevcSIL2ControlProtocolAction_Object = MibTableColumn
cevcSIL2ControlProtocolAction = _CevcSIL2ControlProtocolAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 4, 1, 2),
    _CevcSIL2ControlProtocolAction_Type()
)
cevcSIL2ControlProtocolAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIL2ControlProtocolAction.setStatus("current")
_CevcSICEVlanTable_Object = MibTable
cevcSICEVlanTable = _CevcSICEVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 5)
)
if mibBuilder.loadTexts:
    cevcSICEVlanTable.setStatus("current")
_CevcSICEVlanEntry_Object = MibTableRow
cevcSICEVlanEntry = _CevcSICEVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 5, 1)
)
cevcSICEVlanEntry.setIndexNames(
    (0, "CISCO-EVC-MIB", "cevcSIIndex"),
    (0, "CISCO-EVC-MIB", "cevcSICEVlanBeginningVlan"),
)
if mibBuilder.loadTexts:
    cevcSICEVlanEntry.setStatus("current")
_CevcSICEVlanBeginningVlan_Type = VlanId
_CevcSICEVlanBeginningVlan_Object = MibTableColumn
cevcSICEVlanBeginningVlan = _CevcSICEVlanBeginningVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 5, 1, 1),
    _CevcSICEVlanBeginningVlan_Type()
)
cevcSICEVlanBeginningVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cevcSICEVlanBeginningVlan.setStatus("current")
_CevcSICEVlanRowStatus_Type = RowStatus
_CevcSICEVlanRowStatus_Object = MibTableColumn
cevcSICEVlanRowStatus = _CevcSICEVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 5, 1, 2),
    _CevcSICEVlanRowStatus_Type()
)
cevcSICEVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSICEVlanRowStatus.setStatus("current")


class _CevcSICEVlanStorageType_Type(StorageType):
    """Custom type cevcSICEVlanStorageType based on StorageType"""


_CevcSICEVlanStorageType_Object = MibTableColumn
cevcSICEVlanStorageType = _CevcSICEVlanStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 5, 1, 3),
    _CevcSICEVlanStorageType_Type()
)
cevcSICEVlanStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSICEVlanStorageType.setStatus("current")
_CevcSICEVlanEndingVlan_Type = VlanIdOrNone
_CevcSICEVlanEndingVlan_Object = MibTableColumn
cevcSICEVlanEndingVlan = _CevcSICEVlanEndingVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 5, 1, 4),
    _CevcSICEVlanEndingVlan_Type()
)
cevcSICEVlanEndingVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSICEVlanEndingVlan.setStatus("current")
_CevcSIMatchCriteriaTable_Object = MibTable
cevcSIMatchCriteriaTable = _CevcSIMatchCriteriaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 6)
)
if mibBuilder.loadTexts:
    cevcSIMatchCriteriaTable.setStatus("current")
_CevcSIMatchCriteriaEntry_Object = MibTableRow
cevcSIMatchCriteriaEntry = _CevcSIMatchCriteriaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 6, 1)
)
cevcSIMatchCriteriaEntry.setIndexNames(
    (0, "CISCO-EVC-MIB", "cevcSIIndex"),
    (0, "CISCO-EVC-MIB", "cevcSIMatchCriteriaIndex"),
)
if mibBuilder.loadTexts:
    cevcSIMatchCriteriaEntry.setStatus("current")


class _CevcSIMatchCriteriaIndex_Type(Unsigned32):
    """Custom type cevcSIMatchCriteriaIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CevcSIMatchCriteriaIndex_Type.__name__ = "Unsigned32"
_CevcSIMatchCriteriaIndex_Object = MibTableColumn
cevcSIMatchCriteriaIndex = _CevcSIMatchCriteriaIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 6, 1, 1),
    _CevcSIMatchCriteriaIndex_Type()
)
cevcSIMatchCriteriaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cevcSIMatchCriteriaIndex.setStatus("current")
_CevcSIMatchRowStatus_Type = RowStatus
_CevcSIMatchRowStatus_Object = MibTableColumn
cevcSIMatchRowStatus = _CevcSIMatchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 6, 1, 2),
    _CevcSIMatchRowStatus_Type()
)
cevcSIMatchRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIMatchRowStatus.setStatus("current")


class _CevcSIMatchStorageType_Type(StorageType):
    """Custom type cevcSIMatchStorageType based on StorageType"""


_CevcSIMatchStorageType_Object = MibTableColumn
cevcSIMatchStorageType = _CevcSIMatchStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 6, 1, 3),
    _CevcSIMatchStorageType_Type()
)
cevcSIMatchStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIMatchStorageType.setStatus("current")


class _CevcSIMatchCriteriaType_Type(Integer32):
    """Custom type cevcSIMatchCriteriaType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("defaultTagged", 8),
          ("dot1ad", 3),
          ("dot1q", 2),
          ("priorityTagged", 7),
          ("unknown", 1),
          ("untagged", 4),
          ("untaggedAndDot1ad", 6),
          ("untaggedAndDot1q", 5))
    )


_CevcSIMatchCriteriaType_Type.__name__ = "Integer32"
_CevcSIMatchCriteriaType_Object = MibTableColumn
cevcSIMatchCriteriaType = _CevcSIMatchCriteriaType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 6, 1, 4),
    _CevcSIMatchCriteriaType_Type()
)
cevcSIMatchCriteriaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIMatchCriteriaType.setStatus("current")
_CevcSIMatchEncapTable_Object = MibTable
cevcSIMatchEncapTable = _CevcSIMatchEncapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 7)
)
if mibBuilder.loadTexts:
    cevcSIMatchEncapTable.setStatus("current")
_CevcSIMatchEncapEntry_Object = MibTableRow
cevcSIMatchEncapEntry = _CevcSIMatchEncapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 7, 1)
)
cevcSIMatchEncapEntry.setIndexNames(
    (0, "CISCO-EVC-MIB", "cevcSIIndex"),
    (0, "CISCO-EVC-MIB", "cevcSIMatchCriteriaIndex"),
)
if mibBuilder.loadTexts:
    cevcSIMatchEncapEntry.setStatus("current")
_CevcSIMatchEncapRowStatus_Type = RowStatus
_CevcSIMatchEncapRowStatus_Object = MibTableColumn
cevcSIMatchEncapRowStatus = _CevcSIMatchEncapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 7, 1, 1),
    _CevcSIMatchEncapRowStatus_Type()
)
cevcSIMatchEncapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIMatchEncapRowStatus.setStatus("current")


class _CevcSIMatchEncapStorageType_Type(StorageType):
    """Custom type cevcSIMatchEncapStorageType based on StorageType"""


_CevcSIMatchEncapStorageType_Object = MibTableColumn
cevcSIMatchEncapStorageType = _CevcSIMatchEncapStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 7, 1, 2),
    _CevcSIMatchEncapStorageType_Type()
)
cevcSIMatchEncapStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIMatchEncapStorageType.setStatus("current")


class _CevcSIMatchEncapValid_Type(Bits):
    """Custom type cevcSIMatchEncapValid based on Bits"""
    namedValues = NamedValues(
        *(("dot1adNativeVlan", 6),
          ("dot1qNativeVlan", 5),
          ("encapExact", 7),
          ("payloadType", 2),
          ("payloadTypes", 3),
          ("primaryCos", 0),
          ("priorityCos", 4),
          ("secondaryCos", 1))
    )

_CevcSIMatchEncapValid_Type.__name__ = "Bits"
_CevcSIMatchEncapValid_Object = MibTableColumn
cevcSIMatchEncapValid = _CevcSIMatchEncapValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 7, 1, 3),
    _CevcSIMatchEncapValid_Type()
)
cevcSIMatchEncapValid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIMatchEncapValid.setStatus("current")


class _CevcSIMatchEncapEncapsulation_Type(Integer32):
    """Custom type cevcSIMatchEncapEncapsulation based on Integer32"""
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
        *(("dot1adEthertype0x88A8", 5),
          ("dot1ahEthertype0x88A8", 6),
          ("dot1qEthertype0x8100", 1),
          ("dot1qEthertype0x88A8", 4),
          ("dot1qEthertype0x9100", 2),
          ("dot1qEthertype0x9200", 3))
    )


_CevcSIMatchEncapEncapsulation_Type.__name__ = "Integer32"
_CevcSIMatchEncapEncapsulation_Object = MibTableColumn
cevcSIMatchEncapEncapsulation = _CevcSIMatchEncapEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 7, 1, 4),
    _CevcSIMatchEncapEncapsulation_Type()
)
cevcSIMatchEncapEncapsulation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIMatchEncapEncapsulation.setStatus("current")
_CevcSIMatchEncapPrimaryCos_Type = CiscoCosList
_CevcSIMatchEncapPrimaryCos_Object = MibTableColumn
cevcSIMatchEncapPrimaryCos = _CevcSIMatchEncapPrimaryCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 7, 1, 5),
    _CevcSIMatchEncapPrimaryCos_Type()
)
cevcSIMatchEncapPrimaryCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIMatchEncapPrimaryCos.setStatus("current")
_CevcSIMatchEncapSecondaryCos_Type = CiscoCosList
_CevcSIMatchEncapSecondaryCos_Object = MibTableColumn
cevcSIMatchEncapSecondaryCos = _CevcSIMatchEncapSecondaryCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 7, 1, 6),
    _CevcSIMatchEncapSecondaryCos_Type()
)
cevcSIMatchEncapSecondaryCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIMatchEncapSecondaryCos.setStatus("current")


class _CevcSIMatchEncapPayloadType_Type(Integer32):
    """Custom type cevcSIMatchEncapPayloadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("payloadType0x0800ip", 2))
    )


_CevcSIMatchEncapPayloadType_Type.__name__ = "Integer32"
_CevcSIMatchEncapPayloadType_Object = MibTableColumn
cevcSIMatchEncapPayloadType = _CevcSIMatchEncapPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 7, 1, 7),
    _CevcSIMatchEncapPayloadType_Type()
)
cevcSIMatchEncapPayloadType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIMatchEncapPayloadType.setStatus("deprecated")


class _CevcSIMatchEncapPayloadTypes_Type(Bits):
    """Custom type cevcSIMatchEncapPayloadTypes based on Bits"""
    namedValues = NamedValues(
        *(("payloadTypeIPv4", 0),
          ("payloadTypeIPv6", 1),
          ("payloadTypePPPoEAll", 4),
          ("payloadTypePPPoEDiscovery", 2),
          ("payloadTypePPPoESession", 3))
    )

_CevcSIMatchEncapPayloadTypes_Type.__name__ = "Bits"
_CevcSIMatchEncapPayloadTypes_Object = MibTableColumn
cevcSIMatchEncapPayloadTypes = _CevcSIMatchEncapPayloadTypes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 7, 1, 8),
    _CevcSIMatchEncapPayloadTypes_Type()
)
cevcSIMatchEncapPayloadTypes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIMatchEncapPayloadTypes.setStatus("current")
_CevcSIMatchEncapPriorityCos_Type = CiscoCosList
_CevcSIMatchEncapPriorityCos_Object = MibTableColumn
cevcSIMatchEncapPriorityCos = _CevcSIMatchEncapPriorityCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 7, 1, 9),
    _CevcSIMatchEncapPriorityCos_Type()
)
cevcSIMatchEncapPriorityCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIMatchEncapPriorityCos.setStatus("current")
_CevcSIPrimaryVlanTable_Object = MibTable
cevcSIPrimaryVlanTable = _CevcSIPrimaryVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 8)
)
if mibBuilder.loadTexts:
    cevcSIPrimaryVlanTable.setStatus("current")
_CevcSIPrimaryVlanEntry_Object = MibTableRow
cevcSIPrimaryVlanEntry = _CevcSIPrimaryVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 8, 1)
)
cevcSIPrimaryVlanEntry.setIndexNames(
    (0, "CISCO-EVC-MIB", "cevcSIIndex"),
    (0, "CISCO-EVC-MIB", "cevcSIMatchCriteriaIndex"),
    (0, "CISCO-EVC-MIB", "cevcSIPrimaryVlanBeginningVlan"),
)
if mibBuilder.loadTexts:
    cevcSIPrimaryVlanEntry.setStatus("current")
_CevcSIPrimaryVlanBeginningVlan_Type = VlanId
_CevcSIPrimaryVlanBeginningVlan_Object = MibTableColumn
cevcSIPrimaryVlanBeginningVlan = _CevcSIPrimaryVlanBeginningVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 8, 1, 1),
    _CevcSIPrimaryVlanBeginningVlan_Type()
)
cevcSIPrimaryVlanBeginningVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cevcSIPrimaryVlanBeginningVlan.setStatus("current")
_CevcSIPrimaryVlanRowStatus_Type = RowStatus
_CevcSIPrimaryVlanRowStatus_Object = MibTableColumn
cevcSIPrimaryVlanRowStatus = _CevcSIPrimaryVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 8, 1, 2),
    _CevcSIPrimaryVlanRowStatus_Type()
)
cevcSIPrimaryVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIPrimaryVlanRowStatus.setStatus("current")


class _CevcSIPrimaryVlanStorageType_Type(StorageType):
    """Custom type cevcSIPrimaryVlanStorageType based on StorageType"""


_CevcSIPrimaryVlanStorageType_Object = MibTableColumn
cevcSIPrimaryVlanStorageType = _CevcSIPrimaryVlanStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 8, 1, 3),
    _CevcSIPrimaryVlanStorageType_Type()
)
cevcSIPrimaryVlanStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIPrimaryVlanStorageType.setStatus("current")
_CevcSIPrimaryVlanEndingVlan_Type = VlanIdOrNone
_CevcSIPrimaryVlanEndingVlan_Object = MibTableColumn
cevcSIPrimaryVlanEndingVlan = _CevcSIPrimaryVlanEndingVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 8, 1, 4),
    _CevcSIPrimaryVlanEndingVlan_Type()
)
cevcSIPrimaryVlanEndingVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIPrimaryVlanEndingVlan.setStatus("current")
_CevcSISecondaryVlanTable_Object = MibTable
cevcSISecondaryVlanTable = _CevcSISecondaryVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 9)
)
if mibBuilder.loadTexts:
    cevcSISecondaryVlanTable.setStatus("current")
_CevcSISecondaryVlanEntry_Object = MibTableRow
cevcSISecondaryVlanEntry = _CevcSISecondaryVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 9, 1)
)
cevcSISecondaryVlanEntry.setIndexNames(
    (0, "CISCO-EVC-MIB", "cevcSIIndex"),
    (0, "CISCO-EVC-MIB", "cevcSIMatchCriteriaIndex"),
    (0, "CISCO-EVC-MIB", "cevcSISecondaryVlanBeginningVlan"),
)
if mibBuilder.loadTexts:
    cevcSISecondaryVlanEntry.setStatus("current")
_CevcSISecondaryVlanBeginningVlan_Type = VlanId
_CevcSISecondaryVlanBeginningVlan_Object = MibTableColumn
cevcSISecondaryVlanBeginningVlan = _CevcSISecondaryVlanBeginningVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 9, 1, 1),
    _CevcSISecondaryVlanBeginningVlan_Type()
)
cevcSISecondaryVlanBeginningVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cevcSISecondaryVlanBeginningVlan.setStatus("current")
_CevcSISecondaryVlanRowStatus_Type = RowStatus
_CevcSISecondaryVlanRowStatus_Object = MibTableColumn
cevcSISecondaryVlanRowStatus = _CevcSISecondaryVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 9, 1, 2),
    _CevcSISecondaryVlanRowStatus_Type()
)
cevcSISecondaryVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSISecondaryVlanRowStatus.setStatus("current")


class _CevcSISecondaryVlanStorageType_Type(StorageType):
    """Custom type cevcSISecondaryVlanStorageType based on StorageType"""


_CevcSISecondaryVlanStorageType_Object = MibTableColumn
cevcSISecondaryVlanStorageType = _CevcSISecondaryVlanStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 9, 1, 3),
    _CevcSISecondaryVlanStorageType_Type()
)
cevcSISecondaryVlanStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSISecondaryVlanStorageType.setStatus("current")
_CevcSISecondaryVlanEndingVlan_Type = VlanIdOrNone
_CevcSISecondaryVlanEndingVlan_Object = MibTableColumn
cevcSISecondaryVlanEndingVlan = _CevcSISecondaryVlanEndingVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 9, 1, 4),
    _CevcSISecondaryVlanEndingVlan_Type()
)
cevcSISecondaryVlanEndingVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSISecondaryVlanEndingVlan.setStatus("current")
_CevcSIForwardBdTable_Object = MibTable
cevcSIForwardBdTable = _CevcSIForwardBdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 10)
)
if mibBuilder.loadTexts:
    cevcSIForwardBdTable.setStatus("current")
_CevcSIForwardBdEntry_Object = MibTableRow
cevcSIForwardBdEntry = _CevcSIForwardBdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 10, 1)
)
cevcSIForwardBdEntry.setIndexNames(
    (0, "CISCO-EVC-MIB", "cevcSIIndex"),
)
if mibBuilder.loadTexts:
    cevcSIForwardBdEntry.setStatus("current")
_CevcSIForwardBdRowStatus_Type = RowStatus
_CevcSIForwardBdRowStatus_Object = MibTableColumn
cevcSIForwardBdRowStatus = _CevcSIForwardBdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 10, 1, 1),
    _CevcSIForwardBdRowStatus_Type()
)
cevcSIForwardBdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIForwardBdRowStatus.setStatus("current")


class _CevcSIForwardBdStorageType_Type(StorageType):
    """Custom type cevcSIForwardBdStorageType based on StorageType"""


_CevcSIForwardBdStorageType_Object = MibTableColumn
cevcSIForwardBdStorageType = _CevcSIForwardBdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 10, 1, 2),
    _CevcSIForwardBdStorageType_Type()
)
cevcSIForwardBdStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIForwardBdStorageType.setStatus("current")
_CevcSIForwardBdNumber_Type = Unsigned32
_CevcSIForwardBdNumber_Object = MibTableColumn
cevcSIForwardBdNumber = _CevcSIForwardBdNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 10, 1, 3),
    _CevcSIForwardBdNumber_Type()
)
cevcSIForwardBdNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIForwardBdNumber.setStatus("deprecated")


class _CevcSIForwardBdNumberBase_Type(Integer32):
    """Custom type cevcSIForwardBdNumberBase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4096,
              8192,
              12288,
              16384)
        )
    )
    namedValues = NamedValues(
        *(("bdNumBase0", 0),
          ("bdNumBase12288", 12288),
          ("bdNumBase16384", 16384),
          ("bdNumBase4096", 4096),
          ("bdNumBase8192", 8192))
    )


_CevcSIForwardBdNumberBase_Type.__name__ = "Integer32"
_CevcSIForwardBdNumberBase_Object = MibTableColumn
cevcSIForwardBdNumberBase = _CevcSIForwardBdNumberBase_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 10, 1, 4),
    _CevcSIForwardBdNumberBase_Type()
)
cevcSIForwardBdNumberBase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIForwardBdNumberBase.setStatus("current")


class _CevcSIForwardBdNumber1kBitmap_Type(OctetString):
    """Custom type cevcSIForwardBdNumber1kBitmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CevcSIForwardBdNumber1kBitmap_Type.__name__ = "OctetString"
_CevcSIForwardBdNumber1kBitmap_Object = MibTableColumn
cevcSIForwardBdNumber1kBitmap = _CevcSIForwardBdNumber1kBitmap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 10, 1, 5),
    _CevcSIForwardBdNumber1kBitmap_Type()
)
cevcSIForwardBdNumber1kBitmap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIForwardBdNumber1kBitmap.setStatus("current")


class _CevcSIForwardBdNumber2kBitmap_Type(OctetString):
    """Custom type cevcSIForwardBdNumber2kBitmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CevcSIForwardBdNumber2kBitmap_Type.__name__ = "OctetString"
_CevcSIForwardBdNumber2kBitmap_Object = MibTableColumn
cevcSIForwardBdNumber2kBitmap = _CevcSIForwardBdNumber2kBitmap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 10, 1, 6),
    _CevcSIForwardBdNumber2kBitmap_Type()
)
cevcSIForwardBdNumber2kBitmap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIForwardBdNumber2kBitmap.setStatus("current")


class _CevcSIForwardBdNumber3kBitmap_Type(OctetString):
    """Custom type cevcSIForwardBdNumber3kBitmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CevcSIForwardBdNumber3kBitmap_Type.__name__ = "OctetString"
_CevcSIForwardBdNumber3kBitmap_Object = MibTableColumn
cevcSIForwardBdNumber3kBitmap = _CevcSIForwardBdNumber3kBitmap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 10, 1, 7),
    _CevcSIForwardBdNumber3kBitmap_Type()
)
cevcSIForwardBdNumber3kBitmap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIForwardBdNumber3kBitmap.setStatus("current")


class _CevcSIForwardBdNumber4kBitmap_Type(OctetString):
    """Custom type cevcSIForwardBdNumber4kBitmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CevcSIForwardBdNumber4kBitmap_Type.__name__ = "OctetString"
_CevcSIForwardBdNumber4kBitmap_Object = MibTableColumn
cevcSIForwardBdNumber4kBitmap = _CevcSIForwardBdNumber4kBitmap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 4, 10, 1, 8),
    _CevcSIForwardBdNumber4kBitmap_Type()
)
cevcSIForwardBdNumber4kBitmap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cevcSIForwardBdNumber4kBitmap.setStatus("current")
_CevcEvcNotificationConfig_ObjectIdentity = ObjectIdentity
cevcEvcNotificationConfig = _CevcEvcNotificationConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 5)
)


class _CevcEvcNotifyEnabled_Type(Bits):
    """Custom type cevcEvcNotifyEnabled based on Bits"""
    namedValues = NamedValues(
        *(("creation", 1),
          ("deletion", 2),
          ("macSecurityViolation", 3),
          ("status", 0))
    )

_CevcEvcNotifyEnabled_Type.__name__ = "Bits"
_CevcEvcNotifyEnabled_Object = MibScalar
cevcEvcNotifyEnabled = _CevcEvcNotifyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 5, 1),
    _CevcEvcNotifyEnabled_Type()
)
cevcEvcNotifyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cevcEvcNotifyEnabled.setStatus("current")
_CevcMacSecurityViolation_ObjectIdentity = ObjectIdentity
cevcMacSecurityViolation = _CevcMacSecurityViolation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 6)
)
_CevcMacAddress_Type = MacAddress
_CevcMacAddress_Object = MibScalar
cevcMacAddress = _CevcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 6, 1),
    _CevcMacAddress_Type()
)
cevcMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cevcMacAddress.setStatus("current")
_CevcMaxMacConfigLimit_Type = Unsigned32
_CevcMaxMacConfigLimit_Object = MibScalar
cevcMaxMacConfigLimit = _CevcMaxMacConfigLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 6, 2),
    _CevcMaxMacConfigLimit_Type()
)
cevcMaxMacConfigLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cevcMaxMacConfigLimit.setStatus("current")
_CevcSIID_Type = Integer32
_CevcSIID_Object = MibScalar
cevcSIID = _CevcSIID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 6, 3),
    _CevcSIID_Type()
)
cevcSIID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cevcSIID.setStatus("current")
_CevcViolationCause_Type = CevcMacSecurityViolationCauseType
_CevcViolationCause_Object = MibScalar
cevcViolationCause = _CevcViolationCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 1, 6, 4),
    _CevcViolationCause_Type()
)
cevcViolationCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cevcViolationCause.setStatus("current")
_CiscoEvcMIBConformance_ObjectIdentity = ObjectIdentity
ciscoEvcMIBConformance = _CiscoEvcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 2)
)
_CiscoEvcMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoEvcMIBCompliances = _CiscoEvcMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 2, 1)
)
_CiscoEvcMIBGroups_ObjectIdentity = ObjectIdentity
ciscoEvcMIBGroups = _CiscoEvcMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 2, 2)
)

# Managed Objects groups

cevcSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 2, 2, 1)
)
cevcSystemGroup.setObjects(
      *(("CISCO-EVC-MIB", "cevcMaxNumEvcs"),
        ("CISCO-EVC-MIB", "cevcNumCfgEvcs"))
)
if mibBuilder.loadTexts:
    cevcSystemGroup.setStatus("current")

cevcPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 2, 2, 2)
)
cevcPortGroup.setObjects(
      *(("CISCO-EVC-MIB", "cevcPortMode"),
        ("CISCO-EVC-MIB", "cevcPortMaxNumEVCs"),
        ("CISCO-EVC-MIB", "cevcPortMaxNumServiceInstances"),
        ("CISCO-EVC-MIB", "cevcPortL2ControlProtocolAction"),
        ("CISCO-EVC-MIB", "cevcUniIdentifier"),
        ("CISCO-EVC-MIB", "cevcUniPortType"),
        ("CISCO-EVC-MIB", "cevcUniServiceAttributes"),
        ("CISCO-EVC-MIB", "cevcUniCEVlanEvcEndingVlan"))
)
if mibBuilder.loadTexts:
    cevcPortGroup.setStatus("current")

cevcEvcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 2, 2, 3)
)
cevcEvcGroup.setObjects(
      *(("CISCO-EVC-MIB", "cevcEvcIdentifier"),
        ("CISCO-EVC-MIB", "cevcEvcType"),
        ("CISCO-EVC-MIB", "cevcEvcOperStatus"),
        ("CISCO-EVC-MIB", "cevcEvcCfgUnis"),
        ("CISCO-EVC-MIB", "cevcEvcActiveUnis"),
        ("CISCO-EVC-MIB", "cevcEvcStorageType"),
        ("CISCO-EVC-MIB", "cevcEvcRowStatus"),
        ("CISCO-EVC-MIB", "cevcEvcUniId"),
        ("CISCO-EVC-MIB", "cevcEvcUniOperStatus"),
        ("CISCO-EVC-MIB", "cevcEvcLocalUniIfIndex"))
)
if mibBuilder.loadTexts:
    cevcEvcGroup.setStatus("current")

cevcSIGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 2, 2, 4)
)
cevcSIGroup.setObjects(
      *(("CISCO-EVC-MIB", "cevcSIName"),
        ("CISCO-EVC-MIB", "cevcSITargetType"),
        ("CISCO-EVC-MIB", "cevcSITarget"),
        ("CISCO-EVC-MIB", "cevcSIEvcIndex"),
        ("CISCO-EVC-MIB", "cevcSIRowStatus"),
        ("CISCO-EVC-MIB", "cevcSIStorageType"),
        ("CISCO-EVC-MIB", "cevcSIAdminStatus"),
        ("CISCO-EVC-MIB", "cevcSIOperStatus"),
        ("CISCO-EVC-MIB", "cevcSIL2ControlProtocolAction"),
        ("CISCO-EVC-MIB", "cevcSIVlanRewriteAction"),
        ("CISCO-EVC-MIB", "cevcSIVlanRewriteEncapsulation"),
        ("CISCO-EVC-MIB", "cevcSIVlanRewriteVlan1"),
        ("CISCO-EVC-MIB", "cevcSIVlanRewriteVlan2"),
        ("CISCO-EVC-MIB", "cevcSIVlanRewriteSymmetric"),
        ("CISCO-EVC-MIB", "cevcSIVlanRewriteStorageType"),
        ("CISCO-EVC-MIB", "cevcSIVlanRewriteRowStatus"),
        ("CISCO-EVC-MIB", "cevcSIForwardingType"),
        ("CISCO-EVC-MIB", "cevcSICEVlanRowStatus"),
        ("CISCO-EVC-MIB", "cevcSICEVlanStorageType"),
        ("CISCO-EVC-MIB", "cevcSICEVlanEndingVlan"),
        ("CISCO-EVC-MIB", "cevcSIMatchStorageType"),
        ("CISCO-EVC-MIB", "cevcSIMatchRowStatus"),
        ("CISCO-EVC-MIB", "cevcSIMatchCriteriaType"),
        ("CISCO-EVC-MIB", "cevcSIMatchEncapRowStatus"),
        ("CISCO-EVC-MIB", "cevcSIMatchEncapStorageType"),
        ("CISCO-EVC-MIB", "cevcSIMatchEncapValid"),
        ("CISCO-EVC-MIB", "cevcSIMatchEncapEncapsulation"),
        ("CISCO-EVC-MIB", "cevcSIPrimaryVlanRowStatus"),
        ("CISCO-EVC-MIB", "cevcSIPrimaryVlanStorageType"),
        ("CISCO-EVC-MIB", "cevcSIPrimaryVlanEndingVlan"))
)
if mibBuilder.loadTexts:
    cevcSIGroup.setStatus("deprecated")

cevcSIVlanRewriteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 2, 2, 5)
)
cevcSIVlanRewriteGroup.setObjects(
      *(("CISCO-EVC-MIB", "cevcSIVlanRewriteAction"),
        ("CISCO-EVC-MIB", "cevcSIVlanRewriteEncapsulation"),
        ("CISCO-EVC-MIB", "cevcSIVlanRewriteVlan1"),
        ("CISCO-EVC-MIB", "cevcSIVlanRewriteVlan2"),
        ("CISCO-EVC-MIB", "cevcSIVlanRewriteSymmetric"),
        ("CISCO-EVC-MIB", "cevcSIVlanRewriteStorageType"),
        ("CISCO-EVC-MIB", "cevcSIVlanRewriteRowStatus"))
)
if mibBuilder.loadTexts:
    cevcSIVlanRewriteGroup.setStatus("current")

cevcSICosMatchCriteriaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 2, 2, 6)
)
cevcSICosMatchCriteriaGroup.setObjects(
      *(("CISCO-EVC-MIB", "cevcSIMatchEncapPrimaryCos"),
        ("CISCO-EVC-MIB", "cevcSIMatchEncapSecondaryCos"))
)
if mibBuilder.loadTexts:
    cevcSICosMatchCriteriaGroup.setStatus("current")

cevcSIMatchCriteriaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 2, 2, 7)
)
cevcSIMatchCriteriaGroup.setObjects(
      *(("CISCO-EVC-MIB", "cevcSIMatchRowStatus"),
        ("CISCO-EVC-MIB", "cevcSIMatchStorageType"),
        ("CISCO-EVC-MIB", "cevcSIMatchCriteriaType"),
        ("CISCO-EVC-MIB", "cevcSIMatchEncapRowStatus"),
        ("CISCO-EVC-MIB", "cevcSIMatchEncapStorageType"),
        ("CISCO-EVC-MIB", "cevcSIMatchEncapValid"),
        ("CISCO-EVC-MIB", "cevcSIMatchEncapEncapsulation"),
        ("CISCO-EVC-MIB", "cevcSIMatchEncapPrimaryCos"),
        ("CISCO-EVC-MIB", "cevcSIMatchEncapSecondaryCos"),
        ("CISCO-EVC-MIB", "cevcSIMatchEncapPayloadType"),
        ("CISCO-EVC-MIB", "cevcSIPrimaryVlanRowStatus"),
        ("CISCO-EVC-MIB", "cevcSIPrimaryVlanStorageType"),
        ("CISCO-EVC-MIB", "cevcSIPrimaryVlanEndingVlan"),
        ("CISCO-EVC-MIB", "cevcSISecondaryVlanRowStatus"),
        ("CISCO-EVC-MIB", "cevcSISecondaryVlanStorageType"),
        ("CISCO-EVC-MIB", "cevcSISecondaryVlanEndingVlan"))
)
if mibBuilder.loadTexts:
    cevcSIMatchCriteriaGroup.setStatus("deprecated")

cevcSIForwardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 2, 2, 8)
)
cevcSIForwardGroup.setObjects(
      *(("CISCO-EVC-MIB", "cevcSIForwardingType"),
        ("CISCO-EVC-MIB", "cevcSIForwardBdRowStatus"),
        ("CISCO-EVC-MIB", "cevcSIForwardBdStorageType"),
        ("CISCO-EVC-MIB", "cevcSIForwardBdNumber"))
)
if mibBuilder.loadTexts:
    cevcSIForwardGroup.setStatus("deprecated")

cevcEvcNotificationConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 2, 2, 9)
)
cevcEvcNotificationConfigGroup.setObjects(
    ("CISCO-EVC-MIB", "cevcEvcNotifyEnabled")
)
if mibBuilder.loadTexts:
    cevcEvcNotificationConfigGroup.setStatus("current")

cevcSIMatchCriteriaGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 2, 2, 11)
)
cevcSIMatchCriteriaGroupRev1.setObjects(
      *(("CISCO-EVC-MIB", "cevcSIMatchRowStatus"),
        ("CISCO-EVC-MIB", "cevcSIMatchStorageType"),
        ("CISCO-EVC-MIB", "cevcSIMatchCriteriaType"),
        ("CISCO-EVC-MIB", "cevcSIMatchEncapRowStatus"),
        ("CISCO-EVC-MIB", "cevcSIMatchEncapStorageType"),
        ("CISCO-EVC-MIB", "cevcSIMatchEncapValid"),
        ("CISCO-EVC-MIB", "cevcSIMatchEncapEncapsulation"),
        ("CISCO-EVC-MIB", "cevcSIMatchEncapPrimaryCos"),
        ("CISCO-EVC-MIB", "cevcSIMatchEncapSecondaryCos"),
        ("CISCO-EVC-MIB", "cevcSIMatchEncapPayloadTypes"),
        ("CISCO-EVC-MIB", "cevcSIMatchEncapPriorityCos"),
        ("CISCO-EVC-MIB", "cevcSIPrimaryVlanRowStatus"),
        ("CISCO-EVC-MIB", "cevcSIPrimaryVlanStorageType"),
        ("CISCO-EVC-MIB", "cevcSIPrimaryVlanEndingVlan"),
        ("CISCO-EVC-MIB", "cevcSISecondaryVlanRowStatus"),
        ("CISCO-EVC-MIB", "cevcSISecondaryVlanStorageType"),
        ("CISCO-EVC-MIB", "cevcSISecondaryVlanEndingVlan"))
)
if mibBuilder.loadTexts:
    cevcSIMatchCriteriaGroupRev1.setStatus("current")

cevcSIGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 2, 2, 13)
)
cevcSIGroupRev1.setObjects(
      *(("CISCO-EVC-MIB", "cevcSIName"),
        ("CISCO-EVC-MIB", "cevcSITargetType"),
        ("CISCO-EVC-MIB", "cevcSITarget"),
        ("CISCO-EVC-MIB", "cevcSIEvcIndex"),
        ("CISCO-EVC-MIB", "cevcSIRowStatus"),
        ("CISCO-EVC-MIB", "cevcSIStorageType"),
        ("CISCO-EVC-MIB", "cevcSIAdminStatus"),
        ("CISCO-EVC-MIB", "cevcSIOperStatus"),
        ("CISCO-EVC-MIB", "cevcPortL2ControlProtocolAction"),
        ("CISCO-EVC-MIB", "cevcSIVlanRewriteAction"),
        ("CISCO-EVC-MIB", "cevcSIVlanRewriteEncapsulation"),
        ("CISCO-EVC-MIB", "cevcSIVlanRewriteVlan1"),
        ("CISCO-EVC-MIB", "cevcSIVlanRewriteVlan2"),
        ("CISCO-EVC-MIB", "cevcSIVlanRewriteSymmetric"),
        ("CISCO-EVC-MIB", "cevcSIVlanRewriteRowStatus"),
        ("CISCO-EVC-MIB", "cevcSIVlanRewriteStorageType"),
        ("CISCO-EVC-MIB", "cevcSIForwardingType"),
        ("CISCO-EVC-MIB", "cevcSICEVlanRowStatus"),
        ("CISCO-EVC-MIB", "cevcSICEVlanStorageType"),
        ("CISCO-EVC-MIB", "cevcSICEVlanEndingVlan"),
        ("CISCO-EVC-MIB", "cevcSIMatchStorageType"),
        ("CISCO-EVC-MIB", "cevcSIMatchCriteriaType"),
        ("CISCO-EVC-MIB", "cevcSIMatchEncapRowStatus"),
        ("CISCO-EVC-MIB", "cevcSIMatchEncapStorageType"),
        ("CISCO-EVC-MIB", "cevcSIMatchEncapValid"),
        ("CISCO-EVC-MIB", "cevcSIMatchEncapEncapsulation"),
        ("CISCO-EVC-MIB", "cevcSIPrimaryVlanRowStatus"),
        ("CISCO-EVC-MIB", "cevcSIPrimaryVlanStorageType"),
        ("CISCO-EVC-MIB", "cevcSIPrimaryVlanEndingVlan"),
        ("CISCO-EVC-MIB", "cevcSIMatchRowStatus"),
        ("CISCO-EVC-MIB", "cevcSICreationType"),
        ("CISCO-EVC-MIB", "cevcSIType"))
)
if mibBuilder.loadTexts:
    cevcSIGroupRev1.setStatus("current")

cevcSIForwardGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 2, 2, 14)
)
cevcSIForwardGroupRev1.setObjects(
      *(("CISCO-EVC-MIB", "cevcSIForwardingType"),
        ("CISCO-EVC-MIB", "cevcSIForwardBdRowStatus"),
        ("CISCO-EVC-MIB", "cevcSIForwardBdStorageType"),
        ("CISCO-EVC-MIB", "cevcSIForwardBdNumberBase"),
        ("CISCO-EVC-MIB", "cevcSIForwardBdNumber1kBitmap"),
        ("CISCO-EVC-MIB", "cevcSIForwardBdNumber2kBitmap"),
        ("CISCO-EVC-MIB", "cevcSIForwardBdNumber3kBitmap"),
        ("CISCO-EVC-MIB", "cevcSIForwardBdNumber4kBitmap"))
)
if mibBuilder.loadTexts:
    cevcSIForwardGroupRev1.setStatus("current")

cevcMacSecurityViolationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 2, 2, 15)
)
cevcMacSecurityViolationGroup.setObjects(
      *(("CISCO-EVC-MIB", "cevcMacAddress"),
        ("CISCO-EVC-MIB", "cevcMaxMacConfigLimit"),
        ("CISCO-EVC-MIB", "cevcSIID"),
        ("CISCO-EVC-MIB", "cevcViolationCause"))
)
if mibBuilder.loadTexts:
    cevcMacSecurityViolationGroup.setStatus("current")


# Notification objects

cevcEvcStatusChangedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 0, 0, 1)
)
cevcEvcStatusChangedNotification.setObjects(
      *(("CISCO-EVC-MIB", "cevcEvcOperStatus"),
        ("CISCO-EVC-MIB", "cevcEvcCfgUnis"),
        ("CISCO-EVC-MIB", "cevcEvcActiveUnis"))
)
if mibBuilder.loadTexts:
    cevcEvcStatusChangedNotification.setStatus(
        "current"
    )

cevcEvcCreationNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 0, 0, 2)
)
cevcEvcCreationNotification.setObjects(
    ("CISCO-EVC-MIB", "cevcEvcOperStatus")
)
if mibBuilder.loadTexts:
    cevcEvcCreationNotification.setStatus(
        "current"
    )

cevcEvcDeletionNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 0, 0, 3)
)
cevcEvcDeletionNotification.setObjects(
    ("CISCO-EVC-MIB", "cevcEvcOperStatus")
)
if mibBuilder.loadTexts:
    cevcEvcDeletionNotification.setStatus(
        "current"
    )

cevcMacSecurityViolationNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 0, 0, 4)
)
cevcMacSecurityViolationNotification.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-EVC-MIB", "cevcSIForwardBdNumberBase"),
        ("CISCO-EVC-MIB", "cevcSIForwardBdNumber1kBitmap"),
        ("CISCO-EVC-MIB", "cevcSIForwardBdNumber2kBitmap"),
        ("CISCO-EVC-MIB", "cevcSIForwardBdNumber3kBitmap"),
        ("CISCO-EVC-MIB", "cevcSIForwardBdNumber4kBitmap"),
        ("CISCO-EVC-MIB", "cevcSIID"),
        ("CISCO-EVC-MIB", "cevcMacAddress"),
        ("CISCO-EVC-MIB", "cevcMaxMacConfigLimit"),
        ("CISCO-EVC-MIB", "cevcViolationCause"))
)
if mibBuilder.loadTexts:
    cevcMacSecurityViolationNotification.setStatus(
        "current"
    )


# Notifications groups

cevcEvcNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 2, 2, 10)
)
cevcEvcNotificationGroup.setObjects(
      *(("CISCO-EVC-MIB", "cevcEvcStatusChangedNotification"),
        ("CISCO-EVC-MIB", "cevcEvcCreationNotification"),
        ("CISCO-EVC-MIB", "cevcEvcDeletionNotification"))
)
if mibBuilder.loadTexts:
    cevcEvcNotificationGroup.setStatus(
        "deprecated"
    )

cevcEvcNotificationGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 2, 2, 12)
)
cevcEvcNotificationGroupRev1.setObjects(
      *(("CISCO-EVC-MIB", "cevcEvcStatusChangedNotification"),
        ("CISCO-EVC-MIB", "cevcEvcCreationNotification"),
        ("CISCO-EVC-MIB", "cevcEvcDeletionNotification"),
        ("CISCO-EVC-MIB", "cevcMacSecurityViolationNotification"))
)
if mibBuilder.loadTexts:
    cevcEvcNotificationGroupRev1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoEvcMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoEvcMIBCompliance.setStatus(
        "deprecated"
    )

ciscoEvcMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoEvcMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoEvcMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 613, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoEvcMIBComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-EVC-MIB",
    **{"CevcMacSecurityViolationCauseType": CevcMacSecurityViolationCauseType,
       "CiscoEvcIndex": CiscoEvcIndex,
       "CiscoEvcIndexOrZero": CiscoEvcIndexOrZero,
       "CevcL2ControlProtocolType": CevcL2ControlProtocolType,
       "ServiceInstanceTarget": ServiceInstanceTarget,
       "ServiceInstanceTargetType": ServiceInstanceTargetType,
       "ServiceInstanceInterface": ServiceInstanceInterface,
       "ciscoEvcMIB": ciscoEvcMIB,
       "ciscoEvcMIBNotifications": ciscoEvcMIBNotifications,
       "ciscoEvcNotificationPrefix": ciscoEvcNotificationPrefix,
       "cevcEvcStatusChangedNotification": cevcEvcStatusChangedNotification,
       "cevcEvcCreationNotification": cevcEvcCreationNotification,
       "cevcEvcDeletionNotification": cevcEvcDeletionNotification,
       "cevcMacSecurityViolationNotification": cevcMacSecurityViolationNotification,
       "ciscoEvcMIBObjects": ciscoEvcMIBObjects,
       "cevcSystem": cevcSystem,
       "cevcMaxNumEvcs": cevcMaxNumEvcs,
       "cevcNumCfgEvcs": cevcNumCfgEvcs,
       "cevcPort": cevcPort,
       "cevcPortTable": cevcPortTable,
       "cevcPortEntry": cevcPortEntry,
       "cevcPortMode": cevcPortMode,
       "cevcPortMaxNumEVCs": cevcPortMaxNumEVCs,
       "cevcPortMaxNumServiceInstances": cevcPortMaxNumServiceInstances,
       "cevcUniTable": cevcUniTable,
       "cevcUniEntry": cevcUniEntry,
       "cevcUniIdentifier": cevcUniIdentifier,
       "cevcUniPortType": cevcUniPortType,
       "cevcUniServiceAttributes": cevcUniServiceAttributes,
       "cevcPortL2ControlProtocolTable": cevcPortL2ControlProtocolTable,
       "cevcPortL2ControlProtocolEntry": cevcPortL2ControlProtocolEntry,
       "cevcPortL2ControlProtocolType": cevcPortL2ControlProtocolType,
       "cevcPortL2ControlProtocolAction": cevcPortL2ControlProtocolAction,
       "cevcUniCEVlanEvcTable": cevcUniCEVlanEvcTable,
       "cevcUniCEVlanEvcEntry": cevcUniCEVlanEvcEntry,
       "cevcUniEvcIndex": cevcUniEvcIndex,
       "cevcUniCEVlanEvcBeginningVlan": cevcUniCEVlanEvcBeginningVlan,
       "cevcUniCEVlanEvcEndingVlan": cevcUniCEVlanEvcEndingVlan,
       "cevcEvc": cevcEvc,
       "cevcEvcTable": cevcEvcTable,
       "cevcEvcEntry": cevcEvcEntry,
       "cevcEvcIndex": cevcEvcIndex,
       "cevcEvcRowStatus": cevcEvcRowStatus,
       "cevcEvcStorageType": cevcEvcStorageType,
       "cevcEvcIdentifier": cevcEvcIdentifier,
       "cevcEvcType": cevcEvcType,
       "cevcEvcCfgUnis": cevcEvcCfgUnis,
       "cevcEvcStateTable": cevcEvcStateTable,
       "cevcEvcStateEntry": cevcEvcStateEntry,
       "cevcEvcOperStatus": cevcEvcOperStatus,
       "cevcEvcActiveUnis": cevcEvcActiveUnis,
       "cevcEvcUniTable": cevcEvcUniTable,
       "cevcEvcUniEntry": cevcEvcUniEntry,
       "cevcEvcUniIndex": cevcEvcUniIndex,
       "cevcEvcUniId": cevcEvcUniId,
       "cevcEvcUniOperStatus": cevcEvcUniOperStatus,
       "cevcEvcLocalUniIfIndex": cevcEvcLocalUniIfIndex,
       "cevcServiceInstance": cevcServiceInstance,
       "cevcSITable": cevcSITable,
       "cevcSIEntry": cevcSIEntry,
       "cevcSIIndex": cevcSIIndex,
       "cevcSIRowStatus": cevcSIRowStatus,
       "cevcSIStorageType": cevcSIStorageType,
       "cevcSITargetType": cevcSITargetType,
       "cevcSITarget": cevcSITarget,
       "cevcSIName": cevcSIName,
       "cevcSIEvcIndex": cevcSIEvcIndex,
       "cevcSIAdminStatus": cevcSIAdminStatus,
       "cevcSIForwardingType": cevcSIForwardingType,
       "cevcSICreationType": cevcSICreationType,
       "cevcSIType": cevcSIType,
       "cevcSIStateTable": cevcSIStateTable,
       "cevcSIStateEntry": cevcSIStateEntry,
       "cevcSIOperStatus": cevcSIOperStatus,
       "cevcSIVlanRewriteTable": cevcSIVlanRewriteTable,
       "cevcSIVlanRewriteEntry": cevcSIVlanRewriteEntry,
       "cevcSIVlanRewriteDirection": cevcSIVlanRewriteDirection,
       "cevcSIVlanRewriteRowStatus": cevcSIVlanRewriteRowStatus,
       "cevcSIVlanRewriteStorageType": cevcSIVlanRewriteStorageType,
       "cevcSIVlanRewriteAction": cevcSIVlanRewriteAction,
       "cevcSIVlanRewriteEncapsulation": cevcSIVlanRewriteEncapsulation,
       "cevcSIVlanRewriteVlan1": cevcSIVlanRewriteVlan1,
       "cevcSIVlanRewriteVlan2": cevcSIVlanRewriteVlan2,
       "cevcSIVlanRewriteSymmetric": cevcSIVlanRewriteSymmetric,
       "cevcSIL2ControlProtocolTable": cevcSIL2ControlProtocolTable,
       "cevcSIL2ControlProtocolEntry": cevcSIL2ControlProtocolEntry,
       "cevcSIL2ControlProtocolType": cevcSIL2ControlProtocolType,
       "cevcSIL2ControlProtocolAction": cevcSIL2ControlProtocolAction,
       "cevcSICEVlanTable": cevcSICEVlanTable,
       "cevcSICEVlanEntry": cevcSICEVlanEntry,
       "cevcSICEVlanBeginningVlan": cevcSICEVlanBeginningVlan,
       "cevcSICEVlanRowStatus": cevcSICEVlanRowStatus,
       "cevcSICEVlanStorageType": cevcSICEVlanStorageType,
       "cevcSICEVlanEndingVlan": cevcSICEVlanEndingVlan,
       "cevcSIMatchCriteriaTable": cevcSIMatchCriteriaTable,
       "cevcSIMatchCriteriaEntry": cevcSIMatchCriteriaEntry,
       "cevcSIMatchCriteriaIndex": cevcSIMatchCriteriaIndex,
       "cevcSIMatchRowStatus": cevcSIMatchRowStatus,
       "cevcSIMatchStorageType": cevcSIMatchStorageType,
       "cevcSIMatchCriteriaType": cevcSIMatchCriteriaType,
       "cevcSIMatchEncapTable": cevcSIMatchEncapTable,
       "cevcSIMatchEncapEntry": cevcSIMatchEncapEntry,
       "cevcSIMatchEncapRowStatus": cevcSIMatchEncapRowStatus,
       "cevcSIMatchEncapStorageType": cevcSIMatchEncapStorageType,
       "cevcSIMatchEncapValid": cevcSIMatchEncapValid,
       "cevcSIMatchEncapEncapsulation": cevcSIMatchEncapEncapsulation,
       "cevcSIMatchEncapPrimaryCos": cevcSIMatchEncapPrimaryCos,
       "cevcSIMatchEncapSecondaryCos": cevcSIMatchEncapSecondaryCos,
       "cevcSIMatchEncapPayloadType": cevcSIMatchEncapPayloadType,
       "cevcSIMatchEncapPayloadTypes": cevcSIMatchEncapPayloadTypes,
       "cevcSIMatchEncapPriorityCos": cevcSIMatchEncapPriorityCos,
       "cevcSIPrimaryVlanTable": cevcSIPrimaryVlanTable,
       "cevcSIPrimaryVlanEntry": cevcSIPrimaryVlanEntry,
       "cevcSIPrimaryVlanBeginningVlan": cevcSIPrimaryVlanBeginningVlan,
       "cevcSIPrimaryVlanRowStatus": cevcSIPrimaryVlanRowStatus,
       "cevcSIPrimaryVlanStorageType": cevcSIPrimaryVlanStorageType,
       "cevcSIPrimaryVlanEndingVlan": cevcSIPrimaryVlanEndingVlan,
       "cevcSISecondaryVlanTable": cevcSISecondaryVlanTable,
       "cevcSISecondaryVlanEntry": cevcSISecondaryVlanEntry,
       "cevcSISecondaryVlanBeginningVlan": cevcSISecondaryVlanBeginningVlan,
       "cevcSISecondaryVlanRowStatus": cevcSISecondaryVlanRowStatus,
       "cevcSISecondaryVlanStorageType": cevcSISecondaryVlanStorageType,
       "cevcSISecondaryVlanEndingVlan": cevcSISecondaryVlanEndingVlan,
       "cevcSIForwardBdTable": cevcSIForwardBdTable,
       "cevcSIForwardBdEntry": cevcSIForwardBdEntry,
       "cevcSIForwardBdRowStatus": cevcSIForwardBdRowStatus,
       "cevcSIForwardBdStorageType": cevcSIForwardBdStorageType,
       "cevcSIForwardBdNumber": cevcSIForwardBdNumber,
       "cevcSIForwardBdNumberBase": cevcSIForwardBdNumberBase,
       "cevcSIForwardBdNumber1kBitmap": cevcSIForwardBdNumber1kBitmap,
       "cevcSIForwardBdNumber2kBitmap": cevcSIForwardBdNumber2kBitmap,
       "cevcSIForwardBdNumber3kBitmap": cevcSIForwardBdNumber3kBitmap,
       "cevcSIForwardBdNumber4kBitmap": cevcSIForwardBdNumber4kBitmap,
       "cevcEvcNotificationConfig": cevcEvcNotificationConfig,
       "cevcEvcNotifyEnabled": cevcEvcNotifyEnabled,
       "cevcMacSecurityViolation": cevcMacSecurityViolation,
       "cevcMacAddress": cevcMacAddress,
       "cevcMaxMacConfigLimit": cevcMaxMacConfigLimit,
       "cevcSIID": cevcSIID,
       "cevcViolationCause": cevcViolationCause,
       "ciscoEvcMIBConformance": ciscoEvcMIBConformance,
       "ciscoEvcMIBCompliances": ciscoEvcMIBCompliances,
       "ciscoEvcMIBCompliance": ciscoEvcMIBCompliance,
       "ciscoEvcMIBComplianceRev1": ciscoEvcMIBComplianceRev1,
       "ciscoEvcMIBComplianceRev2": ciscoEvcMIBComplianceRev2,
       "ciscoEvcMIBGroups": ciscoEvcMIBGroups,
       "cevcSystemGroup": cevcSystemGroup,
       "cevcPortGroup": cevcPortGroup,
       "cevcEvcGroup": cevcEvcGroup,
       "cevcSIGroup": cevcSIGroup,
       "cevcSIVlanRewriteGroup": cevcSIVlanRewriteGroup,
       "cevcSICosMatchCriteriaGroup": cevcSICosMatchCriteriaGroup,
       "cevcSIMatchCriteriaGroup": cevcSIMatchCriteriaGroup,
       "cevcSIForwardGroup": cevcSIForwardGroup,
       "cevcEvcNotificationConfigGroup": cevcEvcNotificationConfigGroup,
       "cevcEvcNotificationGroup": cevcEvcNotificationGroup,
       "cevcSIMatchCriteriaGroupRev1": cevcSIMatchCriteriaGroupRev1,
       "cevcEvcNotificationGroupRev1": cevcEvcNotificationGroupRev1,
       "cevcSIGroupRev1": cevcSIGroupRev1,
       "cevcSIForwardGroupRev1": cevcSIForwardGroupRev1,
       "cevcMacSecurityViolationGroup": cevcMacSecurityViolationGroup}
)
