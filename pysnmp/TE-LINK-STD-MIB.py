# SNMP MIB module (TE-LINK-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TE-LINK-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:19:14 2024
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

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

teLinkStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 200)
)
teLinkStdMIB.setRevisions(
        ("2005-10-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TeLinkBandwidth(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class TeLinkPriority(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class TeLinkProtection(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )



class TeLinkSwitchingCapability(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              51,
              100,
              150,
              200)
        )
    )
    namedValues = NamedValues(
        *(("fiberSwitch", 200),
          ("lambdaSwitch", 150),
          ("layer2Switch", 51),
          ("packetSwitch1", 1),
          ("packetSwitch2", 2),
          ("packetSwitch3", 3),
          ("packetSwitch4", 4),
          ("tdm", 100))
    )



class TeLinkEncodingType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              7,
              8,
              9,
              11)
        )
    )
    namedValues = NamedValues(
        *(("ansiEtsiPdh", 3),
          ("digitalWrapper", 7),
          ("ethernet", 2),
          ("fiber", 9),
          ("fiberChannel", 11),
          ("lambda", 8),
          ("packet", 1),
          ("sdhItuSonetAnsi", 5))
    )



class TeLinkSonetSdhIndication(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("arbitrary", 1),
          ("standard", 0))
    )



# MIB Managed Objects in the order of their OIDs

_TeLinkNotifications_ObjectIdentity = ObjectIdentity
teLinkNotifications = _TeLinkNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 200, 0)
)
_TeLinkObjects_ObjectIdentity = ObjectIdentity
teLinkObjects = _TeLinkObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 200, 1)
)
_TeLinkTable_Object = MibTable
teLinkTable = _TeLinkTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 1)
)
if mibBuilder.loadTexts:
    teLinkTable.setStatus("current")
_TeLinkEntry_Object = MibTableRow
teLinkEntry = _TeLinkEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 1, 1)
)
teLinkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    teLinkEntry.setStatus("current")
_TeLinkAddressType_Type = InetAddressType
_TeLinkAddressType_Object = MibTableColumn
teLinkAddressType = _TeLinkAddressType_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 1, 1, 1),
    _TeLinkAddressType_Type()
)
teLinkAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teLinkAddressType.setStatus("current")
_TeLinkLocalIpAddr_Type = InetAddress
_TeLinkLocalIpAddr_Object = MibTableColumn
teLinkLocalIpAddr = _TeLinkLocalIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 1, 1, 2),
    _TeLinkLocalIpAddr_Type()
)
teLinkLocalIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teLinkLocalIpAddr.setStatus("current")
_TeLinkRemoteIpAddr_Type = InetAddress
_TeLinkRemoteIpAddr_Object = MibTableColumn
teLinkRemoteIpAddr = _TeLinkRemoteIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 1, 1, 3),
    _TeLinkRemoteIpAddr_Type()
)
teLinkRemoteIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teLinkRemoteIpAddr.setStatus("current")
_TeLinkMetric_Type = Unsigned32
_TeLinkMetric_Object = MibTableColumn
teLinkMetric = _TeLinkMetric_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 1, 1, 4),
    _TeLinkMetric_Type()
)
teLinkMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teLinkMetric.setStatus("current")
_TeLinkMaximumReservableBandwidth_Type = TeLinkBandwidth
_TeLinkMaximumReservableBandwidth_Object = MibTableColumn
teLinkMaximumReservableBandwidth = _TeLinkMaximumReservableBandwidth_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 1, 1, 5),
    _TeLinkMaximumReservableBandwidth_Type()
)
teLinkMaximumReservableBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teLinkMaximumReservableBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    teLinkMaximumReservableBandwidth.setUnits("bps")


class _TeLinkProtectionType_Type(Integer32):
    """Custom type teLinkProtectionType based on Integer32"""
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
        *(("dedicated1For1", 4),
          ("dedicated1Plus1", 5),
          ("enhanced", 6),
          ("extraTraffic", 1),
          ("shared", 3),
          ("unprotected", 2))
    )


_TeLinkProtectionType_Type.__name__ = "Integer32"
_TeLinkProtectionType_Object = MibTableColumn
teLinkProtectionType = _TeLinkProtectionType_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 1, 1, 6),
    _TeLinkProtectionType_Type()
)
teLinkProtectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teLinkProtectionType.setStatus("current")
_TeLinkWorkingPriority_Type = TeLinkPriority
_TeLinkWorkingPriority_Object = MibTableColumn
teLinkWorkingPriority = _TeLinkWorkingPriority_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 1, 1, 7),
    _TeLinkWorkingPriority_Type()
)
teLinkWorkingPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teLinkWorkingPriority.setStatus("current")
_TeLinkResourceClass_Type = Unsigned32
_TeLinkResourceClass_Object = MibTableColumn
teLinkResourceClass = _TeLinkResourceClass_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 1, 1, 8),
    _TeLinkResourceClass_Type()
)
teLinkResourceClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teLinkResourceClass.setStatus("current")


