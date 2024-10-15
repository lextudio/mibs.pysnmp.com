# SNMP MIB module (HUAWEI-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:24 2024
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

(hwConfigChangeIP,
 hwFrameIndex,
 hwSlotIndex) = mibBuilder.importSymbols(
    "HUAWEI-DEVICE-MIB",
    "hwConfigChangeIP",
    "hwFrameIndex",
    "hwSlotIndex")

(huaweiMgmt,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "huaweiMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwVlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6)
)
hwVlan.setRevisions(
        ("2015-08-07 10:00",
         "2015-04-13 00:00",
         "2015-01-22 10:00",
         "2014-12-24 10:00",
         "2014-12-23 10:00",
         "2014-11-24 10:00",
         "2014-11-13 10:00",
         "2014-09-26 10:00",
         "2014-08-30 10:00",
         "2014-08-15 10:00",
         "2014-07-20 10:00",
         "2014-06-23 10:00",
         "2014-05-08 10:00",
         "2014-04-22 10:00",
         "2014-01-15 10:00",
         "2013-12-13 10:00",
         "2013-10-29 10:00",
         "2013-08-02 10:00",
         "2013-09-14 10:00",
         "2013-02-01 10:00",
         "2013-01-18 10:00",
         "2012-11-13 10:00",
         "2012-10-29 10:00",
         "2012-08-13 10:00",
         "2012-06-15 10:00",
         "2012-03-07 00:00",
         "2012-01-30 10:00",
         "2011-09-21 00:00",
         "2011-07-15 10:00",
         "2011-04-01 10:00",
         "2011-03-25 10:00",
         "2011-02-11 10:00",
         "2011-01-24 10:00",
         "2010-12-13 00:00",
         "2010-11-24 10:00",
         "2010-11-19 10:00",
         "2010-07-03 10:00",
         "2010-06-21 10:00",
         "2010-06-20 10:00",
         "2010-06-10 10:00",
         "2010-06-07 10:00",
         "2010-05-18 10:00",
         "2010-04-26 10:00",
         "2010-03-22 10:00",
         "2010-03-18 10:00",
         "2010-02-11 10:00",
         "2010-01-25 10:00",
         "2010-01-11 10:00",
         "2010-01-08 10:00",
         "2009-12-03 00:00",
         "2009-11-16 00:00",
         "2009-02-20 00:00",
         "2007-12-20 00:00",
         "2007-04-23 00:00",
         "2005-12-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanIndex(Unsigned32, TextualConvention):
    status = "current"


class SnmpAdminString(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class PortList(OctetString, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_HwVlanMngObject_ObjectIdentity = ObjectIdentity
hwVlanMngObject = _HwVlanMngObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1)
)
if mibBuilder.loadTexts:
    hwVlanMngObject.setStatus("current")
_HwVlanMIBTable_Object = MibTable
hwVlanMIBTable = _HwVlanMIBTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 1)
)
if mibBuilder.loadTexts:
    hwVlanMIBTable.setStatus("current")
_HwVlanMIBEntry_Object = MibTableRow
hwVlanMIBEntry = _HwVlanMIBEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 1, 1)
)
hwVlanMIBEntry.setIndexNames(
    (0, "HUAWEI-VLAN-MIB", "hwVlanIndex"),
)
if mibBuilder.loadTexts:
    hwVlanMIBEntry.setStatus("current")
_HwVlanIndex_Type = VlanIndex
_HwVlanIndex_Object = MibTableColumn
hwVlanIndex = _HwVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 1, 1, 1),
    _HwVlanIndex_Type()
)
hwVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanIndex.setStatus("current")


class _HwVlanName_Type(OctetString):
    """Custom type hwVlanName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwVlanName_Type.__name__ = "OctetString"
_HwVlanName_Object = MibTableColumn
hwVlanName = _HwVlanName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 1, 1, 2),
    _HwVlanName_Type()
)
hwVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanName.setStatus("current")
_HwVlanPorts_Type = PortList
_HwVlanPorts_Object = MibTableColumn
hwVlanPorts = _HwVlanPorts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 1, 1, 3),
    _HwVlanPorts_Type()
)
hwVlanPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanPorts.setStatus("current")


class _HwVlanType_Type(Integer32):
    """Custom type hwVlanType based on Integer32"""
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
        *(("commonVlan", 2),
          ("multiVlan", 9),
          ("muxVlan", 8),
          ("primaryVlan", 4),
          ("regionVlan", 6),
          ("secondaryVlan", 5),
          ("smartVlan", 7),
          ("subVlan", 3),
          ("superVlan", 1))
    )


_HwVlanType_Type.__name__ = "Integer32"
_HwVlanType_Object = MibTableColumn
hwVlanType = _HwVlanType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 1, 1, 4),
    _HwVlanType_Type()
)
hwVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanType.setStatus("current")
_HwVlanMacFilter_Type = TruthValue
_HwVlanMacFilter_Object = MibTableColumn
hwVlanMacFilter = _HwVlanMacFilter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 1, 1, 5),
    _HwVlanMacFilter_Type()
)
hwVlanMacFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanMacFilter.setStatus("current")
_HwVlanMcastUnknownProtos_Type = TruthValue
_HwVlanMcastUnknownProtos_Object = MibTableColumn
hwVlanMcastUnknownProtos = _HwVlanMcastUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 1, 1, 6),
    _HwVlanMcastUnknownProtos_Type()
)
hwVlanMcastUnknownProtos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanMcastUnknownProtos.setStatus("current")
_HwExistInterface_Type = TruthValue
_HwExistInterface_Object = MibTableColumn
hwExistInterface = _HwExistInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 1, 1, 7),
    _HwExistInterface_Type()
)
hwExistInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwExistInterface.setStatus("current")
_HwVlanInterfaceIndex_Type = Integer32
_HwVlanInterfaceIndex_Object = MibTableColumn
hwVlanInterfaceIndex = _HwVlanInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 1, 1, 8),
    _HwVlanInterfaceIndex_Type()
)
hwVlanInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanInterfaceIndex.setStatus("current")
_HwVlanMacLearn_Type = TruthValue
_HwVlanMacLearn_Object = MibTableColumn
hwVlanMacLearn = _HwVlanMacLearn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 1, 1, 9),
    _HwVlanMacLearn_Type()
)
hwVlanMacLearn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanMacLearn.setStatus("current")


class _HwVlanStatus_Type(Integer32):
    """Custom type hwVlanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamicGvrp", 3),
          ("other", 1),
          ("permanent", 2))
    )


_HwVlanStatus_Type.__name__ = "Integer32"
_HwVlanStatus_Object = MibTableColumn
hwVlanStatus = _HwVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 1, 1, 10),
    _HwVlanStatus_Type()
)
hwVlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanStatus.setStatus("current")
_HwVlanCreationTime_Type = TimeTicks
_HwVlanCreationTime_Object = MibTableColumn
hwVlanCreationTime = _HwVlanCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 1, 1, 11),
    _HwVlanCreationTime_Type()
)
hwVlanCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanCreationTime.setStatus("current")


class _HwVlanPriority_Type(Integer32):
    """Custom type hwVlanPriority based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HwVlanPriority_Type.__name__ = "Integer32"
_HwVlanPriority_Object = MibTableColumn
hwVlanPriority = _HwVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 1, 1, 12),
    _HwVlanPriority_Type()
)
hwVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanPriority.setStatus("current")
_HwVlanRowStatus_Type = RowStatus
_HwVlanRowStatus_Object = MibTableColumn
hwVlanRowStatus = _HwVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 1, 1, 13),
    _HwVlanRowStatus_Type()
)
hwVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVlanRowStatus.setStatus("current")


class _HwVlanAttrib_Type(Integer32):
    """Custom type hwVlanAttrib based on Integer32"""
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
        *(("common", 1),
          ("qinq", 2),
          ("stacking", 3),
          ("subVlan", 4))
    )


_HwVlanAttrib_Type.__name__ = "Integer32"
_HwVlanAttrib_Object = MibTableColumn
hwVlanAttrib = _HwVlanAttrib_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 1, 1, 14),
    _HwVlanAttrib_Type()
)
hwVlanAttrib.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanAttrib.setStatus("current")


class _HwVlanSuperID_Type(Integer32):
    """Custom type hwVlanSuperID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(2, 4093),
    )


_HwVlanSuperID_Type.__name__ = "Integer32"
_HwVlanSuperID_Object = MibTableColumn
hwVlanSuperID = _HwVlanSuperID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 1, 1, 15),
    _HwVlanSuperID_Type()
)
hwVlanSuperID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanSuperID.setStatus("current")


class _HwVlanForwarding_Type(Integer32):
    """Custom type hwVlanForwarding based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vlanConnect", 2),
          ("vlanMac", 1))
    )


_HwVlanForwarding_Type.__name__ = "Integer32"
_HwVlanForwarding_Object = MibTableColumn
hwVlanForwarding = _HwVlanForwarding_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 1, 1, 16),
    _HwVlanForwarding_Type()
)
hwVlanForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanForwarding.setStatus("current")


class _HwVlanPolicyBroadcast_Type(Integer32):
    """Custom type hwVlanPolicyBroadcast based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1))
    )


_HwVlanPolicyBroadcast_Type.__name__ = "Integer32"
_HwVlanPolicyBroadcast_Object = MibTableColumn
hwVlanPolicyBroadcast = _HwVlanPolicyBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 1, 1, 17),
    _HwVlanPolicyBroadcast_Type()
)
hwVlanPolicyBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanPolicyBroadcast.setStatus("current")


class _HwVlanPolicyMulticast_Type(Integer32):
    """Custom type hwVlanPolicyMulticast based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1))
    )


_HwVlanPolicyMulticast_Type.__name__ = "Integer32"
_HwVlanPolicyMulticast_Object = MibTableColumn
hwVlanPolicyMulticast = _HwVlanPolicyMulticast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 1, 1, 18),
    _HwVlanPolicyMulticast_Type()
)
hwVlanPolicyMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanPolicyMulticast.setStatus("current")


class _HwVlanPolicyUnknowncast_Type(Integer32):
    """Custom type hwVlanPolicyUnknowncast based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1))
    )


_HwVlanPolicyUnknowncast_Type.__name__ = "Integer32"
_HwVlanPolicyUnknowncast_Object = MibTableColumn
hwVlanPolicyUnknowncast = _HwVlanPolicyUnknowncast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 1, 1, 19),
    _HwVlanPolicyUnknowncast_Type()
)
hwVlanPolicyUnknowncast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanPolicyUnknowncast.setStatus("current")


class _HwVlanOuterTpid_Type(Unsigned32):
    """Custom type hwVlanOuterTpid based on Unsigned32"""
    defaultValue = 33024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_HwVlanOuterTpid_Type.__name__ = "Unsigned32"
_HwVlanOuterTpid_Object = MibTableColumn
hwVlanOuterTpid = _HwVlanOuterTpid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 1, 1, 20),
    _HwVlanOuterTpid_Type()
)
hwVlanOuterTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanOuterTpid.setStatus("current")


class _HwVlanBindSrvProfName_Type(OctetString):
    """Custom type hwVlanBindSrvProfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwVlanBindSrvProfName_Type.__name__ = "OctetString"
_HwVlanBindSrvProfName_Object = MibTableColumn
hwVlanBindSrvProfName = _HwVlanBindSrvProfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 1, 1, 21),
    _HwVlanBindSrvProfName_Type()
)
hwVlanBindSrvProfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanBindSrvProfName.setStatus("current")


class _HwVlanChangeEnable_Type(Integer32):
    """Custom type hwVlanChangeEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addPort", 1),
          ("idle", 0),
          ("removePort", 2))
    )


_HwVlanChangeEnable_Type.__name__ = "Integer32"
_HwVlanChangeEnable_Object = MibTableColumn
hwVlanChangeEnable = _HwVlanChangeEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 1, 1, 22),
    _HwVlanChangeEnable_Type()
)
hwVlanChangeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanChangeEnable.setStatus("current")


class _HwVlanBindRaioProfileName_Type(OctetString):
    """Custom type hwVlanBindRaioProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwVlanBindRaioProfileName_Type.__name__ = "OctetString"
_HwVlanBindRaioProfileName_Object = MibTableColumn
hwVlanBindRaioProfileName = _HwVlanBindRaioProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 1, 1, 23),
    _HwVlanBindRaioProfileName_Type()
)
hwVlanBindRaioProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanBindRaioProfileName.setStatus("current")


class _HwVlanTrafficSuppressUnknowncastNetwork_Type(Integer32):
    """Custom type hwVlanTrafficSuppressUnknowncastNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 13),
    )


_HwVlanTrafficSuppressUnknowncastNetwork_Type.__name__ = "Integer32"
_HwVlanTrafficSuppressUnknowncastNetwork_Object = MibTableColumn
hwVlanTrafficSuppressUnknowncastNetwork = _HwVlanTrafficSuppressUnknowncastNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 1, 1, 24),
    _HwVlanTrafficSuppressUnknowncastNetwork_Type()
)
hwVlanTrafficSuppressUnknowncastNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanTrafficSuppressUnknowncastNetwork.setStatus("current")


class _HwVlanMethL2Forward_Type(Integer32):
    """Custom type hwVlanMethL2Forward based on Integer32"""
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


_HwVlanMethL2Forward_Type.__name__ = "Integer32"
_HwVlanMethL2Forward_Object = MibTableColumn
hwVlanMethL2Forward = _HwVlanMethL2Forward_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 1, 1, 25),
    _HwVlanMethL2Forward_Type()
)
hwVlanMethL2Forward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanMethL2Forward.setStatus("current")
_HwVlanInterfaceTable_Object = MibTable
hwVlanInterfaceTable = _HwVlanInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 2)
)
if mibBuilder.loadTexts:
    hwVlanInterfaceTable.setStatus("current")
_HwVlanInterfaceEntry_Object = MibTableRow
hwVlanInterfaceEntry = _HwVlanInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 2, 1)
)
hwVlanInterfaceEntry.setIndexNames(
    (0, "HUAWEI-VLAN-MIB", "hwVlanInterfaceID"),
)
if mibBuilder.loadTexts:
    hwVlanInterfaceEntry.setStatus("current")
_HwVlanInterfaceID_Type = Integer32
_HwVlanInterfaceID_Object = MibTableColumn
hwVlanInterfaceID = _HwVlanInterfaceID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 2, 1, 1),
    _HwVlanInterfaceID_Type()
)
hwVlanInterfaceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanInterfaceID.setStatus("current")
_HwVlanID_Type = Integer32
_HwVlanID_Object = MibTableColumn
hwVlanID = _HwVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 2, 1, 2),
    _HwVlanID_Type()
)
hwVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanID.setStatus("current")
_HwVlanIpAddress_Type = IpAddress
_HwVlanIpAddress_Object = MibTableColumn
hwVlanIpAddress = _HwVlanIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 2, 1, 3),
    _HwVlanIpAddress_Type()
)
hwVlanIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanIpAddress.setStatus("current")
_HwVlanIpAddressMask_Type = IpAddress
_HwVlanIpAddressMask_Object = MibTableColumn
hwVlanIpAddressMask = _HwVlanIpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 2, 1, 4),
    _HwVlanIpAddressMask_Type()
)
hwVlanIpAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanIpAddressMask.setStatus("current")


class _HwVlanInterfaceAdminStatus_Type(Integer32):
    """Custom type hwVlanInterfaceAdminStatus based on Integer32"""
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


_HwVlanInterfaceAdminStatus_Type.__name__ = "Integer32"
_HwVlanInterfaceAdminStatus_Object = MibTableColumn
hwVlanInterfaceAdminStatus = _HwVlanInterfaceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 2, 1, 5),
    _HwVlanInterfaceAdminStatus_Type()
)
hwVlanInterfaceAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanInterfaceAdminStatus.setStatus("current")


class _HwVlanInterfaceFrameType_Type(Integer32):
    """Custom type hwVlanInterfaceFrameType based on Integer32"""
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
        *(("ethernet8022", 3),
          ("ethernet8023", 4),
          ("ethernetii", 1),
          ("ethernetsnap", 2))
    )


_HwVlanInterfaceFrameType_Type.__name__ = "Integer32"
_HwVlanInterfaceFrameType_Object = MibTableColumn
hwVlanInterfaceFrameType = _HwVlanInterfaceFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 2, 1, 6),
    _HwVlanInterfaceFrameType_Type()
)
hwVlanInterfaceFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanInterfaceFrameType.setStatus("current")
_HwInterfaceRowStatus_Type = RowStatus
_HwInterfaceRowStatus_Object = MibTableColumn
hwInterfaceRowStatus = _HwInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 2, 1, 7),
    _HwInterfaceRowStatus_Type()
)
hwInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwInterfaceRowStatus.setStatus("current")


class _HwVlanInterfaceLinkStatus_Type(Integer32):
    """Custom type hwVlanInterfaceLinkStatus based on Integer32"""
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


_HwVlanInterfaceLinkStatus_Type.__name__ = "Integer32"
_HwVlanInterfaceLinkStatus_Object = MibTableColumn
hwVlanInterfaceLinkStatus = _HwVlanInterfaceLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 2, 1, 8),
    _HwVlanInterfaceLinkStatus_Type()
)
hwVlanInterfaceLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanInterfaceLinkStatus.setStatus("current")


class _HwVlanIfIPMode_Type(Integer32):
    """Custom type hwVlanIfIPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 2),
          ("static", 1))
    )


_HwVlanIfIPMode_Type.__name__ = "Integer32"
_HwVlanIfIPMode_Object = MibTableColumn
hwVlanIfIPMode = _HwVlanIfIPMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 2, 1, 9),
    _HwVlanIfIPMode_Type()
)
hwVlanIfIPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanIfIPMode.setStatus("current")


class _HwVlanIfDhcpClientOption60_Type(OctetString):
    """Custom type hwVlanIfDhcpClientOption60 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwVlanIfDhcpClientOption60_Type.__name__ = "OctetString"
_HwVlanIfDhcpClientOption60_Object = MibTableColumn
hwVlanIfDhcpClientOption60 = _HwVlanIfDhcpClientOption60_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 2, 1, 10),
    _HwVlanIfDhcpClientOption60_Type()
)
hwVlanIfDhcpClientOption60.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanIfDhcpClientOption60.setStatus("current")


class _HwVlanIfVlanEncapMode_Type(Integer32):
    """Custom type hwVlanIfVlanEncapMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doubleTag", 2),
          ("singleTag", 1))
    )


_HwVlanIfVlanEncapMode_Type.__name__ = "Integer32"
_HwVlanIfVlanEncapMode_Object = MibTableColumn
hwVlanIfVlanEncapMode = _HwVlanIfVlanEncapMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 2, 1, 11),
    _HwVlanIfVlanEncapMode_Type()
)
hwVlanIfVlanEncapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanIfVlanEncapMode.setStatus("current")


class _HwVlanIfVlanInnerLabel_Type(Integer32):
    """Custom type hwVlanIfVlanInnerLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_HwVlanIfVlanInnerLabel_Type.__name__ = "Integer32"
