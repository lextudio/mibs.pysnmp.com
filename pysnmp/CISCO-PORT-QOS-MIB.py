# SNMP MIB module (CISCO-PORT-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-PORT-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:55 2024
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

(Dscp,
 QosLayer2Cos) = mibBuilder.importSymbols(
    "CISCO-QOS-PIB-MIB",
    "Dscp",
    "QosLayer2Cos")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(vtpVlanIndex,) = mibBuilder.importSymbols(
    "CISCO-VTP-MIB",
    "vtpVlanIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoPortQosMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 189)
)
ciscoPortQosMIB.setRevisions(
        ("2015-09-25 00:00",
         "2008-09-10 00:00",
         "2008-03-05 00:00",
         "2008-01-09 00:00",
         "2006-02-17 00:00",
         "2005-02-23 00:00",
         "2004-05-20 00:00",
         "2004-01-30 00:00",
         "2002-03-20 00:00",
         "2001-05-15 00:00",
         "2000-12-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoPortQosMIBObjects_ObjectIdentity = ObjectIdentity
ciscoPortQosMIBObjects = _CiscoPortQosMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1)
)
_CportQosRLConfig_ObjectIdentity = ObjectIdentity
cportQosRLConfig = _CportQosRLConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 1)
)
_CportQosRLConfigTable_Object = MibTable
cportQosRLConfigTable = _CportQosRLConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cportQosRLConfigTable.setStatus("deprecated")
_CportQosRLConfigEntry_Object = MibTableRow
cportQosRLConfigEntry = _CportQosRLConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 1, 1, 1)
)
cportQosRLConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-PORT-QOS-MIB", "cportQosRLConfigDirection"),
)
if mibBuilder.loadTexts:
    cportQosRLConfigEntry.setStatus("deprecated")


class _CportQosRLConfigDirection_Type(Integer32):
    """Custom type cportQosRLConfigDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_CportQosRLConfigDirection_Type.__name__ = "Integer32"
_CportQosRLConfigDirection_Object = MibTableColumn
cportQosRLConfigDirection = _CportQosRLConfigDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 1, 1, 1, 1),
    _CportQosRLConfigDirection_Type()
)
cportQosRLConfigDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cportQosRLConfigDirection.setStatus("deprecated")
_CportQosRLConfigEnable_Type = TruthValue
_CportQosRLConfigEnable_Object = MibTableColumn
cportQosRLConfigEnable = _CportQosRLConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 1, 1, 1, 2),
    _CportQosRLConfigEnable_Type()
)
cportQosRLConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cportQosRLConfigEnable.setStatus("deprecated")


class _CportQosRLConfigRate_Type(Integer32):
    """Custom type cportQosRLConfigRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32000, 2147483647),
    )


_CportQosRLConfigRate_Type.__name__ = "Integer32"
_CportQosRLConfigRate_Object = MibTableColumn
cportQosRLConfigRate = _CportQosRLConfigRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 1, 1, 1, 3),
    _CportQosRLConfigRate_Type()
)
cportQosRLConfigRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cportQosRLConfigRate.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosRLConfigRate.setUnits("bits per second")


class _CportQosRLConfigBurstSize_Type(Integer32):
    """Custom type cportQosRLConfigBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000),
    )


_CportQosRLConfigBurstSize_Type.__name__ = "Integer32"
_CportQosRLConfigBurstSize_Object = MibTableColumn
cportQosRLConfigBurstSize = _CportQosRLConfigBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 1, 1, 1, 4),
    _CportQosRLConfigBurstSize_Type()
)
cportQosRLConfigBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cportQosRLConfigBurstSize.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosRLConfigBurstSize.setUnits("bytes")
_CportQosTSConfig_ObjectIdentity = ObjectIdentity
cportQosTSConfig = _CportQosTSConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 2)
)
_CportQosTSConfigTable_Object = MibTable
cportQosTSConfigTable = _CportQosTSConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cportQosTSConfigTable.setStatus("deprecated")
_CportQosTSConfigEntry_Object = MibTableRow
cportQosTSConfigEntry = _CportQosTSConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 2, 1, 1)
)
cportQosTSConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cportQosTSConfigEntry.setStatus("deprecated")
_CportQosTSConfigEnable_Type = TruthValue
_CportQosTSConfigEnable_Object = MibTableColumn
cportQosTSConfigEnable = _CportQosTSConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 2, 1, 1, 1),
    _CportQosTSConfigEnable_Type()
)
cportQosTSConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cportQosTSConfigEnable.setStatus("deprecated")


class _CportQosTSConfigRate_Type(Integer32):
    """Custom type cportQosTSConfigRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32000, 2147483647),
    )


_CportQosTSConfigRate_Type.__name__ = "Integer32"
_CportQosTSConfigRate_Object = MibTableColumn
cportQosTSConfigRate = _CportQosTSConfigRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 2, 1, 1, 2),
    _CportQosTSConfigRate_Type()
)
cportQosTSConfigRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cportQosTSConfigRate.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosTSConfigRate.setUnits("bits per second")


class _CportQosTSConfigBurstSize_Type(Integer32):
    """Custom type cportQosTSConfigBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512000),
    )


_CportQosTSConfigBurstSize_Type.__name__ = "Integer32"
_CportQosTSConfigBurstSize_Object = MibTableColumn
cportQosTSConfigBurstSize = _CportQosTSConfigBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 2, 1, 1, 3),
    _CportQosTSConfigBurstSize_Type()
)
cportQosTSConfigBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cportQosTSConfigBurstSize.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosTSConfigBurstSize.setUnits("bits")
_CportQosStatistics_ObjectIdentity = ObjectIdentity
cportQosStatistics = _CportQosStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3)
)


class _CportQosIndexType_Type(Integer32):
    """Custom type cportQosIndexType based on Integer32"""
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
        *(("cos", 4),
          ("dscp", 2),
          ("ipPrecedence", 3),
          ("none", 1))
    )


_CportQosIndexType_Type.__name__ = "Integer32"
_CportQosIndexType_Object = MibScalar
cportQosIndexType = _CportQosIndexType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 1),
    _CportQosIndexType_Type()
)
cportQosIndexType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosIndexType.setStatus("deprecated")
_CportQosStatsTable_Object = MibTable
cportQosStatsTable = _CportQosStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cportQosStatsTable.setStatus("deprecated")
_CportQosStatsEntry_Object = MibTableRow
cportQosStatsEntry = _CportQosStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 2, 1)
)
cportQosStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-PORT-QOS-MIB", "cportQosDirection"),
    (0, "CISCO-PORT-QOS-MIB", "cportQosIndex"),
)
if mibBuilder.loadTexts:
    cportQosStatsEntry.setStatus("deprecated")


class _CportQosDirection_Type(Integer32):
    """Custom type cportQosDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("egress", 2),
          ("ingress", 1))
    )


