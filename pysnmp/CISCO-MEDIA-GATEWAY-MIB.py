# SNMP MIB module (CISCO-MEDIA-GATEWAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-MEDIA-GATEWAY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:35 2024
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

(CiscoPort,
 EntPhysicalIndexOrZero) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoPort",
    "EntPhysicalIndexOrZero")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

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

ciscoMediaGatewayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 324)
)
ciscoMediaGatewayMIB.setRevisions(
        ("2009-02-25 00:00",
         "2006-06-15 00:00",
         "2005-09-01 00:00",
         "2004-11-19 00:00",
         "2004-07-30 00:00",
         "2003-04-07 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CGwServiceState(Integer32, TextualConvention):
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
        *(("forcedOutOfService", 2),
          ("gracefulOutOfService", 3),
          ("inService", 1))
    )



class CGwAdminState(Integer32, TextualConvention):
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
        *(("forcedOutOfService", 2),
          ("gracefulOutOfService", 3),
          ("inService", 1))
    )



class GatewayLifNumber(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class CVoiceTonePlanIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class CVoiceTonePlanIndexOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class CCallControlProfileIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class CCallControlProfileIndexOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class CCallControlJitterDelayMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 1),
          ("fixed", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoMediaGatewayMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoMediaGatewayMIBNotifs = _CiscoMediaGatewayMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 0)
)
_CiscoMediaGatewayMIBObjects_ObjectIdentity = ObjectIdentity
ciscoMediaGatewayMIBObjects = _CiscoMediaGatewayMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1)
)
_CMediaGwConfig_ObjectIdentity = ObjectIdentity
cMediaGwConfig = _CMediaGwConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1)
)
_CMediaGwTable_Object = MibTable
cMediaGwTable = _CMediaGwTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cMediaGwTable.setStatus("current")
_CMediaGwEntry_Object = MibTableRow
cMediaGwEntry = _CMediaGwEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 1, 1)
)
cMediaGwEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
)
if mibBuilder.loadTexts:
    cMediaGwEntry.setStatus("current")


class _CmgwIndex_Type(Integer32):
    """Custom type cmgwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CmgwIndex_Type.__name__ = "Integer32"
_CmgwIndex_Object = MibTableColumn
cmgwIndex = _CmgwIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 1, 1, 1),
    _CmgwIndex_Type()
)
cmgwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmgwIndex.setStatus("current")


class _CmgwDomainName_Type(SnmpAdminString):
    """Custom type cmgwDomainName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmgwDomainName_Type.__name__ = "SnmpAdminString"
_CmgwDomainName_Object = MibTableColumn
cmgwDomainName = _CmgwDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 1, 1, 2),
    _CmgwDomainName_Type()
)
cmgwDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgwDomainName.setStatus("current")
_CmgwPhysicalIndex_Type = EntPhysicalIndexOrZero
_CmgwPhysicalIndex_Object = MibTableColumn
cmgwPhysicalIndex = _CmgwPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 1, 1, 3),
    _CmgwPhysicalIndex_Type()
)
cmgwPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgwPhysicalIndex.setStatus("current")
_CmgwServiceState_Type = CGwServiceState
_CmgwServiceState_Object = MibTableColumn
cmgwServiceState = _CmgwServiceState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 1, 1, 4),
    _CmgwServiceState_Type()
)
cmgwServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgwServiceState.setStatus("current")
_CmgwAdminState_Type = CGwAdminState
_CmgwAdminState_Object = MibTableColumn
cmgwAdminState = _CmgwAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 1, 1, 5),
    _CmgwAdminState_Type()
)
cmgwAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgwAdminState.setStatus("current")


class _CmgwGraceTime_Type(Integer32):
    """Custom type cmgwGraceTime based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_CmgwGraceTime_Type.__name__ = "Integer32"
_CmgwGraceTime_Object = MibTableColumn
cmgwGraceTime = _CmgwGraceTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 1, 1, 6),
    _CmgwGraceTime_Type()
)
cmgwGraceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgwGraceTime.setStatus("current")
if mibBuilder.loadTexts:
    cmgwGraceTime.setUnits("seconds")


class _CmgwVtMappingMode_Type(Integer32):
    """Custom type cmgwVtMappingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standard", 1),
          ("titan", 2))
    )


_CmgwVtMappingMode_Type.__name__ = "Integer32"
_CmgwVtMappingMode_Object = MibTableColumn
cmgwVtMappingMode = _CmgwVtMappingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 1, 1, 7),
    _CmgwVtMappingMode_Type()
)
cmgwVtMappingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgwVtMappingMode.setStatus("current")


class _CmgwSrcFilterEnabled_Type(TruthValue):
    """Custom type cmgwSrcFilterEnabled based on TruthValue"""


_CmgwSrcFilterEnabled_Object = MibTableColumn
cmgwSrcFilterEnabled = _CmgwSrcFilterEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 1, 1, 8),
    _CmgwSrcFilterEnabled_Type()
)
cmgwSrcFilterEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgwSrcFilterEnabled.setStatus("current")


class _CmgwLawInterceptEnabled_Type(TruthValue):
    """Custom type cmgwLawInterceptEnabled based on TruthValue"""


_CmgwLawInterceptEnabled_Object = MibTableColumn
cmgwLawInterceptEnabled = _CmgwLawInterceptEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 1, 1, 9),
    _CmgwLawInterceptEnabled_Type()
)
cmgwLawInterceptEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgwLawInterceptEnabled.setStatus("current")


class _CmgwV23Enabled_Type(TruthValue):
    """Custom type cmgwV23Enabled based on TruthValue"""


_CmgwV23Enabled_Object = MibTableColumn
cmgwV23Enabled = _CmgwV23Enabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 1, 1, 10),
    _CmgwV23Enabled_Type()
)
cmgwV23Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgwV23Enabled.setStatus("current")
_CmgwSignalProtocolTable_Object = MibTable
cmgwSignalProtocolTable = _CmgwSignalProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cmgwSignalProtocolTable.setStatus("current")
_CmgwSignalProtocolEntry_Object = MibTableRow
cmgwSignalProtocolEntry = _CmgwSignalProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 2, 1)
)
cmgwSignalProtocolEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwSignalProtocolIndex"),
)
if mibBuilder.loadTexts:
    cmgwSignalProtocolEntry.setStatus("current")


class _CmgwSignalProtocolIndex_Type(Integer32):
    """Custom type cmgwSignalProtocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmgwSignalProtocolIndex_Type.__name__ = "Integer32"
_CmgwSignalProtocolIndex_Object = MibTableColumn
cmgwSignalProtocolIndex = _CmgwSignalProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 2, 1, 1),
    _CmgwSignalProtocolIndex_Type()
)
cmgwSignalProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmgwSignalProtocolIndex.setStatus("current")


class _CmgwSignalProtocol_Type(Integer32):
    """Custom type cmgwSignalProtocol based on Integer32"""
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
        *(("h248", 3),
          ("mgcp", 2),
          ("other", 1),
          ("tgcp", 4))
    )


_CmgwSignalProtocol_Type.__name__ = "Integer32"
_CmgwSignalProtocol_Object = MibTableColumn
cmgwSignalProtocol = _CmgwSignalProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 2, 1, 2),
    _CmgwSignalProtocol_Type()
)
cmgwSignalProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgwSignalProtocol.setStatus("current")


class _CmgwSignalProtocolVersion_Type(SnmpAdminString):
    """Custom type cmgwSignalProtocolVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CmgwSignalProtocolVersion_Type.__name__ = "SnmpAdminString"