_HwVlanIfVlanInnerLabel_Object = MibTableColumn
hwVlanIfVlanInnerLabel = _HwVlanIfVlanInnerLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 2, 1, 12),
    _HwVlanIfVlanInnerLabel_Type()
)
hwVlanIfVlanInnerLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanIfVlanInnerLabel.setStatus("current")


class _HwVlanIfDHCPSStatus_Type(Integer32):
    """Custom type hwVlanIfDHCPSStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwVlanIfDHCPSStatus_Type.__name__ = "Integer32"
_HwVlanIfDHCPSStatus_Object = MibTableColumn
hwVlanIfDHCPSStatus = _HwVlanIfDHCPSStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 2, 1, 13),
    _HwVlanIfDHCPSStatus_Type()
)
hwVlanIfDHCPSStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanIfDHCPSStatus.setStatus("current")


class _HwIPv6MTU_Type(Integer32):
    """Custom type hwIPv6MTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1280, 1499),
        ValueRangeConstraint(1501, 1560),
    )


_HwIPv6MTU_Type.__name__ = "Integer32"
_HwIPv6MTU_Object = MibTableColumn
hwIPv6MTU = _HwIPv6MTU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 2, 1, 14),
    _HwIPv6MTU_Type()
)
hwIPv6MTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPv6MTU.setStatus("current")


class _HwIPv4MTU_Type(Integer32):
    """Custom type hwIPv4MTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1501, 1560),
    )


_HwIPv4MTU_Type.__name__ = "Integer32"
_HwIPv4MTU_Object = MibTableColumn
hwIPv4MTU = _HwIPv4MTU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 2, 1, 15),
    _HwIPv4MTU_Type()
)
hwIPv4MTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPv4MTU.setStatus("current")
_HwifSVLANVlanListTable_Object = MibTable
hwifSVLANVlanListTable = _HwifSVLANVlanListTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 3)
)
if mibBuilder.loadTexts:
    hwifSVLANVlanListTable.setStatus("current")
_HwifSVLANVlanListEntry_Object = MibTableRow
hwifSVLANVlanListEntry = _HwifSVLANVlanListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 3, 1)
)
hwifSVLANVlanListEntry.setIndexNames(
    (0, "HUAWEI-VLAN-MIB", "hwifSvlanVlanID"),
)
if mibBuilder.loadTexts:
    hwifSVLANVlanListEntry.setStatus("current")
_HwifSvlanVlanID_Type = VlanIndex
_HwifSvlanVlanID_Object = MibTableColumn
hwifSvlanVlanID = _HwifSvlanVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 3, 1, 1),
    _HwifSvlanVlanID_Type()
)
hwifSvlanVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifSvlanVlanID.setStatus("current")


class _HwifSvlanSubVlanlistLow_Type(OctetString):
    """Custom type hwifSvlanSubVlanlistLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwifSvlanSubVlanlistLow_Type.__name__ = "OctetString"
_HwifSvlanSubVlanlistLow_Object = MibTableColumn
hwifSvlanSubVlanlistLow = _HwifSvlanSubVlanlistLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 3, 1, 2),
    _HwifSvlanSubVlanlistLow_Type()
)
hwifSvlanSubVlanlistLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifSvlanSubVlanlistLow.setStatus("current")


class _HwifSvlanSubVlanlisHigh_Type(OctetString):
    """Custom type hwifSvlanSubVlanlisHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwifSvlanSubVlanlisHigh_Type.__name__ = "OctetString"
_HwifSvlanSubVlanlisHigh_Object = MibTableColumn
hwifSvlanSubVlanlisHigh = _HwifSvlanSubVlanlisHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 3, 1, 3),
    _HwifSvlanSubVlanlisHigh_Type()
)
hwifSvlanSubVlanlisHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifSvlanSubVlanlisHigh.setStatus("current")
_HwifSvlanOperStatus_Type = RowStatus
_HwifSvlanOperStatus_Object = MibTableColumn
hwifSvlanOperStatus = _HwifSvlanOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 3, 1, 4),
    _HwifSvlanOperStatus_Type()
)
hwifSvlanOperStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwifSvlanOperStatus.setStatus("current")
_HwifPVLANMappingTable_Object = MibTable
hwifPVLANMappingTable = _HwifPVLANMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 4)
)
if mibBuilder.loadTexts:
    hwifPVLANMappingTable.setStatus("current")
_HwifPVLANMappingEntry_Object = MibTableRow
hwifPVLANMappingEntry = _HwifPVLANMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 4, 1)
)
hwifPVLANMappingEntry.setIndexNames(
    (0, "HUAWEI-VLAN-MIB", "hwifPvlanPrimaryVlanID"),
)
if mibBuilder.loadTexts:
    hwifPVLANMappingEntry.setStatus("current")
_HwifPvlanPrimaryVlanID_Type = VlanIndex
_HwifPvlanPrimaryVlanID_Object = MibTableColumn
hwifPvlanPrimaryVlanID = _HwifPvlanPrimaryVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 4, 1, 1),
    _HwifPvlanPrimaryVlanID_Type()
)
hwifPvlanPrimaryVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifPvlanPrimaryVlanID.setStatus("current")


class _HwifPvlanSecondaryVlanlistLow_Type(OctetString):
    """Custom type hwifPvlanSecondaryVlanlistLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwifPvlanSecondaryVlanlistLow_Type.__name__ = "OctetString"
_HwifPvlanSecondaryVlanlistLow_Object = MibTableColumn
hwifPvlanSecondaryVlanlistLow = _HwifPvlanSecondaryVlanlistLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 4, 1, 2),
    _HwifPvlanSecondaryVlanlistLow_Type()
)
hwifPvlanSecondaryVlanlistLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifPvlanSecondaryVlanlistLow.setStatus("current")


class _HwifPvlanSecondaryVlanlistHigh_Type(OctetString):
    """Custom type hwifPvlanSecondaryVlanlistHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwifPvlanSecondaryVlanlistHigh_Type.__name__ = "OctetString"
_HwifPvlanSecondaryVlanlistHigh_Object = MibTableColumn
hwifPvlanSecondaryVlanlistHigh = _HwifPvlanSecondaryVlanlistHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 4, 1, 3),
    _HwifPvlanSecondaryVlanlistHigh_Type()
)
hwifPvlanSecondaryVlanlistHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifPvlanSecondaryVlanlistHigh.setStatus("current")
_HwifPvlanOperStatus_Type = RowStatus
_HwifPvlanOperStatus_Object = MibTableColumn
hwifPvlanOperStatus = _HwifPvlanOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 4, 1, 4),
    _HwifPvlanOperStatus_Type()
)
hwifPvlanOperStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwifPvlanOperStatus.setStatus("current")
_HwRegionVLanTable_Object = MibTable
hwRegionVLanTable = _HwRegionVLanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 5)
)
if mibBuilder.loadTexts:
    hwRegionVLanTable.setStatus("current")
_HwRegionVLanEntry_Object = MibTableRow
hwRegionVLanEntry = _HwRegionVLanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 5, 1)
)
hwRegionVLanEntry.setIndexNames(
    (0, "HUAWEI-VLAN-MIB", "hwVlanIndex"),
)
if mibBuilder.loadTexts:
    hwRegionVLanEntry.setStatus("current")
_HwRegionVpi_Type = Integer32
_HwRegionVpi_Object = MibTableColumn
hwRegionVpi = _HwRegionVpi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 5, 1, 1),
    _HwRegionVpi_Type()
)
hwRegionVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRegionVpi.setStatus("current")
_HwRegionVci_Type = Integer32
_HwRegionVci_Object = MibTableColumn
hwRegionVci = _HwRegionVci_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 5, 1, 2),
    _HwRegionVci_Type()
)
hwRegionVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRegionVci.setStatus("current")
_HwRegionPVCRowStatus_Type = RowStatus
_HwRegionPVCRowStatus_Object = MibTableColumn
hwRegionPVCRowStatus = _HwRegionPVCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 5, 1, 3),
    _HwRegionPVCRowStatus_Type()
)
hwRegionPVCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRegionPVCRowStatus.setStatus("current")
_HwSmartVLanTable_Object = MibTable
hwSmartVLanTable = _HwSmartVLanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 6)
)
if mibBuilder.loadTexts:
    hwSmartVLanTable.setStatus("current")
_HwSmartVLanEntry_Object = MibTableRow
hwSmartVLanEntry = _HwSmartVLanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 6, 1)
)
hwSmartVLanEntry.setIndexNames(
    (0, "HUAWEI-VLAN-MIB", "hwSmartVlanID"),
)
if mibBuilder.loadTexts:
    hwSmartVLanEntry.setStatus("current")
_HwSmartVlanID_Type = VlanIndex
_HwSmartVlanID_Object = MibTableColumn
hwSmartVlanID = _HwSmartVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 6, 1, 1),
    _HwSmartVlanID_Type()
)
hwSmartVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSmartVlanID.setStatus("current")
_HwSmartVlanUplinkPort_Type = PortList
_HwSmartVlanUplinkPort_Object = MibTableColumn
hwSmartVlanUplinkPort = _HwSmartVlanUplinkPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 6, 1, 2),
    _HwSmartVlanUplinkPort_Type()
)
hwSmartVlanUplinkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSmartVlanUplinkPort.setStatus("current")
_HwSmartVlanDownlinkPort_Type = PortList
_HwSmartVlanDownlinkPort_Object = MibTableColumn
hwSmartVlanDownlinkPort = _HwSmartVlanDownlinkPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 6, 1, 3),
    _HwSmartVlanDownlinkPort_Type()
)
hwSmartVlanDownlinkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSmartVlanDownlinkPort.setStatus("current")
_HwSmartVlanRowStatus_Type = RowStatus
_HwSmartVlanRowStatus_Object = MibTableColumn
hwSmartVlanRowStatus = _HwSmartVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 6, 1, 4),
    _HwSmartVlanRowStatus_Type()
)
hwSmartVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSmartVlanRowStatus.setStatus("current")


class _HwMuxVlanEnable_Type(Integer32):
    """Custom type hwMuxVlanEnable based on Integer32"""
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


_HwMuxVlanEnable_Type.__name__ = "Integer32"
_HwMuxVlanEnable_Object = MibScalar
hwMuxVlanEnable = _HwMuxVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 7),
    _HwMuxVlanEnable_Type()
)
hwMuxVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMuxVlanEnable.setStatus("current")
_HwMuxVlanPortConfTable_Object = MibTable
hwMuxVlanPortConfTable = _HwMuxVlanPortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 8)
)
if mibBuilder.loadTexts:
    hwMuxVlanPortConfTable.setStatus("current")
_HwMuxVlanPortConfEntry_Object = MibTableRow
hwMuxVlanPortConfEntry = _HwMuxVlanPortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 8, 1)
)
hwMuxVlanPortConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hwMuxVlanPortConfEntry.setStatus("current")


class _HwMuxVlanPortType_Type(Integer32):
    """Custom type hwMuxVlanPortType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cascadingPort", 2),
          ("uplinkPort", 1))
    )


_HwMuxVlanPortType_Type.__name__ = "Integer32"
_HwMuxVlanPortType_Object = MibTableColumn
hwMuxVlanPortType = _HwMuxVlanPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 8, 1, 1),
    _HwMuxVlanPortType_Type()
)
hwMuxVlanPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMuxVlanPortType.setStatus("current")


class _HwMuxVlanStartVlanId_Type(Integer32):
    """Custom type hwMuxVlanStartVlanId based on Integer32"""
    defaultValue = 128


_HwMuxVlanStartVlanId_Object = MibTableColumn
hwMuxVlanStartVlanId = _HwMuxVlanStartVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 8, 1, 2),
    _HwMuxVlanStartVlanId_Type()
)
hwMuxVlanStartVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMuxVlanStartVlanId.setStatus("current")
_HwMuxVlanGroupNum_Type = Integer32
_HwMuxVlanGroupNum_Object = MibTableColumn
hwMuxVlanGroupNum = _HwMuxVlanGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 8, 1, 3),
    _HwMuxVlanGroupNum_Type()
)
hwMuxVlanGroupNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMuxVlanGroupNum.setStatus("current")
_HwMuxVlanPortConfRowStatus_Type = RowStatus
_HwMuxVlanPortConfRowStatus_Object = MibTableColumn
hwMuxVlanPortConfRowStatus = _HwMuxVlanPortConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 8, 1, 4),
    _HwMuxVlanPortConfRowStatus_Type()
)
hwMuxVlanPortConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMuxVlanPortConfRowStatus.setStatus("current")
_HwMuxVlanUplinkPort_Type = Integer32
_HwMuxVlanUplinkPort_Object = MibTableColumn
hwMuxVlanUplinkPort = _HwMuxVlanUplinkPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 8, 1, 5),
    _HwMuxVlanUplinkPort_Type()
)
hwMuxVlanUplinkPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMuxVlanUplinkPort.setStatus("current")
_HwMuxVlanDownlinkPort_Type = Integer32
_HwMuxVlanDownlinkPort_Object = MibTableColumn
hwMuxVlanDownlinkPort = _HwMuxVlanDownlinkPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 8, 1, 6),
    _HwMuxVlanDownlinkPort_Type()
)
hwMuxVlanDownlinkPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMuxVlanDownlinkPort.setStatus("current")
_HwMuxVlanSlotConfTable_Object = MibTable
hwMuxVlanSlotConfTable = _HwMuxVlanSlotConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 9)
)
if mibBuilder.loadTexts:
    hwMuxVlanSlotConfTable.setStatus("current")
_HwMuxVlanSlotConfEntry_Object = MibTableRow
hwMuxVlanSlotConfEntry = _HwMuxVlanSlotConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 9, 1)
)
hwMuxVlanSlotConfEntry.setIndexNames(
    (0, "HUAWEI-DEVICE-MIB", "hwSlotIndex"),
)
if mibBuilder.loadTexts:
    hwMuxVlanSlotConfEntry.setStatus("current")
_HwMuxVlanSlotStartVlanId_Type = Integer32
_HwMuxVlanSlotStartVlanId_Object = MibTableColumn
hwMuxVlanSlotStartVlanId = _HwMuxVlanSlotStartVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 9, 1, 1),
    _HwMuxVlanSlotStartVlanId_Type()
)
hwMuxVlanSlotStartVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMuxVlanSlotStartVlanId.setStatus("current")
_HwMuxVlanSlotRowStatus_Type = RowStatus
_HwMuxVlanSlotRowStatus_Object = MibTableColumn
hwMuxVlanSlotRowStatus = _HwMuxVlanSlotRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 9, 1, 2),
    _HwMuxVlanSlotRowStatus_Type()
)
hwMuxVlanSlotRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMuxVlanSlotRowStatus.setStatus("current")
_HwMultiVLanTable_Object = MibTable
hwMultiVLanTable = _HwMultiVLanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 10)
)
if mibBuilder.loadTexts:
    hwMultiVLanTable.setStatus("current")
_HwMultiVLanEntry_Object = MibTableRow
hwMultiVLanEntry = _HwMultiVLanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 10, 1)
)
hwMultiVLanEntry.setIndexNames(
    (0, "HUAWEI-VLAN-MIB", "hwMultiVlanID"),
)
if mibBuilder.loadTexts:
    hwMultiVLanEntry.setStatus("current")
_HwMultiVlanID_Type = VlanIndex
_HwMultiVlanID_Object = MibTableColumn
hwMultiVlanID = _HwMultiVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 10, 1, 1),
    _HwMultiVlanID_Type()
)
hwMultiVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMultiVlanID.setStatus("current")
_HwMultiVlanUplinkPort_Type = PortList
_HwMultiVlanUplinkPort_Object = MibTableColumn
hwMultiVlanUplinkPort = _HwMultiVlanUplinkPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 10, 1, 2),
    _HwMultiVlanUplinkPort_Type()
)
hwMultiVlanUplinkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMultiVlanUplinkPort.setStatus("current")
_HwMultiVlanDownlinkPort_Type = PortList
_HwMultiVlanDownlinkPort_Object = MibTableColumn
hwMultiVlanDownlinkPort = _HwMultiVlanDownlinkPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 10, 1, 3),
    _HwMultiVlanDownlinkPort_Type()
)
hwMultiVlanDownlinkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMultiVlanDownlinkPort.setStatus("current")
_HwMultiVlanRowStatus_Type = RowStatus
_HwMultiVlanRowStatus_Object = MibTableColumn
hwMultiVlanRowStatus = _HwMultiVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 10, 1, 4),
    _HwMultiVlanRowStatus_Type()
)
hwMultiVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMultiVlanRowStatus.setStatus("current")
_HwVlanAggregationTable_Object = MibTable
hwVlanAggregationTable = _HwVlanAggregationTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 11)
)
if mibBuilder.loadTexts:
    hwVlanAggregationTable.setStatus("current")
_HwVlanAggregationEntry_Object = MibTableRow
hwVlanAggregationEntry = _HwVlanAggregationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 11, 1)
)
hwVlanAggregationEntry.setIndexNames(
    (0, "HUAWEI-VLAN-MIB", "hwVlanAggregationSuperVlanId"),
    (0, "HUAWEI-VLAN-MIB", "hwVlanAggregationSubVlanId"),
)
if mibBuilder.loadTexts:
    hwVlanAggregationEntry.setStatus("current")


class _HwVlanAggregationSuperVlanId_Type(Integer32):
    """Custom type hwVlanAggregationSuperVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4093),
    )


_HwVlanAggregationSuperVlanId_Type.__name__ = "Integer32"
_HwVlanAggregationSuperVlanId_Object = MibTableColumn
hwVlanAggregationSuperVlanId = _HwVlanAggregationSuperVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 11, 1, 1),
    _HwVlanAggregationSuperVlanId_Type()
)
hwVlanAggregationSuperVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanAggregationSuperVlanId.setStatus("current")


class _HwVlanAggregationSubVlanId_Type(Integer32):
    """Custom type hwVlanAggregationSubVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4093),
    )


_HwVlanAggregationSubVlanId_Type.__name__ = "Integer32"
_HwVlanAggregationSubVlanId_Object = MibTableColumn
hwVlanAggregationSubVlanId = _HwVlanAggregationSubVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 11, 1, 2),
    _HwVlanAggregationSubVlanId_Type()
)
hwVlanAggregationSubVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanAggregationSubVlanId.setStatus("current")


class _HwVlanAggregationSubVlanArpProxyStatus_Type(Integer32):
    """Custom type hwVlanAggregationSubVlanArpProxyStatus based on Integer32"""
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