_CportQosDirection_Type.__name__ = "Integer32"
_CportQosDirection_Object = MibTableColumn
cportQosDirection = _CportQosDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 2, 1, 1),
    _CportQosDirection_Type()
)
cportQosDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cportQosDirection.setStatus("deprecated")
_CportQosIndex_Type = Unsigned32
_CportQosIndex_Object = MibTableColumn
cportQosIndex = _CportQosIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 2, 1, 2),
    _CportQosIndex_Type()
)
cportQosIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cportQosIndex.setStatus("deprecated")
_CportQosPrePolicyPkts_Type = Counter64
_CportQosPrePolicyPkts_Object = MibTableColumn
cportQosPrePolicyPkts = _CportQosPrePolicyPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 2, 1, 3),
    _CportQosPrePolicyPkts_Type()
)
cportQosPrePolicyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosPrePolicyPkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosPrePolicyPkts.setUnits("packets")
_CportQosPrePolicyOctets_Type = Counter64
_CportQosPrePolicyOctets_Object = MibTableColumn
cportQosPrePolicyOctets = _CportQosPrePolicyOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 2, 1, 4),
    _CportQosPrePolicyOctets_Type()
)
cportQosPrePolicyOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosPrePolicyOctets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosPrePolicyOctets.setUnits("octets")
_CportQosPostPolicyPkts_Type = Counter64
_CportQosPostPolicyPkts_Object = MibTableColumn
cportQosPostPolicyPkts = _CportQosPostPolicyPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 2, 1, 5),
    _CportQosPostPolicyPkts_Type()
)
cportQosPostPolicyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosPostPolicyPkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosPostPolicyPkts.setUnits("packets")
_CportQosPostPolicyOctets_Type = Counter64
_CportQosPostPolicyOctets_Object = MibTableColumn
cportQosPostPolicyOctets = _CportQosPostPolicyOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 2, 1, 6),
    _CportQosPostPolicyOctets_Type()
)
cportQosPostPolicyOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosPostPolicyOctets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosPostPolicyOctets.setUnits("octets")
_CportQosDropPkts_Type = Counter64
_CportQosDropPkts_Object = MibTableColumn
cportQosDropPkts = _CportQosDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 2, 1, 7),
    _CportQosDropPkts_Type()
)
cportQosDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosDropPkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosDropPkts.setUnits("packets")
_CportQosDropOctets_Type = Counter64
_CportQosDropOctets_Object = MibTableColumn
cportQosDropOctets = _CportQosDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 2, 1, 8),
    _CportQosDropOctets_Type()
)
cportQosDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosDropOctets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosDropOctets.setUnits("octets")
_CportQosClassifiedOctets_Type = Counter64
_CportQosClassifiedOctets_Object = MibTableColumn
cportQosClassifiedOctets = _CportQosClassifiedOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 2, 1, 9),
    _CportQosClassifiedOctets_Type()
)
cportQosClassifiedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosClassifiedOctets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosClassifiedOctets.setUnits("octets")
_CportQosClassifiedPkts_Type = Counter64
_CportQosClassifiedPkts_Object = MibTableColumn
cportQosClassifiedPkts = _CportQosClassifiedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 2, 1, 10),
    _CportQosClassifiedPkts_Type()
)
cportQosClassifiedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosClassifiedPkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosClassifiedPkts.setUnits("packets")
_CportQosNoChangePkts_Type = Counter64
_CportQosNoChangePkts_Object = MibTableColumn
cportQosNoChangePkts = _CportQosNoChangePkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 2, 1, 11),
    _CportQosNoChangePkts_Type()
)
cportQosNoChangePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosNoChangePkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosNoChangePkts.setUnits("packets")
_CportQosNoChangeOctets_Type = Counter64
_CportQosNoChangeOctets_Object = MibTableColumn
cportQosNoChangeOctets = _CportQosNoChangeOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 2, 1, 12),
    _CportQosNoChangeOctets_Type()
)
cportQosNoChangeOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosNoChangeOctets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosNoChangeOctets.setUnits("octets")
_CportQosInProfPolicyPkts_Type = Counter64
_CportQosInProfPolicyPkts_Object = MibTableColumn
cportQosInProfPolicyPkts = _CportQosInProfPolicyPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 2, 1, 13),
    _CportQosInProfPolicyPkts_Type()
)
cportQosInProfPolicyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosInProfPolicyPkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosInProfPolicyPkts.setUnits("packets")
_CportQosOutOfProfPolicyPkts_Type = Counter64
_CportQosOutOfProfPolicyPkts_Object = MibTableColumn
cportQosOutOfProfPolicyPkts = _CportQosOutOfProfPolicyPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 2, 1, 14),
    _CportQosOutOfProfPolicyPkts_Type()
)
cportQosOutOfProfPolicyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosOutOfProfPolicyPkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosOutOfProfPolicyPkts.setUnits("packets")
_CportQosInProfPolicyOctets_Type = Counter64
_CportQosInProfPolicyOctets_Object = MibTableColumn
cportQosInProfPolicyOctets = _CportQosInProfPolicyOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 2, 1, 15),
    _CportQosInProfPolicyOctets_Type()
)
cportQosInProfPolicyOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosInProfPolicyOctets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosInProfPolicyOctets.setUnits("octets")
_CportQosOutOfProfPolicyOctets_Type = Counter64
_CportQosOutOfProfPolicyOctets_Object = MibTableColumn
cportQosOutOfProfPolicyOctets = _CportQosOutOfProfPolicyOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 2, 1, 16),
    _CportQosOutOfProfPolicyOctets_Type()
)
cportQosOutOfProfPolicyOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosOutOfProfPolicyOctets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosOutOfProfPolicyOctets.setUnits("octets")
_CportQosViolateProfPolicyPkts_Type = Counter64
_CportQosViolateProfPolicyPkts_Object = MibTableColumn
cportQosViolateProfPolicyPkts = _CportQosViolateProfPolicyPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 2, 1, 17),
    _CportQosViolateProfPolicyPkts_Type()
)
cportQosViolateProfPolicyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosViolateProfPolicyPkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosViolateProfPolicyPkts.setUnits("packets")
_CportQosViolateProfPolicyOctets_Type = Counter64
_CportQosViolateProfPolicyOctets_Object = MibTableColumn
cportQosViolateProfPolicyOctets = _CportQosViolateProfPolicyOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 2, 1, 18),
    _CportQosViolateProfPolicyOctets_Type()
)
cportQosViolateProfPolicyOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosViolateProfPolicyOctets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosViolateProfPolicyOctets.setUnits("octets")


class _CportQosIndexTypeNew_Type(Integer32):
    """Custom type cportQosIndexTypeNew based on Integer32"""
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
        *(("cos", 4),
          ("dscp", 2),
          ("ipPrecedence", 3),
          ("none", 1),
          ("police", 5))
    )


