# SNMP MIB module (CISCO-PACKET-CAPTURE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-PACKET-CAPTURE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:38 2024
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

(VlanIndex,) = mibBuilder.importSymbols(
    "CISCO-VTP-MIB",
    "VlanIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoPacketCaptureMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 602)
)
ciscoPacketCaptureMIB.setRevisions(
        ("2008-07-07 00:00",
         "2007-01-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoPacketCaptureFilterCriteria(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dest", 2),
          ("source", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CpcMIBNotification_ObjectIdentity = ObjectIdentity
cpcMIBNotification = _CpcMIBNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 0)
)
_CpcMIBObjects_ObjectIdentity = ObjectIdentity
cpcMIBObjects = _CpcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1)
)
_CpcGenericConfig_ObjectIdentity = ObjectIdentity
cpcGenericConfig = _CpcGenericConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 1)
)
_CpcMaxSessionAllowed_Type = Unsigned32
_CpcMaxSessionAllowed_Object = MibScalar
cpcMaxSessionAllowed = _CpcMaxSessionAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 1, 1),
    _CpcMaxSessionAllowed_Type()
)
cpcMaxSessionAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpcMaxSessionAllowed.setStatus("current")
_CpcSessionConfigTable_Object = MibTable
cpcSessionConfigTable = _CpcSessionConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cpcSessionConfigTable.setStatus("current")
_CpcSessionConfigEntry_Object = MibTableRow
cpcSessionConfigEntry = _CpcSessionConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 1, 2, 1)
)
cpcSessionConfigEntry.setIndexNames(
    (0, "CISCO-PACKET-CAPTURE-MIB", "cpcSessionId"),
)
if mibBuilder.loadTexts:
    cpcSessionConfigEntry.setStatus("current")


class _CpcSessionId_Type(Unsigned32):
    """Custom type cpcSessionId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CpcSessionId_Type.__name__ = "Unsigned32"
_CpcSessionId_Object = MibTableColumn
cpcSessionId = _CpcSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 1, 2, 1, 1),
    _CpcSessionId_Type()
)
cpcSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpcSessionId.setStatus("current")


class _CpcSessionOperStatus_Type(Integer32):
    """Custom type cpcSessionOperStatus based on Integer32"""
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
        *(("bufferFull", 6),
          ("completed", 3),
          ("inProgress", 2),
          ("other", 1),
          ("stopped", 4),
          ("storageFull", 5))
    )


_CpcSessionOperStatus_Type.__name__ = "Integer32"
_CpcSessionOperStatus_Object = MibTableColumn
cpcSessionOperStatus = _CpcSessionOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 1, 2, 1, 2),
    _CpcSessionOperStatus_Type()
)
cpcSessionOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpcSessionOperStatus.setStatus("current")
_CpcSessionDestFileName_Type = SnmpAdminString
_CpcSessionDestFileName_Object = MibTableColumn
cpcSessionDestFileName = _CpcSessionDestFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 1, 2, 1, 3),
    _CpcSessionDestFileName_Type()
)
cpcSessionDestFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpcSessionDestFileName.setStatus("current")


class _CpcSessionPacketLength_Type(Unsigned32):
    """Custom type cpcSessionPacketLength based on Unsigned32"""
    defaultValue = 0


_CpcSessionPacketLength_Object = MibTableColumn
cpcSessionPacketLength = _CpcSessionPacketLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 1, 2, 1, 4),
    _CpcSessionPacketLength_Type()
)
cpcSessionPacketLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpcSessionPacketLength.setStatus("current")
if mibBuilder.loadTexts:
    cpcSessionPacketLength.setUnits("octets")


class _CpcSessionPacketLimits_Type(Unsigned32):
    """Custom type cpcSessionPacketLimits based on Unsigned32"""
    defaultValue = 0


_CpcSessionPacketLimits_Object = MibTableColumn
cpcSessionPacketLimits = _CpcSessionPacketLimits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 1, 2, 1, 5),
    _CpcSessionPacketLimits_Type()
)
cpcSessionPacketLimits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpcSessionPacketLimits.setStatus("current")
if mibBuilder.loadTexts:
    cpcSessionPacketLimits.setUnits("packets")


class _CpcSessionAction_Type(Integer32):
    """Custom type cpcSessionAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_CpcSessionAction_Type.__name__ = "Integer32"
_CpcSessionAction_Object = MibTableColumn
cpcSessionAction = _CpcSessionAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 1, 2, 1, 6),
    _CpcSessionAction_Type()
)
cpcSessionAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpcSessionAction.setStatus("current")
_CpcSessionConfigStatus_Type = RowStatus
_CpcSessionConfigStatus_Object = MibTableColumn
cpcSessionConfigStatus = _CpcSessionConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 1, 2, 1, 7),
    _CpcSessionConfigStatus_Type()
)
cpcSessionConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpcSessionConfigStatus.setStatus("current")


class _CpcSessionPacketRateLimit_Type(Unsigned32):
    """Custom type cpcSessionPacketRateLimit based on Unsigned32"""
    defaultValue = 10000


