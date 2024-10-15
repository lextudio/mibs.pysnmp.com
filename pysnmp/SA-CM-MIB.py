# SNMP MIB module (SA-CM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SA-CM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:13 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TAddress,
 TDomain,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

saCmMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 77)
)
saCmMib.setRevisions(
        ("2016-05-18 00:00",
         "2015-05-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sa_ObjectIdentity = ObjectIdentity
sa = _Sa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429)
)
_DpxCmMibObjects_ObjectIdentity = ObjectIdentity
dpxCmMibObjects = _DpxCmMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1)
)
_CmVendorInfo_ObjectIdentity = ObjectIdentity
cmVendorInfo = _CmVendorInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 2)
)


class _VendorDefaultDSfreq_Type(Integer32):
    """Custom type vendorDefaultDSfreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(93000000, 855000000),
    )


_VendorDefaultDSfreq_Type.__name__ = "Integer32"
_VendorDefaultDSfreq_Object = MibScalar
vendorDefaultDSfreq = _VendorDefaultDSfreq_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 2, 6),
    _VendorDefaultDSfreq_Type()
)
vendorDefaultDSfreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vendorDefaultDSfreq.setStatus("current")


class _VendorDSLEDTreatment_Type(Integer32):
    """Custom type vendorDSLEDTreatment based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("signalNB", 0),
          ("signalWB", 1),
          ("signalWBNBA", 3),
          ("signalWBNBG", 2))
    )


_VendorDSLEDTreatment_Type.__name__ = "Integer32"
_VendorDSLEDTreatment_Object = MibScalar
vendorDSLEDTreatment = _VendorDSLEDTreatment_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 2, 7),
    _VendorDSLEDTreatment_Type()
)
vendorDSLEDTreatment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vendorDSLEDTreatment.setStatus("current")


class _VendorLINKLEDTreatment_Type(Integer32):
    """Custom type vendorLINKLEDTreatment based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("d3Amberledslowspeed", 2),
          ("d3Greenledslowspeed", 3),
          ("default", 0),
          ("showlinkspeed", 1))
    )


_VendorLINKLEDTreatment_Type.__name__ = "Integer32"
_VendorLINKLEDTreatment_Object = MibScalar
vendorLINKLEDTreatment = _VendorLINKLEDTreatment_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 2, 8),
    _VendorLINKLEDTreatment_Type()
)
vendorLINKLEDTreatment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vendorLINKLEDTreatment.setStatus("current")


class _VendorUSLEDTreatment_Type(Integer32):
    """Custom type vendorUSLEDTreatment based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("signalNB", 1),
          ("signalWB", 2),
          ("signalWBNBA", 3),
          ("signalWBNBG", 0))
    )


_VendorUSLEDTreatment_Type.__name__ = "Integer32"
_VendorUSLEDTreatment_Object = MibScalar
vendorUSLEDTreatment = _VendorUSLEDTreatment_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 2, 9),
    _VendorUSLEDTreatment_Type()
)
vendorUSLEDTreatment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vendorUSLEDTreatment.setStatus("current")


class _VendorONLINELEDTreatment_Type(Integer32):
    """Custom type vendorONLINELEDTreatment based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("signalNB", 1),
          ("signalWB", 2),
          ("signalWBNBA", 3),
          ("signalWBNBG", 0))
    )


_VendorONLINELEDTreatment_Type.__name__ = "Integer32"
_VendorONLINELEDTreatment_Object = MibScalar
vendorONLINELEDTreatment = _VendorONLINELEDTreatment_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 2, 10),
    _VendorONLINELEDTreatment_Type()
)
vendorONLINELEDTreatment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vendorONLINELEDTreatment.setStatus("current")
_CmAPInfo_ObjectIdentity = ObjectIdentity
cmAPInfo = _CmAPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 3)
)


class _CmAPIgmp_Type(Integer32):
    """Custom type cmAPIgmp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disableIGMP", 0),
          ("enableIGMP", 1))
    )


_CmAPIgmp_Type.__name__ = "Integer32"
_CmAPIgmp_Object = MibScalar
cmAPIgmp = _CmAPIgmp_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 3, 1),
    _CmAPIgmp_Type()
)
cmAPIgmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmAPIgmp.setStatus("current")


class _CmAPAgingOut_Type(Integer32):
    """Custom type cmAPAgingOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disableAgingOut", 0),
          ("enableAgingOut", 1))
    )


_CmAPAgingOut_Type.__name__ = "Integer32"
_CmAPAgingOut_Object = MibScalar
cmAPAgingOut = _CmAPAgingOut_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 3, 4),
    _CmAPAgingOut_Type()
)
cmAPAgingOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmAPAgingOut.setStatus("current")


class _CmAPMulticastPromiscuousMode_Type(Integer32):
    """Custom type cmAPMulticastPromiscuousMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_CmAPMulticastPromiscuousMode_Type.__name__ = "Integer32"
_CmAPMulticastPromiscuousMode_Object = MibScalar
cmAPMulticastPromiscuousMode = _CmAPMulticastPromiscuousMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 3, 13),
    _CmAPMulticastPromiscuousMode_Type()
)
cmAPMulticastPromiscuousMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmAPMulticastPromiscuousMode.setStatus("current")


class _CmAPInternalInterface_Type(Integer32):
    """Custom type cmAPInternalInterface based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_CmAPInternalInterface_Type.__name__ = "Integer32"
_CmAPInternalInterface_Object = MibScalar
cmAPInternalInterface = _CmAPInternalInterface_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 3, 15),
    _CmAPInternalInterface_Type()
)
cmAPInternalInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmAPInternalInterface.setStatus("current")
_CmAPFactoryReset_Type = TruthValue
_CmAPFactoryReset_Object = MibScalar
cmAPFactoryReset = _CmAPFactoryReset_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 3, 18),
    _CmAPFactoryReset_Type()
)
cmAPFactoryReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmAPFactoryReset.setStatus("current")


class _SaCmArpRateLimit_Type(Integer32):
    """Custom type saCmArpRateLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SaCmArpRateLimit_Type.__name__ = "Integer32"
