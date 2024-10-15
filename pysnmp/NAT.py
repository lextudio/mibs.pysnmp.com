# SNMP MIB module (NAT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NAT
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:39 2024
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nat_ObjectIdentity = ObjectIdentity
nat = _Nat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 86)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 86, 1)
)
_Natmib_ObjectIdentity = ObjectIdentity
natmib = _Natmib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 86, 2)
)
_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 86, 2, 1)
)
_CfFirmware_Type = OctetString
_CfFirmware_Object = MibScalar
cfFirmware = _CfFirmware_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 1, 1),
    _CfFirmware_Type()
)
cfFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfFirmware.setStatus("mandatory")
_CfCmstrTable_Object = MibTable
cfCmstrTable = _CfCmstrTable_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cfCmstrTable.setStatus("mandatory")
_CfCmstrEntry_Object = MibTableRow
cfCmstrEntry = _CfCmstrEntry_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 1, 2, 1)
)
cfCmstrEntry.setIndexNames(
    (0, "NAT", "pysmiFakeCol1"),
)
if mibBuilder.loadTexts:
    cfCmstrEntry.setStatus("mandatory")
_CfCmstrReadPublic_Type = OctetString
_CfCmstrReadPublic_Object = MibTableColumn
cfCmstrReadPublic = _CfCmstrReadPublic_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 1, 2, 1, 1),
    _CfCmstrReadPublic_Type()
)
cfCmstrReadPublic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfCmstrReadPublic.setStatus("mandatory")
_CfCmstrReadEnterprise_Type = OctetString
_CfCmstrReadEnterprise_Object = MibTableColumn
cfCmstrReadEnterprise = _CfCmstrReadEnterprise_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 1, 2, 1, 2),
    _CfCmstrReadEnterprise_Type()
)
cfCmstrReadEnterprise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfCmstrReadEnterprise.setStatus("mandatory")
_CfCmstrReadTrap_Type = OctetString
_CfCmstrReadTrap_Object = MibTableColumn
cfCmstrReadTrap = _CfCmstrReadTrap_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 1, 2, 1, 3),
    _CfCmstrReadTrap_Type()
)
cfCmstrReadTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfCmstrReadTrap.setStatus("mandatory")
_CfCmstrReadWrite_Type = OctetString
_CfCmstrReadWrite_Object = MibTableColumn
cfCmstrReadWrite = _CfCmstrReadWrite_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 1, 2, 1, 4),
    _CfCmstrReadWrite_Type()
)
cfCmstrReadWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfCmstrReadWrite.setStatus("mandatory")
_PysmiFakeCol1_Type = Integer32
_PysmiFakeCol1_Object = MibTableColumn
pysmiFakeCol1 = _PysmiFakeCol1_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 1, 2, 1, 4294967295),
    _PysmiFakeCol1_Type()
)
pysmiFakeCol1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol1.setStatus("mandatory")
_CfCmstrAliasTable_Object = MibTable
cfCmstrAliasTable = _CfCmstrAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 1, 3)
)
if mibBuilder.loadTexts:
    cfCmstrAliasTable.setStatus("mandatory")
_CfCmstrAliasEntry_Object = MibTableRow
cfCmstrAliasEntry = _CfCmstrAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 1, 3, 1)
)
cfCmstrAliasEntry.setIndexNames(
    (0, "NAT", "pysmiFakeCol2"),
)
if mibBuilder.loadTexts:
    cfCmstrAliasEntry.setStatus("mandatory")
_CfCmstrAliasReadPublic_Type = OctetString
_CfCmstrAliasReadPublic_Object = MibTableColumn
cfCmstrAliasReadPublic = _CfCmstrAliasReadPublic_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 1, 3, 1, 1),
    _CfCmstrAliasReadPublic_Type()
)
cfCmstrAliasReadPublic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfCmstrAliasReadPublic.setStatus("mandatory")
_CfCmstrAliasReadEnterprise_Type = OctetString
_CfCmstrAliasReadEnterprise_Object = MibTableColumn
cfCmstrAliasReadEnterprise = _CfCmstrAliasReadEnterprise_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 1, 3, 1, 2),
    _CfCmstrAliasReadEnterprise_Type()
)
cfCmstrAliasReadEnterprise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfCmstrAliasReadEnterprise.setStatus("mandatory")
_CfCmstrAliasReadTrap_Type = OctetString
_CfCmstrAliasReadTrap_Object = MibTableColumn
cfCmstrAliasReadTrap = _CfCmstrAliasReadTrap_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 1, 3, 1, 3),
    _CfCmstrAliasReadTrap_Type()
)
cfCmstrAliasReadTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfCmstrAliasReadTrap.setStatus("mandatory")
_CfCmstrAliasReadWrite_Type = OctetString
_CfCmstrAliasReadWrite_Object = MibTableColumn
cfCmstrAliasReadWrite = _CfCmstrAliasReadWrite_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 1, 3, 1, 4),
    _CfCmstrAliasReadWrite_Type()
)
cfCmstrAliasReadWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfCmstrAliasReadWrite.setStatus("mandatory")
_PysmiFakeCol2_Type = Integer32
_PysmiFakeCol2_Object = MibTableColumn
pysmiFakeCol2 = _PysmiFakeCol2_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 1, 3, 1, 4294967295),
    _PysmiFakeCol2_Type()
)
pysmiFakeCol2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol2.setStatus("mandatory")
_CfAcchostTable_Object = MibTable
cfAcchostTable = _CfAcchostTable_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 1, 4)
)
if mibBuilder.loadTexts:
    cfAcchostTable.setStatus("mandatory")
_CfAcchostEntry_Object = MibTableRow
cfAcchostEntry = _CfAcchostEntry_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 1, 4, 1)
)
cfAcchostEntry.setIndexNames(
    (0, "NAT", "pysmiFakeCol3"),
)
if mibBuilder.loadTexts:
    cfAcchostEntry.setStatus("mandatory")
_CfAcchostHostIP_Type = IpAddress
_CfAcchostHostIP_Object = MibTableColumn
cfAcchostHostIP = _CfAcchostHostIP_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 1, 4, 1, 1),
    _CfAcchostHostIP_Type()
)
cfAcchostHostIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfAcchostHostIP.setStatus("mandatory")


class _CfAcchostLevel_Type(Integer32):
    """Custom type cfAcchostLevel based on Integer32"""
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
        *(("readenterprise", 2),
          ("readstandard", 1),
          ("readwrite", 4),
          ("readwriteenterprise", 5),
          ("trap", 3))
    )


_CfAcchostLevel_Type.__name__ = "Integer32"
_CfAcchostLevel_Object = MibTableColumn
cfAcchostLevel = _CfAcchostLevel_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 1, 4, 1, 2),
    _CfAcchostLevel_Type()
)
cfAcchostLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfAcchostLevel.setStatus("mandatory")
_PysmiFakeCol3_Type = Integer32
_PysmiFakeCol3_Object = MibTableColumn
pysmiFakeCol3 = _PysmiFakeCol3_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 1, 4, 1, 4294967295),
    _PysmiFakeCol3_Type()
)
pysmiFakeCol3.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol3.setStatus("mandatory")


class _CfDenyReadPublic_Type(Integer32):
    """Custom type cfDenyReadPublic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_CfDenyReadPublic_Type.__name__ = "Integer32"
_CfDenyReadPublic_Object = MibScalar
cfDenyReadPublic = _CfDenyReadPublic_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 1, 5),
    _CfDenyReadPublic_Type()
)
cfDenyReadPublic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfDenyReadPublic.setStatus("mandatory")
_CfDevIPAddr_Type = IpAddress
_CfDevIPAddr_Object = MibScalar
cfDevIPAddr = _CfDevIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 1, 6),
    _CfDevIPAddr_Type()
)
cfDevIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfDevIPAddr.setStatus("mandatory")
_CfSubnetMask_Type = IpAddress
_CfSubnetMask_Object = MibScalar
cfSubnetMask = _CfSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 1, 7),
    _CfSubnetMask_Type()
)
cfSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfSubnetMask.setStatus("mandatory")
_CfAcchostCfgTable_Object = MibTable
cfAcchostCfgTable = _CfAcchostCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 1, 8)
)
if mibBuilder.loadTexts:
    cfAcchostCfgTable.setStatus("mandatory")
_CfAcchostCfgEntry_Object = MibTableRow
cfAcchostCfgEntry = _CfAcchostCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 1, 8, 1)
)
cfAcchostCfgEntry.setIndexNames(
    (0, "NAT", "pysmiFakeCol4"),
)
if mibBuilder.loadTexts:
    cfAcchostCfgEntry.setStatus("mandatory")


class _CfAcchostCfgAcclvl_Type(Integer32):
    """Custom type cfAcchostCfgAcclvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cfAddReadEnterprise", 2),
          ("cfAddReadStd", 1),
          ("cfAddReadwrite", 4),
          ("cfAddTrap", 3),
          ("cfDelet", 0))
    )


_CfAcchostCfgAcclvl_Type.__name__ = "Integer32"
_CfAcchostCfgAcclvl_Object = MibScalar
cfAcchostCfgAcclvl = _CfAcchostCfgAcclvl_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 1, 8, 1, 1),
    _CfAcchostCfgAcclvl_Type()
)
cfAcchostCfgAcclvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfAcchostCfgAcclvl.setStatus("mandatory")
_PysmiFakeCol4_Type = IpAddress
_PysmiFakeCol4_Object = MibTableColumn
pysmiFakeCol4 = _PysmiFakeCol4_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 1, 8, 1, 4294967295),
    _PysmiFakeCol4_Type()
)
pysmiFakeCol4.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol4.setStatus("mandatory")


