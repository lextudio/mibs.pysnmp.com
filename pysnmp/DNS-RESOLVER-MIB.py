# SNMP MIB module (DNS-RESOLVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DNS-RESOLVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:14:13 2024
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

(DnsClass,
 DnsName,
 DnsNameAsIndex,
 DnsOpCode,
 DnsTime,
 DnsType,
 dns) = mibBuilder.importSymbols(
    "DNS-SERVER-MIB",
    "DnsClass",
    "DnsName",
    "DnsNameAsIndex",
    "DnsOpCode",
    "DnsTime",
    "DnsType",
    "dns")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

dnsResMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 32, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DnsQClass(Integer32, TextualConvention):
    status = "current"
    displayHint = "2d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class DnsQType(Integer32, TextualConvention):
    status = "current"
    displayHint = "2d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class DnsRespCode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )



# MIB Managed Objects in the order of their OIDs

_DnsResMIBObjects_ObjectIdentity = ObjectIdentity
dnsResMIBObjects = _DnsResMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 32, 2, 1)
)
_DnsResConfig_ObjectIdentity = ObjectIdentity
dnsResConfig = _DnsResConfig_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 1)
)
_DnsResConfigImplementIdent_Type = DisplayString
_DnsResConfigImplementIdent_Object = MibScalar
dnsResConfigImplementIdent = _DnsResConfigImplementIdent_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 1, 1),
    _DnsResConfigImplementIdent_Type()
)
dnsResConfigImplementIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResConfigImplementIdent.setStatus("current")


class _DnsResConfigService_Type(Integer32):
    """Custom type dnsResConfigService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("iterativeOnly", 2),
          ("recursiveAndIterative", 3),
          ("recursiveOnly", 1))
    )


_DnsResConfigService_Type.__name__ = "Integer32"
_DnsResConfigService_Object = MibScalar
dnsResConfigService = _DnsResConfigService_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 1, 2),
    _DnsResConfigService_Type()
)
dnsResConfigService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResConfigService.setStatus("current")


class _DnsResConfigMaxCnames_Type(Integer32):
    """Custom type dnsResConfigMaxCnames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DnsResConfigMaxCnames_Type.__name__ = "Integer32"
_DnsResConfigMaxCnames_Object = MibScalar
dnsResConfigMaxCnames = _DnsResConfigMaxCnames_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 1, 3),
    _DnsResConfigMaxCnames_Type()
)
dnsResConfigMaxCnames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsResConfigMaxCnames.setStatus("current")
_DnsResConfigSbeltTable_Object = MibTable
dnsResConfigSbeltTable = _DnsResConfigSbeltTable_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    dnsResConfigSbeltTable.setStatus("current")
_DnsResConfigSbeltEntry_Object = MibTableRow
dnsResConfigSbeltEntry = _DnsResConfigSbeltEntry_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 1, 4, 1)
)
dnsResConfigSbeltEntry.setIndexNames(
    (0, "DNS-RESOLVER-MIB", "dnsResConfigSbeltAddr"),
    (0, "DNS-RESOLVER-MIB", "dnsResConfigSbeltSubTree"),
    (0, "DNS-RESOLVER-MIB", "dnsResConfigSbeltClass"),
)
if mibBuilder.loadTexts:
    dnsResConfigSbeltEntry.setStatus("current")
_DnsResConfigSbeltAddr_Type = IpAddress
_DnsResConfigSbeltAddr_Object = MibTableColumn
dnsResConfigSbeltAddr = _DnsResConfigSbeltAddr_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 1, 4, 1, 1),
    _DnsResConfigSbeltAddr_Type()
)
dnsResConfigSbeltAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsResConfigSbeltAddr.setStatus("current")
_DnsResConfigSbeltName_Type = DnsName
_DnsResConfigSbeltName_Object = MibTableColumn
dnsResConfigSbeltName = _DnsResConfigSbeltName_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 1, 4, 1, 2),
    _DnsResConfigSbeltName_Type()
)
dnsResConfigSbeltName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsResConfigSbeltName.setStatus("current")


class _DnsResConfigSbeltRecursion_Type(Integer32):
    """Custom type dnsResConfigSbeltRecursion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("iterative", 1),
          ("recursive", 2),
          ("recursiveAndIterative", 3))
    )


_DnsResConfigSbeltRecursion_Type.__name__ = "Integer32"
_DnsResConfigSbeltRecursion_Object = MibTableColumn
dnsResConfigSbeltRecursion = _DnsResConfigSbeltRecursion_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 1, 4, 1, 3),
    _DnsResConfigSbeltRecursion_Type()
)
dnsResConfigSbeltRecursion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsResConfigSbeltRecursion.setStatus("current")


class _DnsResConfigSbeltPref_Type(Integer32):
    """Custom type dnsResConfigSbeltPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DnsResConfigSbeltPref_Type.__name__ = "Integer32"
