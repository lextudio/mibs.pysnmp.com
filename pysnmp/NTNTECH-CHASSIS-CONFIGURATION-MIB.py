# SNMP MIB module (NTNTECH-CHASSIS-CONFIGURATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NTNTECH-CHASSIS-CONFIGURATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:42 2024
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

(NtnDefaultGateway,
 NtnDisplayString,
 NtnSubnetMask,
 NtnTimeTicks,
 ntntechChassis) = mibBuilder.importSymbols(
    "NTNTECH-ROOT-MIB",
    "NtnDefaultGateway",
    "NtnDisplayString",
    "NtnSubnetMask",
    "NtnTimeTicks",
    "ntntechChassis")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ntntechChassisConfigurationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1)
)
ntntechChassisConfigurationMIB.setRevisions(
        ("1902-08-13 11:12",
         "1902-08-28 09:12",
         "1902-10-11 09:13",
         "1902-10-22 02:00",
         "1902-11-04 12:58",
         "1904-03-15 10:15",
         "1904-04-27 11:16",
         "1904-10-11 09:09",
         "1904-11-17 09:58")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ChsCfgMIBObjects_ObjectIdentity = ObjectIdentity
chsCfgMIBObjects = _ChsCfgMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1)
)
_ChsCfgParameterConfiguration_ObjectIdentity = ObjectIdentity
chsCfgParameterConfiguration = _ChsCfgParameterConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1)
)
_PrmCfgMultiplexerUplinkModule_ObjectIdentity = ObjectIdentity
prmCfgMultiplexerUplinkModule = _PrmCfgMultiplexerUplinkModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1)
)
_MumCfgNotes_Type = NtnDisplayString
_MumCfgNotes_Object = MibScalar
mumCfgNotes = _MumCfgNotes_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 1),
    _MumCfgNotes_Type()
)
mumCfgNotes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mumCfgNotes.setStatus("current")
_MumCfgTable_Object = MibTable
mumCfgTable = _MumCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mumCfgTable.setStatus("current")
_MumCfgEntry_Object = MibTableRow
mumCfgEntry = _MumCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 2, 1)
)
mumCfgEntry.setIndexNames(
    (0, "NTNTECH-CHASSIS-CONFIGURATION-MIB", "mumCfgIndex"),
)
if mibBuilder.loadTexts:
    mumCfgEntry.setStatus("current")


class _MumCfgIndex_Type(Integer32):
    """Custom type mumCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_MumCfgIndex_Type.__name__ = "Integer32"
_MumCfgIndex_Object = MibTableColumn
mumCfgIndex = _MumCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 2, 1, 1),
    _MumCfgIndex_Type()
)
mumCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mumCfgIndex.setStatus("current")
_MumCfgIpAddress_Type = IpAddress
_MumCfgIpAddress_Object = MibTableColumn
mumCfgIpAddress = _MumCfgIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 2, 1, 2),
    _MumCfgIpAddress_Type()
)
mumCfgIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mumCfgIpAddress.setStatus("current")
_MumCfgSubnetMask_Type = IpAddress
_MumCfgSubnetMask_Object = MibTableColumn
mumCfgSubnetMask = _MumCfgSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 2, 1, 3),
    _MumCfgSubnetMask_Type()
)
mumCfgSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mumCfgSubnetMask.setStatus("current")
_MumCfgDefaultGateway_Type = IpAddress
_MumCfgDefaultGateway_Object = MibTableColumn
mumCfgDefaultGateway = _MumCfgDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 2, 1, 4),
    _MumCfgDefaultGateway_Type()
)
mumCfgDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mumCfgDefaultGateway.setStatus("current")


class _MumCfgInbandMgmt_Type(Integer32):
    """Custom type mumCfgInbandMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_MumCfgInbandMgmt_Type.__name__ = "Integer32"