_SaCmArpRateLimit_Object = MibScalar
saCmArpRateLimit = _SaCmArpRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 3, 19),
    _SaCmArpRateLimit_Type()
)
saCmArpRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saCmArpRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    saCmArpRateLimit.setUnits("packets-per-second")


class _SaCmInternalDhcpServer_Type(Integer32):
    """Custom type saCmInternalDhcpServer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SaCmInternalDhcpServer_Type.__name__ = "Integer32"
_SaCmInternalDhcpServer_Object = MibScalar
saCmInternalDhcpServer = _SaCmInternalDhcpServer_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 3, 20),
    _SaCmInternalDhcpServer_Type()
)
saCmInternalDhcpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saCmInternalDhcpServer.setStatus("current")
_CmInterfaceInfo_ObjectIdentity = ObjectIdentity
cmInterfaceInfo = _CmInterfaceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 4)
)


class _CmConsoleMode_Type(Integer32):
    """Custom type cmConsoleMode based on Integer32"""
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
        *(("disable", 0),
          ("readOnly", 1),
          ("readWrite", 2))
    )


_CmConsoleMode_Type.__name__ = "Integer32"
_CmConsoleMode_Object = MibScalar
cmConsoleMode = _CmConsoleMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 4, 7),
    _CmConsoleMode_Type()
)
cmConsoleMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmConsoleMode.setStatus("current")


class _CmTimerT4_Type(Integer32):
    """Custom type cmTimerT4 based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 60),
    )


_CmTimerT4_Type.__name__ = "Integer32"
_CmTimerT4_Object = MibScalar
cmTimerT4 = _CmTimerT4_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 4, 8),
    _CmTimerT4_Type()
)
cmTimerT4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmTimerT4.setStatus("current")
if mibBuilder.loadTexts:
    cmTimerT4.setUnits("seconds")


class _SaCmTodRenewal_Type(Integer32):
    """Custom type saCmTodRenewal based on Integer32"""
    defaultValue = 0


_SaCmTodRenewal_Object = MibScalar
saCmTodRenewal = _SaCmTodRenewal_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 4, 9),
    _SaCmTodRenewal_Type()
)
saCmTodRenewal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saCmTodRenewal.setStatus("current")
if mibBuilder.loadTexts:
    saCmTodRenewal.setUnits("hours")


class _SaCmAutoResetNoActivity_Type(Integer32):
    """Custom type saCmAutoResetNoActivity based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 43200),
    )


_SaCmAutoResetNoActivity_Type.__name__ = "Integer32"
_SaCmAutoResetNoActivity_Object = MibScalar
saCmAutoResetNoActivity = _SaCmAutoResetNoActivity_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 4, 10),
    _SaCmAutoResetNoActivity_Type()
)
saCmAutoResetNoActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saCmAutoResetNoActivity.setStatus("current")
if mibBuilder.loadTexts:
    saCmAutoResetNoActivity.setUnits("minutes")


class _SaCmCpeMacAging_Type(Integer32):
    """Custom type saCmCpeMacAging based on Integer32"""
    defaultValue = 0


_SaCmCpeMacAging_Object = MibScalar
saCmCpeMacAging = _SaCmCpeMacAging_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 4, 11),
    _SaCmCpeMacAging_Type()
)
saCmCpeMacAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saCmCpeMacAging.setStatus("current")
if mibBuilder.loadTexts:
    saCmCpeMacAging.setUnits("seconds")


class _SaCmBpiForward_Type(Integer32):
    """Custom type saCmBpiForward based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allPackets", 2),
          ("macTable", 1))
    )


_SaCmBpiForward_Type.__name__ = "Integer32"
_SaCmBpiForward_Object = MibScalar
saCmBpiForward = _SaCmBpiForward_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 4, 12),
    _SaCmBpiForward_Type()
)
saCmBpiForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saCmBpiForward.setStatus("current")


class _SaCmForceDualscan_Type(Integer32):
    """Custom type saCmForceDualscan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("docsis1", 2),
          ("enable", 1),
          ("euroDocsis", 3),
          ("useFactorySetting", 0))
    )


_SaCmForceDualscan_Type.__name__ = "Integer32"
_SaCmForceDualscan_Object = MibScalar
saCmForceDualscan = _SaCmForceDualscan_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 4, 14),
    _SaCmForceDualscan_Type()
)
saCmForceDualscan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saCmForceDualscan.setStatus("current")


class _SaCmDsBonding_Type(Integer32):
    """Custom type saCmDsBonding based on Integer32"""
    defaultValue = 1

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("enable2DS", 2),
          ("enable3DS", 3),
          ("enable4DS", 4),
          ("enable5DS", 5),
          ("enable6DS", 6),
          ("enable7DS", 7),
          ("enable8DS", 8))
    )


_SaCmDsBonding_Type.__name__ = "Integer32"
_SaCmDsBonding_Object = MibScalar
saCmDsBonding = _SaCmDsBonding_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 4, 15),
    _SaCmDsBonding_Type()
)
saCmDsBonding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saCmDsBonding.setStatus("current")
_SaCmDocsisCapableVersion_Type = SnmpAdminString
_SaCmDocsisCapableVersion_Object = MibScalar
saCmDocsisCapableVersion = _SaCmDocsisCapableVersion_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 4, 33),
    _SaCmDocsisCapableVersion_Type()
)
saCmDocsisCapableVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saCmDocsisCapableVersion.setStatus("current")


class _SaOorDsidOverride_Type(Integer32):
    """Custom type saOorDsidOverride based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SaOorDsidOverride_Type.__name__ = "Integer32"
_SaOorDsidOverride_Object = MibScalar
saOorDsidOverride = _SaOorDsidOverride_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 4, 34),
    _SaOorDsidOverride_Type()
)
saOorDsidOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saOorDsidOverride.setStatus("current")


