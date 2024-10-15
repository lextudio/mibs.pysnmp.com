# SNMP MIB module (CISCO-CRYPTO-ACCELERATOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CRYPTO-ACCELERATOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:49 2024
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

(ModuleOperType,) = mibBuilder.importSymbols(
    "CISCO-ENTITY-FRU-CONTROL-MIB",
    "ModuleOperType")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(EntPhysicalIndexOrZero,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "EntPhysicalIndexOrZero")

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

ciscoCryptoAcceleratorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 467)
)
ciscoCryptoAcceleratorMIB.setRevisions(
        ("2005-03-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CAModuleType(Integer32, TextualConvention):
    status = "current"
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
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("a1700VpnModule", 6),
          ("aimVpnIBp", 7),
          ("aimVpnIEp", 8),
          ("aimVpnIIBp", 9),
          ("aimVpnIIEp", 10),
          ("aimVpnIIHp", 11),
          ("caviumNitrox", 17),
          ("caviumNitroxII", 18),
          ("caviumNitroxLite", 19),
          ("integrated", 3),
          ("isa", 12),
          ("other", 1),
          ("sep", 4),
          ("sepe", 5),
          ("software", 2),
          ("vam", 13),
          ("vam2", 14),
          ("vam2plus", 15),
          ("vpnsm", 16))
    )



class CAModuleCount(Unsigned32, TextualConvention):
    status = "current"


class CAProtocolType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ikev1", 2),
          ("ikev2", 3),
          ("ipsec", 4),
          ("other", 1),
          ("srtp", 7),
          ("ssh", 6),
          ("ssl", 5))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoCryAcceleratorMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoCryAcceleratorMIBNotifs = _CiscoCryAcceleratorMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 0)
)
_CiscoCryAcceleratorMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCryAcceleratorMIBObjects = _CiscoCryAcceleratorMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1)
)
_CcaCapability_ObjectIdentity = ObjectIdentity
ccaCapability = _CcaCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 1)
)
_CcaSupportsHwCrypto_Type = TruthValue
_CcaSupportsHwCrypto_Object = MibScalar
ccaSupportsHwCrypto = _CcaSupportsHwCrypto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 1, 1),
    _CcaSupportsHwCrypto_Type()
)
ccaSupportsHwCrypto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaSupportsHwCrypto.setStatus("current")
_CcaSupportsModularHwCrypto_Type = TruthValue
_CcaSupportsModularHwCrypto_Object = MibScalar
ccaSupportsModularHwCrypto = _CcaSupportsModularHwCrypto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 1, 2),
    _CcaSupportsModularHwCrypto_Type()
)
ccaSupportsModularHwCrypto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaSupportsModularHwCrypto.setStatus("current")


