# SNMP MIB module (CISCO-IPSEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IPSEC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:51 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

ciscoIPsecMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 62)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CIPsecLifetime(Gauge32, TextualConvention):
    status = "current"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 86400),
    )



class CIPsecLifesize(Gauge32, TextualConvention):
    status = "current"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2560, 536870912),
    )



class CIPsecNumCryptoMaps(Gauge32, TextualConvention):
    status = "current"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class CryptomapType(Integer32, TextualConvention):
    status = "current"
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
        *(("cryptomapTypeCET", 3),
          ("cryptomapTypeDYNAMIC", 4),
          ("cryptomapTypeDYNAMICDISCOVERY", 5),
          ("cryptomapTypeISAKMP", 2),
          ("cryptomapTypeMANUAL", 1),
          ("cryptomapTypeNONE", 0))
    )



class CryptomapSetBindStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("attached", 1),
          ("detached", 2),
          ("unknown", 0))
    )



class IPSIpAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )



class IkeHashAlgo(Integer32, TextualConvention):
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
        *(("md5", 2),
          ("none", 1),
          ("sha", 3))
    )



class IkeAuthMethod(Integer32, TextualConvention):
    status = "current"
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
        *(("none", 1),
          ("preSharedKey", 2),
          ("revPublicKey", 5),
          ("rsaEncrypt", 4),
          ("rsaSig", 3))
    )



class IkeIdentityType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isakmpIdTypeADDRESS", 1),
          ("isakmpIdTypeHOSTNAME", 2),
          ("isakmpIdTypeUNKNOWN", 0))
    )



class DiffHellmanGrp(Integer32, TextualConvention):
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
        *(("dhGroup1", 2),
          ("dhGroup2", 3),
          ("none", 1))
    )



class EncryptAlgo(Integer32, TextualConvention):
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
        *(("des", 2),
          ("des3", 3),
          ("none", 1))
    )



class TrapStatus(Integer32, TextualConvention):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_CiscoIPsecMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIPsecMIBObjects = _CiscoIPsecMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1)
)
_CipsIsakmpGroup_ObjectIdentity = ObjectIdentity
cipsIsakmpGroup = _CipsIsakmpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 1)
)
_CipsIsakmpEnabled_Type = TruthValue
_CipsIsakmpEnabled_Object = MibScalar
cipsIsakmpEnabled = _CipsIsakmpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 1, 1),
    _CipsIsakmpEnabled_Type()
)
cipsIsakmpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsIsakmpEnabled.setStatus("current")
_CipsIsakmpIdentity_Type = IkeIdentityType
_CipsIsakmpIdentity_Object = MibScalar
cipsIsakmpIdentity = _CipsIsakmpIdentity_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 1, 2),
    _CipsIsakmpIdentity_Type()
)
cipsIsakmpIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsIsakmpIdentity.setStatus("current")


class _CipsIsakmpKeepaliveInterval_Type(Integer32):
    """Custom type cipsIsakmpKeepaliveInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_CipsIsakmpKeepaliveInterval_Type.__name__ = "Integer32"
_CipsIsakmpKeepaliveInterval_Object = MibScalar
cipsIsakmpKeepaliveInterval = _CipsIsakmpKeepaliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 1, 3),
    _CipsIsakmpKeepaliveInterval_Type()
)
cipsIsakmpKeepaliveInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsIsakmpKeepaliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    cipsIsakmpKeepaliveInterval.setUnits("seconds")


class _CipsNumIsakmpPolicies_Type(Integer32):
    """Custom type cipsNumIsakmpPolicies based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CipsNumIsakmpPolicies_Type.__name__ = "Integer32"
_CipsNumIsakmpPolicies_Object = MibScalar
cipsNumIsakmpPolicies = _CipsNumIsakmpPolicies_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 1, 4),
    _CipsNumIsakmpPolicies_Type()
)
cipsNumIsakmpPolicies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsNumIsakmpPolicies.setStatus("current")
_CipsIsakmpPolicyTable_Object = MibTable
cipsIsakmpPolicyTable = _CipsIsakmpPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cipsIsakmpPolicyTable.setStatus("current")
_CipsIsakmpPolicyEntry_Object = MibTableRow
cipsIsakmpPolicyEntry = _CipsIsakmpPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 1, 5, 1)
)
cipsIsakmpPolicyEntry.setIndexNames(
    (0, "CISCO-IPSEC-MIB", "cipsIsakmpPolPriority"),
)
if mibBuilder.loadTexts:
    cipsIsakmpPolicyEntry.setStatus("current")


