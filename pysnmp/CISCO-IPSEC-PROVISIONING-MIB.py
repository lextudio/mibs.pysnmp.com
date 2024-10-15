# SNMP MIB module (CISCO-IPSEC-PROVISIONING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IPSEC-PROVISIONING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:54 2024
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

(CIPsecCryptomapType,
 CIPsecDiffHellmanGrp,
 CIPsecEncapMode,
 CIPsecLifesize,
 CIPsecLifetime,
 CIPsecNumCryptoMaps,
 CIPsecSecuritySuite,
 CIPsecTransform,
 CIPsecTunnelIdleTime) = mibBuilder.importSymbols(
    "CISCO-IPSEC-TC",
    "CIPsecCryptomapType",
    "CIPsecDiffHellmanGrp",
    "CIPsecEncapMode",
    "CIPsecLifesize",
    "CIPsecLifetime",
    "CIPsecNumCryptoMaps",
    "CIPsecSecuritySuite",
    "CIPsecTransform",
    "CIPsecTunnelIdleTime")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

ciscoIPsecProvisioningMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 431)
)
ciscoIPsecProvisioningMIB.setRevisions(
        ("2005-11-02 00:00",
         "2005-01-25 00:00",
         "2004-10-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoIPsecProvisioningMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoIPsecProvisioningMIBNotifs = _CiscoIPsecProvisioningMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 0)
)
_CiscoIPsecProvisioningMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIPsecProvisioningMIBObjects = _CiscoIPsecProvisioningMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1)
)
_CipsIPsecGlobals_ObjectIdentity = ObjectIdentity
cipsIPsecGlobals = _CipsIPsecGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 1)
)


class _CipsTunnelLifetime_Type(CIPsecLifetime):
    """Custom type cipsTunnelLifetime based on CIPsecLifetime"""
    defaultValue = 3600


_CipsTunnelLifetime_Object = MibScalar
cipsTunnelLifetime = _CipsTunnelLifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 1, 1),
    _CipsTunnelLifetime_Type()
)
cipsTunnelLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipsTunnelLifetime.setStatus("current")
if mibBuilder.loadTexts:
    cipsTunnelLifetime.setUnits("seconds")


class _CipsTunnelLifesize_Type(CIPsecLifesize):
    """Custom type cipsTunnelLifesize based on CIPsecLifesize"""
    defaultValue = 4608000


_CipsTunnelLifesize_Object = MibScalar
cipsTunnelLifesize = _CipsTunnelLifesize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 1, 2),
    _CipsTunnelLifesize_Type()
)
cipsTunnelLifesize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipsTunnelLifesize.setStatus("current")
if mibBuilder.loadTexts:
    cipsTunnelLifesize.setUnits("KBytes")


class _CipsTunnelIdleTimeout_Type(CIPsecTunnelIdleTime):
    """Custom type cipsTunnelIdleTimeout based on CIPsecTunnelIdleTime"""
    defaultValue = 0


_CipsTunnelIdleTimeout_Object = MibScalar
cipsTunnelIdleTimeout = _CipsTunnelIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 1, 3),
    _CipsTunnelIdleTimeout_Type()
)
cipsTunnelIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipsTunnelIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cipsTunnelIdleTimeout.setUnits("seconds")
_CipsIPsecTransforms_ObjectIdentity = ObjectIdentity
cipsIPsecTransforms = _CipsIPsecTransforms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 2)
)
_CipsIPsecXformSetTable_Object = MibTable
cipsIPsecXformSetTable = _CipsIPsecXformSetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cipsIPsecXformSetTable.setStatus("current")
_CipsIPsecXformSetEntry_Object = MibTableRow
cipsIPsecXformSetEntry = _CipsIPsecXformSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 2, 1, 1)
)
cipsIPsecXformSetEntry.setIndexNames(
    (0, "CISCO-IPSEC-PROVISIONING-MIB", "cipsXformSetName"),
)
if mibBuilder.loadTexts:
    cipsIPsecXformSetEntry.setStatus("current")


class _CipsXformSetName_Type(SnmpAdminString):
    """Custom type cipsXformSetName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_CipsXformSetName_Type.__name__ = "SnmpAdminString"
_CipsXformSetName_Object = MibTableColumn
cipsXformSetName = _CipsXformSetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 2, 1, 1, 1),
    _CipsXformSetName_Type()
)
cipsXformSetName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipsXformSetName.setStatus("current")


class _CipsXformSetId_Type(Unsigned32):
    """Custom type cipsXformSetId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CipsXformSetId_Type.__name__ = "Unsigned32"
_CipsXformSetId_Object = MibTableColumn
cipsXformSetId = _CipsXformSetId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 2, 1, 1, 2),
    _CipsXformSetId_Type()
)
cipsXformSetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsXformSetId.setStatus("current")
_CipsXformSetSuite_Type = CIPsecSecuritySuite
_CipsXformSetSuite_Object = MibTableColumn
cipsXformSetSuite = _CipsXformSetSuite_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 2, 1, 1, 3),
    _CipsXformSetSuite_Type()
)
cipsXformSetSuite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipsXformSetSuite.setStatus("current")


class _CipsXformSetEncryptionXform_Type(CIPsecTransform):
    """Custom type cipsXformSetEncryptionXform based on CIPsecTransform"""


_CipsXformSetEncryptionXform_Object = MibTableColumn
cipsXformSetEncryptionXform = _CipsXformSetEncryptionXform_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 2, 1, 1, 4),
    _CipsXformSetEncryptionXform_Type()
)
cipsXformSetEncryptionXform.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipsXformSetEncryptionXform.setStatus("current")