class _CfParmsSave_Type(Integer32):
    """Custom type cfParmsSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cfClear", 0),
          ("cfStore", 1))
    )


_CfParmsSave_Type.__name__ = "Integer32"
_CfParmsSave_Object = MibScalar
cfParmsSave = _CfParmsSave_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 1, 9),
    _CfParmsSave_Type()
)
cfParmsSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfParmsSave.setStatus("mandatory")
_CfPassword_Type = OctetString
_CfPassword_Object = MibScalar
cfPassword = _CfPassword_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 1, 10),
    _CfPassword_Type()
)
cfPassword.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cfPassword.setStatus("mandatory")
_CfIPAddr2_Type = IpAddress
_CfIPAddr2_Object = MibScalar
cfIPAddr2 = _CfIPAddr2_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 1, 11),
    _CfIPAddr2_Type()
)
cfIPAddr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfIPAddr2.setStatus("mandatory")
_CfSubnetMask2_Type = IpAddress
_CfSubnetMask2_Object = MibScalar
cfSubnetMask2 = _CfSubnetMask2_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 1, 12),
    _CfSubnetMask2_Type()
)
cfSubnetMask2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfSubnetMask2.setStatus("mandatory")
_Natinf_ObjectIdentity = ObjectIdentity
natinf = _Natinf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 86, 2, 2)
)
_StatsTable_Object = MibTable
statsTable = _StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 2, 1)
)
if mibBuilder.loadTexts:
    statsTable.setStatus("mandatory")
_StatsEntry_Object = MibTableRow
statsEntry = _StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 2, 1, 1)
)
statsEntry.setIndexNames(
    (0, "NAT", "pysmiFakeCol5"),
)
if mibBuilder.loadTexts:
    statsEntry.setStatus("mandatory")
_StatsReset_Type = Integer32
_StatsReset_Object = MibTableColumn
statsReset = _StatsReset_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 2, 1, 1, 1),
    _StatsReset_Type()
)
statsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statsReset.setStatus("mandatory")
_StatsResetTime_Type = TimeTicks
_StatsResetTime_Object = MibTableColumn
statsResetTime = _StatsResetTime_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 2, 1, 1, 2),
    _StatsResetTime_Type()
)
statsResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsResetTime.setStatus("mandatory")
_StatsRcvpkts_Type = Counter32
_StatsRcvpkts_Object = MibTableColumn
statsRcvpkts = _StatsRcvpkts_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 2, 1, 1, 3),
    _StatsRcvpkts_Type()
)
statsRcvpkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsRcvpkts.setStatus("mandatory")
_StatsFwdpkts_Type = Counter32
_StatsFwdpkts_Object = MibTableColumn
statsFwdpkts = _StatsFwdpkts_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 2, 1, 1, 4),
    _StatsFwdpkts_Type()
)
statsFwdpkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsFwdpkts.setStatus("mandatory")
_StatsBufOvflows_Type = Counter32
_StatsBufOvflows_Object = MibTableColumn
statsBufOvflows = _StatsBufOvflows_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 2, 1, 1, 5),
    _StatsBufOvflows_Type()
)
statsBufOvflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsBufOvflows.setStatus("mandatory")
_StatsCrcs_Type = Counter32
_StatsCrcs_Object = MibTableColumn
statsCrcs = _StatsCrcs_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 2, 1, 1, 6),
    _StatsCrcs_Type()
)
statsCrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsCrcs.setStatus("mandatory")
_StatsAlgns_Type = Counter32
_StatsAlgns_Object = MibTableColumn
statsAlgns = _StatsAlgns_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 2, 1, 1, 7),
    _StatsAlgns_Type()
)
statsAlgns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsAlgns.setStatus("mandatory")
_StatsCntlOvflows_Type = Counter32
_StatsCntlOvflows_Object = MibTableColumn
statsCntlOvflows = _StatsCntlOvflows_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 2, 1, 1, 8),
    _StatsCntlOvflows_Type()
)
statsCntlOvflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsCntlOvflows.setStatus("mandatory")
_StatsXmtColls_Type = Counter32
_StatsXmtColls_Object = MibTableColumn
statsXmtColls = _StatsXmtColls_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 2, 1, 1, 9),
    _StatsXmtColls_Type()
)
statsXmtColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsXmtColls.setStatus("mandatory")
_StatsBlkDiscards_Type = Counter32
_StatsBlkDiscards_Object = MibTableColumn
statsBlkDiscards = _StatsBlkDiscards_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 2, 1, 1, 10),
    _StatsBlkDiscards_Type()
)
statsBlkDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsBlkDiscards.setStatus("mandatory")
_StatsPassDiscards_Type = Counter32
_StatsPassDiscards_Object = MibScalar
statsPassDiscards = _StatsPassDiscards_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 2, 1, 1, 11),
    _StatsPassDiscards_Type()
)
statsPassDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsPassDiscards.setStatus("mandatory")
_StatsFwdMultiPkts_Type = Counter32
_StatsFwdMultiPkts_Object = MibTableColumn
statsFwdMultiPkts = _StatsFwdMultiPkts_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 2, 1, 1, 12),
    _StatsFwdMultiPkts_Type()
)
statsFwdMultiPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsFwdMultiPkts.setStatus("mandatory")
_StatsKbytes_Type = Counter32
_StatsKbytes_Object = MibTableColumn
statsKbytes = _StatsKbytes_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 2, 1, 1, 13),
    _StatsKbytes_Type()
)
statsKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsKbytes.setStatus("mandatory")
_StatsBcastPkts_Type = Counter32
_StatsBcastPkts_Object = MibTableColumn
statsBcastPkts = _StatsBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 2, 1, 1, 14),
    _StatsBcastPkts_Type()
)
statsBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsBcastPkts.setStatus("mandatory")
_StatsMcastPkts_Type = Counter32
_StatsMcastPkts_Object = MibTableColumn
statsMcastPkts = _StatsMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 2, 1, 1, 15),
    _StatsMcastPkts_Type()
)
statsMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsMcastPkts.setStatus("mandatory")
_StatsSize64_127Pkts_Type = Counter32
_StatsSize64_127Pkts_Object = MibScalar
statsSize64_127Pkts = _StatsSize64_127Pkts_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 2, 1, 1, 16),
    _StatsSize64_127Pkts_Type()
)
statsSize64_127Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsSize64_127Pkts.setStatus("mandatory")
_StatsSize128_255Pkts_Type = Counter32
_StatsSize128_255Pkts_Object = MibScalar
statsSize128_255Pkts = _StatsSize128_255Pkts_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 2, 1, 1, 17),
    _StatsSize128_255Pkts_Type()
)
statsSize128_255Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsSize128_255Pkts.setStatus("mandatory")
_StatsSize256_511Pkts_Type = Counter32
_StatsSize256_511Pkts_Object = MibScalar
statsSize256_511Pkts = _StatsSize256_511Pkts_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 2, 1, 1, 18),
    _StatsSize256_511Pkts_Type()
)
statsSize256_511Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsSize256_511Pkts.setStatus("mandatory")
_StatsSize512_1023Pkts_Type = Counter32
_StatsSize512_1023Pkts_Object = MibScalar
statsSize512_1023Pkts = _StatsSize512_1023Pkts_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 2, 1, 1, 19),
    _StatsSize512_1023Pkts_Type()
)
statsSize512_1023Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsSize512_1023Pkts.setStatus("mandatory")
_StatsSize1024_1518Pkts_Type = Counter32
_StatsSize1024_1518Pkts_Object = MibScalar
statsSize1024_1518Pkts = _StatsSize1024_1518Pkts_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 2, 1, 1, 20),
    _StatsSize1024_1518Pkts_Type()
)
statsSize1024_1518Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsSize1024_1518Pkts.setStatus("mandatory")
_StatsShortPkts_Type = Counter32
_StatsShortPkts_Object = MibTableColumn
statsShortPkts = _StatsShortPkts_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 2, 1, 1, 21),
    _StatsShortPkts_Type()
)
statsShortPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsShortPkts.setStatus("mandatory")
_StatsOvsizePkts_Type = Counter32
_StatsOvsizePkts_Object = MibTableColumn
statsOvsizePkts = _StatsOvsizePkts_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 2, 1, 1, 22),
    _StatsOvsizePkts_Type()
)
statsOvsizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsOvsizePkts.setStatus("mandatory")
_PysmiFakeCol5_Type = Integer32
_PysmiFakeCol5_Object = MibTableColumn
pysmiFakeCol5 = _PysmiFakeCol5_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 2, 1, 1, 4294967295),
    _PysmiFakeCol5_Type()
)
pysmiFakeCol5.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol5.setStatus("mandatory")
_Natopr_ObjectIdentity = ObjectIdentity
natopr = _Natopr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 86, 2, 3)
)
_OpSysReset_Type = Integer32
_OpSysReset_Object = MibScalar
opSysReset = _OpSysReset_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 3, 1),
    _OpSysReset_Type()
)
opSysReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opSysReset.setStatus("mandatory")


class _OpNoStatColl_Type(Integer32):
    """Custom type opNoStatColl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_OpNoStatColl_Type.__name__ = "Integer32"
_OpNoStatColl_Object = MibScalar
opNoStatColl = _OpNoStatColl_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 3, 2),
    _OpNoStatColl_Type()
)
opNoStatColl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opNoStatColl.setStatus("mandatory")


class _OpTrapInact_Type(Integer32):
    """Custom type opTrapInact based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_OpTrapInact_Type.__name__ = "Integer32"
_OpTrapInact_Object = MibScalar
opTrapInact = _OpTrapInact_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 3, 3),
    _OpTrapInact_Type()
)
opTrapInact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opTrapInact.setStatus("mandatory")
_Natbrg_ObjectIdentity = ObjectIdentity
natbrg = _Natbrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 86, 2, 4)
)
_LanTable_Object = MibTable
lanTable = _LanTable_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 4, 1)
)
if mibBuilder.loadTexts:
    lanTable.setStatus("mandatory")
_LanEntry_Object = MibTableRow
lanEntry = _LanEntry_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 4, 1, 1)
)
lanEntry.setIndexNames(
    (0, "NAT", "lanPhyAddr"),
)
if mibBuilder.loadTexts:
    lanEntry.setStatus("mandatory")
_LanIfIndex_Type = Integer32
_LanIfIndex_Object = MibTableColumn
lanIfIndex = _LanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 4, 1, 1, 1),
    _LanIfIndex_Type()
)
lanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanIfIndex.setStatus("mandatory")
_LanPhyAddr_Type = OctetString
_LanPhyAddr_Object = MibTableColumn
lanPhyAddr = _LanPhyAddr_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 4, 1, 1, 2),
    _LanPhyAddr_Type()
)
lanPhyAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanPhyAddr.setStatus("mandatory")
_BlanTable_Object = MibTable
blanTable = _BlanTable_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 4, 2)
)
if mibBuilder.loadTexts:
    blanTable.setStatus("mandatory")
_BlanEntry_Object = MibTableRow
blanEntry = _BlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 4, 2, 1)
)
blanEntry.setIndexNames(
    (0, "NAT", "blanIfIndex"),
    (0, "NAT", "blanOffset"),
    (0, "NAT", "blanPtrn"),
)
if mibBuilder.loadTexts:
    blanEntry.setStatus("mandatory")
_BlanIfIndex_Type = Integer32
_BlanIfIndex_Object = MibTableColumn
blanIfIndex = _BlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 4, 2, 1, 1),
    _BlanIfIndex_Type()
)
blanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blanIfIndex.setStatus("mandatory")
_BlanOffset_Type = Integer32
_BlanOffset_Object = MibTableColumn
blanOffset = _BlanOffset_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 4, 2, 1, 2),
    _BlanOffset_Type()
)
blanOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blanOffset.setStatus("mandatory")
_BlanLength_Type = Integer32
_BlanLength_Object = MibTableColumn
blanLength = _BlanLength_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 4, 2, 1, 3),
    _BlanLength_Type()
)
blanLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blanLength.setStatus("mandatory")
_BlanPtrn_Type = OctetString
_BlanPtrn_Object = MibTableColumn
blanPtrn = _BlanPtrn_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 4, 2, 1, 4),
    _BlanPtrn_Type()
)
blanPtrn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blanPtrn.setStatus("mandatory")
_PlanTable_Object = MibTable
planTable = _PlanTable_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 4, 3)
)
if mibBuilder.loadTexts:
    planTable.setStatus("mandatory")
_PlanEntry_Object = MibTableRow
planEntry = _PlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 4, 3, 1)
)
planEntry.setIndexNames(
    (0, "NAT", "planIfIndex"),
    (0, "NAT", "planOffset"),
    (0, "NAT", "planPtrn"),
)
if mibBuilder.loadTexts:
    planEntry.setStatus("mandatory")
_PlanIfIndex_Type = Integer32
_PlanIfIndex_Object = MibTableColumn
planIfIndex = _PlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 4, 3, 1, 1),
    _PlanIfIndex_Type()
)
planIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    planIfIndex.setStatus("mandatory")
_PlanOffset_Type = Integer32
_PlanOffset_Object = MibTableColumn
planOffset = _PlanOffset_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 4, 3, 1, 2),
    _PlanOffset_Type()
)
planOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    planOffset.setStatus("mandatory")
_PlanLength_Type = Integer32
_PlanLength_Object = MibTableColumn
planLength = _PlanLength_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 4, 3, 1, 3),
    _PlanLength_Type()
)
planLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    planLength.setStatus("mandatory")
_PlanPtrn_Type = OctetString
_PlanPtrn_Object = MibTableColumn
planPtrn = _PlanPtrn_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 4, 3, 1, 4),
    _PlanPtrn_Type()
)
planPtrn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    planPtrn.setStatus("mandatory")
_LanTblFlush_Type = Integer32
_LanTblFlush_Object = MibScalar
lanTblFlush = _LanTblFlush_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 4, 4),
    _LanTblFlush_Type()
)
lanTblFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanTblFlush.setStatus("mandatory")


class _BrgState_Type(Integer32):
    """Custom type brgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("backup", 1),
          ("forwarding", 2),
          ("idle", 3),
          ("init", 0),
          ("serial-handshake", 4))
    )


