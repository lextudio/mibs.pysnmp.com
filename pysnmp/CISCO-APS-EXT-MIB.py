# SNMP MIB module (CISCO-APS-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-APS-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:41 2024
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

(CApsK1K2,
 cApsChanConfigEntry,
 cApsChanStatusEntry,
 cApsConfigEntry,
 cApsStatusEntry) = mibBuilder.importSymbols(
    "CISCO-APS-MIB",
    "CApsK1K2",
    "cApsChanConfigEntry",
    "cApsChanStatusEntry",
    "cApsConfigEntry",
    "cApsStatusEntry")

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cApsExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 72)
)
cApsExtMIB.setRevisions(
        ("2003-01-31 00:00",
         "2002-05-31 00:00",
         "2002-05-20 00:00",
         "2001-05-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CdlApsBytes(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )



class CApsMessageTransport(Integer32, TextualConvention):
    status = "current"
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
        *(("apsChannel", 4),
          ("autoSelect", 2),
          ("dcc", 3),
          ("ip", 5),
          ("none", 1),
          ("osc", 6))
    )



class CApsChannelConfigNumber(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )



# MIB Managed Objects in the order of their OIDs

_CApsExtMIBObjects_ObjectIdentity = ObjectIdentity
cApsExtMIBObjects = _CApsExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 1)
)
_CApsNotifiesEnable_Type = TruthValue
_CApsNotifiesEnable_Object = MibScalar
cApsNotifiesEnable = _CApsNotifiesEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 1),
    _CApsNotifiesEnable_Type()
)
cApsNotifiesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cApsNotifiesEnable.setStatus("current")
_CApsConfigExtTable_Object = MibTable
cApsConfigExtTable = _CApsConfigExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2)
)
if mibBuilder.loadTexts:
    cApsConfigExtTable.setStatus("current")
_CApsConfigExtEntry_Object = MibTableRow
cApsConfigExtEntry = _CApsConfigExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cApsConfigExtEntry.setStatus("current")


class _CApsConfigSpan_Type(Integer32):
    """Custom type cApsConfigSpan based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("endToEnd", 2),
          ("hopByHop", 1))
    )


_CApsConfigSpan_Type.__name__ = "Integer32"
_CApsConfigSpan_Object = MibTableColumn
cApsConfigSpan = _CApsConfigSpan_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1, 1),
    _CApsConfigSpan_Type()
)
cApsConfigSpan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cApsConfigSpan.setStatus("current")


class _CApsConfigYcable_Type(Integer32):
    """Custom type cApsConfigYcable based on Integer32"""
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
        *(("noYcable", 1),
          ("ycable", 2),
          ("ycableXconnectCommon", 3))
    )


_CApsConfigYcable_Type.__name__ = "Integer32"
_CApsConfigYcable_Object = MibTableColumn
cApsConfigYcable = _CApsConfigYcable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1, 2),
    _CApsConfigYcable_Type()
)
cApsConfigYcable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cApsConfigYcable.setStatus("current")


class _CApsConfigMinSearchUpInterval_Type(Integer32):
    """Custom type cApsConfigMinSearchUpInterval based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_CApsConfigMinSearchUpInterval_Type.__name__ = "Integer32"
_CApsConfigMinSearchUpInterval_Object = MibTableColumn
cApsConfigMinSearchUpInterval = _CApsConfigMinSearchUpInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1, 3),
    _CApsConfigMinSearchUpInterval_Type()
)
cApsConfigMinSearchUpInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cApsConfigMinSearchUpInterval.setStatus("current")


class _CApsConfigMaxSearchUpInterval_Type(Integer32):
    """Custom type cApsConfigMaxSearchUpInterval based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_CApsConfigMaxSearchUpInterval_Type.__name__ = "Integer32"
_CApsConfigMaxSearchUpInterval_Object = MibTableColumn
cApsConfigMaxSearchUpInterval = _CApsConfigMaxSearchUpInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1, 4),
    _CApsConfigMaxSearchUpInterval_Type()
)
cApsConfigMaxSearchUpInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cApsConfigMaxSearchUpInterval.setStatus("current")
if mibBuilder.loadTexts:
    cApsConfigMaxSearchUpInterval.setUnits("seconds")


class _CApsConfigSwitchoverEnableInterval_Type(Integer32):
    """Custom type cApsConfigSwitchoverEnableInterval based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_CApsConfigSwitchoverEnableInterval_Type.__name__ = "Integer32"