_CpcSessionPacketRateLimit_Object = MibTableColumn
cpcSessionPacketRateLimit = _CpcSessionPacketRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 1, 2, 1, 8),
    _CpcSessionPacketRateLimit_Type()
)
cpcSessionPacketRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpcSessionPacketRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    cpcSessionPacketRateLimit.setUnits("packets per second")
_CpcSessionDescr_Type = SnmpAdminString
_CpcSessionDescr_Object = MibTableColumn
cpcSessionDescr = _CpcSessionDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 1, 2, 1, 9),
    _CpcSessionDescr_Type()
)
cpcSessionDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpcSessionDescr.setStatus("current")
_CpcSessionMaxSources_Type = Unsigned32
_CpcSessionMaxSources_Object = MibScalar
cpcSessionMaxSources = _CpcSessionMaxSources_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 1, 3),
    _CpcSessionMaxSources_Type()
)
cpcSessionMaxSources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpcSessionMaxSources.setStatus("current")
_CpcCaptureSourceIfTable_Object = MibTable
cpcCaptureSourceIfTable = _CpcCaptureSourceIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cpcCaptureSourceIfTable.setStatus("current")
_CpcCaptureSourceIfEntry_Object = MibTableRow
cpcCaptureSourceIfEntry = _CpcCaptureSourceIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 1, 4, 1)
)
cpcCaptureSourceIfEntry.setIndexNames(
    (0, "CISCO-PACKET-CAPTURE-MIB", "cpcSessionId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cpcCaptureSourceIfEntry.setStatus("current")


class _CpcCaptureSourceIfDirection_Type(Integer32):
    """Custom type cpcCaptureSourceIfDirection based on Integer32"""
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
        *(("both", 3),
          ("rx", 1),
          ("tx", 2))
    )


_CpcCaptureSourceIfDirection_Type.__name__ = "Integer32"
_CpcCaptureSourceIfDirection_Object = MibTableColumn
cpcCaptureSourceIfDirection = _CpcCaptureSourceIfDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 1, 4, 1, 1),
    _CpcCaptureSourceIfDirection_Type()
)
cpcCaptureSourceIfDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpcCaptureSourceIfDirection.setStatus("current")
_CpcCaptureSourceIfStatus_Type = RowStatus
_CpcCaptureSourceIfStatus_Object = MibTableColumn
cpcCaptureSourceIfStatus = _CpcCaptureSourceIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 1, 4, 1, 2),
    _CpcCaptureSourceIfStatus_Type()
)
cpcCaptureSourceIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpcCaptureSourceIfStatus.setStatus("current")
_CpcFilterConfig_ObjectIdentity = ObjectIdentity
cpcFilterConfig = _CpcFilterConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 2)
)
_CpcMaxFilterAllowed_Type = Unsigned32
_CpcMaxFilterAllowed_Object = MibScalar
cpcMaxFilterAllowed = _CpcMaxFilterAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 2, 1),
    _CpcMaxFilterAllowed_Type()
)
cpcMaxFilterAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpcMaxFilterAllowed.setStatus("current")
_CpcMacFilterTable_Object = MibTable
cpcMacFilterTable = _CpcMacFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cpcMacFilterTable.setStatus("current")
_CpcMacFilterEntry_Object = MibTableRow
cpcMacFilterEntry = _CpcMacFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 2, 2, 1)
)
cpcMacFilterEntry.setIndexNames(
    (0, "CISCO-PACKET-CAPTURE-MIB", "cpcSessionId"),
    (0, "CISCO-PACKET-CAPTURE-MIB", "cpcMacFilterMacAddress"),
    (0, "CISCO-PACKET-CAPTURE-MIB", "cpcMacFilterCriteria"),
)
if mibBuilder.loadTexts:
    cpcMacFilterEntry.setStatus("current")
_CpcMacFilterMacAddress_Type = MacAddress
_CpcMacFilterMacAddress_Object = MibTableColumn
cpcMacFilterMacAddress = _CpcMacFilterMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 2, 2, 1, 1),
    _CpcMacFilterMacAddress_Type()
)
cpcMacFilterMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpcMacFilterMacAddress.setStatus("current")
_CpcMacFilterCriteria_Type = CiscoPacketCaptureFilterCriteria
_CpcMacFilterCriteria_Object = MibTableColumn
cpcMacFilterCriteria = _CpcMacFilterCriteria_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 2, 2, 1, 2),
    _CpcMacFilterCriteria_Type()
)
cpcMacFilterCriteria.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpcMacFilterCriteria.setStatus("current")
_CpcMacFilterRowStatus_Type = RowStatus
_CpcMacFilterRowStatus_Object = MibTableColumn
cpcMacFilterRowStatus = _CpcMacFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 2, 2, 1, 3),
    _CpcMacFilterRowStatus_Type()
)
cpcMacFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpcMacFilterRowStatus.setStatus("current")
_CpcIpFilterTable_Object = MibTable
cpcIpFilterTable = _CpcIpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cpcIpFilterTable.setStatus("current")
_CpcIpFilterEntry_Object = MibTableRow
cpcIpFilterEntry = _CpcIpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 2, 3, 1)
)
cpcIpFilterEntry.setIndexNames(
    (0, "CISCO-PACKET-CAPTURE-MIB", "cpcSessionId"),
    (0, "CISCO-PACKET-CAPTURE-MIB", "cpcIpFilterAddressType"),
    (0, "CISCO-PACKET-CAPTURE-MIB", "cpcIpFilterAddress"),
    (0, "CISCO-PACKET-CAPTURE-MIB", "cpcIpFilterCriteria"),
)
if mibBuilder.loadTexts:
    cpcIpFilterEntry.setStatus("current")