_CportQosIndexTypeNew_Type.__name__ = "Integer32"
_CportQosIndexTypeNew_Object = MibScalar
cportQosIndexTypeNew = _CportQosIndexTypeNew_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 3),
    _CportQosIndexTypeNew_Type()
)
cportQosIndexTypeNew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cportQosIndexTypeNew.setStatus("deprecated")
_CportQosInVlanStatsTable_Object = MibTable
cportQosInVlanStatsTable = _CportQosInVlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 4)
)
if mibBuilder.loadTexts:
    cportQosInVlanStatsTable.setStatus("deprecated")
_CportQosInVlanStatsEntry_Object = MibTableRow
cportQosInVlanStatsEntry = _CportQosInVlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 4, 1)
)
cportQosInVlanStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-VTP-MIB", "vtpVlanIndex"),
    (0, "CISCO-PORT-QOS-MIB", "cportQosIndex"),
)
if mibBuilder.loadTexts:
    cportQosInVlanStatsEntry.setStatus("deprecated")
_CportQosVlanInProfPolicyPkts_Type = Counter64
_CportQosVlanInProfPolicyPkts_Object = MibTableColumn
cportQosVlanInProfPolicyPkts = _CportQosVlanInProfPolicyPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 4, 1, 1),
    _CportQosVlanInProfPolicyPkts_Type()
)
cportQosVlanInProfPolicyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosVlanInProfPolicyPkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosVlanInProfPolicyPkts.setUnits("packets")
_CportQosVlanOutOfProfPolicyPkts_Type = Counter64
_CportQosVlanOutOfProfPolicyPkts_Object = MibTableColumn
cportQosVlanOutOfProfPolicyPkts = _CportQosVlanOutOfProfPolicyPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 4, 1, 2),
    _CportQosVlanOutOfProfPolicyPkts_Type()
)
cportQosVlanOutOfProfPolicyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosVlanOutOfProfPolicyPkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosVlanOutOfProfPolicyPkts.setUnits("packets")
_CportQosVlanInProfPolicyOctets_Type = Counter64
_CportQosVlanInProfPolicyOctets_Object = MibTableColumn
cportQosVlanInProfPolicyOctets = _CportQosVlanInProfPolicyOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 4, 1, 3),
    _CportQosVlanInProfPolicyOctets_Type()
)
cportQosVlanInProfPolicyOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosVlanInProfPolicyOctets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosVlanInProfPolicyOctets.setUnits("octets")
_CportQosVlanOutOfProfPolicyOctets_Type = Counter64
_CportQosVlanOutOfProfPolicyOctets_Object = MibTableColumn
cportQosVlanOutOfProfPolicyOctets = _CportQosVlanOutOfProfPolicyOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 4, 1, 4),
    _CportQosVlanOutOfProfPolicyOctets_Type()
)
cportQosVlanOutOfProfPolicyOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosVlanOutOfProfPolicyOctets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosVlanOutOfProfPolicyOctets.setUnits("octets")
_CportQosVlanViolateProfPolicyPkts_Type = Counter64
_CportQosVlanViolateProfPolicyPkts_Object = MibTableColumn
cportQosVlanViolateProfPolicyPkts = _CportQosVlanViolateProfPolicyPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 4, 1, 5),
    _CportQosVlanViolateProfPolicyPkts_Type()
)
cportQosVlanViolateProfPolicyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosVlanViolateProfPolicyPkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosVlanViolateProfPolicyPkts.setUnits("packets")
_CportQosVlanViolateProfPolicyOctets_Type = Counter64
_CportQosVlanViolateProfPolicyOctets_Object = MibTableColumn
cportQosVlanViolateProfPolicyOctets = _CportQosVlanViolateProfPolicyOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 4, 1, 6),
    _CportQosVlanViolateProfPolicyOctets_Type()
)
cportQosVlanViolateProfPolicyOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosVlanViolateProfPolicyOctets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosVlanViolateProfPolicyOctets.setUnits("octets")
_CportQosEgressQueueStatsTable_Object = MibTable
cportQosEgressQueueStatsTable = _CportQosEgressQueueStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 5)
)
if mibBuilder.loadTexts:
    cportQosEgressQueueStatsTable.setStatus("deprecated")
_CportQosEgressQueueStatsEntry_Object = MibTableRow
cportQosEgressQueueStatsEntry = _CportQosEgressQueueStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 5, 1)
)
cportQosEgressQueueStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-PORT-QOS-MIB", "cportQosQueueId"),
    (0, "CISCO-PORT-QOS-MIB", "cportQosQueueThreshold"),
)
if mibBuilder.loadTexts:
    cportQosEgressQueueStatsEntry.setStatus("deprecated")


class _CportQosQueueId_Type(Unsigned32):
    """Custom type cportQosQueueId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CportQosQueueId_Type.__name__ = "Unsigned32"
_CportQosQueueId_Object = MibTableColumn
cportQosQueueId = _CportQosQueueId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 5, 1, 1),
    _CportQosQueueId_Type()
)
cportQosQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cportQosQueueId.setStatus("deprecated")


class _CportQosQueueThreshold_Type(Unsigned32):
    """Custom type cportQosQueueThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CportQosQueueThreshold_Type.__name__ = "Unsigned32"
_CportQosQueueThreshold_Object = MibTableColumn
cportQosQueueThreshold = _CportQosQueueThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 5, 1, 2),
    _CportQosQueueThreshold_Type()
)
cportQosQueueThreshold.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cportQosQueueThreshold.setStatus("deprecated")
_CportQosQueueEnqueuePkts_Type = Counter64
_CportQosQueueEnqueuePkts_Object = MibTableColumn
cportQosQueueEnqueuePkts = _CportQosQueueEnqueuePkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 5, 1, 3),
    _CportQosQueueEnqueuePkts_Type()
)
cportQosQueueEnqueuePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosQueueEnqueuePkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosQueueEnqueuePkts.setUnits("Packets")
_CportQosQueueDropPkts_Type = Counter64
_CportQosQueueDropPkts_Object = MibTableColumn
cportQosQueueDropPkts = _CportQosQueueDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 5, 1, 4),
    _CportQosQueueDropPkts_Type()
)
cportQosQueueDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosQueueDropPkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosQueueDropPkts.setUnits("Packets")
_CportQosClassEgressStatsTable_Object = MibTable
cportQosClassEgressStatsTable = _CportQosClassEgressStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 6)
)
if mibBuilder.loadTexts:
    cportQosClassEgressStatsTable.setStatus("deprecated")
_CportQosClassEgressStatsEntry_Object = MibTableRow
cportQosClassEgressStatsEntry = _CportQosClassEgressStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 6, 1)
)
cportQosClassEgressStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-PORT-QOS-MIB", "cportQosClassId"),
    (0, "CISCO-PORT-QOS-MIB", "cportQosClassThreshold"),
)
if mibBuilder.loadTexts:
    cportQosClassEgressStatsEntry.setStatus("deprecated")