class _CipsIsakmpPolPriority_Type(Integer32):
    """Custom type cipsIsakmpPolPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CipsIsakmpPolPriority_Type.__name__ = "Integer32"
_CipsIsakmpPolPriority_Object = MibTableColumn
cipsIsakmpPolPriority = _CipsIsakmpPolPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 1, 5, 1, 1),
    _CipsIsakmpPolPriority_Type()
)
cipsIsakmpPolPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipsIsakmpPolPriority.setStatus("current")
_CipsIsakmpPolEncr_Type = EncryptAlgo
_CipsIsakmpPolEncr_Object = MibTableColumn
cipsIsakmpPolEncr = _CipsIsakmpPolEncr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 1, 5, 1, 2),
    _CipsIsakmpPolEncr_Type()
)
cipsIsakmpPolEncr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsIsakmpPolEncr.setStatus("current")
_CipsIsakmpPolHash_Type = IkeHashAlgo
_CipsIsakmpPolHash_Object = MibTableColumn
cipsIsakmpPolHash = _CipsIsakmpPolHash_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 1, 5, 1, 3),
    _CipsIsakmpPolHash_Type()
)
cipsIsakmpPolHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsIsakmpPolHash.setStatus("current")
_CipsIsakmpPolAuth_Type = IkeAuthMethod
_CipsIsakmpPolAuth_Object = MibTableColumn
cipsIsakmpPolAuth = _CipsIsakmpPolAuth_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 1, 5, 1, 4),
    _CipsIsakmpPolAuth_Type()
)
cipsIsakmpPolAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsIsakmpPolAuth.setStatus("current")
_CipsIsakmpPolGroup_Type = DiffHellmanGrp
_CipsIsakmpPolGroup_Object = MibTableColumn
cipsIsakmpPolGroup = _CipsIsakmpPolGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 1, 5, 1, 5),
    _CipsIsakmpPolGroup_Type()
)
cipsIsakmpPolGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsIsakmpPolGroup.setStatus("current")


class _CipsIsakmpPolLifetime_Type(Integer32):
    """Custom type cipsIsakmpPolLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_CipsIsakmpPolLifetime_Type.__name__ = "Integer32"
_CipsIsakmpPolLifetime_Object = MibTableColumn
cipsIsakmpPolLifetime = _CipsIsakmpPolLifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 1, 5, 1, 6),
    _CipsIsakmpPolLifetime_Type()
)
cipsIsakmpPolLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsIsakmpPolLifetime.setStatus("current")
if mibBuilder.loadTexts:
    cipsIsakmpPolLifetime.setUnits("seconds")
_CipsIPsecGroup_ObjectIdentity = ObjectIdentity
cipsIPsecGroup = _CipsIPsecGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2)
)
_CipsIPsecGlobals_ObjectIdentity = ObjectIdentity
cipsIPsecGlobals = _CipsIPsecGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 1)
)
_CipsSALifetime_Type = CIPsecLifetime
_CipsSALifetime_Object = MibScalar
cipsSALifetime = _CipsSALifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 1, 1),
    _CipsSALifetime_Type()
)
cipsSALifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsSALifetime.setStatus("current")
if mibBuilder.loadTexts:
    cipsSALifetime.setUnits("Seconds")
_CipsSALifesize_Type = CIPsecLifesize
_CipsSALifesize_Object = MibScalar
cipsSALifesize = _CipsSALifesize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 1, 2),
    _CipsSALifesize_Type()
)
cipsSALifesize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsSALifesize.setStatus("current")
if mibBuilder.loadTexts:
    cipsSALifesize.setUnits("KBytes")
_CipsNumStaticCryptomapSets_Type = CIPsecNumCryptoMaps
_CipsNumStaticCryptomapSets_Object = MibScalar
cipsNumStaticCryptomapSets = _CipsNumStaticCryptomapSets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 1, 3),
    _CipsNumStaticCryptomapSets_Type()
)
cipsNumStaticCryptomapSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsNumStaticCryptomapSets.setStatus("current")
if mibBuilder.loadTexts:
    cipsNumStaticCryptomapSets.setUnits("Integral Units")
_CipsNumCETCryptomapSets_Type = CIPsecNumCryptoMaps
_CipsNumCETCryptomapSets_Object = MibScalar
cipsNumCETCryptomapSets = _CipsNumCETCryptomapSets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 1, 4),
    _CipsNumCETCryptomapSets_Type()
)
cipsNumCETCryptomapSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsNumCETCryptomapSets.setStatus("current")
if mibBuilder.loadTexts:
    cipsNumCETCryptomapSets.setUnits("Integral Units")
_CipsNumDynamicCryptomapSets_Type = CIPsecNumCryptoMaps
_CipsNumDynamicCryptomapSets_Object = MibScalar
cipsNumDynamicCryptomapSets = _CipsNumDynamicCryptomapSets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 1, 5),
    _CipsNumDynamicCryptomapSets_Type()
)
cipsNumDynamicCryptomapSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsNumDynamicCryptomapSets.setStatus("current")
if mibBuilder.loadTexts:
    cipsNumDynamicCryptomapSets.setUnits("Integral Units")
_CipsNumTEDCryptomapSets_Type = CIPsecNumCryptoMaps
_CipsNumTEDCryptomapSets_Object = MibScalar
cipsNumTEDCryptomapSets = _CipsNumTEDCryptomapSets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 1, 6),
    _CipsNumTEDCryptomapSets_Type()
)
cipsNumTEDCryptomapSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsNumTEDCryptomapSets.setStatus("current")
if mibBuilder.loadTexts:
    cipsNumTEDCryptomapSets.setUnits("Integral Units")
_CipsIPsecStatistics_ObjectIdentity = ObjectIdentity
cipsIPsecStatistics = _CipsIPsecStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 2)
)
_CipsNumTEDProbesReceived_Type = Counter32
_CipsNumTEDProbesReceived_Object = MibScalar
cipsNumTEDProbesReceived = _CipsNumTEDProbesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 2, 1),
    _CipsNumTEDProbesReceived_Type()
)
cipsNumTEDProbesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsNumTEDProbesReceived.setStatus("current")
if mibBuilder.loadTexts:
    cipsNumTEDProbesReceived.setUnits("Integral Units")
_CipsNumTEDProbesSent_Type = Counter32
_CipsNumTEDProbesSent_Object = MibScalar
cipsNumTEDProbesSent = _CipsNumTEDProbesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 2, 2),
    _CipsNumTEDProbesSent_Type()
)
cipsNumTEDProbesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsNumTEDProbesSent.setStatus("current")
if mibBuilder.loadTexts:
    cipsNumTEDProbesSent.setUnits("Integral Units")