_CpcIpFilterAddressType_Type = InetAddressType
_CpcIpFilterAddressType_Object = MibTableColumn
cpcIpFilterAddressType = _CpcIpFilterAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 2, 3, 1, 1),
    _CpcIpFilterAddressType_Type()
)
cpcIpFilterAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpcIpFilterAddressType.setStatus("current")


class _CpcIpFilterAddress_Type(InetAddress):
    """Custom type cpcIpFilterAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CpcIpFilterAddress_Type.__name__ = "InetAddress"
_CpcIpFilterAddress_Object = MibTableColumn
cpcIpFilterAddress = _CpcIpFilterAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 2, 3, 1, 2),
    _CpcIpFilterAddress_Type()
)
cpcIpFilterAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpcIpFilterAddress.setStatus("current")
_CpcIpFilterCriteria_Type = CiscoPacketCaptureFilterCriteria
_CpcIpFilterCriteria_Object = MibTableColumn
cpcIpFilterCriteria = _CpcIpFilterCriteria_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 2, 3, 1, 3),
    _CpcIpFilterCriteria_Type()
)
cpcIpFilterCriteria.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpcIpFilterCriteria.setStatus("current")
_CpcIpFilterMask_Type = InetAddressPrefixLength
_CpcIpFilterMask_Object = MibTableColumn
cpcIpFilterMask = _CpcIpFilterMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 2, 3, 1, 4),
    _CpcIpFilterMask_Type()
)
cpcIpFilterMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpcIpFilterMask.setStatus("current")
_CpcIpFilterRowStatus_Type = RowStatus
_CpcIpFilterRowStatus_Object = MibTableColumn
cpcIpFilterRowStatus = _CpcIpFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 2, 3, 1, 5),
    _CpcIpFilterRowStatus_Type()
)
cpcIpFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpcIpFilterRowStatus.setStatus("current")
_CpcMaxMacFilterAllowed_Type = Unsigned32
_CpcMaxMacFilterAllowed_Object = MibScalar
cpcMaxMacFilterAllowed = _CpcMaxMacFilterAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 2, 4),
    _CpcMaxMacFilterAllowed_Type()
)
cpcMaxMacFilterAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpcMaxMacFilterAllowed.setStatus("current")
_CpcMaxIpFilterAllowed_Type = Unsigned32
_CpcMaxIpFilterAllowed_Object = MibScalar
cpcMaxIpFilterAllowed = _CpcMaxIpFilterAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 2, 5),
    _CpcMaxIpFilterAllowed_Type()
)
cpcMaxIpFilterAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpcMaxIpFilterAllowed.setStatus("current")
_CpcPacketLengthFilterTable_Object = MibTable
cpcPacketLengthFilterTable = _CpcPacketLengthFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 2, 6)
)
if mibBuilder.loadTexts:
    cpcPacketLengthFilterTable.setStatus("current")
_CpcPacketLengthFilterEntry_Object = MibTableRow
cpcPacketLengthFilterEntry = _CpcPacketLengthFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 2, 6, 1)
)
cpcPacketLengthFilterEntry.setIndexNames(
    (0, "CISCO-PACKET-CAPTURE-MIB", "cpcSessionId"),
)
if mibBuilder.loadTexts:
    cpcPacketLengthFilterEntry.setStatus("current")
_CpcPacketLengthFilterMin_Type = Unsigned32
_CpcPacketLengthFilterMin_Object = MibTableColumn
cpcPacketLengthFilterMin = _CpcPacketLengthFilterMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 2, 6, 1, 1),
    _CpcPacketLengthFilterMin_Type()
)
cpcPacketLengthFilterMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpcPacketLengthFilterMin.setStatus("current")
if mibBuilder.loadTexts:
    cpcPacketLengthFilterMin.setUnits("bytes")
_CpcPacketLengthFilterMax_Type = Unsigned32
_CpcPacketLengthFilterMax_Object = MibTableColumn
cpcPacketLengthFilterMax = _CpcPacketLengthFilterMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 2, 6, 1, 2),
    _CpcPacketLengthFilterMax_Type()
)
cpcPacketLengthFilterMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpcPacketLengthFilterMax.setStatus("current")
if mibBuilder.loadTexts:
    cpcPacketLengthFilterMax.setUnits("bytes")
_CpcMaxEthertypeFilterAllowed_Type = Unsigned32
_CpcMaxEthertypeFilterAllowed_Object = MibScalar
cpcMaxEthertypeFilterAllowed = _CpcMaxEthertypeFilterAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 2, 7),
    _CpcMaxEthertypeFilterAllowed_Type()
)
cpcMaxEthertypeFilterAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpcMaxEthertypeFilterAllowed.setStatus("current")
_CpcEthertypeFilterTable_Object = MibTable
cpcEthertypeFilterTable = _CpcEthertypeFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 2, 8)
)
if mibBuilder.loadTexts:
    cpcEthertypeFilterTable.setStatus("current")
_CpcEthertypeFilterEntry_Object = MibTableRow
cpcEthertypeFilterEntry = _CpcEthertypeFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 2, 8, 1)
)
cpcEthertypeFilterEntry.setIndexNames(
    (0, "CISCO-PACKET-CAPTURE-MIB", "cpcSessionId"),
    (0, "CISCO-PACKET-CAPTURE-MIB", "cpcEthertypeFilterValue"),
)
if mibBuilder.loadTexts:
    cpcEthertypeFilterEntry.setStatus("current")


class _CpcEthertypeFilterValue_Type(Integer32):
    """Custom type cpcEthertypeFilterValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpcEthertypeFilterValue_Type.__name__ = "Integer32"