_BrgState_Type.__name__ = "Integer32"
_BrgState_Object = MibScalar
brgState = _BrgState_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 4, 5),
    _BrgState_Type()
)
brgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brgState.setStatus("mandatory")
_Natmtr_ObjectIdentity = ObjectIdentity
natmtr = _Natmtr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 86, 2, 5)
)
_EtypeInfo_ObjectIdentity = ObjectIdentity
etypeInfo = _EtypeInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 1)
)
_EtypeTypes_Type = Counter32
_EtypeTypes_Object = MibScalar
etypeTypes = _EtypeTypes_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 1, 1),
    _EtypeTypes_Type()
)
etypeTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etypeTypes.setStatus("mandatory")
_EtypeTable_Object = MibTable
etypeTable = _EtypeTable_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 1, 2)
)
if mibBuilder.loadTexts:
    etypeTable.setStatus("mandatory")
_EtypeTblEntry_Object = MibTableRow
etypeTblEntry = _EtypeTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 1, 2, 1)
)
etypeTblEntry.setIndexNames(
    (0, "NAT", "pysmiFakeCol6"),
)
if mibBuilder.loadTexts:
    etypeTblEntry.setStatus("mandatory")


class _EtypeEtype_Type(Integer32):
    """Custom type etypeEtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(512,
              513,
              1536,
              2048,
              2049,
              2050,
              2051,
              2052,
              2053,
              2054,
              2055,
              2076,
              2184,
              2185,
              2186,
              2304,
              2560,
              2561,
              2989,
              4096,
              4097,
              4098,
              4099,
              4100,
              4101,
              4102,
              4103,
              4104,
              4105,
              4106,
              4107,
              4108,
              4109,
              4110,
              4111,
              4660,
              5632,
              15367,
              17185,
              21000,
              24576,
              24577,
              24578,
              24579,
              24580,
              24581,
              24582,
              24583,
              24584,
              24585,
              24592,
              24593,
              24594,
              24595,
              24596,
              28672,
              28673,
              28674,
              28677,
              28679,
              28681,
              28704,
              28705,
              28706,
              28707,
              28708,
              28709,
              28710,
              28711,
              28712,
              28713,
              28720,
              32771,
              32772,
              32773,
              32774,
              32776,
              32784,
              32787,
              32788,
              32789,
              32790,
              32793,
              32814,
              32815,
              32821,
              32822,
              32824,
              32825,
              32826,
              32827,
              32828,
              32829,
              32830,
              32831,
              32832,
              32833,
              32834,
              32836,
              32838,
              32839,
              32841,
              32859,
              32860,
              32861,
              32864,
              32866,
              32869,
              32870,
              32871,
              32872,
              32873,
              32874,
              32876,
              32877,
              32878,
              32879,
              32880,
              32881,
              32882,
              32883,
              32884,
              32885,
              32886,
              32887,
              32890,
              32891,
              32892,
              32893,
              32894,
              32895,
              32896,
              32897,
              32898,
              32899,
              32923,
              32924,
              32925,
              32926,
              32927,
              32931,
              32932,
              32933,
              32934,
              32935,
              32936,
              32937,
              32938,
              32939,
              32940,
              32941,
              32942,
              32943,
              32944,
              32945,
              32946,
              32947,
              32960,
              32961,
              32962,
              32963,
              32966,
              32967,
              32968,
              32969,
              32970,
              32971,
              32972,
              32973,
              32974,
              32975,
              32976,
              32977,
              32978,
              32979,
              32980,
              32989,
              32990,
              32991,
              32992,
              32993,
              32994,
              32995,
              32996,
              32997,
              32998,
              32999,
              33000,
              33001,
              33002,
              33003,
              33004,
              33005,
              33006,
              33007,
              33008,
              33010,
              33011,
              33012,
              33013,
              33015,
              33023,
              33024,
              33025,
              33026,
              33027,
              33031,
              33032,
              33033,
              33067,
              33072,
              33073,
              33079,
              33080,
              33081,
              33082,
              33083,
              33084,
              33085,
              36864,
              36865,
              36866,
              36867,
              39321,
              65280)
        )
    )
    namedValues = NamedValues(
        *(("ab", 32992),
          ("ab-1", 32993),
          ("ab-2", 32994),
          ("ab-3", 32995),
          ("aeonic", 32822),
          ("ap-DOMAIN", 32793),
          ("apollo", 33015),
          ("apple-TSS", 33011),
          ("appletlk", 32923),
          ("applitek", 32967),
          ("atandt", 32873),
          ("atandt-1", 32776),
          ("atandt-2", 32838),
          ("atandt-3", 32839),
          ("autophon", 32874),
          ("banyan", 2989),
          ("bbn-SIMNET", 21000),
          ("bbn-VITA", 65280),
          ("berk-IP-0", 4096),
          ("berk-IP-1", 4097),
          ("berk-IP-10", 4106),
          ("berk-IP-11", 4107),
          ("berk-IP-12", 4108),
          ("berk-IP-13", 4109),
          ("berk-IP-14", 4110),
          ("berk-IP-15", 4111),
          ("berk-IP-2", 4098),
          ("berk-IP-3", 4099),
          ("berk-IP-4", 4100),
          ("berk-IP-5", 4101),
          ("berk-IP-6", 4102),
          ("berk-IP-7", 4103),
          ("berk-IP-8", 4104),
          ("berk-IP-9", 4105),
          ("brg-BRG1", 36865),
          ("brg-BRG2", 36866),
          ("brg-BRG3", 36867),
          ("cc", 32897),
          ("cc-1", 32898),
          ("cc-2", 32899),
          ("cc-3", 32866),
          ("chaosnet", 2052),
          ("comdesign", 32876),
          ("compuGraphic", 32877),
          ("cron-DIR", 32772),
          ("cron-VLN", 32771),
          ("dansk", 32891),
          ("datability", 32924),
          ("datability-1", 32925),
          ("datability-10", 33003),
          ("datability-11", 33004),
          ("datability-12", 33005),
          ("datability-13", 33006),
          ("datability-14", 33007),
          ("datability-15", 33008),
          ("datability-2", 32926),
          ("datability-3", 32996),
          ("datability-4", 32997),
          ("datability-5", 32998),
          ("datability-6", 32999),
          ("datability-7", 33000),
          ("datability-8", 33001),
          ("datability-9", 33002),
          ("dca", 32963),
          ("dca-HELLO", 32960),
          ("dca-MULTI", 4660),
          ("dca-TALK1", 32961),
          ("dca-TALK2", 32962),
          ("dec-BRIDGE", 32824),
          ("dec-C-DIAG", 24581),
          ("dec-C-LAT", 24580),
          ("dec-C-LAVC", 24583),
          ("dec-C-MOPDL", 24577),
          ("dec-C-MOPRC", 24578),
          ("dec-C-NET", 24579),
          ("dec-C-UA1", 24576),
          ("dec-C-UA13", 32834),
          ("dec-C-UA2", 24584),
          ("dec-C-UA3", 24585),
          ("dec-C-UA4", 32825),
          ("dec-C-UA5", 32826),
          ("dec-C-UA6", 32827),
          ("dec-C-UA9", 32830),
          ("dec-C-USE", 24582),
          ("dec-DNS", 32828),
          ("dec-ENCRYP", 32829),
          ("dec-LTM", 32831),
          ("dec-MS-DOS", 32833),
          ("dec-PC-ENim", 32832),
          ("dod-TCPIP", 2048),
          ("eands", 32861),
          ("ecma-IP", 2051),
          ("excelan", 32784),
          ("expertdata", 32841),
          ("gd", 32872),
          ("harris", 32973),
          ("harris-1", 32974),
          ("hp-PROBE", 32773),
          ("integraph", 32968),
          ("integraph-1", 32969),
          ("integraph-2", 32970),
          ("integraph-3", 32971),
          ("integraph-4", 32972),
          ("is", 32991),
          ("is-TRFS", 32990),
          ("kinetics", 33012),
          ("kinetics-1", 33013),
          ("kti", 33081),
          ("kti-1", 33082),
          ("kti-2", 33083),
          ("kti-3", 33084),
          ("kti-4", 33085),
          ("lg", 32878),
          ("lg-1", 32879),
          ("lg-2", 32880),
          ("lg-3", 32881),
          ("lg-4", 32882),
          ("lg-5", 32883),
          ("lg-6", 32884),
          ("lg-7", 32885),
          ("lg-8", 32886),
          ("lg-9", 32887),
          ("lm", 32864),
          ("loopback", 36864),
          ("lrt", 28704),
          ("lrt-1", 28705),
          ("lrt-2", 28706),
          ("lrt-3", 28707),
          ("lrt-4", 28708),
          ("lrt-5", 28709),
          ("lrt-6", 28710),
          ("lrt-7", 28711),
          ("lrt-8", 28712),
          ("lrt-9", 28713),
          ("matra", 32890),
          ("mrt-I-NODAL", 32892),
          ("mytype", 39321),
          ("nbp", 15367),
          ("nbs-IP", 2050),
          ("nestar", 32774),
          ("nixdorf", 32931),
          ("novell", 33079),
          ("novell-1", 33080),
          ("os9net-1", 28679),
          ("os9net-2", 28681),
          ("pacer", 32966),
          ("prc", 32836),
          ("proteon", 28720),
          ("retix", 33010),
          ("rev-ARP", 32821),
          ("rosemount", 32979),
          ("rosemount-1", 32980),
          ("sg", 32788),
          ("sg-DIAG", 32787),
          ("sg-UA", 32789),
          ("sg-XNS", 32790),
          ("siemens", 32932),
          ("siemens-1", 32933),
          ("siemens-10", 32942),
          ("siemens-11", 32943),
          ("siemens-12", 32944),
          ("siemens-13", 32945),
          ("siemens-14", 32946),
          ("siemens-15", 32947),
          ("siemens-2", 32934),
          ("siemens-3", 32935),
          ("siemens-4", 32936),
          ("siemens-5", 32937),
          ("siemens-6", 32938),
          ("siemens-7", 32939),
          ("siemens-8", 32940),
          ("siemens-9", 32941),
          ("spider", 32927),
          ("stan-ESP", 32859),
          ("stan-PRO", 32860),
          ("symbolics", 2076),
          ("symbolics-1", 33031),
          ("symbolics-2", 33032),
          ("symbolics-3", 33033),
          ("talaris", 33067),
          ("taylor", 32975),
          ("taylor-1", 32976),
          ("taylor-2", 32977),
          ("taylor-3", 32978),
          ("tcpip-ARP", 2054),
          ("thd-DIDDLE", 17185),
          ("three-COM", 24592),
          ("three-COM-1", 24593),
          ("three-COM-2", 24594),
          ("three-COM-3", 24595),
          ("three-COM-4", 24596),
          ("tigan", 32815),
          ("tymshare", 32814),
          ("um-AMH", 32869),
          ("um-AMH-1", 32870),
          ("ung-BASS1", 28673),
          ("ung-BASS2", 28674),
          ("ung-BASS5", 28677),
          ("ung-BASSO", 28672),
          ("ung-DB", 2304),
          ("valid-MH", 5632),
          ("varian", 32989),
          ("veeco", 32871),
          ("vg", 33073),
          ("vit-B-MAN", 32896),
          ("vitalink", 32893),
          ("vitalink-1", 32894),
          ("vitalink-2", 32895),
          ("waterloo", 33072),
          ("wellfleet", 33023),
          ("wellfleet-1", 33024),
          ("wellfleet-2", 33025),
          ("wellfleet-3", 33026),
          ("wellfleet-4", 33027),
          ("xdot25-LEV3", 2053),
          ("xdot75-IP", 2049),
          ("xns-IDP", 1536),
          ("xrx-PUP", 512),
          ("xrx-PUP2", 2560),
          ("xrx-PUPAT2", 2561),
          ("xrx-PUPUT", 513),
          ("xrx-XNS", 2055),
          ("xyplex", 2184),
          ("xyplex-1", 2185),
          ("xyplex-2", 2186))
    )


_EtypeEtype_Type.__name__ = "Integer32"
_EtypeEtype_Object = MibTableColumn
etypeEtype = _EtypeEtype_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 1, 2, 1, 1),
    _EtypeEtype_Type()
)
etypeEtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etypeEtype.setStatus("mandatory")
_EtypePkts_Type = Counter32
_EtypePkts_Object = MibTableColumn
etypePkts = _EtypePkts_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 1, 2, 1, 2),
    _EtypePkts_Type()
)
etypePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etypePkts.setStatus("mandatory")
_PysmiFakeCol6_Type = Integer32
_PysmiFakeCol6_Object = MibTableColumn
pysmiFakeCol6 = _PysmiFakeCol6_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 1, 2, 1, 4294967295),
    _PysmiFakeCol6_Type()
)
pysmiFakeCol6.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol6.setStatus("mandatory")
_EtypeOtherTypes_Type = Counter32
_EtypeOtherTypes_Object = MibScalar
etypeOtherTypes = _EtypeOtherTypes_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 1, 3),
    _EtypeOtherTypes_Type()
)
etypeOtherTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etypeOtherTypes.setStatus("mandatory")
_PeakInfo_ObjectIdentity = ObjectIdentity
peakInfo = _PeakInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2)
)
_PeakReset_Type = Integer32
_PeakReset_Object = MibScalar
peakReset = _PeakReset_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 1),
    _PeakReset_Type()
)
peakReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    peakReset.setStatus("mandatory")
_PeakResetTime_Type = TimeTicks
_PeakResetTime_Object = MibScalar
peakResetTime = _PeakResetTime_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 2),
    _PeakResetTime_Type()
)
peakResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakResetTime.setStatus("mandatory")
_PeakSmplIntv_Type = Integer32
_PeakSmplIntv_Object = MibScalar
peakSmplIntv = _PeakSmplIntv_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 3),
    _PeakSmplIntv_Type()
)
peakSmplIntv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    peakSmplIntv.setStatus("mandatory")
_PeakData_ObjectIdentity = ObjectIdentity
peakData = _PeakData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 4)
)
_PeakFrameInfo_ObjectIdentity = ObjectIdentity
peakFrameInfo = _PeakFrameInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 4, 1)
)
_PeakFramePkts_Type = Counter32
_PeakFramePkts_Object = MibScalar
peakFramePkts = _PeakFramePkts_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 4, 1, 1),
    _PeakFramePkts_Type()
)
peakFramePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakFramePkts.setStatus("mandatory")
_PeakFrameTime_Type = TimeTicks
_PeakFrameTime_Object = MibScalar
peakFrameTime = _PeakFrameTime_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 4, 1, 2),
    _PeakFrameTime_Type()
)
peakFrameTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakFrameTime.setStatus("mandatory")
_PeakFrameErrors_Type = Counter32
_PeakFrameErrors_Object = MibScalar
peakFrameErrors = _PeakFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 4, 1, 3),
    _PeakFrameErrors_Type()
)
peakFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakFrameErrors.setStatus("mandatory")
_PeakKbyteInfo_ObjectIdentity = ObjectIdentity
peakKbyteInfo = _PeakKbyteInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 4, 2)
)
_PeakKbytes_Type = Counter32
_PeakKbytes_Object = MibScalar
peakKbytes = _PeakKbytes_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 4, 2, 1),
    _PeakKbytes_Type()
)
peakKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakKbytes.setStatus("mandatory")
_PeakKbyteTime_Type = TimeTicks
_PeakKbyteTime_Object = MibScalar
peakKbyteTime = _PeakKbyteTime_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 4, 2, 2),
    _PeakKbyteTime_Type()
)
peakKbyteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakKbyteTime.setStatus("mandatory")
_PeakKbyteTotalPkts_Type = Counter32
_PeakKbyteTotalPkts_Object = MibScalar
peakKbyteTotalPkts = _PeakKbyteTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 4, 2, 3),
    _PeakKbyteTotalPkts_Type()
)
peakKbyteTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakKbyteTotalPkts.setStatus("mandatory")
_PeakKbyteErrors_Type = Counter32
_PeakKbyteErrors_Object = MibScalar
peakKbyteErrors = _PeakKbyteErrors_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 4, 2, 4),
    _PeakKbyteErrors_Type()
)
peakKbyteErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakKbyteErrors.setStatus("mandatory")
_PeakBcastInfo_ObjectIdentity = ObjectIdentity
peakBcastInfo = _PeakBcastInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 4, 3)
)
_PeakBcastPkts_Type = Counter32
_PeakBcastPkts_Object = MibScalar
peakBcastPkts = _PeakBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 4, 3, 1),
    _PeakBcastPkts_Type()
)
peakBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakBcastPkts.setStatus("mandatory")
_PeakBcastTime_Type = TimeTicks
_PeakBcastTime_Object = MibScalar
peakBcastTime = _PeakBcastTime_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 4, 3, 2),
    _PeakBcastTime_Type()
)
peakBcastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakBcastTime.setStatus("mandatory")
_PeakBcastTotalPkts_Type = Counter32
_PeakBcastTotalPkts_Object = MibScalar
peakBcastTotalPkts = _PeakBcastTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 4, 3, 3),
    _PeakBcastTotalPkts_Type()
)
peakBcastTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakBcastTotalPkts.setStatus("mandatory")
_PeakBcastErrors_Type = Counter32
_PeakBcastErrors_Object = MibScalar
peakBcastErrors = _PeakBcastErrors_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 4, 3, 4),
    _PeakBcastErrors_Type()
)
peakBcastErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakBcastErrors.setStatus("mandatory")
_PeakMcastInfo_ObjectIdentity = ObjectIdentity
peakMcastInfo = _PeakMcastInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 4, 4)
)
_PeakMcastPkts_Type = Counter32
_PeakMcastPkts_Object = MibScalar
peakMcastPkts = _PeakMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 4, 4, 1),
    _PeakMcastPkts_Type()
)
peakMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakMcastPkts.setStatus("mandatory")
_PeakMcastTime_Type = TimeTicks
_PeakMcastTime_Object = MibScalar
peakMcastTime = _PeakMcastTime_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 4, 4, 2),
    _PeakMcastTime_Type()
)
peakMcastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakMcastTime.setStatus("mandatory")
_PeakMcastTotalPkts_Type = Counter32
_PeakMcastTotalPkts_Object = MibScalar
peakMcastTotalPkts = _PeakMcastTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 4, 4, 3),
    _PeakMcastTotalPkts_Type()
)
peakMcastTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakMcastTotalPkts.setStatus("mandatory")
_PeakMcastErrors_Type = Counter32
_PeakMcastErrors_Object = MibScalar
peakMcastErrors = _PeakMcastErrors_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 4, 4, 4),
    _PeakMcastErrors_Type()
)
peakMcastErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakMcastErrors.setStatus("mandatory")
_PeakErrInfo_ObjectIdentity = ObjectIdentity
peakErrInfo = _PeakErrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 4, 5)
)
_PeakErrErrors_Type = Counter32
_PeakErrErrors_Object = MibScalar
peakErrErrors = _PeakErrErrors_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 4, 5, 1),
    _PeakErrErrors_Type()
)
peakErrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakErrErrors.setStatus("mandatory")
_PeakErrTime_Type = TimeTicks
_PeakErrTime_Object = MibScalar
peakErrTime = _PeakErrTime_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 4, 5, 2),
    _PeakErrTime_Type()
)
peakErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakErrTime.setStatus("mandatory")
_PeakErrTotalPkts_Type = Counter32
_PeakErrTotalPkts_Object = MibScalar
peakErrTotalPkts = _PeakErrTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 4, 5, 3),
    _PeakErrTotalPkts_Type()
)
peakErrTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakErrTotalPkts.setStatus("mandatory")
_PeakErrCrcs_Type = Counter32
_PeakErrCrcs_Object = MibScalar
peakErrCrcs = _PeakErrCrcs_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 4, 5, 4),
    _PeakErrCrcs_Type()
)
peakErrCrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakErrCrcs.setStatus("mandatory")
_PeakErrAlgns_Type = Counter32
_PeakErrAlgns_Object = MibScalar
peakErrAlgns = _PeakErrAlgns_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 4, 5, 5),
    _PeakErrAlgns_Type()
)
peakErrAlgns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakErrAlgns.setStatus("mandatory")
_PeakErrXmtColls_Type = Counter32
_PeakErrXmtColls_Object = MibScalar
peakErrXmtColls = _PeakErrXmtColls_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 4, 5, 6),
    _PeakErrXmtColls_Type()
)
peakErrXmtColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakErrXmtColls.setStatus("mandatory")
_PeakErrShorts_Type = Counter32
_PeakErrShorts_Object = MibScalar
peakErrShorts = _PeakErrShorts_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 4, 5, 7),
    _PeakErrShorts_Type()
)
peakErrShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakErrShorts.setStatus("mandatory")
_PeakErrOvsizes_Type = Counter32
_PeakErrOvsizes_Object = MibScalar
peakErrOvsizes = _PeakErrOvsizes_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 4, 5, 8),
    _PeakErrOvsizes_Type()
)
peakErrOvsizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakErrOvsizes.setStatus("mandatory")
_PeakUtilInfo_ObjectIdentity = ObjectIdentity
peakUtilInfo = _PeakUtilInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 4, 6)
)
_PeakUtilVal_Type = Integer32
_PeakUtilVal_Object = MibScalar
peakUtilVal = _PeakUtilVal_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 4, 6, 1),
    _PeakUtilVal_Type()
)
peakUtilVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakUtilVal.setStatus("mandatory")
_PeakUtilTime_Type = TimeTicks
_PeakUtilTime_Object = MibScalar
peakUtilTime = _PeakUtilTime_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 4, 6, 2),
    _PeakUtilTime_Type()
)
peakUtilTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakUtilTime.setStatus("mandatory")
_PeakUtilTotalPkts_Type = Counter32
_PeakUtilTotalPkts_Object = MibScalar
peakUtilTotalPkts = _PeakUtilTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 4, 6, 3),
    _PeakUtilTotalPkts_Type()
)
peakUtilTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakUtilTotalPkts.setStatus("mandatory")
_PeakUtilErrors_Type = Counter32
_PeakUtilErrors_Object = MibScalar
peakUtilErrors = _PeakUtilErrors_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 2, 4, 6, 4),
    _PeakUtilErrors_Type()
)
peakUtilErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakUtilErrors.setStatus("mandatory")
_Top10Info_ObjectIdentity = ObjectIdentity
top10Info = _Top10Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 3)
)


class _Top10Enable_Type(Integer32):
    """Custom type top10Enable based on Integer32"""
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
        *(("ethernetbroadcasterON", 7),
          ("ethernetlistenerON", 3),
          ("ethernetpairON", 5),
          ("ethernettalkerON", 1),
          ("iplistenerON", 4),
          ("ippairON", 6),
          ("iptalkerON", 2),
          ("off", 0))
    )


_Top10Enable_Type.__name__ = "Integer32"
_Top10Enable_Object = MibScalar
top10Enable = _Top10Enable_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 3, 1),
    _Top10Enable_Type()
)
top10Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    top10Enable.setStatus("mandatory")
_Top10ThresholdVal_Type = Integer32
_Top10ThresholdVal_Object = MibScalar
top10ThresholdVal = _Top10ThresholdVal_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 3, 2),
    _Top10ThresholdVal_Type()
)
top10ThresholdVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    top10ThresholdVal.setStatus("mandatory")
_Top10SmplIntv_Type = Integer32
_Top10SmplIntv_Object = MibScalar
top10SmplIntv = _Top10SmplIntv_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 3, 3),
    _Top10SmplIntv_Type()
)
top10SmplIntv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    top10SmplIntv.setStatus("mandatory")
_Top10SeqNum_Type = Integer32
_Top10SeqNum_Object = MibScalar
top10SeqNum = _Top10SeqNum_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 3, 4),
    _Top10SeqNum_Type()
)
top10SeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    top10SeqNum.setStatus("mandatory")
_Top10SmplTime_Type = TimeTicks
_Top10SmplTime_Object = MibScalar
top10SmplTime = _Top10SmplTime_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 3, 5),
    _Top10SmplTime_Type()
)
top10SmplTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    top10SmplTime.setStatus("mandatory")
_Top10TotalEntries_Type = Counter32
_Top10TotalEntries_Object = MibScalar
top10TotalEntries = _Top10TotalEntries_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 3, 6),
    _Top10TotalEntries_Type()
)
top10TotalEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    top10TotalEntries.setStatus("mandatory")
_Top10Ovflow_Type = Integer32
_Top10Ovflow_Object = MibScalar
top10Ovflow = _Top10Ovflow_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 3, 7),
    _Top10Ovflow_Type()
)
top10Ovflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    top10Ovflow.setStatus("mandatory")
_Top10TotalPkts_Type = Counter32
_Top10TotalPkts_Object = MibScalar
top10TotalPkts = _Top10TotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 3, 8),
    _Top10TotalPkts_Type()
)
top10TotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    top10TotalPkts.setStatus("mandatory")
_Top10MatchedPkts_Type = Counter32
_Top10MatchedPkts_Object = MibScalar
top10MatchedPkts = _Top10MatchedPkts_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 3, 9),
    _Top10MatchedPkts_Type()
)
top10MatchedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    top10MatchedPkts.setStatus("mandatory")
_Top10ValidEntries_Type = Counter32
_Top10ValidEntries_Object = MibScalar
top10ValidEntries = _Top10ValidEntries_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 3, 10),
    _Top10ValidEntries_Type()
)
top10ValidEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    top10ValidEntries.setStatus("mandatory")
_Top10Data_ObjectIdentity = ObjectIdentity
top10Data = _Top10Data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 3, 11)
)
_Top10StrID_Type = OctetString
_Top10StrID_Object = MibScalar
top10StrID = _Top10StrID_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 3, 11, 1),
    _Top10StrID_Type()
)
top10StrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    top10StrID.setStatus("mandatory")
_Top10Pkts_Type = Counter32
_Top10Pkts_Object = MibScalar
top10Pkts = _Top10Pkts_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 5, 3, 11, 2),
    _Top10Pkts_Type()
)
top10Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    top10Pkts.setStatus("mandatory")
_Natalert_ObjectIdentity = ObjectIdentity
natalert = _Natalert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 86, 2, 6)
)
_AlertParms_ObjectIdentity = ObjectIdentity
alertParms = _AlertParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 1)
)
_AlertTypes_Type = Counter32
_AlertTypes_Object = MibScalar
alertTypes = _AlertTypes_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 1, 1),
    _AlertTypes_Type()
)
alertTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertTypes.setStatus("mandatory")
_AlertSmplIntv_Type = Integer32
_AlertSmplIntv_Object = MibScalar
alertSmplIntv = _AlertSmplIntv_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 1, 2),
    _AlertSmplIntv_Type()
)
alertSmplIntv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertSmplIntv.setStatus("mandatory")
_AlertReset_Type = Integer32
_AlertReset_Object = MibScalar
alertReset = _AlertReset_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 1, 3),
    _AlertReset_Type()
)
alertReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertReset.setStatus("mandatory")
_AlertResetTime_Type = TimeTicks
_AlertResetTime_Object = MibScalar
alertResetTime = _AlertResetTime_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 1, 4),
    _AlertResetTime_Type()
)
alertResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertResetTime.setStatus("mandatory")
_Alerts_ObjectIdentity = ObjectIdentity
alerts = _Alerts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2)
)
_AlertFrameInfo_ObjectIdentity = ObjectIdentity
alertFrameInfo = _AlertFrameInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 1)
)


class _AlertFrameEnable_Type(Integer32):
    """Custom type alertFrameEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_AlertFrameEnable_Type.__name__ = "Integer32"