class _CcaMaxAccelerators_Type(Integer32):
    """Custom type ccaMaxAccelerators based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 50),
    )


_CcaMaxAccelerators_Type.__name__ = "Integer32"
_CcaMaxAccelerators_Object = MibScalar
ccaMaxAccelerators = _CcaMaxAccelerators_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 1, 3),
    _CcaMaxAccelerators_Type()
)
ccaMaxAccelerators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaMaxAccelerators.setStatus("current")
_CcaMaxCryptoThroughput_Type = Unsigned32
_CcaMaxCryptoThroughput_Object = MibScalar
ccaMaxCryptoThroughput = _CcaMaxCryptoThroughput_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 1, 4),
    _CcaMaxCryptoThroughput_Type()
)
ccaMaxCryptoThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaMaxCryptoThroughput.setStatus("current")
if mibBuilder.loadTexts:
    ccaMaxCryptoThroughput.setUnits("megabits per second")
_CcaMaxCryptoConnections_Type = Unsigned32
_CcaMaxCryptoConnections_Object = MibScalar
ccaMaxCryptoConnections = _CcaMaxCryptoConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 1, 5),
    _CcaMaxCryptoConnections_Type()
)
ccaMaxCryptoConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaMaxCryptoConnections.setStatus("current")
_CcaActivity_ObjectIdentity = ObjectIdentity
ccaActivity = _CcaActivity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2)
)
_CcaGlobalStats_ObjectIdentity = ObjectIdentity
ccaGlobalStats = _CcaGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 1)
)
_CcaGlobalNumActiveAccelerators_Type = CAModuleCount
_CcaGlobalNumActiveAccelerators_Object = MibScalar
ccaGlobalNumActiveAccelerators = _CcaGlobalNumActiveAccelerators_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 1, 1),
    _CcaGlobalNumActiveAccelerators_Type()
)
ccaGlobalNumActiveAccelerators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaGlobalNumActiveAccelerators.setStatus("current")
_CcaGlobalNumNonOperAccelerators_Type = CAModuleCount
_CcaGlobalNumNonOperAccelerators_Object = MibScalar
ccaGlobalNumNonOperAccelerators = _CcaGlobalNumNonOperAccelerators_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 1, 2),
    _CcaGlobalNumNonOperAccelerators_Type()
)
ccaGlobalNumNonOperAccelerators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaGlobalNumNonOperAccelerators.setStatus("current")
_CcaGlobalInOctets_Type = Counter64
_CcaGlobalInOctets_Object = MibScalar
ccaGlobalInOctets = _CcaGlobalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 1, 3),
    _CcaGlobalInOctets_Type()
)
ccaGlobalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaGlobalInOctets.setStatus("current")
_CcaGlobalOutOctets_Type = Counter64
_CcaGlobalOutOctets_Object = MibScalar
ccaGlobalOutOctets = _CcaGlobalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 1, 4),
    _CcaGlobalOutOctets_Type()
)
ccaGlobalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaGlobalOutOctets.setStatus("current")
_CcaGlobalInPkts_Type = Counter64
_CcaGlobalInPkts_Object = MibScalar
ccaGlobalInPkts = _CcaGlobalInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 1, 5),
    _CcaGlobalInPkts_Type()
)
ccaGlobalInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaGlobalInPkts.setStatus("current")
_CcaGlobalOutPkts_Type = Counter64
_CcaGlobalOutPkts_Object = MibScalar
ccaGlobalOutPkts = _CcaGlobalOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 1, 6),
    _CcaGlobalOutPkts_Type()
)
ccaGlobalOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaGlobalOutPkts.setStatus("current")
_CcaGlobalOutErrPkts_Type = Counter64
_CcaGlobalOutErrPkts_Object = MibScalar
ccaGlobalOutErrPkts = _CcaGlobalOutErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 1, 7),
    _CcaGlobalOutErrPkts_Type()
)
ccaGlobalOutErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaGlobalOutErrPkts.setStatus("current")
_CcaAcceleratorTable_Object = MibTable
ccaAcceleratorTable = _CcaAcceleratorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ccaAcceleratorTable.setStatus("current")
_CcaAcceleratorEntry_Object = MibTableRow
ccaAcceleratorEntry = _CcaAcceleratorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1)
)
ccaAcceleratorEntry.setIndexNames(
    (0, "CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclIndex"),
)
if mibBuilder.loadTexts:
    ccaAcceleratorEntry.setStatus("current")


class _CcaAcclIndex_Type(Unsigned32):
    """Custom type ccaAcclIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_CcaAcclIndex_Type.__name__ = "Unsigned32"