class _SaCmCpeL2VpnMacAging_Type(Integer32):
    """Custom type saCmCpeL2VpnMacAging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SaCmCpeL2VpnMacAging_Type.__name__ = "Integer32"
_SaCmCpeL2VpnMacAging_Object = MibScalar
saCmCpeL2VpnMacAging = _SaCmCpeL2VpnMacAging_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 4, 39),
    _SaCmCpeL2VpnMacAging_Type()
)
saCmCpeL2VpnMacAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saCmCpeL2VpnMacAging.setStatus("current")


class _SaCmL2VpnUsForwardingCriteria_Type(Integer32):
    """Custom type saCmL2VpnUsForwardingCriteria based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("forwardOnPrimarySF", 0))
    )


_SaCmL2VpnUsForwardingCriteria_Type.__name__ = "Integer32"
_SaCmL2VpnUsForwardingCriteria_Object = MibScalar
saCmL2VpnUsForwardingCriteria = _SaCmL2VpnUsForwardingCriteria_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 4, 40),
    _SaCmL2VpnUsForwardingCriteria_Type()
)
saCmL2VpnUsForwardingCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saCmL2VpnUsForwardingCriteria.setStatus("current")
_CmEthernetOperTable_Object = MibTable
cmEthernetOperTable = _CmEthernetOperTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 4, 41)
)
if mibBuilder.loadTexts:
    cmEthernetOperTable.setStatus("current")
_CmEthernetOperEntry_Object = MibTableRow
cmEthernetOperEntry = _CmEthernetOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 4, 41, 1)
)
cmEthernetOperEntry.setIndexNames(
    (0, "SA-CM-MIB", "cmEthernetOperIndex"),
)
if mibBuilder.loadTexts:
    cmEthernetOperEntry.setStatus("current")


class _CmEthernetOperIndex_Type(Integer32):
    """Custom type cmEthernetOperIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CmEthernetOperIndex_Type.__name__ = "Integer32"
_CmEthernetOperIndex_Object = MibTableColumn
cmEthernetOperIndex = _CmEthernetOperIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 4, 41, 1, 1),
    _CmEthernetOperIndex_Type()
)
cmEthernetOperIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmEthernetOperIndex.setStatus("current")


class _CmEthernetOperSetting_Type(Integer32):
    """Custom type cmEthernetOperSetting based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("ethernetNotConnected", 5),
          ("full-duplex-100Mbps", 4),
          ("full-duplex-10Mbps", 2),
          ("full-duplex-1Gbps", 7),
          ("half-duplex-100Mbps", 3),
          ("half-duplex-10Mbps", 1),
          ("half-duplex-1Gbps", 6),
          ("link-down", 0))
    )


_CmEthernetOperSetting_Type.__name__ = "Integer32"
_CmEthernetOperSetting_Object = MibTableColumn
cmEthernetOperSetting = _CmEthernetOperSetting_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 4, 41, 1, 2),
    _CmEthernetOperSetting_Type()
)
cmEthernetOperSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetOperSetting.setStatus("current")


class _CmEthernetOperMode_Type(Integer32):
    """Custom type cmEthernetOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("auto-negotiate", 0),
          ("manual", 1))
    )


_CmEthernetOperMode_Type.__name__ = "Integer32"
_CmEthernetOperMode_Object = MibTableColumn
cmEthernetOperMode = _CmEthernetOperMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 4, 41, 1, 3),
    _CmEthernetOperMode_Type()
)
cmEthernetOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetOperMode.setStatus("current")


class _CmEthernetIfAdminStatus_Type(Integer32):
    """Custom type cmEthernetIfAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_CmEthernetIfAdminStatus_Type.__name__ = "Integer32"
_CmEthernetIfAdminStatus_Object = MibTableColumn
cmEthernetIfAdminStatus = _CmEthernetIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 4, 41, 1, 4),
    _CmEthernetIfAdminStatus_Type()
)
cmEthernetIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmEthernetIfAdminStatus.setStatus("current")


class _CmEthernetIfAdminOverride_Type(Integer32):
    """Custom type cmEthernetIfAdminOverride based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_CmEthernetIfAdminOverride_Type.__name__ = "Integer32"
_CmEthernetIfAdminOverride_Object = MibScalar
cmEthernetIfAdminOverride = _CmEthernetIfAdminOverride_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 4, 42),
    _CmEthernetIfAdminOverride_Type()
)
cmEthernetIfAdminOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmEthernetIfAdminOverride.setStatus("current")


class _SaCmUsBonding_Type(Integer32):
    """Custom type saCmUsBonding based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SaCmUsBonding_Type.__name__ = "Integer32"
_SaCmUsBonding_Object = MibScalar
saCmUsBonding = _SaCmUsBonding_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 4, 43),
    _SaCmUsBonding_Type()
)
saCmUsBonding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saCmUsBonding.setStatus("current")