_DnsResConfigSbeltPref_Object = MibTableColumn
dnsResConfigSbeltPref = _DnsResConfigSbeltPref_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 1, 4, 1, 4),
    _DnsResConfigSbeltPref_Type()
)
dnsResConfigSbeltPref.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsResConfigSbeltPref.setStatus("current")
_DnsResConfigSbeltSubTree_Type = DnsNameAsIndex
_DnsResConfigSbeltSubTree_Object = MibTableColumn
dnsResConfigSbeltSubTree = _DnsResConfigSbeltSubTree_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 1, 4, 1, 5),
    _DnsResConfigSbeltSubTree_Type()
)
dnsResConfigSbeltSubTree.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsResConfigSbeltSubTree.setStatus("current")
_DnsResConfigSbeltClass_Type = DnsClass
_DnsResConfigSbeltClass_Object = MibTableColumn
dnsResConfigSbeltClass = _DnsResConfigSbeltClass_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 1, 4, 1, 6),
    _DnsResConfigSbeltClass_Type()
)
dnsResConfigSbeltClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsResConfigSbeltClass.setStatus("current")
_DnsResConfigSbeltStatus_Type = RowStatus
_DnsResConfigSbeltStatus_Object = MibTableColumn
dnsResConfigSbeltStatus = _DnsResConfigSbeltStatus_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 1, 4, 1, 7),
    _DnsResConfigSbeltStatus_Type()
)
dnsResConfigSbeltStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsResConfigSbeltStatus.setStatus("current")
_DnsResConfigUpTime_Type = DnsTime
_DnsResConfigUpTime_Object = MibScalar
dnsResConfigUpTime = _DnsResConfigUpTime_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 1, 5),
    _DnsResConfigUpTime_Type()
)
dnsResConfigUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResConfigUpTime.setStatus("current")
_DnsResConfigResetTime_Type = DnsTime
_DnsResConfigResetTime_Object = MibScalar
dnsResConfigResetTime = _DnsResConfigResetTime_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 1, 6),
    _DnsResConfigResetTime_Type()
)
dnsResConfigResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResConfigResetTime.setStatus("current")


class _DnsResConfigReset_Type(Integer32):
    """Custom type dnsResConfigReset based on Integer32"""
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
        *(("initializing", 3),
          ("other", 1),
          ("reset", 2),
          ("running", 4))
    )


_DnsResConfigReset_Type.__name__ = "Integer32"
_DnsResConfigReset_Object = MibScalar
dnsResConfigReset = _DnsResConfigReset_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 1, 7),
    _DnsResConfigReset_Type()
)
dnsResConfigReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsResConfigReset.setStatus("current")
_DnsResCounter_ObjectIdentity = ObjectIdentity
dnsResCounter = _DnsResCounter_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 2)
)
_DnsResCounterByOpcodeTable_Object = MibTable
dnsResCounterByOpcodeTable = _DnsResCounterByOpcodeTable_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    dnsResCounterByOpcodeTable.setStatus("current")
_DnsResCounterByOpcodeEntry_Object = MibTableRow
dnsResCounterByOpcodeEntry = _DnsResCounterByOpcodeEntry_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 2, 3, 1)
)
dnsResCounterByOpcodeEntry.setIndexNames(
    (0, "DNS-RESOLVER-MIB", "dnsResCounterByOpcodeCode"),
)
if mibBuilder.loadTexts:
    dnsResCounterByOpcodeEntry.setStatus("current")
_DnsResCounterByOpcodeCode_Type = DnsOpCode
_DnsResCounterByOpcodeCode_Object = MibTableColumn
dnsResCounterByOpcodeCode = _DnsResCounterByOpcodeCode_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 2, 3, 1, 1),
    _DnsResCounterByOpcodeCode_Type()
)
dnsResCounterByOpcodeCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsResCounterByOpcodeCode.setStatus("current")
_DnsResCounterByOpcodeQueries_Type = Counter32
_DnsResCounterByOpcodeQueries_Object = MibTableColumn
dnsResCounterByOpcodeQueries = _DnsResCounterByOpcodeQueries_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 2, 3, 1, 2),
    _DnsResCounterByOpcodeQueries_Type()
)
dnsResCounterByOpcodeQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResCounterByOpcodeQueries.setStatus("current")
_DnsResCounterByOpcodeResponses_Type = Counter32
_DnsResCounterByOpcodeResponses_Object = MibTableColumn
dnsResCounterByOpcodeResponses = _DnsResCounterByOpcodeResponses_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 2, 3, 1, 3),
    _DnsResCounterByOpcodeResponses_Type()
)
dnsResCounterByOpcodeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResCounterByOpcodeResponses.setStatus("current")
_DnsResCounterByRcodeTable_Object = MibTable
dnsResCounterByRcodeTable = _DnsResCounterByRcodeTable_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    dnsResCounterByRcodeTable.setStatus("current")
_DnsResCounterByRcodeEntry_Object = MibTableRow
dnsResCounterByRcodeEntry = _DnsResCounterByRcodeEntry_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 2, 4, 1)
)
dnsResCounterByRcodeEntry.setIndexNames(
    (0, "DNS-RESOLVER-MIB", "dnsResCounterByRcodeCode"),
)
if mibBuilder.loadTexts:
    dnsResCounterByRcodeEntry.setStatus("current")