_CmgwSignalProtocolVersion_Object = MibTableColumn
cmgwSignalProtocolVersion = _CmgwSignalProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 2, 1, 3),
    _CmgwSignalProtocolVersion_Type()
)
cmgwSignalProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgwSignalProtocolVersion.setStatus("current")
_CmgwSignalProtocolPort_Type = CiscoPort
_CmgwSignalProtocolPort_Object = MibTableColumn
cmgwSignalProtocolPort = _CmgwSignalProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 2, 1, 4),
    _CmgwSignalProtocolPort_Type()
)
cmgwSignalProtocolPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgwSignalProtocolPort.setStatus("current")
_CmgwSignalMgcProtocolPort_Type = InetPortNumber
_CmgwSignalMgcProtocolPort_Object = MibTableColumn
cmgwSignalMgcProtocolPort = _CmgwSignalMgcProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 2, 1, 5),
    _CmgwSignalMgcProtocolPort_Type()
)
cmgwSignalMgcProtocolPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgwSignalMgcProtocolPort.setStatus("current")


class _CmgwSignalProtocolPreference_Type(Integer32):
    """Custom type cmgwSignalProtocolPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CmgwSignalProtocolPreference_Type.__name__ = "Integer32"
_CmgwSignalProtocolPreference_Object = MibTableColumn
cmgwSignalProtocolPreference = _CmgwSignalProtocolPreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 2, 1, 6),
    _CmgwSignalProtocolPreference_Type()
)
cmgwSignalProtocolPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgwSignalProtocolPreference.setStatus("current")


class _CmgwSignalProtocolConfigVer_Type(SnmpAdminString):
    """Custom type cmgwSignalProtocolConfigVer based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CmgwSignalProtocolConfigVer_Type.__name__ = "SnmpAdminString"
_CmgwSignalProtocolConfigVer_Object = MibTableColumn
cmgwSignalProtocolConfigVer = _CmgwSignalProtocolConfigVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 2, 1, 7),
    _CmgwSignalProtocolConfigVer_Type()
)
cmgwSignalProtocolConfigVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmgwSignalProtocolConfigVer.setStatus("current")
_CMediaGwIpConfigTable_Object = MibTable
cMediaGwIpConfigTable = _CMediaGwIpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cMediaGwIpConfigTable.setStatus("current")
_CMediaGwIpConfigEntry_Object = MibTableRow
cMediaGwIpConfigEntry = _CMediaGwIpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 3, 1)
)
cMediaGwIpConfigEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIpConfigIndex"),
)
if mibBuilder.loadTexts:
    cMediaGwIpConfigEntry.setStatus("current")


class _CmgwIpConfigIndex_Type(Integer32):
    """Custom type cmgwIpConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_CmgwIpConfigIndex_Type.__name__ = "Integer32"
_CmgwIpConfigIndex_Object = MibTableColumn
cmgwIpConfigIndex = _CmgwIpConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 3, 1, 1),
    _CmgwIpConfigIndex_Type()
)
cmgwIpConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmgwIpConfigIndex.setStatus("current")
_CmgwIpConfigIfIndex_Type = InterfaceIndexOrZero
_CmgwIpConfigIfIndex_Object = MibTableColumn
cmgwIpConfigIfIndex = _CmgwIpConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 3, 1, 2),
    _CmgwIpConfigIfIndex_Type()
)
cmgwIpConfigIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmgwIpConfigIfIndex.setStatus("current")


class _CmgwIpConfigVpi_Type(Integer32):
    """Custom type cmgwIpConfigVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4095),
    )


_CmgwIpConfigVpi_Type.__name__ = "Integer32"
_CmgwIpConfigVpi_Object = MibTableColumn
cmgwIpConfigVpi = _CmgwIpConfigVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 3, 1, 3),
    _CmgwIpConfigVpi_Type()
)
cmgwIpConfigVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmgwIpConfigVpi.setStatus("current")


class _CmgwIpConfigVci_Type(Integer32):
    """Custom type cmgwIpConfigVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_CmgwIpConfigVci_Type.__name__ = "Integer32"
_CmgwIpConfigVci_Object = MibTableColumn
cmgwIpConfigVci = _CmgwIpConfigVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 3, 1, 4),
    _CmgwIpConfigVci_Type()
)
cmgwIpConfigVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmgwIpConfigVci.setStatus("current")


class _CmgwIpConfigAddrType_Type(InetAddressType):
    """Custom type cmgwIpConfigAddrType based on InetAddressType"""


_CmgwIpConfigAddrType_Object = MibTableColumn
cmgwIpConfigAddrType = _CmgwIpConfigAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 3, 1, 5),
    _CmgwIpConfigAddrType_Type()
)
cmgwIpConfigAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmgwIpConfigAddrType.setStatus("current")
_CmgwIpConfigAddress_Type = InetAddress
_CmgwIpConfigAddress_Object = MibTableColumn
cmgwIpConfigAddress = _CmgwIpConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 3, 1, 6),
    _CmgwIpConfigAddress_Type()
)
cmgwIpConfigAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmgwIpConfigAddress.setStatus("current")
_CmgwIpConfigSubnetMask_Type = InetAddressPrefixLength
_CmgwIpConfigSubnetMask_Object = MibTableColumn
cmgwIpConfigSubnetMask = _CmgwIpConfigSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 3, 1, 7),
    _CmgwIpConfigSubnetMask_Type()
)
cmgwIpConfigSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmgwIpConfigSubnetMask.setStatus("current")


class _CmgwIpConfigDefaultGwIp_Type(TruthValue):
    """Custom type cmgwIpConfigDefaultGwIp based on TruthValue"""


_CmgwIpConfigDefaultGwIp_Object = MibTableColumn
cmgwIpConfigDefaultGwIp = _CmgwIpConfigDefaultGwIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 3, 1, 8),
    _CmgwIpConfigDefaultGwIp_Type()
)
cmgwIpConfigDefaultGwIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmgwIpConfigDefaultGwIp.setStatus("current")


class _CmgwIpConfigForRemoteMapping_Type(TruthValue):
    """Custom type cmgwIpConfigForRemoteMapping based on TruthValue"""


_CmgwIpConfigForRemoteMapping_Object = MibTableColumn
cmgwIpConfigForRemoteMapping = _CmgwIpConfigForRemoteMapping_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 3, 1, 9),
    _CmgwIpConfigForRemoteMapping_Type()
)
cmgwIpConfigForRemoteMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmgwIpConfigForRemoteMapping.setStatus("current")
_CmgwIpConfigRowStatus_Type = RowStatus
_CmgwIpConfigRowStatus_Object = MibTableColumn
cmgwIpConfigRowStatus = _CmgwIpConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 3, 1, 10),
    _CmgwIpConfigRowStatus_Type()
)
cmgwIpConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmgwIpConfigRowStatus.setStatus("current")
_CMediaGwDomainNameConfigTable_Object = MibTable
cMediaGwDomainNameConfigTable = _CMediaGwDomainNameConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cMediaGwDomainNameConfigTable.setStatus("current")
_CMediaGwDomainNameConfigEntry_Object = MibTableRow
cMediaGwDomainNameConfigEntry = _CMediaGwDomainNameConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 4, 1)
)
cMediaGwDomainNameConfigEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwConfigDomainNameIndex"),
)
if mibBuilder.loadTexts:
    cMediaGwDomainNameConfigEntry.setStatus("current")


class _CmgwConfigDomainNameIndex_Type(Integer32):
    """Custom type cmgwConfigDomainNameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CmgwConfigDomainNameIndex_Type.__name__ = "Integer32"