_MumCfgInbandMgmt_Object = MibTableColumn
mumCfgInbandMgmt = _MumCfgInbandMgmt_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 2, 1, 5),
    _MumCfgInbandMgmt_Type()
)
mumCfgInbandMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mumCfgInbandMgmt.setStatus("current")


class _MumCfgInbandMGMTVlanID_Type(Integer32):
    """Custom type mumCfgInbandMGMTVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4085),
    )


_MumCfgInbandMGMTVlanID_Type.__name__ = "Integer32"
_MumCfgInbandMGMTVlanID_Object = MibTableColumn
mumCfgInbandMGMTVlanID = _MumCfgInbandMGMTVlanID_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 2, 1, 6),
    _MumCfgInbandMGMTVlanID_Type()
)
mumCfgInbandMGMTVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mumCfgInbandMGMTVlanID.setStatus("current")


class _MumCfgInterConnection_Type(Integer32):
    """Custom type mumCfgInterConnection based on Integer32"""
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
        *(("mgmt", 6),
          ("neither", 1),
          ("uplink1", 2),
          ("uplink2", 3),
          ("uplink3", 4),
          ("uplink4", 5))
    )


_MumCfgInterConnection_Type.__name__ = "Integer32"
_MumCfgInterConnection_Object = MibTableColumn
mumCfgInterConnection = _MumCfgInterConnection_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 2, 1, 7),
    _MumCfgInterConnection_Type()
)
mumCfgInterConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mumCfgInterConnection.setStatus("current")


class _MumCfgCommitChange_Type(Integer32):
    """Custom type mumCfgCommitChange based on Integer32"""
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


_MumCfgCommitChange_Type.__name__ = "Integer32"
_MumCfgCommitChange_Object = MibTableColumn
mumCfgCommitChange = _MumCfgCommitChange_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 2, 1, 8),
    _MumCfgCommitChange_Type()
)
mumCfgCommitChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mumCfgCommitChange.setStatus("current")
_MumCfgUplinkInterfaceModule_ObjectIdentity = ObjectIdentity
mumCfgUplinkInterfaceModule = _MumCfgUplinkInterfaceModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3)
)
_UimCfgEthTable_Object = MibTable
uimCfgEthTable = _UimCfgEthTable_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    uimCfgEthTable.setStatus("current")
_UimCfgEthEntry_Object = MibTableRow
uimCfgEthEntry = _UimCfgEthEntry_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 1, 1)
)
uimCfgEthEntry.setIndexNames(
    (0, "NTNTECH-CHASSIS-CONFIGURATION-MIB", "uimCfgEthMumIndex"),
    (0, "NTNTECH-CHASSIS-CONFIGURATION-MIB", "uimCfgEthIndex"),
)
if mibBuilder.loadTexts:
    uimCfgEthEntry.setStatus("current")


class _UimCfgEthMumIndex_Type(Integer32):
    """Custom type uimCfgEthMumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_UimCfgEthMumIndex_Type.__name__ = "Integer32"
_UimCfgEthMumIndex_Object = MibTableColumn
uimCfgEthMumIndex = _UimCfgEthMumIndex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1),
    _UimCfgEthMumIndex_Type()
)
uimCfgEthMumIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uimCfgEthMumIndex.setStatus("current")


class _UimCfgEthIndex_Type(Integer32):
    """Custom type uimCfgEthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_UimCfgEthIndex_Type.__name__ = "Integer32"
_UimCfgEthIndex_Object = MibTableColumn
uimCfgEthIndex = _UimCfgEthIndex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 1, 1, 2),
    _UimCfgEthIndex_Type()
)
uimCfgEthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uimCfgEthIndex.setStatus("current")


class _UimCfgEthRxTxRate_Type(Integer32):
    """Custom type uimCfgEthRxTxRate based on Integer32"""
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
        *(("uimEth10", 1),
          ("uimEth100", 2),
          ("uimEthAutoNegotiate", 0),
          ("uimEthGig", 3))
    )


_UimCfgEthRxTxRate_Type.__name__ = "Integer32"
_UimCfgEthRxTxRate_Object = MibTableColumn
uimCfgEthRxTxRate = _UimCfgEthRxTxRate_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 1, 1, 3),
    _UimCfgEthRxTxRate_Type()
)
uimCfgEthRxTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uimCfgEthRxTxRate.setStatus("current")


class _UimCfgEthDuplex_Type(Integer32):
    """Custom type uimCfgEthDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uimEthAutoNegotiate", 0),
          ("uimEthFull", 2),
          ("uimEthHalf", 1))
    )