_CpcEthertypeFilterValue_Object = MibTableColumn
cpcEthertypeFilterValue = _CpcEthertypeFilterValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 2, 8, 1, 1),
    _CpcEthertypeFilterValue_Type()
)
cpcEthertypeFilterValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpcEthertypeFilterValue.setStatus("current")
_CpcEthertypeFilterStatus_Type = RowStatus
_CpcEthertypeFilterStatus_Object = MibTableColumn
cpcEthertypeFilterStatus = _CpcEthertypeFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 2, 8, 1, 2),
    _CpcEthertypeFilterStatus_Type()
)
cpcEthertypeFilterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpcEthertypeFilterStatus.setStatus("current")
_CpcMaxVlanFilterAllowed_Type = Unsigned32
_CpcMaxVlanFilterAllowed_Object = MibScalar
cpcMaxVlanFilterAllowed = _CpcMaxVlanFilterAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 2, 9),
    _CpcMaxVlanFilterAllowed_Type()
)
cpcMaxVlanFilterAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpcMaxVlanFilterAllowed.setStatus("current")
_CpcVlanFilterTable_Object = MibTable
cpcVlanFilterTable = _CpcVlanFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 2, 10)
)
if mibBuilder.loadTexts:
    cpcVlanFilterTable.setStatus("current")
_CpcVlanFilterEntry_Object = MibTableRow
cpcVlanFilterEntry = _CpcVlanFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 2, 10, 1)
)
cpcVlanFilterEntry.setIndexNames(
    (0, "CISCO-PACKET-CAPTURE-MIB", "cpcSessionId"),
    (0, "CISCO-PACKET-CAPTURE-MIB", "cpcVlanFilterVlanIndex"),
)
if mibBuilder.loadTexts:
    cpcVlanFilterEntry.setStatus("current")
_CpcVlanFilterVlanIndex_Type = VlanIndex
_CpcVlanFilterVlanIndex_Object = MibTableColumn
cpcVlanFilterVlanIndex = _CpcVlanFilterVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 2, 10, 1, 1),
    _CpcVlanFilterVlanIndex_Type()
)
cpcVlanFilterVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpcVlanFilterVlanIndex.setStatus("current")
_CpcVlanFilterRowStatus_Type = RowStatus
_CpcVlanFilterRowStatus_Object = MibTableColumn
cpcVlanFilterRowStatus = _CpcVlanFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 2, 10, 1, 2),
    _CpcVlanFilterRowStatus_Type()
)
cpcVlanFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpcVlanFilterRowStatus.setStatus("current")
_CpcMaxAccessGroupFilterAllowed_Type = Unsigned32
_CpcMaxAccessGroupFilterAllowed_Object = MibScalar
cpcMaxAccessGroupFilterAllowed = _CpcMaxAccessGroupFilterAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 2, 11),
    _CpcMaxAccessGroupFilterAllowed_Type()
)
cpcMaxAccessGroupFilterAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpcMaxAccessGroupFilterAllowed.setStatus("current")
_CpcAccessGroupFilterTable_Object = MibTable
cpcAccessGroupFilterTable = _CpcAccessGroupFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 2, 12)
)
if mibBuilder.loadTexts:
    cpcAccessGroupFilterTable.setStatus("current")
_CpcAccessGroupFilterEntry_Object = MibTableRow
cpcAccessGroupFilterEntry = _CpcAccessGroupFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 2, 12, 1)
)
cpcAccessGroupFilterEntry.setIndexNames(
    (0, "CISCO-PACKET-CAPTURE-MIB", "cpcSessionId"),
    (0, "CISCO-PACKET-CAPTURE-MIB", "cpcAccessGroupFilterType"),
    (1, "CISCO-PACKET-CAPTURE-MIB", "cpcAccessGroupFilterName"),
)
if mibBuilder.loadTexts:
    cpcAccessGroupFilterEntry.setStatus("current")


class _CpcAccessGroupFilterType_Type(Integer32):
    """Custom type cpcAccessGroupFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 1),
          ("software", 2))
    )


_CpcAccessGroupFilterType_Type.__name__ = "Integer32"
_CpcAccessGroupFilterType_Object = MibTableColumn
cpcAccessGroupFilterType = _CpcAccessGroupFilterType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 2, 12, 1, 1),
    _CpcAccessGroupFilterType_Type()
)
cpcAccessGroupFilterType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpcAccessGroupFilterType.setStatus("current")


class _CpcAccessGroupFilterName_Type(SnmpAdminString):
    """Custom type cpcAccessGroupFilterName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 99),
    )