_DnsResCounterByRcodeCode_Type = DnsRespCode
_DnsResCounterByRcodeCode_Object = MibTableColumn
dnsResCounterByRcodeCode = _DnsResCounterByRcodeCode_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 2, 4, 1, 1),
    _DnsResCounterByRcodeCode_Type()
)
dnsResCounterByRcodeCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsResCounterByRcodeCode.setStatus("current")
_DnsResCounterByRcodeResponses_Type = Counter32
_DnsResCounterByRcodeResponses_Object = MibTableColumn
dnsResCounterByRcodeResponses = _DnsResCounterByRcodeResponses_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 2, 4, 1, 2),
    _DnsResCounterByRcodeResponses_Type()
)
dnsResCounterByRcodeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResCounterByRcodeResponses.setStatus("current")
_DnsResCounterNonAuthDataResps_Type = Counter32
_DnsResCounterNonAuthDataResps_Object = MibScalar
dnsResCounterNonAuthDataResps = _DnsResCounterNonAuthDataResps_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 2, 5),
    _DnsResCounterNonAuthDataResps_Type()
)
dnsResCounterNonAuthDataResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResCounterNonAuthDataResps.setStatus("current")
_DnsResCounterNonAuthNoDataResps_Type = Counter32
_DnsResCounterNonAuthNoDataResps_Object = MibScalar
dnsResCounterNonAuthNoDataResps = _DnsResCounterNonAuthNoDataResps_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 2, 6),
    _DnsResCounterNonAuthNoDataResps_Type()
)
dnsResCounterNonAuthNoDataResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResCounterNonAuthNoDataResps.setStatus("current")
_DnsResCounterMartians_Type = Counter32
_DnsResCounterMartians_Object = MibScalar
dnsResCounterMartians = _DnsResCounterMartians_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 2, 7),
    _DnsResCounterMartians_Type()
)
dnsResCounterMartians.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResCounterMartians.setStatus("current")
_DnsResCounterRecdResponses_Type = Counter32
_DnsResCounterRecdResponses_Object = MibScalar
dnsResCounterRecdResponses = _DnsResCounterRecdResponses_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 2, 8),
    _DnsResCounterRecdResponses_Type()
)
dnsResCounterRecdResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResCounterRecdResponses.setStatus("current")
_DnsResCounterUnparseResps_Type = Counter32
_DnsResCounterUnparseResps_Object = MibScalar
dnsResCounterUnparseResps = _DnsResCounterUnparseResps_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 2, 9),
    _DnsResCounterUnparseResps_Type()
)
dnsResCounterUnparseResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResCounterUnparseResps.setStatus("current")
_DnsResCounterFallbacks_Type = Counter32
_DnsResCounterFallbacks_Object = MibScalar
dnsResCounterFallbacks = _DnsResCounterFallbacks_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 2, 10),
    _DnsResCounterFallbacks_Type()
)
dnsResCounterFallbacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResCounterFallbacks.setStatus("current")
_DnsResLameDelegation_ObjectIdentity = ObjectIdentity
dnsResLameDelegation = _DnsResLameDelegation_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 3)
)
_DnsResLameDelegationOverflows_Type = Counter32
_DnsResLameDelegationOverflows_Object = MibScalar
dnsResLameDelegationOverflows = _DnsResLameDelegationOverflows_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 3, 1),
    _DnsResLameDelegationOverflows_Type()
)
dnsResLameDelegationOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResLameDelegationOverflows.setStatus("current")
_DnsResLameDelegationTable_Object = MibTable
dnsResLameDelegationTable = _DnsResLameDelegationTable_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dnsResLameDelegationTable.setStatus("current")
_DnsResLameDelegationEntry_Object = MibTableRow
dnsResLameDelegationEntry = _DnsResLameDelegationEntry_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 3, 2, 1)
)
dnsResLameDelegationEntry.setIndexNames(
    (0, "DNS-RESOLVER-MIB", "dnsResLameDelegationSource"),
    (0, "DNS-RESOLVER-MIB", "dnsResLameDelegationName"),
    (0, "DNS-RESOLVER-MIB", "dnsResLameDelegationClass"),
)
if mibBuilder.loadTexts:
    dnsResLameDelegationEntry.setStatus("current")
_DnsResLameDelegationSource_Type = IpAddress
_DnsResLameDelegationSource_Object = MibTableColumn
dnsResLameDelegationSource = _DnsResLameDelegationSource_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 3, 2, 1, 1),
    _DnsResLameDelegationSource_Type()
)
dnsResLameDelegationSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsResLameDelegationSource.setStatus("current")
_DnsResLameDelegationName_Type = DnsNameAsIndex
_DnsResLameDelegationName_Object = MibTableColumn
dnsResLameDelegationName = _DnsResLameDelegationName_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 3, 2, 1, 2),
    _DnsResLameDelegationName_Type()
)
dnsResLameDelegationName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsResLameDelegationName.setStatus("current")
_DnsResLameDelegationClass_Type = DnsClass
_DnsResLameDelegationClass_Object = MibTableColumn
dnsResLameDelegationClass = _DnsResLameDelegationClass_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 3, 2, 1, 3),
    _DnsResLameDelegationClass_Type()
)
dnsResLameDelegationClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsResLameDelegationClass.setStatus("current")
_DnsResLameDelegationCounts_Type = Counter32
_DnsResLameDelegationCounts_Object = MibTableColumn
dnsResLameDelegationCounts = _DnsResLameDelegationCounts_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 3, 2, 1, 4),
    _DnsResLameDelegationCounts_Type()
)
dnsResLameDelegationCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResLameDelegationCounts.setStatus("current")
_DnsResLameDelegationStatus_Type = RowStatus
_DnsResLameDelegationStatus_Object = MibTableColumn
dnsResLameDelegationStatus = _DnsResLameDelegationStatus_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 3, 2, 1, 5),
    _DnsResLameDelegationStatus_Type()
)
dnsResLameDelegationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsResLameDelegationStatus.setStatus("current")
_DnsResCache_ObjectIdentity = ObjectIdentity
dnsResCache = _DnsResCache_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 4)
)