_HwVlanAggregationSubVlanArpProxyStatus_Type.__name__ = "Integer32"
_HwVlanAggregationSubVlanArpProxyStatus_Object = MibTableColumn
hwVlanAggregationSubVlanArpProxyStatus = _HwVlanAggregationSubVlanArpProxyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 11, 1, 3),
    _HwVlanAggregationSubVlanArpProxyStatus_Type()
)
hwVlanAggregationSubVlanArpProxyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanAggregationSubVlanArpProxyStatus.setStatus("current")
_HwVlanAggregationRowStatus_Type = RowStatus
_HwVlanAggregationRowStatus_Object = MibTableColumn
hwVlanAggregationRowStatus = _HwVlanAggregationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 11, 1, 4),
    _HwVlanAggregationRowStatus_Type()
)
hwVlanAggregationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVlanAggregationRowStatus.setStatus("current")


class _HwVlanAggregationSubVlanNdProxyStatus_Type(Integer32):
    """Custom type hwVlanAggregationSubVlanNdProxyStatus based on Integer32"""
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


_HwVlanAggregationSubVlanNdProxyStatus_Type.__name__ = "Integer32"
_HwVlanAggregationSubVlanNdProxyStatus_Object = MibTableColumn
hwVlanAggregationSubVlanNdProxyStatus = _HwVlanAggregationSubVlanNdProxyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 11, 1, 5),
    _HwVlanAggregationSubVlanNdProxyStatus_Type()
)
hwVlanAggregationSubVlanNdProxyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanAggregationSubVlanNdProxyStatus.setStatus("current")


class _HwStackingVlanInnerEthernetType_Type(Unsigned32):
    """Custom type hwStackingVlanInnerEthernetType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwStackingVlanInnerEthernetType_Type.__name__ = "Unsigned32"
_HwStackingVlanInnerEthernetType_Object = MibScalar
hwStackingVlanInnerEthernetType = _HwStackingVlanInnerEthernetType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 13),
    _HwStackingVlanInnerEthernetType_Type()
)
hwStackingVlanInnerEthernetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStackingVlanInnerEthernetType.setStatus("current")
_HwVlanFlowAccountTable_Object = MibTable
hwVlanFlowAccountTable = _HwVlanFlowAccountTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 14)
)
if mibBuilder.loadTexts:
    hwVlanFlowAccountTable.setStatus("current")
_HwVlanFlowAccountEntry_Object = MibTableRow
hwVlanFlowAccountEntry = _HwVlanFlowAccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 14, 1)
)
hwVlanFlowAccountEntry.setIndexNames(
    (0, "HUAWEI-VLAN-MIB", "hwVlanIndex"),
    (0, "HUAWEI-VLAN-MIB", "hwInnerVlanID"),
)
if mibBuilder.loadTexts:
    hwVlanFlowAccountEntry.setStatus("current")


class _HwInnerVlanID_Type(Integer32):
    """Custom type hwInnerVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 4095),
    )


_HwInnerVlanID_Type.__name__ = "Integer32"
_HwInnerVlanID_Object = MibTableColumn
hwInnerVlanID = _HwInnerVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 14, 1, 1),
    _HwInnerVlanID_Type()
)
hwInnerVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInnerVlanID.setStatus("current")
_HwUpFlowAccountByte_Type = Counter64
_HwUpFlowAccountByte_Object = MibTableColumn
hwUpFlowAccountByte = _HwUpFlowAccountByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 14, 1, 2),
    _HwUpFlowAccountByte_Type()
)
hwUpFlowAccountByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUpFlowAccountByte.setStatus("current")
_HwDownFlowAccountByte_Type = Counter64
_HwDownFlowAccountByte_Object = MibTableColumn
hwDownFlowAccountByte = _HwDownFlowAccountByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 14, 1, 3),
    _HwDownFlowAccountByte_Type()
)
hwDownFlowAccountByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDownFlowAccountByte.setStatus("current")
_HwUpFlowAccountPacket_Type = Counter64
_HwUpFlowAccountPacket_Object = MibTableColumn
hwUpFlowAccountPacket = _HwUpFlowAccountPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 14, 1, 4),
    _HwUpFlowAccountPacket_Type()
)
hwUpFlowAccountPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUpFlowAccountPacket.setStatus("current")
_HwDownFlowAccountPacket_Type = Counter64
_HwDownFlowAccountPacket_Object = MibTableColumn
hwDownFlowAccountPacket = _HwDownFlowAccountPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 14, 1, 5),
    _HwDownFlowAccountPacket_Type()
)
hwDownFlowAccountPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDownFlowAccountPacket.setStatus("current")
_HwUpStreamPacket_Type = Counter64
_HwUpStreamPacket_Object = MibTableColumn
hwUpStreamPacket = _HwUpStreamPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 14, 1, 6),
    _HwUpStreamPacket_Type()
)
hwUpStreamPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUpStreamPacket.setStatus("current")
_HwDownStreamPacket_Type = Counter64
_HwDownStreamPacket_Object = MibTableColumn
hwDownStreamPacket = _HwDownStreamPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 14, 1, 7),
    _HwDownStreamPacket_Type()
)
hwDownStreamPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDownStreamPacket.setStatus("current")


class _HwFlowAccountAdminStatus_Type(Integer32):
    """Custom type hwFlowAccountAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", -1),
          ("reset", 0),
          ("resetAcl", 1))
    )


_HwFlowAccountAdminStatus_Type.__name__ = "Integer32"
_HwFlowAccountAdminStatus_Object = MibTableColumn
hwFlowAccountAdminStatus = _HwFlowAccountAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 14, 1, 8),
    _HwFlowAccountAdminStatus_Type()
)
hwFlowAccountAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwFlowAccountAdminStatus.setStatus("current")
_HwUpFlowAccountDiscardPacket_Type = Counter64
_HwUpFlowAccountDiscardPacket_Object = MibTableColumn
hwUpFlowAccountDiscardPacket = _HwUpFlowAccountDiscardPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 14, 1, 9),
    _HwUpFlowAccountDiscardPacket_Type()
)
hwUpFlowAccountDiscardPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUpFlowAccountDiscardPacket.setStatus("current")
_HwDownFlowAccountDiscardPacket_Type = Counter64
_HwDownFlowAccountDiscardPacket_Object = MibTableColumn
hwDownFlowAccountDiscardPacket = _HwDownFlowAccountDiscardPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 14, 1, 10),
    _HwDownFlowAccountDiscardPacket_Type()
)
hwDownFlowAccountDiscardPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDownFlowAccountDiscardPacket.setStatus("current")
_HwVlanUpCarTable_Object = MibTable
hwVlanUpCarTable = _HwVlanUpCarTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 15)
)
if mibBuilder.loadTexts:
    hwVlanUpCarTable.setStatus("current")
_HwVlanUpCarEntry_Object = MibTableRow
hwVlanUpCarEntry = _HwVlanUpCarEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 15, 1)
)
hwVlanUpCarEntry.setIndexNames(
    (0, "HUAWEI-VLAN-MIB", "hwVlanUpCarId"),
)
if mibBuilder.loadTexts:
    hwVlanUpCarEntry.setStatus("current")


class _HwVlanUpCarId_Type(Integer32):
    """Custom type hwVlanUpCarId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_HwVlanUpCarId_Type.__name__ = "Integer32"
_HwVlanUpCarId_Object = MibTableColumn
hwVlanUpCarId = _HwVlanUpCarId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 15, 1, 1),
    _HwVlanUpCarId_Type()
)
hwVlanUpCarId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanUpCarId.setStatus("current")


class _HwVlanUpCarName_Type(OctetString):
    """Custom type hwVlanUpCarName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwVlanUpCarName_Type.__name__ = "OctetString"
_HwVlanUpCarName_Object = MibTableColumn
hwVlanUpCarName = _HwVlanUpCarName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 15, 1, 2),
    _HwVlanUpCarName_Type()
)
hwVlanUpCarName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanUpCarName.setStatus("current")


class _HwVlanUpCarBandValue_Type(Integer32):
    """Custom type hwVlanUpCarBandValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1048512),
    )


_HwVlanUpCarBandValue_Type.__name__ = "Integer32"
_HwVlanUpCarBandValue_Object = MibTableColumn
hwVlanUpCarBandValue = _HwVlanUpCarBandValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 15, 1, 3),
    _HwVlanUpCarBandValue_Type()
)
hwVlanUpCarBandValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanUpCarBandValue.setStatus("current")


class _HwVlanUpCarBurstValue_Type(Integer32):
    """Custom type hwVlanUpCarBurstValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 8192),
    )


_HwVlanUpCarBurstValue_Type.__name__ = "Integer32"
_HwVlanUpCarBurstValue_Object = MibTableColumn
hwVlanUpCarBurstValue = _HwVlanUpCarBurstValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 15, 1, 4),
    _HwVlanUpCarBurstValue_Type()
)
hwVlanUpCarBurstValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanUpCarBurstValue.setStatus("current")


class _HwVlanUpCarIsUsed_Type(Integer32):
    """Custom type hwVlanUpCarIsUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noUsed", 2),
          ("used", 1))
    )


_HwVlanUpCarIsUsed_Type.__name__ = "Integer32"
_HwVlanUpCarIsUsed_Object = MibTableColumn
hwVlanUpCarIsUsed = _HwVlanUpCarIsUsed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 15, 1, 5),
    _HwVlanUpCarIsUsed_Type()
)
hwVlanUpCarIsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanUpCarIsUsed.setStatus("current")
_HwVlanUpCarRowStatus_Type = RowStatus
_HwVlanUpCarRowStatus_Object = MibTableColumn
hwVlanUpCarRowStatus = _HwVlanUpCarRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 15, 1, 6),
    _HwVlanUpCarRowStatus_Type()
)
hwVlanUpCarRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVlanUpCarRowStatus.setStatus("current")
_HwVlanDownCarTable_Object = MibTable
hwVlanDownCarTable = _HwVlanDownCarTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 16)
)
if mibBuilder.loadTexts:
    hwVlanDownCarTable.setStatus("current")
_HwVlanDownCarEntry_Object = MibTableRow
hwVlanDownCarEntry = _HwVlanDownCarEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 16, 1)
)
hwVlanDownCarEntry.setIndexNames(
    (0, "HUAWEI-VLAN-MIB", "hwVlanDownCarId"),
)
if mibBuilder.loadTexts:
    hwVlanDownCarEntry.setStatus("current")


class _HwVlanDownCarId_Type(Integer32):
    """Custom type hwVlanDownCarId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_HwVlanDownCarId_Type.__name__ = "Integer32"
_HwVlanDownCarId_Object = MibTableColumn
hwVlanDownCarId = _HwVlanDownCarId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 16, 1, 1),
    _HwVlanDownCarId_Type()
)
hwVlanDownCarId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanDownCarId.setStatus("current")


class _HwVlanDownCarName_Type(OctetString):
    """Custom type hwVlanDownCarName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwVlanDownCarName_Type.__name__ = "OctetString"
_HwVlanDownCarName_Object = MibTableColumn
hwVlanDownCarName = _HwVlanDownCarName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 16, 1, 2),
    _HwVlanDownCarName_Type()
)
hwVlanDownCarName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanDownCarName.setStatus("current")


class _HwVlanDownCarBandValue_Type(Integer32):
    """Custom type hwVlanDownCarBandValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1048512),
    )


_HwVlanDownCarBandValue_Type.__name__ = "Integer32"
_HwVlanDownCarBandValue_Object = MibTableColumn
hwVlanDownCarBandValue = _HwVlanDownCarBandValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 16, 1, 3),
    _HwVlanDownCarBandValue_Type()
)
hwVlanDownCarBandValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanDownCarBandValue.setStatus("current")


class _HwVlanDownCarBurstValue_Type(Integer32):
    """Custom type hwVlanDownCarBurstValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 8192),
    )


_HwVlanDownCarBurstValue_Type.__name__ = "Integer32"
_HwVlanDownCarBurstValue_Object = MibTableColumn
hwVlanDownCarBurstValue = _HwVlanDownCarBurstValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 16, 1, 4),
    _HwVlanDownCarBurstValue_Type()
)
hwVlanDownCarBurstValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanDownCarBurstValue.setStatus("current")


class _HwVlanDownCarIsUsed_Type(Integer32):
    """Custom type hwVlanDownCarIsUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noUsed", 2),
          ("used", 1))
    )


_HwVlanDownCarIsUsed_Type.__name__ = "Integer32"
_HwVlanDownCarIsUsed_Object = MibTableColumn
hwVlanDownCarIsUsed = _HwVlanDownCarIsUsed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 16, 1, 5),
    _HwVlanDownCarIsUsed_Type()
)
hwVlanDownCarIsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanDownCarIsUsed.setStatus("current")
_HwVlanDownCarRowStatus_Type = RowStatus
_HwVlanDownCarRowStatus_Object = MibTableColumn
hwVlanDownCarRowStatus = _HwVlanDownCarRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 16, 1, 6),
    _HwVlanDownCarRowStatus_Type()
)
hwVlanDownCarRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVlanDownCarRowStatus.setStatus("current")
_HwVlanParaTable_Object = MibTable
hwVlanParaTable = _HwVlanParaTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 17)
)
if mibBuilder.loadTexts:
    hwVlanParaTable.setStatus("current")
_HwVlanParaEntry_Object = MibTableRow
hwVlanParaEntry = _HwVlanParaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 17, 1)
)
hwVlanParaEntry.setIndexNames(
    (0, "HUAWEI-VLAN-MIB", "hwVlanParaIndex"),
)
if mibBuilder.loadTexts:
    hwVlanParaEntry.setStatus("current")
_HwVlanParaIndex_Type = VlanIndex
_HwVlanParaIndex_Object = MibTableColumn
hwVlanParaIndex = _HwVlanParaIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 17, 1, 1),
    _HwVlanParaIndex_Type()
)
hwVlanParaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanParaIndex.setStatus("current")


class _HwVlanMacLearnCpability_Type(Integer32):
    """Custom type hwVlanMacLearnCpability based on Integer32"""
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


_HwVlanMacLearnCpability_Type.__name__ = "Integer32"
_HwVlanMacLearnCpability_Object = MibTableColumn
hwVlanMacLearnCpability = _HwVlanMacLearnCpability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 17, 1, 2),
    _HwVlanMacLearnCpability_Type()
)
hwVlanMacLearnCpability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanMacLearnCpability.setStatus("current")


class _HwVlanMaxMacLearnNum_Type(Integer32):
    """Custom type hwVlanMaxMacLearnNum based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwVlanMaxMacLearnNum_Type.__name__ = "Integer32"
_HwVlanMaxMacLearnNum_Object = MibTableColumn
hwVlanMaxMacLearnNum = _HwVlanMaxMacLearnNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 17, 1, 3),
    _HwVlanMaxMacLearnNum_Type()
)
hwVlanMaxMacLearnNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanMaxMacLearnNum.setStatus("current")


class _HwVlanUpDirectCarID_Type(Integer32):
    """Custom type hwVlanUpDirectCarID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_HwVlanUpDirectCarID_Type.__name__ = "Integer32"
_HwVlanUpDirectCarID_Object = MibTableColumn
hwVlanUpDirectCarID = _HwVlanUpDirectCarID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 17, 1, 4),
    _HwVlanUpDirectCarID_Type()
)
hwVlanUpDirectCarID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanUpDirectCarID.setStatus("current")


class _HwVlanDownDirectCarID_Type(Integer32):
    """Custom type hwVlanDownDirectCarID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_HwVlanDownDirectCarID_Type.__name__ = "Integer32"
_HwVlanDownDirectCarID_Object = MibTableColumn
hwVlanDownDirectCarID = _HwVlanDownDirectCarID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 17, 1, 5),
    _HwVlanDownDirectCarID_Type()
)
hwVlanDownDirectCarID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanDownDirectCarID.setStatus("current")
_HwBpduTunnelTable_Object = MibTable
hwBpduTunnelTable = _HwBpduTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 18)
)
if mibBuilder.loadTexts:
    hwBpduTunnelTable.setStatus("current")
_HwBpduTunnelEntry_Object = MibTableRow
hwBpduTunnelEntry = _HwBpduTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 18, 1)
)
hwBpduTunnelEntry.setIndexNames(
    (0, "HUAWEI-VLAN-MIB", "hwVlanIndex"),
)
if mibBuilder.loadTexts:
    hwBpduTunnelEntry.setStatus("current")


class _HwBpduTunnel_Type(Integer32):
    """Custom type hwBpduTunnel based on Integer32"""
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


_HwBpduTunnel_Type.__name__ = "Integer32"
_HwBpduTunnel_Object = MibTableColumn
hwBpduTunnel = _HwBpduTunnel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 18, 1, 1),
    _HwBpduTunnel_Type()
)
hwBpduTunnel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBpduTunnel.setStatus("current")
_HwVOIPAddressTable_Object = MibTable
hwVOIPAddressTable = _HwVOIPAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 19)
)
if mibBuilder.loadTexts:
    hwVOIPAddressTable.setStatus("current")
_HwVOIPAddressEntry_Object = MibTableRow
hwVOIPAddressEntry = _HwVOIPAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 19, 1)
)
hwVOIPAddressEntry.setIndexNames(
    (0, "HUAWEI-VLAN-MIB", "hwVOIPAddressIndex"),
)
if mibBuilder.loadTexts:
    hwVOIPAddressEntry.setStatus("current")


class _HwVOIPAddressIndex_Type(Integer32):
    """Custom type hwVOIPAddressIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HwVOIPAddressIndex_Type.__name__ = "Integer32"
_HwVOIPAddressIndex_Object = MibTableColumn
hwVOIPAddressIndex = _HwVOIPAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 19, 1, 1),
    _HwVOIPAddressIndex_Type()
)
hwVOIPAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVOIPAddressIndex.setStatus("current")


class _HwVOIPIPType_Type(Integer32):
    """Custom type hwVOIPIPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("media", 1),
          ("signaling", 2))
    )


_HwVOIPIPType_Type.__name__ = "Integer32"
_HwVOIPIPType_Object = MibTableColumn
hwVOIPIPType = _HwVOIPIPType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 19, 1, 2),
    _HwVOIPIPType_Type()
)
hwVOIPIPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVOIPIPType.setStatus("current")
_HwVOIPIPAddress_Type = IpAddress
_HwVOIPIPAddress_Object = MibTableColumn
hwVOIPIPAddress = _HwVOIPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 19, 1, 3),
    _HwVOIPIPAddress_Type()
)
hwVOIPIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVOIPIPAddress.setStatus("current")
_HwVOIPSubMask_Type = IpAddress
_HwVOIPSubMask_Object = MibTableColumn
hwVOIPSubMask = _HwVOIPSubMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 19, 1, 4),
    _HwVOIPSubMask_Type()
)
hwVOIPSubMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVOIPSubMask.setStatus("current")
_HwVOIPGateway_Type = IpAddress
_HwVOIPGateway_Object = MibTableColumn
hwVOIPGateway = _HwVOIPGateway_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 19, 1, 5),
    _HwVOIPGateway_Type()
)
hwVOIPGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVOIPGateway.setStatus("current")