_UimCfgEthDuplex_Type.__name__ = "Integer32"
_UimCfgEthDuplex_Object = MibTableColumn
uimCfgEthDuplex = _UimCfgEthDuplex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 1, 1, 4),
    _UimCfgEthDuplex_Type()
)
uimCfgEthDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uimCfgEthDuplex.setStatus("current")
_UimCfgT1Table_Object = MibTable
uimCfgT1Table = _UimCfgT1Table_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    uimCfgT1Table.setStatus("current")
_UimCfgT1Entry_Object = MibTableRow
uimCfgT1Entry = _UimCfgT1Entry_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 2, 1)
)
uimCfgT1Entry.setIndexNames(
    (0, "NTNTECH-CHASSIS-CONFIGURATION-MIB", "uimCfgT1MumIndex"),
    (0, "NTNTECH-CHASSIS-CONFIGURATION-MIB", "uimCfgT1Index"),
)
if mibBuilder.loadTexts:
    uimCfgT1Entry.setStatus("current")


class _UimCfgT1MumIndex_Type(Integer32):
    """Custom type uimCfgT1MumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_UimCfgT1MumIndex_Type.__name__ = "Integer32"
_UimCfgT1MumIndex_Object = MibTableColumn
uimCfgT1MumIndex = _UimCfgT1MumIndex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 2, 1, 1),
    _UimCfgT1MumIndex_Type()
)
uimCfgT1MumIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uimCfgT1MumIndex.setStatus("current")


class _UimCfgT1Index_Type(Integer32):
    """Custom type uimCfgT1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_UimCfgT1Index_Type.__name__ = "Integer32"
_UimCfgT1Index_Object = MibTableColumn
uimCfgT1Index = _UimCfgT1Index_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 2, 1, 2),
    _UimCfgT1Index_Type()
)
uimCfgT1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uimCfgT1Index.setStatus("current")


class _UimCfgT1Frame_Type(Integer32):
    """Custom type uimCfgT1Frame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uimT1ESF", 1),
          ("uimT1SFD4", 2))
    )


_UimCfgT1Frame_Type.__name__ = "Integer32"
_UimCfgT1Frame_Object = MibTableColumn
uimCfgT1Frame = _UimCfgT1Frame_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 2, 1, 3),
    _UimCfgT1Frame_Type()
)
uimCfgT1Frame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uimCfgT1Frame.setStatus("current")


class _UimCfgT1LineCode_Type(Integer32):
    """Custom type uimCfgT1LineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uimT1AMI", 2),
          ("uimT1B8ZS", 1))
    )


_UimCfgT1LineCode_Type.__name__ = "Integer32"
_UimCfgT1LineCode_Object = MibTableColumn
uimCfgT1LineCode = _UimCfgT1LineCode_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 2, 1, 4),
    _UimCfgT1LineCode_Type()
)
uimCfgT1LineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uimCfgT1LineCode.setStatus("current")


class _UimCfgT1LineBuildout_Type(Integer32):
    """Custom type uimCfgT1LineBuildout based on Integer32"""
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
        *(("uimT10db", 1),
          ("uimT1N15db", 3),
          ("uimT1N22p5db", 4),
          ("uimT1N7p5db", 2))
    )


