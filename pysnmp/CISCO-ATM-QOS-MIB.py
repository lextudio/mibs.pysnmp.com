# SNMP MIB module (CISCO-ATM-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ATM-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:57 2024
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

(AtmServiceCategory,) = mibBuilder.importSymbols(
    "ATM-FORUM-TC-MIB",
    "AtmServiceCategory")

(atmVclVci,
 atmVclVpi,
 atmVplVpi) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmVclVci",
    "atmVclVpi",
    "atmVplVpi")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoAtmQosMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 279)
)
ciscoAtmQosMIB.setRevisions(
        ("2002-06-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VcParamConfigLocation(Integer32, TextualConvention):
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
        *(("configDefault", 1),
          ("configVcClass", 3),
          ("configVcClassInterface", 5),
          ("configVcClassSubInterface", 4),
          ("configVcDirect", 2))
    )



class VpState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vpStateActive", 2),
          ("vpStateInactive", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoAtmQosMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoAtmQosMIBNotifs = _CiscoAtmQosMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 0)
)
_CiscoAtmQosMIBObjects_ObjectIdentity = ObjectIdentity
ciscoAtmQosMIBObjects = _CiscoAtmQosMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1)
)
_CaqVccParams_ObjectIdentity = ObjectIdentity
caqVccParams = _CaqVccParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 1)
)
_CaqVccParamsTable_Object = MibTable
caqVccParamsTable = _CaqVccParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 1, 1)
)
if mibBuilder.loadTexts:
    caqVccParamsTable.setStatus("current")
