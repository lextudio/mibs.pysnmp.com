# SNMP MIB module (CISCO-MGC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-MGC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:56 2024
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

(cmgwIndex,
 cmgwSignalProtocolIndex) = mibBuilder.importSymbols(
    "CISCO-MEDIA-GATEWAY-MIB",
    "cmgwIndex",
    "cmgwSignalProtocolIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoPort,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoPort")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoMgcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 321)
)
ciscoMgcMIB.setRevisions(
        ("2003-04-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CMgcGroupIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )



class CMgcGroupIndexOrZero(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )



# MIB Managed Objects in the order of their OIDs

_CMgcMibNotifications_ObjectIdentity = ObjectIdentity
cMgcMibNotifications = _CMgcMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 0)
)
_CMgcMibObjects_ObjectIdentity = ObjectIdentity
cMgcMibObjects = _CMgcMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 1)
)
_CMgcConfig_ObjectIdentity = ObjectIdentity
cMgcConfig = _CMgcConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 1, 1)
)
_CMgcConfigTable_Object = MibTable
cMgcConfigTable = _CMgcConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cMgcConfigTable.setStatus("current")
_CMgcConfigEntry_Object = MibTableRow
cMgcConfigEntry = _CMgcConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 1, 1, 1, 1)
)
cMgcConfigEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
    (0, "CISCO-MGC-MIB", "cMgcIndex"),
)
if mibBuilder.loadTexts:
    cMgcConfigEntry.setStatus("current")


class _CMgcIndex_Type(Integer32):
    """Custom type cMgcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CMgcIndex_Type.__name__ = "Integer32"
_CMgcIndex_Object = MibTableColumn
cMgcIndex = _CMgcIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 1, 1, 1, 1, 1),
    _CMgcIndex_Type()
)
cMgcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMgcIndex.setStatus("current")


class _CMgcDomainName_Type(SnmpAdminString):
    """Custom type cMgcDomainName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CMgcDomainName_Type.__name__ = "SnmpAdminString"
_CMgcDomainName_Object = MibTableColumn
cMgcDomainName = _CMgcDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 1, 1, 1, 1, 2),
    _CMgcDomainName_Type()
)
cMgcDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMgcDomainName.setStatus("current")


class _CMgcNumMgcGroups_Type(Integer32):
    """Custom type cMgcNumMgcGroups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CMgcNumMgcGroups_Type.__name__ = "Integer32"
_CMgcNumMgcGroups_Object = MibTableColumn
cMgcNumMgcGroups = _CMgcNumMgcGroups_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 1, 1, 1, 1, 3),
    _CMgcNumMgcGroups_Type()
)
cMgcNumMgcGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMgcNumMgcGroups.setStatus("current")


class _CMgcNumIP_Type(Integer32):
    """Custom type cMgcNumIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CMgcNumIP_Type.__name__ = "Integer32"
_CMgcNumIP_Object = MibTableColumn
cMgcNumIP = _CMgcNumIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 1, 1, 1, 1, 4),
    _CMgcNumIP_Type()
)
cMgcNumIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMgcNumIP.setStatus("current")


class _CMgcResolution_Type(Integer32):
    """Custom type cMgcResolution based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("externalOnly", 2),
          ("internalOnly", 1))
    )


_CMgcResolution_Type.__name__ = "Integer32"
_CMgcResolution_Object = MibTableColumn
cMgcResolution = _CMgcResolution_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 1, 1, 1, 1, 5),
    _CMgcResolution_Type()
)
cMgcResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMgcResolution.setStatus("current")
_CMgcIpConfigTable_Object = MibTable
cMgcIpConfigTable = _CMgcIpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cMgcIpConfigTable.setStatus("current")
_CMgcIpConfigEntry_Object = MibTableRow
cMgcIpConfigEntry = _CMgcIpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 1, 1, 2, 1)
)
cMgcIpConfigEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
    (0, "CISCO-MGC-MIB", "cMgcIndex"),
    (0, "CISCO-MGC-MIB", "cMgcIpIndex"),
)
if mibBuilder.loadTexts:
    cMgcIpConfigEntry.setStatus("current")


class _CMgcIpIndex_Type(Integer32):
    """Custom type cMgcIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CMgcIpIndex_Type.__name__ = "Integer32"
_CMgcIpIndex_Object = MibTableColumn
cMgcIpIndex = _CMgcIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 1, 1, 2, 1, 1),
    _CMgcIpIndex_Type()
)
cMgcIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMgcIpIndex.setStatus("current")