_UimCfgT1LineBuildout_Type.__name__ = "Integer32"
_UimCfgT1LineBuildout_Object = MibTableColumn
uimCfgT1LineBuildout = _UimCfgT1LineBuildout_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 2, 1, 5),
    _UimCfgT1LineBuildout_Type()
)
uimCfgT1LineBuildout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uimCfgT1LineBuildout.setStatus("current")
_UimCfgE1Table_Object = MibTable
uimCfgE1Table = _UimCfgE1Table_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    uimCfgE1Table.setStatus("current")
_UimCfgE1Entry_Object = MibTableRow
uimCfgE1Entry = _UimCfgE1Entry_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 3, 1)
)
uimCfgE1Entry.setIndexNames(
    (0, "NTNTECH-CHASSIS-CONFIGURATION-MIB", "uimCfgE1MumIndex"),
    (0, "NTNTECH-CHASSIS-CONFIGURATION-MIB", "uimCfgE1Index"),
)
if mibBuilder.loadTexts:
    uimCfgE1Entry.setStatus("current")


class _UimCfgE1MumIndex_Type(Integer32):
    """Custom type uimCfgE1MumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_UimCfgE1MumIndex_Type.__name__ = "Integer32"
_UimCfgE1MumIndex_Object = MibTableColumn
uimCfgE1MumIndex = _UimCfgE1MumIndex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1),
    _UimCfgE1MumIndex_Type()
)
uimCfgE1MumIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uimCfgE1MumIndex.setStatus("current")


class _UimCfgE1Index_Type(Integer32):
    """Custom type uimCfgE1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_UimCfgE1Index_Type.__name__ = "Integer32"
_UimCfgE1Index_Object = MibTableColumn
uimCfgE1Index = _UimCfgE1Index_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 3, 1, 2),
    _UimCfgE1Index_Type()
)
uimCfgE1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uimCfgE1Index.setStatus("current")


class _UimCfgE1Frame_Type(Integer32):
    """Custom type uimCfgE1Frame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uimE1CRC", 1),
          ("uimE1NoCRC", 2))
    )


_UimCfgE1Frame_Type.__name__ = "Integer32"
_UimCfgE1Frame_Object = MibTableColumn
uimCfgE1Frame = _UimCfgE1Frame_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 3, 1, 3),
    _UimCfgE1Frame_Type()
)
uimCfgE1Frame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uimCfgE1Frame.setStatus("current")


class _UimCfgE1LineCode_Type(Integer32):
    """Custom type uimCfgE1LineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uimE1AMI", 2),
          ("uimE1HDB3", 1))
    )


_UimCfgE1LineCode_Type.__name__ = "Integer32"
_UimCfgE1LineCode_Object = MibTableColumn
uimCfgE1LineCode = _UimCfgE1LineCode_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 3, 1, 4),
    _UimCfgE1LineCode_Type()
)
uimCfgE1LineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uimCfgE1LineCode.setStatus("current")
_MumSNMPConfiguration_ObjectIdentity = ObjectIdentity
mumSNMPConfiguration = _MumSNMPConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 4)
)
_SnmpCfgNoticeIpTable_Object = MibTable
snmpCfgNoticeIpTable = _SnmpCfgNoticeIpTable_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    snmpCfgNoticeIpTable.setStatus("current")
_SnmpCfgNoticeIpEntry_Object = MibTableRow
snmpCfgNoticeIpEntry = _SnmpCfgNoticeIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 4, 1, 1)
)
snmpCfgNoticeIpEntry.setIndexNames(
    (0, "NTNTECH-CHASSIS-CONFIGURATION-MIB", "snmpCfgNoticeIndex"),
)
if mibBuilder.loadTexts:
    snmpCfgNoticeIpEntry.setStatus("current")