class _SaCmIcmpRateLimit_Type(Integer32):
    """Custom type saCmIcmpRateLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SaCmIcmpRateLimit_Type.__name__ = "Integer32"
_SaCmIcmpRateLimit_Object = MibScalar
saCmIcmpRateLimit = _SaCmIcmpRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 4, 44),
    _SaCmIcmpRateLimit_Type()
)
saCmIcmpRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saCmIcmpRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    saCmIcmpRateLimit.setUnits("packets-per-second")


class _SaCmTftpBlockSizeV4_Type(Integer32):
    """Custom type saCmTftpBlockSizeV4 based on Integer32"""
    defaultValue = 0


_SaCmTftpBlockSizeV4_Object = MibScalar
saCmTftpBlockSizeV4 = _SaCmTftpBlockSizeV4_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 4, 46),
    _SaCmTftpBlockSizeV4_Type()
)
saCmTftpBlockSizeV4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saCmTftpBlockSizeV4.setStatus("current")


class _SaCmTftpBlockSizeV6_Type(Integer32):
    """Custom type saCmTftpBlockSizeV6 based on Integer32"""
    defaultValue = 0


_SaCmTftpBlockSizeV6_Object = MibScalar
saCmTftpBlockSizeV6 = _SaCmTftpBlockSizeV6_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 4, 47),
    _SaCmTftpBlockSizeV6_Type()
)
saCmTftpBlockSizeV6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saCmTftpBlockSizeV6.setStatus("current")


class _SaCmUsPowerLimit_Type(Integer32):
    """Custom type saCmUsPowerLimit based on Integer32"""
    defaultValue = 51


_SaCmUsPowerLimit_Object = MibScalar
saCmUsPowerLimit = _SaCmUsPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 4, 48),
    _SaCmUsPowerLimit_Type()
)
saCmUsPowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saCmUsPowerLimit.setStatus("current")
_SaCmSoftwareDownload_ObjectIdentity = ObjectIdentity
saCmSoftwareDownload = _SaCmSoftwareDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 6)
)
_SaCmSoftwareTable_Object = MibTable
saCmSoftwareTable = _SaCmSoftwareTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 6, 1)
)
if mibBuilder.loadTexts:
    saCmSoftwareTable.setStatus("current")
_SaCmSoftwareEntry_Object = MibTableRow
saCmSoftwareEntry = _SaCmSoftwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 6, 1, 1)
)
saCmSoftwareEntry.setIndexNames(
    (0, "SA-CM-MIB", "saCmSwIndex"),
)
if mibBuilder.loadTexts:
    saCmSoftwareEntry.setStatus("current")


class _SaCmSwIndex_Type(Integer32):
    """Custom type saCmSwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_SaCmSwIndex_Type.__name__ = "Integer32"
_SaCmSwIndex_Object = MibTableColumn
saCmSwIndex = _SaCmSwIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 6, 1, 1, 1),
    _SaCmSwIndex_Type()
)
saCmSwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saCmSwIndex.setStatus("current")
_SaCmSwModel_Type = SnmpAdminString
_SaCmSwModel_Object = MibTableColumn
saCmSwModel = _SaCmSwModel_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 6, 1, 1, 2),
    _SaCmSwModel_Type()
)
saCmSwModel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saCmSwModel.setStatus("current")


class _SaCmSwHwVer_Type(SnmpAdminString):
    """Custom type saCmSwHwVer based on SnmpAdminString"""
    defaultValue = OctetString("any")


_SaCmSwHwVer_Object = MibTableColumn
saCmSwHwVer = _SaCmSwHwVer_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 6, 1, 1, 3),
    _SaCmSwHwVer_Type()
)
saCmSwHwVer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saCmSwHwVer.setStatus("current")


class _SaCmSwBootLoader_Type(SnmpAdminString):
    """Custom type saCmSwBootLoader based on SnmpAdminString"""
    defaultValue = OctetString("any")


_SaCmSwBootLoader_Object = MibTableColumn
saCmSwBootLoader = _SaCmSwBootLoader_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 6, 1, 1, 4),
    _SaCmSwBootLoader_Type()
)
saCmSwBootLoader.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saCmSwBootLoader.setStatus("current")


class _SaCmSwProtocol_Type(Integer32):
    """Custom type saCmSwProtocol based on Integer32"""
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
        *(("any", 0),
          ("ncs", 1),
          ("sip", 2))
    )


_SaCmSwProtocol_Type.__name__ = "Integer32"
_SaCmSwProtocol_Object = MibTableColumn
saCmSwProtocol = _SaCmSwProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 6, 1, 1, 5),
    _SaCmSwProtocol_Type()
)
saCmSwProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saCmSwProtocol.setStatus("current")


class _SaCmSwFilename_Type(SnmpAdminString):
    """Custom type saCmSwFilename based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SaCmSwFilename_Type.__name__ = "SnmpAdminString"
_SaCmSwFilename_Object = MibTableColumn
saCmSwFilename = _SaCmSwFilename_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 6, 1, 1, 6),
    _SaCmSwFilename_Type()
)
saCmSwFilename.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saCmSwFilename.setStatus("current")
_SaCmSwServer_Type = IpAddress
_SaCmSwServer_Object = MibTableColumn
saCmSwServer = _SaCmSwServer_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 6, 1, 1, 7),
    _SaCmSwServer_Type()
)
saCmSwServer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saCmSwServer.setStatus("deprecated")


class _SaCmSwAdminStatus_Type(Integer32):
    """Custom type saCmSwAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("saCmSwAllowProvisioningUpgrade", 2),
          ("saCmSwIgnoreProvisioningUpgrade", 3))
    )


_SaCmSwAdminStatus_Type.__name__ = "Integer32"
_SaCmSwAdminStatus_Object = MibTableColumn
saCmSwAdminStatus = _SaCmSwAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 6, 1, 1, 8),
    _SaCmSwAdminStatus_Type()
)
saCmSwAdminStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saCmSwAdminStatus.setStatus("current")


class _SaCmSwMethod_Type(Integer32):
    """Custom type saCmSwMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("secure", 1),
          ("unsecure", 2))
    )


_SaCmSwMethod_Type.__name__ = "Integer32"
_SaCmSwMethod_Object = MibTableColumn
saCmSwMethod = _SaCmSwMethod_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 6, 1, 1, 9),
    _SaCmSwMethod_Type()
)
saCmSwMethod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saCmSwMethod.setStatus("current")
_SaCmSwServerAddressType_Type = InetAddressType
_SaCmSwServerAddressType_Object = MibTableColumn
saCmSwServerAddressType = _SaCmSwServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 6, 1, 1, 11),
    _SaCmSwServerAddressType_Type()
)
saCmSwServerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saCmSwServerAddressType.setStatus("current")
_SaCmSwServerAddress_Type = InetAddress
_SaCmSwServerAddress_Object = MibTableColumn
saCmSwServerAddress = _SaCmSwServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 6, 1, 1, 12),
    _SaCmSwServerAddress_Type()
)
saCmSwServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saCmSwServerAddress.setStatus("current")


class _SaCmSoftwareDownloadTFTPServer_Type(Integer32):
    """Custom type saCmSoftwareDownloadTFTPServer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcpOption54", 2),
          ("sameAsCM", 1))
    )