class _HwVOIPMACAddress_Type(OctetString):
    """Custom type hwVOIPMACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_HwVOIPMACAddress_Type.__name__ = "OctetString"
_HwVOIPMACAddress_Object = MibTableColumn
hwVOIPMACAddress = _HwVOIPMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 19, 1, 6),
    _HwVOIPMACAddress_Type()
)
hwVOIPMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVOIPMACAddress.setStatus("current")


class _HwVOIPVlanTagIdentifier_Type(Integer32):
    """Custom type hwVOIPVlanTagIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_HwVOIPVlanTagIdentifier_Type.__name__ = "Integer32"
_HwVOIPVlanTagIdentifier_Object = MibTableColumn
hwVOIPVlanTagIdentifier = _HwVOIPVlanTagIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 19, 1, 7),
    _HwVOIPVlanTagIdentifier_Type()
)
hwVOIPVlanTagIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVOIPVlanTagIdentifier.setStatus("current")


class _HwVOIPQosIPStrategy_Type(Integer32):
    """Custom type hwVOIPQosIPStrategy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dscp", 2),
          ("tos", 1))
    )


_HwVOIPQosIPStrategy_Type.__name__ = "Integer32"
_HwVOIPQosIPStrategy_Object = MibTableColumn
hwVOIPQosIPStrategy = _HwVOIPQosIPStrategy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 19, 1, 8),
    _HwVOIPQosIPStrategy_Type()
)
hwVOIPQosIPStrategy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVOIPQosIPStrategy.setStatus("current")
_HwVOIPAddressRowStatus_Type = RowStatus
_HwVOIPAddressRowStatus_Object = MibTableColumn
hwVOIPAddressRowStatus = _HwVOIPAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 19, 1, 9),
    _HwVOIPAddressRowStatus_Type()
)
hwVOIPAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVOIPAddressRowStatus.setStatus("current")


class _HwVOIPAddressObtainMode_Type(Integer32):
    """Custom type hwVOIPAddressObtainMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 3),
          ("pppoe", 2),
          ("static", 1))
    )


_HwVOIPAddressObtainMode_Type.__name__ = "Integer32"
_HwVOIPAddressObtainMode_Object = MibTableColumn
hwVOIPAddressObtainMode = _HwVOIPAddressObtainMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 19, 1, 10),
    _HwVOIPAddressObtainMode_Type()
)
hwVOIPAddressObtainMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVOIPAddressObtainMode.setStatus("current")


class _HwVOIPPPPOEClientName_Type(OctetString):
    """Custom type hwVOIPPPPOEClientName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65),
    )


_HwVOIPPPPOEClientName_Type.__name__ = "OctetString"
_HwVOIPPPPOEClientName_Object = MibTableColumn
hwVOIPPPPOEClientName = _HwVOIPPPPOEClientName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 19, 1, 11),
    _HwVOIPPPPOEClientName_Type()
)
hwVOIPPPPOEClientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVOIPPPPOEClientName.setStatus("current")


class _HwVOIPIPAddressSrc_Type(Integer32):
    """Custom type hwVOIPIPAddressSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 1),
          ("static", 0))
    )


_HwVOIPIPAddressSrc_Type.__name__ = "Integer32"
_HwVOIPIPAddressSrc_Object = MibTableColumn
hwVOIPIPAddressSrc = _HwVOIPIPAddressSrc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 19, 1, 12),
    _HwVOIPIPAddressSrc_Type()
)
hwVOIPIPAddressSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVOIPIPAddressSrc.setStatus("current")
_HwVOIPQosTable_Object = MibTable
hwVOIPQosTable = _HwVOIPQosTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 20)
)
if mibBuilder.loadTexts:
    hwVOIPQosTable.setStatus("current")
_HwVOIPQosEntry_Object = MibTableRow
hwVOIPQosEntry = _HwVOIPQosEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 20, 1)
)
hwVOIPQosEntry.setIndexNames(
    (0, "HUAWEI-VLAN-MIB", "hwVOIPAddressIndex"),
)
if mibBuilder.loadTexts:
    hwVOIPQosEntry.setStatus("current")


class _HwVOIPQosIPTosValue_Type(Integer32):
    """Custom type hwVOIPQosIPTosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwVOIPQosIPTosValue_Type.__name__ = "Integer32"
_HwVOIPQosIPTosValue_Object = MibTableColumn
hwVOIPQosIPTosValue = _HwVOIPQosIPTosValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 20, 1, 1),
    _HwVOIPQosIPTosValue_Type()
)
hwVOIPQosIPTosValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVOIPQosIPTosValue.setStatus("current")


class _HwVOIPQosIPDscpValue_Type(Integer32):
    """Custom type hwVOIPQosIPDscpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwVOIPQosIPDscpValue_Type.__name__ = "Integer32"
_HwVOIPQosIPDscpValue_Object = MibTableColumn
hwVOIPQosIPDscpValue = _HwVOIPQosIPDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 20, 1, 2),
    _HwVOIPQosIPDscpValue_Type()
)
hwVOIPQosIPDscpValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVOIPQosIPDscpValue.setStatus("current")


class _HwVOIPQosVlanPriority_Type(Integer32):
    """Custom type hwVOIPQosVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwVOIPQosVlanPriority_Type.__name__ = "Integer32"
_HwVOIPQosVlanPriority_Object = MibTableColumn
hwVOIPQosVlanPriority = _HwVOIPQosVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 20, 1, 3),
    _HwVOIPQosVlanPriority_Type()
)
hwVOIPQosVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVOIPQosVlanPriority.setStatus("current")


class _HwVOIPQosIPAddressSrc_Type(Integer32):
    """Custom type hwVOIPQosIPAddressSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 1),
          ("static", 0))
    )


_HwVOIPQosIPAddressSrc_Type.__name__ = "Integer32"
_HwVOIPQosIPAddressSrc_Object = MibTableColumn
hwVOIPQosIPAddressSrc = _HwVOIPQosIPAddressSrc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 20, 1, 4),
    _HwVOIPQosIPAddressSrc_Type()
)
hwVOIPQosIPAddressSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVOIPQosIPAddressSrc.setStatus("current")
_HwPacketTunnelTable_Object = MibTable
hwPacketTunnelTable = _HwPacketTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 21)
)
if mibBuilder.loadTexts:
    hwPacketTunnelTable.setStatus("current")
_HwPacketTunnelEntry_Object = MibTableRow
hwPacketTunnelEntry = _HwPacketTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 21, 1)
)
hwPacketTunnelEntry.setIndexNames(
    (0, "HUAWEI-VLAN-MIB", "hwVlanIndex"),
)
if mibBuilder.loadTexts:
    hwPacketTunnelEntry.setStatus("current")


class _HwPacketTunnelRip_Type(Integer32):
    """Custom type hwPacketTunnelRip based on Integer32"""
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


_HwPacketTunnelRip_Type.__name__ = "Integer32"
_HwPacketTunnelRip_Object = MibTableColumn
hwPacketTunnelRip = _HwPacketTunnelRip_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 21, 1, 1),
    _HwPacketTunnelRip_Type()
)
hwPacketTunnelRip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPacketTunnelRip.setStatus("current")


class _HwPacketTunnelVTPCDP_Type(Integer32):
    """Custom type hwPacketTunnelVTPCDP based on Integer32"""
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


_HwPacketTunnelVTPCDP_Type.__name__ = "Integer32"
_HwPacketTunnelVTPCDP_Object = MibTableColumn
hwPacketTunnelVTPCDP = _HwPacketTunnelVTPCDP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 21, 1, 2),
    _HwPacketTunnelVTPCDP_Type()
)
hwPacketTunnelVTPCDP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPacketTunnelVTPCDP.setStatus("current")
_HwVlanInterfaceSubIpAddrTable_Object = MibTable
hwVlanInterfaceSubIpAddrTable = _HwVlanInterfaceSubIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 22)
)
if mibBuilder.loadTexts:
    hwVlanInterfaceSubIpAddrTable.setStatus("current")
_HwVlanInterfaceSubIpAddrEntry_Object = MibTableRow
hwVlanInterfaceSubIpAddrEntry = _HwVlanInterfaceSubIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 22, 1)
)
hwVlanInterfaceSubIpAddrEntry.setIndexNames(
    (0, "HUAWEI-VLAN-MIB", "hwVlanInterfaceIDWithSub"),
    (0, "HUAWEI-VLAN-MIB", "hwVlanSubIpAddress"),
    (0, "HUAWEI-VLAN-MIB", "hwVlanSubIpAddressMask"),
)
if mibBuilder.loadTexts:
    hwVlanInterfaceSubIpAddrEntry.setStatus("current")
_HwVlanInterfaceIDWithSub_Type = Integer32
_HwVlanInterfaceIDWithSub_Object = MibTableColumn
hwVlanInterfaceIDWithSub = _HwVlanInterfaceIDWithSub_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 22, 1, 1),
    _HwVlanInterfaceIDWithSub_Type()
)
hwVlanInterfaceIDWithSub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanInterfaceIDWithSub.setStatus("current")
_HwVlanSubIpAddress_Type = IpAddress
_HwVlanSubIpAddress_Object = MibTableColumn
hwVlanSubIpAddress = _HwVlanSubIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 22, 1, 2),
    _HwVlanSubIpAddress_Type()
)
hwVlanSubIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanSubIpAddress.setStatus("current")
_HwVlanSubIpAddressMask_Type = IpAddress
_HwVlanSubIpAddressMask_Object = MibTableColumn
hwVlanSubIpAddressMask = _HwVlanSubIpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 22, 1, 3),
    _HwVlanSubIpAddressMask_Type()
)
hwVlanSubIpAddressMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanSubIpAddressMask.setStatus("current")
_HwInterfaceSubIpAddrRowStatus_Type = RowStatus
_HwInterfaceSubIpAddrRowStatus_Object = MibTableColumn
hwInterfaceSubIpAddrRowStatus = _HwInterfaceSubIpAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 22, 1, 4),
    _HwInterfaceSubIpAddrRowStatus_Type()
)
hwInterfaceSubIpAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwInterfaceSubIpAddrRowStatus.setStatus("current")


class _HwMethL2Vlan_Type(Integer32):
    """Custom type hwMethL2Vlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_HwMethL2Vlan_Type.__name__ = "Integer32"
_HwMethL2Vlan_Object = MibScalar
hwMethL2Vlan = _HwMethL2Vlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 23),
    _HwMethL2Vlan_Type()
)
hwMethL2Vlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMethL2Vlan.setStatus("current")


class _HwDocsDefaultSrvVlanID_Type(Integer32):
    """Custom type hwDocsDefaultSrvVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_HwDocsDefaultSrvVlanID_Type.__name__ = "Integer32"
_HwDocsDefaultSrvVlanID_Object = MibScalar
hwDocsDefaultSrvVlanID = _HwDocsDefaultSrvVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 24),
    _HwDocsDefaultSrvVlanID_Type()
)
hwDocsDefaultSrvVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDocsDefaultSrvVlanID.setStatus("current")
_HwVlanSrvProfTable_Object = MibTable
hwVlanSrvProfTable = _HwVlanSrvProfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25)
)
if mibBuilder.loadTexts:
    hwVlanSrvProfTable.setStatus("current")
_HwVlanSrvProfEntry_Object = MibTableRow
hwVlanSrvProfEntry = _HwVlanSrvProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1)
)
hwVlanSrvProfEntry.setIndexNames(
    (0, "HUAWEI-VLAN-MIB", "hwVlanSrvProfName"),
)
if mibBuilder.loadTexts:
    hwVlanSrvProfEntry.setStatus("current")


class _HwVlanSrvProfName_Type(OctetString):
    """Custom type hwVlanSrvProfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwVlanSrvProfName_Type.__name__ = "OctetString"
_HwVlanSrvProfName_Object = MibTableColumn
hwVlanSrvProfName = _HwVlanSrvProfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 1),
    _HwVlanSrvProfName_Type()
)
hwVlanSrvProfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanSrvProfName.setStatus("current")


class _HwForwardingMode_Type(Integer32):
    """Custom type hwForwardingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notConfig", 3),
          ("vlanConnect", 2),
          ("vlanMac", 1))
    )


_HwForwardingMode_Type.__name__ = "Integer32"
_HwForwardingMode_Object = MibTableColumn
hwForwardingMode = _HwForwardingMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 2),
    _HwForwardingMode_Type()
)
hwForwardingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwForwardingMode.setStatus("current")


class _HwAntiIpSpoofingSwitch_Type(Integer32):
    """Custom type hwAntiIpSpoofingSwitch based on Integer32"""
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


_HwAntiIpSpoofingSwitch_Type.__name__ = "Integer32"
_HwAntiIpSpoofingSwitch_Object = MibTableColumn
hwAntiIpSpoofingSwitch = _HwAntiIpSpoofingSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 3),
    _HwAntiIpSpoofingSwitch_Type()
)
hwAntiIpSpoofingSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAntiIpSpoofingSwitch.setStatus("current")


class _HwAntiMacSpoofingSwitch_Type(Integer32):
    """Custom type hwAntiMacSpoofingSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notConfig", 3))
    )


_HwAntiMacSpoofingSwitch_Type.__name__ = "Integer32"
_HwAntiMacSpoofingSwitch_Object = MibTableColumn
hwAntiMacSpoofingSwitch = _HwAntiMacSpoofingSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 4),
    _HwAntiMacSpoofingSwitch_Type()
)
hwAntiMacSpoofingSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAntiMacSpoofingSwitch.setStatus("current")


class _HwPPPoEMacMode_Type(Integer32):
    """Custom type hwPPPoEMacMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("multiMac", 1),
          ("notConfig", 3),
          ("singleMac", 2))
    )


_HwPPPoEMacMode_Type.__name__ = "Integer32"
_HwPPPoEMacMode_Object = MibTableColumn
hwPPPoEMacMode = _HwPPPoEMacMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 5),
    _HwPPPoEMacMode_Type()
)
hwPPPoEMacMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPPPoEMacMode.setStatus("current")


class _HwBpduTunnelSwitch_Type(Integer32):
    """Custom type hwBpduTunnelSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notConfig", 3))
    )


_HwBpduTunnelSwitch_Type.__name__ = "Integer32"
_HwBpduTunnelSwitch_Object = MibTableColumn
hwBpduTunnelSwitch = _HwBpduTunnelSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 6),
    _HwBpduTunnelSwitch_Type()
)
hwBpduTunnelSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBpduTunnelSwitch.setStatus("current")


class _HwRipTunnelSwitch_Type(Integer32):
    """Custom type hwRipTunnelSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notConfig", 3))
    )


_HwRipTunnelSwitch_Type.__name__ = "Integer32"
_HwRipTunnelSwitch_Object = MibTableColumn
hwRipTunnelSwitch = _HwRipTunnelSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 7),
    _HwRipTunnelSwitch_Type()
)
hwRipTunnelSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRipTunnelSwitch.setStatus("current")


class _HwVtpCdpTunnelSwitch_Type(Integer32):
    """Custom type hwVtpCdpTunnelSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notConfig", 3))
    )


_HwVtpCdpTunnelSwitch_Type.__name__ = "Integer32"
_HwVtpCdpTunnelSwitch_Object = MibTableColumn
hwVtpCdpTunnelSwitch = _HwVtpCdpTunnelSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 8),
    _HwVtpCdpTunnelSwitch_Type()
)
hwVtpCdpTunnelSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVtpCdpTunnelSwitch.setStatus("current")


class _HwDhcpMode_Type(Integer32):
    """Custom type hwDhcpMode based on Integer32"""
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
        *(("l3MacRange", 5),
          ("l3Option60", 4),
          ("l3Standard", 3),
          ("layer2", 2),
          ("notConfig", 1))
    )


_HwDhcpMode_Type.__name__ = "Integer32"
_HwDhcpMode_Object = MibTableColumn
hwDhcpMode = _HwDhcpMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 9),
    _HwDhcpMode_Type()
)
hwDhcpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDhcpMode.setStatus("current")


class _HwDhcpProxySwitch_Type(Integer32):
    """Custom type hwDhcpProxySwitch based on Integer32"""
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


_HwDhcpProxySwitch_Type.__name__ = "Integer32"
_HwDhcpProxySwitch_Object = MibTableColumn
hwDhcpProxySwitch = _HwDhcpProxySwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 10),
    _HwDhcpProxySwitch_Type()
)
hwDhcpProxySwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDhcpProxySwitch.setStatus("current")


class _HwDhcpOption82Switch_Type(Integer32):
    """Custom type hwDhcpOption82Switch based on Integer32"""
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


_HwDhcpOption82Switch_Type.__name__ = "Integer32"
_HwDhcpOption82Switch_Object = MibTableColumn
hwDhcpOption82Switch = _HwDhcpOption82Switch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 11),
    _HwDhcpOption82Switch_Type()
)
hwDhcpOption82Switch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDhcpOption82Switch.setStatus("current")


class _HwPitpSwitch_Type(Integer32):
    """Custom type hwPitpSwitch based on Integer32"""
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


_HwPitpSwitch_Type.__name__ = "Integer32"
_HwPitpSwitch_Object = MibTableColumn
hwPitpSwitch = _HwPitpSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 12),
    _HwPitpSwitch_Type()
)
hwPitpSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPitpSwitch.setStatus("current")


class _HwPolicyBroadcast_Type(Integer32):
    """Custom type hwPolicyBroadcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1),
          ("notConfig", 3))
    )


_HwPolicyBroadcast_Type.__name__ = "Integer32"
_HwPolicyBroadcast_Object = MibTableColumn
hwPolicyBroadcast = _HwPolicyBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 13),
    _HwPolicyBroadcast_Type()
)
hwPolicyBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPolicyBroadcast.setStatus("current")


class _HwPolicyMulticast_Type(Integer32):
    """Custom type hwPolicyMulticast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1),
          ("notConfig", 3))
    )


_HwPolicyMulticast_Type.__name__ = "Integer32"
_HwPolicyMulticast_Object = MibTableColumn
hwPolicyMulticast = _HwPolicyMulticast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 14),
    _HwPolicyMulticast_Type()
)
hwPolicyMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPolicyMulticast.setStatus("current")


class _HwPolicyUnknowncast_Type(Integer32):
    """Custom type hwPolicyUnknowncast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1),
          ("notConfig", 3))
    )


_HwPolicyUnknowncast_Type.__name__ = "Integer32"
_HwPolicyUnknowncast_Object = MibTableColumn
hwPolicyUnknowncast = _HwPolicyUnknowncast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 15),
    _HwPolicyUnknowncast_Type()
)
hwPolicyUnknowncast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPolicyUnknowncast.setStatus("current")