class _CportQosClassId_Type(Unsigned32):
    """Custom type cportQosClassId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CportQosClassId_Type.__name__ = "Unsigned32"
_CportQosClassId_Object = MibTableColumn
cportQosClassId = _CportQosClassId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 6, 1, 1),
    _CportQosClassId_Type()
)
cportQosClassId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cportQosClassId.setStatus("deprecated")


class _CportQosClassThreshold_Type(Unsigned32):
    """Custom type cportQosClassThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CportQosClassThreshold_Type.__name__ = "Unsigned32"
_CportQosClassThreshold_Object = MibTableColumn
cportQosClassThreshold = _CportQosClassThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 6, 1, 2),
    _CportQosClassThreshold_Type()
)
cportQosClassThreshold.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cportQosClassThreshold.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosClassThreshold.setUnits("Number of buffers")
_CportQosClassName_Type = SnmpAdminString
_CportQosClassName_Object = MibTableColumn
cportQosClassName = _CportQosClassName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 6, 1, 3),
    _CportQosClassName_Type()
)
cportQosClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosClassName.setStatus("deprecated")
_CportQosClassEnqueuePkts_Type = Counter64
_CportQosClassEnqueuePkts_Object = MibTableColumn
cportQosClassEnqueuePkts = _CportQosClassEnqueuePkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 6, 1, 4),
    _CportQosClassEnqueuePkts_Type()
)
cportQosClassEnqueuePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosClassEnqueuePkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosClassEnqueuePkts.setUnits("Packets")
_CportQosClassDropPkts_Type = Counter64
_CportQosClassDropPkts_Object = MibTableColumn
cportQosClassDropPkts = _CportQosClassDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 6, 1, 5),
    _CportQosClassDropPkts_Type()
)
cportQosClassDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosClassDropPkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosClassDropPkts.setUnits("Packets")
_CportQosClassDiscontinuityTime_Type = TimeStamp
_CportQosClassDiscontinuityTime_Object = MibTableColumn
cportQosClassDiscontinuityTime = _CportQosClassDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 6, 1, 6),
    _CportQosClassDiscontinuityTime_Type()
)
cportQosClassDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosClassDiscontinuityTime.setStatus("deprecated")
_CportQosClassIngressStatsTable_Object = MibTable
cportQosClassIngressStatsTable = _CportQosClassIngressStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 7)
)
if mibBuilder.loadTexts:
    cportQosClassIngressStatsTable.setStatus("deprecated")
_CportQosClassIngressStatsEntry_Object = MibTableRow
cportQosClassIngressStatsEntry = _CportQosClassIngressStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 7, 1)
)
cportQosClassIngressStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-PORT-QOS-MIB", "cportQosClassIdLevel1"),
    (0, "CISCO-PORT-QOS-MIB", "cportQosClassIdLevel2"),
)
if mibBuilder.loadTexts:
    cportQosClassIngressStatsEntry.setStatus("deprecated")


class _CportQosClassIdLevel1_Type(Unsigned32):
    """Custom type cportQosClassIdLevel1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CportQosClassIdLevel1_Type.__name__ = "Unsigned32"
_CportQosClassIdLevel1_Object = MibTableColumn
cportQosClassIdLevel1 = _CportQosClassIdLevel1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 7, 1, 1),
    _CportQosClassIdLevel1_Type()
)
cportQosClassIdLevel1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cportQosClassIdLevel1.setStatus("deprecated")


class _CportQosClassIdLevel2_Type(Unsigned32):
    """Custom type cportQosClassIdLevel2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CportQosClassIdLevel2_Type.__name__ = "Unsigned32"
_CportQosClassIdLevel2_Object = MibTableColumn
cportQosClassIdLevel2 = _CportQosClassIdLevel2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 7, 1, 2),
    _CportQosClassIdLevel2_Type()
)
cportQosClassIdLevel2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cportQosClassIdLevel2.setStatus("deprecated")
_CportQosClassNameLevel1_Type = SnmpAdminString
_CportQosClassNameLevel1_Object = MibTableColumn
cportQosClassNameLevel1 = _CportQosClassNameLevel1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 7, 1, 3),
    _CportQosClassNameLevel1_Type()
)
cportQosClassNameLevel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosClassNameLevel1.setStatus("deprecated")
_CportQosClassNameLevel2_Type = SnmpAdminString
_CportQosClassNameLevel2_Object = MibTableColumn
cportQosClassNameLevel2 = _CportQosClassNameLevel2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 7, 1, 4),
    _CportQosClassNameLevel2_Type()
)
cportQosClassNameLevel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosClassNameLevel2.setStatus("deprecated")
_CportQosPoliceConformPkts_Type = Counter64
_CportQosPoliceConformPkts_Object = MibTableColumn
cportQosPoliceConformPkts = _CportQosPoliceConformPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 7, 1, 5),
    _CportQosPoliceConformPkts_Type()
)
cportQosPoliceConformPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosPoliceConformPkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosPoliceConformPkts.setUnits("Packets")
_CportQosPoliceConformOctets_Type = Counter64
_CportQosPoliceConformOctets_Object = MibTableColumn
cportQosPoliceConformOctets = _CportQosPoliceConformOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 7, 1, 6),
    _CportQosPoliceConformOctets_Type()
)
cportQosPoliceConformOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosPoliceConformOctets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosPoliceConformOctets.setUnits("Octets")
_CportQosPoliceExceedPkts_Type = Counter64
_CportQosPoliceExceedPkts_Object = MibTableColumn
cportQosPoliceExceedPkts = _CportQosPoliceExceedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 7, 1, 7),
    _CportQosPoliceExceedPkts_Type()
)
cportQosPoliceExceedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosPoliceExceedPkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosPoliceExceedPkts.setUnits("Packets")
_CportQosPoliceExceedOctets_Type = Counter64
_CportQosPoliceExceedOctets_Object = MibTableColumn
cportQosPoliceExceedOctets = _CportQosPoliceExceedOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 7, 1, 8),
    _CportQosPoliceExceedOctets_Type()
)
cportQosPoliceExceedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosPoliceExceedOctets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosPoliceExceedOctets.setUnits("Octets")
_CportQosPoliceViolatePkts_Type = Counter64
_CportQosPoliceViolatePkts_Object = MibTableColumn
cportQosPoliceViolatePkts = _CportQosPoliceViolatePkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 7, 1, 9),
    _CportQosPoliceViolatePkts_Type()
)
cportQosPoliceViolatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosPoliceViolatePkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosPoliceViolatePkts.setUnits("Packets")
_CportQosPoliceViolateOctets_Type = Counter64
_CportQosPoliceViolateOctets_Object = MibTableColumn
cportQosPoliceViolateOctets = _CportQosPoliceViolateOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 7, 1, 10),
    _CportQosPoliceViolateOctets_Type()
)
cportQosPoliceViolateOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosPoliceViolateOctets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosPoliceViolateOctets.setUnits("Octets")
_CportQosPoliceConformRate_Type = Gauge32
_CportQosPoliceConformRate_Object = MibTableColumn
cportQosPoliceConformRate = _CportQosPoliceConformRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 7, 1, 11),
    _CportQosPoliceConformRate_Type()
)
cportQosPoliceConformRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosPoliceConformRate.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosPoliceConformRate.setUnits("bits per second")
_CportQosPoliceExceedRate_Type = Gauge32
_CportQosPoliceExceedRate_Object = MibTableColumn
cportQosPoliceExceedRate = _CportQosPoliceExceedRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 7, 1, 12),
    _CportQosPoliceExceedRate_Type()
)
cportQosPoliceExceedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosPoliceExceedRate.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosPoliceExceedRate.setUnits("bits per second")
_CportQosPoliceViolateRate_Type = Gauge32
_CportQosPoliceViolateRate_Object = MibTableColumn
cportQosPoliceViolateRate = _CportQosPoliceViolateRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 7, 1, 13),
    _CportQosPoliceViolateRate_Type()
)
cportQosPoliceViolateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosPoliceViolateRate.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosPoliceViolateRate.setUnits("bits per second")
_CportQosPoliceDiscontinuityTime_Type = TimeStamp
_CportQosPoliceDiscontinuityTime_Object = MibTableColumn
cportQosPoliceDiscontinuityTime = _CportQosPoliceDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 7, 1, 14),
    _CportQosPoliceDiscontinuityTime_Type()
)
cportQosPoliceDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosPoliceDiscontinuityTime.setStatus("deprecated")
_CportQosDscpStatsTable_Object = MibTable
cportQosDscpStatsTable = _CportQosDscpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 8)
)
if mibBuilder.loadTexts:
    cportQosDscpStatsTable.setStatus("deprecated")