_AlertFrameEnable_Object = MibScalar
alertFrameEnable = _AlertFrameEnable_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 1, 1),
    _AlertFrameEnable_Type()
)
alertFrameEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertFrameEnable.setStatus("mandatory")
_AlertFrameThreshold_Type = Integer32
_AlertFrameThreshold_Object = MibScalar
alertFrameThreshold = _AlertFrameThreshold_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 1, 2),
    _AlertFrameThreshold_Type()
)
alertFrameThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertFrameThreshold.setStatus("mandatory")
_AlertFramePkts_Type = Counter32
_AlertFramePkts_Object = MibScalar
alertFramePkts = _AlertFramePkts_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 1, 3),
    _AlertFramePkts_Type()
)
alertFramePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertFramePkts.setStatus("mandatory")
_AlertFrameTime_Type = TimeTicks
_AlertFrameTime_Object = MibScalar
alertFrameTime = _AlertFrameTime_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 1, 4),
    _AlertFrameTime_Type()
)
alertFrameTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertFrameTime.setStatus("mandatory")
_AlertFrameTotalPkts_Type = Counter32
_AlertFrameTotalPkts_Object = MibScalar
alertFrameTotalPkts = _AlertFrameTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 1, 5),
    _AlertFrameTotalPkts_Type()
)
alertFrameTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertFrameTotalPkts.setStatus("mandatory")
_AlertFrameErrors_Type = Counter32
_AlertFrameErrors_Object = MibScalar
alertFrameErrors = _AlertFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 1, 6),
    _AlertFrameErrors_Type()
)
alertFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertFrameErrors.setStatus("mandatory")
_AlertBcastInfo_ObjectIdentity = ObjectIdentity
alertBcastInfo = _AlertBcastInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 2)
)