class _HwUserBridging_Type(Integer32):
    """Custom type hwUserBridging based on Integer32"""
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


_HwUserBridging_Type.__name__ = "Integer32"
_HwUserBridging_Object = MibTableColumn
hwUserBridging = _HwUserBridging_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 16),
    _HwUserBridging_Type()
)
hwUserBridging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserBridging.setStatus("current")


class _HwDhcpSuppressSwitch_Type(Integer32):
    """Custom type hwDhcpSuppressSwitch based on Integer32"""
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


_HwDhcpSuppressSwitch_Type.__name__ = "Integer32"
_HwDhcpSuppressSwitch_Object = MibTableColumn
hwDhcpSuppressSwitch = _HwDhcpSuppressSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 17),
    _HwDhcpSuppressSwitch_Type()
)
hwDhcpSuppressSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDhcpSuppressSwitch.setStatus("current")


class _HwMismatchIgmpPolicy_Type(Integer32):
    """Custom type hwMismatchIgmpPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("transparent", 1))
    )


_HwMismatchIgmpPolicy_Type.__name__ = "Integer32"
_HwMismatchIgmpPolicy_Object = MibTableColumn
hwMismatchIgmpPolicy = _HwMismatchIgmpPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 18),
    _HwMismatchIgmpPolicy_Type()
)
hwMismatchIgmpPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMismatchIgmpPolicy.setStatus("current")


class _HwVmacStatus_Type(Integer32):
    """Custom type hwVmacStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notConfig", 3))
    )


_HwVmacStatus_Type.__name__ = "Integer32"
_HwVmacStatus_Object = MibTableColumn
hwVmacStatus = _HwVmacStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 19),
    _HwVmacStatus_Type()
)
hwVmacStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVmacStatus.setStatus("current")


class _HwIPoEMacMode_Type(Integer32):
    """Custom type hwIPoEMacMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multiMac", 1),
          ("singleMac", 2))
    )


_HwIPoEMacMode_Type.__name__ = "Integer32"
_HwIPoEMacMode_Object = MibTableColumn
hwIPoEMacMode = _HwIPoEMacMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 20),
    _HwIPoEMacMode_Type()
)
hwIPoEMacMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIPoEMacMode.setStatus("current")


class _HwVmacAgingMode_Type(Integer32):
    """Custom type hwVmacAgingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 2),
          ("macLearning", 1))
    )


_HwVmacAgingMode_Type.__name__ = "Integer32"
_HwVmacAgingMode_Object = MibTableColumn
hwVmacAgingMode = _HwVmacAgingMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 21),
    _HwVmacAgingMode_Type()
)
hwVmacAgingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVmacAgingMode.setStatus("current")


class _HwFabricMacLearningSwitch_Type(Integer32):
    """Custom type hwFabricMacLearningSwitch based on Integer32"""
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


_HwFabricMacLearningSwitch_Type.__name__ = "Integer32"
_HwFabricMacLearningSwitch_Object = MibTableColumn
hwFabricMacLearningSwitch = _HwFabricMacLearningSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 22),
    _HwFabricMacLearningSwitch_Type()
)
hwFabricMacLearningSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwFabricMacLearningSwitch.setStatus("current")


class _HwOspfTunnelSwitch_Type(Integer32):
    """Custom type hwOspfTunnelSwitch based on Integer32"""
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


_HwOspfTunnelSwitch_Type.__name__ = "Integer32"
_HwOspfTunnelSwitch_Object = MibTableColumn
hwOspfTunnelSwitch = _HwOspfTunnelSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 23),
    _HwOspfTunnelSwitch_Type()
)
hwOspfTunnelSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwOspfTunnelSwitch.setStatus("current")


class _HwL3ProtocolTunnelSwitch_Type(Integer32):
    """Custom type hwL3ProtocolTunnelSwitch based on Integer32"""
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


_HwL3ProtocolTunnelSwitch_Type.__name__ = "Integer32"
_HwL3ProtocolTunnelSwitch_Object = MibTableColumn
hwL3ProtocolTunnelSwitch = _HwL3ProtocolTunnelSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 24),
    _HwL3ProtocolTunnelSwitch_Type()
)
hwL3ProtocolTunnelSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL3ProtocolTunnelSwitch.setStatus("current")


class _HwDhcpv6Mode_Type(Integer32):
    """Custom type hwDhcpv6Mode based on Integer32"""
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
        *(("layer2", 2),
          ("layer3", 3),
          ("layer3option16", 4),
          ("notConfig", 1))
    )


_HwDhcpv6Mode_Type.__name__ = "Integer32"
_HwDhcpv6Mode_Object = MibTableColumn
hwDhcpv6Mode = _HwDhcpv6Mode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 25),
    _HwDhcpv6Mode_Type()
)
hwDhcpv6Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDhcpv6Mode.setStatus("current")


class _HwDhcpv6OptionSwitch_Type(Integer32):
    """Custom type hwDhcpv6OptionSwitch based on Integer32"""
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


_HwDhcpv6OptionSwitch_Type.__name__ = "Integer32"
_HwDhcpv6OptionSwitch_Object = MibTableColumn
hwDhcpv6OptionSwitch = _HwDhcpv6OptionSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 26),
    _HwDhcpv6OptionSwitch_Type()
)
hwDhcpv6OptionSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDhcpv6OptionSwitch.setStatus("current")


class _HwVmacIPoESubStatus_Type(Integer32):
    """Custom type hwVmacIPoESubStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notConfig", 3))
    )


_HwVmacIPoESubStatus_Type.__name__ = "Integer32"
_HwVmacIPoESubStatus_Object = MibTableColumn
hwVmacIPoESubStatus = _HwVmacIPoESubStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 27),
    _HwVmacIPoESubStatus_Type()
)
hwVmacIPoESubStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVmacIPoESubStatus.setStatus("current")


class _HwVmacPPPoESubStatus_Type(Integer32):
    """Custom type hwVmacPPPoESubStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notConfig", 3))
    )


_HwVmacPPPoESubStatus_Type.__name__ = "Integer32"
_HwVmacPPPoESubStatus_Object = MibTableColumn
hwVmacPPPoESubStatus = _HwVmacPPPoESubStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 28),
    _HwVmacPPPoESubStatus_Type()
)
hwVmacPPPoESubStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVmacPPPoESubStatus.setStatus("current")


class _HwVmacPPPoASubStatus_Type(Integer32):
    """Custom type hwVmacPPPoASubStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notConfig", 3))
    )


_HwVmacPPPoASubStatus_Type.__name__ = "Integer32"
_HwVmacPPPoASubStatus_Object = MibTableColumn
hwVmacPPPoASubStatus = _HwVmacPPPoASubStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 29),
    _HwVmacPPPoASubStatus_Type()
)
hwVmacPPPoASubStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVmacPPPoASubStatus.setStatus("current")


class _HwPPPoAMacMode_Type(Integer32):
    """Custom type hwPPPoAMacMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("multiMac", 1),
          ("notConfig", 3),
          ("singleMac", 2))
    )


_HwPPPoAMacMode_Type.__name__ = "Integer32"
_HwPPPoAMacMode_Object = MibTableColumn
hwPPPoAMacMode = _HwPPPoAMacMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 30),
    _HwPPPoAMacMode_Type()
)
hwPPPoAMacMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPPPoAMacMode.setStatus("current")


class _HwAntiIpv6SpoofingSwitch_Type(Integer32):
    """Custom type hwAntiIpv6SpoofingSwitch based on Integer32"""
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


_HwAntiIpv6SpoofingSwitch_Type.__name__ = "Integer32"
_HwAntiIpv6SpoofingSwitch_Object = MibTableColumn
hwAntiIpv6SpoofingSwitch = _HwAntiIpv6SpoofingSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 31),
    _HwAntiIpv6SpoofingSwitch_Type()
)
hwAntiIpv6SpoofingSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAntiIpv6SpoofingSwitch.setStatus("current")


class _HwIpv6DadProxySwitch_Type(Integer32):
    """Custom type hwIpv6DadProxySwitch based on Integer32"""
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


_HwIpv6DadProxySwitch_Type.__name__ = "Integer32"
_HwIpv6DadProxySwitch_Object = MibTableColumn
hwIpv6DadProxySwitch = _HwIpv6DadProxySwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 32),
    _HwIpv6DadProxySwitch_Type()
)
hwIpv6DadProxySwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpv6DadProxySwitch.setStatus("current")


class _HwIpv6BindRouteAndNdSwitch_Type(Integer32):
    """Custom type hwIpv6BindRouteAndNdSwitch based on Integer32"""
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


_HwIpv6BindRouteAndNdSwitch_Type.__name__ = "Integer32"
_HwIpv6BindRouteAndNdSwitch_Object = MibTableColumn
hwIpv6BindRouteAndNdSwitch = _HwIpv6BindRouteAndNdSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 33),
    _HwIpv6BindRouteAndNdSwitch_Type()
)
hwIpv6BindRouteAndNdSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpv6BindRouteAndNdSwitch.setStatus("current")


class _HwIpv6NsReplySwitch_Type(Integer32):
    """Custom type hwIpv6NsReplySwitch based on Integer32"""
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


_HwIpv6NsReplySwitch_Type.__name__ = "Integer32"
_HwIpv6NsReplySwitch_Object = MibTableColumn
hwIpv6NsReplySwitch = _HwIpv6NsReplySwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 34),
    _HwIpv6NsReplySwitch_Type()
)
hwIpv6NsReplySwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpv6NsReplySwitch.setStatus("current")


class _HwIpv4ArpReplySwitch_Type(Integer32):
    """Custom type hwIpv4ArpReplySwitch based on Integer32"""
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


_HwIpv4ArpReplySwitch_Type.__name__ = "Integer32"
_HwIpv4ArpReplySwitch_Object = MibTableColumn
hwIpv4ArpReplySwitch = _HwIpv4ArpReplySwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 35),
    _HwIpv4ArpReplySwitch_Type()
)
hwIpv4ArpReplySwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpv4ArpReplySwitch.setStatus("current")


class _HwDhcpRelayInterfaceRelayAgentSwitch_Type(Integer32):
    """Custom type hwDhcpRelayInterfaceRelayAgentSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notConfig", 3),
          ("receive", 1),
          ("send", 2))
    )


_HwDhcpRelayInterfaceRelayAgentSwitch_Type.__name__ = "Integer32"
_HwDhcpRelayInterfaceRelayAgentSwitch_Object = MibTableColumn
hwDhcpRelayInterfaceRelayAgentSwitch = _HwDhcpRelayInterfaceRelayAgentSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 36),
    _HwDhcpRelayInterfaceRelayAgentSwitch_Type()
)
hwDhcpRelayInterfaceRelayAgentSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDhcpRelayInterfaceRelayAgentSwitch.setStatus("current")


class _HwPolicyMulticastFabric_Type(Integer32):
    """Custom type hwPolicyMulticastFabric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1))
    )


_HwPolicyMulticastFabric_Type.__name__ = "Integer32"
_HwPolicyMulticastFabric_Object = MibTableColumn
hwPolicyMulticastFabric = _HwPolicyMulticastFabric_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 37),
    _HwPolicyMulticastFabric_Type()
)
hwPolicyMulticastFabric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPolicyMulticastFabric.setStatus("current")


class _HwCableSourceVerify_Type(Integer32):
    """Custom type hwCableSourceVerify based on Integer32"""
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


_HwCableSourceVerify_Type.__name__ = "Integer32"
_HwCableSourceVerify_Object = MibTableColumn
hwCableSourceVerify = _HwCableSourceVerify_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 38),
    _HwCableSourceVerify_Type()
)
hwCableSourceVerify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCableSourceVerify.setStatus("current")


class _HwRipngTunnelSwitch_Type(Integer32):
    """Custom type hwRipngTunnelSwitch based on Integer32"""
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


_HwRipngTunnelSwitch_Type.__name__ = "Integer32"
_HwRipngTunnelSwitch_Object = MibTableColumn
hwRipngTunnelSwitch = _HwRipngTunnelSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 39),
    _HwRipngTunnelSwitch_Type()
)
hwRipngTunnelSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRipngTunnelSwitch.setStatus("current")


class _HwIpv4ArpUnicastSwitch_Type(Integer32):
    """Custom type hwIpv4ArpUnicastSwitch based on Integer32"""
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


_HwIpv4ArpUnicastSwitch_Type.__name__ = "Integer32"
_HwIpv4ArpUnicastSwitch_Object = MibTableColumn
hwIpv4ArpUnicastSwitch = _HwIpv4ArpUnicastSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 40),
    _HwIpv4ArpUnicastSwitch_Type()
)
hwIpv4ArpUnicastSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpv4ArpUnicastSwitch.setStatus("current")


class _HwIpv4ArpUnicastunkonwnpolicy_Type(Integer32):
    """Custom type hwIpv4ArpUnicastunkonwnpolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1))
    )


_HwIpv4ArpUnicastunkonwnpolicy_Type.__name__ = "Integer32"
_HwIpv4ArpUnicastunkonwnpolicy_Object = MibTableColumn
hwIpv4ArpUnicastunkonwnpolicy = _HwIpv4ArpUnicastunkonwnpolicy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 41),
    _HwIpv4ArpUnicastunkonwnpolicy_Type()
)
hwIpv4ArpUnicastunkonwnpolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpv4ArpUnicastunkonwnpolicy.setStatus("current")


class _HwIpv6NsUnicastSwitch_Type(Integer32):
    """Custom type hwIpv6NsUnicastSwitch based on Integer32"""
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


_HwIpv6NsUnicastSwitch_Type.__name__ = "Integer32"
_HwIpv6NsUnicastSwitch_Object = MibTableColumn
hwIpv6NsUnicastSwitch = _HwIpv6NsUnicastSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 42),
    _HwIpv6NsUnicastSwitch_Type()
)
hwIpv6NsUnicastSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpv6NsUnicastSwitch.setStatus("current")


class _HwIpv6NsUnicastunkonwnpolicy_Type(Integer32):
    """Custom type hwIpv6NsUnicastunkonwnpolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1))
    )


_HwIpv6NsUnicastunkonwnpolicy_Type.__name__ = "Integer32"
_HwIpv6NsUnicastunkonwnpolicy_Object = MibTableColumn
hwIpv6NsUnicastunkonwnpolicy = _HwIpv6NsUnicastunkonwnpolicy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 43),
    _HwIpv6NsUnicastunkonwnpolicy_Type()
)
hwIpv6NsUnicastunkonwnpolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpv6NsUnicastunkonwnpolicy.setStatus("current")


class _HwIgmpUserMaxVlanTag_Type(Integer32):
    """Custom type hwIgmpUserMaxVlanTag based on Integer32"""
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
        *(("double", 4),
          ("single", 3),
          ("unaware", 1),
          ("untag", 2))
    )


_HwIgmpUserMaxVlanTag_Type.__name__ = "Integer32"
_HwIgmpUserMaxVlanTag_Object = MibTableColumn
hwIgmpUserMaxVlanTag = _HwIgmpUserMaxVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 44),
    _HwIgmpUserMaxVlanTag_Type()
)
hwIgmpUserMaxVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIgmpUserMaxVlanTag.setStatus("current")


class _HwRouterRedirectReverse_Type(Integer32):
    """Custom type hwRouterRedirectReverse based on Integer32"""
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


_HwRouterRedirectReverse_Type.__name__ = "Integer32"
_HwRouterRedirectReverse_Object = MibTableColumn
hwRouterRedirectReverse = _HwRouterRedirectReverse_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 45),
    _HwRouterRedirectReverse_Type()
)
hwRouterRedirectReverse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRouterRedirectReverse.setStatus("current")


class _HwCableIPv6SourceVerify_Type(Integer32):
    """Custom type hwCableIPv6SourceVerify based on Integer32"""
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


_HwCableIPv6SourceVerify_Type.__name__ = "Integer32"
_HwCableIPv6SourceVerify_Object = MibTableColumn
hwCableIPv6SourceVerify = _HwCableIPv6SourceVerify_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 46),
    _HwCableIPv6SourceVerify_Type()
)
hwCableIPv6SourceVerify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCableIPv6SourceVerify.setStatus("current")
_HwProfileRowStatus_Type = RowStatus
_HwProfileRowStatus_Object = MibTableColumn
hwProfileRowStatus = _HwProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 25, 1, 255),
    _HwProfileRowStatus_Type()
)
hwProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwProfileRowStatus.setStatus("current")


class _HwSmartVlanIsolateSwitch_Type(Integer32):
    """Custom type hwSmartVlanIsolateSwitch based on Integer32"""
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


_HwSmartVlanIsolateSwitch_Type.__name__ = "Integer32"
_HwSmartVlanIsolateSwitch_Object = MibScalar
hwSmartVlanIsolateSwitch = _HwSmartVlanIsolateSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 26),
    _HwSmartVlanIsolateSwitch_Type()
)
hwSmartVlanIsolateSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSmartVlanIsolateSwitch.setStatus("current")
_HwVlanIpAwareTable_Object = MibTable
hwVlanIpAwareTable = _HwVlanIpAwareTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 27)
)
if mibBuilder.loadTexts:
    hwVlanIpAwareTable.setStatus("current")
_HwVlanIpAwareEntry_Object = MibTableRow
hwVlanIpAwareEntry = _HwVlanIpAwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 27, 1)
)
hwVlanIpAwareEntry.setIndexNames(
    (0, "HUAWEI-VLAN-MIB", "hwVlanIpAwareVlanID"),
)
if mibBuilder.loadTexts:
    hwVlanIpAwareEntry.setStatus("current")
_HwVlanIpAwareVlanID_Type = Integer32
_HwVlanIpAwareVlanID_Object = MibTableColumn
hwVlanIpAwareVlanID = _HwVlanIpAwareVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 27, 1, 1),
    _HwVlanIpAwareVlanID_Type()
)
hwVlanIpAwareVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanIpAwareVlanID.setStatus("current")


class _HwVlanIpAwareVrfName_Type(OctetString):
    """Custom type hwVlanIpAwareVrfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwVlanIpAwareVrfName_Type.__name__ = "OctetString"
_HwVlanIpAwareVrfName_Object = MibTableColumn
hwVlanIpAwareVrfName = _HwVlanIpAwareVrfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 27, 1, 2),
    _HwVlanIpAwareVrfName_Type()
)
hwVlanIpAwareVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanIpAwareVrfName.setStatus("current")
_HwVlanIpAwareRowStatus_Type = RowStatus
_HwVlanIpAwareRowStatus_Object = MibTableColumn
hwVlanIpAwareRowStatus = _HwVlanIpAwareRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 27, 1, 3),
    _HwVlanIpAwareRowStatus_Type()
)
hwVlanIpAwareRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVlanIpAwareRowStatus.setStatus("current")


class _HwVlanIpAwareSrcIPMode_Type(Integer32):
    """Custom type hwVlanIpAwareSrcIPMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clientIp", 1),
          ("virtualIp", 2))
    )