class _DnsResCacheStatus_Type(Integer32):
    """Custom type dnsResCacheStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_DnsResCacheStatus_Type.__name__ = "Integer32"
_DnsResCacheStatus_Object = MibScalar
dnsResCacheStatus = _DnsResCacheStatus_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 4, 1),
    _DnsResCacheStatus_Type()
)
dnsResCacheStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsResCacheStatus.setStatus("current")
_DnsResCacheMaxTTL_Type = DnsTime
_DnsResCacheMaxTTL_Object = MibScalar
dnsResCacheMaxTTL = _DnsResCacheMaxTTL_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 4, 2),
    _DnsResCacheMaxTTL_Type()
)
dnsResCacheMaxTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsResCacheMaxTTL.setStatus("current")
_DnsResCacheGoodCaches_Type = Counter32
_DnsResCacheGoodCaches_Object = MibScalar
dnsResCacheGoodCaches = _DnsResCacheGoodCaches_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 4, 3),
    _DnsResCacheGoodCaches_Type()
)
dnsResCacheGoodCaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResCacheGoodCaches.setStatus("current")
_DnsResCacheBadCaches_Type = Counter32
_DnsResCacheBadCaches_Object = MibScalar
dnsResCacheBadCaches = _DnsResCacheBadCaches_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 4, 4),
    _DnsResCacheBadCaches_Type()
)
dnsResCacheBadCaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResCacheBadCaches.setStatus("current")
_DnsResCacheRRTable_Object = MibTable
dnsResCacheRRTable = _DnsResCacheRRTable_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 4, 5)
)
if mibBuilder.loadTexts:
    dnsResCacheRRTable.setStatus("current")
_DnsResCacheRREntry_Object = MibTableRow
dnsResCacheRREntry = _DnsResCacheRREntry_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 4, 5, 1)
)
dnsResCacheRREntry.setIndexNames(
    (0, "DNS-RESOLVER-MIB", "dnsResCacheRRName"),
    (0, "DNS-RESOLVER-MIB", "dnsResCacheRRClass"),
    (0, "DNS-RESOLVER-MIB", "dnsResCacheRRType"),
    (0, "DNS-RESOLVER-MIB", "dnsResCacheRRIndex"),
)
if mibBuilder.loadTexts:
    dnsResCacheRREntry.setStatus("current")
_DnsResCacheRRName_Type = DnsNameAsIndex
_DnsResCacheRRName_Object = MibTableColumn
dnsResCacheRRName = _DnsResCacheRRName_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 4, 5, 1, 1),
    _DnsResCacheRRName_Type()
)
dnsResCacheRRName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsResCacheRRName.setStatus("current")
_DnsResCacheRRClass_Type = DnsClass
_DnsResCacheRRClass_Object = MibTableColumn
dnsResCacheRRClass = _DnsResCacheRRClass_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 4, 5, 1, 2),
    _DnsResCacheRRClass_Type()
)
dnsResCacheRRClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsResCacheRRClass.setStatus("current")
_DnsResCacheRRType_Type = DnsType
_DnsResCacheRRType_Object = MibTableColumn
dnsResCacheRRType = _DnsResCacheRRType_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 4, 5, 1, 3),
    _DnsResCacheRRType_Type()
)
dnsResCacheRRType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsResCacheRRType.setStatus("current")
_DnsResCacheRRTTL_Type = DnsTime
_DnsResCacheRRTTL_Object = MibTableColumn
dnsResCacheRRTTL = _DnsResCacheRRTTL_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 4, 5, 1, 4),
    _DnsResCacheRRTTL_Type()
)
dnsResCacheRRTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResCacheRRTTL.setStatus("current")
_DnsResCacheRRElapsedTTL_Type = DnsTime
_DnsResCacheRRElapsedTTL_Object = MibTableColumn
dnsResCacheRRElapsedTTL = _DnsResCacheRRElapsedTTL_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 4, 5, 1, 5),
    _DnsResCacheRRElapsedTTL_Type()
)
dnsResCacheRRElapsedTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResCacheRRElapsedTTL.setStatus("current")
_DnsResCacheRRSource_Type = IpAddress
_DnsResCacheRRSource_Object = MibTableColumn
dnsResCacheRRSource = _DnsResCacheRRSource_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 4, 5, 1, 6),
    _DnsResCacheRRSource_Type()
)
dnsResCacheRRSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResCacheRRSource.setStatus("current")
_DnsResCacheRRData_Type = OctetString
_DnsResCacheRRData_Object = MibTableColumn
dnsResCacheRRData = _DnsResCacheRRData_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 4, 5, 1, 7),
    _DnsResCacheRRData_Type()
)
dnsResCacheRRData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResCacheRRData.setStatus("current")
_DnsResCacheRRStatus_Type = RowStatus
_DnsResCacheRRStatus_Object = MibTableColumn
dnsResCacheRRStatus = _DnsResCacheRRStatus_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 4, 5, 1, 8),
    _DnsResCacheRRStatus_Type()
)
dnsResCacheRRStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsResCacheRRStatus.setStatus("current")
_DnsResCacheRRIndex_Type = Integer32
_DnsResCacheRRIndex_Object = MibTableColumn
dnsResCacheRRIndex = _DnsResCacheRRIndex_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 4, 5, 1, 9),
    _DnsResCacheRRIndex_Type()
)
dnsResCacheRRIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsResCacheRRIndex.setStatus("current")
_DnsResCacheRRPrettyName_Type = DnsName
_DnsResCacheRRPrettyName_Object = MibTableColumn
dnsResCacheRRPrettyName = _DnsResCacheRRPrettyName_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 4, 5, 1, 10),
    _DnsResCacheRRPrettyName_Type()
)
dnsResCacheRRPrettyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResCacheRRPrettyName.setStatus("current")
_DnsResNCache_ObjectIdentity = ObjectIdentity
dnsResNCache = _DnsResNCache_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 5)
)


class _DnsResNCacheStatus_Type(Integer32):
    """Custom type dnsResNCacheStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_DnsResNCacheStatus_Type.__name__ = "Integer32"