_CportQosDscpStatsEntry_Object = MibTableRow
cportQosDscpStatsEntry = _CportQosDscpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 8, 1)
)
cportQosDscpStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-PORT-QOS-MIB", "cportQosDscpValue"),
)
if mibBuilder.loadTexts:
    cportQosDscpStatsEntry.setStatus("deprecated")
_CportQosDscpValue_Type = Dscp
_CportQosDscpValue_Object = MibTableColumn
cportQosDscpValue = _CportQosDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 8, 1, 1),
    _CportQosDscpValue_Type()
)
cportQosDscpValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cportQosDscpValue.setStatus("deprecated")
_CportQosDscpIngressPkts_Type = Counter64
_CportQosDscpIngressPkts_Object = MibTableColumn
cportQosDscpIngressPkts = _CportQosDscpIngressPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 8, 1, 2),
    _CportQosDscpIngressPkts_Type()
)
cportQosDscpIngressPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosDscpIngressPkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosDscpIngressPkts.setUnits("Packets")
_CportQosDscpIngressOctets_Type = Counter64
_CportQosDscpIngressOctets_Object = MibTableColumn
cportQosDscpIngressOctets = _CportQosDscpIngressOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 8, 1, 3),
    _CportQosDscpIngressOctets_Type()
)
cportQosDscpIngressOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosDscpIngressOctets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosDscpIngressOctets.setUnits("Octets")
_CportQosDscpEgressPkts_Type = Counter64
_CportQosDscpEgressPkts_Object = MibTableColumn
cportQosDscpEgressPkts = _CportQosDscpEgressPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 8, 1, 4),
    _CportQosDscpEgressPkts_Type()
)
cportQosDscpEgressPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosDscpEgressPkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosDscpEgressPkts.setUnits("Packets")
_CportQosDscpEgressOctets_Type = Counter64
_CportQosDscpEgressOctets_Object = MibTableColumn
cportQosDscpEgressOctets = _CportQosDscpEgressOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 8, 1, 5),
    _CportQosDscpEgressOctets_Type()
)
cportQosDscpEgressOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosDscpEgressOctets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosDscpEgressOctets.setUnits("Octets")
_CportQosCosStatsTable_Object = MibTable
cportQosCosStatsTable = _CportQosCosStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 9)
)
if mibBuilder.loadTexts:
    cportQosCosStatsTable.setStatus("deprecated")
_CportQosCosStatsEntry_Object = MibTableRow
cportQosCosStatsEntry = _CportQosCosStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 9, 1)
)
cportQosCosStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-PORT-QOS-MIB", "cportQosCosValue"),
)
if mibBuilder.loadTexts:
    cportQosCosStatsEntry.setStatus("deprecated")
_CportQosCosValue_Type = QosLayer2Cos
_CportQosCosValue_Object = MibTableColumn
cportQosCosValue = _CportQosCosValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 9, 1, 1),
    _CportQosCosValue_Type()
)
cportQosCosValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cportQosCosValue.setStatus("deprecated")
_CportQosCosIngressPkts_Type = Counter64
_CportQosCosIngressPkts_Object = MibTableColumn
cportQosCosIngressPkts = _CportQosCosIngressPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 9, 1, 2),
    _CportQosCosIngressPkts_Type()
)
cportQosCosIngressPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosCosIngressPkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosCosIngressPkts.setUnits("Packets")
_CportQosCosIngressOctets_Type = Counter64
_CportQosCosIngressOctets_Object = MibTableColumn
cportQosCosIngressOctets = _CportQosCosIngressOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 9, 1, 3),
    _CportQosCosIngressOctets_Type()
)
cportQosCosIngressOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosCosIngressOctets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosCosIngressOctets.setUnits("Octets")
_CportQosCosEgressPkts_Type = Counter64
_CportQosCosEgressPkts_Object = MibTableColumn
cportQosCosEgressPkts = _CportQosCosEgressPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 9, 1, 4),
    _CportQosCosEgressPkts_Type()
)
cportQosCosEgressPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosCosEgressPkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosCosEgressPkts.setUnits("Packets")
_CportQosCosEgressOctets_Type = Counter64
_CportQosCosEgressOctets_Object = MibTableColumn
cportQosCosEgressOctets = _CportQosCosEgressOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 1, 3, 9, 1, 5),
    _CportQosCosEgressOctets_Type()
)
cportQosCosEgressOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cportQosCosEgressOctets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cportQosCosEgressOctets.setUnits("Octets")
_CiscoPortQosMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoPortQosMIBNotifications = _CiscoPortQosMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 2)
)
_CiscoPortQosMIBConformance_ObjectIdentity = ObjectIdentity
ciscoPortQosMIBConformance = _CiscoPortQosMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 3)
)
_CiscoPortQosMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoPortQosMIBCompliances = _CiscoPortQosMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 3, 1)
)
_CiscoPortQosMIBGroups_ObjectIdentity = ObjectIdentity
ciscoPortQosMIBGroups = _CiscoPortQosMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 3, 2)
)