_CcaAcclIndex_Object = MibTableColumn
ccaAcclIndex = _CcaAcclIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 1),
    _CcaAcclIndex_Type()
)
ccaAcclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccaAcclIndex.setStatus("current")
_CcaAcclEntPhysicalIndex_Type = EntPhysicalIndexOrZero
_CcaAcclEntPhysicalIndex_Object = MibTableColumn
ccaAcclEntPhysicalIndex = _CcaAcclEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 2),
    _CcaAcclEntPhysicalIndex_Type()
)
ccaAcclEntPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclEntPhysicalIndex.setStatus("current")
_CcaAcclStatus_Type = ModuleOperType
_CcaAcclStatus_Object = MibTableColumn
ccaAcclStatus = _CcaAcclStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 3),
    _CcaAcclStatus_Type()
)
ccaAcclStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclStatus.setStatus("current")
_CcaAcclType_Type = CAModuleType
_CcaAcclType_Object = MibTableColumn
ccaAcclType = _CcaAcclType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 4),
    _CcaAcclType_Type()
)
ccaAcclType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclType.setStatus("current")
_CcaAcclVersion_Type = SnmpAdminString
_CcaAcclVersion_Object = MibTableColumn
ccaAcclVersion = _CcaAcclVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 5),
    _CcaAcclVersion_Type()
)
ccaAcclVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclVersion.setStatus("current")
_CcaAcclSlot_Type = Unsigned32
_CcaAcclSlot_Object = MibTableColumn
ccaAcclSlot = _CcaAcclSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 6),
    _CcaAcclSlot_Type()
)
ccaAcclSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclSlot.setStatus("current")
_CcaAcclActiveTime_Type = TimeTicks
_CcaAcclActiveTime_Object = MibTableColumn
ccaAcclActiveTime = _CcaAcclActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 7),
    _CcaAcclActiveTime_Type()
)
ccaAcclActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    ccaAcclActiveTime.setUnits("seconds")
_CcaAcclInPkts_Type = Counter64
_CcaAcclInPkts_Object = MibTableColumn
ccaAcclInPkts = _CcaAcclInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 8),
    _CcaAcclInPkts_Type()
)
ccaAcclInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclInPkts.setStatus("current")
_CcaAcclOutPkts_Type = Counter64
_CcaAcclOutPkts_Object = MibTableColumn
ccaAcclOutPkts = _CcaAcclOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 9),
    _CcaAcclOutPkts_Type()
)
ccaAcclOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclOutPkts.setStatus("current")
_CcaAcclOutBadPkts_Type = Counter64
_CcaAcclOutBadPkts_Object = MibTableColumn
ccaAcclOutBadPkts = _CcaAcclOutBadPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 10),
    _CcaAcclOutBadPkts_Type()
)
ccaAcclOutBadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclOutBadPkts.setStatus("current")
_CcaAcclInOctets_Type = Counter64
_CcaAcclInOctets_Object = MibTableColumn
ccaAcclInOctets = _CcaAcclInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 11),
    _CcaAcclInOctets_Type()
)
ccaAcclInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclInOctets.setStatus("current")
_CcaAcclOutOctets_Type = Counter64
_CcaAcclOutOctets_Object = MibTableColumn
ccaAcclOutOctets = _CcaAcclOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 12),
    _CcaAcclOutOctets_Type()
)
ccaAcclOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclOutOctets.setStatus("current")
_CcaAcclHashOutboundPkts_Type = Counter64
_CcaAcclHashOutboundPkts_Object = MibTableColumn
ccaAcclHashOutboundPkts = _CcaAcclHashOutboundPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 13),
    _CcaAcclHashOutboundPkts_Type()
)
ccaAcclHashOutboundPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclHashOutboundPkts.setStatus("current")
_CcaAcclHashOutboundOctets_Type = Counter64
_CcaAcclHashOutboundOctets_Object = MibTableColumn
ccaAcclHashOutboundOctets = _CcaAcclHashOutboundOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 14),
    _CcaAcclHashOutboundOctets_Type()
)
ccaAcclHashOutboundOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclHashOutboundOctets.setStatus("current")
_CcaAcclHashInboundPkts_Type = Counter64
_CcaAcclHashInboundPkts_Object = MibTableColumn
ccaAcclHashInboundPkts = _CcaAcclHashInboundPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 15),
    _CcaAcclHashInboundPkts_Type()
)
ccaAcclHashInboundPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclHashInboundPkts.setStatus("current")
_CcaAcclHashInboundOctets_Type = Counter64
_CcaAcclHashInboundOctets_Object = MibTableColumn
ccaAcclHashInboundOctets = _CcaAcclHashInboundOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 16),
    _CcaAcclHashInboundOctets_Type()
)
ccaAcclHashInboundOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclHashInboundOctets.setStatus("current")
_CcaAcclEncryptPkts_Type = Counter64
_CcaAcclEncryptPkts_Object = MibTableColumn
ccaAcclEncryptPkts = _CcaAcclEncryptPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 17),
    _CcaAcclEncryptPkts_Type()
)
ccaAcclEncryptPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclEncryptPkts.setStatus("current")
_CcaAcclEncryptOctets_Type = Counter64
_CcaAcclEncryptOctets_Object = MibTableColumn
ccaAcclEncryptOctets = _CcaAcclEncryptOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 18),
    _CcaAcclEncryptOctets_Type()
)
ccaAcclEncryptOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclEncryptOctets.setStatus("current")
_CcaAcclDecryptPkts_Type = Counter64
_CcaAcclDecryptPkts_Object = MibTableColumn
ccaAcclDecryptPkts = _CcaAcclDecryptPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 19),
    _CcaAcclDecryptPkts_Type()
)
ccaAcclDecryptPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclDecryptPkts.setStatus("current")
_CcaAcclDecryptOctets_Type = Counter64
_CcaAcclDecryptOctets_Object = MibTableColumn
ccaAcclDecryptOctets = _CcaAcclDecryptOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 20),
    _CcaAcclDecryptOctets_Type()
)
ccaAcclDecryptOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclDecryptOctets.setStatus("current")
_CcaAcclTransformsTotal_Type = Counter64
_CcaAcclTransformsTotal_Object = MibTableColumn
ccaAcclTransformsTotal = _CcaAcclTransformsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 21),
    _CcaAcclTransformsTotal_Type()
)
ccaAcclTransformsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclTransformsTotal.setStatus("current")
_CcaAcclDropsPkts_Type = Counter64
_CcaAcclDropsPkts_Object = MibTableColumn
ccaAcclDropsPkts = _CcaAcclDropsPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 22),
    _CcaAcclDropsPkts_Type()
)
ccaAcclDropsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclDropsPkts.setStatus("current")
_CcaAcclRandRequests_Type = Counter64
_CcaAcclRandRequests_Object = MibTableColumn
ccaAcclRandRequests = _CcaAcclRandRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 23),
    _CcaAcclRandRequests_Type()
)
ccaAcclRandRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclRandRequests.setStatus("current")
_CcaAcclRandReqFails_Type = Counter64
_CcaAcclRandReqFails_Object = MibTableColumn
ccaAcclRandReqFails = _CcaAcclRandReqFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 24),
    _CcaAcclRandReqFails_Type()
)
ccaAcclRandReqFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclRandReqFails.setStatus("current")
_CcaAcclDHKeysGenerated_Type = Counter64
_CcaAcclDHKeysGenerated_Object = MibTableColumn
ccaAcclDHKeysGenerated = _CcaAcclDHKeysGenerated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 25),
    _CcaAcclDHKeysGenerated_Type()
)
ccaAcclDHKeysGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclDHKeysGenerated.setStatus("current")
_CcaAcclDHDerivedSecretKeys_Type = Counter64
_CcaAcclDHDerivedSecretKeys_Object = MibTableColumn
ccaAcclDHDerivedSecretKeys = _CcaAcclDHDerivedSecretKeys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 26),
    _CcaAcclDHDerivedSecretKeys_Type()
)
ccaAcclDHDerivedSecretKeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclDHDerivedSecretKeys.setStatus("current")
_CcaAcclRSAKeysGenerated_Type = Counter64
_CcaAcclRSAKeysGenerated_Object = MibTableColumn
ccaAcclRSAKeysGenerated = _CcaAcclRSAKeysGenerated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 27),
    _CcaAcclRSAKeysGenerated_Type()
)
ccaAcclRSAKeysGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclRSAKeysGenerated.setStatus("current")
_CcaAcclRSASignings_Type = Counter64
_CcaAcclRSASignings_Object = MibTableColumn
ccaAcclRSASignings = _CcaAcclRSASignings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 28),
    _CcaAcclRSASignings_Type()
)
ccaAcclRSASignings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclRSASignings.setStatus("current")
_CcaAcclRSAVerifications_Type = Counter64
_CcaAcclRSAVerifications_Object = MibTableColumn
ccaAcclRSAVerifications = _CcaAcclRSAVerifications_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 29),
    _CcaAcclRSAVerifications_Type()
)
ccaAcclRSAVerifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclRSAVerifications.setStatus("current")
_CcaAcclRSAEncryptPkts_Type = Counter64
_CcaAcclRSAEncryptPkts_Object = MibTableColumn
ccaAcclRSAEncryptPkts = _CcaAcclRSAEncryptPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 30),
    _CcaAcclRSAEncryptPkts_Type()
)
ccaAcclRSAEncryptPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclRSAEncryptPkts.setStatus("current")
_CcaAcclRSAEncryptOctets_Type = Counter64
_CcaAcclRSAEncryptOctets_Object = MibTableColumn
ccaAcclRSAEncryptOctets = _CcaAcclRSAEncryptOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 31),
    _CcaAcclRSAEncryptOctets_Type()
)
ccaAcclRSAEncryptOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclRSAEncryptOctets.setStatus("current")
_CcaAcclRSADecryptPkts_Type = Counter64
_CcaAcclRSADecryptPkts_Object = MibTableColumn
ccaAcclRSADecryptPkts = _CcaAcclRSADecryptPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 32),
    _CcaAcclRSADecryptPkts_Type()
)
ccaAcclRSADecryptPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclRSADecryptPkts.setStatus("current")
_CcaAcclRSADecryptOctets_Type = Counter64
_CcaAcclRSADecryptOctets_Object = MibTableColumn
ccaAcclRSADecryptOctets = _CcaAcclRSADecryptOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 33),
    _CcaAcclRSADecryptOctets_Type()
)
ccaAcclRSADecryptOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclRSADecryptOctets.setStatus("current")
_CcaAcclDSAKeysGenerated_Type = Counter64
_CcaAcclDSAKeysGenerated_Object = MibTableColumn
ccaAcclDSAKeysGenerated = _CcaAcclDSAKeysGenerated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 34),
    _CcaAcclDSAKeysGenerated_Type()
)
ccaAcclDSAKeysGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclDSAKeysGenerated.setStatus("current")
_CcaAcclDSASignings_Type = Counter64
_CcaAcclDSASignings_Object = MibTableColumn
ccaAcclDSASignings = _CcaAcclDSASignings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 35),
    _CcaAcclDSASignings_Type()
)
ccaAcclDSASignings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclDSASignings.setStatus("current")
_CcaAcclDSAVerifications_Type = Counter64
_CcaAcclDSAVerifications_Object = MibTableColumn
ccaAcclDSAVerifications = _CcaAcclDSAVerifications_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 36),
    _CcaAcclDSAVerifications_Type()
)
ccaAcclDSAVerifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclDSAVerifications.setStatus("current")
_CcaAcclOutboundSSLRecords_Type = Counter64
_CcaAcclOutboundSSLRecords_Object = MibTableColumn
ccaAcclOutboundSSLRecords = _CcaAcclOutboundSSLRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 37),
    _CcaAcclOutboundSSLRecords_Type()
)
ccaAcclOutboundSSLRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclOutboundSSLRecords.setStatus("current")
_CcaAcclInboundSSLRecords_Type = Counter64
_CcaAcclInboundSSLRecords_Object = MibTableColumn
ccaAcclInboundSSLRecords = _CcaAcclInboundSSLRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 2, 1, 38),
    _CcaAcclInboundSSLRecords_Type()
)
ccaAcclInboundSSLRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaAcclInboundSSLRecords.setStatus("current")
_CcaProtocolActivity_ObjectIdentity = ObjectIdentity
ccaProtocolActivity = _CcaProtocolActivity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 3)
)
_CcaProtocolStatsTable_Object = MibTable
ccaProtocolStatsTable = _CcaProtocolStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ccaProtocolStatsTable.setStatus("current")
_CcaProtocolStatsEntry_Object = MibTableRow
ccaProtocolStatsEntry = _CcaProtocolStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 3, 1, 1)
)
ccaProtocolStatsEntry.setIndexNames(
    (0, "CISCO-CRYPTO-ACCELERATOR-MIB", "ccaProtId"),
)
if mibBuilder.loadTexts:
    ccaProtocolStatsEntry.setStatus("current")