_CpcAccessGroupFilterName_Type.__name__ = "SnmpAdminString"
_CpcAccessGroupFilterName_Object = MibTableColumn
cpcAccessGroupFilterName = _CpcAccessGroupFilterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 2, 12, 1, 2),
    _CpcAccessGroupFilterName_Type()
)
cpcAccessGroupFilterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpcAccessGroupFilterName.setStatus("current")
_CpcAccessGroupFilterStatus_Type = RowStatus
_CpcAccessGroupFilterStatus_Object = MibTableColumn
cpcAccessGroupFilterStatus = _CpcAccessGroupFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 2, 12, 1, 3),
    _CpcAccessGroupFilterStatus_Type()
)
cpcAccessGroupFilterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpcAccessGroupFilterStatus.setStatus("current")
_CpcBufferConfig_ObjectIdentity = ObjectIdentity
cpcBufferConfig = _CpcBufferConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 3)
)
_CpcBufferConfigTable_Object = MibTable
cpcBufferConfigTable = _CpcBufferConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cpcBufferConfigTable.setStatus("current")
_CpcBufferConfigEntry_Object = MibTableRow
cpcBufferConfigEntry = _CpcBufferConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 3, 1, 1)
)
cpcBufferConfigEntry.setIndexNames(
    (0, "CISCO-PACKET-CAPTURE-MIB", "cpcSessionId"),
)
if mibBuilder.loadTexts:
    cpcBufferConfigEntry.setStatus("current")


class _CpcBufferType_Type(Integer32):
    """Custom type cpcBufferType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("circular", 2),
          ("linear", 1))
    )


_CpcBufferType_Type.__name__ = "Integer32"
_CpcBufferType_Object = MibTableColumn
cpcBufferType = _CpcBufferType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 3, 1, 1, 1),
    _CpcBufferType_Type()
)
cpcBufferType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpcBufferType.setStatus("current")
_CpcBufferSize_Type = Unsigned32
_CpcBufferSize_Object = MibTableColumn
cpcBufferSize = _CpcBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 3, 1, 1, 2),
    _CpcBufferSize_Type()
)
cpcBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpcBufferSize.setStatus("current")
if mibBuilder.loadTexts:
    cpcBufferSize.setUnits("Kilo-bytes")


class _CpcBufferAction_Type(Integer32):
    """Custom type cpcBufferAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("export", 3),
          ("noAction", 1))
    )


_CpcBufferAction_Type.__name__ = "Integer32"
_CpcBufferAction_Object = MibTableColumn
cpcBufferAction = _CpcBufferAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 3, 1, 1, 3),
    _CpcBufferAction_Type()
)
cpcBufferAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpcBufferAction.setStatus("current")