_CaqVccParamsEntry_Object = MibTableRow
caqVccParamsEntry = _CaqVccParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 1, 1, 1)
)
caqVccParamsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    caqVccParamsEntry.setStatus("current")
_CaqVccParamsType_Type = AtmServiceCategory
_CaqVccParamsType_Object = MibTableColumn
caqVccParamsType = _CaqVccParamsType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 1, 1, 1, 1),
    _CaqVccParamsType_Type()
)
caqVccParamsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqVccParamsType.setStatus("current")
_CaqVccParamsPcrIn0_Type = Unsigned32
_CaqVccParamsPcrIn0_Object = MibTableColumn
caqVccParamsPcrIn0 = _CaqVccParamsPcrIn0_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 1, 1, 1, 2),
    _CaqVccParamsPcrIn0_Type()
)
caqVccParamsPcrIn0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqVccParamsPcrIn0.setStatus("current")
_CaqVccParamsPcrIn01_Type = Unsigned32
_CaqVccParamsPcrIn01_Object = MibTableColumn
caqVccParamsPcrIn01 = _CaqVccParamsPcrIn01_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 1, 1, 1, 3),
    _CaqVccParamsPcrIn01_Type()
)
caqVccParamsPcrIn01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqVccParamsPcrIn01.setStatus("current")
_CaqVccParamsPcrOut0_Type = Unsigned32
_CaqVccParamsPcrOut0_Object = MibTableColumn
caqVccParamsPcrOut0 = _CaqVccParamsPcrOut0_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 1, 1, 1, 4),
    _CaqVccParamsPcrOut0_Type()
)
caqVccParamsPcrOut0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqVccParamsPcrOut0.setStatus("current")
_CaqVccParamsPcrOut01_Type = Unsigned32
_CaqVccParamsPcrOut01_Object = MibTableColumn
caqVccParamsPcrOut01 = _CaqVccParamsPcrOut01_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 1, 1, 1, 5),
    _CaqVccParamsPcrOut01_Type()
)
caqVccParamsPcrOut01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqVccParamsPcrOut01.setStatus("current")
_CaqVccParamsScrIn0_Type = Unsigned32
_CaqVccParamsScrIn0_Object = MibTableColumn
caqVccParamsScrIn0 = _CaqVccParamsScrIn0_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 1, 1, 1, 6),
    _CaqVccParamsScrIn0_Type()
)
caqVccParamsScrIn0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqVccParamsScrIn0.setStatus("current")
_CaqVccParamsScrIn01_Type = Unsigned32
_CaqVccParamsScrIn01_Object = MibTableColumn
caqVccParamsScrIn01 = _CaqVccParamsScrIn01_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 1, 1, 1, 7),
    _CaqVccParamsScrIn01_Type()
)
caqVccParamsScrIn01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqVccParamsScrIn01.setStatus("current")
_CaqVccParamsScrOut0_Type = Unsigned32
_CaqVccParamsScrOut0_Object = MibTableColumn
caqVccParamsScrOut0 = _CaqVccParamsScrOut0_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 1, 1, 1, 8),
    _CaqVccParamsScrOut0_Type()
)
caqVccParamsScrOut0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqVccParamsScrOut0.setStatus("current")
_CaqVccParamsScrOut01_Type = Unsigned32
_CaqVccParamsScrOut01_Object = MibTableColumn
caqVccParamsScrOut01 = _CaqVccParamsScrOut01_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 1, 1, 1, 9),
    _CaqVccParamsScrOut01_Type()
)
caqVccParamsScrOut01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqVccParamsScrOut01.setStatus("current")
_CaqVccParamsBcsIn0_Type = Unsigned32
_CaqVccParamsBcsIn0_Object = MibTableColumn
caqVccParamsBcsIn0 = _CaqVccParamsBcsIn0_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 1, 1, 1, 10),
    _CaqVccParamsBcsIn0_Type()
)
caqVccParamsBcsIn0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqVccParamsBcsIn0.setStatus("current")
_CaqVccParamsBcsIn01_Type = Unsigned32
_CaqVccParamsBcsIn01_Object = MibTableColumn
caqVccParamsBcsIn01 = _CaqVccParamsBcsIn01_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 1, 1, 1, 11),
    _CaqVccParamsBcsIn01_Type()
)
caqVccParamsBcsIn01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqVccParamsBcsIn01.setStatus("current")
_CaqVccParamsBcsOut0_Type = Unsigned32
_CaqVccParamsBcsOut0_Object = MibTableColumn
caqVccParamsBcsOut0 = _CaqVccParamsBcsOut0_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 1, 1, 1, 12),
    _CaqVccParamsBcsOut0_Type()
)
caqVccParamsBcsOut0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqVccParamsBcsOut0.setStatus("current")
_CaqVccParamsBcsOut01_Type = Unsigned32
_CaqVccParamsBcsOut01_Object = MibTableColumn
caqVccParamsBcsOut01 = _CaqVccParamsBcsOut01_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 1, 1, 1, 13),
    _CaqVccParamsBcsOut01_Type()
)
caqVccParamsBcsOut01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqVccParamsBcsOut01.setStatus("current")
_CaqVccParamsInheritLevel_Type = VcParamConfigLocation
_CaqVccParamsInheritLevel_Object = MibTableColumn
caqVccParamsInheritLevel = _CaqVccParamsInheritLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 1, 1, 1, 14),
    _CaqVccParamsInheritLevel_Type()
)
caqVccParamsInheritLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqVccParamsInheritLevel.setStatus("current")
_CaqVccParamsMcrIn_Type = Unsigned32
_CaqVccParamsMcrIn_Object = MibTableColumn
caqVccParamsMcrIn = _CaqVccParamsMcrIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 1, 1, 1, 15),
    _CaqVccParamsMcrIn_Type()
)
caqVccParamsMcrIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqVccParamsMcrIn.setStatus("current")
_CaqVccParamsMcrOut_Type = Unsigned32
_CaqVccParamsMcrOut_Object = MibTableColumn
caqVccParamsMcrOut = _CaqVccParamsMcrOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 1, 1, 1, 16),
    _CaqVccParamsMcrOut_Type()
)
caqVccParamsMcrOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqVccParamsMcrOut.setStatus("current")
_CaqVccParamsInvRdf_Type = Unsigned32
_CaqVccParamsInvRdf_Object = MibTableColumn
caqVccParamsInvRdf = _CaqVccParamsInvRdf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 1, 1, 1, 17),
    _CaqVccParamsInvRdf_Type()
)
caqVccParamsInvRdf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqVccParamsInvRdf.setStatus("current")
_CaqVccParamsInvRif_Type = Unsigned32
_CaqVccParamsInvRif_Object = MibTableColumn
caqVccParamsInvRif = _CaqVccParamsInvRif_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 1, 1, 1, 18),
    _CaqVccParamsInvRif_Type()
)
caqVccParamsInvRif.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqVccParamsInvRif.setStatus("current")
_CaqVccParamsRfl_Type = VcParamConfigLocation
_CaqVccParamsRfl_Object = MibTableColumn
caqVccParamsRfl = _CaqVccParamsRfl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 1, 1, 1, 19),
    _CaqVccParamsRfl_Type()
)
caqVccParamsRfl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqVccParamsRfl.setStatus("current")
_CaqVccParamsCdv_Type = Unsigned32
_CaqVccParamsCdv_Object = MibTableColumn
caqVccParamsCdv = _CaqVccParamsCdv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 1, 1, 1, 20),
    _CaqVccParamsCdv_Type()
)
caqVccParamsCdv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqVccParamsCdv.setStatus("current")
_CaqVccParamsCdvt_Type = Unsigned32
_CaqVccParamsCdvt_Object = MibTableColumn
caqVccParamsCdvt = _CaqVccParamsCdvt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 1, 1, 1, 21),
    _CaqVccParamsCdvt_Type()
)
caqVccParamsCdvt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqVccParamsCdvt.setStatus("current")
_CaqVccParamsIcr_Type = Unsigned32
_CaqVccParamsIcr_Object = MibTableColumn
caqVccParamsIcr = _CaqVccParamsIcr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 1, 1, 1, 22),
    _CaqVccParamsIcr_Type()
)
caqVccParamsIcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqVccParamsIcr.setStatus("current")
_CaqVccParamsTbe_Type = Unsigned32
_CaqVccParamsTbe_Object = MibTableColumn
caqVccParamsTbe = _CaqVccParamsTbe_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 1, 1, 1, 23),
    _CaqVccParamsTbe_Type()
)
caqVccParamsTbe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqVccParamsTbe.setStatus("current")
_CaqVccParamsFrtt_Type = Unsigned32
_CaqVccParamsFrtt_Object = MibTableColumn
caqVccParamsFrtt = _CaqVccParamsFrtt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 1, 1, 1, 24),
    _CaqVccParamsFrtt_Type()
)
caqVccParamsFrtt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqVccParamsFrtt.setStatus("current")
_CaqVccParamsNrm_Type = Unsigned32
_CaqVccParamsNrm_Object = MibTableColumn
caqVccParamsNrm = _CaqVccParamsNrm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 1, 1, 1, 25),
    _CaqVccParamsNrm_Type()
)
caqVccParamsNrm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqVccParamsNrm.setStatus("current")
_CaqVccParamsInvTrm_Type = Unsigned32
_CaqVccParamsInvTrm_Object = MibTableColumn
caqVccParamsInvTrm = _CaqVccParamsInvTrm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 1, 1, 1, 26),
    _CaqVccParamsInvTrm_Type()
)
caqVccParamsInvTrm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqVccParamsInvTrm.setStatus("current")
_CaqVccParamsInvCdf_Type = Unsigned32
_CaqVccParamsInvCdf_Object = MibTableColumn
caqVccParamsInvCdf = _CaqVccParamsInvCdf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 1, 1, 1, 27),
    _CaqVccParamsInvCdf_Type()
)
caqVccParamsInvCdf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqVccParamsInvCdf.setStatus("current")
_CaqVccParamsAdtf_Type = Unsigned32
_CaqVccParamsAdtf_Object = MibTableColumn
caqVccParamsAdtf = _CaqVccParamsAdtf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 1, 1, 1, 28),
    _CaqVccParamsAdtf_Type()
)
caqVccParamsAdtf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caqVccParamsAdtf.setStatus("current")
_CaqVpcParams_ObjectIdentity = ObjectIdentity
caqVpcParams = _CaqVpcParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 2)
)
_CaqVpcParamsTable_Object = MibTable
caqVpcParamsTable = _CaqVpcParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 2, 1)
)
if mibBuilder.loadTexts:
    caqVpcParamsTable.setStatus("current")