_CmgwConfigDomainNameIndex_Object = MibTableColumn
cmgwConfigDomainNameIndex = _CmgwConfigDomainNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 4, 1, 1),
    _CmgwConfigDomainNameIndex_Type()
)
cmgwConfigDomainNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmgwConfigDomainNameIndex.setStatus("current")


class _CmgwConfigDomainNameEntity_Type(Integer32):
    """Custom type cmgwConfigDomainNameEntity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dnsServer", 2),
          ("gateway", 1),
          ("mgc", 3))
    )


_CmgwConfigDomainNameEntity_Type.__name__ = "Integer32"
_CmgwConfigDomainNameEntity_Object = MibTableColumn
cmgwConfigDomainNameEntity = _CmgwConfigDomainNameEntity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 4, 1, 2),
    _CmgwConfigDomainNameEntity_Type()
)
cmgwConfigDomainNameEntity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmgwConfigDomainNameEntity.setStatus("current")


class _CmgwConfigDomainName_Type(SnmpAdminString):
    """Custom type cmgwConfigDomainName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CmgwConfigDomainName_Type.__name__ = "SnmpAdminString"
_CmgwConfigDomainName_Object = MibTableColumn
cmgwConfigDomainName = _CmgwConfigDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 4, 1, 3),
    _CmgwConfigDomainName_Type()
)
cmgwConfigDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmgwConfigDomainName.setStatus("current")
_CmgwConfigDomainNameRowStatus_Type = RowStatus
_CmgwConfigDomainNameRowStatus_Object = MibTableColumn
cmgwConfigDomainNameRowStatus = _CmgwConfigDomainNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 4, 1, 4),
    _CmgwConfigDomainNameRowStatus_Type()
)
cmgwConfigDomainNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmgwConfigDomainNameRowStatus.setStatus("current")
_CMediaGwDnsIpConfigTable_Object = MibTable
cMediaGwDnsIpConfigTable = _CMediaGwDnsIpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cMediaGwDnsIpConfigTable.setStatus("current")
_CMediaGwDnsIpConfigEntry_Object = MibTableRow
cMediaGwDnsIpConfigEntry = _CMediaGwDnsIpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 5, 1)
)
cMediaGwDnsIpConfigEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwDnsIpIndex"),
)
if mibBuilder.loadTexts:
    cMediaGwDnsIpConfigEntry.setStatus("current")


class _CmgwDnsIpIndex_Type(Integer32):
    """Custom type cmgwDnsIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_CmgwDnsIpIndex_Type.__name__ = "Integer32"
_CmgwDnsIpIndex_Object = MibTableColumn
cmgwDnsIpIndex = _CmgwDnsIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 5, 1, 1),
    _CmgwDnsIpIndex_Type()
)
cmgwDnsIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmgwDnsIpIndex.setStatus("current")


class _CmgwDnsDomainName_Type(SnmpAdminString):
    """Custom type cmgwDnsDomainName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CmgwDnsDomainName_Type.__name__ = "SnmpAdminString"
_CmgwDnsDomainName_Object = MibTableColumn
cmgwDnsDomainName = _CmgwDnsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 5, 1, 2),
    _CmgwDnsDomainName_Type()
)
cmgwDnsDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgwDnsDomainName.setStatus("current")


class _CmgwDnsIpType_Type(InetAddressType):
    """Custom type cmgwDnsIpType based on InetAddressType"""


_CmgwDnsIpType_Object = MibTableColumn
cmgwDnsIpType = _CmgwDnsIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 5, 1, 3),
    _CmgwDnsIpType_Type()
)
cmgwDnsIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmgwDnsIpType.setStatus("current")
_CmgwDnsIp_Type = InetAddress
_CmgwDnsIp_Object = MibTableColumn
cmgwDnsIp = _CmgwDnsIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 5, 1, 4),
    _CmgwDnsIp_Type()
)
cmgwDnsIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmgwDnsIp.setStatus("current")
_CmgwDnsIpRowStatus_Type = RowStatus
_CmgwDnsIpRowStatus_Object = MibTableColumn
cmgwDnsIpRowStatus = _CmgwDnsIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 5, 1, 5),
    _CmgwDnsIpRowStatus_Type()
)
cmgwDnsIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmgwDnsIpRowStatus.setStatus("current")
_CmgwLifTable_Object = MibTable
cmgwLifTable = _CmgwLifTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cmgwLifTable.setStatus("current")
_CmgwLifEntry_Object = MibTableRow
cmgwLifEntry = _CmgwLifEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 6, 1)
)
cmgwLifEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwLifNumber"),
)
if mibBuilder.loadTexts:
    cmgwLifEntry.setStatus("current")
_CmgwLifNumber_Type = GatewayLifNumber
_CmgwLifNumber_Object = MibTableColumn
cmgwLifNumber = _CmgwLifNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 6, 1, 1),
    _CmgwLifNumber_Type()
)
cmgwLifNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmgwLifNumber.setStatus("current")


class _CmgwLifPvcCount_Type(Gauge32):
    """Custom type cmgwLifPvcCount based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_CmgwLifPvcCount_Type.__name__ = "Gauge32"
_CmgwLifPvcCount_Object = MibTableColumn
cmgwLifPvcCount = _CmgwLifPvcCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 6, 1, 2),
    _CmgwLifPvcCount_Type()
)
cmgwLifPvcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgwLifPvcCount.setStatus("current")


class _CmgwLifVoiceIfCount_Type(Gauge32):
    """Custom type cmgwLifVoiceIfCount based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CmgwLifVoiceIfCount_Type.__name__ = "Gauge32"