class _CipsXformSetIntegrityXformEsp_Type(CIPsecTransform):
    """Custom type cipsXformSetIntegrityXformEsp based on CIPsecTransform"""


_CipsXformSetIntegrityXformEsp_Object = MibTableColumn
cipsXformSetIntegrityXformEsp = _CipsXformSetIntegrityXformEsp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 2, 1, 1, 5),
    _CipsXformSetIntegrityXformEsp_Type()
)
cipsXformSetIntegrityXformEsp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipsXformSetIntegrityXformEsp.setStatus("current")


class _CipsXformSetIntegrityXformAh_Type(CIPsecTransform):
    """Custom type cipsXformSetIntegrityXformAh based on CIPsecTransform"""


_CipsXformSetIntegrityXformAh_Object = MibTableColumn
cipsXformSetIntegrityXformAh = _CipsXformSetIntegrityXformAh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 2, 1, 1, 6),
    _CipsXformSetIntegrityXformAh_Type()
)
cipsXformSetIntegrityXformAh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipsXformSetIntegrityXformAh.setStatus("current")


class _CipsXformSetCompressionXform_Type(CIPsecTransform):
    """Custom type cipsXformSetCompressionXform based on CIPsecTransform"""


_CipsXformSetCompressionXform_Object = MibTableColumn
cipsXformSetCompressionXform = _CipsXformSetCompressionXform_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 2, 1, 1, 7),
    _CipsXformSetCompressionXform_Type()
)
cipsXformSetCompressionXform.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipsXformSetCompressionXform.setStatus("current")


class _CipsXformSetMode_Type(CIPsecEncapMode):
    """Custom type cipsXformSetMode based on CIPsecEncapMode"""


_CipsXformSetMode_Object = MibTableColumn
cipsXformSetMode = _CipsXformSetMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 2, 1, 1, 8),
    _CipsXformSetMode_Type()
)
cipsXformSetMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipsXformSetMode.setStatus("current")
_CipsXformSetStatus_Type = RowStatus
_CipsXformSetStatus_Object = MibTableColumn
cipsXformSetStatus = _CipsXformSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 2, 1, 1, 9),
    _CipsXformSetStatus_Type()
)
cipsXformSetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipsXformSetStatus.setStatus("current")
_CipsCryptoMapGeneral_ObjectIdentity = ObjectIdentity
cipsCryptoMapGeneral = _CipsCryptoMapGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 3)
)
_CipsNumStaticCryptomapSets_Type = CIPsecNumCryptoMaps
_CipsNumStaticCryptomapSets_Object = MibScalar
cipsNumStaticCryptomapSets = _CipsNumStaticCryptomapSets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 3, 1),
    _CipsNumStaticCryptomapSets_Type()
)
cipsNumStaticCryptomapSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsNumStaticCryptomapSets.setStatus("current")
_CipsNumDynamicCryptomapSets_Type = CIPsecNumCryptoMaps
_CipsNumDynamicCryptomapSets_Object = MibScalar
cipsNumDynamicCryptomapSets = _CipsNumDynamicCryptomapSets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 3, 2),
    _CipsNumDynamicCryptomapSets_Type()
)
cipsNumDynamicCryptomapSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsNumDynamicCryptomapSets.setStatus("current")
_CipsNumTEDCryptomapSets_Type = CIPsecNumCryptoMaps
_CipsNumTEDCryptomapSets_Object = MibScalar
cipsNumTEDCryptomapSets = _CipsNumTEDCryptomapSets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 3, 3),
    _CipsNumTEDCryptomapSets_Type()
)
cipsNumTEDCryptomapSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsNumTEDCryptomapSets.setStatus("current")
_CipsCryptoMaps_ObjectIdentity = ObjectIdentity
cipsCryptoMaps = _CipsCryptoMaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4)
)
_CipsStaticCryptomapSetTable_Object = MibTable
cipsStaticCryptomapSetTable = _CipsStaticCryptomapSetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cipsStaticCryptomapSetTable.setStatus("current")
_CipsStaticCryptomapSetEntry_Object = MibTableRow
cipsStaticCryptomapSetEntry = _CipsStaticCryptomapSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 1, 1)
)
cipsStaticCryptomapSetEntry.setIndexNames(
    (0, "CISCO-IPSEC-PROVISIONING-MIB", "cipsStaticCryptomapSetName"),
)
if mibBuilder.loadTexts:
    cipsStaticCryptomapSetEntry.setStatus("current")