class _TeLinkIncomingIfId_Type(Integer32):
    """Custom type teLinkIncomingIfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TeLinkIncomingIfId_Type.__name__ = "Integer32"
_TeLinkIncomingIfId_Object = MibTableColumn
teLinkIncomingIfId = _TeLinkIncomingIfId_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 1, 1, 9),
    _TeLinkIncomingIfId_Type()
)
teLinkIncomingIfId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teLinkIncomingIfId.setStatus("current")
_TeLinkOutgoingIfId_Type = InterfaceIndexOrZero
_TeLinkOutgoingIfId_Object = MibTableColumn
teLinkOutgoingIfId = _TeLinkOutgoingIfId_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 1, 1, 10),
    _TeLinkOutgoingIfId_Type()
)
teLinkOutgoingIfId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teLinkOutgoingIfId.setStatus("current")
_TeLinkRowStatus_Type = RowStatus
_TeLinkRowStatus_Object = MibTableColumn
teLinkRowStatus = _TeLinkRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 1, 1, 11),
    _TeLinkRowStatus_Type()
)
teLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teLinkRowStatus.setStatus("current")
_TeLinkStorageType_Type = StorageType
_TeLinkStorageType_Object = MibTableColumn
teLinkStorageType = _TeLinkStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 1, 1, 12),
    _TeLinkStorageType_Type()
)
teLinkStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teLinkStorageType.setStatus("current")
_TeLinkDescriptorTable_Object = MibTable
teLinkDescriptorTable = _TeLinkDescriptorTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 2)
)
if mibBuilder.loadTexts:
    teLinkDescriptorTable.setStatus("current")
_TeLinkDescriptorEntry_Object = MibTableRow
teLinkDescriptorEntry = _TeLinkDescriptorEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 2, 1)
)
teLinkDescriptorEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TE-LINK-STD-MIB", "teLinkDescriptorId"),
)
if mibBuilder.loadTexts:
    teLinkDescriptorEntry.setStatus("current")


class _TeLinkDescriptorId_Type(Unsigned32):
    """Custom type teLinkDescriptorId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TeLinkDescriptorId_Type.__name__ = "Unsigned32"
_TeLinkDescriptorId_Object = MibTableColumn
teLinkDescriptorId = _TeLinkDescriptorId_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 2, 1, 1),
    _TeLinkDescriptorId_Type()
)
teLinkDescriptorId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    teLinkDescriptorId.setStatus("current")
_TeLinkDescrSwitchingCapability_Type = TeLinkSwitchingCapability
_TeLinkDescrSwitchingCapability_Object = MibTableColumn
teLinkDescrSwitchingCapability = _TeLinkDescrSwitchingCapability_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 2, 1, 2),
    _TeLinkDescrSwitchingCapability_Type()
)
teLinkDescrSwitchingCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teLinkDescrSwitchingCapability.setStatus("current")
_TeLinkDescrEncodingType_Type = TeLinkEncodingType
_TeLinkDescrEncodingType_Object = MibTableColumn
teLinkDescrEncodingType = _TeLinkDescrEncodingType_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 2, 1, 3),
    _TeLinkDescrEncodingType_Type()
)
teLinkDescrEncodingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teLinkDescrEncodingType.setStatus("current")
_TeLinkDescrMinLspBandwidth_Type = TeLinkBandwidth
_TeLinkDescrMinLspBandwidth_Object = MibTableColumn
teLinkDescrMinLspBandwidth = _TeLinkDescrMinLspBandwidth_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 2, 1, 4),
    _TeLinkDescrMinLspBandwidth_Type()
)
teLinkDescrMinLspBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teLinkDescrMinLspBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    teLinkDescrMinLspBandwidth.setUnits("bps")
_TeLinkDescrMaxLspBandwidthPrio0_Type = TeLinkBandwidth
_TeLinkDescrMaxLspBandwidthPrio0_Object = MibTableColumn
teLinkDescrMaxLspBandwidthPrio0 = _TeLinkDescrMaxLspBandwidthPrio0_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 2, 1, 5),
    _TeLinkDescrMaxLspBandwidthPrio0_Type()
)
teLinkDescrMaxLspBandwidthPrio0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teLinkDescrMaxLspBandwidthPrio0.setStatus("current")
if mibBuilder.loadTexts:
    teLinkDescrMaxLspBandwidthPrio0.setUnits("bps")
_TeLinkDescrMaxLspBandwidthPrio1_Type = TeLinkBandwidth
_TeLinkDescrMaxLspBandwidthPrio1_Object = MibTableColumn
teLinkDescrMaxLspBandwidthPrio1 = _TeLinkDescrMaxLspBandwidthPrio1_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 2, 1, 6),
    _TeLinkDescrMaxLspBandwidthPrio1_Type()
)
teLinkDescrMaxLspBandwidthPrio1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teLinkDescrMaxLspBandwidthPrio1.setStatus("current")
if mibBuilder.loadTexts:
    teLinkDescrMaxLspBandwidthPrio1.setUnits("bps")
_TeLinkDescrMaxLspBandwidthPrio2_Type = TeLinkBandwidth
_TeLinkDescrMaxLspBandwidthPrio2_Object = MibTableColumn
teLinkDescrMaxLspBandwidthPrio2 = _TeLinkDescrMaxLspBandwidthPrio2_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 2, 1, 7),
    _TeLinkDescrMaxLspBandwidthPrio2_Type()
)
teLinkDescrMaxLspBandwidthPrio2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teLinkDescrMaxLspBandwidthPrio2.setStatus("current")
if mibBuilder.loadTexts:
    teLinkDescrMaxLspBandwidthPrio2.setUnits("bps")
_TeLinkDescrMaxLspBandwidthPrio3_Type = TeLinkBandwidth
_TeLinkDescrMaxLspBandwidthPrio3_Object = MibTableColumn
teLinkDescrMaxLspBandwidthPrio3 = _TeLinkDescrMaxLspBandwidthPrio3_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 2, 1, 8),
    _TeLinkDescrMaxLspBandwidthPrio3_Type()
)
teLinkDescrMaxLspBandwidthPrio3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teLinkDescrMaxLspBandwidthPrio3.setStatus("current")
if mibBuilder.loadTexts:
    teLinkDescrMaxLspBandwidthPrio3.setUnits("bps")
_TeLinkDescrMaxLspBandwidthPrio4_Type = TeLinkBandwidth
_TeLinkDescrMaxLspBandwidthPrio4_Object = MibTableColumn
teLinkDescrMaxLspBandwidthPrio4 = _TeLinkDescrMaxLspBandwidthPrio4_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 2, 1, 9),
    _TeLinkDescrMaxLspBandwidthPrio4_Type()
)
teLinkDescrMaxLspBandwidthPrio4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teLinkDescrMaxLspBandwidthPrio4.setStatus("current")
if mibBuilder.loadTexts:
    teLinkDescrMaxLspBandwidthPrio4.setUnits("bps")