class _SnmpCfgNoticeIndex_Type(Integer32):
    """Custom type snmpCfgNoticeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SnmpCfgNoticeIndex_Type.__name__ = "Integer32"
_SnmpCfgNoticeIndex_Object = MibTableColumn
snmpCfgNoticeIndex = _SnmpCfgNoticeIndex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1),
    _SnmpCfgNoticeIndex_Type()
)
snmpCfgNoticeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpCfgNoticeIndex.setStatus("current")
_SnmpCfgNoticeIpAddress_Type = IpAddress
_SnmpCfgNoticeIpAddress_Object = MibTableColumn
snmpCfgNoticeIpAddress = _SnmpCfgNoticeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 4, 1, 1, 2),
    _SnmpCfgNoticeIpAddress_Type()
)
snmpCfgNoticeIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCfgNoticeIpAddress.setStatus("current")


class _SnmpCfgAuthenticationTrapState_Type(Integer32):
    """Custom type snmpCfgAuthenticationTrapState based on Integer32"""
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


_SnmpCfgAuthenticationTrapState_Type.__name__ = "Integer32"
_SnmpCfgAuthenticationTrapState_Object = MibScalar
snmpCfgAuthenticationTrapState = _SnmpCfgAuthenticationTrapState_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 4, 2),
    _SnmpCfgAuthenticationTrapState_Type()
)
snmpCfgAuthenticationTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCfgAuthenticationTrapState.setStatus("current")


class _SnmpCfgEnvironmentTrapState_Type(Integer32):
    """Custom type snmpCfgEnvironmentTrapState based on Integer32"""
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


_SnmpCfgEnvironmentTrapState_Type.__name__ = "Integer32"
_SnmpCfgEnvironmentTrapState_Object = MibScalar
snmpCfgEnvironmentTrapState = _SnmpCfgEnvironmentTrapState_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 4, 3),
    _SnmpCfgEnvironmentTrapState_Type()
)
snmpCfgEnvironmentTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCfgEnvironmentTrapState.setStatus("current")


class _SnmpCfgColdstartTrapState_Type(Integer32):
    """Custom type snmpCfgColdstartTrapState based on Integer32"""
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


_SnmpCfgColdstartTrapState_Type.__name__ = "Integer32"
_SnmpCfgColdstartTrapState_Object = MibScalar
snmpCfgColdstartTrapState = _SnmpCfgColdstartTrapState_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 4, 4),
    _SnmpCfgColdstartTrapState_Type()
)
snmpCfgColdstartTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCfgColdstartTrapState.setStatus("current")


class _SnmpCfgModulePortTrapState_Type(Integer32):
    """Custom type snmpCfgModulePortTrapState based on Integer32"""
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


_SnmpCfgModulePortTrapState_Type.__name__ = "Integer32"
_SnmpCfgModulePortTrapState_Object = MibScalar
snmpCfgModulePortTrapState = _SnmpCfgModulePortTrapState_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 4, 5),
    _SnmpCfgModulePortTrapState_Type()
)
snmpCfgModulePortTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCfgModulePortTrapState.setStatus("current")
_SnmpCfgCommunity_ObjectIdentity = ObjectIdentity
snmpCfgCommunity = _SnmpCfgCommunity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 4, 6)
)


class _ComReadWriteAccess_Type(OctetString):
    """Custom type comReadWriteAccess based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ComReadWriteAccess_Type.__name__ = "OctetString"
_ComReadWriteAccess_Object = MibScalar
comReadWriteAccess = _ComReadWriteAccess_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 4, 6, 1),
    _ComReadWriteAccess_Type()
)
comReadWriteAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comReadWriteAccess.setStatus("current")