_CipsStaticCryptomapSetSize_Type = Unsigned32
_CipsStaticCryptomapSetSize_Object = MibTableColumn
cipsStaticCryptomapSetSize = _CipsStaticCryptomapSetSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 1, 1, 1),
    _CipsStaticCryptomapSetSize_Type()
)
cipsStaticCryptomapSetSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsStaticCryptomapSetSize.setStatus("current")
_CipsStaticCryptomapSetNumIsakmp_Type = Unsigned32
_CipsStaticCryptomapSetNumIsakmp_Object = MibTableColumn
cipsStaticCryptomapSetNumIsakmp = _CipsStaticCryptomapSetNumIsakmp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 1, 1, 2),
    _CipsStaticCryptomapSetNumIsakmp_Type()
)
cipsStaticCryptomapSetNumIsakmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsStaticCryptomapSetNumIsakmp.setStatus("current")
_CipsStaticCryptomapSetNumManual_Type = Unsigned32
_CipsStaticCryptomapSetNumManual_Object = MibTableColumn
cipsStaticCryptomapSetNumManual = _CipsStaticCryptomapSetNumManual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 1, 1, 3),
    _CipsStaticCryptomapSetNumManual_Type()
)
cipsStaticCryptomapSetNumManual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsStaticCryptomapSetNumManual.setStatus("current")
_CipsStaticCryptomapSetNumDynamic_Type = Unsigned32
_CipsStaticCryptomapSetNumDynamic_Object = MibTableColumn
cipsStaticCryptomapSetNumDynamic = _CipsStaticCryptomapSetNumDynamic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 1, 1, 4),
    _CipsStaticCryptomapSetNumDynamic_Type()
)
cipsStaticCryptomapSetNumDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsStaticCryptomapSetNumDynamic.setStatus("current")
_CipsStaticCryptomapSetNumTED_Type = Unsigned32
_CipsStaticCryptomapSetNumTED_Object = MibTableColumn
cipsStaticCryptomapSetNumTED = _CipsStaticCryptomapSetNumTED_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 1, 1, 5),
    _CipsStaticCryptomapSetNumTED_Type()
)
cipsStaticCryptomapSetNumTED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsStaticCryptomapSetNumTED.setStatus("current")
_CipsStaticCryptomapSetNumSAs_Type = Unsigned32
_CipsStaticCryptomapSetNumSAs_Object = MibTableColumn
cipsStaticCryptomapSetNumSAs = _CipsStaticCryptomapSetNumSAs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 1, 1, 6),
    _CipsStaticCryptomapSetNumSAs_Type()
)
cipsStaticCryptomapSetNumSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsStaticCryptomapSetNumSAs.setStatus("current")
_CipsStaticCryptomapTable_Object = MibTable
cipsStaticCryptomapTable = _CipsStaticCryptomapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 3)
)
if mibBuilder.loadTexts:
    cipsStaticCryptomapTable.setStatus("current")
_CipsStaticCryptomapEntry_Object = MibTableRow
cipsStaticCryptomapEntry = _CipsStaticCryptomapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 3, 1)
)
cipsStaticCryptomapEntry.setIndexNames(
    (0, "CISCO-IPSEC-PROVISIONING-MIB", "cipsStaticCryptomapSetName"),
    (0, "CISCO-IPSEC-PROVISIONING-MIB", "cipsStaticCryptomapPriority"),
)
if mibBuilder.loadTexts:
    cipsStaticCryptomapEntry.setStatus("current")


class _CipsStaticCryptomapSetName_Type(SnmpAdminString):
    """Custom type cipsStaticCryptomapSetName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_CipsStaticCryptomapSetName_Type.__name__ = "SnmpAdminString"
_CipsStaticCryptomapSetName_Object = MibTableColumn
cipsStaticCryptomapSetName = _CipsStaticCryptomapSetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 3, 1, 1),
    _CipsStaticCryptomapSetName_Type()
)
cipsStaticCryptomapSetName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipsStaticCryptomapSetName.setStatus("current")


class _CipsStaticCryptomapPriority_Type(Unsigned32):
    """Custom type cipsStaticCryptomapPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CipsStaticCryptomapPriority_Type.__name__ = "Unsigned32"
_CipsStaticCryptomapPriority_Object = MibTableColumn
cipsStaticCryptomapPriority = _CipsStaticCryptomapPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 3, 1, 2),
    _CipsStaticCryptomapPriority_Type()
)
cipsStaticCryptomapPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipsStaticCryptomapPriority.setStatus("current")
_CipsStaticCryptomapType_Type = CIPsecCryptomapType
_CipsStaticCryptomapType_Object = MibTableColumn
cipsStaticCryptomapType = _CipsStaticCryptomapType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 3, 1, 3),
    _CipsStaticCryptomapType_Type()
)
cipsStaticCryptomapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipsStaticCryptomapType.setStatus("current")


class _CipsStaticCryptomapDescr_Type(SnmpAdminString):
    """Custom type cipsStaticCryptomapDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_CipsStaticCryptomapDescr_Type.__name__ = "SnmpAdminString"
_CipsStaticCryptomapDescr_Object = MibTableColumn
cipsStaticCryptomapDescr = _CipsStaticCryptomapDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 3, 1, 4),
    _CipsStaticCryptomapDescr_Type()
)
cipsStaticCryptomapDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsStaticCryptomapDescr.setStatus("current")


class _CipsStaticCryptomapIpFilter_Type(OctetString):
    """Custom type cipsStaticCryptomapIpFilter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CipsStaticCryptomapIpFilter_Type.__name__ = "OctetString"
_CipsStaticCryptomapIpFilter_Object = MibTableColumn
cipsStaticCryptomapIpFilter = _CipsStaticCryptomapIpFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 3, 1, 5),
    _CipsStaticCryptomapIpFilter_Type()
)
cipsStaticCryptomapIpFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipsStaticCryptomapIpFilter.setStatus("current")


class _CipsStaticCryptomapXformSetList_Type(OctetString):
    """Custom type cipsStaticCryptomapXformSetList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CipsStaticCryptomapXformSetList_Type.__name__ = "OctetString"
_CipsStaticCryptomapXformSetList_Object = MibTableColumn
cipsStaticCryptomapXformSetList = _CipsStaticCryptomapXformSetList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 3, 1, 6),
    _CipsStaticCryptomapXformSetList_Type()
)
cipsStaticCryptomapXformSetList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipsStaticCryptomapXformSetList.setStatus("current")


class _CipsStaticCryptomapNumPeers_Type(Unsigned32):
    """Custom type cipsStaticCryptomapNumPeers based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_CipsStaticCryptomapNumPeers_Type.__name__ = "Unsigned32"