_TeLinkDescrMaxLspBandwidthPrio5_Type = TeLinkBandwidth
_TeLinkDescrMaxLspBandwidthPrio5_Object = MibTableColumn
teLinkDescrMaxLspBandwidthPrio5 = _TeLinkDescrMaxLspBandwidthPrio5_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 2, 1, 10),
    _TeLinkDescrMaxLspBandwidthPrio5_Type()
)
teLinkDescrMaxLspBandwidthPrio5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teLinkDescrMaxLspBandwidthPrio5.setStatus("current")
if mibBuilder.loadTexts:
    teLinkDescrMaxLspBandwidthPrio5.setUnits("bps")
_TeLinkDescrMaxLspBandwidthPrio6_Type = TeLinkBandwidth
_TeLinkDescrMaxLspBandwidthPrio6_Object = MibTableColumn
teLinkDescrMaxLspBandwidthPrio6 = _TeLinkDescrMaxLspBandwidthPrio6_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 2, 1, 11),
    _TeLinkDescrMaxLspBandwidthPrio6_Type()
)
teLinkDescrMaxLspBandwidthPrio6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teLinkDescrMaxLspBandwidthPrio6.setStatus("current")
if mibBuilder.loadTexts:
    teLinkDescrMaxLspBandwidthPrio6.setUnits("bps")
_TeLinkDescrMaxLspBandwidthPrio7_Type = TeLinkBandwidth
_TeLinkDescrMaxLspBandwidthPrio7_Object = MibTableColumn
teLinkDescrMaxLspBandwidthPrio7 = _TeLinkDescrMaxLspBandwidthPrio7_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 2, 1, 12),
    _TeLinkDescrMaxLspBandwidthPrio7_Type()
)
teLinkDescrMaxLspBandwidthPrio7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teLinkDescrMaxLspBandwidthPrio7.setStatus("current")
if mibBuilder.loadTexts:
    teLinkDescrMaxLspBandwidthPrio7.setUnits("bps")


class _TeLinkDescrInterfaceMtu_Type(Unsigned32):
    """Custom type teLinkDescrInterfaceMtu based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TeLinkDescrInterfaceMtu_Type.__name__ = "Unsigned32"
_TeLinkDescrInterfaceMtu_Object = MibTableColumn
teLinkDescrInterfaceMtu = _TeLinkDescrInterfaceMtu_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 2, 1, 13),
    _TeLinkDescrInterfaceMtu_Type()
)
teLinkDescrInterfaceMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teLinkDescrInterfaceMtu.setStatus("current")
_TeLinkDescrIndication_Type = TeLinkSonetSdhIndication
_TeLinkDescrIndication_Object = MibTableColumn
teLinkDescrIndication = _TeLinkDescrIndication_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 2, 1, 14),
    _TeLinkDescrIndication_Type()
)
teLinkDescrIndication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teLinkDescrIndication.setStatus("current")
_TeLinkDescrRowStatus_Type = RowStatus
_TeLinkDescrRowStatus_Object = MibTableColumn
teLinkDescrRowStatus = _TeLinkDescrRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 2, 1, 15),
    _TeLinkDescrRowStatus_Type()
)
teLinkDescrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teLinkDescrRowStatus.setStatus("current")
_TeLinkDescrStorageType_Type = StorageType
_TeLinkDescrStorageType_Object = MibTableColumn
teLinkDescrStorageType = _TeLinkDescrStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 2, 1, 16),
    _TeLinkDescrStorageType_Type()
)
teLinkDescrStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teLinkDescrStorageType.setStatus("current")
_TeLinkSrlgTable_Object = MibTable
teLinkSrlgTable = _TeLinkSrlgTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 3)
)
if mibBuilder.loadTexts:
    teLinkSrlgTable.setStatus("current")
_TeLinkSrlgEntry_Object = MibTableRow
teLinkSrlgEntry = _TeLinkSrlgEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 3, 1)
)
teLinkSrlgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TE-LINK-STD-MIB", "teLinkSrlg"),
)
if mibBuilder.loadTexts:
    teLinkSrlgEntry.setStatus("current")


class _TeLinkSrlg_Type(Unsigned32):
    """Custom type teLinkSrlg based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TeLinkSrlg_Type.__name__ = "Unsigned32"
_TeLinkSrlg_Object = MibTableColumn
teLinkSrlg = _TeLinkSrlg_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 3, 1, 1),
    _TeLinkSrlg_Type()
)
teLinkSrlg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    teLinkSrlg.setStatus("current")
_TeLinkSrlgRowStatus_Type = RowStatus
_TeLinkSrlgRowStatus_Object = MibTableColumn
teLinkSrlgRowStatus = _TeLinkSrlgRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 3, 1, 2),
    _TeLinkSrlgRowStatus_Type()
)
teLinkSrlgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teLinkSrlgRowStatus.setStatus("current")
_TeLinkSrlgStorageType_Type = StorageType
_TeLinkSrlgStorageType_Object = MibTableColumn
teLinkSrlgStorageType = _TeLinkSrlgStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 3, 1, 3),
    _TeLinkSrlgStorageType_Type()
)
teLinkSrlgStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teLinkSrlgStorageType.setStatus("current")
_TeLinkBandwidthTable_Object = MibTable
teLinkBandwidthTable = _TeLinkBandwidthTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 4)
)
if mibBuilder.loadTexts:
    teLinkBandwidthTable.setStatus("current")
_TeLinkBandwidthEntry_Object = MibTableRow
teLinkBandwidthEntry = _TeLinkBandwidthEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 4, 1)
)
teLinkBandwidthEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TE-LINK-STD-MIB", "teLinkBandwidthPriority"),
)
if mibBuilder.loadTexts:
    teLinkBandwidthEntry.setStatus("current")