_CipsNumTEDFailures_Type = Counter32
_CipsNumTEDFailures_Object = MibScalar
cipsNumTEDFailures = _CipsNumTEDFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 2, 3),
    _CipsNumTEDFailures_Type()
)
cipsNumTEDFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsNumTEDFailures.setStatus("current")
if mibBuilder.loadTexts:
    cipsNumTEDFailures.setUnits("Integral Units")
_CipsCryptomapGroup_ObjectIdentity = ObjectIdentity
cipsCryptomapGroup = _CipsCryptomapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3)
)
_CipsStaticCryptomapSetTable_Object = MibTable
cipsStaticCryptomapSetTable = _CipsStaticCryptomapSetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    cipsStaticCryptomapSetTable.setStatus("current")
_CipsStaticCryptomapSetEntry_Object = MibTableRow
cipsStaticCryptomapSetEntry = _CipsStaticCryptomapSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 1, 1)
)
cipsStaticCryptomapSetEntry.setIndexNames(
    (0, "CISCO-IPSEC-MIB", "cipsStaticCryptomapSetName"),
)
if mibBuilder.loadTexts:
    cipsStaticCryptomapSetEntry.setStatus("current")
_CipsStaticCryptomapSetName_Type = DisplayString
_CipsStaticCryptomapSetName_Object = MibTableColumn
cipsStaticCryptomapSetName = _CipsStaticCryptomapSetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 1, 1, 1),
    _CipsStaticCryptomapSetName_Type()
)
cipsStaticCryptomapSetName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipsStaticCryptomapSetName.setStatus("current")
_CipsStaticCryptomapSetSize_Type = Gauge32
_CipsStaticCryptomapSetSize_Object = MibTableColumn
cipsStaticCryptomapSetSize = _CipsStaticCryptomapSetSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 1, 1, 2),
    _CipsStaticCryptomapSetSize_Type()
)
cipsStaticCryptomapSetSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsStaticCryptomapSetSize.setStatus("current")
_CipsStaticCryptomapSetNumIsakmp_Type = Gauge32
_CipsStaticCryptomapSetNumIsakmp_Object = MibTableColumn
cipsStaticCryptomapSetNumIsakmp = _CipsStaticCryptomapSetNumIsakmp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 1, 1, 3),
    _CipsStaticCryptomapSetNumIsakmp_Type()
)
cipsStaticCryptomapSetNumIsakmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsStaticCryptomapSetNumIsakmp.setStatus("current")
_CipsStaticCryptomapSetNumManual_Type = Gauge32
_CipsStaticCryptomapSetNumManual_Object = MibTableColumn
cipsStaticCryptomapSetNumManual = _CipsStaticCryptomapSetNumManual_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 1, 1, 4),
    _CipsStaticCryptomapSetNumManual_Type()
)
cipsStaticCryptomapSetNumManual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsStaticCryptomapSetNumManual.setStatus("current")
_CipsStaticCryptomapSetNumCET_Type = Gauge32
_CipsStaticCryptomapSetNumCET_Object = MibTableColumn
cipsStaticCryptomapSetNumCET = _CipsStaticCryptomapSetNumCET_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 1, 1, 5),
    _CipsStaticCryptomapSetNumCET_Type()
)
cipsStaticCryptomapSetNumCET.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsStaticCryptomapSetNumCET.setStatus("current")
_CipsStaticCryptomapSetNumDynamic_Type = Gauge32
_CipsStaticCryptomapSetNumDynamic_Object = MibTableColumn
cipsStaticCryptomapSetNumDynamic = _CipsStaticCryptomapSetNumDynamic_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 1, 1, 6),
    _CipsStaticCryptomapSetNumDynamic_Type()
)
cipsStaticCryptomapSetNumDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsStaticCryptomapSetNumDynamic.setStatus("current")
_CipsStaticCryptomapSetNumDisc_Type = Gauge32
_CipsStaticCryptomapSetNumDisc_Object = MibTableColumn
cipsStaticCryptomapSetNumDisc = _CipsStaticCryptomapSetNumDisc_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 1, 1, 7),
    _CipsStaticCryptomapSetNumDisc_Type()
)
cipsStaticCryptomapSetNumDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsStaticCryptomapSetNumDisc.setStatus("current")
_CipsStaticCryptomapSetNumSAs_Type = Gauge32
_CipsStaticCryptomapSetNumSAs_Object = MibTableColumn
cipsStaticCryptomapSetNumSAs = _CipsStaticCryptomapSetNumSAs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 1, 1, 8),
    _CipsStaticCryptomapSetNumSAs_Type()
)
cipsStaticCryptomapSetNumSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsStaticCryptomapSetNumSAs.setStatus("current")
_CipsDynamicCryptomapSetTable_Object = MibTable
cipsDynamicCryptomapSetTable = _CipsDynamicCryptomapSetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    cipsDynamicCryptomapSetTable.setStatus("current")
_CipsDynamicCryptomapSetEntry_Object = MibTableRow
cipsDynamicCryptomapSetEntry = _CipsDynamicCryptomapSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 2, 1)
)
cipsDynamicCryptomapSetEntry.setIndexNames(
    (0, "CISCO-IPSEC-MIB", "cipsDynamicCryptomapSetName"),
)
if mibBuilder.loadTexts:
    cipsDynamicCryptomapSetEntry.setStatus("current")