_CaqVpcParamsEntry_Object = MibTableRow
caqVpcParamsEntry = _CaqVpcParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 2, 1, 1)
)
caqVpcParamsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
)
if mibBuilder.loadTexts:
    caqVpcParamsEntry.setStatus("current")
_CaqVpcParamsVpState_Type = VpState
_CaqVpcParamsVpState_Object = MibTableColumn
caqVpcParamsVpState = _CaqVpcParamsVpState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 2, 1, 1, 1),
    _CaqVpcParamsVpState_Type()
)
caqVpcParamsVpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqVpcParamsVpState.setStatus("current")
_CaqVpcParamsPeakRate_Type = Unsigned32
_CaqVpcParamsPeakRate_Object = MibTableColumn
caqVpcParamsPeakRate = _CaqVpcParamsPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 2, 1, 1, 2),
    _CaqVpcParamsPeakRate_Type()
)
caqVpcParamsPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqVpcParamsPeakRate.setStatus("current")
_CaqVpcParamsCesRate_Type = Unsigned32
_CaqVpcParamsCesRate_Object = MibTableColumn
caqVpcParamsCesRate = _CaqVpcParamsCesRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 2, 1, 1, 3),
    _CaqVpcParamsCesRate_Type()
)
caqVpcParamsCesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqVpcParamsCesRate.setStatus("current")