_TeLinkBandwidthPriority_Type = TeLinkPriority
_TeLinkBandwidthPriority_Object = MibTableColumn
teLinkBandwidthPriority = _TeLinkBandwidthPriority_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 4, 1, 1),
    _TeLinkBandwidthPriority_Type()
)
teLinkBandwidthPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    teLinkBandwidthPriority.setStatus("current")
_TeLinkBandwidthUnreserved_Type = TeLinkBandwidth
_TeLinkBandwidthUnreserved_Object = MibTableColumn
teLinkBandwidthUnreserved = _TeLinkBandwidthUnreserved_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 4, 1, 2),
    _TeLinkBandwidthUnreserved_Type()
)
teLinkBandwidthUnreserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teLinkBandwidthUnreserved.setStatus("current")
if mibBuilder.loadTexts:
    teLinkBandwidthUnreserved.setUnits("bps")
_TeLinkBandwidthRowStatus_Type = RowStatus
_TeLinkBandwidthRowStatus_Object = MibTableColumn
teLinkBandwidthRowStatus = _TeLinkBandwidthRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 4, 1, 3),
    _TeLinkBandwidthRowStatus_Type()
)
teLinkBandwidthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teLinkBandwidthRowStatus.setStatus("current")
_TeLinkBandwidthStorageType_Type = StorageType
_TeLinkBandwidthStorageType_Object = MibTableColumn
teLinkBandwidthStorageType = _TeLinkBandwidthStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 4, 1, 4),
    _TeLinkBandwidthStorageType_Type()
)
teLinkBandwidthStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teLinkBandwidthStorageType.setStatus("current")
_ComponentLinkTable_Object = MibTable
componentLinkTable = _ComponentLinkTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 5)
)
if mibBuilder.loadTexts:
    componentLinkTable.setStatus("current")
_ComponentLinkEntry_Object = MibTableRow
componentLinkEntry = _ComponentLinkEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 5, 1)
)
componentLinkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    componentLinkEntry.setStatus("current")
_ComponentLinkMaxResBandwidth_Type = TeLinkBandwidth
_ComponentLinkMaxResBandwidth_Object = MibTableColumn
componentLinkMaxResBandwidth = _ComponentLinkMaxResBandwidth_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 5, 1, 1),
    _ComponentLinkMaxResBandwidth_Type()
)
componentLinkMaxResBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    componentLinkMaxResBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    componentLinkMaxResBandwidth.setUnits("bps")
_ComponentLinkPreferredProtection_Type = TeLinkProtection
_ComponentLinkPreferredProtection_Object = MibTableColumn
componentLinkPreferredProtection = _ComponentLinkPreferredProtection_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 5, 1, 2),
    _ComponentLinkPreferredProtection_Type()
)
componentLinkPreferredProtection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    componentLinkPreferredProtection.setStatus("current")
_ComponentLinkCurrentProtection_Type = TeLinkProtection
_ComponentLinkCurrentProtection_Object = MibTableColumn
componentLinkCurrentProtection = _ComponentLinkCurrentProtection_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 5, 1, 3),
    _ComponentLinkCurrentProtection_Type()
)
componentLinkCurrentProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLinkCurrentProtection.setStatus("current")
_ComponentLinkRowStatus_Type = RowStatus
_ComponentLinkRowStatus_Object = MibTableColumn
componentLinkRowStatus = _ComponentLinkRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 5, 1, 4),
    _ComponentLinkRowStatus_Type()
)
componentLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    componentLinkRowStatus.setStatus("current")
_ComponentLinkStorageType_Type = StorageType
_ComponentLinkStorageType_Object = MibTableColumn
componentLinkStorageType = _ComponentLinkStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 5, 1, 5),
    _ComponentLinkStorageType_Type()
)
componentLinkStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    componentLinkStorageType.setStatus("current")
_ComponentLinkDescriptorTable_Object = MibTable
componentLinkDescriptorTable = _ComponentLinkDescriptorTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 6)
)
if mibBuilder.loadTexts:
    componentLinkDescriptorTable.setStatus("current")
_ComponentLinkDescriptorEntry_Object = MibTableRow
componentLinkDescriptorEntry = _ComponentLinkDescriptorEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 6, 1)
)
componentLinkDescriptorEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TE-LINK-STD-MIB", "componentLinkDescrId"),
)
if mibBuilder.loadTexts:
    componentLinkDescriptorEntry.setStatus("current")