_CipsDynamicCryptomapSetName_Type = DisplayString
_CipsDynamicCryptomapSetName_Object = MibTableColumn
cipsDynamicCryptomapSetName = _CipsDynamicCryptomapSetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 2, 1, 1),
    _CipsDynamicCryptomapSetName_Type()
)
cipsDynamicCryptomapSetName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipsDynamicCryptomapSetName.setStatus("current")
_CipsDynamicCryptomapSetSize_Type = Gauge32
_CipsDynamicCryptomapSetSize_Object = MibTableColumn
cipsDynamicCryptomapSetSize = _CipsDynamicCryptomapSetSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 2, 1, 2),
    _CipsDynamicCryptomapSetSize_Type()
)
cipsDynamicCryptomapSetSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsDynamicCryptomapSetSize.setStatus("current")
_CipsDynamicCryptomapSetNumAssoc_Type = Gauge32
_CipsDynamicCryptomapSetNumAssoc_Object = MibTableColumn
cipsDynamicCryptomapSetNumAssoc = _CipsDynamicCryptomapSetNumAssoc_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 2, 1, 3),
    _CipsDynamicCryptomapSetNumAssoc_Type()
)
cipsDynamicCryptomapSetNumAssoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsDynamicCryptomapSetNumAssoc.setStatus("current")
_CipsStaticCryptomapTable_Object = MibTable
cipsStaticCryptomapTable = _CipsStaticCryptomapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 3)
)
if mibBuilder.loadTexts:
    cipsStaticCryptomapTable.setStatus("current")
_CipsStaticCryptomapEntry_Object = MibTableRow
cipsStaticCryptomapEntry = _CipsStaticCryptomapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 3, 1)
)
cipsStaticCryptomapEntry.setIndexNames(
    (0, "CISCO-IPSEC-MIB", "cipsStaticCryptomapSetName"),
    (0, "CISCO-IPSEC-MIB", "cipsStaticCryptomapPriority"),
)
if mibBuilder.loadTexts:
    cipsStaticCryptomapEntry.setStatus("current")


class _CipsStaticCryptomapPriority_Type(Integer32):
    """Custom type cipsStaticCryptomapPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CipsStaticCryptomapPriority_Type.__name__ = "Integer32"
_CipsStaticCryptomapPriority_Object = MibTableColumn
cipsStaticCryptomapPriority = _CipsStaticCryptomapPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 3, 1, 1),
    _CipsStaticCryptomapPriority_Type()
)
cipsStaticCryptomapPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipsStaticCryptomapPriority.setStatus("current")
_CipsStaticCryptomapType_Type = CryptomapType
_CipsStaticCryptomapType_Object = MibTableColumn
cipsStaticCryptomapType = _CipsStaticCryptomapType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 3, 1, 2),
    _CipsStaticCryptomapType_Type()
)
cipsStaticCryptomapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsStaticCryptomapType.setStatus("current")
_CipsStaticCryptomapDescr_Type = DisplayString
_CipsStaticCryptomapDescr_Object = MibTableColumn
cipsStaticCryptomapDescr = _CipsStaticCryptomapDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 3, 1, 3),
    _CipsStaticCryptomapDescr_Type()
)
cipsStaticCryptomapDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsStaticCryptomapDescr.setStatus("current")
_CipsStaticCryptomapPeer_Type = IPSIpAddress
_CipsStaticCryptomapPeer_Object = MibTableColumn
cipsStaticCryptomapPeer = _CipsStaticCryptomapPeer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 3, 1, 4),
    _CipsStaticCryptomapPeer_Type()
)
cipsStaticCryptomapPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsStaticCryptomapPeer.setStatus("current")


class _CipsStaticCryptomapNumPeers_Type(Integer32):
    """Custom type cipsStaticCryptomapNumPeers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_CipsStaticCryptomapNumPeers_Type.__name__ = "Integer32"
_CipsStaticCryptomapNumPeers_Object = MibTableColumn
cipsStaticCryptomapNumPeers = _CipsStaticCryptomapNumPeers_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 3, 1, 5),
    _CipsStaticCryptomapNumPeers_Type()
)
cipsStaticCryptomapNumPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsStaticCryptomapNumPeers.setStatus("current")
_CipsStaticCryptomapPfs_Type = DiffHellmanGrp
_CipsStaticCryptomapPfs_Object = MibTableColumn
cipsStaticCryptomapPfs = _CipsStaticCryptomapPfs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 3, 1, 6),
    _CipsStaticCryptomapPfs_Type()
)
cipsStaticCryptomapPfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsStaticCryptomapPfs.setStatus("current")


class _CipsStaticCryptomapLifetime_Type(Integer32):
    """Custom type cipsStaticCryptomapLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(120, 86400),
    )


_CipsStaticCryptomapLifetime_Type.__name__ = "Integer32"
_CipsStaticCryptomapLifetime_Object = MibTableColumn
cipsStaticCryptomapLifetime = _CipsStaticCryptomapLifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 3, 1, 7),
    _CipsStaticCryptomapLifetime_Type()
)
cipsStaticCryptomapLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsStaticCryptomapLifetime.setStatus("current")


class _CipsStaticCryptomapLifesize_Type(Integer32):
    """Custom type cipsStaticCryptomapLifesize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2560, 536870912),
    )