_SaCmSoftwareDownloadTFTPServer_Type.__name__ = "Integer32"
_SaCmSoftwareDownloadTFTPServer_Object = MibScalar
saCmSoftwareDownloadTFTPServer = _SaCmSoftwareDownloadTFTPServer_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 6, 3),
    _SaCmSoftwareDownloadTFTPServer_Type()
)
saCmSoftwareDownloadTFTPServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saCmSoftwareDownloadTFTPServer.setStatus("current")
_SaCmWebAccess_ObjectIdentity = ObjectIdentity
saCmWebAccess = _SaCmWebAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 7)
)
_SaCmWebAccessUserIfTypeTable_Object = MibTable
saCmWebAccessUserIfTypeTable = _SaCmWebAccessUserIfTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 7, 2)
)
if mibBuilder.loadTexts:
    saCmWebAccessUserIfTypeTable.setStatus("current")
_SaCmWebAccessUserIfTypeEntry_Object = MibTableRow
saCmWebAccessUserIfTypeEntry = _SaCmWebAccessUserIfTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 7, 2, 1)
)
saCmWebAccessUserIfTypeEntry.setIndexNames(
    (0, "SA-CM-MIB", "saCmWebAccessUserTypeIndex"),
    (0, "SA-CM-MIB", "saCmWebAccessIfTypeIndex"),
)
if mibBuilder.loadTexts:
    saCmWebAccessUserIfTypeEntry.setStatus("current")


class _SaCmWebAccessUserTypeIndex_Type(Integer32):
    """Custom type saCmWebAccessUserTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              10,
              100)
        )
    )
    namedValues = NamedValues(
        *(("adv-user", 10),
          ("all-users", 100),
          ("cus-admin", 5),
          ("home-user", 1))
    )


_SaCmWebAccessUserTypeIndex_Type.__name__ = "Integer32"
_SaCmWebAccessUserTypeIndex_Object = MibTableColumn
saCmWebAccessUserTypeIndex = _SaCmWebAccessUserTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 7, 2, 1, 1),
    _SaCmWebAccessUserTypeIndex_Type()
)
saCmWebAccessUserTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saCmWebAccessUserTypeIndex.setStatus("current")


class _SaCmWebAccessIfTypeIndex_Type(Integer32):
    """Custom type saCmWebAccessIfTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              16,
              40,
              100)
        )
    )
    namedValues = NamedValues(
        *(("all-ifs", 100),
          ("lan", 1),
          ("mta", 16),
          ("rf-cm", 2),
          ("wan-rg", 40))
    )


_SaCmWebAccessIfTypeIndex_Type.__name__ = "Integer32"
_SaCmWebAccessIfTypeIndex_Object = MibTableColumn
saCmWebAccessIfTypeIndex = _SaCmWebAccessIfTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 7, 2, 1, 2),
    _SaCmWebAccessIfTypeIndex_Type()
)
saCmWebAccessIfTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saCmWebAccessIfTypeIndex.setStatus("current")


class _SaCmWebAccessUserIfLevel_Type(Integer32):
    """Custom type saCmWebAccessUserIfLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              100)
        )
    )
    namedValues = NamedValues(
        *(("advanced", 100),
          ("basic", 2),
          ("not-applicable", -1),
          ("off", 0),
          ("readonly", 3),
          ("system", 1))
    )


_SaCmWebAccessUserIfLevel_Type.__name__ = "Integer32"
_SaCmWebAccessUserIfLevel_Object = MibTableColumn
saCmWebAccessUserIfLevel = _SaCmWebAccessUserIfLevel_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 7, 2, 1, 3),
    _SaCmWebAccessUserIfLevel_Type()
)
saCmWebAccessUserIfLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saCmWebAccessUserIfLevel.setStatus("current")
_SaCmWebAccessHomeUsername_Type = SnmpAdminString
_SaCmWebAccessHomeUsername_Object = MibScalar
saCmWebAccessHomeUsername = _SaCmWebAccessHomeUsername_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 7, 3),
    _SaCmWebAccessHomeUsername_Type()
)
saCmWebAccessHomeUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saCmWebAccessHomeUsername.setStatus("current")
_SaCmWebAccessHomeUserPassword_Type = SnmpAdminString
_SaCmWebAccessHomeUserPassword_Object = MibScalar
saCmWebAccessHomeUserPassword = _SaCmWebAccessHomeUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 7, 4),
    _SaCmWebAccessHomeUserPassword_Type()
)
saCmWebAccessHomeUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saCmWebAccessHomeUserPassword.setStatus("current")


class _SaCmWebAccessAdvancedType_Type(Integer32):
    """Custom type saCmWebAccessAdvancedType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("plain", 1),
          ("potd", 2))
    )


_SaCmWebAccessAdvancedType_Type.__name__ = "Integer32"
_SaCmWebAccessAdvancedType_Object = MibScalar
saCmWebAccessAdvancedType = _SaCmWebAccessAdvancedType_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 7, 5),
    _SaCmWebAccessAdvancedType_Type()
)
saCmWebAccessAdvancedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saCmWebAccessAdvancedType.setStatus("current")


class _SaCmWebAccessAdvancedUsername_Type(SnmpAdminString):
    """Custom type saCmWebAccessAdvancedUsername based on SnmpAdminString"""
    defaultValue = OctetString("admin")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SaCmWebAccessAdvancedUsername_Type.__name__ = "SnmpAdminString"