class _CaqVpcParamsDataVcCount_Type(Integer32):
    """Custom type caqVpcParamsDataVcCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CaqVpcParamsDataVcCount_Type.__name__ = "Integer32"
_CaqVpcParamsDataVcCount_Object = MibTableColumn
caqVpcParamsDataVcCount = _CaqVpcParamsDataVcCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 2, 1, 1, 4),
    _CaqVpcParamsDataVcCount_Type()
)
caqVpcParamsDataVcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqVpcParamsDataVcCount.setStatus("current")


class _CaqVpcParamsCesVcCount_Type(Integer32):
    """Custom type caqVpcParamsCesVcCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CaqVpcParamsCesVcCount_Type.__name__ = "Integer32"
_CaqVpcParamsCesVcCount_Object = MibTableColumn
caqVpcParamsCesVcCount = _CaqVpcParamsCesVcCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 2, 1, 1, 5),
    _CaqVpcParamsCesVcCount_Type()
)
caqVpcParamsCesVcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqVpcParamsCesVcCount.setStatus("current")


class _CaqVpcParamsVcdF4Seg_Type(Integer32):
    """Custom type caqVpcParamsVcdF4Seg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CaqVpcParamsVcdF4Seg_Type.__name__ = "Integer32"
_CaqVpcParamsVcdF4Seg_Object = MibTableColumn
caqVpcParamsVcdF4Seg = _CaqVpcParamsVcdF4Seg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 2, 1, 1, 6),
    _CaqVpcParamsVcdF4Seg_Type()
)
caqVpcParamsVcdF4Seg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqVpcParamsVcdF4Seg.setStatus("current")


class _CaqVpcParamsVcdF4Ete_Type(Integer32):
    """Custom type caqVpcParamsVcdF4Ete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CaqVpcParamsVcdF4Ete_Type.__name__ = "Integer32"