_DnsResNCacheStatus_Object = MibScalar
dnsResNCacheStatus = _DnsResNCacheStatus_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 5, 1),
    _DnsResNCacheStatus_Type()
)
dnsResNCacheStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsResNCacheStatus.setStatus("current")
_DnsResNCacheMaxTTL_Type = DnsTime
_DnsResNCacheMaxTTL_Object = MibScalar
dnsResNCacheMaxTTL = _DnsResNCacheMaxTTL_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 5, 2),
    _DnsResNCacheMaxTTL_Type()
)
dnsResNCacheMaxTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsResNCacheMaxTTL.setStatus("current")
_DnsResNCacheGoodNCaches_Type = Counter32
_DnsResNCacheGoodNCaches_Object = MibScalar
dnsResNCacheGoodNCaches = _DnsResNCacheGoodNCaches_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 5, 3),
    _DnsResNCacheGoodNCaches_Type()
)
dnsResNCacheGoodNCaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResNCacheGoodNCaches.setStatus("current")
_DnsResNCacheBadNCaches_Type = Counter32
_DnsResNCacheBadNCaches_Object = MibScalar
dnsResNCacheBadNCaches = _DnsResNCacheBadNCaches_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 5, 4),
    _DnsResNCacheBadNCaches_Type()
)
dnsResNCacheBadNCaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResNCacheBadNCaches.setStatus("current")
_DnsResNCacheErrTable_Object = MibTable
dnsResNCacheErrTable = _DnsResNCacheErrTable_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 5, 5)
)
if mibBuilder.loadTexts:
    dnsResNCacheErrTable.setStatus("current")
_DnsResNCacheErrEntry_Object = MibTableRow
dnsResNCacheErrEntry = _DnsResNCacheErrEntry_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 5, 5, 1)
)
dnsResNCacheErrEntry.setIndexNames(
    (0, "DNS-RESOLVER-MIB", "dnsResNCacheErrQName"),
    (0, "DNS-RESOLVER-MIB", "dnsResNCacheErrQClass"),
    (0, "DNS-RESOLVER-MIB", "dnsResNCacheErrQType"),
    (0, "DNS-RESOLVER-MIB", "dnsResNCacheErrIndex"),
)
if mibBuilder.loadTexts:
    dnsResNCacheErrEntry.setStatus("current")
_DnsResNCacheErrQName_Type = DnsNameAsIndex
_DnsResNCacheErrQName_Object = MibTableColumn
dnsResNCacheErrQName = _DnsResNCacheErrQName_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 5, 5, 1, 1),
    _DnsResNCacheErrQName_Type()
)
dnsResNCacheErrQName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsResNCacheErrQName.setStatus("current")
_DnsResNCacheErrQClass_Type = DnsQClass
_DnsResNCacheErrQClass_Object = MibTableColumn
dnsResNCacheErrQClass = _DnsResNCacheErrQClass_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 5, 5, 1, 2),
    _DnsResNCacheErrQClass_Type()
)
dnsResNCacheErrQClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsResNCacheErrQClass.setStatus("current")
_DnsResNCacheErrQType_Type = DnsQType
_DnsResNCacheErrQType_Object = MibTableColumn
dnsResNCacheErrQType = _DnsResNCacheErrQType_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 5, 5, 1, 3),
    _DnsResNCacheErrQType_Type()
)
dnsResNCacheErrQType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsResNCacheErrQType.setStatus("current")
_DnsResNCacheErrTTL_Type = DnsTime
_DnsResNCacheErrTTL_Object = MibTableColumn
dnsResNCacheErrTTL = _DnsResNCacheErrTTL_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 5, 5, 1, 4),
    _DnsResNCacheErrTTL_Type()
)
dnsResNCacheErrTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResNCacheErrTTL.setStatus("current")
_DnsResNCacheErrElapsedTTL_Type = DnsTime
_DnsResNCacheErrElapsedTTL_Object = MibTableColumn
dnsResNCacheErrElapsedTTL = _DnsResNCacheErrElapsedTTL_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 5, 5, 1, 5),
    _DnsResNCacheErrElapsedTTL_Type()
)
dnsResNCacheErrElapsedTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResNCacheErrElapsedTTL.setStatus("current")
_DnsResNCacheErrSource_Type = IpAddress
_DnsResNCacheErrSource_Object = MibTableColumn
dnsResNCacheErrSource = _DnsResNCacheErrSource_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 5, 5, 1, 6),
    _DnsResNCacheErrSource_Type()
)
dnsResNCacheErrSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResNCacheErrSource.setStatus("current")