class _AlertBcastEnable_Type(Integer32):
    """Custom type alertBcastEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_AlertBcastEnable_Type.__name__ = "Integer32"
_AlertBcastEnable_Object = MibScalar
alertBcastEnable = _AlertBcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 2, 1),
    _AlertBcastEnable_Type()
)
alertBcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertBcastEnable.setStatus("mandatory")
_AlertBcastThreshold_Type = Integer32
_AlertBcastThreshold_Object = MibScalar
alertBcastThreshold = _AlertBcastThreshold_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 2, 2),
    _AlertBcastThreshold_Type()
)
alertBcastThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertBcastThreshold.setStatus("mandatory")
_AlertBcastPkts_Type = Counter32
_AlertBcastPkts_Object = MibScalar
alertBcastPkts = _AlertBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 2, 3),
    _AlertBcastPkts_Type()
)
alertBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertBcastPkts.setStatus("mandatory")
_AlertBcastTime_Type = TimeTicks
_AlertBcastTime_Object = MibScalar
alertBcastTime = _AlertBcastTime_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 2, 4),
    _AlertBcastTime_Type()
)
alertBcastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertBcastTime.setStatus("mandatory")
_AlertBcastTotalPkts_Type = Counter32
_AlertBcastTotalPkts_Object = MibScalar
alertBcastTotalPkts = _AlertBcastTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 2, 5),
    _AlertBcastTotalPkts_Type()
)
alertBcastTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertBcastTotalPkts.setStatus("mandatory")
_AlertBcastErrors_Type = Counter32
_AlertBcastErrors_Object = MibScalar
alertBcastErrors = _AlertBcastErrors_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 2, 6),
    _AlertBcastErrors_Type()
)
alertBcastErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertBcastErrors.setStatus("mandatory")
_AlertMcastInfo_ObjectIdentity = ObjectIdentity
alertMcastInfo = _AlertMcastInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 3)
)


class _AlertMcastEnable_Type(Integer32):
    """Custom type alertMcastEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_AlertMcastEnable_Type.__name__ = "Integer32"