_CApsConfigSwitchoverEnableInterval_Object = MibTableColumn
cApsConfigSwitchoverEnableInterval = _CApsConfigSwitchoverEnableInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1, 5),
    _CApsConfigSwitchoverEnableInterval_Type()
)
cApsConfigSwitchoverEnableInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cApsConfigSwitchoverEnableInterval.setStatus("current")
if mibBuilder.loadTexts:
    cApsConfigSwitchoverEnableInterval.setUnits("seconds")


class _CApsConfigMessageTransport_Type(CApsMessageTransport):
    """Custom type cApsConfigMessageTransport based on CApsMessageTransport"""


_CApsConfigMessageTransport_Object = MibTableColumn
cApsConfigMessageTransport = _CApsConfigMessageTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1, 6),
    _CApsConfigMessageTransport_Type()
)
cApsConfigMessageTransport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cApsConfigMessageTransport.setStatus("current")


class _CApsConfigMessageHolddown_Type(Integer32):
    """Custom type cApsConfigMessageHolddown based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_CApsConfigMessageHolddown_Type.__name__ = "Integer32"
_CApsConfigMessageHolddown_Object = MibTableColumn
cApsConfigMessageHolddown = _CApsConfigMessageHolddown_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1, 7),
    _CApsConfigMessageHolddown_Type()
)
cApsConfigMessageHolddown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cApsConfigMessageHolddown.setStatus("current")
if mibBuilder.loadTexts:
    cApsConfigMessageHolddown.setUnits("milliseconds")


class _CApsConfigMessageHolddownCount_Type(Integer32):
    """Custom type cApsConfigMessageHolddownCount based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_CApsConfigMessageHolddownCount_Type.__name__ = "Integer32"
_CApsConfigMessageHolddownCount_Object = MibTableColumn
cApsConfigMessageHolddownCount = _CApsConfigMessageHolddownCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1, 8),
    _CApsConfigMessageHolddownCount_Type()
)
cApsConfigMessageHolddownCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cApsConfigMessageHolddownCount.setStatus("current")


class _CApsConfigMessageMaxInterval_Type(Integer32):
    """Custom type cApsConfigMessageMaxInterval based on Integer32"""
    defaultValue = 15000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 120000),
    )


_CApsConfigMessageMaxInterval_Type.__name__ = "Integer32"
_CApsConfigMessageMaxInterval_Object = MibTableColumn
cApsConfigMessageMaxInterval = _CApsConfigMessageMaxInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1, 9),
    _CApsConfigMessageMaxInterval_Type()
)
cApsConfigMessageMaxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cApsConfigMessageMaxInterval.setStatus("current")
if mibBuilder.loadTexts:
    cApsConfigMessageMaxInterval.setUnits("milliseconds")