class _CMgcIpAddressType_Type(InetAddressType):
    """Custom type cMgcIpAddressType based on InetAddressType"""


_CMgcIpAddressType_Object = MibTableColumn
cMgcIpAddressType = _CMgcIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 1, 1, 2, 1, 2),
    _CMgcIpAddressType_Type()
)
cMgcIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMgcIpAddressType.setStatus("current")
_CMgcIpAddress_Type = InetAddress
_CMgcIpAddress_Object = MibTableColumn
cMgcIpAddress = _CMgcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 1, 1, 2, 1, 3),
    _CMgcIpAddress_Type()
)
cMgcIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMgcIpAddress.setStatus("current")


class _CMgcIpPreference_Type(Integer32):
    """Custom type cMgcIpPreference based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CMgcIpPreference_Type.__name__ = "Integer32"
_CMgcIpPreference_Object = MibTableColumn
cMgcIpPreference = _CMgcIpPreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 1, 1, 2, 1, 4),
    _CMgcIpPreference_Type()
)
cMgcIpPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMgcIpPreference.setStatus("current")
_CMgcIpRowStatus_Type = RowStatus
_CMgcIpRowStatus_Object = MibTableColumn
cMgcIpRowStatus = _CMgcIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 1, 1, 2, 1, 5),
    _CMgcIpRowStatus_Type()
)
cMgcIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMgcIpRowStatus.setStatus("current")
_CMgcGroupConfig_ObjectIdentity = ObjectIdentity
cMgcGroupConfig = _CMgcGroupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 1, 2)
)
_CMgcGrpParamTable_Object = MibTable
cMgcGrpParamTable = _CMgcGrpParamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cMgcGrpParamTable.setStatus("current")
_CMgcGrpParamEntry_Object = MibTableRow
cMgcGrpParamEntry = _CMgcGrpParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 1, 2, 1, 1)
)
cMgcGrpParamEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
    (0, "CISCO-MGC-MIB", "cMgcGrpIndex"),
)
if mibBuilder.loadTexts:
    cMgcGrpParamEntry.setStatus("current")
_CMgcGrpIndex_Type = CMgcGroupIndex
_CMgcGrpIndex_Object = MibTableColumn
cMgcGrpIndex = _CMgcGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 1, 2, 1, 1, 1),
    _CMgcGrpIndex_Type()
)
cMgcGrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMgcGrpIndex.setStatus("current")


class _CMgcGrpNumMgc_Type(Integer32):
    """Custom type cMgcGrpNumMgc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_CMgcGrpNumMgc_Type.__name__ = "Integer32"
_CMgcGrpNumMgc_Object = MibTableColumn
cMgcGrpNumMgc = _CMgcGrpNumMgc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 1, 2, 1, 1, 2),
    _CMgcGrpNumMgc_Type()
)
cMgcGrpNumMgc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMgcGrpNumMgc.setStatus("current")
_CMgcGrpAssociationInfo_Type = Unsigned32
_CMgcGrpAssociationInfo_Object = MibTableColumn
cMgcGrpAssociationInfo = _CMgcGrpAssociationInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 1, 2, 1, 1, 3),
    _CMgcGrpAssociationInfo_Type()
)
cMgcGrpAssociationInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMgcGrpAssociationInfo.setStatus("current")


class _CMgcGrpNumProtocol_Type(Integer32):
    """Custom type cMgcGrpNumProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_CMgcGrpNumProtocol_Type.__name__ = "Integer32"
_CMgcGrpNumProtocol_Object = MibTableColumn
cMgcGrpNumProtocol = _CMgcGrpNumProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 1, 2, 1, 1, 4),
    _CMgcGrpNumProtocol_Type()
)
cMgcGrpNumProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMgcGrpNumProtocol.setStatus("current")


class _CMgcGrpStateChangeNtfy_Type(TruthValue):
    """Custom type cMgcGrpStateChangeNtfy based on TruthValue"""


_CMgcGrpStateChangeNtfy_Object = MibTableColumn
cMgcGrpStateChangeNtfy = _CMgcGrpStateChangeNtfy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 1, 2, 1, 1, 5),
    _CMgcGrpStateChangeNtfy_Type()
)
cMgcGrpStateChangeNtfy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMgcGrpStateChangeNtfy.setStatus("current")
_CMgcGrpTable_Object = MibTable
cMgcGrpTable = _CMgcGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cMgcGrpTable.setStatus("current")
_CMgcGrpEntry_Object = MibTableRow
cMgcGrpEntry = _CMgcGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 1, 2, 2, 1)
)
cMgcGrpEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
    (0, "CISCO-MGC-MIB", "cMgcGrpIndex"),
    (0, "CISCO-MGC-MIB", "cMgcIndex"),
)
if mibBuilder.loadTexts:
    cMgcGrpEntry.setStatus("current")


class _CMgcGrpMgcPreference_Type(Integer32):
    """Custom type cMgcGrpMgcPreference based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_CMgcGrpMgcPreference_Type.__name__ = "Integer32"