_AlertMcastEnable_Object = MibScalar
alertMcastEnable = _AlertMcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 3, 1),
    _AlertMcastEnable_Type()
)
alertMcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertMcastEnable.setStatus("mandatory")
_AlertMcastThreshold_Type = Integer32
_AlertMcastThreshold_Object = MibScalar
alertMcastThreshold = _AlertMcastThreshold_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 3, 2),
    _AlertMcastThreshold_Type()
)
alertMcastThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertMcastThreshold.setStatus("mandatory")
_AlertMcastPkts_Type = Counter32
_AlertMcastPkts_Object = MibScalar
alertMcastPkts = _AlertMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 3, 3),
    _AlertMcastPkts_Type()
)
alertMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertMcastPkts.setStatus("mandatory")
_AlertMcastTime_Type = TimeTicks
_AlertMcastTime_Object = MibScalar
alertMcastTime = _AlertMcastTime_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 3, 4),
    _AlertMcastTime_Type()
)
alertMcastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertMcastTime.setStatus("mandatory")
_AlertMcastTotalPkts_Type = Counter32
_AlertMcastTotalPkts_Object = MibScalar
alertMcastTotalPkts = _AlertMcastTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 3, 5),
    _AlertMcastTotalPkts_Type()
)
alertMcastTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertMcastTotalPkts.setStatus("mandatory")
_AlertMcastErrors_Type = Counter32
_AlertMcastErrors_Object = MibScalar
alertMcastErrors = _AlertMcastErrors_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 3, 6),
    _AlertMcastErrors_Type()
)
alertMcastErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertMcastErrors.setStatus("mandatory")
_AlertErrInfo_ObjectIdentity = ObjectIdentity
alertErrInfo = _AlertErrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 4)
)


class _AlertErrEnable_Type(Integer32):
    """Custom type alertErrEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_AlertErrEnable_Type.__name__ = "Integer32"
_AlertErrEnable_Object = MibScalar
alertErrEnable = _AlertErrEnable_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 4, 1),
    _AlertErrEnable_Type()
)
alertErrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertErrEnable.setStatus("mandatory")
_AlertErrThreshold_Type = Integer32
_AlertErrThreshold_Object = MibScalar
alertErrThreshold = _AlertErrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 4, 2),
    _AlertErrThreshold_Type()
)
alertErrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertErrThreshold.setStatus("mandatory")
_AlertErrErrors_Type = Counter32
_AlertErrErrors_Object = MibScalar
alertErrErrors = _AlertErrErrors_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 4, 3),
    _AlertErrErrors_Type()
)
alertErrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertErrErrors.setStatus("mandatory")
_AlertErrTime_Type = TimeTicks
_AlertErrTime_Object = MibScalar
alertErrTime = _AlertErrTime_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 4, 4),
    _AlertErrTime_Type()
)
alertErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertErrTime.setStatus("mandatory")
_AlertErrTotalPkts_Type = Counter32
_AlertErrTotalPkts_Object = MibScalar
alertErrTotalPkts = _AlertErrTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 4, 5),
    _AlertErrTotalPkts_Type()
)
alertErrTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertErrTotalPkts.setStatus("mandatory")
_AlertErrTotalErrors_Type = Counter32
_AlertErrTotalErrors_Object = MibScalar
alertErrTotalErrors = _AlertErrTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 4, 6),
    _AlertErrTotalErrors_Type()
)
alertErrTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertErrTotalErrors.setStatus("mandatory")
_AlertErrCrcs_Type = Counter32
_AlertErrCrcs_Object = MibScalar
alertErrCrcs = _AlertErrCrcs_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 4, 7),
    _AlertErrCrcs_Type()
)
alertErrCrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertErrCrcs.setStatus("mandatory")
_AlertErrAlgns_Type = Counter32
_AlertErrAlgns_Object = MibScalar
alertErrAlgns = _AlertErrAlgns_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 4, 8),
    _AlertErrAlgns_Type()
)
alertErrAlgns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertErrAlgns.setStatus("mandatory")
_AlertErrXmtColls_Type = Counter32
_AlertErrXmtColls_Object = MibScalar
alertErrXmtColls = _AlertErrXmtColls_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 4, 9),
    _AlertErrXmtColls_Type()
)
alertErrXmtColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertErrXmtColls.setStatus("mandatory")
_AlertErrShorts_Type = Counter32
_AlertErrShorts_Object = MibScalar
alertErrShorts = _AlertErrShorts_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 4, 10),
    _AlertErrShorts_Type()
)
alertErrShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertErrShorts.setStatus("mandatory")
_AlertErrOvsizes_Type = Counter32
_AlertErrOvsizes_Object = MibScalar
alertErrOvsizes = _AlertErrOvsizes_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 4, 11),
    _AlertErrOvsizes_Type()
)
alertErrOvsizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertErrOvsizes.setStatus("mandatory")
_AlertUtilInfo_ObjectIdentity = ObjectIdentity
alertUtilInfo = _AlertUtilInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 5)
)


class _AlertUtilEnable_Type(Integer32):
    """Custom type alertUtilEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_AlertUtilEnable_Type.__name__ = "Integer32"
_AlertUtilEnable_Object = MibScalar
alertUtilEnable = _AlertUtilEnable_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 5, 1),
    _AlertUtilEnable_Type()
)
alertUtilEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertUtilEnable.setStatus("mandatory")
_AlertUtilThreshold_Type = Integer32
_AlertUtilThreshold_Object = MibScalar
alertUtilThreshold = _AlertUtilThreshold_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 5, 2),
    _AlertUtilThreshold_Type()
)
alertUtilThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertUtilThreshold.setStatus("mandatory")
_AlertUtilValue_Type = Integer32
_AlertUtilValue_Object = MibScalar
alertUtilValue = _AlertUtilValue_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 5, 3),
    _AlertUtilValue_Type()
)
alertUtilValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertUtilValue.setStatus("mandatory")
_AlertUtilTime_Type = TimeTicks
_AlertUtilTime_Object = MibScalar
alertUtilTime = _AlertUtilTime_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 5, 4),
    _AlertUtilTime_Type()
)
alertUtilTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertUtilTime.setStatus("mandatory")
_AlertUtilTotalPkts_Type = Counter32
_AlertUtilTotalPkts_Object = MibScalar
alertUtilTotalPkts = _AlertUtilTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 5, 5),
    _AlertUtilTotalPkts_Type()
)
alertUtilTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertUtilTotalPkts.setStatus("mandatory")
_AlertUtilErrors_Type = Counter32
_AlertUtilErrors_Object = MibScalar
alertUtilErrors = _AlertUtilErrors_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 6, 2, 5, 6),
    _AlertUtilErrors_Type()
)
alertUtilErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertUtilErrors.setStatus("mandatory")
_Rmeter_ObjectIdentity = ObjectIdentity
rmeter = _Rmeter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 86, 2, 7)
)
_Rconfiguration_ObjectIdentity = ObjectIdentity
rconfiguration = _Rconfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 86, 2, 7, 1)
)
_PrTrapchannel_Type = Integer32
_PrTrapchannel_Object = MibScalar
prTrapchannel = _PrTrapchannel_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 7, 1, 1),
    _PrTrapchannel_Type()
)
prTrapchannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prTrapchannel.setStatus("mandatory")
_AuxTrapchannel_Type = Integer32
_AuxTrapchannel_Object = MibScalar
auxTrapchannel = _AuxTrapchannel_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 7, 1, 2),
    _AuxTrapchannel_Type()
)
auxTrapchannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxTrapchannel.setStatus("mandatory")
_Natrtr_ObjectIdentity = ObjectIdentity
natrtr = _Natrtr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 86, 2, 8)
)
_Rtrcfg_ObjectIdentity = ObjectIdentity
rtrcfg = _Rtrcfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 86, 2, 8, 1)
)
_RtrcfRtupdintv_Type = Integer32
_RtrcfRtupdintv_Object = MibScalar
rtrcfRtupdintv = _RtrcfRtupdintv_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 8, 1, 1),
    _RtrcfRtupdintv_Type()
)
rtrcfRtupdintv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrcfRtupdintv.setStatus("mandatory")
_RtrcfRtdownintv_Type = Integer32
_RtrcfRtdownintv_Object = MibScalar
rtrcfRtdownintv = _RtrcfRtdownintv_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 8, 1, 2),
    _RtrcfRtdownintv_Type()
)
rtrcfRtdownintv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrcfRtdownintv.setStatus("mandatory")
_RtrcfRtholdintv_Type = Integer32
_RtrcfRtholdintv_Object = MibScalar
rtrcfRtholdintv = _RtrcfRtholdintv_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 8, 1, 3),
    _RtrcfRtholdintv_Type()
)
rtrcfRtholdintv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrcfRtholdintv.setStatus("mandatory")
_RtrcfRtdropintv_Type = Integer32
_RtrcfRtdropintv_Object = MibScalar
rtrcfRtdropintv = _RtrcfRtdropintv_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 8, 1, 4),
    _RtrcfRtdropintv_Type()
)
rtrcfRtdropintv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrcfRtdropintv.setStatus("mandatory")
_RtrcfIfTable_Object = MibTable
rtrcfIfTable = _RtrcfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 8, 1, 5)
)
if mibBuilder.loadTexts:
    rtrcfIfTable.setStatus("mandatory")
_RtrcfIfEntry_Object = MibTableRow
rtrcfIfEntry = _RtrcfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 8, 1, 5, 1)
)
rtrcfIfEntry.setIndexNames(
    (0, "NAT", "pysmiFakeCol7"),
)
if mibBuilder.loadTexts:
    rtrcfIfEntry.setStatus("mandatory")


class _RtrcfProxyarp_Type(Integer32):
    """Custom type rtrcfProxyarp based on Integer32"""
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


_RtrcfProxyarp_Type.__name__ = "Integer32"
_RtrcfProxyarp_Object = MibTableColumn
rtrcfProxyarp = _RtrcfProxyarp_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 8, 1, 5, 1, 1),
    _RtrcfProxyarp_Type()
)
rtrcfProxyarp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrcfProxyarp.setStatus("mandatory")


class _RtrcfIcmp_Type(Integer32):
    """Custom type rtrcfIcmp based on Integer32"""
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