class _ComReadOnlyAccess_Type(OctetString):
    """Custom type comReadOnlyAccess based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ComReadOnlyAccess_Type.__name__ = "OctetString"
_ComReadOnlyAccess_Object = MibScalar
comReadOnlyAccess = _ComReadOnlyAccess_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 4, 6, 2),
    _ComReadOnlyAccess_Type()
)
comReadOnlyAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comReadOnlyAccess.setStatus("current")
_MumCfgUniques_ObjectIdentity = ObjectIdentity
mumCfgUniques = _MumCfgUniques_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 5)
)


class _UnqEmbHttpWebsrvrState_Type(Integer32):
    """Custom type unqEmbHttpWebsrvrState based on Integer32"""
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


_UnqEmbHttpWebsrvrState_Type.__name__ = "Integer32"
_UnqEmbHttpWebsrvrState_Object = MibScalar
unqEmbHttpWebsrvrState = _UnqEmbHttpWebsrvrState_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 5, 1),
    _UnqEmbHttpWebsrvrState_Type()
)
unqEmbHttpWebsrvrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unqEmbHttpWebsrvrState.setStatus("current")
_MumCfgAdvanced_ObjectIdentity = ObjectIdentity
mumCfgAdvanced = _MumCfgAdvanced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 6)
)
_AdvCfgTable_Object = MibTable
advCfgTable = _AdvCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    advCfgTable.setStatus("current")
_AdvCfgEntry_Object = MibTableRow
advCfgEntry = _AdvCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 6, 1, 1)
)
advCfgEntry.setIndexNames(
    (0, "NTNTECH-CHASSIS-CONFIGURATION-MIB", "advCfgMumIndex"),
)
if mibBuilder.loadTexts:
    advCfgEntry.setStatus("current")


class _AdvCfgMumIndex_Type(Integer32):
    """Custom type advCfgMumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AdvCfgMumIndex_Type.__name__ = "Integer32"
_AdvCfgMumIndex_Object = MibTableColumn
advCfgMumIndex = _AdvCfgMumIndex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 6, 1, 1, 1),
    _AdvCfgMumIndex_Type()
)
advCfgMumIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advCfgMumIndex.setStatus("current")


class _AdvCfgTFTPState_Type(Integer32):
    """Custom type advCfgTFTPState based on Integer32"""
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


_AdvCfgTFTPState_Type.__name__ = "Integer32"
_AdvCfgTFTPState_Object = MibTableColumn
advCfgTFTPState = _AdvCfgTFTPState_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 6, 1, 1, 2),
    _AdvCfgTFTPState_Type()
)
advCfgTFTPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    advCfgTFTPState.setStatus("current")


class _AdvCfgTelnetState_Type(Integer32):
    """Custom type advCfgTelnetState based on Integer32"""
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


_AdvCfgTelnetState_Type.__name__ = "Integer32"
_AdvCfgTelnetState_Object = MibTableColumn
advCfgTelnetState = _AdvCfgTelnetState_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 6, 1, 1, 3),
    _AdvCfgTelnetState_Type()
)
advCfgTelnetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    advCfgTelnetState.setStatus("current")
_AdvCfgMgmtFltrIpStart_Type = IpAddress
_AdvCfgMgmtFltrIpStart_Object = MibTableColumn
advCfgMgmtFltrIpStart = _AdvCfgMgmtFltrIpStart_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 6, 1, 1, 4),
    _AdvCfgMgmtFltrIpStart_Type()
)
advCfgMgmtFltrIpStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    advCfgMgmtFltrIpStart.setStatus("current")
_AdvCfgMgmtFltrIpEnd_Type = IpAddress
_AdvCfgMgmtFltrIpEnd_Object = MibTableColumn
advCfgMgmtFltrIpEnd = _AdvCfgMgmtFltrIpEnd_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 6, 1, 1, 5),
    _AdvCfgMgmtFltrIpEnd_Type()
)
advCfgMgmtFltrIpEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    advCfgMgmtFltrIpEnd.setStatus("current")
_AdvCfgMgmtSessionTimeout_Type = NtnTimeTicks
_AdvCfgMgmtSessionTimeout_Object = MibTableColumn
advCfgMgmtSessionTimeout = _AdvCfgMgmtSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 6, 1, 1, 6),
    _AdvCfgMgmtSessionTimeout_Type()
)
advCfgMgmtSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    advCfgMgmtSessionTimeout.setStatus("current")
_MumCfgManagementPort_ObjectIdentity = ObjectIdentity
mumCfgManagementPort = _MumCfgManagementPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 7)
)
_MgmtPortCfgTable_Object = MibTable
mgmtPortCfgTable = _MgmtPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    mgmtPortCfgTable.setStatus("current")
_MgmtPortCfgEntry_Object = MibTableRow
mgmtPortCfgEntry = _MgmtPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 7, 1, 1)
)
mgmtPortCfgEntry.setIndexNames(
    (0, "NTNTECH-CHASSIS-CONFIGURATION-MIB", "mgmtPortCfgMumIndex"),
)
if mibBuilder.loadTexts:
    mgmtPortCfgEntry.setStatus("current")