class _DnsResNCacheErrCode_Type(Integer32):
    """Custom type dnsResNCacheErrCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noData", 2),
          ("nonexistantName", 1),
          ("other", 3))
    )


_DnsResNCacheErrCode_Type.__name__ = "Integer32"
_DnsResNCacheErrCode_Object = MibTableColumn
dnsResNCacheErrCode = _DnsResNCacheErrCode_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 5, 5, 1, 7),
    _DnsResNCacheErrCode_Type()
)
dnsResNCacheErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResNCacheErrCode.setStatus("current")
_DnsResNCacheErrStatus_Type = RowStatus
_DnsResNCacheErrStatus_Object = MibTableColumn
dnsResNCacheErrStatus = _DnsResNCacheErrStatus_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 5, 5, 1, 8),
    _DnsResNCacheErrStatus_Type()
)
dnsResNCacheErrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsResNCacheErrStatus.setStatus("current")
_DnsResNCacheErrIndex_Type = Integer32
_DnsResNCacheErrIndex_Object = MibTableColumn
dnsResNCacheErrIndex = _DnsResNCacheErrIndex_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 5, 5, 1, 9),
    _DnsResNCacheErrIndex_Type()
)
dnsResNCacheErrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResNCacheErrIndex.setStatus("current")
_DnsResNCacheErrPrettyName_Type = DnsName
_DnsResNCacheErrPrettyName_Object = MibTableColumn
dnsResNCacheErrPrettyName = _DnsResNCacheErrPrettyName_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 5, 5, 1, 10),
    _DnsResNCacheErrPrettyName_Type()
)
dnsResNCacheErrPrettyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResNCacheErrPrettyName.setStatus("current")
_DnsResOptCounter_ObjectIdentity = ObjectIdentity
dnsResOptCounter = _DnsResOptCounter_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 6)
)
_DnsResOptCounterReferals_Type = Counter32
_DnsResOptCounterReferals_Object = MibScalar
dnsResOptCounterReferals = _DnsResOptCounterReferals_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 6, 1),
    _DnsResOptCounterReferals_Type()
)
dnsResOptCounterReferals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResOptCounterReferals.setStatus("current")
_DnsResOptCounterRetrans_Type = Counter32
_DnsResOptCounterRetrans_Object = MibScalar
dnsResOptCounterRetrans = _DnsResOptCounterRetrans_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 6, 2),
    _DnsResOptCounterRetrans_Type()
)
dnsResOptCounterRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResOptCounterRetrans.setStatus("current")
_DnsResOptCounterNoResponses_Type = Counter32
_DnsResOptCounterNoResponses_Object = MibScalar
dnsResOptCounterNoResponses = _DnsResOptCounterNoResponses_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 6, 3),
    _DnsResOptCounterNoResponses_Type()
)
dnsResOptCounterNoResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResOptCounterNoResponses.setStatus("current")
_DnsResOptCounterRootRetrans_Type = Counter32
_DnsResOptCounterRootRetrans_Object = MibScalar
dnsResOptCounterRootRetrans = _DnsResOptCounterRootRetrans_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 6, 4),
    _DnsResOptCounterRootRetrans_Type()
)
dnsResOptCounterRootRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResOptCounterRootRetrans.setStatus("current")
_DnsResOptCounterInternals_Type = Counter32
_DnsResOptCounterInternals_Object = MibScalar
dnsResOptCounterInternals = _DnsResOptCounterInternals_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 6, 5),
    _DnsResOptCounterInternals_Type()
)
dnsResOptCounterInternals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResOptCounterInternals.setStatus("current")
_DnsResOptCounterInternalTimeOuts_Type = Counter32
_DnsResOptCounterInternalTimeOuts_Object = MibScalar
dnsResOptCounterInternalTimeOuts = _DnsResOptCounterInternalTimeOuts_Object(
    (1, 3, 6, 1, 2, 1, 32, 2, 1, 6, 6),
    _DnsResOptCounterInternalTimeOuts_Type()
)
dnsResOptCounterInternalTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsResOptCounterInternalTimeOuts.setStatus("current")
_DnsResMIBGroups_ObjectIdentity = ObjectIdentity
dnsResMIBGroups = _DnsResMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 32, 2, 2)
)
_DnsResMIBCompliances_ObjectIdentity = ObjectIdentity
dnsResMIBCompliances = _DnsResMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 32, 2, 3)
)

# Managed Objects groups

dnsResConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 32, 2, 2, 1)
)
dnsResConfigGroup.setObjects(
      *(("DNS-RESOLVER-MIB", "dnsResConfigImplementIdent"),
        ("DNS-RESOLVER-MIB", "dnsResConfigService"),
        ("DNS-RESOLVER-MIB", "dnsResConfigMaxCnames"),
        ("DNS-RESOLVER-MIB", "dnsResConfigSbeltName"),
        ("DNS-RESOLVER-MIB", "dnsResConfigSbeltRecursion"),
        ("DNS-RESOLVER-MIB", "dnsResConfigSbeltPref"),
        ("DNS-RESOLVER-MIB", "dnsResConfigSbeltStatus"),
        ("DNS-RESOLVER-MIB", "dnsResConfigUpTime"),
        ("DNS-RESOLVER-MIB", "dnsResConfigResetTime"),
        ("DNS-RESOLVER-MIB", "dnsResConfigReset"))
)
if mibBuilder.loadTexts:
    dnsResConfigGroup.setStatus("current")

dnsResCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 32, 2, 2, 2)
)
dnsResCounterGroup.setObjects(
      *(("DNS-RESOLVER-MIB", "dnsResCounterByOpcodeQueries"),
        ("DNS-RESOLVER-MIB", "dnsResCounterByOpcodeResponses"),
        ("DNS-RESOLVER-MIB", "dnsResCounterByRcodeResponses"),
        ("DNS-RESOLVER-MIB", "dnsResCounterNonAuthDataResps"),
        ("DNS-RESOLVER-MIB", "dnsResCounterNonAuthNoDataResps"),
        ("DNS-RESOLVER-MIB", "dnsResCounterMartians"),
        ("DNS-RESOLVER-MIB", "dnsResCounterRecdResponses"),
        ("DNS-RESOLVER-MIB", "dnsResCounterUnparseResps"),
        ("DNS-RESOLVER-MIB", "dnsResCounterFallbacks"))
)
if mibBuilder.loadTexts:
    dnsResCounterGroup.setStatus("current")

dnsResLameDelegationGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 32, 2, 2, 3)
)
dnsResLameDelegationGroup.setObjects(
      *(("DNS-RESOLVER-MIB", "dnsResLameDelegationOverflows"),
        ("DNS-RESOLVER-MIB", "dnsResLameDelegationCounts"),
        ("DNS-RESOLVER-MIB", "dnsResLameDelegationStatus"))
)
if mibBuilder.loadTexts:
    dnsResLameDelegationGroup.setStatus("current")

dnsResCacheGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 32, 2, 2, 4)
)
dnsResCacheGroup.setObjects(
      *(("DNS-RESOLVER-MIB", "dnsResCacheStatus"),
        ("DNS-RESOLVER-MIB", "dnsResCacheMaxTTL"),
        ("DNS-RESOLVER-MIB", "dnsResCacheGoodCaches"),
        ("DNS-RESOLVER-MIB", "dnsResCacheBadCaches"),
        ("DNS-RESOLVER-MIB", "dnsResCacheRRTTL"),
        ("DNS-RESOLVER-MIB", "dnsResCacheRRElapsedTTL"),
        ("DNS-RESOLVER-MIB", "dnsResCacheRRSource"),
        ("DNS-RESOLVER-MIB", "dnsResCacheRRData"),
        ("DNS-RESOLVER-MIB", "dnsResCacheRRStatus"),
        ("DNS-RESOLVER-MIB", "dnsResCacheRRPrettyName"))
)
if mibBuilder.loadTexts:
    dnsResCacheGroup.setStatus("current")

dnsResNCacheGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 32, 2, 2, 5)
)
dnsResNCacheGroup.setObjects(
      *(("DNS-RESOLVER-MIB", "dnsResNCacheStatus"),
        ("DNS-RESOLVER-MIB", "dnsResNCacheMaxTTL"),
        ("DNS-RESOLVER-MIB", "dnsResNCacheGoodNCaches"),
        ("DNS-RESOLVER-MIB", "dnsResNCacheBadNCaches"),
        ("DNS-RESOLVER-MIB", "dnsResNCacheErrTTL"),
        ("DNS-RESOLVER-MIB", "dnsResNCacheErrElapsedTTL"),
        ("DNS-RESOLVER-MIB", "dnsResNCacheErrSource"),
        ("DNS-RESOLVER-MIB", "dnsResNCacheErrCode"),
        ("DNS-RESOLVER-MIB", "dnsResNCacheErrStatus"),
        ("DNS-RESOLVER-MIB", "dnsResNCacheErrIndex"),
        ("DNS-RESOLVER-MIB", "dnsResNCacheErrPrettyName"))
)
if mibBuilder.loadTexts:
    dnsResNCacheGroup.setStatus("current")

dnsResOptCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 32, 2, 2, 6)
)
dnsResOptCounterGroup.setObjects(
      *(("DNS-RESOLVER-MIB", "dnsResOptCounterReferals"),
        ("DNS-RESOLVER-MIB", "dnsResOptCounterRetrans"),
        ("DNS-RESOLVER-MIB", "dnsResOptCounterNoResponses"),
        ("DNS-RESOLVER-MIB", "dnsResOptCounterRootRetrans"),
        ("DNS-RESOLVER-MIB", "dnsResOptCounterInternals"),
        ("DNS-RESOLVER-MIB", "dnsResOptCounterInternalTimeOuts"))
)
if mibBuilder.loadTexts:
    dnsResOptCounterGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dnsResMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 32, 2, 3, 1)
)
if mibBuilder.loadTexts:
    dnsResMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNS-RESOLVER-MIB",
    **{"DnsQClass": DnsQClass,
       "DnsQType": DnsQType,
       "DnsRespCode": DnsRespCode,
       "dnsResMIB": dnsResMIB,
       "dnsResMIBObjects": dnsResMIBObjects,
       "dnsResConfig": dnsResConfig,
       "dnsResConfigImplementIdent": dnsResConfigImplementIdent,
       "dnsResConfigService": dnsResConfigService,
       "dnsResConfigMaxCnames": dnsResConfigMaxCnames,
       "dnsResConfigSbeltTable": dnsResConfigSbeltTable,
       "dnsResConfigSbeltEntry": dnsResConfigSbeltEntry,
       "dnsResConfigSbeltAddr": dnsResConfigSbeltAddr,
       "dnsResConfigSbeltName": dnsResConfigSbeltName,
       "dnsResConfigSbeltRecursion": dnsResConfigSbeltRecursion,
       "dnsResConfigSbeltPref": dnsResConfigSbeltPref,
       "dnsResConfigSbeltSubTree": dnsResConfigSbeltSubTree,
       "dnsResConfigSbeltClass": dnsResConfigSbeltClass,
       "dnsResConfigSbeltStatus": dnsResConfigSbeltStatus,
       "dnsResConfigUpTime": dnsResConfigUpTime,
       "dnsResConfigResetTime": dnsResConfigResetTime,
       "dnsResConfigReset": dnsResConfigReset,
       "dnsResCounter": dnsResCounter,
       "dnsResCounterByOpcodeTable": dnsResCounterByOpcodeTable,
       "dnsResCounterByOpcodeEntry": dnsResCounterByOpcodeEntry,
       "dnsResCounterByOpcodeCode": dnsResCounterByOpcodeCode,
       "dnsResCounterByOpcodeQueries": dnsResCounterByOpcodeQueries,
       "dnsResCounterByOpcodeResponses": dnsResCounterByOpcodeResponses,
       "dnsResCounterByRcodeTable": dnsResCounterByRcodeTable,
       "dnsResCounterByRcodeEntry": dnsResCounterByRcodeEntry,
       "dnsResCounterByRcodeCode": dnsResCounterByRcodeCode,
       "dnsResCounterByRcodeResponses": dnsResCounterByRcodeResponses,
       "dnsResCounterNonAuthDataResps": dnsResCounterNonAuthDataResps,
       "dnsResCounterNonAuthNoDataResps": dnsResCounterNonAuthNoDataResps,
       "dnsResCounterMartians": dnsResCounterMartians,
       "dnsResCounterRecdResponses": dnsResCounterRecdResponses,
       "dnsResCounterUnparseResps": dnsResCounterUnparseResps,
       "dnsResCounterFallbacks": dnsResCounterFallbacks,
       "dnsResLameDelegation": dnsResLameDelegation,
       "dnsResLameDelegationOverflows": dnsResLameDelegationOverflows,
       "dnsResLameDelegationTable": dnsResLameDelegationTable,
       "dnsResLameDelegationEntry": dnsResLameDelegationEntry,
       "dnsResLameDelegationSource": dnsResLameDelegationSource,
       "dnsResLameDelegationName": dnsResLameDelegationName,
       "dnsResLameDelegationClass": dnsResLameDelegationClass,
       "dnsResLameDelegationCounts": dnsResLameDelegationCounts,
       "dnsResLameDelegationStatus": dnsResLameDelegationStatus,
       "dnsResCache": dnsResCache,
       "dnsResCacheStatus": dnsResCacheStatus,
       "dnsResCacheMaxTTL": dnsResCacheMaxTTL,
       "dnsResCacheGoodCaches": dnsResCacheGoodCaches,
       "dnsResCacheBadCaches": dnsResCacheBadCaches,
       "dnsResCacheRRTable": dnsResCacheRRTable,
       "dnsResCacheRREntry": dnsResCacheRREntry,
       "dnsResCacheRRName": dnsResCacheRRName,
       "dnsResCacheRRClass": dnsResCacheRRClass,
       "dnsResCacheRRType": dnsResCacheRRType,
       "dnsResCacheRRTTL": dnsResCacheRRTTL,
       "dnsResCacheRRElapsedTTL": dnsResCacheRRElapsedTTL,
       "dnsResCacheRRSource": dnsResCacheRRSource,
       "dnsResCacheRRData": dnsResCacheRRData,
       "dnsResCacheRRStatus": dnsResCacheRRStatus,
       "dnsResCacheRRIndex": dnsResCacheRRIndex,
       "dnsResCacheRRPrettyName": dnsResCacheRRPrettyName,
       "dnsResNCache": dnsResNCache,
       "dnsResNCacheStatus": dnsResNCacheStatus,
       "dnsResNCacheMaxTTL": dnsResNCacheMaxTTL,
       "dnsResNCacheGoodNCaches": dnsResNCacheGoodNCaches,
       "dnsResNCacheBadNCaches": dnsResNCacheBadNCaches,
       "dnsResNCacheErrTable": dnsResNCacheErrTable,
       "dnsResNCacheErrEntry": dnsResNCacheErrEntry,
       "dnsResNCacheErrQName": dnsResNCacheErrQName,
       "dnsResNCacheErrQClass": dnsResNCacheErrQClass,
       "dnsResNCacheErrQType": dnsResNCacheErrQType,
       "dnsResNCacheErrTTL": dnsResNCacheErrTTL,
       "dnsResNCacheErrElapsedTTL": dnsResNCacheErrElapsedTTL,
       "dnsResNCacheErrSource": dnsResNCacheErrSource,
       "dnsResNCacheErrCode": dnsResNCacheErrCode,
       "dnsResNCacheErrStatus": dnsResNCacheErrStatus,
       "dnsResNCacheErrIndex": dnsResNCacheErrIndex,
       "dnsResNCacheErrPrettyName": dnsResNCacheErrPrettyName,
       "dnsResOptCounter": dnsResOptCounter,
       "dnsResOptCounterReferals": dnsResOptCounterReferals,
       "dnsResOptCounterRetrans": dnsResOptCounterRetrans,
       "dnsResOptCounterNoResponses": dnsResOptCounterNoResponses,
       "dnsResOptCounterRootRetrans": dnsResOptCounterRootRetrans,
       "dnsResOptCounterInternals": dnsResOptCounterInternals,
       "dnsResOptCounterInternalTimeOuts": dnsResOptCounterInternalTimeOuts,
       "dnsResMIBGroups": dnsResMIBGroups,
       "dnsResConfigGroup": dnsResConfigGroup,
       "dnsResCounterGroup": dnsResCounterGroup,
       "dnsResLameDelegationGroup": dnsResLameDelegationGroup,
       "dnsResCacheGroup": dnsResCacheGroup,
       "dnsResNCacheGroup": dnsResNCacheGroup,
       "dnsResOptCounterGroup": dnsResOptCounterGroup,
       "dnsResMIBCompliances": dnsResMIBCompliances,
       "dnsResMIBCompliance": dnsResMIBCompliance}
)