_CcaProtId_Type = CAProtocolType
_CcaProtId_Object = MibTableColumn
ccaProtId = _CcaProtId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 3, 1, 1, 1),
    _CcaProtId_Type()
)
ccaProtId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccaProtId.setStatus("current")
_CcaProtPktEncryptsReqs_Type = Counter64
_CcaProtPktEncryptsReqs_Object = MibTableColumn
ccaProtPktEncryptsReqs = _CcaProtPktEncryptsReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 3, 1, 1, 2),
    _CcaProtPktEncryptsReqs_Type()
)
ccaProtPktEncryptsReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaProtPktEncryptsReqs.setStatus("current")
_CcaProtPktDecryptsReqs_Type = Counter64
_CcaProtPktDecryptsReqs_Object = MibTableColumn
ccaProtPktDecryptsReqs = _CcaProtPktDecryptsReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 3, 1, 1, 3),
    _CcaProtPktDecryptsReqs_Type()
)
ccaProtPktDecryptsReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaProtPktDecryptsReqs.setStatus("current")
_CcaProtHmacCalcReqs_Type = Counter64
_CcaProtHmacCalcReqs_Object = MibTableColumn
ccaProtHmacCalcReqs = _CcaProtHmacCalcReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 3, 1, 1, 4),
    _CcaProtHmacCalcReqs_Type()
)
ccaProtHmacCalcReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaProtHmacCalcReqs.setStatus("current")
_CcaProtSaCreateReqs_Type = Counter64
_CcaProtSaCreateReqs_Object = MibTableColumn
ccaProtSaCreateReqs = _CcaProtSaCreateReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 3, 1, 1, 5),
    _CcaProtSaCreateReqs_Type()
)
ccaProtSaCreateReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaProtSaCreateReqs.setStatus("current")
_CcaProtSaRekeyReqs_Type = Counter64
_CcaProtSaRekeyReqs_Object = MibTableColumn
ccaProtSaRekeyReqs = _CcaProtSaRekeyReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 3, 1, 1, 6),
    _CcaProtSaRekeyReqs_Type()
)
ccaProtSaRekeyReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaProtSaRekeyReqs.setStatus("current")
_CcaProtSaDeleteReqs_Type = Counter64
_CcaProtSaDeleteReqs_Object = MibTableColumn
ccaProtSaDeleteReqs = _CcaProtSaDeleteReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 3, 1, 1, 7),
    _CcaProtSaDeleteReqs_Type()
)
ccaProtSaDeleteReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaProtSaDeleteReqs.setStatus("current")
_CcaProtPktEncapReqs_Type = Counter64
_CcaProtPktEncapReqs_Object = MibTableColumn
ccaProtPktEncapReqs = _CcaProtPktEncapReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 3, 1, 1, 8),
    _CcaProtPktEncapReqs_Type()
)
ccaProtPktEncapReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaProtPktEncapReqs.setStatus("current")
_CcaProtPktDecapReqs_Type = Counter64
_CcaProtPktDecapReqs_Object = MibTableColumn
ccaProtPktDecapReqs = _CcaProtPktDecapReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 3, 1, 1, 9),
    _CcaProtPktDecapReqs_Type()
)
ccaProtPktDecapReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaProtPktDecapReqs.setStatus("current")
_CcaProtNextPhaseKeyAllocReqs_Type = Counter64
_CcaProtNextPhaseKeyAllocReqs_Object = MibTableColumn
ccaProtNextPhaseKeyAllocReqs = _CcaProtNextPhaseKeyAllocReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 3, 1, 1, 10),
    _CcaProtNextPhaseKeyAllocReqs_Type()
)
ccaProtNextPhaseKeyAllocReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaProtNextPhaseKeyAllocReqs.setStatus("current")
_CcaProtRndGenReqs_Type = Counter64
_CcaProtRndGenReqs_Object = MibTableColumn
ccaProtRndGenReqs = _CcaProtRndGenReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 3, 1, 1, 11),
    _CcaProtRndGenReqs_Type()
)
ccaProtRndGenReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaProtRndGenReqs.setStatus("current")
_CcaProtFailedReqs_Type = Counter64
_CcaProtFailedReqs_Object = MibTableColumn
ccaProtFailedReqs = _CcaProtFailedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 2, 3, 1, 1, 12),
    _CcaProtFailedReqs_Type()
)
ccaProtFailedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccaProtFailedReqs.setStatus("current")
_CcaAcNotifCntl_ObjectIdentity = ObjectIdentity
ccaAcNotifCntl = _CcaAcNotifCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 3)
)
_CcaNotifCntlAcclInserted_Type = TruthValue
_CcaNotifCntlAcclInserted_Object = MibScalar
ccaNotifCntlAcclInserted = _CcaNotifCntlAcclInserted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 3, 1),
    _CcaNotifCntlAcclInserted_Type()
)
ccaNotifCntlAcclInserted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccaNotifCntlAcclInserted.setStatus("current")
_CcaNotifCntlAcclRemoved_Type = TruthValue
_CcaNotifCntlAcclRemoved_Object = MibScalar
ccaNotifCntlAcclRemoved = _CcaNotifCntlAcclRemoved_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 3, 2),
    _CcaNotifCntlAcclRemoved_Type()
)
ccaNotifCntlAcclRemoved.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccaNotifCntlAcclRemoved.setStatus("current")
_CcaNotifCntlAcclOperational_Type = TruthValue
_CcaNotifCntlAcclOperational_Object = MibScalar
ccaNotifCntlAcclOperational = _CcaNotifCntlAcclOperational_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 3, 3),
    _CcaNotifCntlAcclOperational_Type()
)
ccaNotifCntlAcclOperational.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccaNotifCntlAcclOperational.setStatus("current")