_CmgwLifVoiceIfCount_Object = MibTableColumn
cmgwLifVoiceIfCount = _CmgwLifVoiceIfCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 6, 1, 3),
    _CmgwLifVoiceIfCount_Type()
)
cmgwLifVoiceIfCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgwLifVoiceIfCount.setStatus("current")
_CMediaGwCallControlConfigTable_Object = MibTable
cMediaGwCallControlConfigTable = _CMediaGwCallControlConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cMediaGwCallControlConfigTable.setStatus("current")
_CMediaGwCallControlConfigEntry_Object = MibTableRow
cMediaGwCallControlConfigEntry = _CMediaGwCallControlConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 7, 1)
)
cMediaGwCallControlConfigEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
)
if mibBuilder.loadTexts:
    cMediaGwCallControlConfigEntry.setStatus("current")


class _CMediaGwCcCfgControlTos_Type(Unsigned32):
    """Custom type cMediaGwCcCfgControlTos based on Unsigned32"""
    defaultValue = 96

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CMediaGwCcCfgControlTos_Type.__name__ = "Unsigned32"
_CMediaGwCcCfgControlTos_Object = MibTableColumn
cMediaGwCcCfgControlTos = _CMediaGwCcCfgControlTos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 7, 1, 1),
    _CMediaGwCcCfgControlTos_Type()
)
cMediaGwCcCfgControlTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMediaGwCcCfgControlTos.setStatus("current")


class _CMediaGwCcCfgBearerTos_Type(Unsigned32):
    """Custom type cMediaGwCcCfgBearerTos based on Unsigned32"""
    defaultValue = 160

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CMediaGwCcCfgBearerTos_Type.__name__ = "Unsigned32"
_CMediaGwCcCfgBearerTos_Object = MibTableColumn
cMediaGwCcCfgBearerTos = _CMediaGwCcCfgBearerTos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 7, 1, 2),
    _CMediaGwCcCfgBearerTos_Type()
)
cMediaGwCcCfgBearerTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMediaGwCcCfgBearerTos.setStatus("current")


class _CMediaGwCcCfgNtePayload_Type(Unsigned32):
    """Custom type cMediaGwCcCfgNtePayload based on Unsigned32"""
    defaultValue = 101

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 127),
    )


_CMediaGwCcCfgNtePayload_Type.__name__ = "Unsigned32"
_CMediaGwCcCfgNtePayload_Object = MibTableColumn
cMediaGwCcCfgNtePayload = _CMediaGwCcCfgNtePayload_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 7, 1, 3),
    _CMediaGwCcCfgNtePayload_Type()
)
cMediaGwCcCfgNtePayload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMediaGwCcCfgNtePayload.setStatus("current")


class _CMediaGwCcCfgNsePayload_Type(Unsigned32):
    """Custom type cMediaGwCcCfgNsePayload based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(98, 117),
    )


_CMediaGwCcCfgNsePayload_Type.__name__ = "Unsigned32"
_CMediaGwCcCfgNsePayload_Object = MibTableColumn
cMediaGwCcCfgNsePayload = _CMediaGwCcCfgNsePayload_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 7, 1, 4),
    _CMediaGwCcCfgNsePayload_Type()
)
cMediaGwCcCfgNsePayload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMediaGwCcCfgNsePayload.setStatus("current")


class _CMediaGwCcCfgNseRespTimer_Type(Unsigned32):
    """Custom type cMediaGwCcCfgNseRespTimer based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 10000),
    )


_CMediaGwCcCfgNseRespTimer_Type.__name__ = "Unsigned32"
_CMediaGwCcCfgNseRespTimer_Object = MibTableColumn
cMediaGwCcCfgNseRespTimer = _CMediaGwCcCfgNseRespTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 7, 1, 5),
    _CMediaGwCcCfgNseRespTimer_Type()
)
cMediaGwCcCfgNseRespTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMediaGwCcCfgNseRespTimer.setStatus("current")
if mibBuilder.loadTexts:
    cMediaGwCcCfgNseRespTimer.setUnits("milliseconds")


class _CMediaGwCcCfgVbdJitterDelayMode_Type(CCallControlJitterDelayMode):
    """Custom type cMediaGwCcCfgVbdJitterDelayMode based on CCallControlJitterDelayMode"""


_CMediaGwCcCfgVbdJitterDelayMode_Object = MibTableColumn
cMediaGwCcCfgVbdJitterDelayMode = _CMediaGwCcCfgVbdJitterDelayMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 7, 1, 6),
    _CMediaGwCcCfgVbdJitterDelayMode_Type()
)
cMediaGwCcCfgVbdJitterDelayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMediaGwCcCfgVbdJitterDelayMode.setStatus("current")


class _CMediaGwCcCfgVbdJitterMaxDelay_Type(Unsigned32):
    """Custom type cMediaGwCcCfgVbdJitterMaxDelay based on Unsigned32"""
    defaultValue = 135

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 135),
    )


_CMediaGwCcCfgVbdJitterMaxDelay_Type.__name__ = "Unsigned32"
_CMediaGwCcCfgVbdJitterMaxDelay_Object = MibTableColumn
cMediaGwCcCfgVbdJitterMaxDelay = _CMediaGwCcCfgVbdJitterMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 7, 1, 7),
    _CMediaGwCcCfgVbdJitterMaxDelay_Type()
)
cMediaGwCcCfgVbdJitterMaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMediaGwCcCfgVbdJitterMaxDelay.setStatus("current")
if mibBuilder.loadTexts:
    cMediaGwCcCfgVbdJitterMaxDelay.setUnits("milliseconds")


class _CMediaGwCcCfgVbdJitterNomDelay_Type(Unsigned32):
    """Custom type cMediaGwCcCfgVbdJitterNomDelay based on Unsigned32"""
    defaultValue = 70

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 135),
    )


_CMediaGwCcCfgVbdJitterNomDelay_Type.__name__ = "Unsigned32"
_CMediaGwCcCfgVbdJitterNomDelay_Object = MibTableColumn
cMediaGwCcCfgVbdJitterNomDelay = _CMediaGwCcCfgVbdJitterNomDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 7, 1, 8),
    _CMediaGwCcCfgVbdJitterNomDelay_Type()
)
cMediaGwCcCfgVbdJitterNomDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMediaGwCcCfgVbdJitterNomDelay.setStatus("current")
if mibBuilder.loadTexts:
    cMediaGwCcCfgVbdJitterNomDelay.setUnits("milliseconds")