_HwVlanIpAwareSrcIPMode_Type.__name__ = "Integer32"
_HwVlanIpAwareSrcIPMode_Object = MibTableColumn
hwVlanIpAwareSrcIPMode = _HwVlanIpAwareSrcIPMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 27, 1, 4),
    _HwVlanIpAwareSrcIPMode_Type()
)
hwVlanIpAwareSrcIPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanIpAwareSrcIPMode.setStatus("current")


class _HwVlanIpAwareArpSendPeriod_Type(Integer32):
    """Custom type hwVlanIpAwareArpSendPeriod based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_HwVlanIpAwareArpSendPeriod_Type.__name__ = "Integer32"
_HwVlanIpAwareArpSendPeriod_Object = MibTableColumn
hwVlanIpAwareArpSendPeriod = _HwVlanIpAwareArpSendPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 27, 1, 5),
    _HwVlanIpAwareArpSendPeriod_Type()
)
hwVlanIpAwareArpSendPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanIpAwareArpSendPeriod.setStatus("current")
_HwIpAwareVirtualIPTable_Object = MibTable
hwIpAwareVirtualIPTable = _HwIpAwareVirtualIPTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 28)
)
if mibBuilder.loadTexts:
    hwIpAwareVirtualIPTable.setStatus("current")
_HwIpAwareVirtualIPEntry_Object = MibTableRow
hwIpAwareVirtualIPEntry = _HwIpAwareVirtualIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 28, 1)
)
hwIpAwareVirtualIPEntry.setIndexNames(
    (0, "HUAWEI-VLAN-MIB", "hwIpAwareVirtualIPVlanID"),
    (0, "HUAWEI-VLAN-MIB", "hwIpAwareVirtualIP"),
    (0, "HUAWEI-VLAN-MIB", "hwIpAwareVirtualIPMask"),
)
if mibBuilder.loadTexts:
    hwIpAwareVirtualIPEntry.setStatus("current")
_HwIpAwareVirtualIPVlanID_Type = Integer32
_HwIpAwareVirtualIPVlanID_Object = MibTableColumn
hwIpAwareVirtualIPVlanID = _HwIpAwareVirtualIPVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 28, 1, 1),
    _HwIpAwareVirtualIPVlanID_Type()
)
hwIpAwareVirtualIPVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpAwareVirtualIPVlanID.setStatus("current")
_HwIpAwareVirtualIP_Type = IpAddress
_HwIpAwareVirtualIP_Object = MibTableColumn
hwIpAwareVirtualIP = _HwIpAwareVirtualIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 28, 1, 2),
    _HwIpAwareVirtualIP_Type()
)
hwIpAwareVirtualIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpAwareVirtualIP.setStatus("current")
_HwIpAwareVirtualIPMask_Type = IpAddress
_HwIpAwareVirtualIPMask_Object = MibTableColumn
hwIpAwareVirtualIPMask = _HwIpAwareVirtualIPMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 28, 1, 3),
    _HwIpAwareVirtualIPMask_Type()
)
hwIpAwareVirtualIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpAwareVirtualIPMask.setStatus("current")
_HwIpAwareVirtualIPRowStatus_Type = RowStatus
_HwIpAwareVirtualIPRowStatus_Object = MibTableColumn
hwIpAwareVirtualIPRowStatus = _HwIpAwareVirtualIPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 28, 1, 4),
    _HwIpAwareVirtualIPRowStatus_Type()
)
hwIpAwareVirtualIPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpAwareVirtualIPRowStatus.setStatus("current")
_HwIpAwareRouteTable_Object = MibTable
hwIpAwareRouteTable = _HwIpAwareRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 29)
)
if mibBuilder.loadTexts:
    hwIpAwareRouteTable.setStatus("current")
_HwIpAwareRouteEntry_Object = MibTableRow
hwIpAwareRouteEntry = _HwIpAwareRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 29, 1)
)
hwIpAwareRouteEntry.setIndexNames(
    (0, "HUAWEI-VLAN-MIB", "hwIpAwareRouteDstIP"),
    (0, "HUAWEI-VLAN-MIB", "hwIpAwareRouteMask"),
    (0, "HUAWEI-VLAN-MIB", "hwIpAwareRouteVlanID"),
)
if mibBuilder.loadTexts:
    hwIpAwareRouteEntry.setStatus("current")
_HwIpAwareRouteDstIP_Type = IpAddress
_HwIpAwareRouteDstIP_Object = MibTableColumn
hwIpAwareRouteDstIP = _HwIpAwareRouteDstIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 29, 1, 1),
    _HwIpAwareRouteDstIP_Type()
)
hwIpAwareRouteDstIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpAwareRouteDstIP.setStatus("current")
_HwIpAwareRouteMask_Type = IpAddress
_HwIpAwareRouteMask_Object = MibTableColumn
hwIpAwareRouteMask = _HwIpAwareRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 29, 1, 2),
    _HwIpAwareRouteMask_Type()
)
hwIpAwareRouteMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpAwareRouteMask.setStatus("current")
_HwIpAwareRouteVlanID_Type = Integer32
_HwIpAwareRouteVlanID_Object = MibTableColumn
hwIpAwareRouteVlanID = _HwIpAwareRouteVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 29, 1, 3),
    _HwIpAwareRouteVlanID_Type()
)
hwIpAwareRouteVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpAwareRouteVlanID.setStatus("current")
_HwIpAwareRouteNexthopIP_Type = IpAddress
_HwIpAwareRouteNexthopIP_Object = MibTableColumn
hwIpAwareRouteNexthopIP = _HwIpAwareRouteNexthopIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 29, 1, 4),
    _HwIpAwareRouteNexthopIP_Type()
)
hwIpAwareRouteNexthopIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpAwareRouteNexthopIP.setStatus("current")
_HwIpAwareRouteRowStatus_Type = RowStatus
_HwIpAwareRouteRowStatus_Object = MibTableColumn
hwIpAwareRouteRowStatus = _HwIpAwareRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 29, 1, 5),
    _HwIpAwareRouteRowStatus_Type()
)
hwIpAwareRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpAwareRouteRowStatus.setStatus("current")
_HwVlanInterfaceTrapsVbOids_ObjectIdentity = ObjectIdentity
hwVlanInterfaceTrapsVbOids = _HwVlanInterfaceTrapsVbOids_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 30)
)


class _HwL3InterfaceType_Type(Integer32):
    """Custom type hwL3InterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("meth", 2),
          ("vlanif", 1))
    )


_HwL3InterfaceType_Type.__name__ = "Integer32"
_HwL3InterfaceType_Object = MibScalar
hwL3InterfaceType = _HwL3InterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 30, 1),
    _HwL3InterfaceType_Type()
)
hwL3InterfaceType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwL3InterfaceType.setStatus("current")
_HwVlanifTraps_ObjectIdentity = ObjectIdentity
hwVlanifTraps = _HwVlanifTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 31)
)
_HwVlanifCommonTraps_ObjectIdentity = ObjectIdentity
hwVlanifCommonTraps = _HwVlanifCommonTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 31, 1)
)
_HwVlanifAlarmTraps_ObjectIdentity = ObjectIdentity
hwVlanifAlarmTraps = _HwVlanifAlarmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 31, 2)
)
_HwVlanifAlarmTrapsPrefix_ObjectIdentity = ObjectIdentity
hwVlanifAlarmTrapsPrefix = _HwVlanifAlarmTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 31, 2, 0)
)
_HwVlanCfgTrapsVbOids_ObjectIdentity = ObjectIdentity
hwVlanCfgTrapsVbOids = _HwVlanCfgTrapsVbOids_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 32)
)


class _HwVlanList_Type(OctetString):
    """Custom type hwVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_HwVlanList_Type.__name__ = "OctetString"
_HwVlanList_Object = MibScalar
hwVlanList = _HwVlanList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 32, 1),
    _HwVlanList_Type()
)
hwVlanList.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwVlanList.setStatus("current")


class _HwVlanSrvProfOperType_Type(Integer32):
    """Custom type hwVlanSrvProfOperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 3),
          ("modify", 2))
    )


_HwVlanSrvProfOperType_Type.__name__ = "Integer32"
_HwVlanSrvProfOperType_Object = MibScalar
hwVlanSrvProfOperType = _HwVlanSrvProfOperType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 32, 2),
    _HwVlanSrvProfOperType_Type()
)
hwVlanSrvProfOperType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwVlanSrvProfOperType.setStatus("current")


class _HwVlanListType_Type(Integer32):
    """Custom type hwVlanListType based on Integer32"""
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
        *(("commonVlan", 2),
          ("multiVlan", 9),
          ("muxVlan", 8),
          ("primaryVlan", 4),
          ("regionVlan", 6),
          ("secondaryVlan", 5),
          ("smartVlan", 7),
          ("subVlan", 3),
          ("superVlan", 1))
    )


_HwVlanListType_Type.__name__ = "Integer32"
_HwVlanListType_Object = MibScalar
hwVlanListType = _HwVlanListType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 32, 3),
    _HwVlanListType_Type()
)
hwVlanListType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwVlanListType.setStatus("current")


class _HwVlanListAttrib_Type(Integer32):
    """Custom type hwVlanListAttrib based on Integer32"""
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
        *(("common", 1),
          ("qinq", 2),
          ("stacking", 3),
          ("subVlan", 4))
    )


_HwVlanListAttrib_Type.__name__ = "Integer32"
_HwVlanListAttrib_Object = MibScalar
hwVlanListAttrib = _HwVlanListAttrib_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 32, 4),
    _HwVlanListAttrib_Type()
)
hwVlanListAttrib.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwVlanListAttrib.setStatus("current")
_HwVlanCfgTraps_ObjectIdentity = ObjectIdentity
hwVlanCfgTraps = _HwVlanCfgTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 33)
)
_HwVlanCfgCommonTraps_ObjectIdentity = ObjectIdentity
hwVlanCfgCommonTraps = _HwVlanCfgCommonTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 33, 1)
)
_HwVlanCfgCommonTrapsPrefix_ObjectIdentity = ObjectIdentity
hwVlanCfgCommonTrapsPrefix = _HwVlanCfgCommonTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 33, 1, 0)
)
_HwVOIPDhcpQosTable_Object = MibTable
hwVOIPDhcpQosTable = _HwVOIPDhcpQosTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 35)
)
if mibBuilder.loadTexts:
    hwVOIPDhcpQosTable.setStatus("current")
_HwVOIPDhcpQosEntry_Object = MibTableRow
hwVOIPDhcpQosEntry = _HwVOIPDhcpQosEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 35, 1)
)
hwVOIPDhcpQosEntry.setIndexNames(
    (0, "HUAWEI-VLAN-MIB", "hwVOIPDhcpVlanID"),
    (0, "HUAWEI-VLAN-MIB", "hwVOIPDhcpQosType"),
)
if mibBuilder.loadTexts:
    hwVOIPDhcpQosEntry.setStatus("current")


class _HwVOIPDhcpVlanID_Type(Integer32):
    """Custom type hwVOIPDhcpVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_HwVOIPDhcpVlanID_Type.__name__ = "Integer32"
_HwVOIPDhcpVlanID_Object = MibTableColumn
hwVOIPDhcpVlanID = _HwVOIPDhcpVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 35, 1, 1),
    _HwVOIPDhcpVlanID_Type()
)
hwVOIPDhcpVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVOIPDhcpVlanID.setStatus("current")


class _HwVOIPDhcpQosType_Type(Integer32):
    """Custom type hwVOIPDhcpQosType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwVOIPDhcpQosType_Type.__name__ = "Integer32"
_HwVOIPDhcpQosType_Object = MibTableColumn
hwVOIPDhcpQosType = _HwVOIPDhcpQosType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 35, 1, 2),
    _HwVOIPDhcpQosType_Type()
)
hwVOIPDhcpQosType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVOIPDhcpQosType.setStatus("current")


class _HwVOIPDhcpQosIPTos_Type(Integer32):
    """Custom type hwVOIPDhcpQosIPTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_HwVOIPDhcpQosIPTos_Type.__name__ = "Integer32"
_HwVOIPDhcpQosIPTos_Object = MibTableColumn
hwVOIPDhcpQosIPTos = _HwVOIPDhcpQosIPTos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 35, 1, 3),
    _HwVOIPDhcpQosIPTos_Type()
)
hwVOIPDhcpQosIPTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVOIPDhcpQosIPTos.setStatus("current")


class _HwVOIPDhcpQosIPDscp_Type(Integer32):
    """Custom type hwVOIPDhcpQosIPDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_HwVOIPDhcpQosIPDscp_Type.__name__ = "Integer32"
_HwVOIPDhcpQosIPDscp_Object = MibTableColumn
hwVOIPDhcpQosIPDscp = _HwVOIPDhcpQosIPDscp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 35, 1, 4),
    _HwVOIPDhcpQosIPDscp_Type()
)
hwVOIPDhcpQosIPDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVOIPDhcpQosIPDscp.setStatus("current")


class _HwVOIPDhcpQosVlanPriority_Type(Integer32):
    """Custom type hwVOIPDhcpQosVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwVOIPDhcpQosVlanPriority_Type.__name__ = "Integer32"
_HwVOIPDhcpQosVlanPriority_Object = MibTableColumn
hwVOIPDhcpQosVlanPriority = _HwVOIPDhcpQosVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 35, 1, 5),
    _HwVOIPDhcpQosVlanPriority_Type()
)
hwVOIPDhcpQosVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVOIPDhcpQosVlanPriority.setStatus("current")
_HwVOIPDhcpQosRowStatus_Type = RowStatus
_HwVOIPDhcpQosRowStatus_Object = MibTableColumn
hwVOIPDhcpQosRowStatus = _HwVOIPDhcpQosRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 35, 1, 6),
    _HwVOIPDhcpQosRowStatus_Type()
)
hwVOIPDhcpQosRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVOIPDhcpQosRowStatus.setStatus("current")


class _HwStackingVlanOuterEthernetType_Type(Unsigned32):
    """Custom type hwStackingVlanOuterEthernetType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_HwStackingVlanOuterEthernetType_Type.__name__ = "Unsigned32"
_HwStackingVlanOuterEthernetType_Object = MibScalar
hwStackingVlanOuterEthernetType = _HwStackingVlanOuterEthernetType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 65000),
    _HwStackingVlanOuterEthernetType_Type()
)
hwStackingVlanOuterEthernetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStackingVlanOuterEthernetType.setStatus("current")


class _HwDot1adTpid_Type(Unsigned32):
    """Custom type hwDot1adTpid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_HwDot1adTpid_Type.__name__ = "Unsigned32"
_HwDot1adTpid_Object = MibScalar
hwDot1adTpid = _HwDot1adTpid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 65001),
    _HwDot1adTpid_Type()
)
hwDot1adTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot1adTpid.setStatus("current")
_HwPortOuterEthernetTypeTable_Object = MibTable
hwPortOuterEthernetTypeTable = _HwPortOuterEthernetTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 65002)
)
if mibBuilder.loadTexts:
    hwPortOuterEthernetTypeTable.setStatus("current")
_HwPortOuterEthernetTypeEntry_Object = MibTableRow
hwPortOuterEthernetTypeEntry = _HwPortOuterEthernetTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 65002, 1)
)
hwPortOuterEthernetTypeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hwPortOuterEthernetTypeEntry.setStatus("current")


class _HwPortOuterEthernetType_Type(Integer32):
    """Custom type hwPortOuterEthernetType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot1adTpid", 2),
          ("dot1qTpid", 1),
          ("invalid", -1))
    )


_HwPortOuterEthernetType_Type.__name__ = "Integer32"
_HwPortOuterEthernetType_Object = MibTableColumn
hwPortOuterEthernetType = _HwPortOuterEthernetType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 65002, 1, 1),
    _HwPortOuterEthernetType_Type()
)
hwPortOuterEthernetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortOuterEthernetType.setStatus("current")


class _HwVlanLocalSwitch_Type(Integer32):
    """Custom type hwVlanLocalSwitch based on Integer32"""
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


_HwVlanLocalSwitch_Type.__name__ = "Integer32"
_HwVlanLocalSwitch_Object = MibScalar
hwVlanLocalSwitch = _HwVlanLocalSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 65003),
    _HwVlanLocalSwitch_Type()
)
hwVlanLocalSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanLocalSwitch.setStatus("current")
_HwLocalVlanTable_Object = MibTable
hwLocalVlanTable = _HwLocalVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 65004)
)
if mibBuilder.loadTexts:
    hwLocalVlanTable.setStatus("current")
_HwLocalVlanEntry_Object = MibTableRow
hwLocalVlanEntry = _HwLocalVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 65004, 1)
)
hwLocalVlanEntry.setIndexNames(
    (0, "HUAWEI-VLAN-MIB", "hwVlanIndex"),
)
if mibBuilder.loadTexts:
    hwLocalVlanEntry.setStatus("current")


class _HwLocalVlan_Type(Integer32):
    """Custom type hwLocalVlan based on Integer32"""
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


_HwLocalVlan_Type.__name__ = "Integer32"
_HwLocalVlan_Object = MibTableColumn
hwLocalVlan = _HwLocalVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 65004, 1, 1),
    _HwLocalVlan_Type()
)
hwLocalVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLocalVlan.setStatus("current")
_HwVlanTrafficOccupiedTable_Object = MibTable
hwVlanTrafficOccupiedTable = _HwVlanTrafficOccupiedTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 65005)
)
if mibBuilder.loadTexts:
    hwVlanTrafficOccupiedTable.setStatus("current")
_HwVlanTrafficOccupiedEntry_Object = MibTableRow
hwVlanTrafficOccupiedEntry = _HwVlanTrafficOccupiedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 65005, 1)
)
hwVlanTrafficOccupiedEntry.setIndexNames(
    (0, "HUAWEI-VLAN-MIB", "hwVlanIndex"),
    (0, "HUAWEI-VLAN-MIB", "hwInnerVlanID"),
)
if mibBuilder.loadTexts:
    hwVlanTrafficOccupiedEntry.setStatus("current")