_CipsStaticCryptomapNumPeers_Object = MibTableColumn
cipsStaticCryptomapNumPeers = _CipsStaticCryptomapNumPeers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 3, 1, 7),
    _CipsStaticCryptomapNumPeers_Type()
)
cipsStaticCryptomapNumPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsStaticCryptomapNumPeers.setStatus("current")


class _CipsStaticCryotomapNextPIndex_Type(Unsigned32):
    """Custom type cipsStaticCryotomapNextPIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_CipsStaticCryotomapNextPIndex_Type.__name__ = "Unsigned32"
_CipsStaticCryotomapNextPIndex_Object = MibTableColumn
cipsStaticCryotomapNextPIndex = _CipsStaticCryotomapNextPIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 3, 1, 8),
    _CipsStaticCryotomapNextPIndex_Type()
)
cipsStaticCryotomapNextPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsStaticCryotomapNextPIndex.setStatus("current")
_CipsStaticCryptomapCurPAddrType_Type = InetAddressType
_CipsStaticCryptomapCurPAddrType_Object = MibTableColumn
cipsStaticCryptomapCurPAddrType = _CipsStaticCryptomapCurPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 3, 1, 9),
    _CipsStaticCryptomapCurPAddrType_Type()
)
cipsStaticCryptomapCurPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsStaticCryptomapCurPAddrType.setStatus("current")
_CipsStaticCryptomapCurPAddr_Type = InetAddress
_CipsStaticCryptomapCurPAddr_Object = MibTableColumn
cipsStaticCryptomapCurPAddr = _CipsStaticCryptomapCurPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 3, 1, 10),
    _CipsStaticCryptomapCurPAddr_Type()
)
cipsStaticCryptomapCurPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsStaticCryptomapCurPAddr.setStatus("current")
_CipsStaticCryptomapPfs_Type = CIPsecDiffHellmanGrp
_CipsStaticCryptomapPfs_Object = MibTableColumn
cipsStaticCryptomapPfs = _CipsStaticCryptomapPfs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 3, 1, 11),
    _CipsStaticCryptomapPfs_Type()
)
cipsStaticCryptomapPfs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipsStaticCryptomapPfs.setStatus("current")
_CipsStaticCryptomapLifetime_Type = CIPsecLifetime
_CipsStaticCryptomapLifetime_Object = MibTableColumn
cipsStaticCryptomapLifetime = _CipsStaticCryptomapLifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 3, 1, 12),
    _CipsStaticCryptomapLifetime_Type()
)
cipsStaticCryptomapLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipsStaticCryptomapLifetime.setStatus("current")
if mibBuilder.loadTexts:
    cipsStaticCryptomapLifetime.setUnits("seconds")
_CipsStaticCryptomapLifesize_Type = CIPsecLifesize
_CipsStaticCryptomapLifesize_Object = MibTableColumn
cipsStaticCryptomapLifesize = _CipsStaticCryptomapLifesize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 3, 1, 13),
    _CipsStaticCryptomapLifesize_Type()
)
cipsStaticCryptomapLifesize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipsStaticCryptomapLifesize.setStatus("current")
if mibBuilder.loadTexts:
    cipsStaticCryptomapLifesize.setUnits("KBytes")


class _CipsStaticCryptomapLevelHost_Type(TruthValue):
    """Custom type cipsStaticCryptomapLevelHost based on TruthValue"""


_CipsStaticCryptomapLevelHost_Object = MibTableColumn
cipsStaticCryptomapLevelHost = _CipsStaticCryptomapLevelHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 3, 1, 14),
    _CipsStaticCryptomapLevelHost_Type()
)
cipsStaticCryptomapLevelHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipsStaticCryptomapLevelHost.setStatus("current")
_CipsStaticCryptomapIdleTimeout_Type = CIPsecTunnelIdleTime
_CipsStaticCryptomapIdleTimeout_Object = MibTableColumn
cipsStaticCryptomapIdleTimeout = _CipsStaticCryptomapIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 3, 1, 15),
    _CipsStaticCryptomapIdleTimeout_Type()
)
cipsStaticCryptomapIdleTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipsStaticCryptomapIdleTimeout.setStatus("current")


class _CipsStaticCryptomapAutoPeer_Type(TruthValue):
    """Custom type cipsStaticCryptomapAutoPeer based on TruthValue"""


_CipsStaticCryptomapAutoPeer_Object = MibTableColumn
cipsStaticCryptomapAutoPeer = _CipsStaticCryptomapAutoPeer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 3, 1, 16),
    _CipsStaticCryptomapAutoPeer_Type()
)
cipsStaticCryptomapAutoPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipsStaticCryptomapAutoPeer.setStatus("current")
_CipsStaticCryptomapStatus_Type = RowStatus
_CipsStaticCryptomapStatus_Object = MibTableColumn
cipsStaticCryptomapStatus = _CipsStaticCryptomapStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 3, 1, 17),
    _CipsStaticCryptomapStatus_Type()
)
cipsStaticCryptomapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipsStaticCryptomapStatus.setStatus("current")
_CipsIPsecCryMapPeerTable_Object = MibTable
cipsIPsecCryMapPeerTable = _CipsIPsecCryMapPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 4)
)
if mibBuilder.loadTexts:
    cipsIPsecCryMapPeerTable.setStatus("current")
_CipsIPsecCryMapPeerEntry_Object = MibTableRow
cipsIPsecCryMapPeerEntry = _CipsIPsecCryMapPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 4, 1)
)
cipsIPsecCryMapPeerEntry.setIndexNames(
    (0, "CISCO-IPSEC-PROVISIONING-MIB", "cipsStaticCryptomapSetName"),
    (0, "CISCO-IPSEC-PROVISIONING-MIB", "cipsStaticCryptomapPriority"),
    (0, "CISCO-IPSEC-PROVISIONING-MIB", "cipsCryMapPeerIndex"),
)
if mibBuilder.loadTexts:
    cipsIPsecCryMapPeerEntry.setStatus("current")
_CipsCryMapPeerIndex_Type = Unsigned32
_CipsCryMapPeerIndex_Object = MibTableColumn
cipsCryMapPeerIndex = _CipsCryMapPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 4, 1, 1),
    _CipsCryMapPeerIndex_Type()
)
cipsCryMapPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipsCryMapPeerIndex.setStatus("current")
_CipsCryMapPeerAddrType_Type = InetAddressType
_CipsCryMapPeerAddrType_Object = MibTableColumn
cipsCryMapPeerAddrType = _CipsCryMapPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 4, 1, 2),
    _CipsCryMapPeerAddrType_Type()
)
cipsCryMapPeerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipsCryMapPeerAddrType.setStatus("current")
_CipsCryMapPeerAddr_Type = InetAddress
_CipsCryMapPeerAddr_Object = MibTableColumn
cipsCryMapPeerAddr = _CipsCryMapPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 4, 1, 3),
    _CipsCryMapPeerAddr_Type()
)
cipsCryMapPeerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipsCryMapPeerAddr.setStatus("current")


class _CipsCryMapPeerOrder_Type(Unsigned32):
    """Custom type cipsCryMapPeerOrder based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_CipsCryMapPeerOrder_Type.__name__ = "Unsigned32"