_RtrcfIcmp_Type.__name__ = "Integer32"
_RtrcfIcmp_Object = MibTableColumn
rtrcfIcmp = _RtrcfIcmp_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 8, 1, 5, 1, 2),
    _RtrcfIcmp_Type()
)
rtrcfIcmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrcfIcmp.setStatus("mandatory")
_RtrcfHelperAddr_Type = IpAddress
_RtrcfHelperAddr_Object = MibTableColumn
rtrcfHelperAddr = _RtrcfHelperAddr_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 8, 1, 5, 1, 3),
    _RtrcfHelperAddr_Type()
)
rtrcfHelperAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrcfHelperAddr.setStatus("mandatory")
_RtrcfBcastAddr_Type = IpAddress
_RtrcfBcastAddr_Object = MibTableColumn
rtrcfBcastAddr = _RtrcfBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 8, 1, 5, 1, 4),
    _RtrcfBcastAddr_Type()
)
rtrcfBcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrcfBcastAddr.setStatus("mandatory")
_PysmiFakeCol7_Type = Integer32
_PysmiFakeCol7_Object = MibTableColumn
pysmiFakeCol7 = _PysmiFakeCol7_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 8, 1, 5, 1, 4294967295),
    _PysmiFakeCol7_Type()
)
pysmiFakeCol7.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol7.setStatus("mandatory")
_RtrcfStatRtTbl_Object = MibTable
rtrcfStatRtTbl = _RtrcfStatRtTbl_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 8, 1, 6)
)
if mibBuilder.loadTexts:
    rtrcfStatRtTbl.setStatus("mandatory")
_RtrcfStatRtEntry_Object = MibTableRow
rtrcfStatRtEntry = _RtrcfStatRtEntry_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 8, 1, 6, 1)
)
rtrcfStatRtEntry.setIndexNames(
    (0, "NAT", "rtrcfStatRtRoute"),
)
if mibBuilder.loadTexts:
    rtrcfStatRtEntry.setStatus("mandatory")
_RtrcfStatRtRoute_Type = IpAddress
_RtrcfStatRtRoute_Object = MibTableColumn
rtrcfStatRtRoute = _RtrcfStatRtRoute_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 8, 1, 6, 1, 1),
    _RtrcfStatRtRoute_Type()
)
rtrcfStatRtRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrcfStatRtRoute.setStatus("mandatory")
_RtrcfStatRtRouter_Type = IpAddress
_RtrcfStatRtRouter_Object = MibTableColumn
rtrcfStatRtRouter = _RtrcfStatRtRouter_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 8, 1, 6, 1, 2),
    _RtrcfStatRtRouter_Type()
)
rtrcfStatRtRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrcfStatRtRouter.setStatus("mandatory")
_RtrcfStatRtMetric_Type = Integer32
_RtrcfStatRtMetric_Object = MibTableColumn
rtrcfStatRtMetric = _RtrcfStatRtMetric_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 8, 1, 6, 1, 3),
    _RtrcfStatRtMetric_Type()
)
rtrcfStatRtMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrcfStatRtMetric.setStatus("mandatory")
_RtrrtInFltrTbl_Object = MibTable
rtrrtInFltrTbl = _RtrrtInFltrTbl_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 8, 3)
)
if mibBuilder.loadTexts:
    rtrrtInFltrTbl.setStatus("mandatory")
_RtrrtInFltrEntry_Object = MibTableRow
rtrrtInFltrEntry = _RtrrtInFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 8, 3, 1)
)
rtrrtInFltrEntry.setIndexNames(
    (0, "NAT", "rtrrtInFltrInf"),
    (0, "NAT", "rtrrtInFltrAddr"),
    (0, "NAT", "rtrrtInFltrMask"),
)
if mibBuilder.loadTexts:
    rtrrtInFltrEntry.setStatus("mandatory")
_RtrrtInFltrInf_Type = Integer32
_RtrrtInFltrInf_Object = MibTableColumn
rtrrtInFltrInf = _RtrrtInFltrInf_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 8, 3, 1, 1),
    _RtrrtInFltrInf_Type()
)
rtrrtInFltrInf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrrtInFltrInf.setStatus("mandatory")
_RtrrtInFltrAddr_Type = IpAddress
_RtrrtInFltrAddr_Object = MibTableColumn
rtrrtInFltrAddr = _RtrrtInFltrAddr_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 8, 3, 1, 2),
    _RtrrtInFltrAddr_Type()
)
rtrrtInFltrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrrtInFltrAddr.setStatus("mandatory")
_RtrrtInFltrMask_Type = IpAddress
_RtrrtInFltrMask_Object = MibTableColumn
rtrrtInFltrMask = _RtrrtInFltrMask_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 8, 3, 1, 3),
    _RtrrtInFltrMask_Type()
)
rtrrtInFltrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrrtInFltrMask.setStatus("mandatory")
_RtrrtInFltrFlag_Type = Integer32
_RtrrtInFltrFlag_Object = MibTableColumn
rtrrtInFltrFlag = _RtrrtInFltrFlag_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 8, 3, 1, 4),
    _RtrrtInFltrFlag_Type()
)
rtrrtInFltrFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrrtInFltrFlag.setStatus("mandatory")
_RtrrtOutFltrTbl_Object = MibTable
rtrrtOutFltrTbl = _RtrrtOutFltrTbl_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 8, 4)
)
if mibBuilder.loadTexts:
    rtrrtOutFltrTbl.setStatus("mandatory")
_RtrrtOutFltrEntry_Object = MibTableRow
rtrrtOutFltrEntry = _RtrrtOutFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 8, 4, 1)
)
rtrrtOutFltrEntry.setIndexNames(
    (0, "NAT", "rtrrtOutFltrInf"),
    (0, "NAT", "rtrrtOutFltrAddr"),
    (0, "NAT", "rtrrtOutFltrMask"),
)
if mibBuilder.loadTexts:
    rtrrtOutFltrEntry.setStatus("mandatory")