_CaqVpcParamsVcdF4Ete_Object = MibTableColumn
caqVpcParamsVcdF4Ete = _CaqVpcParamsVcdF4Ete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 2, 1, 1, 7),
    _CaqVpcParamsVcdF4Ete_Type()
)
caqVpcParamsVcdF4Ete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqVpcParamsVcdF4Ete.setStatus("current")
_CaqVpcParamsScr_Type = Unsigned32
_CaqVpcParamsScr_Object = MibTableColumn
caqVpcParamsScr = _CaqVpcParamsScr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 2, 1, 1, 8),
    _CaqVpcParamsScr_Type()
)
caqVpcParamsScr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqVpcParamsScr.setStatus("current")
_CaqVpcParamsMbs_Type = Unsigned32
_CaqVpcParamsMbs_Object = MibTableColumn
caqVpcParamsMbs = _CaqVpcParamsMbs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 2, 1, 1, 9),
    _CaqVpcParamsMbs_Type()
)
caqVpcParamsMbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqVpcParamsMbs.setStatus("current")
_CaqVpcParamsAvailBw_Type = Unsigned32
_CaqVpcParamsAvailBw_Object = MibTableColumn
caqVpcParamsAvailBw = _CaqVpcParamsAvailBw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 2, 1, 1, 10),
    _CaqVpcParamsAvailBw_Type()
)
caqVpcParamsAvailBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqVpcParamsAvailBw.setStatus("current")
_CaqQueuingParams_ObjectIdentity = ObjectIdentity
caqQueuingParams = _CaqQueuingParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 3)
)
_CaqQueuingParamsTable_Object = MibTable
caqQueuingParamsTable = _CaqQueuingParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 3, 1)
)
if mibBuilder.loadTexts:
    caqQueuingParamsTable.setStatus("current")
_CaqQueuingParamsEntry_Object = MibTableRow
caqQueuingParamsEntry = _CaqQueuingParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 3, 1, 1)
)
caqQueuingParamsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    caqQueuingParamsEntry.setStatus("current")
_CaqQueuingParamsMeanQDepth_Type = Unsigned32
_CaqQueuingParamsMeanQDepth_Object = MibTableColumn
caqQueuingParamsMeanQDepth = _CaqQueuingParamsMeanQDepth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 3, 1, 1, 1),
    _CaqQueuingParamsMeanQDepth_Type()
)
caqQueuingParamsMeanQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqQueuingParamsMeanQDepth.setStatus("current")
_CaqQueuingParamsClassTable_Object = MibTable
caqQueuingParamsClassTable = _CaqQueuingParamsClassTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 3, 2)
)
if mibBuilder.loadTexts:
    caqQueuingParamsClassTable.setStatus("current")
_CaqQueuingParamsClassEntry_Object = MibTableRow
caqQueuingParamsClassEntry = _CaqQueuingParamsClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 3, 2, 1)
)
caqQueuingParamsClassEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
    (0, "CISCO-ATM-QOS-MIB", "caqQueuingParamsClassIndex"),
)
if mibBuilder.loadTexts:
    caqQueuingParamsClassEntry.setStatus("current")