_SaCmWebAccessAdvancedUsername_Object = MibScalar
saCmWebAccessAdvancedUsername = _SaCmWebAccessAdvancedUsername_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 7, 6),
    _SaCmWebAccessAdvancedUsername_Type()
)
saCmWebAccessAdvancedUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saCmWebAccessAdvancedUsername.setStatus("current")


class _SaCmWebAccessAdvancedPassword_Type(SnmpAdminString):
    """Custom type saCmWebAccessAdvancedPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SaCmWebAccessAdvancedPassword_Type.__name__ = "SnmpAdminString"
_SaCmWebAccessAdvancedPassword_Object = MibScalar
saCmWebAccessAdvancedPassword = _SaCmWebAccessAdvancedPassword_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 7, 7),
    _SaCmWebAccessAdvancedPassword_Type()
)
saCmWebAccessAdvancedPassword.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saCmWebAccessAdvancedPassword.setStatus("current")


class _SaCmWebAccessNoActivityTimeout_Type(Integer32):
    """Custom type saCmWebAccessNoActivityTimeout based on Integer32"""
    defaultValue = 900


_SaCmWebAccessNoActivityTimeout_Object = MibScalar
saCmWebAccessNoActivityTimeout = _SaCmWebAccessNoActivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 7, 8),
    _SaCmWebAccessNoActivityTimeout_Type()
)
saCmWebAccessNoActivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saCmWebAccessNoActivityTimeout.setStatus("current")
if mibBuilder.loadTexts:
    saCmWebAccessNoActivityTimeout.setUnits("seconds")


class _SaCmWebAccessHomeUserClearPassword_Type(TruthValue):
    """Custom type saCmWebAccessHomeUserClearPassword based on TruthValue"""


_SaCmWebAccessHomeUserClearPassword_Object = MibScalar
saCmWebAccessHomeUserClearPassword = _SaCmWebAccessHomeUserClearPassword_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 7, 9),
    _SaCmWebAccessHomeUserClearPassword_Type()
)
saCmWebAccessHomeUserClearPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saCmWebAccessHomeUserClearPassword.setStatus("current")
_SaPUF_ObjectIdentity = ObjectIdentity
saPUF = _SaPUF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 10)
)
_SaPUFTable_Object = MibTable
saPUFTable = _SaPUFTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 10, 1)
)
if mibBuilder.loadTexts:
    saPUFTable.setStatus("current")
_SaPUFEntry_Object = MibTableRow
saPUFEntry = _SaPUFEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 10, 1, 1)
)
saPUFEntry.setIndexNames(
    (0, "SA-CM-MIB", "saPUFIndex"),
)
if mibBuilder.loadTexts:
    saPUFEntry.setStatus("current")


class _SaPUFIndex_Type(Integer32):
    """Custom type saPUFIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SaPUFIndex_Type.__name__ = "Integer32"
_SaPUFIndex_Object = MibTableColumn
saPUFIndex = _SaPUFIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 10, 1, 1, 1),
    _SaPUFIndex_Type()
)
saPUFIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saPUFIndex.setStatus("current")
_SaPUFRowStatus_Type = RowStatus
_SaPUFRowStatus_Object = MibTableColumn
saPUFRowStatus = _SaPUFRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 10, 1, 1, 2),
    _SaPUFRowStatus_Type()
)
saPUFRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saPUFRowStatus.setStatus("current")


class _SaPUFFrequency_Type(Integer32):
    """Custom type saPUFFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(93000000, 999000000),
    )


_SaPUFFrequency_Type.__name__ = "Integer32"
_SaPUFFrequency_Object = MibTableColumn
saPUFFrequency = _SaPUFFrequency_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 10, 1, 1, 3),
    _SaPUFFrequency_Type()
)
saPUFFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    saPUFFrequency.setStatus("current")


class _SaPUFAnnex_Type(Integer32):
    """Custom type saPUFAnnex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("annexA", 0),
          ("annexB", 1))
    )


_SaPUFAnnex_Type.__name__ = "Integer32"
_SaPUFAnnex_Object = MibTableColumn
saPUFAnnex = _SaPUFAnnex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 10, 1, 1, 4),
    _SaPUFAnnex_Type()
)
saPUFAnnex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saPUFAnnex.setStatus("current")
_SaPUFScanNow_Type = TruthValue
_SaPUFScanNow_Object = MibTableColumn
saPUFScanNow = _SaPUFScanNow_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 10, 1, 1, 5),
    _SaPUFScanNow_Type()
)
saPUFScanNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saPUFScanNow.setStatus("current")


class _SaPUFScanOnNextBoot_Type(Integer32):
    """Custom type saPUFScanOnNextBoot based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 0))
    )


_SaPUFScanOnNextBoot_Type.__name__ = "Integer32"
_SaPUFScanOnNextBoot_Object = MibTableColumn
saPUFScanOnNextBoot = _SaPUFScanOnNextBoot_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 10, 1, 1, 6),
    _SaPUFScanOnNextBoot_Type()
)
saPUFScanOnNextBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saPUFScanOnNextBoot.setStatus("current")


class _SaPUFScanResults_Type(Integer32):
    """Custom type saPUFScanResults based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("detected", 1),
          ("notDetected", 0))
    )


_SaPUFScanResults_Type.__name__ = "Integer32"
_SaPUFScanResults_Object = MibTableColumn
saPUFScanResults = _SaPUFScanResults_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 10, 1, 1, 7),
    _SaPUFScanResults_Type()
)
saPUFScanResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saPUFScanResults.setStatus("current")


class _SaPUFScanTimestamp_Type(SnmpAdminString):
    """Custom type saPUFScanTimestamp based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_SaPUFScanTimestamp_Type.__name__ = "SnmpAdminString"
_SaPUFScanTimestamp_Object = MibTableColumn
saPUFScanTimestamp = _SaPUFScanTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 10, 1, 1, 8),
    _SaPUFScanTimestamp_Type()
)
saPUFScanTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saPUFScanTimestamp.setStatus("current")


class _SaPUFScanResultsType_Type(Integer32):
    """Custom type saPUFScanResultsType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("docsisQam", 2),
          ("notDetected", 0),
          ("qam", 1),
          ("unknown", 3))
    )