_RtrrtOutFltrInf_Type = Integer32
_RtrrtOutFltrInf_Object = MibTableColumn
rtrrtOutFltrInf = _RtrrtOutFltrInf_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 8, 4, 1, 1),
    _RtrrtOutFltrInf_Type()
)
rtrrtOutFltrInf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrrtOutFltrInf.setStatus("mandatory")
_RtrrtOutFltrAddr_Type = IpAddress
_RtrrtOutFltrAddr_Object = MibTableColumn
rtrrtOutFltrAddr = _RtrrtOutFltrAddr_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 8, 4, 1, 2),
    _RtrrtOutFltrAddr_Type()
)
rtrrtOutFltrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrrtOutFltrAddr.setStatus("mandatory")
_RtrrtOutFltrMask_Type = IpAddress
_RtrrtOutFltrMask_Object = MibTableColumn
rtrrtOutFltrMask = _RtrrtOutFltrMask_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 8, 4, 1, 3),
    _RtrrtOutFltrMask_Type()
)
rtrrtOutFltrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrrtOutFltrMask.setStatus("mandatory")
_RtrrtOutFltrFlag_Type = Integer32
_RtrrtOutFltrFlag_Object = MibTableColumn
rtrrtOutFltrFlag = _RtrrtOutFltrFlag_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 8, 4, 1, 4),
    _RtrrtOutFltrFlag_Type()
)
rtrrtOutFltrFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrrtOutFltrFlag.setStatus("mandatory")
_Dialup_ObjectIdentity = ObjectIdentity
dialup = _Dialup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 86, 2, 9)
)
_Phonenum_Type = OctetString
_Phonenum_Object = MibScalar
phonenum = _Phonenum_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 9, 1),
    _Phonenum_Type()
)
phonenum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phonenum.setStatus("mandatory")
_ModemInitstr_Type = OctetString
_ModemInitstr_Object = MibScalar
modemInitstr = _ModemInitstr_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 9, 2),
    _ModemInitstr_Type()
)
modemInitstr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemInitstr.setStatus("mandatory")
_ModemDialprefix_Type = OctetString
_ModemDialprefix_Object = MibScalar
modemDialprefix = _ModemDialprefix_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 9, 3),
    _ModemDialprefix_Type()
)
modemDialprefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemDialprefix.setStatus("mandatory")
_ModemDialsuffix_Type = OctetString
_ModemDialsuffix_Object = MibScalar
modemDialsuffix = _ModemDialsuffix_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 9, 4),
    _ModemDialsuffix_Type()
)
modemDialsuffix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemDialsuffix.setStatus("mandatory")
_ModemHangupprefix_Type = OctetString
_ModemHangupprefix_Object = MibScalar
modemHangupprefix = _ModemHangupprefix_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 9, 5),
    _ModemHangupprefix_Type()
)
modemHangupprefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemHangupprefix.setStatus("mandatory")
_ModemHangupsuffix_Type = OctetString
_ModemHangupsuffix_Object = MibScalar
modemHangupsuffix = _ModemHangupsuffix_Object(
    (1, 3, 6, 1, 4, 1, 86, 2, 9, 6),
    _ModemHangupsuffix_Type()
)
modemHangupsuffix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemHangupsuffix.setStatus("mandatory")
_Trapinfo_ObjectIdentity = ObjectIdentity
trapinfo = _Trapinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 86, 8)
)
_TrapSrcAddr_Type = IpAddress
_TrapSrcAddr_Object = MibScalar
trapSrcAddr = _TrapSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 86, 8, 1),
    _TrapSrcAddr_Type()
)
trapSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSrcAddr.setStatus("mandatory")
_TrapErrMsg_Type = OctetString
_TrapErrMsg_Object = MibScalar
trapErrMsg = _TrapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 86, 8, 2),
    _TrapErrMsg_Type()
)
trapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapErrMsg.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NAT",
    **{"nat": nat,
       "products": products,
       "natmib": natmib,
       "configuration": configuration,
       "cfFirmware": cfFirmware,
       "cfCmstrTable": cfCmstrTable,
       "cfCmstrEntry": cfCmstrEntry,
       "cfCmstrReadPublic": cfCmstrReadPublic,
       "cfCmstrReadEnterprise": cfCmstrReadEnterprise,
       "cfCmstrReadTrap": cfCmstrReadTrap,
       "cfCmstrReadWrite": cfCmstrReadWrite,
       "pysmiFakeCol1": pysmiFakeCol1,
       "cfCmstrAliasTable": cfCmstrAliasTable,
       "cfCmstrAliasEntry": cfCmstrAliasEntry,
       "cfCmstrAliasReadPublic": cfCmstrAliasReadPublic,
       "cfCmstrAliasReadEnterprise": cfCmstrAliasReadEnterprise,
       "cfCmstrAliasReadTrap": cfCmstrAliasReadTrap,
       "cfCmstrAliasReadWrite": cfCmstrAliasReadWrite,
       "pysmiFakeCol2": pysmiFakeCol2,
       "cfAcchostTable": cfAcchostTable,
       "cfAcchostEntry": cfAcchostEntry,
       "cfAcchostHostIP": cfAcchostHostIP,
       "cfAcchostLevel": cfAcchostLevel,
       "pysmiFakeCol3": pysmiFakeCol3,
       "cfDenyReadPublic": cfDenyReadPublic,
       "cfDevIPAddr": cfDevIPAddr,
       "cfSubnetMask": cfSubnetMask,
       "cfAcchostCfgTable": cfAcchostCfgTable,
       "cfAcchostCfgEntry": cfAcchostCfgEntry,
       "cfAcchostCfgAcclvl": cfAcchostCfgAcclvl,
       "pysmiFakeCol4": pysmiFakeCol4,
       "cfParmsSave": cfParmsSave,
       "cfPassword": cfPassword,
       "cfIPAddr2": cfIPAddr2,
       "cfSubnetMask2": cfSubnetMask2,
       "natinf": natinf,
       "statsTable": statsTable,
       "statsEntry": statsEntry,
       "statsReset": statsReset,
       "statsResetTime": statsResetTime,
       "statsRcvpkts": statsRcvpkts,
       "statsFwdpkts": statsFwdpkts,
       "statsBufOvflows": statsBufOvflows,
       "statsCrcs": statsCrcs,
       "statsAlgns": statsAlgns,
       "statsCntlOvflows": statsCntlOvflows,
       "statsXmtColls": statsXmtColls,
       "statsBlkDiscards": statsBlkDiscards,
       "statsPassDiscards": statsPassDiscards,
       "statsFwdMultiPkts": statsFwdMultiPkts,
       "statsKbytes": statsKbytes,
       "statsBcastPkts": statsBcastPkts,
       "statsMcastPkts": statsMcastPkts,
       "statsSize64-127Pkts": statsSize64_127Pkts,
       "statsSize128-255Pkts": statsSize128_255Pkts,
       "statsSize256-511Pkts": statsSize256_511Pkts,
       "statsSize512-1023Pkts": statsSize512_1023Pkts,
       "statsSize1024-1518Pkts": statsSize1024_1518Pkts,
       "statsShortPkts": statsShortPkts,
       "statsOvsizePkts": statsOvsizePkts,
       "pysmiFakeCol5": pysmiFakeCol5,
       "natopr": natopr,
       "opSysReset": opSysReset,
       "opNoStatColl": opNoStatColl,
       "opTrapInact": opTrapInact,
       "natbrg": natbrg,
       "lanTable": lanTable,
       "lanEntry": lanEntry,
       "lanIfIndex": lanIfIndex,
       "lanPhyAddr": lanPhyAddr,
       "blanTable": blanTable,
       "blanEntry": blanEntry,
       "blanIfIndex": blanIfIndex,
       "blanOffset": blanOffset,
       "blanLength": blanLength,
       "blanPtrn": blanPtrn,
       "planTable": planTable,
       "planEntry": planEntry,
       "planIfIndex": planIfIndex,
       "planOffset": planOffset,
       "planLength": planLength,
       "planPtrn": planPtrn,
       "lanTblFlush": lanTblFlush,
       "brgState": brgState,
       "natmtr": natmtr,
       "etypeInfo": etypeInfo,
       "etypeTypes": etypeTypes,
       "etypeTable": etypeTable,
       "etypeTblEntry": etypeTblEntry,
       "etypeEtype": etypeEtype,
       "etypePkts": etypePkts,
       "pysmiFakeCol6": pysmiFakeCol6,
       "etypeOtherTypes": etypeOtherTypes,
       "peakInfo": peakInfo,
       "peakReset": peakReset,
       "peakResetTime": peakResetTime,
       "peakSmplIntv": peakSmplIntv,
       "peakData": peakData,
       "peakFrameInfo": peakFrameInfo,
       "peakFramePkts": peakFramePkts,
       "peakFrameTime": peakFrameTime,
       "peakFrameErrors": peakFrameErrors,
       "peakKbyteInfo": peakKbyteInfo,
       "peakKbytes": peakKbytes,
       "peakKbyteTime": peakKbyteTime,
       "peakKbyteTotalPkts": peakKbyteTotalPkts,
       "peakKbyteErrors": peakKbyteErrors,
       "peakBcastInfo": peakBcastInfo,
       "peakBcastPkts": peakBcastPkts,
       "peakBcastTime": peakBcastTime,
       "peakBcastTotalPkts": peakBcastTotalPkts,
       "peakBcastErrors": peakBcastErrors,
       "peakMcastInfo": peakMcastInfo,
       "peakMcastPkts": peakMcastPkts,
       "peakMcastTime": peakMcastTime,
       "peakMcastTotalPkts": peakMcastTotalPkts,
       "peakMcastErrors": peakMcastErrors,
       "peakErrInfo": peakErrInfo,
       "peakErrErrors": peakErrErrors,
       "peakErrTime": peakErrTime,
       "peakErrTotalPkts": peakErrTotalPkts,
       "peakErrCrcs": peakErrCrcs,
       "peakErrAlgns": peakErrAlgns,
       "peakErrXmtColls": peakErrXmtColls,
       "peakErrShorts": peakErrShorts,
       "peakErrOvsizes": peakErrOvsizes,
       "peakUtilInfo": peakUtilInfo,
       "peakUtilVal": peakUtilVal,
       "peakUtilTime": peakUtilTime,
       "peakUtilTotalPkts": peakUtilTotalPkts,
       "peakUtilErrors": peakUtilErrors,
       "top10Info": top10Info,
       "top10Enable": top10Enable,
       "top10ThresholdVal": top10ThresholdVal,
       "top10SmplIntv": top10SmplIntv,
       "top10SeqNum": top10SeqNum,
       "top10SmplTime": top10SmplTime,
       "top10TotalEntries": top10TotalEntries,
       "top10Ovflow": top10Ovflow,
       "top10TotalPkts": top10TotalPkts,
       "top10MatchedPkts": top10MatchedPkts,
       "top10ValidEntries": top10ValidEntries,
       "top10Data": top10Data,
       "top10StrID": top10StrID,
       "top10Pkts": top10Pkts,
       "natalert": natalert,
       "alertParms": alertParms,
       "alertTypes": alertTypes,
       "alertSmplIntv": alertSmplIntv,
       "alertReset": alertReset,
       "alertResetTime": alertResetTime,
       "alerts": alerts,
       "alertFrameInfo": alertFrameInfo,
       "alertFrameEnable": alertFrameEnable,
       "alertFrameThreshold": alertFrameThreshold,
       "alertFramePkts": alertFramePkts,
       "alertFrameTime": alertFrameTime,
       "alertFrameTotalPkts": alertFrameTotalPkts,
       "alertFrameErrors": alertFrameErrors,
       "alertBcastInfo": alertBcastInfo,
       "alertBcastEnable": alertBcastEnable,
       "alertBcastThreshold": alertBcastThreshold,
       "alertBcastPkts": alertBcastPkts,
       "alertBcastTime": alertBcastTime,
       "alertBcastTotalPkts": alertBcastTotalPkts,
       "alertBcastErrors": alertBcastErrors,
       "alertMcastInfo": alertMcastInfo,
       "alertMcastEnable": alertMcastEnable,
       "alertMcastThreshold": alertMcastThreshold,
       "alertMcastPkts": alertMcastPkts,
       "alertMcastTime": alertMcastTime,
       "alertMcastTotalPkts": alertMcastTotalPkts,
       "alertMcastErrors": alertMcastErrors,
       "alertErrInfo": alertErrInfo,
       "alertErrEnable": alertErrEnable,
       "alertErrThreshold": alertErrThreshold,
       "alertErrErrors": alertErrErrors,
       "alertErrTime": alertErrTime,
       "alertErrTotalPkts": alertErrTotalPkts,
       "alertErrTotalErrors": alertErrTotalErrors,
       "alertErrCrcs": alertErrCrcs,
       "alertErrAlgns": alertErrAlgns,
       "alertErrXmtColls": alertErrXmtColls,
       "alertErrShorts": alertErrShorts,
       "alertErrOvsizes": alertErrOvsizes,
       "alertUtilInfo": alertUtilInfo,
       "alertUtilEnable": alertUtilEnable,
       "alertUtilThreshold": alertUtilThreshold,
       "alertUtilValue": alertUtilValue,
       "alertUtilTime": alertUtilTime,
       "alertUtilTotalPkts": alertUtilTotalPkts,
       "alertUtilErrors": alertUtilErrors,
       "rmeter": rmeter,
       "rconfiguration": rconfiguration,
       "prTrapchannel": prTrapchannel,
       "auxTrapchannel": auxTrapchannel,
       "natrtr": natrtr,
       "rtrcfg": rtrcfg,
       "rtrcfRtupdintv": rtrcfRtupdintv,
       "rtrcfRtdownintv": rtrcfRtdownintv,
       "rtrcfRtholdintv": rtrcfRtholdintv,
       "rtrcfRtdropintv": rtrcfRtdropintv,
       "rtrcfIfTable": rtrcfIfTable,
       "rtrcfIfEntry": rtrcfIfEntry,
       "rtrcfProxyarp": rtrcfProxyarp,
       "rtrcfIcmp": rtrcfIcmp,
       "rtrcfHelperAddr": rtrcfHelperAddr,
       "rtrcfBcastAddr": rtrcfBcastAddr,
       "pysmiFakeCol7": pysmiFakeCol7,
       "rtrcfStatRtTbl": rtrcfStatRtTbl,
       "rtrcfStatRtEntry": rtrcfStatRtEntry,
       "rtrcfStatRtRoute": rtrcfStatRtRoute,
       "rtrcfStatRtRouter": rtrcfStatRtRouter,
       "rtrcfStatRtMetric": rtrcfStatRtMetric,
       "rtrrtInFltrTbl": rtrrtInFltrTbl,
       "rtrrtInFltrEntry": rtrrtInFltrEntry,
       "rtrrtInFltrInf": rtrrtInFltrInf,
       "rtrrtInFltrAddr": rtrrtInFltrAddr,
       "rtrrtInFltrMask": rtrrtInFltrMask,
       "rtrrtInFltrFlag": rtrrtInFltrFlag,
       "rtrrtOutFltrTbl": rtrrtOutFltrTbl,
       "rtrrtOutFltrEntry": rtrrtOutFltrEntry,
       "rtrrtOutFltrInf": rtrrtOutFltrInf,
       "rtrrtOutFltrAddr": rtrrtOutFltrAddr,
       "rtrrtOutFltrMask": rtrrtOutFltrMask,
       "rtrrtOutFltrFlag": rtrrtOutFltrFlag,
       "dialup": dialup,
       "phonenum": phonenum,
       "modemInitstr": modemInitstr,
       "modemDialprefix": modemDialprefix,
       "modemDialsuffix": modemDialsuffix,
       "modemHangupprefix": modemHangupprefix,
       "modemHangupsuffix": modemHangupsuffix,
       "trapinfo": trapinfo,
       "trapSrcAddr": trapSrcAddr,
       "trapErrMsg": trapErrMsg}
)