class _MgmtPortCfgMumIndex_Type(Integer32):
    """Custom type mgmtPortCfgMumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_MgmtPortCfgMumIndex_Type.__name__ = "Integer32"
_MgmtPortCfgMumIndex_Object = MibTableColumn
mgmtPortCfgMumIndex = _MgmtPortCfgMumIndex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 7, 1, 1, 1),
    _MgmtPortCfgMumIndex_Type()
)
mgmtPortCfgMumIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtPortCfgMumIndex.setStatus("current")


class _MgmtPortCfgRxTxRate_Type(Integer32):
    """Custom type mgmtPortCfgRxTxRate based on Integer32"""
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
        *(("uimEth10", 1),
          ("uimEth100", 2),
          ("uimEthAutoNegotiate", 0),
          ("uimEthGig", 3))
    )


_MgmtPortCfgRxTxRate_Type.__name__ = "Integer32"
_MgmtPortCfgRxTxRate_Object = MibTableColumn
mgmtPortCfgRxTxRate = _MgmtPortCfgRxTxRate_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 7, 1, 1, 2),
    _MgmtPortCfgRxTxRate_Type()
)
mgmtPortCfgRxTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtPortCfgRxTxRate.setStatus("current")


class _MgmtPortCfgDuplex_Type(Integer32):
    """Custom type mgmtPortCfgDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uimEthAutoNegotiate", 0),
          ("uimEthFull", 2),
          ("uimEthHalf", 1))
    )


_MgmtPortCfgDuplex_Type.__name__ = "Integer32"
_MgmtPortCfgDuplex_Object = MibTableColumn
mgmtPortCfgDuplex = _MgmtPortCfgDuplex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 7, 1, 1, 3),
    _MgmtPortCfgDuplex_Type()
)
mgmtPortCfgDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtPortCfgDuplex.setStatus("current")