# Managed Objects groups

ciscoPortQosMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 3, 2, 1)
)
ciscoPortQosMIBGroup.setObjects(
      *(("CISCO-PORT-QOS-MIB", "cportQosRLConfigEnable"),
        ("CISCO-PORT-QOS-MIB", "cportQosRLConfigRate"),
        ("CISCO-PORT-QOS-MIB", "cportQosRLConfigBurstSize"),
        ("CISCO-PORT-QOS-MIB", "cportQosTSConfigEnable"),
        ("CISCO-PORT-QOS-MIB", "cportQosTSConfigRate"),
        ("CISCO-PORT-QOS-MIB", "cportQosTSConfigBurstSize"))
)
if mibBuilder.loadTexts:
    ciscoPortQosMIBGroup.setStatus("deprecated")

ciscoPortQosStatsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 3, 2, 2)
)
ciscoPortQosStatsMIBGroup.setObjects(
      *(("CISCO-PORT-QOS-MIB", "cportQosIndexType"),
        ("CISCO-PORT-QOS-MIB", "cportQosPrePolicyPkts"),
        ("CISCO-PORT-QOS-MIB", "cportQosPrePolicyOctets"),
        ("CISCO-PORT-QOS-MIB", "cportQosPostPolicyOctets"),
        ("CISCO-PORT-QOS-MIB", "cportQosPostPolicyPkts"),
        ("CISCO-PORT-QOS-MIB", "cportQosDropPkts"),
        ("CISCO-PORT-QOS-MIB", "cportQosDropOctets"),
        ("CISCO-PORT-QOS-MIB", "cportQosClassifiedOctets"),
        ("CISCO-PORT-QOS-MIB", "cportQosClassifiedPkts"))
)
if mibBuilder.loadTexts:
    ciscoPortQosStatsMIBGroup.setStatus("deprecated")

ciscoPortQosStatsMIBGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 3, 2, 3)
)
ciscoPortQosStatsMIBGroupRev1.setObjects(
      *(("CISCO-PORT-QOS-MIB", "cportQosIndexType"),
        ("CISCO-PORT-QOS-MIB", "cportQosPrePolicyPkts"),
        ("CISCO-PORT-QOS-MIB", "cportQosPrePolicyOctets"),
        ("CISCO-PORT-QOS-MIB", "cportQosPostPolicyOctets"),
        ("CISCO-PORT-QOS-MIB", "cportQosPostPolicyPkts"),
        ("CISCO-PORT-QOS-MIB", "cportQosDropPkts"),
        ("CISCO-PORT-QOS-MIB", "cportQosDropOctets"),
        ("CISCO-PORT-QOS-MIB", "cportQosClassifiedOctets"),
        ("CISCO-PORT-QOS-MIB", "cportQosClassifiedPkts"),
        ("CISCO-PORT-QOS-MIB", "cportQosNoChangePkts"),
        ("CISCO-PORT-QOS-MIB", "cportQosNoChangeOctets"))
)
if mibBuilder.loadTexts:
    ciscoPortQosStatsMIBGroupRev1.setStatus("deprecated")

ciscoPortQosStatsMIBGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 3, 2, 4)
)
ciscoPortQosStatsMIBGroupRev2.setObjects(
      *(("CISCO-PORT-QOS-MIB", "cportQosIndexTypeNew"),
        ("CISCO-PORT-QOS-MIB", "cportQosPrePolicyPkts"),
        ("CISCO-PORT-QOS-MIB", "cportQosPrePolicyOctets"),
        ("CISCO-PORT-QOS-MIB", "cportQosPostPolicyOctets"),
        ("CISCO-PORT-QOS-MIB", "cportQosPostPolicyPkts"),
        ("CISCO-PORT-QOS-MIB", "cportQosDropPkts"),
        ("CISCO-PORT-QOS-MIB", "cportQosDropOctets"),
        ("CISCO-PORT-QOS-MIB", "cportQosClassifiedOctets"),
        ("CISCO-PORT-QOS-MIB", "cportQosClassifiedPkts"),
        ("CISCO-PORT-QOS-MIB", "cportQosNoChangePkts"),
        ("CISCO-PORT-QOS-MIB", "cportQosNoChangeOctets"),
        ("CISCO-PORT-QOS-MIB", "cportQosInProfPolicyPkts"),
        ("CISCO-PORT-QOS-MIB", "cportQosOutOfProfPolicyPkts"))
)
if mibBuilder.loadTexts:
    ciscoPortQosStatsMIBGroupRev2.setStatus("deprecated")

ciscoPortQosStatsMIBGroupRev2Supp1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 3, 2, 5)
)
ciscoPortQosStatsMIBGroupRev2Supp1.setObjects(
      *(("CISCO-PORT-QOS-MIB", "cportQosVlanInProfPolicyPkts"),
        ("CISCO-PORT-QOS-MIB", "cportQosVlanOutOfProfPolicyPkts"))
)
if mibBuilder.loadTexts:
    ciscoPortQosStatsMIBGroupRev2Supp1.setStatus("deprecated")

ciscoPortQosStatsMIBGroupRev2Supp2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 3, 2, 6)
)
ciscoPortQosStatsMIBGroupRev2Supp2.setObjects(
      *(("CISCO-PORT-QOS-MIB", "cportQosInProfPolicyOctets"),
        ("CISCO-PORT-QOS-MIB", "cportQosOutOfProfPolicyOctets"),
        ("CISCO-PORT-QOS-MIB", "cportQosViolateProfPolicyPkts"),
        ("CISCO-PORT-QOS-MIB", "cportQosViolateProfPolicyOctets"))
)
if mibBuilder.loadTexts:
    ciscoPortQosStatsMIBGroupRev2Supp2.setStatus("deprecated")

ciscoPortQosStatsMIBGroupRev2Supp3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 3, 2, 7)
)
ciscoPortQosStatsMIBGroupRev2Supp3.setObjects(
      *(("CISCO-PORT-QOS-MIB", "cportQosVlanInProfPolicyOctets"),
        ("CISCO-PORT-QOS-MIB", "cportQosVlanOutOfProfPolicyOctets"),
        ("CISCO-PORT-QOS-MIB", "cportQosVlanViolateProfPolicyPkts"),
        ("CISCO-PORT-QOS-MIB", "cportQosVlanViolateProfPolicyOctets"))
)
if mibBuilder.loadTexts:
    ciscoPortQosStatsMIBGroupRev2Supp3.setStatus("deprecated")