_SaPUFScanResultsType_Type.__name__ = "Integer32"
_SaPUFScanResultsType_Object = MibTableColumn
saPUFScanResultsType = _SaPUFScanResultsType_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 10, 1, 1, 9),
    _SaPUFScanResultsType_Type()
)
saPUFScanResultsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saPUFScanResultsType.setStatus("current")
_SaPUFTrapServer_Type = IpAddress
_SaPUFTrapServer_Object = MibScalar
saPUFTrapServer = _SaPUFTrapServer_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 10, 2),
    _SaPUFTrapServer_Type()
)
saPUFTrapServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saPUFTrapServer.setStatus("current")


class _SaPUFTrapControl_Type(Integer32):
    """Custom type saPUFTrapControl based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enableOnDocsisQamDetection", 5),
          ("enableOnEnergyDetection", 1),
          ("enableOnFrequencyScan", 3),
          ("enableOnNoEnergyDetected", 2),
          ("enableOnQamDetection", 4))
    )


_SaPUFTrapControl_Type.__name__ = "Integer32"
_SaPUFTrapControl_Object = MibScalar
saPUFTrapControl = _SaPUFTrapControl_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 10, 3),
    _SaPUFTrapControl_Type()
)
saPUFTrapControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saPUFTrapControl.setStatus("current")
_SaPUFScanAllNow_Type = TruthValue
_SaPUFScanAllNow_Object = MibScalar
saPUFScanAllNow = _SaPUFScanAllNow_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 10, 4),
    _SaPUFScanAllNow_Type()
)
saPUFScanAllNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saPUFScanAllNow.setStatus("current")


class _SaPUFEntriesClearOnRFD_Type(TruthValue):
    """Custom type saPUFEntriesClearOnRFD based on TruthValue"""


_SaPUFEntriesClearOnRFD_Object = MibScalar
saPUFEntriesClearOnRFD = _SaPUFEntriesClearOnRFD_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 10, 5),
    _SaPUFEntriesClearOnRFD_Type()
)
saPUFEntriesClearOnRFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saPUFEntriesClearOnRFD.setStatus("current")
_SaLKF_ObjectIdentity = ObjectIdentity
saLKF = _SaLKF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 11)
)
_SaLKFTable_Object = MibTable
saLKFTable = _SaLKFTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 11, 1)
)
if mibBuilder.loadTexts:
    saLKFTable.setStatus("current")
_SaLKFEntry_Object = MibTableRow
saLKFEntry = _SaLKFEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 11, 1, 1)
)
saLKFEntry.setIndexNames(
    (0, "SA-CM-MIB", "saLKFIndex"),
)
if mibBuilder.loadTexts:
    saLKFEntry.setStatus("current")


class _SaLKFIndex_Type(Integer32):
    """Custom type saLKFIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SaLKFIndex_Type.__name__ = "Integer32"
_SaLKFIndex_Object = MibTableColumn
saLKFIndex = _SaLKFIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 11, 1, 1, 1),
    _SaLKFIndex_Type()
)
saLKFIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saLKFIndex.setStatus("current")
_SaLKFFrequency_Type = Integer32
_SaLKFFrequency_Object = MibTableColumn
saLKFFrequency = _SaLKFFrequency_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 11, 1, 1, 2),
    _SaLKFFrequency_Type()
)
saLKFFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    saLKFFrequency.setStatus("current")
_SaSoftwareIdentity_ObjectIdentity = ObjectIdentity
saSoftwareIdentity = _SaSoftwareIdentity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 14)
)
_SaSoftwareTable_Object = MibTable
saSoftwareTable = _SaSoftwareTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 14, 1)
)
if mibBuilder.loadTexts:
    saSoftwareTable.setStatus("current")
_SaSoftwareTableEntry_Object = MibTableRow
saSoftwareTableEntry = _SaSoftwareTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 14, 1, 1)
)
saSoftwareTableEntry.setIndexNames(
    (0, "SA-CM-MIB", "saSoftwareIndex"),
)
if mibBuilder.loadTexts:
    saSoftwareTableEntry.setStatus("current")