_CipsStaticCryptomapLifesize_Type.__name__ = "Integer32"
_CipsStaticCryptomapLifesize_Object = MibTableColumn
cipsStaticCryptomapLifesize = _CipsStaticCryptomapLifesize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 3, 1, 8),
    _CipsStaticCryptomapLifesize_Type()
)
cipsStaticCryptomapLifesize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsStaticCryptomapLifesize.setStatus("current")
_CipsStaticCryptomapLevelHost_Type = TruthValue
_CipsStaticCryptomapLevelHost_Object = MibTableColumn
cipsStaticCryptomapLevelHost = _CipsStaticCryptomapLevelHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 3, 1, 9),
    _CipsStaticCryptomapLevelHost_Type()
)
cipsStaticCryptomapLevelHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsStaticCryptomapLevelHost.setStatus("current")
_CipsCryptomapSetIfTable_Object = MibTable
cipsCryptomapSetIfTable = _CipsCryptomapSetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 4)
)
if mibBuilder.loadTexts:
    cipsCryptomapSetIfTable.setStatus("current")
_CipsCryptomapSetIfEntry_Object = MibTableRow
cipsCryptomapSetIfEntry = _CipsCryptomapSetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 4, 1)
)
cipsCryptomapSetIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-IPSEC-MIB", "cipsStaticCryptomapSetName"),
)
if mibBuilder.loadTexts:
    cipsCryptomapSetIfEntry.setStatus("current")
_CipsCryptomapSetIfVirtual_Type = TruthValue
_CipsCryptomapSetIfVirtual_Object = MibTableColumn
cipsCryptomapSetIfVirtual = _CipsCryptomapSetIfVirtual_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 4, 1, 1),
    _CipsCryptomapSetIfVirtual_Type()
)
cipsCryptomapSetIfVirtual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsCryptomapSetIfVirtual.setStatus("current")
_CipsCryptomapSetIfStatus_Type = CryptomapSetBindStatus
_CipsCryptomapSetIfStatus_Object = MibTableColumn
cipsCryptomapSetIfStatus = _CipsCryptomapSetIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 2, 3, 4, 1, 2),
    _CipsCryptomapSetIfStatus_Type()
)
cipsCryptomapSetIfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipsCryptomapSetIfStatus.setStatus("current")
_CipsSysCapacityGroup_ObjectIdentity = ObjectIdentity
cipsSysCapacityGroup = _CipsSysCapacityGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 3)
)