ciscoPortQosStatsMIBGroupRev2Supp4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 3, 2, 8)
)
ciscoPortQosStatsMIBGroupRev2Supp4.setObjects(
      *(("CISCO-PORT-QOS-MIB", "cportQosQueueEnqueuePkts"),
        ("CISCO-PORT-QOS-MIB", "cportQosQueueDropPkts"))
)
if mibBuilder.loadTexts:
    ciscoPortQosStatsMIBGroupRev2Supp4.setStatus("deprecated")

ciscoPortQosStatsMIBGroupRev2Supp5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 3, 2, 9)
)
ciscoPortQosStatsMIBGroupRev2Supp5.setObjects(
      *(("CISCO-PORT-QOS-MIB", "cportQosClassName"),
        ("CISCO-PORT-QOS-MIB", "cportQosClassEnqueuePkts"),
        ("CISCO-PORT-QOS-MIB", "cportQosClassDropPkts"),
        ("CISCO-PORT-QOS-MIB", "cportQosClassDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    ciscoPortQosStatsMIBGroupRev2Supp5.setStatus("deprecated")

ciscoPortQosStatsMIBGroupRev2Supp6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 3, 2, 10)
)
ciscoPortQosStatsMIBGroupRev2Supp6.setObjects(
      *(("CISCO-PORT-QOS-MIB", "cportQosClassNameLevel1"),
        ("CISCO-PORT-QOS-MIB", "cportQosClassNameLevel2"),
        ("CISCO-PORT-QOS-MIB", "cportQosPoliceConformPkts"),
        ("CISCO-PORT-QOS-MIB", "cportQosPoliceConformOctets"),
        ("CISCO-PORT-QOS-MIB", "cportQosPoliceExceedPkts"),
        ("CISCO-PORT-QOS-MIB", "cportQosPoliceExceedOctets"),
        ("CISCO-PORT-QOS-MIB", "cportQosPoliceViolatePkts"),
        ("CISCO-PORT-QOS-MIB", "cportQosPoliceViolateOctets"),
        ("CISCO-PORT-QOS-MIB", "cportQosPoliceConformRate"),
        ("CISCO-PORT-QOS-MIB", "cportQosPoliceExceedRate"),
        ("CISCO-PORT-QOS-MIB", "cportQosPoliceViolateRate"),
        ("CISCO-PORT-QOS-MIB", "cportQosPoliceDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    ciscoPortQosStatsMIBGroupRev2Supp6.setStatus("deprecated")

ciscoPortQosStatsMIBGroupRev2Supp7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 3, 2, 11)
)
ciscoPortQosStatsMIBGroupRev2Supp7.setObjects(
      *(("CISCO-PORT-QOS-MIB", "cportQosDscpIngressPkts"),
        ("CISCO-PORT-QOS-MIB", "cportQosDscpIngressOctets"),
        ("CISCO-PORT-QOS-MIB", "cportQosDscpEgressPkts"),
        ("CISCO-PORT-QOS-MIB", "cportQosDscpEgressOctets"))
)
if mibBuilder.loadTexts:
    ciscoPortQosStatsMIBGroupRev2Supp7.setStatus("deprecated")

ciscoPortQosStatsMIBGroupRev2Supp8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 3, 2, 12)
)
ciscoPortQosStatsMIBGroupRev2Supp8.setObjects(
      *(("CISCO-PORT-QOS-MIB", "cportQosCosIngressPkts"),
        ("CISCO-PORT-QOS-MIB", "cportQosCosIngressOctets"),
        ("CISCO-PORT-QOS-MIB", "cportQosCosEgressPkts"),
        ("CISCO-PORT-QOS-MIB", "cportQosCosEgressOctets"))
)
if mibBuilder.loadTexts:
    ciscoPortQosStatsMIBGroupRev2Supp8.setStatus("deprecated")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoPortQosMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoPortQosMIBCompliance.setStatus(
        "deprecated"
    )

ciscoPortQosMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoPortQosMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoPortQosMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoPortQosMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoPortQosMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoPortQosMIBComplianceRev3.setStatus(
        "deprecated"
    )

ciscoPortQosMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 3, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoPortQosMIBComplianceRev4.setStatus(
        "deprecated"
    )

ciscoPortQosMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 3, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoPortQosMIBComplianceRev5.setStatus(
        "deprecated"
    )