_HwVlanUplinkTraffic_Type = Unsigned32
_HwVlanUplinkTraffic_Object = MibTableColumn
hwVlanUplinkTraffic = _HwVlanUplinkTraffic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 65005, 1, 1),
    _HwVlanUplinkTraffic_Type()
)
hwVlanUplinkTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanUplinkTraffic.setStatus("current")
_HwVlanDownTraffic_Type = Unsigned32
_HwVlanDownTraffic_Object = MibTableColumn
hwVlanDownTraffic = _HwVlanDownTraffic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 65005, 1, 2),
    _HwVlanDownTraffic_Type()
)
hwVlanDownTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanDownTraffic.setStatus("current")
_HwVlanUplinkBandwidthOccupancyRate_Type = Unsigned32
_HwVlanUplinkBandwidthOccupancyRate_Object = MibTableColumn
hwVlanUplinkBandwidthOccupancyRate = _HwVlanUplinkBandwidthOccupancyRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 65005, 1, 3),
    _HwVlanUplinkBandwidthOccupancyRate_Type()
)
hwVlanUplinkBandwidthOccupancyRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanUplinkBandwidthOccupancyRate.setStatus("current")
_HwVlanDownBandwidthOccupancyRate_Type = Unsigned32
_HwVlanDownBandwidthOccupancyRate_Object = MibTableColumn
hwVlanDownBandwidthOccupancyRate = _HwVlanDownBandwidthOccupancyRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 65005, 1, 4),
    _HwVlanDownBandwidthOccupancyRate_Type()
)
hwVlanDownBandwidthOccupancyRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanDownBandwidthOccupancyRate.setStatus("current")
_HwMplsVlanTable_Object = MibTable
hwMplsVlanTable = _HwMplsVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 65006)
)
if mibBuilder.loadTexts:
    hwMplsVlanTable.setStatus("current")
_HwMplsVlanEntry_Object = MibTableRow
hwMplsVlanEntry = _HwMplsVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 65006, 1)
)
hwMplsVlanEntry.setIndexNames(
    (0, "HUAWEI-VLAN-MIB", "hwVlanIndex"),
)
if mibBuilder.loadTexts:
    hwMplsVlanEntry.setStatus("current")


class _HwMplsVlanEnable_Type(Integer32):
    """Custom type hwMplsVlanEnable based on Integer32"""
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


_HwMplsVlanEnable_Type.__name__ = "Integer32"
_HwMplsVlanEnable_Object = MibTableColumn
hwMplsVlanEnable = _HwMplsVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 65006, 1, 1),
    _HwMplsVlanEnable_Type()
)
hwMplsVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsVlanEnable.setStatus("current")
_HwVlanConnectTable_Object = MibTable
hwVlanConnectTable = _HwVlanConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 65007)
)
if mibBuilder.loadTexts:
    hwVlanConnectTable.setStatus("current")
_HwVlanConnectEntry_Object = MibTableRow
hwVlanConnectEntry = _HwVlanConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 65007, 1)
)
hwVlanConnectEntry.setIndexNames(
    (0, "HUAWEI-VLAN-MIB", "hwVlanConnectOuterVlanID"),
    (0, "HUAWEI-VLAN-MIB", "hwVlanConnectInnerVlanID"),
)
if mibBuilder.loadTexts:
    hwVlanConnectEntry.setStatus("current")


class _HwVlanConnectOuterVlanID_Type(Integer32):
    """Custom type hwVlanConnectOuterVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 4095),
    )


_HwVlanConnectOuterVlanID_Type.__name__ = "Integer32"
_HwVlanConnectOuterVlanID_Object = MibTableColumn
hwVlanConnectOuterVlanID = _HwVlanConnectOuterVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 65007, 1, 1),
    _HwVlanConnectOuterVlanID_Type()
)
hwVlanConnectOuterVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVlanConnectOuterVlanID.setStatus("current")


class _HwVlanConnectInnerVlanID_Type(Integer32):
    """Custom type hwVlanConnectInnerVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 4095),
    )


_HwVlanConnectInnerVlanID_Type.__name__ = "Integer32"
_HwVlanConnectInnerVlanID_Object = MibTableColumn
hwVlanConnectInnerVlanID = _HwVlanConnectInnerVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 65007, 1, 2),
    _HwVlanConnectInnerVlanID_Type()
)
hwVlanConnectInnerVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVlanConnectInnerVlanID.setStatus("current")


class _HwVlanConnectSrcType_Type(Integer32):
    """Custom type hwVlanConnectSrcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", -1),
          ("port", 1))
    )


_HwVlanConnectSrcType_Type.__name__ = "Integer32"
_HwVlanConnectSrcType_Object = MibTableColumn
hwVlanConnectSrcType = _HwVlanConnectSrcType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 65007, 1, 3),
    _HwVlanConnectSrcType_Type()
)
hwVlanConnectSrcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanConnectSrcType.setStatus("current")
_HwVlanConnectSrcPara_Type = Integer32
_HwVlanConnectSrcPara_Object = MibTableColumn
hwVlanConnectSrcPara = _HwVlanConnectSrcPara_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 65007, 1, 4),
    _HwVlanConnectSrcPara_Type()
)
hwVlanConnectSrcPara.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanConnectSrcPara.setStatus("current")


class _HwVlanConnectDstType_Type(Integer32):
    """Custom type hwVlanConnectDstType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bundle", 3),
          ("flow", 2),
          ("invalid", -1),
          ("port", 1))
    )


_HwVlanConnectDstType_Type.__name__ = "Integer32"
_HwVlanConnectDstType_Object = MibTableColumn
hwVlanConnectDstType = _HwVlanConnectDstType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 65007, 1, 5),
    _HwVlanConnectDstType_Type()
)
hwVlanConnectDstType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanConnectDstType.setStatus("current")
_HwVlanConnectDstPara_Type = Integer32
_HwVlanConnectDstPara_Object = MibTableColumn
hwVlanConnectDstPara = _HwVlanConnectDstPara_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 65007, 1, 6),
    _HwVlanConnectDstPara_Type()
)
hwVlanConnectDstPara.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanConnectDstPara.setStatus("current")
_HwVlanConnectRowStatus_Type = RowStatus
_HwVlanConnectRowStatus_Object = MibTableColumn
hwVlanConnectRowStatus = _HwVlanConnectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 65007, 1, 255),
    _HwVlanConnectRowStatus_Type()
)
hwVlanConnectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVlanConnectRowStatus.setStatus("current")
_HwDoubleTagTunnelConfig_ObjectIdentity = ObjectIdentity
hwDoubleTagTunnelConfig = _HwDoubleTagTunnelConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 65008)
)


class _HwDoubleTagTunnelIgmp_Type(Integer32):
    """Custom type hwDoubleTagTunnelIgmp based on Integer32"""
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


_HwDoubleTagTunnelIgmp_Type.__name__ = "Integer32"
_HwDoubleTagTunnelIgmp_Object = MibScalar
hwDoubleTagTunnelIgmp = _HwDoubleTagTunnelIgmp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 65008, 1),
    _HwDoubleTagTunnelIgmp_Type()
)
hwDoubleTagTunnelIgmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDoubleTagTunnelIgmp.setStatus("current")


class _HwDoubleTagTunnelRip_Type(Integer32):
    """Custom type hwDoubleTagTunnelRip based on Integer32"""
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


_HwDoubleTagTunnelRip_Type.__name__ = "Integer32"
_HwDoubleTagTunnelRip_Object = MibScalar
hwDoubleTagTunnelRip = _HwDoubleTagTunnelRip_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 65008, 2),
    _HwDoubleTagTunnelRip_Type()
)
hwDoubleTagTunnelRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDoubleTagTunnelRip.setStatus("current")


class _HwDoubleTagTunnelDhcp_Type(Integer32):
    """Custom type hwDoubleTagTunnelDhcp based on Integer32"""
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


_HwDoubleTagTunnelDhcp_Type.__name__ = "Integer32"
_HwDoubleTagTunnelDhcp_Object = MibScalar
hwDoubleTagTunnelDhcp = _HwDoubleTagTunnelDhcp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 65008, 3),
    _HwDoubleTagTunnelDhcp_Type()
)
hwDoubleTagTunnelDhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDoubleTagTunnelDhcp.setStatus("current")
_HwDocsSrvVlanIDTable_Object = MibTable
hwDocsSrvVlanIDTable = _HwDocsSrvVlanIDTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 65009)
)
if mibBuilder.loadTexts:
    hwDocsSrvVlanIDTable.setStatus("current")
_HwDocsSrvVlanIDEntry_Object = MibTableRow
hwDocsSrvVlanIDEntry = _HwDocsSrvVlanIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 65009, 1)
)
hwDocsSrvVlanIDEntry.setIndexNames(
    (0, "HUAWEI-DEVICE-MIB", "hwFrameIndex"),
    (0, "HUAWEI-DEVICE-MIB", "hwSlotIndex"),
)
if mibBuilder.loadTexts:
    hwDocsSrvVlanIDEntry.setStatus("current")


class _HwDocsSrvVlanID_Type(Integer32):
    """Custom type hwDocsSrvVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 4093),
    )


_HwDocsSrvVlanID_Type.__name__ = "Integer32"
_HwDocsSrvVlanID_Object = MibTableColumn
hwDocsSrvVlanID = _HwDocsSrvVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 65009, 1, 1),
    _HwDocsSrvVlanID_Type()
)
hwDocsSrvVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDocsSrvVlanID.setStatus("current")
_HwDocsSrvVlanRowStatus_Type = RowStatus
_HwDocsSrvVlanRowStatus_Object = MibTableColumn
hwDocsSrvVlanRowStatus = _HwDocsSrvVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 65009, 1, 2),
    _HwDocsSrvVlanRowStatus_Type()
)
hwDocsSrvVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDocsSrvVlanRowStatus.setStatus("current")


class _HwMethNativeVlan_Type(Integer32):
    """Custom type hwMethNativeVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(2, 4093),
    )


_HwMethNativeVlan_Type.__name__ = "Integer32"
_HwMethNativeVlan_Object = MibScalar
hwMethNativeVlan = _HwMethNativeVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 65010),
    _HwMethNativeVlan_Type()
)
hwMethNativeVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMethNativeVlan.setStatus("current")

# Managed Objects groups


# Notification objects

hwVlanifUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 31, 2, 0, 1)
)
hwVlanifUpTrap.setObjects(
      *(("HUAWEI-VLAN-MIB", "hwL3InterfaceType"),
        ("HUAWEI-VLAN-MIB", "hwVlanID"))
)
if mibBuilder.loadTexts:
    hwVlanifUpTrap.setStatus(
        "current"
    )

hwVlanifDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 31, 2, 0, 2)
)
hwVlanifDownTrap.setObjects(
      *(("HUAWEI-VLAN-MIB", "hwL3InterfaceType"),
        ("HUAWEI-VLAN-MIB", "hwVlanID"))
)
if mibBuilder.loadTexts:
    hwVlanifDownTrap.setStatus(
        "current"
    )

hwVlanNameChangeInfoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 33, 1, 0, 1)
)
hwVlanNameChangeInfoTrap.setObjects(
      *(("HUAWEI-DEVICE-MIB", "hwConfigChangeIP"),
        ("HUAWEI-VLAN-MIB", "hwVlanIndex"),
        ("HUAWEI-VLAN-MIB", "hwVlanName"))
)
if mibBuilder.loadTexts:
    hwVlanNameChangeInfoTrap.setStatus(
        "current"
    )

hwVlanForwardingModeInfoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 33, 1, 0, 2)
)
hwVlanForwardingModeInfoTrap.setObjects(
      *(("HUAWEI-DEVICE-MIB", "hwConfigChangeIP"),
        ("HUAWEI-VLAN-MIB", "hwVlanIndex"),
        ("HUAWEI-VLAN-MIB", "hwVlanForwarding"))
)
if mibBuilder.loadTexts:
    hwVlanForwardingModeInfoTrap.setStatus(
        "current"
    )

hwVlanSrvProfChageInfoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 33, 1, 0, 3)
)
hwVlanSrvProfChageInfoTrap.setObjects(
      *(("HUAWEI-DEVICE-MIB", "hwConfigChangeIP"),
        ("HUAWEI-VLAN-MIB", "hwVlanSrvProfName"),
        ("HUAWEI-VLAN-MIB", "hwVlanSrvProfOperType"))
)
if mibBuilder.loadTexts:
    hwVlanSrvProfChageInfoTrap.setStatus(
        "current"
    )

hwVlanAndVlanSrvProfOperInfoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 33, 1, 0, 4)
)
hwVlanAndVlanSrvProfOperInfoTrap.setObjects(
      *(("HUAWEI-DEVICE-MIB", "hwConfigChangeIP"),
        ("HUAWEI-VLAN-MIB", "hwVlanList"),
        ("HUAWEI-VLAN-MIB", "hwVlanSrvProfName"))
)
if mibBuilder.loadTexts:
    hwVlanAndVlanSrvProfOperInfoTrap.setStatus(
        "current"
    )

hwVlanAddInfoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 33, 1, 0, 5)
)
hwVlanAddInfoTrap.setObjects(
      *(("HUAWEI-DEVICE-MIB", "hwConfigChangeIP"),
        ("HUAWEI-VLAN-MIB", "hwVlanList"),
        ("HUAWEI-VLAN-MIB", "hwVlanListType"),
        ("HUAWEI-VLAN-MIB", "hwVlanListAttrib"))
)
if mibBuilder.loadTexts:
    hwVlanAddInfoTrap.setStatus(
        "current"
    )

hwVlanDelInfoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 33, 1, 0, 6)
)
hwVlanDelInfoTrap.setObjects(
      *(("HUAWEI-DEVICE-MIB", "hwConfigChangeIP"),
        ("HUAWEI-VLAN-MIB", "hwVlanList"))
)
if mibBuilder.loadTexts:
    hwVlanDelInfoTrap.setStatus(
        "current"
    )

hwVlanAttrChangedInfoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 33, 1, 0, 7)
)
hwVlanAttrChangedInfoTrap.setObjects(
      *(("HUAWEI-DEVICE-MIB", "hwConfigChangeIP"),
        ("HUAWEI-VLAN-MIB", "hwVlanList"),
        ("HUAWEI-VLAN-MIB", "hwVlanListAttrib"))
)
if mibBuilder.loadTexts:
    hwVlanAttrChangedInfoTrap.setStatus(
        "current"
    )

hwPortVlanChangedInfoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 6, 1, 33, 1, 0, 8)
)
hwPortVlanChangedInfoTrap.setObjects(
      *(("HUAWEI-DEVICE-MIB", "hwConfigChangeIP"),
        ("HUAWEI-VLAN-MIB", "hwVlanList"))
)
if mibBuilder.loadTexts:
    hwPortVlanChangedInfoTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-VLAN-MIB",
    **{"VlanIndex": VlanIndex,
       "SnmpAdminString": SnmpAdminString,
       "PortList": PortList,
       "hwVlan": hwVlan,
       "hwVlanMngObject": hwVlanMngObject,
       "hwVlanMIBTable": hwVlanMIBTable,
       "hwVlanMIBEntry": hwVlanMIBEntry,
       "hwVlanIndex": hwVlanIndex,
       "hwVlanName": hwVlanName,
       "hwVlanPorts": hwVlanPorts,
       "hwVlanType": hwVlanType,
       "hwVlanMacFilter": hwVlanMacFilter,
       "hwVlanMcastUnknownProtos": hwVlanMcastUnknownProtos,
       "hwExistInterface": hwExistInterface,
       "hwVlanInterfaceIndex": hwVlanInterfaceIndex,
       "hwVlanMacLearn": hwVlanMacLearn,
       "hwVlanStatus": hwVlanStatus,
       "hwVlanCreationTime": hwVlanCreationTime,
       "hwVlanPriority": hwVlanPriority,
       "hwVlanRowStatus": hwVlanRowStatus,
       "hwVlanAttrib": hwVlanAttrib,
       "hwVlanSuperID": hwVlanSuperID,
       "hwVlanForwarding": hwVlanForwarding,
       "hwVlanPolicyBroadcast": hwVlanPolicyBroadcast,
       "hwVlanPolicyMulticast": hwVlanPolicyMulticast,
       "hwVlanPolicyUnknowncast": hwVlanPolicyUnknowncast,
       "hwVlanOuterTpid": hwVlanOuterTpid,
       "hwVlanBindSrvProfName": hwVlanBindSrvProfName,
       "hwVlanChangeEnable": hwVlanChangeEnable,
       "hwVlanBindRaioProfileName": hwVlanBindRaioProfileName,
       "hwVlanTrafficSuppressUnknowncastNetwork": hwVlanTrafficSuppressUnknowncastNetwork,
       "hwVlanMethL2Forward": hwVlanMethL2Forward,
       "hwVlanInterfaceTable": hwVlanInterfaceTable,
       "hwVlanInterfaceEntry": hwVlanInterfaceEntry,
       "hwVlanInterfaceID": hwVlanInterfaceID,
       "hwVlanID": hwVlanID,
       "hwVlanIpAddress": hwVlanIpAddress,
       "hwVlanIpAddressMask": hwVlanIpAddressMask,
       "hwVlanInterfaceAdminStatus": hwVlanInterfaceAdminStatus,
       "hwVlanInterfaceFrameType": hwVlanInterfaceFrameType,
       "hwInterfaceRowStatus": hwInterfaceRowStatus,
       "hwVlanInterfaceLinkStatus": hwVlanInterfaceLinkStatus,
       "hwVlanIfIPMode": hwVlanIfIPMode,
       "hwVlanIfDhcpClientOption60": hwVlanIfDhcpClientOption60,
       "hwVlanIfVlanEncapMode": hwVlanIfVlanEncapMode,
       "hwVlanIfVlanInnerLabel": hwVlanIfVlanInnerLabel,
       "hwVlanIfDHCPSStatus": hwVlanIfDHCPSStatus,
       "hwIPv6MTU": hwIPv6MTU,
       "hwIPv4MTU": hwIPv4MTU,
       "hwifSVLANVlanListTable": hwifSVLANVlanListTable,
       "hwifSVLANVlanListEntry": hwifSVLANVlanListEntry,
       "hwifSvlanVlanID": hwifSvlanVlanID,
       "hwifSvlanSubVlanlistLow": hwifSvlanSubVlanlistLow,
       "hwifSvlanSubVlanlisHigh": hwifSvlanSubVlanlisHigh,
       "hwifSvlanOperStatus": hwifSvlanOperStatus,
       "hwifPVLANMappingTable": hwifPVLANMappingTable,
       "hwifPVLANMappingEntry": hwifPVLANMappingEntry,
       "hwifPvlanPrimaryVlanID": hwifPvlanPrimaryVlanID,
       "hwifPvlanSecondaryVlanlistLow": hwifPvlanSecondaryVlanlistLow,
       "hwifPvlanSecondaryVlanlistHigh": hwifPvlanSecondaryVlanlistHigh,
       "hwifPvlanOperStatus": hwifPvlanOperStatus,
       "hwRegionVLanTable": hwRegionVLanTable,
       "hwRegionVLanEntry": hwRegionVLanEntry,
       "hwRegionVpi": hwRegionVpi,
       "hwRegionVci": hwRegionVci,
       "hwRegionPVCRowStatus": hwRegionPVCRowStatus,
       "hwSmartVLanTable": hwSmartVLanTable,
       "hwSmartVLanEntry": hwSmartVLanEntry,
       "hwSmartVlanID": hwSmartVlanID,
       "hwSmartVlanUplinkPort": hwSmartVlanUplinkPort,
       "hwSmartVlanDownlinkPort": hwSmartVlanDownlinkPort,
       "hwSmartVlanRowStatus": hwSmartVlanRowStatus,
       "hwMuxVlanEnable": hwMuxVlanEnable,
       "hwMuxVlanPortConfTable": hwMuxVlanPortConfTable,
       "hwMuxVlanPortConfEntry": hwMuxVlanPortConfEntry,
       "hwMuxVlanPortType": hwMuxVlanPortType,
       "hwMuxVlanStartVlanId": hwMuxVlanStartVlanId,
       "hwMuxVlanGroupNum": hwMuxVlanGroupNum,
       "hwMuxVlanPortConfRowStatus": hwMuxVlanPortConfRowStatus,
       "hwMuxVlanUplinkPort": hwMuxVlanUplinkPort,
       "hwMuxVlanDownlinkPort": hwMuxVlanDownlinkPort,
       "hwMuxVlanSlotConfTable": hwMuxVlanSlotConfTable,
       "hwMuxVlanSlotConfEntry": hwMuxVlanSlotConfEntry,
       "hwMuxVlanSlotStartVlanId": hwMuxVlanSlotStartVlanId,
       "hwMuxVlanSlotRowStatus": hwMuxVlanSlotRowStatus,
       "hwMultiVLanTable": hwMultiVLanTable,
       "hwMultiVLanEntry": hwMultiVLanEntry,
       "hwMultiVlanID": hwMultiVlanID,
       "hwMultiVlanUplinkPort": hwMultiVlanUplinkPort,
       "hwMultiVlanDownlinkPort": hwMultiVlanDownlinkPort,
       "hwMultiVlanRowStatus": hwMultiVlanRowStatus,
       "hwVlanAggregationTable": hwVlanAggregationTable,
       "hwVlanAggregationEntry": hwVlanAggregationEntry,
       "hwVlanAggregationSuperVlanId": hwVlanAggregationSuperVlanId,
       "hwVlanAggregationSubVlanId": hwVlanAggregationSubVlanId,
       "hwVlanAggregationSubVlanArpProxyStatus": hwVlanAggregationSubVlanArpProxyStatus,
       "hwVlanAggregationRowStatus": hwVlanAggregationRowStatus,
       "hwVlanAggregationSubVlanNdProxyStatus": hwVlanAggregationSubVlanNdProxyStatus,
       "hwStackingVlanInnerEthernetType": hwStackingVlanInnerEthernetType,
       "hwVlanFlowAccountTable": hwVlanFlowAccountTable,
       "hwVlanFlowAccountEntry": hwVlanFlowAccountEntry,
       "hwInnerVlanID": hwInnerVlanID,
       "hwUpFlowAccountByte": hwUpFlowAccountByte,
       "hwDownFlowAccountByte": hwDownFlowAccountByte,
       "hwUpFlowAccountPacket": hwUpFlowAccountPacket,
       "hwDownFlowAccountPacket": hwDownFlowAccountPacket,
       "hwUpStreamPacket": hwUpStreamPacket,
       "hwDownStreamPacket": hwDownStreamPacket,
       "hwFlowAccountAdminStatus": hwFlowAccountAdminStatus,
       "hwUpFlowAccountDiscardPacket": hwUpFlowAccountDiscardPacket,
       "hwDownFlowAccountDiscardPacket": hwDownFlowAccountDiscardPacket,
       "hwVlanUpCarTable": hwVlanUpCarTable,
       "hwVlanUpCarEntry": hwVlanUpCarEntry,
       "hwVlanUpCarId": hwVlanUpCarId,
       "hwVlanUpCarName": hwVlanUpCarName,
       "hwVlanUpCarBandValue": hwVlanUpCarBandValue,
       "hwVlanUpCarBurstValue": hwVlanUpCarBurstValue,
       "hwVlanUpCarIsUsed": hwVlanUpCarIsUsed,
       "hwVlanUpCarRowStatus": hwVlanUpCarRowStatus,
       "hwVlanDownCarTable": hwVlanDownCarTable,
       "hwVlanDownCarEntry": hwVlanDownCarEntry,
       "hwVlanDownCarId": hwVlanDownCarId,
       "hwVlanDownCarName": hwVlanDownCarName,
       "hwVlanDownCarBandValue": hwVlanDownCarBandValue,
       "hwVlanDownCarBurstValue": hwVlanDownCarBurstValue,
       "hwVlanDownCarIsUsed": hwVlanDownCarIsUsed,
       "hwVlanDownCarRowStatus": hwVlanDownCarRowStatus,
       "hwVlanParaTable": hwVlanParaTable,
       "hwVlanParaEntry": hwVlanParaEntry,
       "hwVlanParaIndex": hwVlanParaIndex,
       "hwVlanMacLearnCpability": hwVlanMacLearnCpability,
       "hwVlanMaxMacLearnNum": hwVlanMaxMacLearnNum,
       "hwVlanUpDirectCarID": hwVlanUpDirectCarID,
       "hwVlanDownDirectCarID": hwVlanDownDirectCarID,
       "hwBpduTunnelTable": hwBpduTunnelTable,
       "hwBpduTunnelEntry": hwBpduTunnelEntry,
       "hwBpduTunnel": hwBpduTunnel,
       "hwVOIPAddressTable": hwVOIPAddressTable,
       "hwVOIPAddressEntry": hwVOIPAddressEntry,
       "hwVOIPAddressIndex": hwVOIPAddressIndex,
       "hwVOIPIPType": hwVOIPIPType,
       "hwVOIPIPAddress": hwVOIPIPAddress,
       "hwVOIPSubMask": hwVOIPSubMask,
       "hwVOIPGateway": hwVOIPGateway,
       "hwVOIPMACAddress": hwVOIPMACAddress,
       "hwVOIPVlanTagIdentifier": hwVOIPVlanTagIdentifier,
       "hwVOIPQosIPStrategy": hwVOIPQosIPStrategy,
       "hwVOIPAddressRowStatus": hwVOIPAddressRowStatus,
       "hwVOIPAddressObtainMode": hwVOIPAddressObtainMode,
       "hwVOIPPPPOEClientName": hwVOIPPPPOEClientName,
       "hwVOIPIPAddressSrc": hwVOIPIPAddressSrc,
       "hwVOIPQosTable": hwVOIPQosTable,
       "hwVOIPQosEntry": hwVOIPQosEntry,
       "hwVOIPQosIPTosValue": hwVOIPQosIPTosValue,
       "hwVOIPQosIPDscpValue": hwVOIPQosIPDscpValue,
       "hwVOIPQosVlanPriority": hwVOIPQosVlanPriority,
       "hwVOIPQosIPAddressSrc": hwVOIPQosIPAddressSrc,
       "hwPacketTunnelTable": hwPacketTunnelTable,
       "hwPacketTunnelEntry": hwPacketTunnelEntry,
       "hwPacketTunnelRip": hwPacketTunnelRip,
       "hwPacketTunnelVTPCDP": hwPacketTunnelVTPCDP,
       "hwVlanInterfaceSubIpAddrTable": hwVlanInterfaceSubIpAddrTable,
       "hwVlanInterfaceSubIpAddrEntry": hwVlanInterfaceSubIpAddrEntry,
       "hwVlanInterfaceIDWithSub": hwVlanInterfaceIDWithSub,
       "hwVlanSubIpAddress": hwVlanSubIpAddress,
       "hwVlanSubIpAddressMask": hwVlanSubIpAddressMask,
       "hwInterfaceSubIpAddrRowStatus": hwInterfaceSubIpAddrRowStatus,
       "hwMethL2Vlan": hwMethL2Vlan,
       "hwDocsDefaultSrvVlanID": hwDocsDefaultSrvVlanID,
       "hwVlanSrvProfTable": hwVlanSrvProfTable,
       "hwVlanSrvProfEntry": hwVlanSrvProfEntry,
       "hwVlanSrvProfName": hwVlanSrvProfName,
       "hwForwardingMode": hwForwardingMode,
       "hwAntiIpSpoofingSwitch": hwAntiIpSpoofingSwitch,
       "hwAntiMacSpoofingSwitch": hwAntiMacSpoofingSwitch,
       "hwPPPoEMacMode": hwPPPoEMacMode,
       "hwBpduTunnelSwitch": hwBpduTunnelSwitch,
       "hwRipTunnelSwitch": hwRipTunnelSwitch,
       "hwVtpCdpTunnelSwitch": hwVtpCdpTunnelSwitch,
       "hwDhcpMode": hwDhcpMode,
       "hwDhcpProxySwitch": hwDhcpProxySwitch,
       "hwDhcpOption82Switch": hwDhcpOption82Switch,
       "hwPitpSwitch": hwPitpSwitch,
       "hwPolicyBroadcast": hwPolicyBroadcast,
       "hwPolicyMulticast": hwPolicyMulticast,
       "hwPolicyUnknowncast": hwPolicyUnknowncast,
       "hwUserBridging": hwUserBridging,
       "hwDhcpSuppressSwitch": hwDhcpSuppressSwitch,
       "hwMismatchIgmpPolicy": hwMismatchIgmpPolicy,
       "hwVmacStatus": hwVmacStatus,
       "hwIPoEMacMode": hwIPoEMacMode,
       "hwVmacAgingMode": hwVmacAgingMode,
       "hwFabricMacLearningSwitch": hwFabricMacLearningSwitch,
       "hwOspfTunnelSwitch": hwOspfTunnelSwitch,
       "hwL3ProtocolTunnelSwitch": hwL3ProtocolTunnelSwitch,
       "hwDhcpv6Mode": hwDhcpv6Mode,
       "hwDhcpv6OptionSwitch": hwDhcpv6OptionSwitch,
       "hwVmacIPoESubStatus": hwVmacIPoESubStatus,
       "hwVmacPPPoESubStatus": hwVmacPPPoESubStatus,
       "hwVmacPPPoASubStatus": hwVmacPPPoASubStatus,
       "hwPPPoAMacMode": hwPPPoAMacMode,
       "hwAntiIpv6SpoofingSwitch": hwAntiIpv6SpoofingSwitch,
       "hwIpv6DadProxySwitch": hwIpv6DadProxySwitch,
       "hwIpv6BindRouteAndNdSwitch": hwIpv6BindRouteAndNdSwitch,
       "hwIpv6NsReplySwitch": hwIpv6NsReplySwitch,
       "hwIpv4ArpReplySwitch": hwIpv4ArpReplySwitch,
       "hwDhcpRelayInterfaceRelayAgentSwitch": hwDhcpRelayInterfaceRelayAgentSwitch,
       "hwPolicyMulticastFabric": hwPolicyMulticastFabric,
       "hwCableSourceVerify": hwCableSourceVerify,
       "hwRipngTunnelSwitch": hwRipngTunnelSwitch,
       "hwIpv4ArpUnicastSwitch": hwIpv4ArpUnicastSwitch,
       "hwIpv4ArpUnicastunkonwnpolicy": hwIpv4ArpUnicastunkonwnpolicy,
       "hwIpv6NsUnicastSwitch": hwIpv6NsUnicastSwitch,
       "hwIpv6NsUnicastunkonwnpolicy": hwIpv6NsUnicastunkonwnpolicy,
       "hwIgmpUserMaxVlanTag": hwIgmpUserMaxVlanTag,
       "hwRouterRedirectReverse": hwRouterRedirectReverse,
       "hwCableIPv6SourceVerify": hwCableIPv6SourceVerify,
       "hwProfileRowStatus": hwProfileRowStatus,
       "hwSmartVlanIsolateSwitch": hwSmartVlanIsolateSwitch,
       "hwVlanIpAwareTable": hwVlanIpAwareTable,
       "hwVlanIpAwareEntry": hwVlanIpAwareEntry,
       "hwVlanIpAwareVlanID": hwVlanIpAwareVlanID,
       "hwVlanIpAwareVrfName": hwVlanIpAwareVrfName,
       "hwVlanIpAwareRowStatus": hwVlanIpAwareRowStatus,
       "hwVlanIpAwareSrcIPMode": hwVlanIpAwareSrcIPMode,
       "hwVlanIpAwareArpSendPeriod": hwVlanIpAwareArpSendPeriod,
       "hwIpAwareVirtualIPTable": hwIpAwareVirtualIPTable,
       "hwIpAwareVirtualIPEntry": hwIpAwareVirtualIPEntry,
       "hwIpAwareVirtualIPVlanID": hwIpAwareVirtualIPVlanID,
       "hwIpAwareVirtualIP": hwIpAwareVirtualIP,
       "hwIpAwareVirtualIPMask": hwIpAwareVirtualIPMask,
       "hwIpAwareVirtualIPRowStatus": hwIpAwareVirtualIPRowStatus,
       "hwIpAwareRouteTable": hwIpAwareRouteTable,
       "hwIpAwareRouteEntry": hwIpAwareRouteEntry,
       "hwIpAwareRouteDstIP": hwIpAwareRouteDstIP,
       "hwIpAwareRouteMask": hwIpAwareRouteMask,
       "hwIpAwareRouteVlanID": hwIpAwareRouteVlanID,
       "hwIpAwareRouteNexthopIP": hwIpAwareRouteNexthopIP,
       "hwIpAwareRouteRowStatus": hwIpAwareRouteRowStatus,
       "hwVlanInterfaceTrapsVbOids": hwVlanInterfaceTrapsVbOids,
       "hwL3InterfaceType": hwL3InterfaceType,
       "hwVlanifTraps": hwVlanifTraps,
       "hwVlanifCommonTraps": hwVlanifCommonTraps,
       "hwVlanifAlarmTraps": hwVlanifAlarmTraps,
       "hwVlanifAlarmTrapsPrefix": hwVlanifAlarmTrapsPrefix,
       "hwVlanifUpTrap": hwVlanifUpTrap,
       "hwVlanifDownTrap": hwVlanifDownTrap,
       "hwVlanCfgTrapsVbOids": hwVlanCfgTrapsVbOids,
       "hwVlanList": hwVlanList,
       "hwVlanSrvProfOperType": hwVlanSrvProfOperType,
       "hwVlanListType": hwVlanListType,
       "hwVlanListAttrib": hwVlanListAttrib,
       "hwVlanCfgTraps": hwVlanCfgTraps,
       "hwVlanCfgCommonTraps": hwVlanCfgCommonTraps,
       "hwVlanCfgCommonTrapsPrefix": hwVlanCfgCommonTrapsPrefix,
       "hwVlanNameChangeInfoTrap": hwVlanNameChangeInfoTrap,
       "hwVlanForwardingModeInfoTrap": hwVlanForwardingModeInfoTrap,
       "hwVlanSrvProfChageInfoTrap": hwVlanSrvProfChageInfoTrap,
       "hwVlanAndVlanSrvProfOperInfoTrap": hwVlanAndVlanSrvProfOperInfoTrap,
       "hwVlanAddInfoTrap": hwVlanAddInfoTrap,
       "hwVlanDelInfoTrap": hwVlanDelInfoTrap,
       "hwVlanAttrChangedInfoTrap": hwVlanAttrChangedInfoTrap,
       "hwPortVlanChangedInfoTrap": hwPortVlanChangedInfoTrap,
       "hwVOIPDhcpQosTable": hwVOIPDhcpQosTable,
       "hwVOIPDhcpQosEntry": hwVOIPDhcpQosEntry,
       "hwVOIPDhcpVlanID": hwVOIPDhcpVlanID,
       "hwVOIPDhcpQosType": hwVOIPDhcpQosType,
       "hwVOIPDhcpQosIPTos": hwVOIPDhcpQosIPTos,
       "hwVOIPDhcpQosIPDscp": hwVOIPDhcpQosIPDscp,
       "hwVOIPDhcpQosVlanPriority": hwVOIPDhcpQosVlanPriority,
       "hwVOIPDhcpQosRowStatus": hwVOIPDhcpQosRowStatus,
       "hwStackingVlanOuterEthernetType": hwStackingVlanOuterEthernetType,
       "hwDot1adTpid": hwDot1adTpid,
       "hwPortOuterEthernetTypeTable": hwPortOuterEthernetTypeTable,
       "hwPortOuterEthernetTypeEntry": hwPortOuterEthernetTypeEntry,
       "hwPortOuterEthernetType": hwPortOuterEthernetType,
       "hwVlanLocalSwitch": hwVlanLocalSwitch,
       "hwLocalVlanTable": hwLocalVlanTable,
       "hwLocalVlanEntry": hwLocalVlanEntry,
       "hwLocalVlan": hwLocalVlan,
       "hwVlanTrafficOccupiedTable": hwVlanTrafficOccupiedTable,
       "hwVlanTrafficOccupiedEntry": hwVlanTrafficOccupiedEntry,
       "hwVlanUplinkTraffic": hwVlanUplinkTraffic,
       "hwVlanDownTraffic": hwVlanDownTraffic,
       "hwVlanUplinkBandwidthOccupancyRate": hwVlanUplinkBandwidthOccupancyRate,
       "hwVlanDownBandwidthOccupancyRate": hwVlanDownBandwidthOccupancyRate,
       "hwMplsVlanTable": hwMplsVlanTable,
       "hwMplsVlanEntry": hwMplsVlanEntry,
       "hwMplsVlanEnable": hwMplsVlanEnable,
       "hwVlanConnectTable": hwVlanConnectTable,
       "hwVlanConnectEntry": hwVlanConnectEntry,
       "hwVlanConnectOuterVlanID": hwVlanConnectOuterVlanID,
       "hwVlanConnectInnerVlanID": hwVlanConnectInnerVlanID,
       "hwVlanConnectSrcType": hwVlanConnectSrcType,
       "hwVlanConnectSrcPara": hwVlanConnectSrcPara,
       "hwVlanConnectDstType": hwVlanConnectDstType,
       "hwVlanConnectDstPara": hwVlanConnectDstPara,
       "hwVlanConnectRowStatus": hwVlanConnectRowStatus,
       "hwDoubleTagTunnelConfig": hwDoubleTagTunnelConfig,
       "hwDoubleTagTunnelIgmp": hwDoubleTagTunnelIgmp,
       "hwDoubleTagTunnelRip": hwDoubleTagTunnelRip,
       "hwDoubleTagTunnelDhcp": hwDoubleTagTunnelDhcp,
       "hwDocsSrvVlanIDTable": hwDocsSrvVlanIDTable,
       "hwDocsSrvVlanIDEntry": hwDocsSrvVlanIDEntry,
       "hwDocsSrvVlanID": hwDocsSrvVlanID,
       "hwDocsSrvVlanRowStatus": hwDocsSrvVlanRowStatus,
       "hwMethNativeVlan": hwMethNativeVlan}
)