_CipsCryMapPeerOrder_Object = MibTableColumn
cipsCryMapPeerOrder = _CipsCryMapPeerOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 4, 1, 4),
    _CipsCryMapPeerOrder_Type()
)
cipsCryMapPeerOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsCryMapPeerOrder.setStatus("current")
_CipsCryMapPeerStatus_Type = RowStatus
_CipsCryMapPeerStatus_Object = MibTableColumn
cipsCryMapPeerStatus = _CipsCryMapPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 4, 1, 5),
    _CipsCryMapPeerStatus_Type()
)
cipsCryMapPeerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipsCryMapPeerStatus.setStatus("current")
_CipsCryptomapSetIfTable_Object = MibTable
cipsCryptomapSetIfTable = _CipsCryptomapSetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 5)
)
if mibBuilder.loadTexts:
    cipsCryptomapSetIfTable.setStatus("current")
_CipsCryptomapSetIfEntry_Object = MibTableRow
cipsCryptomapSetIfEntry = _CipsCryptomapSetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 5, 1)
)
cipsCryptomapSetIfEntry.setIndexNames(
    (0, "CISCO-IPSEC-PROVISIONING-MIB", "cipsStaticCryptomapSetName"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cipsCryptomapSetIfEntry.setStatus("current")
_CipsCryptomapSetIfStatus_Type = RowStatus
_CipsCryptomapSetIfStatus_Object = MibTableColumn
cipsCryptomapSetIfStatus = _CipsCryptomapSetIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 5, 1, 1),
    _CipsCryptomapSetIfStatus_Type()
)
cipsCryptomapSetIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipsCryptomapSetIfStatus.setStatus("current")
_CipsIfCryptomapSetInfoTable_Object = MibTable
cipsIfCryptomapSetInfoTable = _CipsIfCryptomapSetInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 6)
)
if mibBuilder.loadTexts:
    cipsIfCryptomapSetInfoTable.setStatus("current")
_CipsIfCryptomapSetInfoEntry_Object = MibTableRow
cipsIfCryptomapSetInfoEntry = _CipsIfCryptomapSetInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 6, 1)
)
cipsIfCryptomapSetInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cipsIfCryptomapSetInfoEntry.setStatus("current")