class _CpcBufferOperStatus_Type(Integer32):
    """Custom type cpcBufferOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exporting", 2),
          ("other", 1))
    )


_CpcBufferOperStatus_Type.__name__ = "Integer32"
_CpcBufferOperStatus_Object = MibTableColumn
cpcBufferOperStatus = _CpcBufferOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 3, 1, 1, 4),
    _CpcBufferOperStatus_Type()
)
cpcBufferOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpcBufferOperStatus.setStatus("current")
_CpcScheduleConfig_ObjectIdentity = ObjectIdentity
cpcScheduleConfig = _CpcScheduleConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 4)
)
_CpcScheduleConfigTable_Object = MibTable
cpcScheduleConfigTable = _CpcScheduleConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cpcScheduleConfigTable.setStatus("current")
_CpcScheduleConfigEntry_Object = MibTableRow
cpcScheduleConfigEntry = _CpcScheduleConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 4, 1, 1)
)
cpcScheduleConfigEntry.setIndexNames(
    (0, "CISCO-PACKET-CAPTURE-MIB", "cpcSessionId"),
)
if mibBuilder.loadTexts:
    cpcScheduleConfigEntry.setStatus("current")
_CpcScheduleStartTime_Type = DateAndTime
_CpcScheduleStartTime_Object = MibTableColumn
cpcScheduleStartTime = _CpcScheduleStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 4, 1, 1, 1),
    _CpcScheduleStartTime_Type()
)
cpcScheduleStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpcScheduleStartTime.setStatus("current")
_CpcScheduleCapturePeriod_Type = Unsigned32
_CpcScheduleCapturePeriod_Object = MibTableColumn
cpcScheduleCapturePeriod = _CpcScheduleCapturePeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 4, 1, 1, 2),
    _CpcScheduleCapturePeriod_Type()
)
cpcScheduleCapturePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpcScheduleCapturePeriod.setStatus("current")
if mibBuilder.loadTexts:
    cpcScheduleCapturePeriod.setUnits("seconds")
_CpcSessionStats_ObjectIdentity = ObjectIdentity
cpcSessionStats = _CpcSessionStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 5)
)
_CpcSessionStatsTable_Object = MibTable
cpcSessionStatsTable = _CpcSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cpcSessionStatsTable.setStatus("current")
_CpcSessionStatsEntry_Object = MibTableRow
cpcSessionStatsEntry = _CpcSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 5, 1, 1)
)
cpcSessionStatsEntry.setIndexNames(
    (0, "CISCO-PACKET-CAPTURE-MIB", "cpcSessionId"),
)
if mibBuilder.loadTexts:
    cpcSessionStatsEntry.setStatus("current")
_CpcSessionPacketsReceived_Type = Unsigned32
_CpcSessionPacketsReceived_Object = MibTableColumn
cpcSessionPacketsReceived = _CpcSessionPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 5, 1, 1, 1),
    _CpcSessionPacketsReceived_Type()
)
cpcSessionPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpcSessionPacketsReceived.setStatus("current")
_CpcSessionPacketsCaptured_Type = Unsigned32
_CpcSessionPacketsCaptured_Object = MibTableColumn
cpcSessionPacketsCaptured = _CpcSessionPacketsCaptured_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 5, 1, 1, 2),
    _CpcSessionPacketsCaptured_Type()
)
cpcSessionPacketsCaptured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpcSessionPacketsCaptured.setStatus("current")
_CpcSessionPacketsDropped_Type = Unsigned32
_CpcSessionPacketsDropped_Object = MibTableColumn
cpcSessionPacketsDropped = _CpcSessionPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 1, 5, 1, 1, 3),
    _CpcSessionPacketsDropped_Type()
)
cpcSessionPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpcSessionPacketsDropped.setStatus("current")
_CpcMIBConformance_ObjectIdentity = ObjectIdentity
cpcMIBConformance = _CpcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 2)
)
_CpcMIBCompliances_ObjectIdentity = ObjectIdentity
cpcMIBCompliances = _CpcMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 2, 1)
)
_CpcMIBGroups_ObjectIdentity = ObjectIdentity
cpcMIBGroups = _CpcMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 2, 2)
)

# Managed Objects groups

cpcGenericConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 2, 2, 1)
)
cpcGenericConfigGroup.setObjects(
      *(("CISCO-PACKET-CAPTURE-MIB", "cpcMaxSessionAllowed"),
        ("CISCO-PACKET-CAPTURE-MIB", "cpcSessionOperStatus"),
        ("CISCO-PACKET-CAPTURE-MIB", "cpcSessionMaxSources"),
        ("CISCO-PACKET-CAPTURE-MIB", "cpcSessionPacketLength"),
        ("CISCO-PACKET-CAPTURE-MIB", "cpcSessionPacketLimits"),
        ("CISCO-PACKET-CAPTURE-MIB", "cpcSessionAction"),
        ("CISCO-PACKET-CAPTURE-MIB", "cpcSessionConfigStatus"),
        ("CISCO-PACKET-CAPTURE-MIB", "cpcCaptureSourceIfDirection"),
        ("CISCO-PACKET-CAPTURE-MIB", "cpcCaptureSourceIfStatus"))
)
if mibBuilder.loadTexts:
    cpcGenericConfigGroup.setStatus("current")

cpcFilterConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 2, 2, 2)
)
cpcFilterConfigGroup.setObjects(
    ("CISCO-PACKET-CAPTURE-MIB", "cpcMaxFilterAllowed")
)
if mibBuilder.loadTexts:
    cpcFilterConfigGroup.setStatus("current")

cpcMacFilterConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 2, 2, 3)
)
cpcMacFilterConfigGroup.setObjects(
    ("CISCO-PACKET-CAPTURE-MIB", "cpcMacFilterRowStatus")
)
if mibBuilder.loadTexts:
    cpcMacFilterConfigGroup.setStatus("current")

cpcIpFilterConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 2, 2, 4)
)
cpcIpFilterConfigGroup.setObjects(
      *(("CISCO-PACKET-CAPTURE-MIB", "cpcIpFilterMask"),
        ("CISCO-PACKET-CAPTURE-MIB", "cpcIpFilterRowStatus"))
)
if mibBuilder.loadTexts:
    cpcIpFilterConfigGroup.setStatus("current")

cpcDestFileNameConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 2, 2, 5)
)
cpcDestFileNameConfigGroup.setObjects(
    ("CISCO-PACKET-CAPTURE-MIB", "cpcSessionDestFileName")
)
if mibBuilder.loadTexts:
    cpcDestFileNameConfigGroup.setStatus("current")

cpcPacketLengthFilterConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 2, 2, 6)
)
cpcPacketLengthFilterConfigGroup.setObjects(
      *(("CISCO-PACKET-CAPTURE-MIB", "cpcPacketLengthFilterMin"),
        ("CISCO-PACKET-CAPTURE-MIB", "cpcPacketLengthFilterMax"))
)
if mibBuilder.loadTexts:
    cpcPacketLengthFilterConfigGroup.setStatus("current")

cpcEthertypeFilterConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 2, 2, 7)
)
cpcEthertypeFilterConfigGroup.setObjects(
      *(("CISCO-PACKET-CAPTURE-MIB", "cpcMaxEthertypeFilterAllowed"),
        ("CISCO-PACKET-CAPTURE-MIB", "cpcEthertypeFilterStatus"))
)
if mibBuilder.loadTexts:
    cpcEthertypeFilterConfigGroup.setStatus("current")

cpcVlanFilterConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 2, 2, 8)
)
cpcVlanFilterConfigGroup.setObjects(
      *(("CISCO-PACKET-CAPTURE-MIB", "cpcMaxVlanFilterAllowed"),
        ("CISCO-PACKET-CAPTURE-MIB", "cpcVlanFilterRowStatus"))
)
if mibBuilder.loadTexts:
    cpcVlanFilterConfigGroup.setStatus("current")

cpcAccessGroupFilterConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 2, 2, 9)
)
cpcAccessGroupFilterConfigGroup.setObjects(
      *(("CISCO-PACKET-CAPTURE-MIB", "cpcMaxAccessGroupFilterAllowed"),
        ("CISCO-PACKET-CAPTURE-MIB", "cpcAccessGroupFilterStatus"))
)
if mibBuilder.loadTexts:
    cpcAccessGroupFilterConfigGroup.setStatus("current")

cpcBufferConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 2, 2, 10)
)
cpcBufferConfigGroup.setObjects(
      *(("CISCO-PACKET-CAPTURE-MIB", "cpcBufferType"),
        ("CISCO-PACKET-CAPTURE-MIB", "cpcBufferSize"),
        ("CISCO-PACKET-CAPTURE-MIB", "cpcBufferAction"),
        ("CISCO-PACKET-CAPTURE-MIB", "cpcBufferOperStatus"))
)
if mibBuilder.loadTexts:
    cpcBufferConfigGroup.setStatus("current")

cpcScheduleConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 2, 2, 11)
)
cpcScheduleConfigGroup.setObjects(
      *(("CISCO-PACKET-CAPTURE-MIB", "cpcScheduleStartTime"),
        ("CISCO-PACKET-CAPTURE-MIB", "cpcScheduleCapturePeriod"))
)
if mibBuilder.loadTexts:
    cpcScheduleConfigGroup.setStatus("current")

cpcSessionStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 2, 2, 12)
)
cpcSessionStatsGroup.setObjects(
      *(("CISCO-PACKET-CAPTURE-MIB", "cpcSessionPacketsReceived"),
        ("CISCO-PACKET-CAPTURE-MIB", "cpcSessionPacketsCaptured"),
        ("CISCO-PACKET-CAPTURE-MIB", "cpcSessionPacketsDropped"))
)
if mibBuilder.loadTexts:
    cpcSessionStatsGroup.setStatus("current")

cpcMaxMacFilterConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 2, 2, 13)
)
cpcMaxMacFilterConfigGroup.setObjects(
    ("CISCO-PACKET-CAPTURE-MIB", "cpcMaxMacFilterAllowed")
)
if mibBuilder.loadTexts:
    cpcMaxMacFilterConfigGroup.setStatus("current")

cpcMaxIpFilterConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 2, 2, 14)
)
cpcMaxIpFilterConfigGroup.setObjects(
    ("CISCO-PACKET-CAPTURE-MIB", "cpcMaxIpFilterAllowed")
)
if mibBuilder.loadTexts:
    cpcMaxIpFilterConfigGroup.setStatus("current")

cpcSessionPacketRateLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 2, 2, 15)
)
cpcSessionPacketRateLimitGroup.setObjects(
    ("CISCO-PACKET-CAPTURE-MIB", "cpcSessionPacketRateLimit")
)
if mibBuilder.loadTexts:
    cpcSessionPacketRateLimitGroup.setStatus("current")

cpcSessionDescrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 2, 2, 16)
)
cpcSessionDescrGroup.setObjects(
    ("CISCO-PACKET-CAPTURE-MIB", "cpcSessionDescr")
)
if mibBuilder.loadTexts:
    cpcSessionDescrGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cpcCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cpcCompliance.setStatus(
        "deprecated"
    )

cpcComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 602, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cpcComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-PACKET-CAPTURE-MIB",
    **{"CiscoPacketCaptureFilterCriteria": CiscoPacketCaptureFilterCriteria,
       "ciscoPacketCaptureMIB": ciscoPacketCaptureMIB,
       "cpcMIBNotification": cpcMIBNotification,
       "cpcMIBObjects": cpcMIBObjects,
       "cpcGenericConfig": cpcGenericConfig,
       "cpcMaxSessionAllowed": cpcMaxSessionAllowed,
       "cpcSessionConfigTable": cpcSessionConfigTable,
       "cpcSessionConfigEntry": cpcSessionConfigEntry,
       "cpcSessionId": cpcSessionId,
       "cpcSessionOperStatus": cpcSessionOperStatus,
       "cpcSessionDestFileName": cpcSessionDestFileName,
       "cpcSessionPacketLength": cpcSessionPacketLength,
       "cpcSessionPacketLimits": cpcSessionPacketLimits,
       "cpcSessionAction": cpcSessionAction,
       "cpcSessionConfigStatus": cpcSessionConfigStatus,
       "cpcSessionPacketRateLimit": cpcSessionPacketRateLimit,
       "cpcSessionDescr": cpcSessionDescr,
       "cpcSessionMaxSources": cpcSessionMaxSources,
       "cpcCaptureSourceIfTable": cpcCaptureSourceIfTable,
       "cpcCaptureSourceIfEntry": cpcCaptureSourceIfEntry,
       "cpcCaptureSourceIfDirection": cpcCaptureSourceIfDirection,
       "cpcCaptureSourceIfStatus": cpcCaptureSourceIfStatus,
       "cpcFilterConfig": cpcFilterConfig,
       "cpcMaxFilterAllowed": cpcMaxFilterAllowed,
       "cpcMacFilterTable": cpcMacFilterTable,
       "cpcMacFilterEntry": cpcMacFilterEntry,
       "cpcMacFilterMacAddress": cpcMacFilterMacAddress,
       "cpcMacFilterCriteria": cpcMacFilterCriteria,
       "cpcMacFilterRowStatus": cpcMacFilterRowStatus,
       "cpcIpFilterTable": cpcIpFilterTable,
       "cpcIpFilterEntry": cpcIpFilterEntry,
       "cpcIpFilterAddressType": cpcIpFilterAddressType,
       "cpcIpFilterAddress": cpcIpFilterAddress,
       "cpcIpFilterCriteria": cpcIpFilterCriteria,
       "cpcIpFilterMask": cpcIpFilterMask,
       "cpcIpFilterRowStatus": cpcIpFilterRowStatus,
       "cpcMaxMacFilterAllowed": cpcMaxMacFilterAllowed,
       "cpcMaxIpFilterAllowed": cpcMaxIpFilterAllowed,
       "cpcPacketLengthFilterTable": cpcPacketLengthFilterTable,
       "cpcPacketLengthFilterEntry": cpcPacketLengthFilterEntry,
       "cpcPacketLengthFilterMin": cpcPacketLengthFilterMin,
       "cpcPacketLengthFilterMax": cpcPacketLengthFilterMax,
       "cpcMaxEthertypeFilterAllowed": cpcMaxEthertypeFilterAllowed,
       "cpcEthertypeFilterTable": cpcEthertypeFilterTable,
       "cpcEthertypeFilterEntry": cpcEthertypeFilterEntry,
       "cpcEthertypeFilterValue": cpcEthertypeFilterValue,
       "cpcEthertypeFilterStatus": cpcEthertypeFilterStatus,
       "cpcMaxVlanFilterAllowed": cpcMaxVlanFilterAllowed,
       "cpcVlanFilterTable": cpcVlanFilterTable,
       "cpcVlanFilterEntry": cpcVlanFilterEntry,
       "cpcVlanFilterVlanIndex": cpcVlanFilterVlanIndex,
       "cpcVlanFilterRowStatus": cpcVlanFilterRowStatus,
       "cpcMaxAccessGroupFilterAllowed": cpcMaxAccessGroupFilterAllowed,
       "cpcAccessGroupFilterTable": cpcAccessGroupFilterTable,
       "cpcAccessGroupFilterEntry": cpcAccessGroupFilterEntry,
       "cpcAccessGroupFilterType": cpcAccessGroupFilterType,
       "cpcAccessGroupFilterName": cpcAccessGroupFilterName,
       "cpcAccessGroupFilterStatus": cpcAccessGroupFilterStatus,
       "cpcBufferConfig": cpcBufferConfig,
       "cpcBufferConfigTable": cpcBufferConfigTable,
       "cpcBufferConfigEntry": cpcBufferConfigEntry,
       "cpcBufferType": cpcBufferType,
       "cpcBufferSize": cpcBufferSize,
       "cpcBufferAction": cpcBufferAction,
       "cpcBufferOperStatus": cpcBufferOperStatus,
       "cpcScheduleConfig": cpcScheduleConfig,
       "cpcScheduleConfigTable": cpcScheduleConfigTable,
       "cpcScheduleConfigEntry": cpcScheduleConfigEntry,
       "cpcScheduleStartTime": cpcScheduleStartTime,
       "cpcScheduleCapturePeriod": cpcScheduleCapturePeriod,
       "cpcSessionStats": cpcSessionStats,
       "cpcSessionStatsTable": cpcSessionStatsTable,
       "cpcSessionStatsEntry": cpcSessionStatsEntry,
       "cpcSessionPacketsReceived": cpcSessionPacketsReceived,
       "cpcSessionPacketsCaptured": cpcSessionPacketsCaptured,
       "cpcSessionPacketsDropped": cpcSessionPacketsDropped,
       "cpcMIBConformance": cpcMIBConformance,
       "cpcMIBCompliances": cpcMIBCompliances,
       "cpcCompliance": cpcCompliance,
       "cpcComplianceRev1": cpcComplianceRev1,
       "cpcMIBGroups": cpcMIBGroups,
       "cpcGenericConfigGroup": cpcGenericConfigGroup,
       "cpcFilterConfigGroup": cpcFilterConfigGroup,
       "cpcMacFilterConfigGroup": cpcMacFilterConfigGroup,
       "cpcIpFilterConfigGroup": cpcIpFilterConfigGroup,
       "cpcDestFileNameConfigGroup": cpcDestFileNameConfigGroup,
       "cpcPacketLengthFilterConfigGroup": cpcPacketLengthFilterConfigGroup,
       "cpcEthertypeFilterConfigGroup": cpcEthertypeFilterConfigGroup,
       "cpcVlanFilterConfigGroup": cpcVlanFilterConfigGroup,
       "cpcAccessGroupFilterConfigGroup": cpcAccessGroupFilterConfigGroup,
       "cpcBufferConfigGroup": cpcBufferConfigGroup,
       "cpcScheduleConfigGroup": cpcScheduleConfigGroup,
       "cpcSessionStatsGroup": cpcSessionStatsGroup,
       "cpcMaxMacFilterConfigGroup": cpcMaxMacFilterConfigGroup,
       "cpcMaxIpFilterConfigGroup": cpcMaxIpFilterConfigGroup,
       "cpcSessionPacketRateLimitGroup": cpcSessionPacketRateLimitGroup,
       "cpcSessionDescrGroup": cpcSessionDescrGroup}
)