_CMgcGrpMgcPreference_Object = MibTableColumn
cMgcGrpMgcPreference = _CMgcGrpMgcPreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 1, 2, 2, 1, 1),
    _CMgcGrpMgcPreference_Type()
)
cMgcGrpMgcPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMgcGrpMgcPreference.setStatus("current")


class _CMgcGrpMgcUdpPort_Type(CiscoPort):
    """Custom type cMgcGrpMgcUdpPort based on CiscoPort"""
    defaultValue = 0


_CMgcGrpMgcUdpPort_Object = MibTableColumn
cMgcGrpMgcUdpPort = _CMgcGrpMgcUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 1, 2, 2, 1, 2),
    _CMgcGrpMgcUdpPort_Type()
)
cMgcGrpMgcUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMgcGrpMgcUdpPort.setStatus("current")
_CMgcGrpRowStatus_Type = RowStatus
_CMgcGrpRowStatus_Object = MibTableColumn
cMgcGrpRowStatus = _CMgcGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 1, 2, 2, 1, 3),
    _CMgcGrpRowStatus_Type()
)
cMgcGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMgcGrpRowStatus.setStatus("current")
_CMgcGrpProtocolTable_Object = MibTable
cMgcGrpProtocolTable = _CMgcGrpProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cMgcGrpProtocolTable.setStatus("current")
_CMgcGrpProtocolEntry_Object = MibTableRow
cMgcGrpProtocolEntry = _CMgcGrpProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 1, 2, 3, 1)
)
cMgcGrpProtocolEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
    (0, "CISCO-MGC-MIB", "cMgcGrpIndex"),
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwSignalProtocolIndex"),
)
if mibBuilder.loadTexts:
    cMgcGrpProtocolEntry.setStatus("current")