class _CipsIfStaticCryptomapSetName_Type(SnmpAdminString):
    """Custom type cipsIfStaticCryptomapSetName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_CipsIfStaticCryptomapSetName_Type.__name__ = "SnmpAdminString"
_CipsIfStaticCryptomapSetName_Object = MibTableColumn
cipsIfStaticCryptomapSetName = _CipsIfStaticCryptomapSetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 4, 6, 1, 1),
    _CipsIfStaticCryptomapSetName_Type()
)
cipsIfStaticCryptomapSetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsIfStaticCryptomapSetName.setStatus("current")
_CipsNotificationCntl_ObjectIdentity = ObjectIdentity
cipsNotificationCntl = _CipsNotificationCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 5)
)


class _CipsCntlAllNotifs_Type(TruthValue):
    """Custom type cipsCntlAllNotifs based on TruthValue"""


_CipsCntlAllNotifs_Object = MibScalar
cipsCntlAllNotifs = _CipsCntlAllNotifs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 5, 1),
    _CipsCntlAllNotifs_Type()
)
cipsCntlAllNotifs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipsCntlAllNotifs.setStatus("current")


class _CipsCntlCryptomapAdded_Type(TruthValue):
    """Custom type cipsCntlCryptomapAdded based on TruthValue"""


_CipsCntlCryptomapAdded_Object = MibScalar
cipsCntlCryptomapAdded = _CipsCntlCryptomapAdded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 5, 2),
    _CipsCntlCryptomapAdded_Type()
)
cipsCntlCryptomapAdded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipsCntlCryptomapAdded.setStatus("current")


class _CipsCntlCryptomapDeleted_Type(TruthValue):
    """Custom type cipsCntlCryptomapDeleted based on TruthValue"""


_CipsCntlCryptomapDeleted_Object = MibScalar
cipsCntlCryptomapDeleted = _CipsCntlCryptomapDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 5, 3),
    _CipsCntlCryptomapDeleted_Type()
)
cipsCntlCryptomapDeleted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipsCntlCryptomapDeleted.setStatus("current")


class _CipsCntlCryptomapSetAttached_Type(TruthValue):
    """Custom type cipsCntlCryptomapSetAttached based on TruthValue"""


_CipsCntlCryptomapSetAttached_Object = MibScalar
cipsCntlCryptomapSetAttached = _CipsCntlCryptomapSetAttached_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 5, 4),
    _CipsCntlCryptomapSetAttached_Type()
)
cipsCntlCryptomapSetAttached.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipsCntlCryptomapSetAttached.setStatus("current")


class _CipsCntlCryptomapSetDetached_Type(TruthValue):
    """Custom type cipsCntlCryptomapSetDetached based on TruthValue"""


_CipsCntlCryptomapSetDetached_Object = MibScalar
cipsCntlCryptomapSetDetached = _CipsCntlCryptomapSetDetached_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 1, 5, 5),
    _CipsCntlCryptomapSetDetached_Type()
)
cipsCntlCryptomapSetDetached.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipsCntlCryptomapSetDetached.setStatus("current")
_CiscoIPsecProvisioningMIBConform_ObjectIdentity = ObjectIdentity
ciscoIPsecProvisioningMIBConform = _CiscoIPsecProvisioningMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 2)
)
_CiscoIPsecProvMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoIPsecProvMIBCompliances = _CiscoIPsecProvMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 2, 1)
)
_CiscoIPsecProvMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIPsecProvMIBGroups = _CiscoIPsecProvMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 2, 2)
)

# Managed Objects groups

ciscoIPsecProvGlobalsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 2, 2, 1)
)
ciscoIPsecProvGlobalsGroup.setObjects(
      *(("CISCO-IPSEC-PROVISIONING-MIB", "cipsTunnelLifetime"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsTunnelLifesize"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsTunnelIdleTimeout"))
)
if mibBuilder.loadTexts:
    ciscoIPsecProvGlobalsGroup.setStatus("current")

ciscoIPsecProvXformsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 2, 2, 2)
)
ciscoIPsecProvXformsGroup.setObjects(
      *(("CISCO-IPSEC-PROVISIONING-MIB", "cipsXformSetId"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsXformSetMode"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsXformSetSuite"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsXformSetEncryptionXform"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsXformSetIntegrityXformEsp"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsXformSetIntegrityXformAh"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsXformSetCompressionXform"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsXformSetStatus"))
)
if mibBuilder.loadTexts:
    ciscoIPsecProvXformsGroup.setStatus("current")

ciscoIPsecProvStCryptomapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 2, 2, 3)
)
ciscoIPsecProvStCryptomapGroup.setObjects(
      *(("CISCO-IPSEC-PROVISIONING-MIB", "cipsNumStaticCryptomapSets"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsStaticCryptomapSetSize"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsStaticCryptomapSetNumIsakmp"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsStaticCryptomapSetNumManual"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsStaticCryptomapSetNumDynamic"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsStaticCryptomapSetNumTED"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsStaticCryptomapSetNumSAs"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsStaticCryptomapType"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsStaticCryptomapDescr"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsStaticCryptomapIpFilter"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsStaticCryptomapXformSetList"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsStaticCryptomapNumPeers"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsStaticCryotomapNextPIndex"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsStaticCryptomapCurPAddrType"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsStaticCryptomapCurPAddr"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsStaticCryptomapPfs"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsStaticCryptomapLifetime"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsStaticCryptomapLifesize"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsStaticCryptomapLevelHost"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsStaticCryptomapIdleTimeout"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsStaticCryptomapStatus"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsStaticCryptomapAutoPeer"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsCryMapPeerStatus"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsCryptomapSetIfStatus"))
)
if mibBuilder.loadTexts:
    ciscoIPsecProvStCryptomapGroup.setStatus("current")

ciscoIPsecProvDynCryptomapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 2, 2, 4)
)
ciscoIPsecProvDynCryptomapGroup.setObjects(
    ("CISCO-IPSEC-PROVISIONING-MIB", "cipsNumDynamicCryptomapSets")
)
if mibBuilder.loadTexts:
    ciscoIPsecProvDynCryptomapGroup.setStatus("current")

ciscoIPsecProvTedCryptomapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 2, 2, 5)
)
ciscoIPsecProvTedCryptomapGroup.setObjects(
    ("CISCO-IPSEC-PROVISIONING-MIB", "cipsNumTEDCryptomapSets")
)
if mibBuilder.loadTexts:
    ciscoIPsecProvTedCryptomapGroup.setStatus("current")

ciscoIPsecCryptomapPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 2, 2, 6)
)
ciscoIPsecCryptomapPeerGroup.setObjects(
      *(("CISCO-IPSEC-PROVISIONING-MIB", "cipsCryMapPeerAddrType"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsCryMapPeerAddr"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsCryMapPeerOrder"))
)
if mibBuilder.loadTexts:
    ciscoIPsecCryptomapPeerGroup.setStatus("current")

ciscoIPsecProvNotifCntlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 2, 2, 7)
)
ciscoIPsecProvNotifCntlGroup.setObjects(
      *(("CISCO-IPSEC-PROVISIONING-MIB", "cipsCntlAllNotifs"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsCntlCryptomapAdded"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsCntlCryptomapDeleted"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsCntlCryptomapSetAttached"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsCntlCryptomapSetDetached"))
)
if mibBuilder.loadTexts:
    ciscoIPsecProvNotifCntlGroup.setStatus("current")

ciscoIPsecProvInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 2, 2, 9)
)
ciscoIPsecProvInfoGroup.setObjects(
    ("CISCO-IPSEC-PROVISIONING-MIB", "cipsIfStaticCryptomapSetName")
)
if mibBuilder.loadTexts:
    ciscoIPsecProvInfoGroup.setStatus("current")


# Notification objects

ciscoIPsecProvCryptomapAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 0, 1)
)
ciscoIPsecProvCryptomapAdded.setObjects(
      *(("CISCO-IPSEC-PROVISIONING-MIB", "cipsStaticCryptomapType"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsStaticCryptomapSetSize"))
)
if mibBuilder.loadTexts:
    ciscoIPsecProvCryptomapAdded.setStatus(
        "current"
    )

ciscoIPsecProvCryptomapDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 0, 2)
)
ciscoIPsecProvCryptomapDeleted.setObjects(
    ("CISCO-IPSEC-PROVISIONING-MIB", "cipsStaticCryptomapSetSize")
)
if mibBuilder.loadTexts:
    ciscoIPsecProvCryptomapDeleted.setStatus(
        "current"
    )

ciscoIPsecProvCryptomapAttached = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 0, 3)
)
ciscoIPsecProvCryptomapAttached.setObjects(
      *(("CISCO-IPSEC-PROVISIONING-MIB", "cipsStaticCryptomapSetSize"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsStaticCryptomapSetNumIsakmp"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "cipsStaticCryptomapSetNumDynamic"))
)
if mibBuilder.loadTexts:
    ciscoIPsecProvCryptomapAttached.setStatus(
        "current"
    )

ciscoIPsecProvCryptomapDetached = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 0, 4)
)
ciscoIPsecProvCryptomapDetached.setObjects(
    ("CISCO-IPSEC-PROVISIONING-MIB", "cipsStaticCryptomapSetSize")
)
if mibBuilder.loadTexts:
    ciscoIPsecProvCryptomapDetached.setStatus(
        "current"
    )


# Notifications groups

ciscoIPsecProvNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 2, 2, 8)
)
ciscoIPsecProvNotifGroup.setObjects(
      *(("CISCO-IPSEC-PROVISIONING-MIB", "ciscoIPsecProvCryptomapDetached"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "ciscoIPsecProvCryptomapAttached"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "ciscoIPsecProvCryptomapDeleted"),
        ("CISCO-IPSEC-PROVISIONING-MIB", "ciscoIPsecProvCryptomapAdded"))
)
if mibBuilder.loadTexts:
    ciscoIPsecProvNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoIPsecProvMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoIPsecProvMIBCompliance.setStatus(
        "deprecated"
    )

ciscoIPsecProvMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 431, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoIPsecProvMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IPSEC-PROVISIONING-MIB",
    **{"ciscoIPsecProvisioningMIB": ciscoIPsecProvisioningMIB,
       "ciscoIPsecProvisioningMIBNotifs": ciscoIPsecProvisioningMIBNotifs,
       "ciscoIPsecProvCryptomapAdded": ciscoIPsecProvCryptomapAdded,
       "ciscoIPsecProvCryptomapDeleted": ciscoIPsecProvCryptomapDeleted,
       "ciscoIPsecProvCryptomapAttached": ciscoIPsecProvCryptomapAttached,
       "ciscoIPsecProvCryptomapDetached": ciscoIPsecProvCryptomapDetached,
       "ciscoIPsecProvisioningMIBObjects": ciscoIPsecProvisioningMIBObjects,
       "cipsIPsecGlobals": cipsIPsecGlobals,
       "cipsTunnelLifetime": cipsTunnelLifetime,
       "cipsTunnelLifesize": cipsTunnelLifesize,
       "cipsTunnelIdleTimeout": cipsTunnelIdleTimeout,
       "cipsIPsecTransforms": cipsIPsecTransforms,
       "cipsIPsecXformSetTable": cipsIPsecXformSetTable,
       "cipsIPsecXformSetEntry": cipsIPsecXformSetEntry,
       "cipsXformSetName": cipsXformSetName,
       "cipsXformSetId": cipsXformSetId,
       "cipsXformSetSuite": cipsXformSetSuite,
       "cipsXformSetEncryptionXform": cipsXformSetEncryptionXform,
       "cipsXformSetIntegrityXformEsp": cipsXformSetIntegrityXformEsp,
       "cipsXformSetIntegrityXformAh": cipsXformSetIntegrityXformAh,
       "cipsXformSetCompressionXform": cipsXformSetCompressionXform,
       "cipsXformSetMode": cipsXformSetMode,
       "cipsXformSetStatus": cipsXformSetStatus,
       "cipsCryptoMapGeneral": cipsCryptoMapGeneral,
       "cipsNumStaticCryptomapSets": cipsNumStaticCryptomapSets,
       "cipsNumDynamicCryptomapSets": cipsNumDynamicCryptomapSets,
       "cipsNumTEDCryptomapSets": cipsNumTEDCryptomapSets,
       "cipsCryptoMaps": cipsCryptoMaps,
       "cipsStaticCryptomapSetTable": cipsStaticCryptomapSetTable,
       "cipsStaticCryptomapSetEntry": cipsStaticCryptomapSetEntry,
       "cipsStaticCryptomapSetSize": cipsStaticCryptomapSetSize,
       "cipsStaticCryptomapSetNumIsakmp": cipsStaticCryptomapSetNumIsakmp,
       "cipsStaticCryptomapSetNumManual": cipsStaticCryptomapSetNumManual,
       "cipsStaticCryptomapSetNumDynamic": cipsStaticCryptomapSetNumDynamic,
       "cipsStaticCryptomapSetNumTED": cipsStaticCryptomapSetNumTED,
       "cipsStaticCryptomapSetNumSAs": cipsStaticCryptomapSetNumSAs,
       "cipsStaticCryptomapTable": cipsStaticCryptomapTable,
       "cipsStaticCryptomapEntry": cipsStaticCryptomapEntry,
       "cipsStaticCryptomapSetName": cipsStaticCryptomapSetName,
       "cipsStaticCryptomapPriority": cipsStaticCryptomapPriority,
       "cipsStaticCryptomapType": cipsStaticCryptomapType,
       "cipsStaticCryptomapDescr": cipsStaticCryptomapDescr,
       "cipsStaticCryptomapIpFilter": cipsStaticCryptomapIpFilter,
       "cipsStaticCryptomapXformSetList": cipsStaticCryptomapXformSetList,
       "cipsStaticCryptomapNumPeers": cipsStaticCryptomapNumPeers,
       "cipsStaticCryotomapNextPIndex": cipsStaticCryotomapNextPIndex,
       "cipsStaticCryptomapCurPAddrType": cipsStaticCryptomapCurPAddrType,
       "cipsStaticCryptomapCurPAddr": cipsStaticCryptomapCurPAddr,
       "cipsStaticCryptomapPfs": cipsStaticCryptomapPfs,
       "cipsStaticCryptomapLifetime": cipsStaticCryptomapLifetime,
       "cipsStaticCryptomapLifesize": cipsStaticCryptomapLifesize,
       "cipsStaticCryptomapLevelHost": cipsStaticCryptomapLevelHost,
       "cipsStaticCryptomapIdleTimeout": cipsStaticCryptomapIdleTimeout,
       "cipsStaticCryptomapAutoPeer": cipsStaticCryptomapAutoPeer,
       "cipsStaticCryptomapStatus": cipsStaticCryptomapStatus,
       "cipsIPsecCryMapPeerTable": cipsIPsecCryMapPeerTable,
       "cipsIPsecCryMapPeerEntry": cipsIPsecCryMapPeerEntry,
       "cipsCryMapPeerIndex": cipsCryMapPeerIndex,
       "cipsCryMapPeerAddrType": cipsCryMapPeerAddrType,
       "cipsCryMapPeerAddr": cipsCryMapPeerAddr,
       "cipsCryMapPeerOrder": cipsCryMapPeerOrder,
       "cipsCryMapPeerStatus": cipsCryMapPeerStatus,
       "cipsCryptomapSetIfTable": cipsCryptomapSetIfTable,
       "cipsCryptomapSetIfEntry": cipsCryptomapSetIfEntry,
       "cipsCryptomapSetIfStatus": cipsCryptomapSetIfStatus,
       "cipsIfCryptomapSetInfoTable": cipsIfCryptomapSetInfoTable,
       "cipsIfCryptomapSetInfoEntry": cipsIfCryptomapSetInfoEntry,
       "cipsIfStaticCryptomapSetName": cipsIfStaticCryptomapSetName,
       "cipsNotificationCntl": cipsNotificationCntl,
       "cipsCntlAllNotifs": cipsCntlAllNotifs,
       "cipsCntlCryptomapAdded": cipsCntlCryptomapAdded,
       "cipsCntlCryptomapDeleted": cipsCntlCryptomapDeleted,
       "cipsCntlCryptomapSetAttached": cipsCntlCryptomapSetAttached,
       "cipsCntlCryptomapSetDetached": cipsCntlCryptomapSetDetached,
       "ciscoIPsecProvisioningMIBConform": ciscoIPsecProvisioningMIBConform,
       "ciscoIPsecProvMIBCompliances": ciscoIPsecProvMIBCompliances,
       "ciscoIPsecProvMIBCompliance": ciscoIPsecProvMIBCompliance,
       "ciscoIPsecProvMIBComplianceRev1": ciscoIPsecProvMIBComplianceRev1,
       "ciscoIPsecProvMIBGroups": ciscoIPsecProvMIBGroups,
       "ciscoIPsecProvGlobalsGroup": ciscoIPsecProvGlobalsGroup,
       "ciscoIPsecProvXformsGroup": ciscoIPsecProvXformsGroup,
       "ciscoIPsecProvStCryptomapGroup": ciscoIPsecProvStCryptomapGroup,
       "ciscoIPsecProvDynCryptomapGroup": ciscoIPsecProvDynCryptomapGroup,
       "ciscoIPsecProvTedCryptomapGroup": ciscoIPsecProvTedCryptomapGroup,
       "ciscoIPsecCryptomapPeerGroup": ciscoIPsecCryptomapPeerGroup,
       "ciscoIPsecProvNotifCntlGroup": ciscoIPsecProvNotifCntlGroup,
       "ciscoIPsecProvNotifGroup": ciscoIPsecProvNotifGroup,
       "ciscoIPsecProvInfoGroup": ciscoIPsecProvInfoGroup}
)