class _CApsConfigFarEndGroupName_Type(SnmpAdminString):
    """Custom type cApsConfigFarEndGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CApsConfigFarEndGroupName_Type.__name__ = "SnmpAdminString"
_CApsConfigFarEndGroupName_Object = MibTableColumn
cApsConfigFarEndGroupName = _CApsConfigFarEndGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1, 10),
    _CApsConfigFarEndGroupName_Type()
)
cApsConfigFarEndGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cApsConfigFarEndGroupName.setStatus("current")


class _CApsConfigFarEndIpAddressType_Type(InetAddressType):
    """Custom type cApsConfigFarEndIpAddressType based on InetAddressType"""


_CApsConfigFarEndIpAddressType_Object = MibTableColumn
cApsConfigFarEndIpAddressType = _CApsConfigFarEndIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1, 11),
    _CApsConfigFarEndIpAddressType_Type()
)
cApsConfigFarEndIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cApsConfigFarEndIpAddressType.setStatus("current")
_CApsConfigFarEndIpAddress_Type = InetAddress
_CApsConfigFarEndIpAddress_Object = MibTableColumn
cApsConfigFarEndIpAddress = _CApsConfigFarEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1, 12),
    _CApsConfigFarEndIpAddress_Type()
)
cApsConfigFarEndIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cApsConfigFarEndIpAddress.setStatus("current")
_CApsStatusExtTable_Object = MibTable
cApsStatusExtTable = _CApsStatusExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 3)
)
if mibBuilder.loadTexts:
    cApsStatusExtTable.setStatus("current")
_CApsStatusExtEntry_Object = MibTableRow
cApsStatusExtEntry = _CApsStatusExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cApsStatusExtEntry.setStatus("current")
_CApsStatusCdlApsBytesRcv_Type = CdlApsBytes
_CApsStatusCdlApsBytesRcv_Object = MibTableColumn
cApsStatusCdlApsBytesRcv = _CApsStatusCdlApsBytesRcv_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 3, 1, 1),
    _CApsStatusCdlApsBytesRcv_Type()
)
cApsStatusCdlApsBytesRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cApsStatusCdlApsBytesRcv.setStatus("current")
_CApsStatusCdlApsBytesTrans_Type = CdlApsBytes
_CApsStatusCdlApsBytesTrans_Object = MibTableColumn
cApsStatusCdlApsBytesTrans = _CApsStatusCdlApsBytesTrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 3, 1, 2),
    _CApsStatusCdlApsBytesTrans_Type()
)
cApsStatusCdlApsBytesTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cApsStatusCdlApsBytesTrans.setStatus("current")
_CApsStatusMessageTransport_Type = CApsMessageTransport
_CApsStatusMessageTransport_Object = MibTableColumn
cApsStatusMessageTransport = _CApsStatusMessageTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 3, 1, 3),
    _CApsStatusMessageTransport_Type()
)
cApsStatusMessageTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cApsStatusMessageTransport.setStatus("current")
_CApsChanStatusExtTable_Object = MibTable
cApsChanStatusExtTable = _CApsChanStatusExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 4)
)
if mibBuilder.loadTexts:
    cApsChanStatusExtTable.setStatus("current")
_CApsChanStatusExtEntry_Object = MibTableRow
cApsChanStatusExtEntry = _CApsChanStatusExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cApsChanStatusExtEntry.setStatus("current")
_CApsChanStatusExtRequest_Type = CApsK1K2
_CApsChanStatusExtRequest_Object = MibTableColumn
cApsChanStatusExtRequest = _CApsChanStatusExtRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 4, 1, 1),
    _CApsChanStatusExtRequest_Type()
)
cApsChanStatusExtRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cApsChanStatusExtRequest.setStatus("current")
_CApsChanConfigExtTable_Object = MibTable
cApsChanConfigExtTable = _CApsChanConfigExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 5)
)
if mibBuilder.loadTexts:
    cApsChanConfigExtTable.setStatus("current")
_CApsChanConfigExtEntry_Object = MibTableRow
cApsChanConfigExtEntry = _CApsChanConfigExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cApsChanConfigExtEntry.setStatus("current")
_CApsChanConfigReflectorMode_Type = TruthValue
_CApsChanConfigReflectorMode_Object = MibTableColumn
cApsChanConfigReflectorMode = _CApsChanConfigReflectorMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 5, 1, 1),
    _CApsChanConfigReflectorMode_Type()
)
cApsChanConfigReflectorMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cApsChanConfigReflectorMode.setStatus("current")
_CApsChanAssociationTable_Object = MibTable
cApsChanAssociationTable = _CApsChanAssociationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 6)
)
if mibBuilder.loadTexts:
    cApsChanAssociationTable.setStatus("current")
_CApsChanAssociationEntry_Object = MibTableRow
cApsChanAssociationEntry = _CApsChanAssociationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 6, 1)
)
cApsChanAssociationEntry.setIndexNames(
    (0, "CISCO-APS-EXT-MIB", "cApsChanAssociationGroupName"),
    (0, "CISCO-APS-EXT-MIB", "cApsChanAssociationNumber"),
    (0, "CISCO-APS-EXT-MIB", "cApsChanAssociationMapNumber"),
)
if mibBuilder.loadTexts:
    cApsChanAssociationEntry.setStatus("current")


class _CApsChanAssociationGroupName_Type(SnmpAdminString):
    """Custom type cApsChanAssociationGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CApsChanAssociationGroupName_Type.__name__ = "SnmpAdminString"