ciscoPortQosMIBComplianceRev6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 189, 3, 1, 7)
)
if mibBuilder.loadTexts:
    ciscoPortQosMIBComplianceRev6.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-PORT-QOS-MIB",
    **{"ciscoPortQosMIB": ciscoPortQosMIB,
       "ciscoPortQosMIBObjects": ciscoPortQosMIBObjects,
       "cportQosRLConfig": cportQosRLConfig,
       "cportQosRLConfigTable": cportQosRLConfigTable,
       "cportQosRLConfigEntry": cportQosRLConfigEntry,
       "cportQosRLConfigDirection": cportQosRLConfigDirection,
       "cportQosRLConfigEnable": cportQosRLConfigEnable,
       "cportQosRLConfigRate": cportQosRLConfigRate,
       "cportQosRLConfigBurstSize": cportQosRLConfigBurstSize,
       "cportQosTSConfig": cportQosTSConfig,
       "cportQosTSConfigTable": cportQosTSConfigTable,
       "cportQosTSConfigEntry": cportQosTSConfigEntry,
       "cportQosTSConfigEnable": cportQosTSConfigEnable,
       "cportQosTSConfigRate": cportQosTSConfigRate,
       "cportQosTSConfigBurstSize": cportQosTSConfigBurstSize,
       "cportQosStatistics": cportQosStatistics,
       "cportQosIndexType": cportQosIndexType,
       "cportQosStatsTable": cportQosStatsTable,
       "cportQosStatsEntry": cportQosStatsEntry,
       "cportQosDirection": cportQosDirection,
       "cportQosIndex": cportQosIndex,
       "cportQosPrePolicyPkts": cportQosPrePolicyPkts,
       "cportQosPrePolicyOctets": cportQosPrePolicyOctets,
       "cportQosPostPolicyPkts": cportQosPostPolicyPkts,
       "cportQosPostPolicyOctets": cportQosPostPolicyOctets,
       "cportQosDropPkts": cportQosDropPkts,
       "cportQosDropOctets": cportQosDropOctets,
       "cportQosClassifiedOctets": cportQosClassifiedOctets,
       "cportQosClassifiedPkts": cportQosClassifiedPkts,
       "cportQosNoChangePkts": cportQosNoChangePkts,
       "cportQosNoChangeOctets": cportQosNoChangeOctets,
       "cportQosInProfPolicyPkts": cportQosInProfPolicyPkts,
       "cportQosOutOfProfPolicyPkts": cportQosOutOfProfPolicyPkts,
       "cportQosInProfPolicyOctets": cportQosInProfPolicyOctets,
       "cportQosOutOfProfPolicyOctets": cportQosOutOfProfPolicyOctets,
       "cportQosViolateProfPolicyPkts": cportQosViolateProfPolicyPkts,
       "cportQosViolateProfPolicyOctets": cportQosViolateProfPolicyOctets,
       "cportQosIndexTypeNew": cportQosIndexTypeNew,
       "cportQosInVlanStatsTable": cportQosInVlanStatsTable,
       "cportQosInVlanStatsEntry": cportQosInVlanStatsEntry,
       "cportQosVlanInProfPolicyPkts": cportQosVlanInProfPolicyPkts,
       "cportQosVlanOutOfProfPolicyPkts": cportQosVlanOutOfProfPolicyPkts,
       "cportQosVlanInProfPolicyOctets": cportQosVlanInProfPolicyOctets,
       "cportQosVlanOutOfProfPolicyOctets": cportQosVlanOutOfProfPolicyOctets,
       "cportQosVlanViolateProfPolicyPkts": cportQosVlanViolateProfPolicyPkts,
       "cportQosVlanViolateProfPolicyOctets": cportQosVlanViolateProfPolicyOctets,
       "cportQosEgressQueueStatsTable": cportQosEgressQueueStatsTable,
       "cportQosEgressQueueStatsEntry": cportQosEgressQueueStatsEntry,
       "cportQosQueueId": cportQosQueueId,
       "cportQosQueueThreshold": cportQosQueueThreshold,
       "cportQosQueueEnqueuePkts": cportQosQueueEnqueuePkts,
       "cportQosQueueDropPkts": cportQosQueueDropPkts,
       "cportQosClassEgressStatsTable": cportQosClassEgressStatsTable,
       "cportQosClassEgressStatsEntry": cportQosClassEgressStatsEntry,
       "cportQosClassId": cportQosClassId,
       "cportQosClassThreshold": cportQosClassThreshold,
       "cportQosClassName": cportQosClassName,
       "cportQosClassEnqueuePkts": cportQosClassEnqueuePkts,
       "cportQosClassDropPkts": cportQosClassDropPkts,
       "cportQosClassDiscontinuityTime": cportQosClassDiscontinuityTime,
       "cportQosClassIngressStatsTable": cportQosClassIngressStatsTable,
       "cportQosClassIngressStatsEntry": cportQosClassIngressStatsEntry,
       "cportQosClassIdLevel1": cportQosClassIdLevel1,
       "cportQosClassIdLevel2": cportQosClassIdLevel2,
       "cportQosClassNameLevel1": cportQosClassNameLevel1,
       "cportQosClassNameLevel2": cportQosClassNameLevel2,
       "cportQosPoliceConformPkts": cportQosPoliceConformPkts,
       "cportQosPoliceConformOctets": cportQosPoliceConformOctets,
       "cportQosPoliceExceedPkts": cportQosPoliceExceedPkts,
       "cportQosPoliceExceedOctets": cportQosPoliceExceedOctets,
       "cportQosPoliceViolatePkts": cportQosPoliceViolatePkts,
       "cportQosPoliceViolateOctets": cportQosPoliceViolateOctets,
       "cportQosPoliceConformRate": cportQosPoliceConformRate,
       "cportQosPoliceExceedRate": cportQosPoliceExceedRate,
       "cportQosPoliceViolateRate": cportQosPoliceViolateRate,
       "cportQosPoliceDiscontinuityTime": cportQosPoliceDiscontinuityTime,
       "cportQosDscpStatsTable": cportQosDscpStatsTable,
       "cportQosDscpStatsEntry": cportQosDscpStatsEntry,
       "cportQosDscpValue": cportQosDscpValue,
       "cportQosDscpIngressPkts": cportQosDscpIngressPkts,
       "cportQosDscpIngressOctets": cportQosDscpIngressOctets,
       "cportQosDscpEgressPkts": cportQosDscpEgressPkts,
       "cportQosDscpEgressOctets": cportQosDscpEgressOctets,
       "cportQosCosStatsTable": cportQosCosStatsTable,
       "cportQosCosStatsEntry": cportQosCosStatsEntry,
       "cportQosCosValue": cportQosCosValue,
       "cportQosCosIngressPkts": cportQosCosIngressPkts,
       "cportQosCosIngressOctets": cportQosCosIngressOctets,
       "cportQosCosEgressPkts": cportQosCosEgressPkts,
       "cportQosCosEgressOctets": cportQosCosEgressOctets,
       "ciscoPortQosMIBNotifications": ciscoPortQosMIBNotifications,
       "ciscoPortQosMIBConformance": ciscoPortQosMIBConformance,
       "ciscoPortQosMIBCompliances": ciscoPortQosMIBCompliances,
       "ciscoPortQosMIBCompliance": ciscoPortQosMIBCompliance,
       "ciscoPortQosMIBComplianceRev1": ciscoPortQosMIBComplianceRev1,
       "ciscoPortQosMIBComplianceRev2": ciscoPortQosMIBComplianceRev2,
       "ciscoPortQosMIBComplianceRev3": ciscoPortQosMIBComplianceRev3,
       "ciscoPortQosMIBComplianceRev4": ciscoPortQosMIBComplianceRev4,
       "ciscoPortQosMIBComplianceRev5": ciscoPortQosMIBComplianceRev5,
       "ciscoPortQosMIBComplianceRev6": ciscoPortQosMIBComplianceRev6,
       "ciscoPortQosMIBGroups": ciscoPortQosMIBGroups,
       "ciscoPortQosMIBGroup": ciscoPortQosMIBGroup,
       "ciscoPortQosStatsMIBGroup": ciscoPortQosStatsMIBGroup,
       "ciscoPortQosStatsMIBGroupRev1": ciscoPortQosStatsMIBGroupRev1,
       "ciscoPortQosStatsMIBGroupRev2": ciscoPortQosStatsMIBGroupRev2,
       "ciscoPortQosStatsMIBGroupRev2Supp1": ciscoPortQosStatsMIBGroupRev2Supp1,
       "ciscoPortQosStatsMIBGroupRev2Supp2": ciscoPortQosStatsMIBGroupRev2Supp2,
       "ciscoPortQosStatsMIBGroupRev2Supp3": ciscoPortQosStatsMIBGroupRev2Supp3,
       "ciscoPortQosStatsMIBGroupRev2Supp4": ciscoPortQosStatsMIBGroupRev2Supp4,
       "ciscoPortQosStatsMIBGroupRev2Supp5": ciscoPortQosStatsMIBGroupRev2Supp5,
       "ciscoPortQosStatsMIBGroupRev2Supp6": ciscoPortQosStatsMIBGroupRev2Supp6,
       "ciscoPortQosStatsMIBGroupRev2Supp7": ciscoPortQosStatsMIBGroupRev2Supp7,
       "ciscoPortQosStatsMIBGroupRev2Supp8": ciscoPortQosStatsMIBGroupRev2Supp8}
)