class _ComponentLinkDescrId_Type(Unsigned32):
    """Custom type componentLinkDescrId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ComponentLinkDescrId_Type.__name__ = "Unsigned32"
_ComponentLinkDescrId_Object = MibTableColumn
componentLinkDescrId = _ComponentLinkDescrId_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 6, 1, 1),
    _ComponentLinkDescrId_Type()
)
componentLinkDescrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    componentLinkDescrId.setStatus("current")
_ComponentLinkDescrSwitchingCapability_Type = TeLinkSwitchingCapability
_ComponentLinkDescrSwitchingCapability_Object = MibTableColumn
componentLinkDescrSwitchingCapability = _ComponentLinkDescrSwitchingCapability_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 6, 1, 2),
    _ComponentLinkDescrSwitchingCapability_Type()
)
componentLinkDescrSwitchingCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    componentLinkDescrSwitchingCapability.setStatus("current")
_ComponentLinkDescrEncodingType_Type = TeLinkEncodingType
_ComponentLinkDescrEncodingType_Object = MibTableColumn
componentLinkDescrEncodingType = _ComponentLinkDescrEncodingType_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 6, 1, 3),
    _ComponentLinkDescrEncodingType_Type()
)
componentLinkDescrEncodingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    componentLinkDescrEncodingType.setStatus("current")
_ComponentLinkDescrMinLspBandwidth_Type = TeLinkBandwidth
_ComponentLinkDescrMinLspBandwidth_Object = MibTableColumn
componentLinkDescrMinLspBandwidth = _ComponentLinkDescrMinLspBandwidth_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 6, 1, 4),
    _ComponentLinkDescrMinLspBandwidth_Type()
)
componentLinkDescrMinLspBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    componentLinkDescrMinLspBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    componentLinkDescrMinLspBandwidth.setUnits("bps")
_ComponentLinkDescrMaxLspBandwidthPrio0_Type = TeLinkBandwidth
_ComponentLinkDescrMaxLspBandwidthPrio0_Object = MibTableColumn
componentLinkDescrMaxLspBandwidthPrio0 = _ComponentLinkDescrMaxLspBandwidthPrio0_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 6, 1, 5),
    _ComponentLinkDescrMaxLspBandwidthPrio0_Type()
)
componentLinkDescrMaxLspBandwidthPrio0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    componentLinkDescrMaxLspBandwidthPrio0.setStatus("current")
if mibBuilder.loadTexts:
    componentLinkDescrMaxLspBandwidthPrio0.setUnits("bps")
_ComponentLinkDescrMaxLspBandwidthPrio1_Type = TeLinkBandwidth
_ComponentLinkDescrMaxLspBandwidthPrio1_Object = MibTableColumn
componentLinkDescrMaxLspBandwidthPrio1 = _ComponentLinkDescrMaxLspBandwidthPrio1_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 6, 1, 6),
    _ComponentLinkDescrMaxLspBandwidthPrio1_Type()
)
componentLinkDescrMaxLspBandwidthPrio1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    componentLinkDescrMaxLspBandwidthPrio1.setStatus("current")
if mibBuilder.loadTexts:
    componentLinkDescrMaxLspBandwidthPrio1.setUnits("bps")
_ComponentLinkDescrMaxLspBandwidthPrio2_Type = TeLinkBandwidth
_ComponentLinkDescrMaxLspBandwidthPrio2_Object = MibTableColumn
componentLinkDescrMaxLspBandwidthPrio2 = _ComponentLinkDescrMaxLspBandwidthPrio2_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 6, 1, 7),
    _ComponentLinkDescrMaxLspBandwidthPrio2_Type()
)
componentLinkDescrMaxLspBandwidthPrio2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    componentLinkDescrMaxLspBandwidthPrio2.setStatus("current")
if mibBuilder.loadTexts:
    componentLinkDescrMaxLspBandwidthPrio2.setUnits("bps")
_ComponentLinkDescrMaxLspBandwidthPrio3_Type = TeLinkBandwidth
_ComponentLinkDescrMaxLspBandwidthPrio3_Object = MibTableColumn
componentLinkDescrMaxLspBandwidthPrio3 = _ComponentLinkDescrMaxLspBandwidthPrio3_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 6, 1, 8),
    _ComponentLinkDescrMaxLspBandwidthPrio3_Type()
)
componentLinkDescrMaxLspBandwidthPrio3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    componentLinkDescrMaxLspBandwidthPrio3.setStatus("current")
if mibBuilder.loadTexts:
    componentLinkDescrMaxLspBandwidthPrio3.setUnits("bps")
_ComponentLinkDescrMaxLspBandwidthPrio4_Type = TeLinkBandwidth
_ComponentLinkDescrMaxLspBandwidthPrio4_Object = MibTableColumn
componentLinkDescrMaxLspBandwidthPrio4 = _ComponentLinkDescrMaxLspBandwidthPrio4_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 6, 1, 9),
    _ComponentLinkDescrMaxLspBandwidthPrio4_Type()
)
componentLinkDescrMaxLspBandwidthPrio4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    componentLinkDescrMaxLspBandwidthPrio4.setStatus("current")
if mibBuilder.loadTexts:
    componentLinkDescrMaxLspBandwidthPrio4.setUnits("bps")
_ComponentLinkDescrMaxLspBandwidthPrio5_Type = TeLinkBandwidth
_ComponentLinkDescrMaxLspBandwidthPrio5_Object = MibTableColumn
componentLinkDescrMaxLspBandwidthPrio5 = _ComponentLinkDescrMaxLspBandwidthPrio5_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 6, 1, 10),
    _ComponentLinkDescrMaxLspBandwidthPrio5_Type()
)
componentLinkDescrMaxLspBandwidthPrio5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    componentLinkDescrMaxLspBandwidthPrio5.setStatus("current")
if mibBuilder.loadTexts:
    componentLinkDescrMaxLspBandwidthPrio5.setUnits("thousand bps")
_ComponentLinkDescrMaxLspBandwidthPrio6_Type = TeLinkBandwidth
_ComponentLinkDescrMaxLspBandwidthPrio6_Object = MibTableColumn
componentLinkDescrMaxLspBandwidthPrio6 = _ComponentLinkDescrMaxLspBandwidthPrio6_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 6, 1, 11),
    _ComponentLinkDescrMaxLspBandwidthPrio6_Type()
)
componentLinkDescrMaxLspBandwidthPrio6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    componentLinkDescrMaxLspBandwidthPrio6.setStatus("current")
if mibBuilder.loadTexts:
    componentLinkDescrMaxLspBandwidthPrio6.setUnits("bps")
_ComponentLinkDescrMaxLspBandwidthPrio7_Type = TeLinkBandwidth
_ComponentLinkDescrMaxLspBandwidthPrio7_Object = MibTableColumn
componentLinkDescrMaxLspBandwidthPrio7 = _ComponentLinkDescrMaxLspBandwidthPrio7_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 6, 1, 12),
    _ComponentLinkDescrMaxLspBandwidthPrio7_Type()
)
componentLinkDescrMaxLspBandwidthPrio7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    componentLinkDescrMaxLspBandwidthPrio7.setStatus("current")
if mibBuilder.loadTexts:
    componentLinkDescrMaxLspBandwidthPrio7.setUnits("bps")


class _ComponentLinkDescrInterfaceMtu_Type(Unsigned32):
    """Custom type componentLinkDescrInterfaceMtu based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ComponentLinkDescrInterfaceMtu_Type.__name__ = "Unsigned32"