class _CMediaGwCcCfgVbdJitterMinDelay_Type(Unsigned32):
    """Custom type cMediaGwCcCfgVbdJitterMinDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 135),
    )


_CMediaGwCcCfgVbdJitterMinDelay_Type.__name__ = "Unsigned32"
_CMediaGwCcCfgVbdJitterMinDelay_Object = MibTableColumn
cMediaGwCcCfgVbdJitterMinDelay = _CMediaGwCcCfgVbdJitterMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 7, 1, 9),
    _CMediaGwCcCfgVbdJitterMinDelay_Type()
)
cMediaGwCcCfgVbdJitterMinDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMediaGwCcCfgVbdJitterMinDelay.setStatus("current")
if mibBuilder.loadTexts:
    cMediaGwCcCfgVbdJitterMinDelay.setUnits("milliseconds")


class _CMediaGwCcCfgDefaultTonePlanId_Type(CVoiceTonePlanIndex):
    """Custom type cMediaGwCcCfgDefaultTonePlanId based on CVoiceTonePlanIndex"""
    defaultValue = 1


_CMediaGwCcCfgDefaultTonePlanId_Object = MibTableColumn
cMediaGwCcCfgDefaultTonePlanId = _CMediaGwCcCfgDefaultTonePlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 7, 1, 10),
    _CMediaGwCcCfgDefaultTonePlanId_Type()
)
cMediaGwCcCfgDefaultTonePlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMediaGwCcCfgDefaultTonePlanId.setStatus("current")


class _CMediaGwCcCfgDescrInfoEnabled_Type(TruthValue):
    """Custom type cMediaGwCcCfgDescrInfoEnabled based on TruthValue"""


_CMediaGwCcCfgDescrInfoEnabled_Object = MibTableColumn
cMediaGwCcCfgDescrInfoEnabled = _CMediaGwCcCfgDescrInfoEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 7, 1, 11),
    _CMediaGwCcCfgDescrInfoEnabled_Type()
)
cMediaGwCcCfgDescrInfoEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMediaGwCcCfgDescrInfoEnabled.setStatus("current")


class _CMediaGwCcCfgDsNamePrefix_Type(SnmpAdminString):
    """Custom type cMediaGwCcCfgDsNamePrefix based on SnmpAdminString"""
    defaultHexValue = "4453"

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CMediaGwCcCfgDsNamePrefix_Type.__name__ = "SnmpAdminString"
_CMediaGwCcCfgDsNamePrefix_Object = MibTableColumn
cMediaGwCcCfgDsNamePrefix = _CMediaGwCcCfgDsNamePrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 7, 1, 12),
    _CMediaGwCcCfgDsNamePrefix_Type()
)
cMediaGwCcCfgDsNamePrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMediaGwCcCfgDsNamePrefix.setStatus("current")


class _CMediaGwCcCfgRtpNamePrefix_Type(SnmpAdminString):
    """Custom type cMediaGwCcCfgRtpNamePrefix based on SnmpAdminString"""
    defaultHexValue = "525450"

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CMediaGwCcCfgRtpNamePrefix_Type.__name__ = "SnmpAdminString"
_CMediaGwCcCfgRtpNamePrefix_Object = MibTableColumn
cMediaGwCcCfgRtpNamePrefix = _CMediaGwCcCfgRtpNamePrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 7, 1, 13),
    _CMediaGwCcCfgRtpNamePrefix_Type()
)
cMediaGwCcCfgRtpNamePrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMediaGwCcCfgRtpNamePrefix.setStatus("current")


class _CMediaGwCcCfgAal1SvcNamePrefix_Type(SnmpAdminString):
    """Custom type cMediaGwCcCfgAal1SvcNamePrefix based on SnmpAdminString"""
    defaultHexValue = "41414C312F535643"

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CMediaGwCcCfgAal1SvcNamePrefix_Type.__name__ = "SnmpAdminString"
_CMediaGwCcCfgAal1SvcNamePrefix_Object = MibTableColumn
cMediaGwCcCfgAal1SvcNamePrefix = _CMediaGwCcCfgAal1SvcNamePrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 7, 1, 14),
    _CMediaGwCcCfgAal1SvcNamePrefix_Type()
)
cMediaGwCcCfgAal1SvcNamePrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMediaGwCcCfgAal1SvcNamePrefix.setStatus("current")


class _CMediaGwCcCfgAal2SvcNamePrefix_Type(SnmpAdminString):
    """Custom type cMediaGwCcCfgAal2SvcNamePrefix based on SnmpAdminString"""
    defaultHexValue = "41414C322F535643"

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CMediaGwCcCfgAal2SvcNamePrefix_Type.__name__ = "SnmpAdminString"
_CMediaGwCcCfgAal2SvcNamePrefix_Object = MibTableColumn
cMediaGwCcCfgAal2SvcNamePrefix = _CMediaGwCcCfgAal2SvcNamePrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 7, 1, 15),
    _CMediaGwCcCfgAal2SvcNamePrefix_Type()
)
cMediaGwCcCfgAal2SvcNamePrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMediaGwCcCfgAal2SvcNamePrefix.setStatus("current")


class _CMediaGwCcCfgClusterEnabled_Type(Integer32):
    """Custom type cMediaGwCcCfgClusterEnabled based on Integer32"""
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
        *(("conditionalEnabled", 3),
          ("disabled", 1),
          ("enabled", 2))
    )


_CMediaGwCcCfgClusterEnabled_Type.__name__ = "Integer32"
_CMediaGwCcCfgClusterEnabled_Object = MibTableColumn
cMediaGwCcCfgClusterEnabled = _CMediaGwCcCfgClusterEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 7, 1, 16),
    _CMediaGwCcCfgClusterEnabled_Type()
)
cMediaGwCcCfgClusterEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMediaGwCcCfgClusterEnabled.setStatus("current")


class _CMediaGwCcCfgDefBearerTraffic_Type(Integer32):
    """Custom type cMediaGwCcCfgDefBearerTraffic based on Integer32"""
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
        *(("atmPvcAal2", 2),
          ("atmSvcAal1", 4),
          ("atmSvcAal2", 3),
          ("ipPvcAal5", 1))
    )


_CMediaGwCcCfgDefBearerTraffic_Type.__name__ = "Integer32"
_CMediaGwCcCfgDefBearerTraffic_Object = MibTableColumn
cMediaGwCcCfgDefBearerTraffic = _CMediaGwCcCfgDefBearerTraffic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 7, 1, 17),
    _CMediaGwCcCfgDefBearerTraffic_Type()
)
cMediaGwCcCfgDefBearerTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMediaGwCcCfgDefBearerTraffic.setStatus("current")


class _CMediaGwCcCfgDefRtpNamePrefix_Type(SnmpAdminString):
    """Custom type cMediaGwCcCfgDefRtpNamePrefix based on SnmpAdminString"""
    defaultHexValue = "544757525450"

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CMediaGwCcCfgDefRtpNamePrefix_Type.__name__ = "SnmpAdminString"
_CMediaGwCcCfgDefRtpNamePrefix_Object = MibTableColumn
cMediaGwCcCfgDefRtpNamePrefix = _CMediaGwCcCfgDefRtpNamePrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 1, 7, 1, 18),
    _CMediaGwCcCfgDefRtpNamePrefix_Type()
)
cMediaGwCcCfgDefRtpNamePrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMediaGwCcCfgDefRtpNamePrefix.setStatus("current")
_CMediaGwStats_ObjectIdentity = ObjectIdentity
cMediaGwStats = _CMediaGwStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 2)
)
_CMediaGwRscStatsTable_Object = MibTable
cMediaGwRscStatsTable = _CMediaGwRscStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cMediaGwRscStatsTable.setStatus("current")
_CMediaGwRscStatsEntry_Object = MibTableRow
cMediaGwRscStatsEntry = _CMediaGwRscStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 2, 1, 1)
)
cMediaGwRscStatsEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwRscStatsIndex"),
)
if mibBuilder.loadTexts:
    cMediaGwRscStatsEntry.setStatus("current")


class _CmgwRscStatsIndex_Type(Integer32):
    """Custom type cmgwRscStatsIndex based on Integer32"""
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
        *(("atmq", 7),
          ("callpersec", 12),
          ("commbuffer", 5),
          ("cpu", 1),
          ("dspq", 10),
          ("dynamicmemory", 3),
          ("h248congestion", 11),
          ("hugeipcbuffer", 16),
          ("largeipcbuffer", 15),
          ("mblkipcbuffer", 17),
          ("mediumipcbuffer", 14),
          ("msgq", 6),
          ("rsvpq", 9),
          ("smallipcbuffer", 13),
          ("staticmemory", 2),
          ("svccongestion", 8),
          ("sysmemory", 4))
    )


_CmgwRscStatsIndex_Type.__name__ = "Integer32"
_CmgwRscStatsIndex_Object = MibTableColumn
cmgwRscStatsIndex = _CmgwRscStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 2, 1, 1, 1),
    _CmgwRscStatsIndex_Type()
)
cmgwRscStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmgwRscStatsIndex.setStatus("current")
_CmgwRscMaximumUtilization_Type = Gauge32
_CmgwRscMaximumUtilization_Object = MibTableColumn
cmgwRscMaximumUtilization = _CmgwRscMaximumUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 2, 1, 1, 2),
    _CmgwRscMaximumUtilization_Type()
)
cmgwRscMaximumUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgwRscMaximumUtilization.setStatus("current")
_CmgwRscMinimumUtilization_Type = Gauge32
_CmgwRscMinimumUtilization_Object = MibTableColumn
cmgwRscMinimumUtilization = _CmgwRscMinimumUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 2, 1, 1, 3),
    _CmgwRscMinimumUtilization_Type()
)
cmgwRscMinimumUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgwRscMinimumUtilization.setStatus("current")
_CmgwRscAverageUtilization_Type = Gauge32
_CmgwRscAverageUtilization_Object = MibTableColumn
cmgwRscAverageUtilization = _CmgwRscAverageUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 2, 1, 1, 4),
    _CmgwRscAverageUtilization_Type()
)
cmgwRscAverageUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgwRscAverageUtilization.setStatus("current")
_CmgwRscSinceLastReset_Type = Unsigned32
_CmgwRscSinceLastReset_Object = MibTableColumn
cmgwRscSinceLastReset = _CmgwRscSinceLastReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 1, 2, 1, 1, 5),
    _CmgwRscSinceLastReset_Type()
)
cmgwRscSinceLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmgwRscSinceLastReset.setStatus("current")
if mibBuilder.loadTexts:
    cmgwRscSinceLastReset.setUnits("seconds")
_CMediaGwMIBConformance_ObjectIdentity = ObjectIdentity
cMediaGwMIBConformance = _CMediaGwMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 2)
)
_CMediaGwMIBCompliances_ObjectIdentity = ObjectIdentity
cMediaGwMIBCompliances = _CMediaGwMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 2, 1)
)
_CMediaGwMIBGroups_ObjectIdentity = ObjectIdentity
cMediaGwMIBGroups = _CMediaGwMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 2, 2)
)

# Managed Objects groups

cMediaGwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 2, 2, 1)
)
cMediaGwGroup.setObjects(
      *(("CISCO-MEDIA-GATEWAY-MIB", "cmgwDomainName"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwPhysicalIndex"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwServiceState"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwAdminState"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwGraceTime"))
)
if mibBuilder.loadTexts:
    cMediaGwGroup.setStatus("deprecated")

cmgwSignalProtocolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 2, 2, 2)
)
cmgwSignalProtocolGroup.setObjects(
      *(("CISCO-MEDIA-GATEWAY-MIB", "cmgwSignalProtocol"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwSignalProtocolVersion"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwSignalProtocolPort"))
)
if mibBuilder.loadTexts:
    cmgwSignalProtocolGroup.setStatus("deprecated")

cmgwDomainNameGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 2, 2, 3)
)
cmgwDomainNameGroup.setObjects(
      *(("CISCO-MEDIA-GATEWAY-MIB", "cmgwConfigDomainNameEntity"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwConfigDomainName"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwConfigDomainNameRowStatus"))
)
if mibBuilder.loadTexts:
    cmgwDomainNameGroup.setStatus("current")

cMediaGwIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 2, 2, 4)
)
cMediaGwIpGroup.setObjects(
      *(("CISCO-MEDIA-GATEWAY-MIB", "cmgwIpConfigIfIndex"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwIpConfigVpi"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwIpConfigVci"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwIpConfigAddrType"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwIpConfigAddress"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwIpConfigSubnetMask"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwIpConfigDefaultGwIp"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwIpConfigForRemoteMapping"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwIpConfigRowStatus"))
)
if mibBuilder.loadTexts:
    cMediaGwIpGroup.setStatus("current")

cmgwDnsIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 2, 2, 5)
)
cmgwDnsIpGroup.setObjects(
      *(("CISCO-MEDIA-GATEWAY-MIB", "cmgwDnsDomainName"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwDnsIp"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwDnsIpType"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwDnsIpRowStatus"))
)
if mibBuilder.loadTexts:
    cmgwDnsIpGroup.setStatus("current")

cmgwLifGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 2, 2, 6)
)
cmgwLifGroup.setObjects(
      *(("CISCO-MEDIA-GATEWAY-MIB", "cmgwLifPvcCount"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwLifVoiceIfCount"))
)
if mibBuilder.loadTexts:
    cmgwLifGroup.setStatus("current")

cmgwCallControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 2, 2, 7)
)
cmgwCallControlGroup.setObjects(
      *(("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgControlTos"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgBearerTos"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgNtePayload"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgNsePayload"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgNseRespTimer"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgVbdJitterDelayMode"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgVbdJitterMaxDelay"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgVbdJitterNomDelay"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgVbdJitterMinDelay"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgDefaultTonePlanId"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgDescrInfoEnabled"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgDsNamePrefix"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgRtpNamePrefix"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgAal1SvcNamePrefix"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgAal2SvcNamePrefix"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgClusterEnabled"))
)
if mibBuilder.loadTexts:
    cmgwCallControlGroup.setStatus("deprecated")

cMediaGwGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 2, 2, 8)
)
cMediaGwGroupRev1.setObjects(
      *(("CISCO-MEDIA-GATEWAY-MIB", "cmgwDomainName"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwPhysicalIndex"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwServiceState"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwAdminState"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwGraceTime"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwVtMappingMode"))
)
if mibBuilder.loadTexts:
    cMediaGwGroupRev1.setStatus("current")

cmgwCallControlGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 2, 2, 9)
)
cmgwCallControlGroupRev1.setObjects(
      *(("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgControlTos"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgBearerTos"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgNtePayload"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgNsePayload"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgNseRespTimer"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgVbdJitterDelayMode"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgVbdJitterMaxDelay"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgVbdJitterNomDelay"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgVbdJitterMinDelay"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgDefaultTonePlanId"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgDescrInfoEnabled"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgDsNamePrefix"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgRtpNamePrefix"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgAal1SvcNamePrefix"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgAal2SvcNamePrefix"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgClusterEnabled"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgDefBearerTraffic"))
)
if mibBuilder.loadTexts:
    cmgwCallControlGroupRev1.setStatus("current")

cmgwSignalProtocolGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 2, 2, 10)
)
cmgwSignalProtocolGroupRev1.setObjects(
      *(("CISCO-MEDIA-GATEWAY-MIB", "cmgwSignalProtocol"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwSignalProtocolVersion"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwSignalProtocolPort"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwSignalMgcProtocolPort"))
)
if mibBuilder.loadTexts:
    cmgwSignalProtocolGroupRev1.setStatus("deprecated")

cmgwSignalProtocolGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 2, 2, 11)
)
cmgwSignalProtocolGroupRev2.setObjects(
      *(("CISCO-MEDIA-GATEWAY-MIB", "cmgwSignalProtocol"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwSignalProtocolVersion"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwSignalProtocolPort"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwSignalMgcProtocolPort"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwSignalProtocolPreference"))
)
if mibBuilder.loadTexts:
    cmgwSignalProtocolGroupRev2.setStatus("current")

cmgwSignalProtocolGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 2, 2, 12)
)
cmgwSignalProtocolGroupRev3.setObjects(
    ("CISCO-MEDIA-GATEWAY-MIB", "cmgwSignalProtocolConfigVer")
)
if mibBuilder.loadTexts:
    cmgwSignalProtocolGroupRev3.setStatus("current")

cMediaGwRscStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 2, 2, 13)
)
cMediaGwRscStatsGroup.setObjects(
      *(("CISCO-MEDIA-GATEWAY-MIB", "cmgwRscMaximumUtilization"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwRscMinimumUtilization"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwRscAverageUtilization"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwRscSinceLastReset"))
)
if mibBuilder.loadTexts:
    cMediaGwRscStatsGroup.setStatus("current")

cMediaGwGroupExtra = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 2, 2, 14)
)
cMediaGwGroupExtra.setObjects(
      *(("CISCO-MEDIA-GATEWAY-MIB", "cmgwSrcFilterEnabled"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwLawInterceptEnabled"))
)
if mibBuilder.loadTexts:
    cMediaGwGroupExtra.setStatus("current")

cmgwCallControlGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 2, 2, 15)
)
cmgwCallControlGroupRev2.setObjects(
      *(("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgControlTos"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgBearerTos"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgNtePayload"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgNsePayload"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgNseRespTimer"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgVbdJitterDelayMode"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgVbdJitterMaxDelay"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgVbdJitterNomDelay"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgVbdJitterMinDelay"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgDefaultTonePlanId"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgDescrInfoEnabled"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgDsNamePrefix"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgRtpNamePrefix"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgAal1SvcNamePrefix"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgAal2SvcNamePrefix"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgClusterEnabled"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgDefBearerTraffic"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cMediaGwCcCfgDefRtpNamePrefix"))
)
if mibBuilder.loadTexts:
    cmgwCallControlGroupRev2.setStatus("current")

cMediaGwGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 2, 2, 16)
)
cMediaGwGroupRev2.setObjects(
      *(("CISCO-MEDIA-GATEWAY-MIB", "cmgwDomainName"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwPhysicalIndex"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwServiceState"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwAdminState"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwGraceTime"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwVtMappingMode"),
        ("CISCO-MEDIA-GATEWAY-MIB", "cmgwV23Enabled"))
)
if mibBuilder.loadTexts:
    cMediaGwGroupRev2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cMediaGwMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cMediaGwMIBCompliance.setStatus(
        "deprecated"
    )

cMediaGwMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cMediaGwMIBComplianceRev1.setStatus(
        "deprecated"
    )

cMediaGwMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 2, 1, 3)
)
if mibBuilder.loadTexts:
    cMediaGwMIBComplianceRev2.setStatus(
        "deprecated"
    )

cMediaGwMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 2, 1, 4)
)
if mibBuilder.loadTexts:
    cMediaGwMIBComplianceRev3.setStatus(
        "current"
    )

cMediaGwMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 2, 1, 5)
)
if mibBuilder.loadTexts:
    cMediaGwMIBComplianceRev4.setStatus(
        "deprecated"
    )

cMediaGwMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 324, 2, 1, 6)
)
if mibBuilder.loadTexts:
    cMediaGwMIBComplianceRev5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MEDIA-GATEWAY-MIB",
    **{"CGwServiceState": CGwServiceState,
       "CGwAdminState": CGwAdminState,
       "GatewayLifNumber": GatewayLifNumber,
       "CVoiceTonePlanIndex": CVoiceTonePlanIndex,
       "CVoiceTonePlanIndexOrZero": CVoiceTonePlanIndexOrZero,
       "CCallControlProfileIndex": CCallControlProfileIndex,
       "CCallControlProfileIndexOrZero": CCallControlProfileIndexOrZero,
       "CCallControlJitterDelayMode": CCallControlJitterDelayMode,
       "ciscoMediaGatewayMIB": ciscoMediaGatewayMIB,
       "ciscoMediaGatewayMIBNotifs": ciscoMediaGatewayMIBNotifs,
       "ciscoMediaGatewayMIBObjects": ciscoMediaGatewayMIBObjects,
       "cMediaGwConfig": cMediaGwConfig,
       "cMediaGwTable": cMediaGwTable,
       "cMediaGwEntry": cMediaGwEntry,
       "cmgwIndex": cmgwIndex,
       "cmgwDomainName": cmgwDomainName,
       "cmgwPhysicalIndex": cmgwPhysicalIndex,
       "cmgwServiceState": cmgwServiceState,
       "cmgwAdminState": cmgwAdminState,
       "cmgwGraceTime": cmgwGraceTime,
       "cmgwVtMappingMode": cmgwVtMappingMode,
       "cmgwSrcFilterEnabled": cmgwSrcFilterEnabled,
       "cmgwLawInterceptEnabled": cmgwLawInterceptEnabled,
       "cmgwV23Enabled": cmgwV23Enabled,
       "cmgwSignalProtocolTable": cmgwSignalProtocolTable,
       "cmgwSignalProtocolEntry": cmgwSignalProtocolEntry,
       "cmgwSignalProtocolIndex": cmgwSignalProtocolIndex,
       "cmgwSignalProtocol": cmgwSignalProtocol,
       "cmgwSignalProtocolVersion": cmgwSignalProtocolVersion,
       "cmgwSignalProtocolPort": cmgwSignalProtocolPort,
       "cmgwSignalMgcProtocolPort": cmgwSignalMgcProtocolPort,
       "cmgwSignalProtocolPreference": cmgwSignalProtocolPreference,
       "cmgwSignalProtocolConfigVer": cmgwSignalProtocolConfigVer,
       "cMediaGwIpConfigTable": cMediaGwIpConfigTable,
       "cMediaGwIpConfigEntry": cMediaGwIpConfigEntry,
       "cmgwIpConfigIndex": cmgwIpConfigIndex,
       "cmgwIpConfigIfIndex": cmgwIpConfigIfIndex,
       "cmgwIpConfigVpi": cmgwIpConfigVpi,
       "cmgwIpConfigVci": cmgwIpConfigVci,
       "cmgwIpConfigAddrType": cmgwIpConfigAddrType,
       "cmgwIpConfigAddress": cmgwIpConfigAddress,
       "cmgwIpConfigSubnetMask": cmgwIpConfigSubnetMask,
       "cmgwIpConfigDefaultGwIp": cmgwIpConfigDefaultGwIp,
       "cmgwIpConfigForRemoteMapping": cmgwIpConfigForRemoteMapping,
       "cmgwIpConfigRowStatus": cmgwIpConfigRowStatus,
       "cMediaGwDomainNameConfigTable": cMediaGwDomainNameConfigTable,
       "cMediaGwDomainNameConfigEntry": cMediaGwDomainNameConfigEntry,
       "cmgwConfigDomainNameIndex": cmgwConfigDomainNameIndex,
       "cmgwConfigDomainNameEntity": cmgwConfigDomainNameEntity,
       "cmgwConfigDomainName": cmgwConfigDomainName,
       "cmgwConfigDomainNameRowStatus": cmgwConfigDomainNameRowStatus,
       "cMediaGwDnsIpConfigTable": cMediaGwDnsIpConfigTable,
       "cMediaGwDnsIpConfigEntry": cMediaGwDnsIpConfigEntry,
       "cmgwDnsIpIndex": cmgwDnsIpIndex,
       "cmgwDnsDomainName": cmgwDnsDomainName,
       "cmgwDnsIpType": cmgwDnsIpType,
       "cmgwDnsIp": cmgwDnsIp,
       "cmgwDnsIpRowStatus": cmgwDnsIpRowStatus,
       "cmgwLifTable": cmgwLifTable,
       "cmgwLifEntry": cmgwLifEntry,
       "cmgwLifNumber": cmgwLifNumber,
       "cmgwLifPvcCount": cmgwLifPvcCount,
       "cmgwLifVoiceIfCount": cmgwLifVoiceIfCount,
       "cMediaGwCallControlConfigTable": cMediaGwCallControlConfigTable,
       "cMediaGwCallControlConfigEntry": cMediaGwCallControlConfigEntry,
       "cMediaGwCcCfgControlTos": cMediaGwCcCfgControlTos,
       "cMediaGwCcCfgBearerTos": cMediaGwCcCfgBearerTos,
       "cMediaGwCcCfgNtePayload": cMediaGwCcCfgNtePayload,
       "cMediaGwCcCfgNsePayload": cMediaGwCcCfgNsePayload,
       "cMediaGwCcCfgNseRespTimer": cMediaGwCcCfgNseRespTimer,
       "cMediaGwCcCfgVbdJitterDelayMode": cMediaGwCcCfgVbdJitterDelayMode,
       "cMediaGwCcCfgVbdJitterMaxDelay": cMediaGwCcCfgVbdJitterMaxDelay,
       "cMediaGwCcCfgVbdJitterNomDelay": cMediaGwCcCfgVbdJitterNomDelay,
       "cMediaGwCcCfgVbdJitterMinDelay": cMediaGwCcCfgVbdJitterMinDelay,
       "cMediaGwCcCfgDefaultTonePlanId": cMediaGwCcCfgDefaultTonePlanId,
       "cMediaGwCcCfgDescrInfoEnabled": cMediaGwCcCfgDescrInfoEnabled,
       "cMediaGwCcCfgDsNamePrefix": cMediaGwCcCfgDsNamePrefix,
       "cMediaGwCcCfgRtpNamePrefix": cMediaGwCcCfgRtpNamePrefix,
       "cMediaGwCcCfgAal1SvcNamePrefix": cMediaGwCcCfgAal1SvcNamePrefix,
       "cMediaGwCcCfgAal2SvcNamePrefix": cMediaGwCcCfgAal2SvcNamePrefix,
       "cMediaGwCcCfgClusterEnabled": cMediaGwCcCfgClusterEnabled,
       "cMediaGwCcCfgDefBearerTraffic": cMediaGwCcCfgDefBearerTraffic,
       "cMediaGwCcCfgDefRtpNamePrefix": cMediaGwCcCfgDefRtpNamePrefix,
       "cMediaGwStats": cMediaGwStats,
       "cMediaGwRscStatsTable": cMediaGwRscStatsTable,
       "cMediaGwRscStatsEntry": cMediaGwRscStatsEntry,
       "cmgwRscStatsIndex": cmgwRscStatsIndex,
       "cmgwRscMaximumUtilization": cmgwRscMaximumUtilization,
       "cmgwRscMinimumUtilization": cmgwRscMinimumUtilization,
       "cmgwRscAverageUtilization": cmgwRscAverageUtilization,
       "cmgwRscSinceLastReset": cmgwRscSinceLastReset,
       "cMediaGwMIBConformance": cMediaGwMIBConformance,
       "cMediaGwMIBCompliances": cMediaGwMIBCompliances,
       "cMediaGwMIBCompliance": cMediaGwMIBCompliance,
       "cMediaGwMIBComplianceRev1": cMediaGwMIBComplianceRev1,
       "cMediaGwMIBComplianceRev2": cMediaGwMIBComplianceRev2,
       "cMediaGwMIBComplianceRev3": cMediaGwMIBComplianceRev3,
       "cMediaGwMIBComplianceRev4": cMediaGwMIBComplianceRev4,
       "cMediaGwMIBComplianceRev5": cMediaGwMIBComplianceRev5,
       "cMediaGwMIBGroups": cMediaGwMIBGroups,
       "cMediaGwGroup": cMediaGwGroup,
       "cmgwSignalProtocolGroup": cmgwSignalProtocolGroup,
       "cmgwDomainNameGroup": cmgwDomainNameGroup,
       "cMediaGwIpGroup": cMediaGwIpGroup,
       "cmgwDnsIpGroup": cmgwDnsIpGroup,
       "cmgwLifGroup": cmgwLifGroup,
       "cmgwCallControlGroup": cmgwCallControlGroup,
       "cMediaGwGroupRev1": cMediaGwGroupRev1,
       "cmgwCallControlGroupRev1": cmgwCallControlGroupRev1,
       "cmgwSignalProtocolGroupRev1": cmgwSignalProtocolGroupRev1,
       "cmgwSignalProtocolGroupRev2": cmgwSignalProtocolGroupRev2,
       "cmgwSignalProtocolGroupRev3": cmgwSignalProtocolGroupRev3,
       "cMediaGwRscStatsGroup": cMediaGwRscStatsGroup,
       "cMediaGwGroupExtra": cMediaGwGroupExtra,
       "cmgwCallControlGroupRev2": cmgwCallControlGroupRev2,
       "cMediaGwGroupRev2": cMediaGwGroupRev2}
)