class _CipsMaxSAs_Type(Integer32):
    """Custom type cipsMaxSAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CipsMaxSAs_Type.__name__ = "Integer32"
_CipsMaxSAs_Object = MibScalar
cipsMaxSAs = _CipsMaxSAs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 3, 1),
    _CipsMaxSAs_Type()
)
cipsMaxSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipsMaxSAs.setStatus("current")
if mibBuilder.loadTexts:
    cipsMaxSAs.setUnits("Integral Units")
_Cips3DesCapable_Type = TruthValue
_Cips3DesCapable_Object = MibScalar
cips3DesCapable = _Cips3DesCapable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 3, 2),
    _Cips3DesCapable_Type()
)
cips3DesCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cips3DesCapable.setStatus("current")
_CipsTrapCntlGroup_ObjectIdentity = ObjectIdentity
cipsTrapCntlGroup = _CipsTrapCntlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 4)
)


class _CipsCntlIsakmpPolicyAdded_Type(TrapStatus):
    """Custom type cipsCntlIsakmpPolicyAdded based on TrapStatus"""


_CipsCntlIsakmpPolicyAdded_Object = MibScalar
cipsCntlIsakmpPolicyAdded = _CipsCntlIsakmpPolicyAdded_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 4, 1),
    _CipsCntlIsakmpPolicyAdded_Type()
)
cipsCntlIsakmpPolicyAdded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipsCntlIsakmpPolicyAdded.setStatus("current")


class _CipsCntlIsakmpPolicyDeleted_Type(TrapStatus):
    """Custom type cipsCntlIsakmpPolicyDeleted based on TrapStatus"""


_CipsCntlIsakmpPolicyDeleted_Object = MibScalar
cipsCntlIsakmpPolicyDeleted = _CipsCntlIsakmpPolicyDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 4, 2),
    _CipsCntlIsakmpPolicyDeleted_Type()
)
cipsCntlIsakmpPolicyDeleted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipsCntlIsakmpPolicyDeleted.setStatus("current")


class _CipsCntlCryptomapAdded_Type(TrapStatus):
    """Custom type cipsCntlCryptomapAdded based on TrapStatus"""


_CipsCntlCryptomapAdded_Object = MibScalar
cipsCntlCryptomapAdded = _CipsCntlCryptomapAdded_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 4, 3),
    _CipsCntlCryptomapAdded_Type()
)
cipsCntlCryptomapAdded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipsCntlCryptomapAdded.setStatus("current")


class _CipsCntlCryptomapDeleted_Type(TrapStatus):
    """Custom type cipsCntlCryptomapDeleted based on TrapStatus"""


_CipsCntlCryptomapDeleted_Object = MibScalar
cipsCntlCryptomapDeleted = _CipsCntlCryptomapDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 4, 4),
    _CipsCntlCryptomapDeleted_Type()
)
cipsCntlCryptomapDeleted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipsCntlCryptomapDeleted.setStatus("current")


class _CipsCntlCryptomapSetAttached_Type(TrapStatus):
    """Custom type cipsCntlCryptomapSetAttached based on TrapStatus"""


_CipsCntlCryptomapSetAttached_Object = MibScalar
cipsCntlCryptomapSetAttached = _CipsCntlCryptomapSetAttached_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 4, 5),
    _CipsCntlCryptomapSetAttached_Type()
)
cipsCntlCryptomapSetAttached.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipsCntlCryptomapSetAttached.setStatus("current")


class _CipsCntlCryptomapSetDetached_Type(TrapStatus):
    """Custom type cipsCntlCryptomapSetDetached based on TrapStatus"""


_CipsCntlCryptomapSetDetached_Object = MibScalar
cipsCntlCryptomapSetDetached = _CipsCntlCryptomapSetDetached_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 4, 6),
    _CipsCntlCryptomapSetDetached_Type()
)
cipsCntlCryptomapSetDetached.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipsCntlCryptomapSetDetached.setStatus("current")


class _CipsCntlTooManySAs_Type(TrapStatus):
    """Custom type cipsCntlTooManySAs based on TrapStatus"""


_CipsCntlTooManySAs_Object = MibScalar
cipsCntlTooManySAs = _CipsCntlTooManySAs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 1, 4, 7),
    _CipsCntlTooManySAs_Type()
)
cipsCntlTooManySAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipsCntlTooManySAs.setStatus("current")
_CiscoIPsecMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoIPsecMIBNotificationPrefix = _CiscoIPsecMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 2)
)
_CipsMIBNotifications_ObjectIdentity = ObjectIdentity
cipsMIBNotifications = _CipsMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 2, 0)
)
_CiscoIPsecMIBConformance_ObjectIdentity = ObjectIdentity
ciscoIPsecMIBConformance = _CiscoIPsecMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 3)
)
_CipsMIBConformances_ObjectIdentity = ObjectIdentity
cipsMIBConformances = _CipsMIBConformances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 3, 1)
)
_CipsMIBGroups_ObjectIdentity = ObjectIdentity
cipsMIBGroups = _CipsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 3, 2)
)

# Managed Objects groups

cipsMIBConfIsakmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 3, 2, 1)
)
cipsMIBConfIsakmpGroup.setObjects(
      *(("CISCO-IPSEC-MIB", "cipsIsakmpEnabled"),
        ("CISCO-IPSEC-MIB", "cipsIsakmpIdentity"),
        ("CISCO-IPSEC-MIB", "cipsIsakmpKeepaliveInterval"),
        ("CISCO-IPSEC-MIB", "cipsNumIsakmpPolicies"))
)
if mibBuilder.loadTexts:
    cipsMIBConfIsakmpGroup.setStatus("current")

cipsMIBConfIPSecGlobalsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 3, 2, 2)
)
cipsMIBConfIPSecGlobalsGroup.setObjects(
      *(("CISCO-IPSEC-MIB", "cipsSALifetime"),
        ("CISCO-IPSEC-MIB", "cipsSALifesize"))
)
if mibBuilder.loadTexts:
    cipsMIBConfIPSecGlobalsGroup.setStatus("current")

cipsMIBConfCapacityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 3, 2, 3)
)
cipsMIBConfCapacityGroup.setObjects(
      *(("CISCO-IPSEC-MIB", "cipsMaxSAs"),
        ("CISCO-IPSEC-MIB", "cips3DesCapable"))
)
if mibBuilder.loadTexts:
    cipsMIBConfCapacityGroup.setStatus("current")

cipsMIBStaticCryptomapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 3, 2, 4)
)
cipsMIBStaticCryptomapGroup.setObjects(
      *(("CISCO-IPSEC-MIB", "cipsStaticCryptomapSetSize"),
        ("CISCO-IPSEC-MIB", "cipsStaticCryptomapSetNumIsakmp"),
        ("CISCO-IPSEC-MIB", "cipsStaticCryptomapSetNumCET"),
        ("CISCO-IPSEC-MIB", "cipsStaticCryptomapSetNumSAs"))
)
if mibBuilder.loadTexts:
    cipsMIBStaticCryptomapGroup.setStatus("current")

cipsMIBManualCryptomapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 3, 2, 5)
)
cipsMIBManualCryptomapGroup.setObjects(
    ("CISCO-IPSEC-MIB", "cipsStaticCryptomapSetNumManual")
)
if mibBuilder.loadTexts:
    cipsMIBManualCryptomapGroup.setStatus("current")

cipsMIBDynamicCryptomapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 3, 2, 6)
)
cipsMIBDynamicCryptomapGroup.setObjects(
      *(("CISCO-IPSEC-MIB", "cipsNumTEDProbesReceived"),
        ("CISCO-IPSEC-MIB", "cipsNumTEDProbesSent"),
        ("CISCO-IPSEC-MIB", "cipsNumTEDFailures"),
        ("CISCO-IPSEC-MIB", "cipsStaticCryptomapSetNumDynamic"),
        ("CISCO-IPSEC-MIB", "cipsStaticCryptomapSetNumDisc"),
        ("CISCO-IPSEC-MIB", "cipsNumTEDCryptomapSets"),
        ("CISCO-IPSEC-MIB", "cipsDynamicCryptomapSetSize"),
        ("CISCO-IPSEC-MIB", "cipsDynamicCryptomapSetNumAssoc"))
)
if mibBuilder.loadTexts:
    cipsMIBDynamicCryptomapGroup.setStatus("current")

cipsMIBMandatoryNotifCntlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 3, 2, 7)
)
cipsMIBMandatoryNotifCntlGroup.setObjects(
      *(("CISCO-IPSEC-MIB", "cipsCntlIsakmpPolicyAdded"),
        ("CISCO-IPSEC-MIB", "cipsCntlIsakmpPolicyDeleted"),
        ("CISCO-IPSEC-MIB", "cipsCntlCryptomapAdded"),
        ("CISCO-IPSEC-MIB", "cipsCntlCryptomapDeleted"),
        ("CISCO-IPSEC-MIB", "cipsCntlCryptomapSetAttached"),
        ("CISCO-IPSEC-MIB", "cipsCntlCryptomapSetDetached"),
        ("CISCO-IPSEC-MIB", "cipsCntlTooManySAs"))
)
if mibBuilder.loadTexts:
    cipsMIBMandatoryNotifCntlGroup.setStatus("current")


# Notification objects

cipsIsakmpPolicyAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 2, 0, 1)
)
cipsIsakmpPolicyAdded.setObjects(
    ("CISCO-IPSEC-MIB", "cipsNumIsakmpPolicies")
)
if mibBuilder.loadTexts:
    cipsIsakmpPolicyAdded.setStatus(
        "current"
    )

cipsIsakmpPolicyDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 2, 0, 2)
)
cipsIsakmpPolicyDeleted.setObjects(
    ("CISCO-IPSEC-MIB", "cipsNumIsakmpPolicies")
)
if mibBuilder.loadTexts:
    cipsIsakmpPolicyDeleted.setStatus(
        "current"
    )

cipsCryptomapAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 2, 0, 3)
)
cipsCryptomapAdded.setObjects(
      *(("CISCO-IPSEC-MIB", "cipsStaticCryptomapType"),
        ("CISCO-IPSEC-MIB", "cipsStaticCryptomapSetSize"))
)
if mibBuilder.loadTexts:
    cipsCryptomapAdded.setStatus(
        "current"
    )

cipsCryptomapDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 2, 0, 4)
)
cipsCryptomapDeleted.setObjects(
    ("CISCO-IPSEC-MIB", "cipsStaticCryptomapSetSize")
)
if mibBuilder.loadTexts:
    cipsCryptomapDeleted.setStatus(
        "current"
    )

cipsCryptomapSetAttached = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 2, 0, 5)
)
cipsCryptomapSetAttached.setObjects(
      *(("CISCO-IPSEC-MIB", "cipsStaticCryptomapSetSize"),
        ("CISCO-IPSEC-MIB", "cipsStaticCryptomapSetNumIsakmp"),
        ("CISCO-IPSEC-MIB", "cipsStaticCryptomapSetNumDynamic"))
)
if mibBuilder.loadTexts:
    cipsCryptomapSetAttached.setStatus(
        "current"
    )

cipsCryptomapSetDetached = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 2, 0, 6)
)
cipsCryptomapSetDetached.setObjects(
    ("CISCO-IPSEC-MIB", "cipsStaticCryptomapSetSize")
)
if mibBuilder.loadTexts:
    cipsCryptomapSetDetached.setStatus(
        "current"
    )

cipsTooManySAs = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 2, 0, 7)
)
cipsTooManySAs.setObjects(
    ("CISCO-IPSEC-MIB", "cipsMaxSAs")
)
if mibBuilder.loadTexts:
    cipsTooManySAs.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

cipsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 62, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cipsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IPSEC-MIB",
    **{"CIPsecLifetime": CIPsecLifetime,
       "CIPsecLifesize": CIPsecLifesize,
       "CIPsecNumCryptoMaps": CIPsecNumCryptoMaps,
       "CryptomapType": CryptomapType,
       "CryptomapSetBindStatus": CryptomapSetBindStatus,
       "IPSIpAddress": IPSIpAddress,
       "IkeHashAlgo": IkeHashAlgo,
       "IkeAuthMethod": IkeAuthMethod,
       "IkeIdentityType": IkeIdentityType,
       "DiffHellmanGrp": DiffHellmanGrp,
       "EncryptAlgo": EncryptAlgo,
       "TrapStatus": TrapStatus,
       "ciscoIPsecMIB": ciscoIPsecMIB,
       "ciscoIPsecMIBObjects": ciscoIPsecMIBObjects,
       "cipsIsakmpGroup": cipsIsakmpGroup,
       "cipsIsakmpEnabled": cipsIsakmpEnabled,
       "cipsIsakmpIdentity": cipsIsakmpIdentity,
       "cipsIsakmpKeepaliveInterval": cipsIsakmpKeepaliveInterval,
       "cipsNumIsakmpPolicies": cipsNumIsakmpPolicies,
       "cipsIsakmpPolicyTable": cipsIsakmpPolicyTable,
       "cipsIsakmpPolicyEntry": cipsIsakmpPolicyEntry,
       "cipsIsakmpPolPriority": cipsIsakmpPolPriority,
       "cipsIsakmpPolEncr": cipsIsakmpPolEncr,
       "cipsIsakmpPolHash": cipsIsakmpPolHash,
       "cipsIsakmpPolAuth": cipsIsakmpPolAuth,
       "cipsIsakmpPolGroup": cipsIsakmpPolGroup,
       "cipsIsakmpPolLifetime": cipsIsakmpPolLifetime,
       "cipsIPsecGroup": cipsIPsecGroup,
       "cipsIPsecGlobals": cipsIPsecGlobals,
       "cipsSALifetime": cipsSALifetime,
       "cipsSALifesize": cipsSALifesize,
       "cipsNumStaticCryptomapSets": cipsNumStaticCryptomapSets,
       "cipsNumCETCryptomapSets": cipsNumCETCryptomapSets,
       "cipsNumDynamicCryptomapSets": cipsNumDynamicCryptomapSets,
       "cipsNumTEDCryptomapSets": cipsNumTEDCryptomapSets,
       "cipsIPsecStatistics": cipsIPsecStatistics,
       "cipsNumTEDProbesReceived": cipsNumTEDProbesReceived,
       "cipsNumTEDProbesSent": cipsNumTEDProbesSent,
       "cipsNumTEDFailures": cipsNumTEDFailures,
       "cipsCryptomapGroup": cipsCryptomapGroup,
       "cipsStaticCryptomapSetTable": cipsStaticCryptomapSetTable,
       "cipsStaticCryptomapSetEntry": cipsStaticCryptomapSetEntry,
       "cipsStaticCryptomapSetName": cipsStaticCryptomapSetName,
       "cipsStaticCryptomapSetSize": cipsStaticCryptomapSetSize,
       "cipsStaticCryptomapSetNumIsakmp": cipsStaticCryptomapSetNumIsakmp,
       "cipsStaticCryptomapSetNumManual": cipsStaticCryptomapSetNumManual,
       "cipsStaticCryptomapSetNumCET": cipsStaticCryptomapSetNumCET,
       "cipsStaticCryptomapSetNumDynamic": cipsStaticCryptomapSetNumDynamic,
       "cipsStaticCryptomapSetNumDisc": cipsStaticCryptomapSetNumDisc,
       "cipsStaticCryptomapSetNumSAs": cipsStaticCryptomapSetNumSAs,
       "cipsDynamicCryptomapSetTable": cipsDynamicCryptomapSetTable,
       "cipsDynamicCryptomapSetEntry": cipsDynamicCryptomapSetEntry,
       "cipsDynamicCryptomapSetName": cipsDynamicCryptomapSetName,
       "cipsDynamicCryptomapSetSize": cipsDynamicCryptomapSetSize,
       "cipsDynamicCryptomapSetNumAssoc": cipsDynamicCryptomapSetNumAssoc,
       "cipsStaticCryptomapTable": cipsStaticCryptomapTable,
       "cipsStaticCryptomapEntry": cipsStaticCryptomapEntry,
       "cipsStaticCryptomapPriority": cipsStaticCryptomapPriority,
       "cipsStaticCryptomapType": cipsStaticCryptomapType,
       "cipsStaticCryptomapDescr": cipsStaticCryptomapDescr,
       "cipsStaticCryptomapPeer": cipsStaticCryptomapPeer,
       "cipsStaticCryptomapNumPeers": cipsStaticCryptomapNumPeers,
       "cipsStaticCryptomapPfs": cipsStaticCryptomapPfs,
       "cipsStaticCryptomapLifetime": cipsStaticCryptomapLifetime,
       "cipsStaticCryptomapLifesize": cipsStaticCryptomapLifesize,
       "cipsStaticCryptomapLevelHost": cipsStaticCryptomapLevelHost,
       "cipsCryptomapSetIfTable": cipsCryptomapSetIfTable,
       "cipsCryptomapSetIfEntry": cipsCryptomapSetIfEntry,
       "cipsCryptomapSetIfVirtual": cipsCryptomapSetIfVirtual,
       "cipsCryptomapSetIfStatus": cipsCryptomapSetIfStatus,
       "cipsSysCapacityGroup": cipsSysCapacityGroup,
       "cipsMaxSAs": cipsMaxSAs,
       "cips3DesCapable": cips3DesCapable,
       "cipsTrapCntlGroup": cipsTrapCntlGroup,
       "cipsCntlIsakmpPolicyAdded": cipsCntlIsakmpPolicyAdded,
       "cipsCntlIsakmpPolicyDeleted": cipsCntlIsakmpPolicyDeleted,
       "cipsCntlCryptomapAdded": cipsCntlCryptomapAdded,
       "cipsCntlCryptomapDeleted": cipsCntlCryptomapDeleted,
       "cipsCntlCryptomapSetAttached": cipsCntlCryptomapSetAttached,
       "cipsCntlCryptomapSetDetached": cipsCntlCryptomapSetDetached,
       "cipsCntlTooManySAs": cipsCntlTooManySAs,
       "ciscoIPsecMIBNotificationPrefix": ciscoIPsecMIBNotificationPrefix,
       "cipsMIBNotifications": cipsMIBNotifications,
       "cipsIsakmpPolicyAdded": cipsIsakmpPolicyAdded,
       "cipsIsakmpPolicyDeleted": cipsIsakmpPolicyDeleted,
       "cipsCryptomapAdded": cipsCryptomapAdded,
       "cipsCryptomapDeleted": cipsCryptomapDeleted,
       "cipsCryptomapSetAttached": cipsCryptomapSetAttached,
       "cipsCryptomapSetDetached": cipsCryptomapSetDetached,
       "cipsTooManySAs": cipsTooManySAs,
       "ciscoIPsecMIBConformance": ciscoIPsecMIBConformance,
       "cipsMIBConformances": cipsMIBConformances,
       "cipsMIBCompliance": cipsMIBCompliance,
       "cipsMIBGroups": cipsMIBGroups,
       "cipsMIBConfIsakmpGroup": cipsMIBConfIsakmpGroup,
       "cipsMIBConfIPSecGlobalsGroup": cipsMIBConfIPSecGlobalsGroup,
       "cipsMIBConfCapacityGroup": cipsMIBConfCapacityGroup,
       "cipsMIBStaticCryptomapGroup": cipsMIBStaticCryptomapGroup,
       "cipsMIBManualCryptomapGroup": cipsMIBManualCryptomapGroup,
       "cipsMIBDynamicCryptomapGroup": cipsMIBDynamicCryptomapGroup,
       "cipsMIBMandatoryNotifCntlGroup": cipsMIBMandatoryNotifCntlGroup}
)