_ComponentLinkDescrInterfaceMtu_Object = MibTableColumn
componentLinkDescrInterfaceMtu = _ComponentLinkDescrInterfaceMtu_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 6, 1, 13),
    _ComponentLinkDescrInterfaceMtu_Type()
)
componentLinkDescrInterfaceMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    componentLinkDescrInterfaceMtu.setStatus("current")
_ComponentLinkDescrIndication_Type = TeLinkSonetSdhIndication
_ComponentLinkDescrIndication_Object = MibTableColumn
componentLinkDescrIndication = _ComponentLinkDescrIndication_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 6, 1, 14),
    _ComponentLinkDescrIndication_Type()
)
componentLinkDescrIndication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    componentLinkDescrIndication.setStatus("current")
_ComponentLinkDescrRowStatus_Type = RowStatus
_ComponentLinkDescrRowStatus_Object = MibTableColumn
componentLinkDescrRowStatus = _ComponentLinkDescrRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 6, 1, 15),
    _ComponentLinkDescrRowStatus_Type()
)
componentLinkDescrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    componentLinkDescrRowStatus.setStatus("current")
_ComponentLinkDescrStorageType_Type = StorageType
_ComponentLinkDescrStorageType_Object = MibTableColumn
componentLinkDescrStorageType = _ComponentLinkDescrStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 6, 1, 16),
    _ComponentLinkDescrStorageType_Type()
)
componentLinkDescrStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    componentLinkDescrStorageType.setStatus("current")
_ComponentLinkBandwidthTable_Object = MibTable
componentLinkBandwidthTable = _ComponentLinkBandwidthTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 7)
)
if mibBuilder.loadTexts:
    componentLinkBandwidthTable.setStatus("current")
_ComponentLinkBandwidthEntry_Object = MibTableRow
componentLinkBandwidthEntry = _ComponentLinkBandwidthEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 7, 1)
)
componentLinkBandwidthEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TE-LINK-STD-MIB", "componentLinkBandwidthPriority"),
)
if mibBuilder.loadTexts:
    componentLinkBandwidthEntry.setStatus("current")
_ComponentLinkBandwidthPriority_Type = TeLinkPriority
_ComponentLinkBandwidthPriority_Object = MibTableColumn
componentLinkBandwidthPriority = _ComponentLinkBandwidthPriority_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 7, 1, 1),
    _ComponentLinkBandwidthPriority_Type()
)
componentLinkBandwidthPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    componentLinkBandwidthPriority.setStatus("current")
_ComponentLinkBandwidthUnreserved_Type = TeLinkBandwidth
_ComponentLinkBandwidthUnreserved_Object = MibTableColumn
componentLinkBandwidthUnreserved = _ComponentLinkBandwidthUnreserved_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 7, 1, 2),
    _ComponentLinkBandwidthUnreserved_Type()
)
componentLinkBandwidthUnreserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLinkBandwidthUnreserved.setStatus("current")
if mibBuilder.loadTexts:
    componentLinkBandwidthUnreserved.setUnits("bps")
_ComponentLinkBandwidthRowStatus_Type = RowStatus
_ComponentLinkBandwidthRowStatus_Object = MibTableColumn
componentLinkBandwidthRowStatus = _ComponentLinkBandwidthRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 7, 1, 3),
    _ComponentLinkBandwidthRowStatus_Type()
)
componentLinkBandwidthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    componentLinkBandwidthRowStatus.setStatus("current")
_ComponentLinkBandwidthStorageType_Type = StorageType
_ComponentLinkBandwidthStorageType_Object = MibTableColumn
componentLinkBandwidthStorageType = _ComponentLinkBandwidthStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 200, 1, 7, 1, 4),
    _ComponentLinkBandwidthStorageType_Type()
)
componentLinkBandwidthStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    componentLinkBandwidthStorageType.setStatus("current")
_TeLinkConformance_ObjectIdentity = ObjectIdentity
teLinkConformance = _TeLinkConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 200, 2)
)
_TeLinkCompliances_ObjectIdentity = ObjectIdentity
teLinkCompliances = _TeLinkCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 200, 2, 1)
)
_TeLinkGroups_ObjectIdentity = ObjectIdentity
teLinkGroups = _TeLinkGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 200, 2, 2)
)

# Managed Objects groups

teLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 200, 2, 2, 1)
)
teLinkGroup.setObjects(
      *(("TE-LINK-STD-MIB", "teLinkAddressType"),
        ("TE-LINK-STD-MIB", "teLinkLocalIpAddr"),
        ("TE-LINK-STD-MIB", "teLinkRemoteIpAddr"),
        ("TE-LINK-STD-MIB", "teLinkMetric"),
        ("TE-LINK-STD-MIB", "teLinkProtectionType"),
        ("TE-LINK-STD-MIB", "teLinkWorkingPriority"),
        ("TE-LINK-STD-MIB", "teLinkResourceClass"),
        ("TE-LINK-STD-MIB", "teLinkIncomingIfId"),
        ("TE-LINK-STD-MIB", "teLinkOutgoingIfId"),
        ("TE-LINK-STD-MIB", "teLinkRowStatus"),
        ("TE-LINK-STD-MIB", "teLinkStorageType"),
        ("TE-LINK-STD-MIB", "teLinkDescrSwitchingCapability"),
        ("TE-LINK-STD-MIB", "teLinkDescrEncodingType"),
        ("TE-LINK-STD-MIB", "teLinkDescrRowStatus"),
        ("TE-LINK-STD-MIB", "teLinkDescrStorageType"),
        ("TE-LINK-STD-MIB", "componentLinkPreferredProtection"),
        ("TE-LINK-STD-MIB", "componentLinkCurrentProtection"),
        ("TE-LINK-STD-MIB", "componentLinkRowStatus"),
        ("TE-LINK-STD-MIB", "componentLinkStorageType"),
        ("TE-LINK-STD-MIB", "componentLinkDescrSwitchingCapability"),
        ("TE-LINK-STD-MIB", "componentLinkDescrEncodingType"),
        ("TE-LINK-STD-MIB", "componentLinkDescrRowStatus"),
        ("TE-LINK-STD-MIB", "componentLinkDescrStorageType"))
)
if mibBuilder.loadTexts:
    teLinkGroup.setStatus("current")

teLinkSrlgGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 200, 2, 2, 2)
)
teLinkSrlgGroup.setObjects(
      *(("TE-LINK-STD-MIB", "teLinkSrlgRowStatus"),
        ("TE-LINK-STD-MIB", "teLinkSrlgStorageType"))
)
if mibBuilder.loadTexts:
    teLinkSrlgGroup.setStatus("current")

teLinkBandwidthGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 200, 2, 2, 3)
)
teLinkBandwidthGroup.setObjects(
      *(("TE-LINK-STD-MIB", "teLinkMaximumReservableBandwidth"),
        ("TE-LINK-STD-MIB", "teLinkDescrMaxLspBandwidthPrio0"),
        ("TE-LINK-STD-MIB", "teLinkDescrMaxLspBandwidthPrio1"),
        ("TE-LINK-STD-MIB", "teLinkDescrMaxLspBandwidthPrio2"),
        ("TE-LINK-STD-MIB", "teLinkDescrMaxLspBandwidthPrio3"),
        ("TE-LINK-STD-MIB", "teLinkDescrMaxLspBandwidthPrio4"),
        ("TE-LINK-STD-MIB", "teLinkDescrMaxLspBandwidthPrio5"),
        ("TE-LINK-STD-MIB", "teLinkDescrMaxLspBandwidthPrio6"),
        ("TE-LINK-STD-MIB", "teLinkDescrMaxLspBandwidthPrio7"),
        ("TE-LINK-STD-MIB", "teLinkBandwidthUnreserved"),
        ("TE-LINK-STD-MIB", "teLinkBandwidthRowStatus"),
        ("TE-LINK-STD-MIB", "teLinkBandwidthStorageType"))
)
if mibBuilder.loadTexts:
    teLinkBandwidthGroup.setStatus("current")

componentLinkBandwidthGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 200, 2, 2, 4)
)
componentLinkBandwidthGroup.setObjects(
      *(("TE-LINK-STD-MIB", "componentLinkMaxResBandwidth"),
        ("TE-LINK-STD-MIB", "componentLinkDescrMaxLspBandwidthPrio0"),
        ("TE-LINK-STD-MIB", "componentLinkDescrMaxLspBandwidthPrio1"),
        ("TE-LINK-STD-MIB", "componentLinkDescrMaxLspBandwidthPrio2"),
        ("TE-LINK-STD-MIB", "componentLinkDescrMaxLspBandwidthPrio3"),
        ("TE-LINK-STD-MIB", "componentLinkDescrMaxLspBandwidthPrio4"),
        ("TE-LINK-STD-MIB", "componentLinkDescrMaxLspBandwidthPrio5"),
        ("TE-LINK-STD-MIB", "componentLinkDescrMaxLspBandwidthPrio6"),
        ("TE-LINK-STD-MIB", "componentLinkDescrMaxLspBandwidthPrio7"),
        ("TE-LINK-STD-MIB", "componentLinkBandwidthUnreserved"),
        ("TE-LINK-STD-MIB", "componentLinkBandwidthRowStatus"),
        ("TE-LINK-STD-MIB", "componentLinkBandwidthStorageType"))
)
if mibBuilder.loadTexts:
    componentLinkBandwidthGroup.setStatus("current")

teLinkPscGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 200, 2, 2, 5)
)
teLinkPscGroup.setObjects(
      *(("TE-LINK-STD-MIB", "teLinkDescrMinLspBandwidth"),
        ("TE-LINK-STD-MIB", "teLinkDescrInterfaceMtu"),
        ("TE-LINK-STD-MIB", "componentLinkDescrMinLspBandwidth"),
        ("TE-LINK-STD-MIB", "componentLinkDescrInterfaceMtu"))
)
if mibBuilder.loadTexts:
    teLinkPscGroup.setStatus("current")

teLinkTdmGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 200, 2, 2, 6)
)
teLinkTdmGroup.setObjects(
      *(("TE-LINK-STD-MIB", "teLinkDescrMinLspBandwidth"),
        ("TE-LINK-STD-MIB", "teLinkDescrIndication"),
        ("TE-LINK-STD-MIB", "componentLinkDescrMinLspBandwidth"),
        ("TE-LINK-STD-MIB", "componentLinkDescrIndication"))
)
if mibBuilder.loadTexts:
    teLinkTdmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

teLinkModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 200, 2, 1, 1)
)
if mibBuilder.loadTexts:
    teLinkModuleFullCompliance.setStatus(
        "current"
    )

teLinkModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 200, 2, 1, 2)
)
if mibBuilder.loadTexts:
    teLinkModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TE-LINK-STD-MIB",
    **{"TeLinkBandwidth": TeLinkBandwidth,
       "TeLinkPriority": TeLinkPriority,
       "TeLinkProtection": TeLinkProtection,
       "TeLinkSwitchingCapability": TeLinkSwitchingCapability,
       "TeLinkEncodingType": TeLinkEncodingType,
       "TeLinkSonetSdhIndication": TeLinkSonetSdhIndication,
       "teLinkStdMIB": teLinkStdMIB,
       "teLinkNotifications": teLinkNotifications,
       "teLinkObjects": teLinkObjects,
       "teLinkTable": teLinkTable,
       "teLinkEntry": teLinkEntry,
       "teLinkAddressType": teLinkAddressType,
       "teLinkLocalIpAddr": teLinkLocalIpAddr,
       "teLinkRemoteIpAddr": teLinkRemoteIpAddr,
       "teLinkMetric": teLinkMetric,
       "teLinkMaximumReservableBandwidth": teLinkMaximumReservableBandwidth,
       "teLinkProtectionType": teLinkProtectionType,
       "teLinkWorkingPriority": teLinkWorkingPriority,
       "teLinkResourceClass": teLinkResourceClass,
       "teLinkIncomingIfId": teLinkIncomingIfId,
       "teLinkOutgoingIfId": teLinkOutgoingIfId,
       "teLinkRowStatus": teLinkRowStatus,
       "teLinkStorageType": teLinkStorageType,
       "teLinkDescriptorTable": teLinkDescriptorTable,
       "teLinkDescriptorEntry": teLinkDescriptorEntry,
       "teLinkDescriptorId": teLinkDescriptorId,
       "teLinkDescrSwitchingCapability": teLinkDescrSwitchingCapability,
       "teLinkDescrEncodingType": teLinkDescrEncodingType,
       "teLinkDescrMinLspBandwidth": teLinkDescrMinLspBandwidth,
       "teLinkDescrMaxLspBandwidthPrio0": teLinkDescrMaxLspBandwidthPrio0,
       "teLinkDescrMaxLspBandwidthPrio1": teLinkDescrMaxLspBandwidthPrio1,
       "teLinkDescrMaxLspBandwidthPrio2": teLinkDescrMaxLspBandwidthPrio2,
       "teLinkDescrMaxLspBandwidthPrio3": teLinkDescrMaxLspBandwidthPrio3,
       "teLinkDescrMaxLspBandwidthPrio4": teLinkDescrMaxLspBandwidthPrio4,
       "teLinkDescrMaxLspBandwidthPrio5": teLinkDescrMaxLspBandwidthPrio5,
       "teLinkDescrMaxLspBandwidthPrio6": teLinkDescrMaxLspBandwidthPrio6,
       "teLinkDescrMaxLspBandwidthPrio7": teLinkDescrMaxLspBandwidthPrio7,
       "teLinkDescrInterfaceMtu": teLinkDescrInterfaceMtu,
       "teLinkDescrIndication": teLinkDescrIndication,
       "teLinkDescrRowStatus": teLinkDescrRowStatus,
       "teLinkDescrStorageType": teLinkDescrStorageType,
       "teLinkSrlgTable": teLinkSrlgTable,
       "teLinkSrlgEntry": teLinkSrlgEntry,
       "teLinkSrlg": teLinkSrlg,
       "teLinkSrlgRowStatus": teLinkSrlgRowStatus,
       "teLinkSrlgStorageType": teLinkSrlgStorageType,
       "teLinkBandwidthTable": teLinkBandwidthTable,
       "teLinkBandwidthEntry": teLinkBandwidthEntry,
       "teLinkBandwidthPriority": teLinkBandwidthPriority,
       "teLinkBandwidthUnreserved": teLinkBandwidthUnreserved,
       "teLinkBandwidthRowStatus": teLinkBandwidthRowStatus,
       "teLinkBandwidthStorageType": teLinkBandwidthStorageType,
       "componentLinkTable": componentLinkTable,
       "componentLinkEntry": componentLinkEntry,
       "componentLinkMaxResBandwidth": componentLinkMaxResBandwidth,
       "componentLinkPreferredProtection": componentLinkPreferredProtection,
       "componentLinkCurrentProtection": componentLinkCurrentProtection,
       "componentLinkRowStatus": componentLinkRowStatus,
       "componentLinkStorageType": componentLinkStorageType,
       "componentLinkDescriptorTable": componentLinkDescriptorTable,
       "componentLinkDescriptorEntry": componentLinkDescriptorEntry,
       "componentLinkDescrId": componentLinkDescrId,
       "componentLinkDescrSwitchingCapability": componentLinkDescrSwitchingCapability,
       "componentLinkDescrEncodingType": componentLinkDescrEncodingType,
       "componentLinkDescrMinLspBandwidth": componentLinkDescrMinLspBandwidth,
       "componentLinkDescrMaxLspBandwidthPrio0": componentLinkDescrMaxLspBandwidthPrio0,
       "componentLinkDescrMaxLspBandwidthPrio1": componentLinkDescrMaxLspBandwidthPrio1,
       "componentLinkDescrMaxLspBandwidthPrio2": componentLinkDescrMaxLspBandwidthPrio2,
       "componentLinkDescrMaxLspBandwidthPrio3": componentLinkDescrMaxLspBandwidthPrio3,
       "componentLinkDescrMaxLspBandwidthPrio4": componentLinkDescrMaxLspBandwidthPrio4,
       "componentLinkDescrMaxLspBandwidthPrio5": componentLinkDescrMaxLspBandwidthPrio5,
       "componentLinkDescrMaxLspBandwidthPrio6": componentLinkDescrMaxLspBandwidthPrio6,
       "componentLinkDescrMaxLspBandwidthPrio7": componentLinkDescrMaxLspBandwidthPrio7,
       "componentLinkDescrInterfaceMtu": componentLinkDescrInterfaceMtu,
       "componentLinkDescrIndication": componentLinkDescrIndication,
       "componentLinkDescrRowStatus": componentLinkDescrRowStatus,
       "componentLinkDescrStorageType": componentLinkDescrStorageType,
       "componentLinkBandwidthTable": componentLinkBandwidthTable,
       "componentLinkBandwidthEntry": componentLinkBandwidthEntry,
       "componentLinkBandwidthPriority": componentLinkBandwidthPriority,
       "componentLinkBandwidthUnreserved": componentLinkBandwidthUnreserved,
       "componentLinkBandwidthRowStatus": componentLinkBandwidthRowStatus,
       "componentLinkBandwidthStorageType": componentLinkBandwidthStorageType,
       "teLinkConformance": teLinkConformance,
       "teLinkCompliances": teLinkCompliances,
       "teLinkModuleFullCompliance": teLinkModuleFullCompliance,
       "teLinkModuleReadOnlyCompliance": teLinkModuleReadOnlyCompliance,
       "teLinkGroups": teLinkGroups,
       "teLinkGroup": teLinkGroup,
       "teLinkSrlgGroup": teLinkSrlgGroup,
       "teLinkBandwidthGroup": teLinkBandwidthGroup,
       "componentLinkBandwidthGroup": componentLinkBandwidthGroup,
       "teLinkPscGroup": teLinkPscGroup,
       "teLinkTdmGroup": teLinkTdmGroup}
)