class _CMgcGrpProtocolPreference_Type(Integer32):
    """Custom type cMgcGrpProtocolPreference based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CMgcGrpProtocolPreference_Type.__name__ = "Integer32"
_CMgcGrpProtocolPreference_Object = MibTableColumn
cMgcGrpProtocolPreference = _CMgcGrpProtocolPreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 1, 2, 3, 1, 1),
    _CMgcGrpProtocolPreference_Type()
)
cMgcGrpProtocolPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMgcGrpProtocolPreference.setStatus("current")
_CMgcGrpProtocolRowStatus_Type = RowStatus
_CMgcGrpProtocolRowStatus_Object = MibTableColumn
cMgcGrpProtocolRowStatus = _CMgcGrpProtocolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 1, 2, 3, 1, 2),
    _CMgcGrpProtocolRowStatus_Type()
)
cMgcGrpProtocolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMgcGrpProtocolRowStatus.setStatus("current")
_CMgcMIBConformance_ObjectIdentity = ObjectIdentity
cMgcMIBConformance = _CMgcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 2)
)
_CMgcMIBCompliances_ObjectIdentity = ObjectIdentity
cMgcMIBCompliances = _CMgcMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 2, 1)
)
_CMgcMIBGroups_ObjectIdentity = ObjectIdentity
cMgcMIBGroups = _CMgcMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 2, 2)
)

# Managed Objects groups

cMgcMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 2, 2, 1)
)
cMgcMIBGroup.setObjects(
      *(("CISCO-MGC-MIB", "cMgcDomainName"),
        ("CISCO-MGC-MIB", "cMgcNumMgcGroups"),
        ("CISCO-MGC-MIB", "cMgcNumIP"),
        ("CISCO-MGC-MIB", "cMgcResolution"))
)
if mibBuilder.loadTexts:
    cMgcMIBGroup.setStatus("current")

cMgcIpMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 2, 2, 2)
)
cMgcIpMIBGroup.setObjects(
      *(("CISCO-MGC-MIB", "cMgcIpAddress"),
        ("CISCO-MGC-MIB", "cMgcIpAddressType"),
        ("CISCO-MGC-MIB", "cMgcIpPreference"),
        ("CISCO-MGC-MIB", "cMgcIpRowStatus"))
)
if mibBuilder.loadTexts:
    cMgcIpMIBGroup.setStatus("current")

cMgcGrpParamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 2, 2, 3)
)
cMgcGrpParamGroup.setObjects(
      *(("CISCO-MGC-MIB", "cMgcGrpNumMgc"),
        ("CISCO-MGC-MIB", "cMgcGrpAssociationInfo"),
        ("CISCO-MGC-MIB", "cMgcGrpNumProtocol"),
        ("CISCO-MGC-MIB", "cMgcGrpStateChangeNtfy"))
)
if mibBuilder.loadTexts:
    cMgcGrpParamGroup.setStatus("current")

cMgcGrpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 2, 2, 4)
)
cMgcGrpGroup.setObjects(
      *(("CISCO-MGC-MIB", "cMgcGrpMgcPreference"),
        ("CISCO-MGC-MIB", "cMgcGrpMgcUdpPort"),
        ("CISCO-MGC-MIB", "cMgcGrpRowStatus"))
)
if mibBuilder.loadTexts:
    cMgcGrpGroup.setStatus("current")

cMgcGrpProtocolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 2, 2, 5)
)
cMgcGrpProtocolGroup.setObjects(
      *(("CISCO-MGC-MIB", "cMgcGrpProtocolPreference"),
        ("CISCO-MGC-MIB", "cMgcGrpProtocolRowStatus"))
)
if mibBuilder.loadTexts:
    cMgcGrpProtocolGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cMgcMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 321, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cMgcMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MGC-MIB",
    **{"CMgcGroupIndex": CMgcGroupIndex,
       "CMgcGroupIndexOrZero": CMgcGroupIndexOrZero,
       "ciscoMgcMIB": ciscoMgcMIB,
       "cMgcMibNotifications": cMgcMibNotifications,
       "cMgcMibObjects": cMgcMibObjects,
       "cMgcConfig": cMgcConfig,
       "cMgcConfigTable": cMgcConfigTable,
       "cMgcConfigEntry": cMgcConfigEntry,
       "cMgcIndex": cMgcIndex,
       "cMgcDomainName": cMgcDomainName,
       "cMgcNumMgcGroups": cMgcNumMgcGroups,
       "cMgcNumIP": cMgcNumIP,
       "cMgcResolution": cMgcResolution,
       "cMgcIpConfigTable": cMgcIpConfigTable,
       "cMgcIpConfigEntry": cMgcIpConfigEntry,
       "cMgcIpIndex": cMgcIpIndex,
       "cMgcIpAddressType": cMgcIpAddressType,
       "cMgcIpAddress": cMgcIpAddress,
       "cMgcIpPreference": cMgcIpPreference,
       "cMgcIpRowStatus": cMgcIpRowStatus,
       "cMgcGroupConfig": cMgcGroupConfig,
       "cMgcGrpParamTable": cMgcGrpParamTable,
       "cMgcGrpParamEntry": cMgcGrpParamEntry,
       "cMgcGrpIndex": cMgcGrpIndex,
       "cMgcGrpNumMgc": cMgcGrpNumMgc,
       "cMgcGrpAssociationInfo": cMgcGrpAssociationInfo,
       "cMgcGrpNumProtocol": cMgcGrpNumProtocol,
       "cMgcGrpStateChangeNtfy": cMgcGrpStateChangeNtfy,
       "cMgcGrpTable": cMgcGrpTable,
       "cMgcGrpEntry": cMgcGrpEntry,
       "cMgcGrpMgcPreference": cMgcGrpMgcPreference,
       "cMgcGrpMgcUdpPort": cMgcGrpMgcUdpPort,
       "cMgcGrpRowStatus": cMgcGrpRowStatus,
       "cMgcGrpProtocolTable": cMgcGrpProtocolTable,
       "cMgcGrpProtocolEntry": cMgcGrpProtocolEntry,
       "cMgcGrpProtocolPreference": cMgcGrpProtocolPreference,
       "cMgcGrpProtocolRowStatus": cMgcGrpProtocolRowStatus,
       "cMgcMIBConformance": cMgcMIBConformance,
       "cMgcMIBCompliances": cMgcMIBCompliances,
       "cMgcMIBCompliance": cMgcMIBCompliance,
       "cMgcMIBGroups": cMgcMIBGroups,
       "cMgcMIBGroup": cMgcMIBGroup,
       "cMgcIpMIBGroup": cMgcIpMIBGroup,
       "cMgcGrpParamGroup": cMgcGrpParamGroup,
       "cMgcGrpGroup": cMgcGrpGroup,
       "cMgcGrpProtocolGroup": cMgcGrpProtocolGroup}
)