_CApsChanAssociationGroupName_Object = MibTableColumn
cApsChanAssociationGroupName = _CApsChanAssociationGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 6, 1, 1),
    _CApsChanAssociationGroupName_Type()
)
cApsChanAssociationGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cApsChanAssociationGroupName.setStatus("current")
_CApsChanAssociationNumber_Type = CApsChannelConfigNumber
_CApsChanAssociationNumber_Object = MibTableColumn
cApsChanAssociationNumber = _CApsChanAssociationNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 6, 1, 2),
    _CApsChanAssociationNumber_Type()
)
cApsChanAssociationNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cApsChanAssociationNumber.setStatus("current")
_CApsChanAssociationMapNumber_Type = CApsChannelConfigNumber
_CApsChanAssociationMapNumber_Object = MibTableColumn
cApsChanAssociationMapNumber = _CApsChanAssociationMapNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 6, 1, 3),
    _CApsChanAssociationMapNumber_Type()
)
cApsChanAssociationMapNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cApsChanAssociationMapNumber.setStatus("current")
_CApsChanAssociationIpAddressType_Type = InetAddressType
_CApsChanAssociationIpAddressType_Object = MibTableColumn
cApsChanAssociationIpAddressType = _CApsChanAssociationIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 6, 1, 4),
    _CApsChanAssociationIpAddressType_Type()
)
cApsChanAssociationIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cApsChanAssociationIpAddressType.setStatus("current")
_CApsChanAssociationIpAddress_Type = InetAddress
_CApsChanAssociationIpAddress_Object = MibTableColumn
cApsChanAssociationIpAddress = _CApsChanAssociationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 6, 1, 5),
    _CApsChanAssociationIpAddress_Type()
)
cApsChanAssociationIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cApsChanAssociationIpAddress.setStatus("current")
_CApsExtMIBConformance_ObjectIdentity = ObjectIdentity
cApsExtMIBConformance = _CApsExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 2)
)
_CApsExtGroups_ObjectIdentity = ObjectIdentity
cApsExtGroups = _CApsExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1)
)
_CApsExtCompliances_ObjectIdentity = ObjectIdentity
cApsExtCompliances = _CApsExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 2)
)
cApsConfigEntry.registerAugmentions(
    ("CISCO-APS-EXT-MIB",
     "cApsConfigExtEntry")
)
cApsConfigExtEntry.setIndexNames(*cApsConfigEntry.getIndexNames())
cApsStatusEntry.registerAugmentions(
    ("CISCO-APS-EXT-MIB",
     "cApsStatusExtEntry")
)
cApsStatusExtEntry.setIndexNames(*cApsStatusEntry.getIndexNames())
cApsChanStatusEntry.registerAugmentions(
    ("CISCO-APS-EXT-MIB",
     "cApsChanStatusExtEntry")
)
cApsChanStatusExtEntry.setIndexNames(*cApsChanStatusEntry.getIndexNames())
cApsChanConfigEntry.registerAugmentions(
    ("CISCO-APS-EXT-MIB",
     "cApsChanConfigExtEntry")
)
cApsChanConfigExtEntry.setIndexNames(*cApsChanConfigEntry.getIndexNames())

# Managed Objects groups

cApsNotifiesEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1, 1)
)
cApsNotifiesEnableGroup.setObjects(
    ("CISCO-APS-EXT-MIB", "cApsNotifiesEnable")
)
if mibBuilder.loadTexts:
    cApsNotifiesEnableGroup.setStatus("current")

cApsConfigPathExt = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1, 2)
)
cApsConfigPathExt.setObjects(
    ("CISCO-APS-EXT-MIB", "cApsConfigSpan")
)
if mibBuilder.loadTexts:
    cApsConfigPathExt.setStatus("current")