class _CaqQueuingParamsClassIndex_Type(Integer32):
    """Custom type caqQueuingParamsClassIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_CaqQueuingParamsClassIndex_Type.__name__ = "Integer32"
_CaqQueuingParamsClassIndex_Object = MibTableColumn
caqQueuingParamsClassIndex = _CaqQueuingParamsClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 3, 2, 1, 1),
    _CaqQueuingParamsClassIndex_Type()
)
caqQueuingParamsClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caqQueuingParamsClassIndex.setStatus("current")
_CaqQueuingParamsClassRandDrp_Type = Unsigned32
_CaqQueuingParamsClassRandDrp_Object = MibTableColumn
caqQueuingParamsClassRandDrp = _CaqQueuingParamsClassRandDrp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 3, 2, 1, 2),
    _CaqQueuingParamsClassRandDrp_Type()
)
caqQueuingParamsClassRandDrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqQueuingParamsClassRandDrp.setStatus("current")
_CaqQueuingParamsClassTailDrp_Type = Unsigned32
_CaqQueuingParamsClassTailDrp_Object = MibTableColumn
caqQueuingParamsClassTailDrp = _CaqQueuingParamsClassTailDrp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 3, 2, 1, 3),
    _CaqQueuingParamsClassTailDrp_Type()
)
caqQueuingParamsClassTailDrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqQueuingParamsClassTailDrp.setStatus("current")
_CaqQueuingParamsClassMinThre_Type = Unsigned32
_CaqQueuingParamsClassMinThre_Object = MibTableColumn
caqQueuingParamsClassMinThre = _CaqQueuingParamsClassMinThre_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 3, 2, 1, 4),
    _CaqQueuingParamsClassMinThre_Type()
)
caqQueuingParamsClassMinThre.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqQueuingParamsClassMinThre.setStatus("current")
_CaqQueuingParamsClassMaxThre_Type = Unsigned32
_CaqQueuingParamsClassMaxThre_Object = MibTableColumn
caqQueuingParamsClassMaxThre = _CaqQueuingParamsClassMaxThre_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 3, 2, 1, 5),
    _CaqQueuingParamsClassMaxThre_Type()
)
caqQueuingParamsClassMaxThre.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqQueuingParamsClassMaxThre.setStatus("current")
_CaqQueuingParamsClassMrkProb_Type = Unsigned32
_CaqQueuingParamsClassMrkProb_Object = MibTableColumn
caqQueuingParamsClassMrkProb = _CaqQueuingParamsClassMrkProb_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 1, 3, 2, 1, 6),
    _CaqQueuingParamsClassMrkProb_Type()
)
caqQueuingParamsClassMrkProb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caqQueuingParamsClassMrkProb.setStatus("current")
_CiscoAtmQosMIBConform_ObjectIdentity = ObjectIdentity
ciscoAtmQosMIBConform = _CiscoAtmQosMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 2)
)
_CiscoAtmQosMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoAtmQosMIBCompliances = _CiscoAtmQosMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 2, 1)
)
_CiscoAtmQosMIBGroups_ObjectIdentity = ObjectIdentity
ciscoAtmQosMIBGroups = _CiscoAtmQosMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 2, 2)
)

# Managed Objects groups

ciscoAtmQosVccGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 2, 2, 1)
)
ciscoAtmQosVccGroup.setObjects(
      *(("CISCO-ATM-QOS-MIB", "caqVccParamsType"),
        ("CISCO-ATM-QOS-MIB", "caqVccParamsPcrIn0"),
        ("CISCO-ATM-QOS-MIB", "caqVccParamsPcrIn01"),
        ("CISCO-ATM-QOS-MIB", "caqVccParamsPcrOut0"),
        ("CISCO-ATM-QOS-MIB", "caqVccParamsPcrOut01"),
        ("CISCO-ATM-QOS-MIB", "caqVccParamsScrIn0"),
        ("CISCO-ATM-QOS-MIB", "caqVccParamsScrIn01"),
        ("CISCO-ATM-QOS-MIB", "caqVccParamsScrOut0"),
        ("CISCO-ATM-QOS-MIB", "caqVccParamsScrOut01"),
        ("CISCO-ATM-QOS-MIB", "caqVccParamsBcsIn0"),
        ("CISCO-ATM-QOS-MIB", "caqVccParamsBcsIn01"),
        ("CISCO-ATM-QOS-MIB", "caqVccParamsBcsOut0"),
        ("CISCO-ATM-QOS-MIB", "caqVccParamsBcsOut01"),
        ("CISCO-ATM-QOS-MIB", "caqVccParamsInheritLevel"),
        ("CISCO-ATM-QOS-MIB", "caqVccParamsMcrIn"),
        ("CISCO-ATM-QOS-MIB", "caqVccParamsMcrOut"),
        ("CISCO-ATM-QOS-MIB", "caqVccParamsInvRdf"),
        ("CISCO-ATM-QOS-MIB", "caqVccParamsInvRif"),
        ("CISCO-ATM-QOS-MIB", "caqVccParamsRfl"))
)
if mibBuilder.loadTexts:
    ciscoAtmQosVccGroup.setStatus("current")

ciscoAtmQosVccAddon1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 2, 2, 2)
)
ciscoAtmQosVccAddon1Group.setObjects(
      *(("CISCO-ATM-QOS-MIB", "caqVccParamsCdv"),
        ("CISCO-ATM-QOS-MIB", "caqVccParamsCdvt"),
        ("CISCO-ATM-QOS-MIB", "caqVccParamsIcr"),
        ("CISCO-ATM-QOS-MIB", "caqVccParamsTbe"),
        ("CISCO-ATM-QOS-MIB", "caqVccParamsFrtt"),
        ("CISCO-ATM-QOS-MIB", "caqVccParamsNrm"),
        ("CISCO-ATM-QOS-MIB", "caqVccParamsInvTrm"),
        ("CISCO-ATM-QOS-MIB", "caqVccParamsInvCdf"),
        ("CISCO-ATM-QOS-MIB", "caqVccParamsAdtf"))
)
if mibBuilder.loadTexts:
    ciscoAtmQosVccAddon1Group.setStatus("current")

ciscoAtmQosVpcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 2, 2, 3)
)
ciscoAtmQosVpcGroup.setObjects(
      *(("CISCO-ATM-QOS-MIB", "caqVpcParamsVpState"),
        ("CISCO-ATM-QOS-MIB", "caqVpcParamsPeakRate"),
        ("CISCO-ATM-QOS-MIB", "caqVpcParamsCesRate"),
        ("CISCO-ATM-QOS-MIB", "caqVpcParamsDataVcCount"),
        ("CISCO-ATM-QOS-MIB", "caqVpcParamsCesVcCount"),
        ("CISCO-ATM-QOS-MIB", "caqVpcParamsVcdF4Seg"),
        ("CISCO-ATM-QOS-MIB", "caqVpcParamsVcdF4Ete"),
        ("CISCO-ATM-QOS-MIB", "caqVpcParamsScr"),
        ("CISCO-ATM-QOS-MIB", "caqVpcParamsMbs"))
)
if mibBuilder.loadTexts:
    ciscoAtmQosVpcGroup.setStatus("current")

ciscoAtmQosVpcAddon1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 2, 2, 4)
)
ciscoAtmQosVpcAddon1Group.setObjects(
    ("CISCO-ATM-QOS-MIB", "caqVpcParamsAvailBw")
)
if mibBuilder.loadTexts:
    ciscoAtmQosVpcAddon1Group.setStatus("current")

ciscoAtmQosVcQueuingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 2, 2, 5)
)
ciscoAtmQosVcQueuingGroup.setObjects(
      *(("CISCO-ATM-QOS-MIB", "caqQueuingParamsMeanQDepth"),
        ("CISCO-ATM-QOS-MIB", "caqQueuingParamsClassRandDrp"),
        ("CISCO-ATM-QOS-MIB", "caqQueuingParamsClassTailDrp"),
        ("CISCO-ATM-QOS-MIB", "caqQueuingParamsClassMinThre"),
        ("CISCO-ATM-QOS-MIB", "caqQueuingParamsClassMaxThre"),
        ("CISCO-ATM-QOS-MIB", "caqQueuingParamsClassMrkProb"))
)
if mibBuilder.loadTexts:
    ciscoAtmQosVcQueuingGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoAtmQosMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 279, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoAtmQosMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ATM-QOS-MIB",
    **{"VcParamConfigLocation": VcParamConfigLocation,
       "VpState": VpState,
       "ciscoAtmQosMIB": ciscoAtmQosMIB,
       "ciscoAtmQosMIBNotifs": ciscoAtmQosMIBNotifs,
       "ciscoAtmQosMIBObjects": ciscoAtmQosMIBObjects,
       "caqVccParams": caqVccParams,
       "caqVccParamsTable": caqVccParamsTable,
       "caqVccParamsEntry": caqVccParamsEntry,
       "caqVccParamsType": caqVccParamsType,
       "caqVccParamsPcrIn0": caqVccParamsPcrIn0,
       "caqVccParamsPcrIn01": caqVccParamsPcrIn01,
       "caqVccParamsPcrOut0": caqVccParamsPcrOut0,
       "caqVccParamsPcrOut01": caqVccParamsPcrOut01,
       "caqVccParamsScrIn0": caqVccParamsScrIn0,
       "caqVccParamsScrIn01": caqVccParamsScrIn01,
       "caqVccParamsScrOut0": caqVccParamsScrOut0,
       "caqVccParamsScrOut01": caqVccParamsScrOut01,
       "caqVccParamsBcsIn0": caqVccParamsBcsIn0,
       "caqVccParamsBcsIn01": caqVccParamsBcsIn01,
       "caqVccParamsBcsOut0": caqVccParamsBcsOut0,
       "caqVccParamsBcsOut01": caqVccParamsBcsOut01,
       "caqVccParamsInheritLevel": caqVccParamsInheritLevel,
       "caqVccParamsMcrIn": caqVccParamsMcrIn,
       "caqVccParamsMcrOut": caqVccParamsMcrOut,
       "caqVccParamsInvRdf": caqVccParamsInvRdf,
       "caqVccParamsInvRif": caqVccParamsInvRif,
       "caqVccParamsRfl": caqVccParamsRfl,
       "caqVccParamsCdv": caqVccParamsCdv,
       "caqVccParamsCdvt": caqVccParamsCdvt,
       "caqVccParamsIcr": caqVccParamsIcr,
       "caqVccParamsTbe": caqVccParamsTbe,
       "caqVccParamsFrtt": caqVccParamsFrtt,
       "caqVccParamsNrm": caqVccParamsNrm,
       "caqVccParamsInvTrm": caqVccParamsInvTrm,
       "caqVccParamsInvCdf": caqVccParamsInvCdf,
       "caqVccParamsAdtf": caqVccParamsAdtf,
       "caqVpcParams": caqVpcParams,
       "caqVpcParamsTable": caqVpcParamsTable,
       "caqVpcParamsEntry": caqVpcParamsEntry,
       "caqVpcParamsVpState": caqVpcParamsVpState,
       "caqVpcParamsPeakRate": caqVpcParamsPeakRate,
       "caqVpcParamsCesRate": caqVpcParamsCesRate,
       "caqVpcParamsDataVcCount": caqVpcParamsDataVcCount,
       "caqVpcParamsCesVcCount": caqVpcParamsCesVcCount,
       "caqVpcParamsVcdF4Seg": caqVpcParamsVcdF4Seg,
       "caqVpcParamsVcdF4Ete": caqVpcParamsVcdF4Ete,
       "caqVpcParamsScr": caqVpcParamsScr,
       "caqVpcParamsMbs": caqVpcParamsMbs,
       "caqVpcParamsAvailBw": caqVpcParamsAvailBw,
       "caqQueuingParams": caqQueuingParams,
       "caqQueuingParamsTable": caqQueuingParamsTable,
       "caqQueuingParamsEntry": caqQueuingParamsEntry,
       "caqQueuingParamsMeanQDepth": caqQueuingParamsMeanQDepth,
       "caqQueuingParamsClassTable": caqQueuingParamsClassTable,
       "caqQueuingParamsClassEntry": caqQueuingParamsClassEntry,
       "caqQueuingParamsClassIndex": caqQueuingParamsClassIndex,
       "caqQueuingParamsClassRandDrp": caqQueuingParamsClassRandDrp,
       "caqQueuingParamsClassTailDrp": caqQueuingParamsClassTailDrp,
       "caqQueuingParamsClassMinThre": caqQueuingParamsClassMinThre,
       "caqQueuingParamsClassMaxThre": caqQueuingParamsClassMaxThre,
       "caqQueuingParamsClassMrkProb": caqQueuingParamsClassMrkProb,
       "ciscoAtmQosMIBConform": ciscoAtmQosMIBConform,
       "ciscoAtmQosMIBCompliances": ciscoAtmQosMIBCompliances,
       "ciscoAtmQosMIBCompliance": ciscoAtmQosMIBCompliance,
       "ciscoAtmQosMIBGroups": ciscoAtmQosMIBGroups,
       "ciscoAtmQosVccGroup": ciscoAtmQosVccGroup,
       "ciscoAtmQosVccAddon1Group": ciscoAtmQosVccAddon1Group,
       "ciscoAtmQosVpcGroup": ciscoAtmQosVpcGroup,
       "ciscoAtmQosVpcAddon1Group": ciscoAtmQosVpcAddon1Group,
       "ciscoAtmQosVcQueuingGroup": ciscoAtmQosVcQueuingGroup}
)