class _MgmtPortCfgType_Type(Integer32):
    """Custom type mgmtPortCfgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mgmt", 1),
          ("uplink", 2))
    )


_MgmtPortCfgType_Type.__name__ = "Integer32"
_MgmtPortCfgType_Object = MibTableColumn
mgmtPortCfgType = _MgmtPortCfgType_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 7, 1, 1, 4),
    _MgmtPortCfgType_Type()
)
mgmtPortCfgType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtPortCfgType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NTNTECH-CHASSIS-CONFIGURATION-MIB",
    **{"ntntechChassisConfigurationMIB": ntntechChassisConfigurationMIB,
       "chsCfgMIBObjects": chsCfgMIBObjects,
       "chsCfgParameterConfiguration": chsCfgParameterConfiguration,
       "prmCfgMultiplexerUplinkModule": prmCfgMultiplexerUplinkModule,
       "mumCfgNotes": mumCfgNotes,
       "mumCfgTable": mumCfgTable,
       "mumCfgEntry": mumCfgEntry,
       "mumCfgIndex": mumCfgIndex,
       "mumCfgIpAddress": mumCfgIpAddress,
       "mumCfgSubnetMask": mumCfgSubnetMask,
       "mumCfgDefaultGateway": mumCfgDefaultGateway,
       "mumCfgInbandMgmt": mumCfgInbandMgmt,
       "mumCfgInbandMGMTVlanID": mumCfgInbandMGMTVlanID,
       "mumCfgInterConnection": mumCfgInterConnection,
       "mumCfgCommitChange": mumCfgCommitChange,
       "mumCfgUplinkInterfaceModule": mumCfgUplinkInterfaceModule,
       "uimCfgEthTable": uimCfgEthTable,
       "uimCfgEthEntry": uimCfgEthEntry,
       "uimCfgEthMumIndex": uimCfgEthMumIndex,
       "uimCfgEthIndex": uimCfgEthIndex,
       "uimCfgEthRxTxRate": uimCfgEthRxTxRate,
       "uimCfgEthDuplex": uimCfgEthDuplex,
       "uimCfgT1Table": uimCfgT1Table,
       "uimCfgT1Entry": uimCfgT1Entry,
       "uimCfgT1MumIndex": uimCfgT1MumIndex,
       "uimCfgT1Index": uimCfgT1Index,
       "uimCfgT1Frame": uimCfgT1Frame,
       "uimCfgT1LineCode": uimCfgT1LineCode,
       "uimCfgT1LineBuildout": uimCfgT1LineBuildout,
       "uimCfgE1Table": uimCfgE1Table,
       "uimCfgE1Entry": uimCfgE1Entry,
       "uimCfgE1MumIndex": uimCfgE1MumIndex,
       "uimCfgE1Index": uimCfgE1Index,
       "uimCfgE1Frame": uimCfgE1Frame,
       "uimCfgE1LineCode": uimCfgE1LineCode,
       "mumSNMPConfiguration": mumSNMPConfiguration,
       "snmpCfgNoticeIpTable": snmpCfgNoticeIpTable,
       "snmpCfgNoticeIpEntry": snmpCfgNoticeIpEntry,
       "snmpCfgNoticeIndex": snmpCfgNoticeIndex,
       "snmpCfgNoticeIpAddress": snmpCfgNoticeIpAddress,
       "snmpCfgAuthenticationTrapState": snmpCfgAuthenticationTrapState,
       "snmpCfgEnvironmentTrapState": snmpCfgEnvironmentTrapState,
       "snmpCfgColdstartTrapState": snmpCfgColdstartTrapState,
       "snmpCfgModulePortTrapState": snmpCfgModulePortTrapState,
       "snmpCfgCommunity": snmpCfgCommunity,
       "comReadWriteAccess": comReadWriteAccess,
       "comReadOnlyAccess": comReadOnlyAccess,
       "mumCfgUniques": mumCfgUniques,
       "unqEmbHttpWebsrvrState": unqEmbHttpWebsrvrState,
       "mumCfgAdvanced": mumCfgAdvanced,
       "advCfgTable": advCfgTable,
       "advCfgEntry": advCfgEntry,
       "advCfgMumIndex": advCfgMumIndex,
       "advCfgTFTPState": advCfgTFTPState,
       "advCfgTelnetState": advCfgTelnetState,
       "advCfgMgmtFltrIpStart": advCfgMgmtFltrIpStart,
       "advCfgMgmtFltrIpEnd": advCfgMgmtFltrIpEnd,
       "advCfgMgmtSessionTimeout": advCfgMgmtSessionTimeout,
       "mumCfgManagementPort": mumCfgManagementPort,
       "mgmtPortCfgTable": mgmtPortCfgTable,
       "mgmtPortCfgEntry": mgmtPortCfgEntry,
       "mgmtPortCfgMumIndex": mgmtPortCfgMumIndex,
       "mgmtPortCfgRxTxRate": mgmtPortCfgRxTxRate,
       "mgmtPortCfgDuplex": mgmtPortCfgDuplex,
       "mgmtPortCfgType": mgmtPortCfgType}
)