cApsConfigYcableExt = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1, 3)
)
cApsConfigYcableExt.setObjects(
    ("CISCO-APS-EXT-MIB", "cApsConfigYcable")
)
if mibBuilder.loadTexts:
    cApsConfigYcableExt.setStatus("current")

cApsConfigSearchExt = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1, 4)
)
cApsConfigSearchExt.setObjects(
      *(("CISCO-APS-EXT-MIB", "cApsConfigMinSearchUpInterval"),
        ("CISCO-APS-EXT-MIB", "cApsConfigMaxSearchUpInterval"))
)
if mibBuilder.loadTexts:
    cApsConfigSearchExt.setStatus("current")

cApsStatusCdlExt = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1, 5)
)
cApsStatusCdlExt.setObjects(
      *(("CISCO-APS-EXT-MIB", "cApsStatusCdlApsBytesRcv"),
        ("CISCO-APS-EXT-MIB", "cApsStatusCdlApsBytesTrans"))
)
if mibBuilder.loadTexts:
    cApsStatusCdlExt.setStatus("current")

cApsConfigSwitchoverTimerExt = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1, 6)
)
cApsConfigSwitchoverTimerExt.setObjects(
    ("CISCO-APS-EXT-MIB", "cApsConfigSwitchoverEnableInterval")
)
if mibBuilder.loadTexts:
    cApsConfigSwitchoverTimerExt.setStatus("current")

cApsConfigMessageExt = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1, 7)
)
cApsConfigMessageExt.setObjects(
      *(("CISCO-APS-EXT-MIB", "cApsConfigMessageTransport"),
        ("CISCO-APS-EXT-MIB", "cApsConfigMessageHolddown"),
        ("CISCO-APS-EXT-MIB", "cApsConfigMessageHolddownCount"),
        ("CISCO-APS-EXT-MIB", "cApsConfigMessageMaxInterval"),
        ("CISCO-APS-EXT-MIB", "cApsConfigFarEndGroupName"))
)
if mibBuilder.loadTexts:
    cApsConfigMessageExt.setStatus("current")

cApsConfigIPExt = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1, 8)
)
cApsConfigIPExt.setObjects(
      *(("CISCO-APS-EXT-MIB", "cApsConfigFarEndIpAddressType"),
        ("CISCO-APS-EXT-MIB", "cApsConfigFarEndIpAddress"))
)
if mibBuilder.loadTexts:
    cApsConfigIPExt.setStatus("current")

cApsStatusMessageExt = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1, 9)
)
cApsStatusMessageExt.setObjects(
    ("CISCO-APS-EXT-MIB", "cApsStatusMessageTransport")
)
if mibBuilder.loadTexts:
    cApsStatusMessageExt.setStatus("current")

cApsChanStatusRequestExt = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1, 10)
)
cApsChanStatusRequestExt.setObjects(
    ("CISCO-APS-EXT-MIB", "cApsChanStatusExtRequest")
)
if mibBuilder.loadTexts:
    cApsChanStatusRequestExt.setStatus("current")

cApsChanConfigExt = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1, 11)
)
cApsChanConfigExt.setObjects(
    ("CISCO-APS-EXT-MIB", "cApsChanConfigReflectorMode")
)
if mibBuilder.loadTexts:
    cApsChanConfigExt.setStatus("current")

cApsChanAssociationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1, 12)
)
cApsChanAssociationGroup.setObjects(
      *(("CISCO-APS-EXT-MIB", "cApsChanAssociationIpAddressType"),
        ("CISCO-APS-EXT-MIB", "cApsChanAssociationIpAddress"))
)
if mibBuilder.loadTexts:
    cApsChanAssociationGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cApsExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cApsExtCompliance.setStatus(
        "deprecated"
    )

cApsExtCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 2, 2)
)
if mibBuilder.loadTexts:
    cApsExtCompliance2.setStatus(
        "current"
    )

cApsExtComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 2, 3)
)
if mibBuilder.loadTexts:
    cApsExtComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-APS-EXT-MIB",
    **{"CdlApsBytes": CdlApsBytes,
       "CApsMessageTransport": CApsMessageTransport,
       "CApsChannelConfigNumber": CApsChannelConfigNumber,
       "cApsExtMIB": cApsExtMIB,
       "cApsExtMIBObjects": cApsExtMIBObjects,
       "cApsNotifiesEnable": cApsNotifiesEnable,
       "cApsConfigExtTable": cApsConfigExtTable,
       "cApsConfigExtEntry": cApsConfigExtEntry,
       "cApsConfigSpan": cApsConfigSpan,
       "cApsConfigYcable": cApsConfigYcable,
       "cApsConfigMinSearchUpInterval": cApsConfigMinSearchUpInterval,
       "cApsConfigMaxSearchUpInterval": cApsConfigMaxSearchUpInterval,
       "cApsConfigSwitchoverEnableInterval": cApsConfigSwitchoverEnableInterval,
       "cApsConfigMessageTransport": cApsConfigMessageTransport,
       "cApsConfigMessageHolddown": cApsConfigMessageHolddown,
       "cApsConfigMessageHolddownCount": cApsConfigMessageHolddownCount,
       "cApsConfigMessageMaxInterval": cApsConfigMessageMaxInterval,
       "cApsConfigFarEndGroupName": cApsConfigFarEndGroupName,
       "cApsConfigFarEndIpAddressType": cApsConfigFarEndIpAddressType,
       "cApsConfigFarEndIpAddress": cApsConfigFarEndIpAddress,
       "cApsStatusExtTable": cApsStatusExtTable,
       "cApsStatusExtEntry": cApsStatusExtEntry,
       "cApsStatusCdlApsBytesRcv": cApsStatusCdlApsBytesRcv,
       "cApsStatusCdlApsBytesTrans": cApsStatusCdlApsBytesTrans,
       "cApsStatusMessageTransport": cApsStatusMessageTransport,
       "cApsChanStatusExtTable": cApsChanStatusExtTable,
       "cApsChanStatusExtEntry": cApsChanStatusExtEntry,
       "cApsChanStatusExtRequest": cApsChanStatusExtRequest,
       "cApsChanConfigExtTable": cApsChanConfigExtTable,
       "cApsChanConfigExtEntry": cApsChanConfigExtEntry,
       "cApsChanConfigReflectorMode": cApsChanConfigReflectorMode,
       "cApsChanAssociationTable": cApsChanAssociationTable,
       "cApsChanAssociationEntry": cApsChanAssociationEntry,
       "cApsChanAssociationGroupName": cApsChanAssociationGroupName,
       "cApsChanAssociationNumber": cApsChanAssociationNumber,
       "cApsChanAssociationMapNumber": cApsChanAssociationMapNumber,
       "cApsChanAssociationIpAddressType": cApsChanAssociationIpAddressType,
       "cApsChanAssociationIpAddress": cApsChanAssociationIpAddress,
       "cApsExtMIBConformance": cApsExtMIBConformance,
       "cApsExtGroups": cApsExtGroups,
       "cApsNotifiesEnableGroup": cApsNotifiesEnableGroup,
       "cApsConfigPathExt": cApsConfigPathExt,
       "cApsConfigYcableExt": cApsConfigYcableExt,
       "cApsConfigSearchExt": cApsConfigSearchExt,
       "cApsStatusCdlExt": cApsStatusCdlExt,
       "cApsConfigSwitchoverTimerExt": cApsConfigSwitchoverTimerExt,
       "cApsConfigMessageExt": cApsConfigMessageExt,
       "cApsConfigIPExt": cApsConfigIPExt,
       "cApsStatusMessageExt": cApsStatusMessageExt,
       "cApsChanStatusRequestExt": cApsChanStatusRequestExt,
       "cApsChanConfigExt": cApsChanConfigExt,
       "cApsChanAssociationGroup": cApsChanAssociationGroup,
       "cApsExtCompliances": cApsExtCompliances,
       "cApsExtCompliance": cApsExtCompliance,
       "cApsExtCompliance2": cApsExtCompliance2,
       "cApsExtComplianceRev1": cApsExtComplianceRev1}
)