class _CcaNotifCntlAcclDisabled_Type(TruthValue):
    """Custom type ccaNotifCntlAcclDisabled based on TruthValue"""


_CcaNotifCntlAcclDisabled_Object = MibScalar
ccaNotifCntlAcclDisabled = _CcaNotifCntlAcclDisabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 1, 3, 4),
    _CcaNotifCntlAcclDisabled_Type()
)
ccaNotifCntlAcclDisabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccaNotifCntlAcclDisabled.setStatus("current")
_CiscoCryAccleratorMIBConform_ObjectIdentity = ObjectIdentity
ciscoCryAccleratorMIBConform = _CiscoCryAccleratorMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 2)
)
_CiscoCryAccelMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCryAccelMIBCompliances = _CiscoCryAccelMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 2, 1)
)
_CiscoCryAccelMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCryAccelMIBGroups = _CiscoCryAccelMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 2, 2)
)

# Managed Objects groups

ciscoCryAccCapacityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 2, 2, 1)
)
ciscoCryAccCapacityGroup.setObjects(
      *(("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaSupportsHwCrypto"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaSupportsModularHwCrypto"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaMaxAccelerators"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaMaxCryptoThroughput"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaMaxCryptoConnections"))
)
if mibBuilder.loadTexts:
    ciscoCryAccCapacityGroup.setStatus("current")

ciscoCryAccSummaryActivityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 2, 2, 2)
)
ciscoCryAccSummaryActivityGroup.setObjects(
      *(("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaGlobalNumActiveAccelerators"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaGlobalNumNonOperAccelerators"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaGlobalInOctets"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaGlobalOutOctets"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaGlobalInPkts"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaGlobalOutPkts"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaGlobalOutErrPkts"))
)
if mibBuilder.loadTexts:
    ciscoCryAccSummaryActivityGroup.setStatus("current")

ciscoCryAccModuleActivityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 2, 2, 3)
)
ciscoCryAccModuleActivityGroup.setObjects(
      *(("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclEntPhysicalIndex"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclStatus"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclType"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclVersion"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclSlot"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclActiveTime"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclInPkts"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclOutPkts"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclOutBadPkts"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclInOctets"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclOutOctets"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclHashOutboundPkts"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclHashOutboundOctets"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclHashInboundPkts"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclHashInboundOctets"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclEncryptPkts"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclEncryptOctets"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclDecryptPkts"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclDecryptOctets"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclTransformsTotal"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclDropsPkts"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclRandRequests"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclRandReqFails"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclDHKeysGenerated"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclDHDerivedSecretKeys"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclRSAKeysGenerated"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclRSASignings"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclRSAVerifications"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclRSAEncryptPkts"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclRSAEncryptOctets"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclRSADecryptPkts"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclRSADecryptOctets"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclDSAKeysGenerated"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclDSASignings"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclDSAVerifications"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclOutboundSSLRecords"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclInboundSSLRecords"))
)
if mibBuilder.loadTexts:
    ciscoCryAccModuleActivityGroup.setStatus("current")

ciscoCryAccProtocolActivityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 2, 2, 4)
)
ciscoCryAccProtocolActivityGroup.setObjects(
      *(("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaProtPktEncryptsReqs"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaProtPktDecryptsReqs"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaProtHmacCalcReqs"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaProtSaCreateReqs"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaProtSaRekeyReqs"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaProtSaDeleteReqs"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaProtPktEncapReqs"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaProtPktDecapReqs"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaProtNextPhaseKeyAllocReqs"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaProtRndGenReqs"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaProtFailedReqs"))
)
if mibBuilder.loadTexts:
    ciscoCryAccProtocolActivityGroup.setStatus("current")

ciscoCryAccNotifsCntlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 2, 2, 5)
)
ciscoCryAccNotifsCntlGroup.setObjects(
      *(("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaNotifCntlAcclInserted"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaNotifCntlAcclRemoved"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaNotifCntlAcclOperational"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaNotifCntlAcclDisabled"))
)
if mibBuilder.loadTexts:
    ciscoCryAccNotifsCntlGroup.setStatus("current")


# Notification objects

ciscoCryAccelInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 0, 1)
)
ciscoCryAccelInserted.setObjects(
    ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclSlot")
)
if mibBuilder.loadTexts:
    ciscoCryAccelInserted.setStatus(
        "current"
    )

ciscoCryAccelRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 0, 2)
)
ciscoCryAccelRemoved.setObjects(
    ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclSlot")
)
if mibBuilder.loadTexts:
    ciscoCryAccelRemoved.setStatus(
        "current"
    )

ciscoCryAccelOperational = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 0, 3)
)
ciscoCryAccelOperational.setObjects(
    ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclSlot")
)
if mibBuilder.loadTexts:
    ciscoCryAccelOperational.setStatus(
        "current"
    )

ciscoCryAccelDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 0, 4)
)
ciscoCryAccelDisabled.setObjects(
      *(("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclSlot"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclStatus"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ccaAcclActiveTime"))
)
if mibBuilder.loadTexts:
    ciscoCryAccelDisabled.setStatus(
        "current"
    )


# Notifications groups

ciscoCryAccNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 2, 2, 6)
)
ciscoCryAccNotifsGroup.setObjects(
      *(("CISCO-CRYPTO-ACCELERATOR-MIB", "ciscoCryAccelInserted"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ciscoCryAccelRemoved"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ciscoCryAccelOperational"),
        ("CISCO-CRYPTO-ACCELERATOR-MIB", "ciscoCryAccelDisabled"))
)
if mibBuilder.loadTexts:
    ciscoCryAccNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoCryAccelMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 467, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCryAccelMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CRYPTO-ACCELERATOR-MIB",
    **{"CAModuleType": CAModuleType,
       "CAModuleCount": CAModuleCount,
       "CAProtocolType": CAProtocolType,
       "ciscoCryptoAcceleratorMIB": ciscoCryptoAcceleratorMIB,
       "ciscoCryAcceleratorMIBNotifs": ciscoCryAcceleratorMIBNotifs,
       "ciscoCryAccelInserted": ciscoCryAccelInserted,
       "ciscoCryAccelRemoved": ciscoCryAccelRemoved,
       "ciscoCryAccelOperational": ciscoCryAccelOperational,
       "ciscoCryAccelDisabled": ciscoCryAccelDisabled,
       "ciscoCryAcceleratorMIBObjects": ciscoCryAcceleratorMIBObjects,
       "ccaCapability": ccaCapability,
       "ccaSupportsHwCrypto": ccaSupportsHwCrypto,
       "ccaSupportsModularHwCrypto": ccaSupportsModularHwCrypto,
       "ccaMaxAccelerators": ccaMaxAccelerators,
       "ccaMaxCryptoThroughput": ccaMaxCryptoThroughput,
       "ccaMaxCryptoConnections": ccaMaxCryptoConnections,
       "ccaActivity": ccaActivity,
       "ccaGlobalStats": ccaGlobalStats,
       "ccaGlobalNumActiveAccelerators": ccaGlobalNumActiveAccelerators,
       "ccaGlobalNumNonOperAccelerators": ccaGlobalNumNonOperAccelerators,
       "ccaGlobalInOctets": ccaGlobalInOctets,
       "ccaGlobalOutOctets": ccaGlobalOutOctets,
       "ccaGlobalInPkts": ccaGlobalInPkts,
       "ccaGlobalOutPkts": ccaGlobalOutPkts,
       "ccaGlobalOutErrPkts": ccaGlobalOutErrPkts,
       "ccaAcceleratorTable": ccaAcceleratorTable,
       "ccaAcceleratorEntry": ccaAcceleratorEntry,
       "ccaAcclIndex": ccaAcclIndex,
       "ccaAcclEntPhysicalIndex": ccaAcclEntPhysicalIndex,
       "ccaAcclStatus": ccaAcclStatus,
       "ccaAcclType": ccaAcclType,
       "ccaAcclVersion": ccaAcclVersion,
       "ccaAcclSlot": ccaAcclSlot,
       "ccaAcclActiveTime": ccaAcclActiveTime,
       "ccaAcclInPkts": ccaAcclInPkts,
       "ccaAcclOutPkts": ccaAcclOutPkts,
       "ccaAcclOutBadPkts": ccaAcclOutBadPkts,
       "ccaAcclInOctets": ccaAcclInOctets,
       "ccaAcclOutOctets": ccaAcclOutOctets,
       "ccaAcclHashOutboundPkts": ccaAcclHashOutboundPkts,
       "ccaAcclHashOutboundOctets": ccaAcclHashOutboundOctets,
       "ccaAcclHashInboundPkts": ccaAcclHashInboundPkts,
       "ccaAcclHashInboundOctets": ccaAcclHashInboundOctets,
       "ccaAcclEncryptPkts": ccaAcclEncryptPkts,
       "ccaAcclEncryptOctets": ccaAcclEncryptOctets,
       "ccaAcclDecryptPkts": ccaAcclDecryptPkts,
       "ccaAcclDecryptOctets": ccaAcclDecryptOctets,
       "ccaAcclTransformsTotal": ccaAcclTransformsTotal,
       "ccaAcclDropsPkts": ccaAcclDropsPkts,
       "ccaAcclRandRequests": ccaAcclRandRequests,
       "ccaAcclRandReqFails": ccaAcclRandReqFails,
       "ccaAcclDHKeysGenerated": ccaAcclDHKeysGenerated,
       "ccaAcclDHDerivedSecretKeys": ccaAcclDHDerivedSecretKeys,
       "ccaAcclRSAKeysGenerated": ccaAcclRSAKeysGenerated,
       "ccaAcclRSASignings": ccaAcclRSASignings,
       "ccaAcclRSAVerifications": ccaAcclRSAVerifications,
       "ccaAcclRSAEncryptPkts": ccaAcclRSAEncryptPkts,
       "ccaAcclRSAEncryptOctets": ccaAcclRSAEncryptOctets,
       "ccaAcclRSADecryptPkts": ccaAcclRSADecryptPkts,
       "ccaAcclRSADecryptOctets": ccaAcclRSADecryptOctets,
       "ccaAcclDSAKeysGenerated": ccaAcclDSAKeysGenerated,
       "ccaAcclDSASignings": ccaAcclDSASignings,
       "ccaAcclDSAVerifications": ccaAcclDSAVerifications,
       "ccaAcclOutboundSSLRecords": ccaAcclOutboundSSLRecords,
       "ccaAcclInboundSSLRecords": ccaAcclInboundSSLRecords,
       "ccaProtocolActivity": ccaProtocolActivity,
       "ccaProtocolStatsTable": ccaProtocolStatsTable,
       "ccaProtocolStatsEntry": ccaProtocolStatsEntry,
       "ccaProtId": ccaProtId,
       "ccaProtPktEncryptsReqs": ccaProtPktEncryptsReqs,
       "ccaProtPktDecryptsReqs": ccaProtPktDecryptsReqs,
       "ccaProtHmacCalcReqs": ccaProtHmacCalcReqs,
       "ccaProtSaCreateReqs": ccaProtSaCreateReqs,
       "ccaProtSaRekeyReqs": ccaProtSaRekeyReqs,
       "ccaProtSaDeleteReqs": ccaProtSaDeleteReqs,
       "ccaProtPktEncapReqs": ccaProtPktEncapReqs,
       "ccaProtPktDecapReqs": ccaProtPktDecapReqs,
       "ccaProtNextPhaseKeyAllocReqs": ccaProtNextPhaseKeyAllocReqs,
       "ccaProtRndGenReqs": ccaProtRndGenReqs,
       "ccaProtFailedReqs": ccaProtFailedReqs,
       "ccaAcNotifCntl": ccaAcNotifCntl,
       "ccaNotifCntlAcclInserted": ccaNotifCntlAcclInserted,
       "ccaNotifCntlAcclRemoved": ccaNotifCntlAcclRemoved,
       "ccaNotifCntlAcclOperational": ccaNotifCntlAcclOperational,
       "ccaNotifCntlAcclDisabled": ccaNotifCntlAcclDisabled,
       "ciscoCryAccleratorMIBConform": ciscoCryAccleratorMIBConform,
       "ciscoCryAccelMIBCompliances": ciscoCryAccelMIBCompliances,
       "ciscoCryAccelMIBCompliance": ciscoCryAccelMIBCompliance,
       "ciscoCryAccelMIBGroups": ciscoCryAccelMIBGroups,
       "ciscoCryAccCapacityGroup": ciscoCryAccCapacityGroup,
       "ciscoCryAccSummaryActivityGroup": ciscoCryAccSummaryActivityGroup,
       "ciscoCryAccModuleActivityGroup": ciscoCryAccModuleActivityGroup,
       "ciscoCryAccProtocolActivityGroup": ciscoCryAccProtocolActivityGroup,
       "ciscoCryAccNotifsCntlGroup": ciscoCryAccNotifsCntlGroup,
       "ciscoCryAccNotifsGroup": ciscoCryAccNotifsGroup}
)