class _SaSoftwareIndex_Type(Integer32):
    """Custom type saSoftwareIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SaSoftwareIndex_Type.__name__ = "Integer32"
_SaSoftwareIndex_Object = MibTableColumn
saSoftwareIndex = _SaSoftwareIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 14, 1, 1, 1),
    _SaSoftwareIndex_Type()
)
saSoftwareIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saSoftwareIndex.setStatus("current")
_SaSoftwareBaseVersion_Type = DisplayString
_SaSoftwareBaseVersion_Object = MibTableColumn
saSoftwareBaseVersion = _SaSoftwareBaseVersion_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 14, 1, 1, 2),
    _SaSoftwareBaseVersion_Type()
)
saSoftwareBaseVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saSoftwareBaseVersion.setStatus("current")
_SaSoftwareFeatureName_Type = DisplayString
_SaSoftwareFeatureName_Object = MibTableColumn
saSoftwareFeatureName = _SaSoftwareFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 1429, 77, 1, 14, 1, 1, 3),
    _SaSoftwareFeatureName_Type()
)
saSoftwareFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saSoftwareFeatureName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SA-CM-MIB",
    **{"sa": sa,
       "saCmMib": saCmMib,
       "dpxCmMibObjects": dpxCmMibObjects,
       "cmVendorInfo": cmVendorInfo,
       "vendorDefaultDSfreq": vendorDefaultDSfreq,
       "vendorDSLEDTreatment": vendorDSLEDTreatment,
       "vendorLINKLEDTreatment": vendorLINKLEDTreatment,
       "vendorUSLEDTreatment": vendorUSLEDTreatment,
       "vendorONLINELEDTreatment": vendorONLINELEDTreatment,
       "cmAPInfo": cmAPInfo,
       "cmAPIgmp": cmAPIgmp,
       "cmAPAgingOut": cmAPAgingOut,
       "cmAPMulticastPromiscuousMode": cmAPMulticastPromiscuousMode,
       "cmAPInternalInterface": cmAPInternalInterface,
       "cmAPFactoryReset": cmAPFactoryReset,
       "saCmArpRateLimit": saCmArpRateLimit,
       "saCmInternalDhcpServer": saCmInternalDhcpServer,
       "cmInterfaceInfo": cmInterfaceInfo,
       "cmConsoleMode": cmConsoleMode,
       "cmTimerT4": cmTimerT4,
       "saCmTodRenewal": saCmTodRenewal,
       "saCmAutoResetNoActivity": saCmAutoResetNoActivity,
       "saCmCpeMacAging": saCmCpeMacAging,
       "saCmBpiForward": saCmBpiForward,
       "saCmForceDualscan": saCmForceDualscan,
       "saCmDsBonding": saCmDsBonding,
       "saCmDocsisCapableVersion": saCmDocsisCapableVersion,
       "saOorDsidOverride": saOorDsidOverride,
       "saCmCpeL2VpnMacAging": saCmCpeL2VpnMacAging,
       "saCmL2VpnUsForwardingCriteria": saCmL2VpnUsForwardingCriteria,
       "cmEthernetOperTable": cmEthernetOperTable,
       "cmEthernetOperEntry": cmEthernetOperEntry,
       "cmEthernetOperIndex": cmEthernetOperIndex,
       "cmEthernetOperSetting": cmEthernetOperSetting,
       "cmEthernetOperMode": cmEthernetOperMode,
       "cmEthernetIfAdminStatus": cmEthernetIfAdminStatus,
       "cmEthernetIfAdminOverride": cmEthernetIfAdminOverride,
       "saCmUsBonding": saCmUsBonding,
       "saCmIcmpRateLimit": saCmIcmpRateLimit,
       "saCmTftpBlockSizeV4": saCmTftpBlockSizeV4,
       "saCmTftpBlockSizeV6": saCmTftpBlockSizeV6,
       "saCmUsPowerLimit": saCmUsPowerLimit,
       "saCmSoftwareDownload": saCmSoftwareDownload,
       "saCmSoftwareTable": saCmSoftwareTable,
       "saCmSoftwareEntry": saCmSoftwareEntry,
       "saCmSwIndex": saCmSwIndex,
       "saCmSwModel": saCmSwModel,
       "saCmSwHwVer": saCmSwHwVer,
       "saCmSwBootLoader": saCmSwBootLoader,
       "saCmSwProtocol": saCmSwProtocol,
       "saCmSwFilename": saCmSwFilename,
       "saCmSwServer": saCmSwServer,
       "saCmSwAdminStatus": saCmSwAdminStatus,
       "saCmSwMethod": saCmSwMethod,
       "saCmSwServerAddressType": saCmSwServerAddressType,
       "saCmSwServerAddress": saCmSwServerAddress,
       "saCmSoftwareDownloadTFTPServer": saCmSoftwareDownloadTFTPServer,
       "saCmWebAccess": saCmWebAccess,
       "saCmWebAccessUserIfTypeTable": saCmWebAccessUserIfTypeTable,
       "saCmWebAccessUserIfTypeEntry": saCmWebAccessUserIfTypeEntry,
       "saCmWebAccessUserTypeIndex": saCmWebAccessUserTypeIndex,
       "saCmWebAccessIfTypeIndex": saCmWebAccessIfTypeIndex,
       "saCmWebAccessUserIfLevel": saCmWebAccessUserIfLevel,
       "saCmWebAccessHomeUsername": saCmWebAccessHomeUsername,
       "saCmWebAccessHomeUserPassword": saCmWebAccessHomeUserPassword,
       "saCmWebAccessAdvancedType": saCmWebAccessAdvancedType,
       "saCmWebAccessAdvancedUsername": saCmWebAccessAdvancedUsername,
       "saCmWebAccessAdvancedPassword": saCmWebAccessAdvancedPassword,
       "saCmWebAccessNoActivityTimeout": saCmWebAccessNoActivityTimeout,
       "saCmWebAccessHomeUserClearPassword": saCmWebAccessHomeUserClearPassword,
       "saPUF": saPUF,
       "saPUFTable": saPUFTable,
       "saPUFEntry": saPUFEntry,
       "saPUFIndex": saPUFIndex,
       "saPUFRowStatus": saPUFRowStatus,
       "saPUFFrequency": saPUFFrequency,
       "saPUFAnnex": saPUFAnnex,
       "saPUFScanNow": saPUFScanNow,
       "saPUFScanOnNextBoot": saPUFScanOnNextBoot,
       "saPUFScanResults": saPUFScanResults,
       "saPUFScanTimestamp": saPUFScanTimestamp,
       "saPUFScanResultsType": saPUFScanResultsType,
       "saPUFTrapServer": saPUFTrapServer,
       "saPUFTrapControl": saPUFTrapControl,
       "saPUFScanAllNow": saPUFScanAllNow,
       "saPUFEntriesClearOnRFD": saPUFEntriesClearOnRFD,
       "saLKF": saLKF,
       "saLKFTable": saLKFTable,
       "saLKFEntry": saLKFEntry,
       "saLKFIndex": saLKFIndex,
       "saLKFFrequency": saLKFFrequency,
       "saSoftwareIdentity": saSoftwareIdentity,
       "saSoftwareTable": saSoftwareTable,
       "saSoftwareTableEntry": saSoftwareTableEntry,
       "saSoftwareIndex": saSoftwareIndex,
       "saSoftwareBaseVersion": saSoftwareBaseVersion,
       "saSoftwareFeatureName": saSoftwareFeatureName}
)
