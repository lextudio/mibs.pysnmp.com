# SNMP MIB module (NBASE-G1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NBASE-G1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:43 2024
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



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nbase_ObjectIdentity = ObjectIdentity
nbase = _Nbase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629)
)
_NbSwitchG1_ObjectIdentity = ObjectIdentity
nbSwitchG1 = _NbSwitchG1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1)
)
_NbsProducts_ObjectIdentity = ObjectIdentity
nbsProducts = _NbsProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 1)
)
_MiniSwitch_ObjectIdentity = ObjectIdentity
miniSwitch = _MiniSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 1, 1)
)
_MegaSwitch208_ObjectIdentity = ObjectIdentity
megaSwitch208 = _MegaSwitch208_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 1, 2)
)
_MegaSwitch215_ObjectIdentity = ObjectIdentity
megaSwitch215 = _MegaSwitch215_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 1, 3)
)
_MegaFastSwitch_ObjectIdentity = ObjectIdentity
megaFastSwitch = _MegaFastSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 1, 4)
)
_MegaSwitchII_ObjectIdentity = ObjectIdentity
megaSwitchII = _MegaSwitchII_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 1, 5)
)
_MegaSwitch2015_ObjectIdentity = ObjectIdentity
megaSwitch2015 = _MegaSwitch2015_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 1, 6)
)
_MegaSwitch2048_ObjectIdentity = ObjectIdentity
megaSwitch2048 = _MegaSwitch2048_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 1, 7)
)
_NbsSys_ObjectIdentity = ObjectIdentity
nbsSys = _NbsSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 2)
)
_NbsSysFwVers_Type = DisplayString
_NbsSysFwVers_Object = MibScalar
nbsSysFwVers = _NbsSysFwVers_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 2, 1),
    _NbsSysFwVers_Type()
)
nbsSysFwVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSysFwVers.setStatus("mandatory")
_NbsSysPortsNumber_Type = Integer32
_NbsSysPortsNumber_Object = MibScalar
nbsSysPortsNumber = _NbsSysPortsNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 2, 2),
    _NbsSysPortsNumber_Type()
)
nbsSysPortsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSysPortsNumber.setStatus("mandatory")


class _NbsSysRestart_Type(Integer32):
    """Custom type nbsSysRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("coldRestart", 2),
          ("running", 1),
          ("warmRestart", 3))
    )


_NbsSysRestart_Type.__name__ = "Integer32"
_NbsSysRestart_Object = MibScalar
nbsSysRestart = _NbsSysRestart_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 2, 3),
    _NbsSysRestart_Type()
)
nbsSysRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysRestart.setStatus("mandatory")
_NbsSysNumRestarts_Type = Counter32
_NbsSysNumRestarts_Object = MibScalar
nbsSysNumRestarts = _NbsSysNumRestarts_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 2, 4),
    _NbsSysNumRestarts_Type()
)
nbsSysNumRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSysNumRestarts.setStatus("mandatory")


class _NbsSysLastError_Type(Integer32):
    """Custom type nbsSysLastError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("noError", 1)
    )


_NbsSysLastError_Type.__name__ = "Integer32"
_NbsSysLastError_Object = MibScalar
nbsSysLastError = _NbsSysLastError_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 2, 5),
    _NbsSysLastError_Type()
)
nbsSysLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSysLastError.setStatus("mandatory")
_NbsSysErrUptime_Type = TimeTicks
_NbsSysErrUptime_Object = MibScalar
nbsSysErrUptime = _NbsSysErrUptime_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 2, 6),
    _NbsSysErrUptime_Type()
)
nbsSysErrUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSysErrUptime.setStatus("mandatory")
_NbsSysSwitchDBSize_Type = Integer32
_NbsSysSwitchDBSize_Object = MibScalar
nbsSysSwitchDBSize = _NbsSysSwitchDBSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 2, 7),
    _NbsSysSwitchDBSize_Type()
)
nbsSysSwitchDBSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSysSwitchDBSize.setStatus("mandatory")


class _NbsSysSetNvramDefaults_Type(Integer32):
    """Custom type nbsSysSetNvramDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setDefaults", 1)
    )


_NbsSysSetNvramDefaults_Type.__name__ = "Integer32"
_NbsSysSetNvramDefaults_Object = MibScalar
nbsSysSetNvramDefaults = _NbsSysSetNvramDefaults_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 2, 8),
    _NbsSysSetNvramDefaults_Type()
)
nbsSysSetNvramDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysSetNvramDefaults.setStatus("mandatory")


class _NbsSysResetSwitchStats_Type(Integer32):
    """Custom type nbsSysResetSwitchStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetStats", 1)
    )


_NbsSysResetSwitchStats_Type.__name__ = "Integer32"
_NbsSysResetSwitchStats_Object = MibScalar
nbsSysResetSwitchStats = _NbsSysResetSwitchStats_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 2, 9),
    _NbsSysResetSwitchStats_Type()
)
nbsSysResetSwitchStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysResetSwitchStats.setStatus("mandatory")


class _NbsSysStpEnable_Type(Integer32):
    """Custom type nbsSysStpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stpDisable", 1),
          ("stpEnable", 2))
    )


_NbsSysStpEnable_Type.__name__ = "Integer32"
_NbsSysStpEnable_Object = MibScalar
nbsSysStpEnable = _NbsSysStpEnable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 2, 10),
    _NbsSysStpEnable_Type()
)
nbsSysStpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysStpEnable.setStatus("mandatory")


class _NbsSysRunStpState_Type(Integer32):
    """Custom type nbsSysRunStpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stpDisable", 1),
          ("stpEnable", 2))
    )


_NbsSysRunStpState_Type.__name__ = "Integer32"
_NbsSysRunStpState_Object = MibScalar
nbsSysRunStpState = _NbsSysRunStpState_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 2, 11),
    _NbsSysRunStpState_Type()
)
nbsSysRunStpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSysRunStpState.setStatus("mandatory")
_NbsSysFrmGen_ObjectIdentity = ObjectIdentity
nbsSysFrmGen = _NbsSysFrmGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 2, 12)
)


class _NbsSysFrmGenSession_Type(Integer32):
    """Custom type nbsSysFrmGenSession based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idleFG", 1),
          ("runFG", 2))
    )


_NbsSysFrmGenSession_Type.__name__ = "Integer32"
_NbsSysFrmGenSession_Object = MibScalar
nbsSysFrmGenSession = _NbsSysFrmGenSession_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 2, 12, 1),
    _NbsSysFrmGenSession_Type()
)
nbsSysFrmGenSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysFrmGenSession.setStatus("mandatory")


class _NbsSysFrmGenDa_Type(MacAddress):
    """Custom type nbsSysFrmGenDa based on MacAddress"""
    defaultHexValue = "000000000000"


_NbsSysFrmGenDa_Object = MibScalar
nbsSysFrmGenDa = _NbsSysFrmGenDa_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 2, 12, 2),
    _NbsSysFrmGenDa_Type()
)
nbsSysFrmGenDa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysFrmGenDa.setStatus("mandatory")


class _NbsSysFrmGenSa_Type(MacAddress):
    """Custom type nbsSysFrmGenSa based on MacAddress"""
    defaultHexValue = "000000000000"


_NbsSysFrmGenSa_Object = MibScalar
nbsSysFrmGenSa = _NbsSysFrmGenSa_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 2, 12, 3),
    _NbsSysFrmGenSa_Type()
)
nbsSysFrmGenSa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysFrmGenSa.setStatus("mandatory")
_NbsSysFrmGenPktFill_Type = Integer32
_NbsSysFrmGenPktFill_Object = MibScalar
nbsSysFrmGenPktFill = _NbsSysFrmGenPktFill_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 2, 12, 4),
    _NbsSysFrmGenPktFill_Type()
)
nbsSysFrmGenPktFill.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysFrmGenPktFill.setStatus("mandatory")
_NbsSysFrmGenPktRate_Type = Integer32
_NbsSysFrmGenPktRate_Object = MibScalar
nbsSysFrmGenPktRate = _NbsSysFrmGenPktRate_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 2, 12, 5),
    _NbsSysFrmGenPktRate_Type()
)
nbsSysFrmGenPktRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysFrmGenPktRate.setStatus("mandatory")
_NbsSysFrmGenDestMap_Type = OctetString
_NbsSysFrmGenDestMap_Object = MibScalar
nbsSysFrmGenDestMap = _NbsSysFrmGenDestMap_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 2, 12, 6),
    _NbsSysFrmGenDestMap_Type()
)
nbsSysFrmGenDestMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysFrmGenDestMap.setStatus("mandatory")
_NbsSysFrmGenPktNum_Type = Counter32
_NbsSysFrmGenPktNum_Object = MibScalar
nbsSysFrmGenPktNum = _NbsSysFrmGenPktNum_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 2, 12, 7),
    _NbsSysFrmGenPktNum_Type()
)
nbsSysFrmGenPktNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysFrmGenPktNum.setStatus("mandatory")
_NbsSysFrmGenPktLen_Type = Integer32
_NbsSysFrmGenPktLen_Object = MibScalar
nbsSysFrmGenPktLen = _NbsSysFrmGenPktLen_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 2, 12, 8),
    _NbsSysFrmGenPktLen_Type()
)
nbsSysFrmGenPktLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysFrmGenPktLen.setStatus("mandatory")
_NbsSysFrmGenXmtPktNum_Type = Counter32
_NbsSysFrmGenXmtPktNum_Object = MibScalar
nbsSysFrmGenXmtPktNum = _NbsSysFrmGenXmtPktNum_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 2, 12, 9),
    _NbsSysFrmGenXmtPktNum_Type()
)
nbsSysFrmGenXmtPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSysFrmGenXmtPktNum.setStatus("mandatory")


class _NbsSysSelftestLevel_Type(Integer32):
    """Custom type nbsSysSelftestLevel based on Integer32"""
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
        *(("ststDiagnostics", 4),
          ("ststLong", 3),
          ("ststNone", 1),
          ("ststShort", 2))
    )


_NbsSysSelftestLevel_Type.__name__ = "Integer32"
_NbsSysSelftestLevel_Object = MibScalar
nbsSysSelftestLevel = _NbsSysSelftestLevel_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 2, 13),
    _NbsSysSelftestLevel_Type()
)
nbsSysSelftestLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysSelftestLevel.setStatus("mandatory")
_NbsSysSnmpCfg_ObjectIdentity = ObjectIdentity
nbsSysSnmpCfg = _NbsSysSnmpCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 3)
)
_NbsSysIpAddr_Type = IpAddress
_NbsSysIpAddr_Object = MibScalar
nbsSysIpAddr = _NbsSysIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 3, 1),
    _NbsSysIpAddr_Type()
)
nbsSysIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysIpAddr.setStatus("mandatory")
_NbsSysNetMask_Type = IpAddress
_NbsSysNetMask_Object = MibScalar
nbsSysNetMask = _NbsSysNetMask_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 3, 2),
    _NbsSysNetMask_Type()
)
nbsSysNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysNetMask.setStatus("mandatory")
_NbsSysBcastAddr_Type = IpAddress
_NbsSysBcastAddr_Object = MibScalar
nbsSysBcastAddr = _NbsSysBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 3, 3),
    _NbsSysBcastAddr_Type()
)
nbsSysBcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysBcastAddr.setStatus("mandatory")
_NbsSysObIpAddr_Type = IpAddress
_NbsSysObIpAddr_Object = MibScalar
nbsSysObIpAddr = _NbsSysObIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 3, 4),
    _NbsSysObIpAddr_Type()
)
nbsSysObIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysObIpAddr.setStatus("mandatory")
_NbsSysObNetMask_Type = IpAddress
_NbsSysObNetMask_Object = MibScalar
nbsSysObNetMask = _NbsSysObNetMask_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 3, 5),
    _NbsSysObNetMask_Type()
)
nbsSysObNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysObNetMask.setStatus("mandatory")
_NbsSysObBcastAddr_Type = IpAddress
_NbsSysObBcastAddr_Object = MibScalar
nbsSysObBcastAddr = _NbsSysObBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 3, 6),
    _NbsSysObBcastAddr_Type()
)
nbsSysObBcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysObBcastAddr.setStatus("mandatory")
_NbsSysDefaultGateway_Type = IpAddress
_NbsSysDefaultGateway_Object = MibScalar
nbsSysDefaultGateway = _NbsSysDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 3, 7),
    _NbsSysDefaultGateway_Type()
)
nbsSysDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysDefaultGateway.setStatus("mandatory")


class _NbsSysReadComunity_Type(DisplayString):
    """Custom type nbsSysReadComunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_NbsSysReadComunity_Type.__name__ = "DisplayString"
_NbsSysReadComunity_Object = MibScalar
nbsSysReadComunity = _NbsSysReadComunity_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 3, 8),
    _NbsSysReadComunity_Type()
)
nbsSysReadComunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysReadComunity.setStatus("mandatory")


class _NbsSysWriteComunity_Type(DisplayString):
    """Custom type nbsSysWriteComunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_NbsSysWriteComunity_Type.__name__ = "DisplayString"
_NbsSysWriteComunity_Object = MibScalar
nbsSysWriteComunity = _NbsSysWriteComunity_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 3, 9),
    _NbsSysWriteComunity_Type()
)
nbsSysWriteComunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysWriteComunity.setStatus("mandatory")


class _NbsSysBootpEnable_Type(Integer32):
    """Custom type nbsSysBootpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NbsSysBootpEnable_Type.__name__ = "Integer32"
_NbsSysBootpEnable_Object = MibScalar
nbsSysBootpEnable = _NbsSysBootpEnable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 3, 10),
    _NbsSysBootpEnable_Type()
)
nbsSysBootpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysBootpEnable.setStatus("mandatory")
_NbsSysTrapTblMaxSize_Type = Integer32
_NbsSysTrapTblMaxSize_Object = MibScalar
nbsSysTrapTblMaxSize = _NbsSysTrapTblMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 3, 11),
    _NbsSysTrapTblMaxSize_Type()
)
nbsSysTrapTblMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSysTrapTblMaxSize.setStatus("mandatory")
_NbsSysTrapTable_Object = MibTable
nbsSysTrapTable = _NbsSysTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 3, 12)
)
if mibBuilder.loadTexts:
    nbsSysTrapTable.setStatus("mandatory")
_NbsSysTrapEntry_Object = MibTableRow
nbsSysTrapEntry = _NbsSysTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 3, 12, 1)
)
nbsSysTrapEntry.setIndexNames(
    (0, "NBASE-G1-MIB", "nbsSysTrapTblEntIndex"),
)
if mibBuilder.loadTexts:
    nbsSysTrapEntry.setStatus("mandatory")
_NbsSysTrapTblEntIndex_Type = Integer32
_NbsSysTrapTblEntIndex_Object = MibTableColumn
nbsSysTrapTblEntIndex = _NbsSysTrapTblEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 3, 12, 1, 1),
    _NbsSysTrapTblEntIndex_Type()
)
nbsSysTrapTblEntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSysTrapTblEntIndex.setStatus("mandatory")


class _NbsSysTrapTblEntStatus_Type(Integer32):
    """Custom type nbsSysTrapTblEntStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("invalid", 1))
    )


_NbsSysTrapTblEntStatus_Type.__name__ = "Integer32"
_NbsSysTrapTblEntStatus_Object = MibTableColumn
nbsSysTrapTblEntStatus = _NbsSysTrapTblEntStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 3, 12, 1, 2),
    _NbsSysTrapTblEntStatus_Type()
)
nbsSysTrapTblEntStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysTrapTblEntStatus.setStatus("mandatory")
_NbsSysTrapTblEntIpAddr_Type = IpAddress
_NbsSysTrapTblEntIpAddr_Object = MibTableColumn
nbsSysTrapTblEntIpAddr = _NbsSysTrapTblEntIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 3, 12, 1, 3),
    _NbsSysTrapTblEntIpAddr_Type()
)
nbsSysTrapTblEntIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysTrapTblEntIpAddr.setStatus("mandatory")
_NbsSysTrapTblEntComm_Type = DisplayString
_NbsSysTrapTblEntComm_Object = MibTableColumn
nbsSysTrapTblEntComm = _NbsSysTrapTblEntComm_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 3, 12, 1, 4),
    _NbsSysTrapTblEntComm_Type()
)
nbsSysTrapTblEntComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysTrapTblEntComm.setStatus("mandatory")
_NbsSysTftpSwFileName_Type = DisplayString
_NbsSysTftpSwFileName_Object = MibScalar
nbsSysTftpSwFileName = _NbsSysTftpSwFileName_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 3, 13),
    _NbsSysTftpSwFileName_Type()
)
nbsSysTftpSwFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysTftpSwFileName.setStatus("mandatory")
_NbsSysTftpParFileName_Type = DisplayString
_NbsSysTftpParFileName_Object = MibScalar
nbsSysTftpParFileName = _NbsSysTftpParFileName_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 3, 14),
    _NbsSysTftpParFileName_Type()
)
nbsSysTftpParFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysTftpParFileName.setStatus("mandatory")


class _NbsSysSerialLineMode_Type(Integer32):
    """Custom type nbsSysSerialLineMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adminIf", 1),
          ("slipIf", 2))
    )


_NbsSysSerialLineMode_Type.__name__ = "Integer32"
_NbsSysSerialLineMode_Object = MibScalar
nbsSysSerialLineMode = _NbsSysSerialLineMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 3, 15),
    _NbsSysSerialLineMode_Type()
)
nbsSysSerialLineMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysSerialLineMode.setStatus("mandatory")


class _NbsSysSerialSlipBaudRate_Type(Integer32):
    """Custom type nbsSysSerialSlipBaudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("b19200", 2),
          ("b38400", 3),
          ("b9600", 1))
    )


_NbsSysSerialSlipBaudRate_Type.__name__ = "Integer32"
_NbsSysSerialSlipBaudRate_Object = MibScalar
nbsSysSerialSlipBaudRate = _NbsSysSerialSlipBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 3, 16),
    _NbsSysSerialSlipBaudRate_Type()
)
nbsSysSerialSlipBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysSerialSlipBaudRate.setStatus("mandatory")


class _NbsSysTelnetSession_Type(Integer32):
    """Custom type nbsSysTelnetSession based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnect", 2))
    )


_NbsSysTelnetSession_Type.__name__ = "Integer32"
_NbsSysTelnetSession_Object = MibScalar
nbsSysTelnetSession = _NbsSysTelnetSession_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 3, 17),
    _NbsSysTelnetSession_Type()
)
nbsSysTelnetSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSysTelnetSession.setStatus("mandatory")
_NbsSysPing_ObjectIdentity = ObjectIdentity
nbsSysPing = _NbsSysPing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 3, 18)
)


class _NbsSysPingSession_Type(Integer32):
    """Custom type nbsSysPingSession based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idlePing", 1),
          ("runPing", 2))
    )


_NbsSysPingSession_Type.__name__ = "Integer32"
_NbsSysPingSession_Object = MibScalar
nbsSysPingSession = _NbsSysPingSession_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 3, 18, 1),
    _NbsSysPingSession_Type()
)
nbsSysPingSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysPingSession.setStatus("mandatory")


class _NbsSysPingAddr_Type(IpAddress):
    """Custom type nbsSysPingAddr based on IpAddress"""
    defaultHexValue = "7F000001"


_NbsSysPingAddr_Object = MibScalar
nbsSysPingAddr = _NbsSysPingAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 3, 18, 2),
    _NbsSysPingAddr_Type()
)
nbsSysPingAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysPingAddr.setStatus("mandatory")
_NbsSysPingNumber_Type = Counter32
_NbsSysPingNumber_Object = MibScalar
nbsSysPingNumber = _NbsSysPingNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 3, 18, 3),
    _NbsSysPingNumber_Type()
)
nbsSysPingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysPingNumber.setStatus("mandatory")
_NbsSysPingRequests_Type = Counter32
_NbsSysPingRequests_Object = MibScalar
nbsSysPingRequests = _NbsSysPingRequests_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 3, 18, 4),
    _NbsSysPingRequests_Type()
)
nbsSysPingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSysPingRequests.setStatus("mandatory")
_NbsSysPingResps_Type = Integer32
_NbsSysPingResps_Object = MibScalar
nbsSysPingResps = _NbsSysPingResps_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 3, 18, 5),
    _NbsSysPingResps_Type()
)
nbsSysPingResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSysPingResps.setStatus("mandatory")


class _NbsSysPingOwner_Type(Integer32):
    """Custom type nbsSysPingOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adminInterface", 1),
          ("snmpAgent", 2))
    )


_NbsSysPingOwner_Type.__name__ = "Integer32"
_NbsSysPingOwner_Object = MibScalar
nbsSysPingOwner = _NbsSysPingOwner_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 3, 18, 6),
    _NbsSysPingOwner_Type()
)
nbsSysPingOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSysPingOwner.setStatus("mandatory")
_NbsSysTelnetHost_Type = IpAddress
_NbsSysTelnetHost_Object = MibScalar
nbsSysTelnetHost = _NbsSysTelnetHost_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 3, 19),
    _NbsSysTelnetHost_Type()
)
nbsSysTelnetHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSysTelnetHost.setStatus("mandatory")
_NbsSysTftpRswFileName_Type = DisplayString
_NbsSysTftpRswFileName_Object = MibScalar
nbsSysTftpRswFileName = _NbsSysTftpRswFileName_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 3, 20),
    _NbsSysTftpRswFileName_Type()
)
nbsSysTftpRswFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysTftpRswFileName.setStatus("mandatory")
_NbsSysTftpServerIP_Type = IpAddress
_NbsSysTftpServerIP_Object = MibScalar
nbsSysTftpServerIP = _NbsSysTftpServerIP_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 3, 21),
    _NbsSysTftpServerIP_Type()
)
nbsSysTftpServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysTftpServerIP.setStatus("mandatory")


class _NbsSysInitDownload_Type(Integer32):
    """Custom type nbsSysInitDownload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("activeAppl", 3),
          ("inactive", 2))
    )


_NbsSysInitDownload_Type.__name__ = "Integer32"
_NbsSysInitDownload_Object = MibScalar
nbsSysInitDownload = _NbsSysInitDownload_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 3, 22),
    _NbsSysInitDownload_Type()
)
nbsSysInitDownload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysInitDownload.setStatus("mandatory")


class _NbsSysParDownload_Type(Integer32):
    """Custom type nbsSysParDownload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_NbsSysParDownload_Type.__name__ = "Integer32"
_NbsSysParDownload_Object = MibScalar
nbsSysParDownload = _NbsSysParDownload_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 3, 23),
    _NbsSysParDownload_Type()
)
nbsSysParDownload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysParDownload.setStatus("mandatory")


class _NbsSysParUpload_Type(Integer32):
    """Custom type nbsSysParUpload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_NbsSysParUpload_Type.__name__ = "Integer32"
_NbsSysParUpload_Object = MibScalar
nbsSysParUpload = _NbsSysParUpload_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 3, 24),
    _NbsSysParUpload_Type()
)
nbsSysParUpload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSysParUpload.setStatus("mandatory")
_NbsPortCfg_ObjectIdentity = ObjectIdentity
nbsPortCfg = _NbsPortCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 4)
)
_NbsPortCfgTable_Object = MibTable
nbsPortCfgTable = _NbsPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 4, 1)
)
if mibBuilder.loadTexts:
    nbsPortCfgTable.setStatus("mandatory")
_NbsPortCfgEntry_Object = MibTableRow
nbsPortCfgEntry = _NbsPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 4, 1, 1)
)
nbsPortCfgEntry.setIndexNames(
    (0, "NBASE-G1-MIB", "nbsPortCfgIndex"),
)
if mibBuilder.loadTexts:
    nbsPortCfgEntry.setStatus("mandatory")
_NbsPortCfgIndex_Type = Integer32
_NbsPortCfgIndex_Object = MibTableColumn
nbsPortCfgIndex = _NbsPortCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 4, 1, 1, 1),
    _NbsPortCfgIndex_Type()
)
nbsPortCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPortCfgIndex.setStatus("mandatory")


class _NbsPortCfgLanType_Type(Integer32):
    """Custom type nbsPortCfgLanType based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("atmLane", 7),
          ("eth10", 2),
          ("eth10-100", 4),
          ("eth10-100Grp", 9),
          ("eth100", 3),
          ("eth100-1000", 11),
          ("eth1000B", 6),
          ("eth100B", 5),
          ("eth100Grp", 8),
          ("fddi", 10),
          ("none", 1))
    )


_NbsPortCfgLanType_Type.__name__ = "Integer32"
_NbsPortCfgLanType_Object = MibTableColumn
nbsPortCfgLanType = _NbsPortCfgLanType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 4, 1, 1, 2),
    _NbsPortCfgLanType_Type()
)
nbsPortCfgLanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPortCfgLanType.setStatus("mandatory")


class _NbsPortCfgIfType_Type(Integer32):
    """Custom type nbsPortCfgIfType based on Integer32"""
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
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("aui", 1),
          ("auiTp", 3),
          ("coax", 5),
          ("foLxM", 10),
          ("foLxS1", 11),
          ("foLxS2", 12),
          ("foLxS3", 13),
          ("foLxS4", 19),
          ("foLxS5", 20),
          ("foM", 14),
          ("foM-10", 23),
          ("foMX", 15),
          ("foMm", 6),
          ("foS1", 16),
          ("foS2", 17),
          ("foS3", 18),
          ("foS4", 21),
          ("foS5", 22),
          ("foSm", 7),
          ("foSxM", 9),
          ("none", 8),
          ("tp", 2),
          ("tpfd", 4))
    )


_NbsPortCfgIfType_Type.__name__ = "Integer32"
_NbsPortCfgIfType_Object = MibTableColumn
nbsPortCfgIfType = _NbsPortCfgIfType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 4, 1, 1, 3),
    _NbsPortCfgIfType_Type()
)
nbsPortCfgIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPortCfgIfType.setStatus("mandatory")


class _NbsPortCfgPortSelect_Type(Integer32):
    """Custom type nbsPortCfgPortSelect based on Integer32"""
    defaultValue = 4

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
        *(("asel", 4),
          ("aui", 2),
          ("other", 1),
          ("tp", 3))
    )


_NbsPortCfgPortSelect_Type.__name__ = "Integer32"
_NbsPortCfgPortSelect_Object = MibTableColumn
nbsPortCfgPortSelect = _NbsPortCfgPortSelect_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 4, 1, 1, 4),
    _NbsPortCfgPortSelect_Type()
)
nbsPortCfgPortSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsPortCfgPortSelect.setStatus("mandatory")


class _NbsPortCfgIfLink_Type(Integer32):
    """Custom type nbsPortCfgIfLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_NbsPortCfgIfLink_Type.__name__ = "Integer32"
_NbsPortCfgIfLink_Object = MibTableColumn
nbsPortCfgIfLink = _NbsPortCfgIfLink_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 4, 1, 1, 5),
    _NbsPortCfgIfLink_Type()
)
nbsPortCfgIfLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPortCfgIfLink.setStatus("mandatory")


class _NbsPortCfgPortFctrl_Type(Integer32):
    """Custom type nbsPortCfgPortFctrl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NbsPortCfgPortFctrl_Type.__name__ = "Integer32"
_NbsPortCfgPortFctrl_Object = MibTableColumn
nbsPortCfgPortFctrl = _NbsPortCfgPortFctrl_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 4, 1, 1, 6),
    _NbsPortCfgPortFctrl_Type()
)
nbsPortCfgPortFctrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsPortCfgPortFctrl.setStatus("mandatory")


class _NbsPortCfgPortDplex_Type(Integer32):
    """Custom type nbsPortCfgPortDplex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 2),
          ("halfDuplex", 1))
    )


_NbsPortCfgPortDplex_Type.__name__ = "Integer32"
_NbsPortCfgPortDplex_Object = MibTableColumn
nbsPortCfgPortDplex = _NbsPortCfgPortDplex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 4, 1, 1, 7),
    _NbsPortCfgPortDplex_Type()
)
nbsPortCfgPortDplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsPortCfgPortDplex.setStatus("mandatory")


class _NbsPortCfgPortDelay_Type(Integer32):
    """Custom type nbsPortCfgPortDelay based on Integer32"""
    defaultValue = 64


_NbsPortCfgPortDelay_Object = MibTableColumn
nbsPortCfgPortDelay = _NbsPortCfgPortDelay_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 4, 1, 1, 8),
    _NbsPortCfgPortDelay_Type()
)
nbsPortCfgPortDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsPortCfgPortDelay.setStatus("mandatory")


class _NbsPortCfgSpeedSelect_Type(Integer32):
    """Custom type nbsPortCfgSpeedSelect based on Integer32"""
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
        *(("autoSense", 1),
          ("force10", 2),
          ("force100", 3),
          ("force1000", 4))
    )


_NbsPortCfgSpeedSelect_Type.__name__ = "Integer32"
_NbsPortCfgSpeedSelect_Object = MibTableColumn
nbsPortCfgSpeedSelect = _NbsPortCfgSpeedSelect_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 4, 1, 1, 9),
    _NbsPortCfgSpeedSelect_Type()
)
nbsPortCfgSpeedSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsPortCfgSpeedSelect.setStatus("mandatory")


class _NbsPortCfgEnable_Type(Integer32):
    """Custom type nbsPortCfgEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portDisable", 1),
          ("portEnable", 2))
    )


_NbsPortCfgEnable_Type.__name__ = "Integer32"
_NbsPortCfgEnable_Object = MibTableColumn
nbsPortCfgEnable = _NbsPortCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 4, 1, 1, 10),
    _NbsPortCfgEnable_Type()
)
nbsPortCfgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsPortCfgEnable.setStatus("mandatory")


class _NbsPortCfgIsvpMode_Type(Integer32):
    """Custom type nbsPortCfgIsvpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("nonIsvp", 3),
          ("trunk", 2))
    )


_NbsPortCfgIsvpMode_Type.__name__ = "Integer32"
_NbsPortCfgIsvpMode_Object = MibTableColumn
nbsPortCfgIsvpMode = _NbsPortCfgIsvpMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 4, 1, 1, 11),
    _NbsPortCfgIsvpMode_Type()
)
nbsPortCfgIsvpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsPortCfgIsvpMode.setStatus("mandatory")
_NbsPortGrpCfgNum_Type = Integer32
_NbsPortGrpCfgNum_Object = MibScalar
nbsPortGrpCfgNum = _NbsPortGrpCfgNum_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 4, 2),
    _NbsPortGrpCfgNum_Type()
)
nbsPortGrpCfgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPortGrpCfgNum.setStatus("mandatory")
_NbsPortGrpCfgTable_Object = MibTable
nbsPortGrpCfgTable = _NbsPortGrpCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 4, 3)
)
if mibBuilder.loadTexts:
    nbsPortGrpCfgTable.setStatus("mandatory")
_NbsPortGrpCfgEntry_Object = MibTableRow
nbsPortGrpCfgEntry = _NbsPortGrpCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 4, 3, 1)
)
nbsPortGrpCfgEntry.setIndexNames(
    (0, "NBASE-G1-MIB", "nbsPortGrpCfgIndex"),
)
if mibBuilder.loadTexts:
    nbsPortGrpCfgEntry.setStatus("mandatory")
_NbsPortGrpCfgIndex_Type = Integer32
_NbsPortGrpCfgIndex_Object = MibTableColumn
nbsPortGrpCfgIndex = _NbsPortGrpCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 4, 3, 1, 1),
    _NbsPortGrpCfgIndex_Type()
)
nbsPortGrpCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPortGrpCfgIndex.setStatus("mandatory")
_NbsPortGrpCfgGrpNumber_Type = Integer32
_NbsPortGrpCfgGrpNumber_Object = MibTableColumn
nbsPortGrpCfgGrpNumber = _NbsPortGrpCfgGrpNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 4, 3, 1, 2),
    _NbsPortGrpCfgGrpNumber_Type()
)
nbsPortGrpCfgGrpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPortGrpCfgGrpNumber.setStatus("mandatory")
_NbsPortGrpCfgPortNumber_Type = Integer32
_NbsPortGrpCfgPortNumber_Object = MibTableColumn
nbsPortGrpCfgPortNumber = _NbsPortGrpCfgPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 4, 3, 1, 3),
    _NbsPortGrpCfgPortNumber_Type()
)
nbsPortGrpCfgPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPortGrpCfgPortNumber.setStatus("mandatory")


class _NbsPortGrpCfgLinkStatus_Type(Integer32):
    """Custom type nbsPortGrpCfgLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkOff", 1),
          ("linkOn", 2))
    )


_NbsPortGrpCfgLinkStatus_Type.__name__ = "Integer32"
_NbsPortGrpCfgLinkStatus_Object = MibTableColumn
nbsPortGrpCfgLinkStatus = _NbsPortGrpCfgLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 4, 3, 1, 4),
    _NbsPortGrpCfgLinkStatus_Type()
)
nbsPortGrpCfgLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPortGrpCfgLinkStatus.setStatus("mandatory")


class _NbsPortGrpCfgActivity_Type(Integer32):
    """Custom type nbsPortGrpCfgActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activity", 2),
          ("nonActivity", 1))
    )


_NbsPortGrpCfgActivity_Type.__name__ = "Integer32"
_NbsPortGrpCfgActivity_Object = MibTableColumn
nbsPortGrpCfgActivity = _NbsPortGrpCfgActivity_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 4, 3, 1, 5),
    _NbsPortGrpCfgActivity_Type()
)
nbsPortGrpCfgActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPortGrpCfgActivity.setStatus("mandatory")
_NbsEtherInfo_ObjectIdentity = ObjectIdentity
nbsEtherInfo = _NbsEtherInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 5)
)
_NbsEthInfoTable_Object = MibTable
nbsEthInfoTable = _NbsEthInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 5, 1)
)
if mibBuilder.loadTexts:
    nbsEthInfoTable.setStatus("mandatory")
_NbsEthInfoEntry_Object = MibTableRow
nbsEthInfoEntry = _NbsEthInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 5, 1, 1)
)
nbsEthInfoEntry.setIndexNames(
    (0, "NBASE-G1-MIB", "nbsEthInfoIndex"),
)
if mibBuilder.loadTexts:
    nbsEthInfoEntry.setStatus("mandatory")
_NbsEthInfoIndex_Type = Integer32
_NbsEthInfoIndex_Object = MibTableColumn
nbsEthInfoIndex = _NbsEthInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 5, 1, 1, 1),
    _NbsEthInfoIndex_Type()
)
nbsEthInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEthInfoIndex.setStatus("mandatory")
_NbsEthInfoCntFctrls_Type = Counter32
_NbsEthInfoCntFctrls_Object = MibTableColumn
nbsEthInfoCntFctrls = _NbsEthInfoCntFctrls_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 5, 1, 1, 2),
    _NbsEthInfoCntFctrls_Type()
)
nbsEthInfoCntFctrls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEthInfoCntFctrls.setStatus("mandatory")
_NbsEthInfoCntExcessFctrls_Type = Counter32
_NbsEthInfoCntExcessFctrls_Object = MibTableColumn
nbsEthInfoCntExcessFctrls = _NbsEthInfoCntExcessFctrls_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 5, 1, 1, 3),
    _NbsEthInfoCntExcessFctrls_Type()
)
nbsEthInfoCntExcessFctrls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEthInfoCntExcessFctrls.setStatus("mandatory")
_NbsSwitchPerf_ObjectIdentity = ObjectIdentity
nbsSwitchPerf = _NbsSwitchPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 6)
)
_NbsSwitchPerfTable_Object = MibTable
nbsSwitchPerfTable = _NbsSwitchPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 6, 1)
)
if mibBuilder.loadTexts:
    nbsSwitchPerfTable.setStatus("mandatory")
_NbsSwitchPerfEntry_Object = MibTableRow
nbsSwitchPerfEntry = _NbsSwitchPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 6, 1, 1)
)
nbsSwitchPerfEntry.setIndexNames(
    (0, "NBASE-G1-MIB", "nbsSwitchPerfIndex"),
)
if mibBuilder.loadTexts:
    nbsSwitchPerfEntry.setStatus("mandatory")
_NbsSwitchPerfIndex_Type = Integer32
_NbsSwitchPerfIndex_Object = MibTableColumn
nbsSwitchPerfIndex = _NbsSwitchPerfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 6, 1, 1, 1),
    _NbsSwitchPerfIndex_Type()
)
nbsSwitchPerfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSwitchPerfIndex.setStatus("mandatory")
_NbsSwitchPerfMcastPkts_Type = Counter32
_NbsSwitchPerfMcastPkts_Object = MibTableColumn
nbsSwitchPerfMcastPkts = _NbsSwitchPerfMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 6, 1, 1, 2),
    _NbsSwitchPerfMcastPkts_Type()
)
nbsSwitchPerfMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSwitchPerfMcastPkts.setStatus("mandatory")
_NbsSwitchPerfUnknPkts_Type = Counter32
_NbsSwitchPerfUnknPkts_Object = MibTableColumn
nbsSwitchPerfUnknPkts = _NbsSwitchPerfUnknPkts_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 6, 1, 1, 3),
    _NbsSwitchPerfUnknPkts_Type()
)
nbsSwitchPerfUnknPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSwitchPerfUnknPkts.setStatus("mandatory")
_NbsPortFwdPerfTable_Object = MibTable
nbsPortFwdPerfTable = _NbsPortFwdPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 6, 2)
)
if mibBuilder.loadTexts:
    nbsPortFwdPerfTable.setStatus("mandatory")
_NbsPortFwdPerfEntry_Object = MibTableRow
nbsPortFwdPerfEntry = _NbsPortFwdPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 6, 2, 1)
)
nbsPortFwdPerfEntry.setIndexNames(
    (0, "NBASE-G1-MIB", "nbsPortFwdPerfInPort"),
    (0, "NBASE-G1-MIB", "nbsPortFwdPerfOutPort"),
)
if mibBuilder.loadTexts:
    nbsPortFwdPerfEntry.setStatus("mandatory")
_NbsPortFwdPerfInPort_Type = Integer32
_NbsPortFwdPerfInPort_Object = MibTableColumn
nbsPortFwdPerfInPort = _NbsPortFwdPerfInPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 6, 2, 1, 1),
    _NbsPortFwdPerfInPort_Type()
)
nbsPortFwdPerfInPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPortFwdPerfInPort.setStatus("mandatory")
_NbsPortFwdPerfOutPort_Type = Integer32
_NbsPortFwdPerfOutPort_Object = MibTableColumn
nbsPortFwdPerfOutPort = _NbsPortFwdPerfOutPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 6, 2, 1, 2),
    _NbsPortFwdPerfOutPort_Type()
)
nbsPortFwdPerfOutPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPortFwdPerfOutPort.setStatus("mandatory")
_NbsPortFwdPerfFwdPkts_Type = Counter32
_NbsPortFwdPerfFwdPkts_Object = MibTableColumn
nbsPortFwdPerfFwdPkts = _NbsPortFwdPerfFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 6, 2, 1, 3),
    _NbsPortFwdPerfFwdPkts_Type()
)
nbsPortFwdPerfFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPortFwdPerfFwdPkts.setStatus("mandatory")
_NbsPortFwdPerfFwdBytes_Type = Counter32
_NbsPortFwdPerfFwdBytes_Object = MibTableColumn
nbsPortFwdPerfFwdBytes = _NbsPortFwdPerfFwdBytes_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 6, 2, 1, 4),
    _NbsPortFwdPerfFwdBytes_Type()
)
nbsPortFwdPerfFwdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPortFwdPerfFwdBytes.setStatus("mandatory")
_NbsMgmtPerfStats_ObjectIdentity = ObjectIdentity
nbsMgmtPerfStats = _NbsMgmtPerfStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 6, 3)
)
_NbsMgmtPerfRcvdPkts_Type = Counter32
_NbsMgmtPerfRcvdPkts_Object = MibScalar
nbsMgmtPerfRcvdPkts = _NbsMgmtPerfRcvdPkts_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 6, 3, 1),
    _NbsMgmtPerfRcvdPkts_Type()
)
nbsMgmtPerfRcvdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMgmtPerfRcvdPkts.setStatus("mandatory")
_NbsMgmtPerfRcvdBytes_Type = Counter32
_NbsMgmtPerfRcvdBytes_Object = MibScalar
nbsMgmtPerfRcvdBytes = _NbsMgmtPerfRcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 6, 3, 2),
    _NbsMgmtPerfRcvdBytes_Type()
)
nbsMgmtPerfRcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMgmtPerfRcvdBytes.setStatus("mandatory")
_NbsMgmtPerfFilterdPkts_Type = Counter32
_NbsMgmtPerfFilterdPkts_Object = MibScalar
nbsMgmtPerfFilterdPkts = _NbsMgmtPerfFilterdPkts_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 6, 3, 3),
    _NbsMgmtPerfFilterdPkts_Type()
)
nbsMgmtPerfFilterdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMgmtPerfFilterdPkts.setStatus("mandatory")
_NbsMgmtPerfRcvBcastPkts_Type = Counter32
_NbsMgmtPerfRcvBcastPkts_Object = MibScalar
nbsMgmtPerfRcvBcastPkts = _NbsMgmtPerfRcvBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 6, 3, 4),
    _NbsMgmtPerfRcvBcastPkts_Type()
)
nbsMgmtPerfRcvBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMgmtPerfRcvBcastPkts.setStatus("mandatory")
_NbsMgmtPerfXmtPkts_Type = Counter32
_NbsMgmtPerfXmtPkts_Object = MibScalar
nbsMgmtPerfXmtPkts = _NbsMgmtPerfXmtPkts_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 6, 3, 5),
    _NbsMgmtPerfXmtPkts_Type()
)
nbsMgmtPerfXmtPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMgmtPerfXmtPkts.setStatus("mandatory")
_NbsMgmtPerfXmtUcastPkts_Type = Counter32
_NbsMgmtPerfXmtUcastPkts_Object = MibScalar
nbsMgmtPerfXmtUcastPkts = _NbsMgmtPerfXmtUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 6, 3, 6),
    _NbsMgmtPerfXmtUcastPkts_Type()
)
nbsMgmtPerfXmtUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMgmtPerfXmtUcastPkts.setStatus("mandatory")
_NbsMgmtPerfXmtMcastPkts_Type = Counter32
_NbsMgmtPerfXmtMcastPkts_Object = MibScalar
nbsMgmtPerfXmtMcastPkts = _NbsMgmtPerfXmtMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 6, 3, 7),
    _NbsMgmtPerfXmtMcastPkts_Type()
)
nbsMgmtPerfXmtMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMgmtPerfXmtMcastPkts.setStatus("mandatory")
_NbsMgmtPerfXmtBcastPkts_Type = Counter32
_NbsMgmtPerfXmtBcastPkts_Object = MibScalar
nbsMgmtPerfXmtBcastPkts = _NbsMgmtPerfXmtBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 6, 3, 8),
    _NbsMgmtPerfXmtBcastPkts_Type()
)
nbsMgmtPerfXmtBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMgmtPerfXmtBcastPkts.setStatus("mandatory")
_NbsMgmtRcvPerfTable_Object = MibTable
nbsMgmtRcvPerfTable = _NbsMgmtRcvPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 6, 4)
)
if mibBuilder.loadTexts:
    nbsMgmtRcvPerfTable.setStatus("mandatory")
_NbsMgmtRcvPerfEntry_Object = MibTableRow
nbsMgmtRcvPerfEntry = _NbsMgmtRcvPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 6, 4, 1)
)
nbsMgmtRcvPerfEntry.setIndexNames(
    (0, "NBASE-G1-MIB", "nbsMgmtRcvPerfInPort"),
)
if mibBuilder.loadTexts:
    nbsMgmtRcvPerfEntry.setStatus("mandatory")
_NbsMgmtRcvPerfInPort_Type = Integer32
_NbsMgmtRcvPerfInPort_Object = MibTableColumn
nbsMgmtRcvPerfInPort = _NbsMgmtRcvPerfInPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 6, 4, 1, 2),
    _NbsMgmtRcvPerfInPort_Type()
)
nbsMgmtRcvPerfInPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMgmtRcvPerfInPort.setStatus("mandatory")
_NbsMgmtRcvPerfFwdPkts_Type = Counter32
_NbsMgmtRcvPerfFwdPkts_Object = MibTableColumn
nbsMgmtRcvPerfFwdPkts = _NbsMgmtRcvPerfFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 6, 4, 1, 3),
    _NbsMgmtRcvPerfFwdPkts_Type()
)
nbsMgmtRcvPerfFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMgmtRcvPerfFwdPkts.setStatus("mandatory")
_NbsMgmtRcvPerfFwdBytes_Type = Counter32
_NbsMgmtRcvPerfFwdBytes_Object = MibTableColumn
nbsMgmtRcvPerfFwdBytes = _NbsMgmtRcvPerfFwdBytes_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 6, 4, 1, 4),
    _NbsMgmtRcvPerfFwdBytes_Type()
)
nbsMgmtRcvPerfFwdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMgmtRcvPerfFwdBytes.setStatus("mandatory")
_NbsMgmtXmtPerfTable_Object = MibTable
nbsMgmtXmtPerfTable = _NbsMgmtXmtPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 6, 5)
)
if mibBuilder.loadTexts:
    nbsMgmtXmtPerfTable.setStatus("mandatory")
_NbsMgmtXmtPerfEntry_Object = MibTableRow
nbsMgmtXmtPerfEntry = _NbsMgmtXmtPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 6, 5, 1)
)
nbsMgmtXmtPerfEntry.setIndexNames(
    (0, "NBASE-G1-MIB", "nbsMgmtXmtPerfOutPort"),
)
if mibBuilder.loadTexts:
    nbsMgmtXmtPerfEntry.setStatus("mandatory")
_NbsMgmtXmtPerfOutPort_Type = Integer32
_NbsMgmtXmtPerfOutPort_Object = MibTableColumn
nbsMgmtXmtPerfOutPort = _NbsMgmtXmtPerfOutPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 6, 5, 1, 2),
    _NbsMgmtXmtPerfOutPort_Type()
)
nbsMgmtXmtPerfOutPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMgmtXmtPerfOutPort.setStatus("mandatory")
_NbsMgmtXmtPerfFwdPkts_Type = Counter32
_NbsMgmtXmtPerfFwdPkts_Object = MibTableColumn
nbsMgmtXmtPerfFwdPkts = _NbsMgmtXmtPerfFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 6, 5, 1, 3),
    _NbsMgmtXmtPerfFwdPkts_Type()
)
nbsMgmtXmtPerfFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMgmtXmtPerfFwdPkts.setStatus("mandatory")
_NbsMgmtXmtPerfFwdBytes_Type = Counter32
_NbsMgmtXmtPerfFwdBytes_Object = MibTableColumn
nbsMgmtXmtPerfFwdBytes = _NbsMgmtXmtPerfFwdBytes_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 6, 5, 1, 4),
    _NbsMgmtXmtPerfFwdBytes_Type()
)
nbsMgmtXmtPerfFwdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMgmtXmtPerfFwdBytes.setStatus("mandatory")
_NbsTraps_ObjectIdentity = ObjectIdentity
nbsTraps = _NbsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 7)
)
_NbsMiniSwDb_ObjectIdentity = ObjectIdentity
nbsMiniSwDb = _NbsMiniSwDb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 8)
)
_NbsMegaSwDb_ObjectIdentity = ObjectIdentity
nbsMegaSwDb = _NbsMegaSwDb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 9)
)
_NbsMegaSwRunDb_ObjectIdentity = ObjectIdentity
nbsMegaSwRunDb = _NbsMegaSwRunDb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1)
)
_NbsMegaSwRunDbTable_Object = MibTable
nbsMegaSwRunDbTable = _NbsMegaSwRunDbTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    nbsMegaSwRunDbTable.setStatus("mandatory")
_NbsMegaSwRunDbEntry_Object = MibTableRow
nbsMegaSwRunDbEntry = _NbsMegaSwRunDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 1, 1)
)
nbsMegaSwRunDbEntry.setIndexNames(
    (0, "NBASE-G1-MIB", "nbsMegaSwRunDbIndex"),
)
if mibBuilder.loadTexts:
    nbsMegaSwRunDbEntry.setStatus("mandatory")
_NbsMegaSwRunDbIndex_Type = Integer32
_NbsMegaSwRunDbIndex_Object = MibTableColumn
nbsMegaSwRunDbIndex = _NbsMegaSwRunDbIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 1, 1, 1),
    _NbsMegaSwRunDbIndex_Type()
)
nbsMegaSwRunDbIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMegaSwRunDbIndex.setStatus("mandatory")


class _NbsMegaSwRunDbStatus_Type(Integer32):
    """Custom type nbsMegaSwRunDbStatus based on Integer32"""
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
        *(("deleteOnReset", 4),
          ("deleteOnTimeout", 5),
          ("invalid", 1),
          ("permanent", 3),
          ("system", 2))
    )


_NbsMegaSwRunDbStatus_Type.__name__ = "Integer32"
_NbsMegaSwRunDbStatus_Object = MibTableColumn
nbsMegaSwRunDbStatus = _NbsMegaSwRunDbStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 1, 1, 2),
    _NbsMegaSwRunDbStatus_Type()
)
nbsMegaSwRunDbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMegaSwRunDbStatus.setStatus("mandatory")
_NbsMegaSwRunDbAddr_Type = MacAddress
_NbsMegaSwRunDbAddr_Object = MibTableColumn
nbsMegaSwRunDbAddr = _NbsMegaSwRunDbAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 1, 1, 3),
    _NbsMegaSwRunDbAddr_Type()
)
nbsMegaSwRunDbAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMegaSwRunDbAddr.setStatus("mandatory")


class _NbsMegaSwRunDbType_Type(Integer32):
    """Custom type nbsMegaSwRunDbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("customFilter", 2),
          ("virtualFilter", 1))
    )


_NbsMegaSwRunDbType_Type.__name__ = "Integer32"
_NbsMegaSwRunDbType_Object = MibTableColumn
nbsMegaSwRunDbType = _NbsMegaSwRunDbType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 1, 1, 4),
    _NbsMegaSwRunDbType_Type()
)
nbsMegaSwRunDbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMegaSwRunDbType.setStatus("mandatory")
_NbsMegaSwRunDbDport_Type = Integer32
_NbsMegaSwRunDbDport_Object = MibTableColumn
nbsMegaSwRunDbDport = _NbsMegaSwRunDbDport_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 1, 1, 5),
    _NbsMegaSwRunDbDport_Type()
)
nbsMegaSwRunDbDport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMegaSwRunDbDport.setStatus("mandatory")
_NbsMegaSwRunFilterTable_Object = MibTable
nbsMegaSwRunFilterTable = _NbsMegaSwRunFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 2)
)
if mibBuilder.loadTexts:
    nbsMegaSwRunFilterTable.setStatus("mandatory")
_NbsMegaSwRunFilterEntry_Object = MibTableRow
nbsMegaSwRunFilterEntry = _NbsMegaSwRunFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 2, 1)
)
nbsMegaSwRunFilterEntry.setIndexNames(
    (0, "NBASE-G1-MIB", "nbsMegaSwRunFilterAddr"),
    (0, "NBASE-G1-MIB", "nbsMegaSwRunFilterSport"),
)
if mibBuilder.loadTexts:
    nbsMegaSwRunFilterEntry.setStatus("mandatory")


class _NbsMegaSwRunFilterStatus_Type(Integer32):
    """Custom type nbsMegaSwRunFilterStatus based on Integer32"""
    defaultValue = 4

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
        *(("deleteOnReset", 4),
          ("deleteOnTimeout", 5),
          ("invalid", 1),
          ("permanent", 3),
          ("system", 2))
    )


_NbsMegaSwRunFilterStatus_Type.__name__ = "Integer32"
_NbsMegaSwRunFilterStatus_Object = MibTableColumn
nbsMegaSwRunFilterStatus = _NbsMegaSwRunFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 2, 1, 1),
    _NbsMegaSwRunFilterStatus_Type()
)
nbsMegaSwRunFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsMegaSwRunFilterStatus.setStatus("mandatory")
_NbsMegaSwRunFilterAddr_Type = MacAddress
_NbsMegaSwRunFilterAddr_Object = MibTableColumn
nbsMegaSwRunFilterAddr = _NbsMegaSwRunFilterAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 2, 1, 2),
    _NbsMegaSwRunFilterAddr_Type()
)
nbsMegaSwRunFilterAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsMegaSwRunFilterAddr.setStatus("mandatory")


class _NbsMegaSwRunFilterType_Type(Integer32):
    """Custom type nbsMegaSwRunFilterType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("customFilter", 2),
          ("virtualFilter", 1))
    )


_NbsMegaSwRunFilterType_Type.__name__ = "Integer32"
_NbsMegaSwRunFilterType_Object = MibTableColumn
nbsMegaSwRunFilterType = _NbsMegaSwRunFilterType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 2, 1, 3),
    _NbsMegaSwRunFilterType_Type()
)
nbsMegaSwRunFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsMegaSwRunFilterType.setStatus("mandatory")


class _NbsMegaSwRunFilterDport_Type(Integer32):
    """Custom type nbsMegaSwRunFilterDport based on Integer32"""
    defaultValue = 0


_NbsMegaSwRunFilterDport_Object = MibTableColumn
nbsMegaSwRunFilterDport = _NbsMegaSwRunFilterDport_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 2, 1, 4),
    _NbsMegaSwRunFilterDport_Type()
)
nbsMegaSwRunFilterDport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsMegaSwRunFilterDport.setStatus("mandatory")
_NbsMegaSwRunFilterSport_Type = Integer32
_NbsMegaSwRunFilterSport_Object = MibTableColumn
nbsMegaSwRunFilterSport = _NbsMegaSwRunFilterSport_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 2, 1, 5),
    _NbsMegaSwRunFilterSport_Type()
)
nbsMegaSwRunFilterSport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsMegaSwRunFilterSport.setStatus("mandatory")


class _NbsMegaSwRunFilterDmap_Type(OctetString):
    """Custom type nbsMegaSwRunFilterDmap based on OctetString"""
    defaultHexValue = "ffff"


_NbsMegaSwRunFilterDmap_Object = MibTableColumn
nbsMegaSwRunFilterDmap = _NbsMegaSwRunFilterDmap_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 2, 1, 6),
    _NbsMegaSwRunFilterDmap_Type()
)
nbsMegaSwRunFilterDmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsMegaSwRunFilterDmap.setStatus("mandatory")
_NbsMegaSwSvlanConnectTable_Object = MibTable
nbsMegaSwSvlanConnectTable = _NbsMegaSwSvlanConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 3)
)
if mibBuilder.loadTexts:
    nbsMegaSwSvlanConnectTable.setStatus("mandatory")
_NbsMegaSwSvlanConnectEntry_Object = MibTableRow
nbsMegaSwSvlanConnectEntry = _NbsMegaSwSvlanConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 3, 1)
)
nbsMegaSwSvlanConnectEntry.setIndexNames(
    (0, "NBASE-G1-MIB", "nbsMegaSwSvlanConnectSport"),
)
if mibBuilder.loadTexts:
    nbsMegaSwSvlanConnectEntry.setStatus("mandatory")
_NbsMegaSwSvlanConnectSport_Type = Integer32
_NbsMegaSwSvlanConnectSport_Object = MibTableColumn
nbsMegaSwSvlanConnectSport = _NbsMegaSwSvlanConnectSport_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 3, 1, 1),
    _NbsMegaSwSvlanConnectSport_Type()
)
nbsMegaSwSvlanConnectSport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMegaSwSvlanConnectSport.setStatus("mandatory")
_NbsMegaSwSvlanConnectDport_Type = OctetString
_NbsMegaSwSvlanConnectDport_Object = MibTableColumn
nbsMegaSwSvlanConnectDport = _NbsMegaSwSvlanConnectDport_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 3, 1, 2),
    _NbsMegaSwSvlanConnectDport_Type()
)
nbsMegaSwSvlanConnectDport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMegaSwSvlanConnectDport.setStatus("mandatory")
_NbsMegaSwRunSvlanDb_ObjectIdentity = ObjectIdentity
nbsMegaSwRunSvlanDb = _NbsMegaSwRunSvlanDb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 4)
)
_NbsMegaSwRunSvlanMaxNum_Type = Integer32
_NbsMegaSwRunSvlanMaxNum_Object = MibScalar
nbsMegaSwRunSvlanMaxNum = _NbsMegaSwRunSvlanMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 4, 1),
    _NbsMegaSwRunSvlanMaxNum_Type()
)
nbsMegaSwRunSvlanMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMegaSwRunSvlanMaxNum.setStatus("mandatory")
_NbsMegaSwRunSvlanTable_Object = MibTable
nbsMegaSwRunSvlanTable = _NbsMegaSwRunSvlanTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 4, 2)
)
if mibBuilder.loadTexts:
    nbsMegaSwRunSvlanTable.setStatus("mandatory")
_NbsMegaSwRunSvlanEntry_Object = MibTableRow
nbsMegaSwRunSvlanEntry = _NbsMegaSwRunSvlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 4, 2, 1)
)
nbsMegaSwRunSvlanEntry.setIndexNames(
    (0, "NBASE-G1-MIB", "nbsMegaSwRunSvlanIndex"),
)
if mibBuilder.loadTexts:
    nbsMegaSwRunSvlanEntry.setStatus("mandatory")
_NbsMegaSwRunSvlanIndex_Type = Integer32
_NbsMegaSwRunSvlanIndex_Object = MibTableColumn
nbsMegaSwRunSvlanIndex = _NbsMegaSwRunSvlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 4, 2, 1, 1),
    _NbsMegaSwRunSvlanIndex_Type()
)
nbsMegaSwRunSvlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMegaSwRunSvlanIndex.setStatus("mandatory")


class _NbsMegaSwRunSvlanStatus_Type(Integer32):
    """Custom type nbsMegaSwRunSvlanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_NbsMegaSwRunSvlanStatus_Type.__name__ = "Integer32"
_NbsMegaSwRunSvlanStatus_Object = MibTableColumn
nbsMegaSwRunSvlanStatus = _NbsMegaSwRunSvlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 4, 2, 1, 2),
    _NbsMegaSwRunSvlanStatus_Type()
)
nbsMegaSwRunSvlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsMegaSwRunSvlanStatus.setStatus("mandatory")


class _NbsMegaSwRunSvlanList_Type(OctetString):
    """Custom type nbsMegaSwRunSvlanList based on OctetString"""
    defaultHexValue = "ffff"


_NbsMegaSwRunSvlanList_Object = MibTableColumn
nbsMegaSwRunSvlanList = _NbsMegaSwRunSvlanList_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 4, 2, 1, 3),
    _NbsMegaSwRunSvlanList_Type()
)
nbsMegaSwRunSvlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsMegaSwRunSvlanList.setStatus("mandatory")
_NbsMegaSwRunSvlanIsvlanFlag_Type = Integer32
_NbsMegaSwRunSvlanIsvlanFlag_Object = MibTableColumn
nbsMegaSwRunSvlanIsvlanFlag = _NbsMegaSwRunSvlanIsvlanFlag_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 4, 2, 1, 4),
    _NbsMegaSwRunSvlanIsvlanFlag_Type()
)
nbsMegaSwRunSvlanIsvlanFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMegaSwRunSvlanIsvlanFlag.setStatus("mandatory")
_NbsMegaSwRunIsvlanMaxNum_Type = Integer32
_NbsMegaSwRunIsvlanMaxNum_Object = MibScalar
nbsMegaSwRunIsvlanMaxNum = _NbsMegaSwRunIsvlanMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 4, 3),
    _NbsMegaSwRunIsvlanMaxNum_Type()
)
nbsMegaSwRunIsvlanMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMegaSwRunIsvlanMaxNum.setStatus("mandatory")
_NbsMegaSwRunIsvlanTable_Object = MibTable
nbsMegaSwRunIsvlanTable = _NbsMegaSwRunIsvlanTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 4, 4)
)
if mibBuilder.loadTexts:
    nbsMegaSwRunIsvlanTable.setStatus("mandatory")
_NbsMegaSwRunIsvlanEntry_Object = MibTableRow
nbsMegaSwRunIsvlanEntry = _NbsMegaSwRunIsvlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 4, 4, 1)
)
nbsMegaSwRunIsvlanEntry.setIndexNames(
    (0, "NBASE-G1-MIB", "nbsMegaSwRunIsvlanIndex"),
)
if mibBuilder.loadTexts:
    nbsMegaSwRunIsvlanEntry.setStatus("mandatory")
_NbsMegaSwRunIsvlanIndex_Type = Integer32
_NbsMegaSwRunIsvlanIndex_Object = MibTableColumn
nbsMegaSwRunIsvlanIndex = _NbsMegaSwRunIsvlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 4, 4, 1, 1),
    _NbsMegaSwRunIsvlanIndex_Type()
)
nbsMegaSwRunIsvlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMegaSwRunIsvlanIndex.setStatus("mandatory")


class _NbsMegaSwRunIsvlanStatus_Type(Integer32):
    """Custom type nbsMegaSwRunIsvlanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("mcast", 3),
          ("valid", 1))
    )


_NbsMegaSwRunIsvlanStatus_Type.__name__ = "Integer32"
_NbsMegaSwRunIsvlanStatus_Object = MibTableColumn
nbsMegaSwRunIsvlanStatus = _NbsMegaSwRunIsvlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 4, 4, 1, 2),
    _NbsMegaSwRunIsvlanStatus_Type()
)
nbsMegaSwRunIsvlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsMegaSwRunIsvlanStatus.setStatus("mandatory")


class _NbsMegaSwRunIsvlanList_Type(OctetString):
    """Custom type nbsMegaSwRunIsvlanList based on OctetString"""
    defaultHexValue = "ffff"


_NbsMegaSwRunIsvlanList_Object = MibTableColumn
nbsMegaSwRunIsvlanList = _NbsMegaSwRunIsvlanList_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 4, 4, 1, 3),
    _NbsMegaSwRunIsvlanList_Type()
)
nbsMegaSwRunIsvlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsMegaSwRunIsvlanList.setStatus("mandatory")


class _NbsMegaSwRunIsvlanName_Type(DisplayString):
    """Custom type nbsMegaSwRunIsvlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_NbsMegaSwRunIsvlanName_Type.__name__ = "DisplayString"
_NbsMegaSwRunIsvlanName_Object = MibTableColumn
nbsMegaSwRunIsvlanName = _NbsMegaSwRunIsvlanName_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 4, 4, 1, 4),
    _NbsMegaSwRunIsvlanName_Type()
)
nbsMegaSwRunIsvlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsMegaSwRunIsvlanName.setStatus("mandatory")


class _NbsMegaSwRunIsvlanTag_Type(Integer32):
    """Custom type nbsMegaSwRunIsvlanTag based on Integer32"""
    defaultValue = 1


_NbsMegaSwRunIsvlanTag_Object = MibTableColumn
nbsMegaSwRunIsvlanTag = _NbsMegaSwRunIsvlanTag_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 4, 4, 1, 5),
    _NbsMegaSwRunIsvlanTag_Type()
)
nbsMegaSwRunIsvlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsMegaSwRunIsvlanTag.setStatus("mandatory")
_NbsMegaSwRunIsvlanVlanIndex_Type = Integer32
_NbsMegaSwRunIsvlanVlanIndex_Object = MibTableColumn
nbsMegaSwRunIsvlanVlanIndex = _NbsMegaSwRunIsvlanVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 4, 4, 1, 6),
    _NbsMegaSwRunIsvlanVlanIndex_Type()
)
nbsMegaSwRunIsvlanVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMegaSwRunIsvlanVlanIndex.setStatus("mandatory")
_NbsMegaSwRunVbcDb_ObjectIdentity = ObjectIdentity
nbsMegaSwRunVbcDb = _NbsMegaSwRunVbcDb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 5)
)
_NbsMegaSwRunVbcMaxNum_Type = Integer32
_NbsMegaSwRunVbcMaxNum_Object = MibScalar
nbsMegaSwRunVbcMaxNum = _NbsMegaSwRunVbcMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 5, 1),
    _NbsMegaSwRunVbcMaxNum_Type()
)
nbsMegaSwRunVbcMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMegaSwRunVbcMaxNum.setStatus("mandatory")
_NbsMegaSwRunVbcTable_Object = MibTable
nbsMegaSwRunVbcTable = _NbsMegaSwRunVbcTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 5, 2)
)
if mibBuilder.loadTexts:
    nbsMegaSwRunVbcTable.setStatus("mandatory")
_NbsMegaSwRunVbcEntry_Object = MibTableRow
nbsMegaSwRunVbcEntry = _NbsMegaSwRunVbcEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 5, 2, 1)
)
nbsMegaSwRunVbcEntry.setIndexNames(
    (0, "NBASE-G1-MIB", "nbsMegaSwRunVbcIndex"),
)
if mibBuilder.loadTexts:
    nbsMegaSwRunVbcEntry.setStatus("mandatory")
_NbsMegaSwRunVbcIndex_Type = Integer32
_NbsMegaSwRunVbcIndex_Object = MibTableColumn
nbsMegaSwRunVbcIndex = _NbsMegaSwRunVbcIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 5, 2, 1, 1),
    _NbsMegaSwRunVbcIndex_Type()
)
nbsMegaSwRunVbcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMegaSwRunVbcIndex.setStatus("mandatory")


class _NbsMegaSwRunVbcStatus_Type(Integer32):
    """Custom type nbsMegaSwRunVbcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_NbsMegaSwRunVbcStatus_Type.__name__ = "Integer32"
_NbsMegaSwRunVbcStatus_Object = MibTableColumn
nbsMegaSwRunVbcStatus = _NbsMegaSwRunVbcStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 5, 2, 1, 2),
    _NbsMegaSwRunVbcStatus_Type()
)
nbsMegaSwRunVbcStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsMegaSwRunVbcStatus.setStatus("mandatory")


class _NbsMegaSwRunVbcList_Type(OctetString):
    """Custom type nbsMegaSwRunVbcList based on OctetString"""
    defaultHexValue = "ffff"


_NbsMegaSwRunVbcList_Object = MibTableColumn
nbsMegaSwRunVbcList = _NbsMegaSwRunVbcList_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 5, 2, 1, 3),
    _NbsMegaSwRunVbcList_Type()
)
nbsMegaSwRunVbcList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsMegaSwRunVbcList.setStatus("mandatory")
_NbsMegaSwVmon_ObjectIdentity = ObjectIdentity
nbsMegaSwVmon = _NbsMegaSwVmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 6)
)
_NbsMegaSwVmonMonitorPort_Type = Integer32
_NbsMegaSwVmonMonitorPort_Object = MibScalar
nbsMegaSwVmonMonitorPort = _NbsMegaSwVmonMonitorPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 6, 1),
    _NbsMegaSwVmonMonitorPort_Type()
)
nbsMegaSwVmonMonitorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsMegaSwVmonMonitorPort.setStatus("mandatory")
_NbsMegaSwVmonMonitrdPort_Type = Integer32
_NbsMegaSwVmonMonitrdPort_Object = MibScalar
nbsMegaSwVmonMonitrdPort = _NbsMegaSwVmonMonitrdPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 6, 2),
    _NbsMegaSwVmonMonitrdPort_Type()
)
nbsMegaSwVmonMonitrdPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsMegaSwVmonMonitrdPort.setStatus("mandatory")


class _NbsMegaSwVmonStatus_Type(Integer32):
    """Custom type nbsMegaSwVmonStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonInit", 1),
          ("startMon", 2),
          ("stopMon", 3))
    )


_NbsMegaSwVmonStatus_Type.__name__ = "Integer32"
_NbsMegaSwVmonStatus_Object = MibScalar
nbsMegaSwVmonStatus = _NbsMegaSwVmonStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 1, 6, 3),
    _NbsMegaSwVmonStatus_Type()
)
nbsMegaSwVmonStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsMegaSwVmonStatus.setStatus("mandatory")
_NbsMegaSwPermDb_ObjectIdentity = ObjectIdentity
nbsMegaSwPermDb = _NbsMegaSwPermDb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 2)
)
_NbsMegaSwPermSvlanDb_ObjectIdentity = ObjectIdentity
nbsMegaSwPermSvlanDb = _NbsMegaSwPermSvlanDb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 2, 1)
)
_NbsMegaSwPermSvlanMaxNum_Type = Integer32
_NbsMegaSwPermSvlanMaxNum_Object = MibScalar
nbsMegaSwPermSvlanMaxNum = _NbsMegaSwPermSvlanMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 2, 1, 1),
    _NbsMegaSwPermSvlanMaxNum_Type()
)
nbsMegaSwPermSvlanMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMegaSwPermSvlanMaxNum.setStatus("mandatory")
_NbsMegaSwPermSvlanTable_Object = MibTable
nbsMegaSwPermSvlanTable = _NbsMegaSwPermSvlanTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 2, 1, 2)
)
if mibBuilder.loadTexts:
    nbsMegaSwPermSvlanTable.setStatus("mandatory")
_NbsMegaSwPermSvlanEntry_Object = MibTableRow
nbsMegaSwPermSvlanEntry = _NbsMegaSwPermSvlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 2, 1, 2, 1)
)
nbsMegaSwPermSvlanEntry.setIndexNames(
    (0, "NBASE-G1-MIB", "nbsMegaSwPermSvlanIndex"),
)
if mibBuilder.loadTexts:
    nbsMegaSwPermSvlanEntry.setStatus("mandatory")
_NbsMegaSwPermSvlanIndex_Type = Integer32
_NbsMegaSwPermSvlanIndex_Object = MibTableColumn
nbsMegaSwPermSvlanIndex = _NbsMegaSwPermSvlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 2, 1, 2, 1, 1),
    _NbsMegaSwPermSvlanIndex_Type()
)
nbsMegaSwPermSvlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMegaSwPermSvlanIndex.setStatus("mandatory")


class _NbsMegaSwPermSvlanStatus_Type(Integer32):
    """Custom type nbsMegaSwPermSvlanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_NbsMegaSwPermSvlanStatus_Type.__name__ = "Integer32"
_NbsMegaSwPermSvlanStatus_Object = MibTableColumn
nbsMegaSwPermSvlanStatus = _NbsMegaSwPermSvlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 2, 1, 2, 1, 2),
    _NbsMegaSwPermSvlanStatus_Type()
)
nbsMegaSwPermSvlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsMegaSwPermSvlanStatus.setStatus("mandatory")


class _NbsMegaSwPermSvlanList_Type(OctetString):
    """Custom type nbsMegaSwPermSvlanList based on OctetString"""
    defaultHexValue = "ffff"


_NbsMegaSwPermSvlanList_Object = MibTableColumn
nbsMegaSwPermSvlanList = _NbsMegaSwPermSvlanList_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 2, 1, 2, 1, 3),
    _NbsMegaSwPermSvlanList_Type()
)
nbsMegaSwPermSvlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsMegaSwPermSvlanList.setStatus("mandatory")
_NbsMegaSwPermIsvlanMaxNum_Type = Integer32
_NbsMegaSwPermIsvlanMaxNum_Object = MibScalar
nbsMegaSwPermIsvlanMaxNum = _NbsMegaSwPermIsvlanMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 2, 1, 3),
    _NbsMegaSwPermIsvlanMaxNum_Type()
)
nbsMegaSwPermIsvlanMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMegaSwPermIsvlanMaxNum.setStatus("mandatory")
_NbsMegaSwPermIsvlanTable_Object = MibTable
nbsMegaSwPermIsvlanTable = _NbsMegaSwPermIsvlanTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 2, 1, 4)
)
if mibBuilder.loadTexts:
    nbsMegaSwPermIsvlanTable.setStatus("mandatory")
_NbsMegaSwPermIsvlanEntry_Object = MibTableRow
nbsMegaSwPermIsvlanEntry = _NbsMegaSwPermIsvlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 2, 1, 4, 1)
)
nbsMegaSwPermIsvlanEntry.setIndexNames(
    (0, "NBASE-G1-MIB", "nbsMegaSwPermIsvlanIndex"),
)
if mibBuilder.loadTexts:
    nbsMegaSwPermIsvlanEntry.setStatus("mandatory")
_NbsMegaSwPermIsvlanIndex_Type = Integer32
_NbsMegaSwPermIsvlanIndex_Object = MibTableColumn
nbsMegaSwPermIsvlanIndex = _NbsMegaSwPermIsvlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 2, 1, 4, 1, 1),
    _NbsMegaSwPermIsvlanIndex_Type()
)
nbsMegaSwPermIsvlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMegaSwPermIsvlanIndex.setStatus("mandatory")


class _NbsMegaSwPermIsvlanStatus_Type(Integer32):
    """Custom type nbsMegaSwPermIsvlanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("mcast", 3),
          ("valid", 1))
    )


_NbsMegaSwPermIsvlanStatus_Type.__name__ = "Integer32"
_NbsMegaSwPermIsvlanStatus_Object = MibTableColumn
nbsMegaSwPermIsvlanStatus = _NbsMegaSwPermIsvlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 2, 1, 4, 1, 2),
    _NbsMegaSwPermIsvlanStatus_Type()
)
nbsMegaSwPermIsvlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsMegaSwPermIsvlanStatus.setStatus("mandatory")


class _NbsMegaSwPermIsvlanList_Type(OctetString):
    """Custom type nbsMegaSwPermIsvlanList based on OctetString"""
    defaultHexValue = "ffff"


_NbsMegaSwPermIsvlanList_Object = MibTableColumn
nbsMegaSwPermIsvlanList = _NbsMegaSwPermIsvlanList_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 2, 1, 4, 1, 3),
    _NbsMegaSwPermIsvlanList_Type()
)
nbsMegaSwPermIsvlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsMegaSwPermIsvlanList.setStatus("mandatory")


class _NbsMegaSwPermIsvlanName_Type(DisplayString):
    """Custom type nbsMegaSwPermIsvlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_NbsMegaSwPermIsvlanName_Type.__name__ = "DisplayString"
_NbsMegaSwPermIsvlanName_Object = MibTableColumn
nbsMegaSwPermIsvlanName = _NbsMegaSwPermIsvlanName_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 2, 1, 4, 1, 4),
    _NbsMegaSwPermIsvlanName_Type()
)
nbsMegaSwPermIsvlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsMegaSwPermIsvlanName.setStatus("mandatory")
_NbsMegaSwPermIsvlanTag_Type = Integer32
_NbsMegaSwPermIsvlanTag_Object = MibTableColumn
nbsMegaSwPermIsvlanTag = _NbsMegaSwPermIsvlanTag_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 2, 1, 4, 1, 5),
    _NbsMegaSwPermIsvlanTag_Type()
)
nbsMegaSwPermIsvlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsMegaSwPermIsvlanTag.setStatus("mandatory")
_NbsMegaSwPermVbcDb_ObjectIdentity = ObjectIdentity
nbsMegaSwPermVbcDb = _NbsMegaSwPermVbcDb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 2, 2)
)
_NbsMegaSwPermVbcMaxNum_Type = Integer32
_NbsMegaSwPermVbcMaxNum_Object = MibScalar
nbsMegaSwPermVbcMaxNum = _NbsMegaSwPermVbcMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 2, 2, 1),
    _NbsMegaSwPermVbcMaxNum_Type()
)
nbsMegaSwPermVbcMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMegaSwPermVbcMaxNum.setStatus("mandatory")
_NbsMegaSwPermVbcTable_Object = MibTable
nbsMegaSwPermVbcTable = _NbsMegaSwPermVbcTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 2, 2, 2)
)
if mibBuilder.loadTexts:
    nbsMegaSwPermVbcTable.setStatus("mandatory")
_NbsMegaSwPermVbcEntry_Object = MibTableRow
nbsMegaSwPermVbcEntry = _NbsMegaSwPermVbcEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 2, 2, 2, 1)
)
nbsMegaSwPermVbcEntry.setIndexNames(
    (0, "NBASE-G1-MIB", "nbsMegaSwPermVbcIndex"),
)
if mibBuilder.loadTexts:
    nbsMegaSwPermVbcEntry.setStatus("mandatory")
_NbsMegaSwPermVbcIndex_Type = Integer32
_NbsMegaSwPermVbcIndex_Object = MibTableColumn
nbsMegaSwPermVbcIndex = _NbsMegaSwPermVbcIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 2, 2, 2, 1, 1),
    _NbsMegaSwPermVbcIndex_Type()
)
nbsMegaSwPermVbcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMegaSwPermVbcIndex.setStatus("mandatory")


class _NbsMegaSwPermVbcStatus_Type(Integer32):
    """Custom type nbsMegaSwPermVbcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_NbsMegaSwPermVbcStatus_Type.__name__ = "Integer32"
_NbsMegaSwPermVbcStatus_Object = MibTableColumn
nbsMegaSwPermVbcStatus = _NbsMegaSwPermVbcStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 2, 2, 2, 1, 2),
    _NbsMegaSwPermVbcStatus_Type()
)
nbsMegaSwPermVbcStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsMegaSwPermVbcStatus.setStatus("mandatory")


class _NbsMegaSwPermVbcList_Type(OctetString):
    """Custom type nbsMegaSwPermVbcList based on OctetString"""
    defaultHexValue = "ffff"


_NbsMegaSwPermVbcList_Object = MibTableColumn
nbsMegaSwPermVbcList = _NbsMegaSwPermVbcList_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 2, 2, 2, 1, 3),
    _NbsMegaSwPermVbcList_Type()
)
nbsMegaSwPermVbcList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsMegaSwPermVbcList.setStatus("mandatory")
_NbsTpPermAgingTime_Type = Integer32
_NbsTpPermAgingTime_Object = MibScalar
nbsTpPermAgingTime = _NbsTpPermAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 9, 2, 3),
    _NbsTpPermAgingTime_Type()
)
nbsTpPermAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsTpPermAgingTime.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBASE-G1-MIB",
    **{"MacAddress": MacAddress,
       "nbase": nbase,
       "nbSwitchG1": nbSwitchG1,
       "nbsProducts": nbsProducts,
       "miniSwitch": miniSwitch,
       "megaSwitch208": megaSwitch208,
       "megaSwitch215": megaSwitch215,
       "megaFastSwitch": megaFastSwitch,
       "megaSwitchII": megaSwitchII,
       "megaSwitch2015": megaSwitch2015,
       "megaSwitch2048": megaSwitch2048,
       "nbsSys": nbsSys,
       "nbsSysFwVers": nbsSysFwVers,
       "nbsSysPortsNumber": nbsSysPortsNumber,
       "nbsSysRestart": nbsSysRestart,
       "nbsSysNumRestarts": nbsSysNumRestarts,
       "nbsSysLastError": nbsSysLastError,
       "nbsSysErrUptime": nbsSysErrUptime,
       "nbsSysSwitchDBSize": nbsSysSwitchDBSize,
       "nbsSysSetNvramDefaults": nbsSysSetNvramDefaults,
       "nbsSysResetSwitchStats": nbsSysResetSwitchStats,
       "nbsSysStpEnable": nbsSysStpEnable,
       "nbsSysRunStpState": nbsSysRunStpState,
       "nbsSysFrmGen": nbsSysFrmGen,
       "nbsSysFrmGenSession": nbsSysFrmGenSession,
       "nbsSysFrmGenDa": nbsSysFrmGenDa,
       "nbsSysFrmGenSa": nbsSysFrmGenSa,
       "nbsSysFrmGenPktFill": nbsSysFrmGenPktFill,
       "nbsSysFrmGenPktRate": nbsSysFrmGenPktRate,
       "nbsSysFrmGenDestMap": nbsSysFrmGenDestMap,
       "nbsSysFrmGenPktNum": nbsSysFrmGenPktNum,
       "nbsSysFrmGenPktLen": nbsSysFrmGenPktLen,
       "nbsSysFrmGenXmtPktNum": nbsSysFrmGenXmtPktNum,
       "nbsSysSelftestLevel": nbsSysSelftestLevel,
       "nbsSysSnmpCfg": nbsSysSnmpCfg,
       "nbsSysIpAddr": nbsSysIpAddr,
       "nbsSysNetMask": nbsSysNetMask,
       "nbsSysBcastAddr": nbsSysBcastAddr,
       "nbsSysObIpAddr": nbsSysObIpAddr,
       "nbsSysObNetMask": nbsSysObNetMask,
       "nbsSysObBcastAddr": nbsSysObBcastAddr,
       "nbsSysDefaultGateway": nbsSysDefaultGateway,
       "nbsSysReadComunity": nbsSysReadComunity,
       "nbsSysWriteComunity": nbsSysWriteComunity,
       "nbsSysBootpEnable": nbsSysBootpEnable,
       "nbsSysTrapTblMaxSize": nbsSysTrapTblMaxSize,
       "nbsSysTrapTable": nbsSysTrapTable,
       "nbsSysTrapEntry": nbsSysTrapEntry,
       "nbsSysTrapTblEntIndex": nbsSysTrapTblEntIndex,
       "nbsSysTrapTblEntStatus": nbsSysTrapTblEntStatus,
       "nbsSysTrapTblEntIpAddr": nbsSysTrapTblEntIpAddr,
       "nbsSysTrapTblEntComm": nbsSysTrapTblEntComm,
       "nbsSysTftpSwFileName": nbsSysTftpSwFileName,
       "nbsSysTftpParFileName": nbsSysTftpParFileName,
       "nbsSysSerialLineMode": nbsSysSerialLineMode,
       "nbsSysSerialSlipBaudRate": nbsSysSerialSlipBaudRate,
       "nbsSysTelnetSession": nbsSysTelnetSession,
       "nbsSysPing": nbsSysPing,
       "nbsSysPingSession": nbsSysPingSession,
       "nbsSysPingAddr": nbsSysPingAddr,
       "nbsSysPingNumber": nbsSysPingNumber,
       "nbsSysPingRequests": nbsSysPingRequests,
       "nbsSysPingResps": nbsSysPingResps,
       "nbsSysPingOwner": nbsSysPingOwner,
       "nbsSysTelnetHost": nbsSysTelnetHost,
       "nbsSysTftpRswFileName": nbsSysTftpRswFileName,
       "nbsSysTftpServerIP": nbsSysTftpServerIP,
       "nbsSysInitDownload": nbsSysInitDownload,
       "nbsSysParDownload": nbsSysParDownload,
       "nbsSysParUpload": nbsSysParUpload,
       "nbsPortCfg": nbsPortCfg,
       "nbsPortCfgTable": nbsPortCfgTable,
       "nbsPortCfgEntry": nbsPortCfgEntry,
       "nbsPortCfgIndex": nbsPortCfgIndex,
       "nbsPortCfgLanType": nbsPortCfgLanType,
       "nbsPortCfgIfType": nbsPortCfgIfType,
       "nbsPortCfgPortSelect": nbsPortCfgPortSelect,
       "nbsPortCfgIfLink": nbsPortCfgIfLink,
       "nbsPortCfgPortFctrl": nbsPortCfgPortFctrl,
       "nbsPortCfgPortDplex": nbsPortCfgPortDplex,
       "nbsPortCfgPortDelay": nbsPortCfgPortDelay,
       "nbsPortCfgSpeedSelect": nbsPortCfgSpeedSelect,
       "nbsPortCfgEnable": nbsPortCfgEnable,
       "nbsPortCfgIsvpMode": nbsPortCfgIsvpMode,
       "nbsPortGrpCfgNum": nbsPortGrpCfgNum,
       "nbsPortGrpCfgTable": nbsPortGrpCfgTable,
       "nbsPortGrpCfgEntry": nbsPortGrpCfgEntry,
       "nbsPortGrpCfgIndex": nbsPortGrpCfgIndex,
       "nbsPortGrpCfgGrpNumber": nbsPortGrpCfgGrpNumber,
       "nbsPortGrpCfgPortNumber": nbsPortGrpCfgPortNumber,
       "nbsPortGrpCfgLinkStatus": nbsPortGrpCfgLinkStatus,
       "nbsPortGrpCfgActivity": nbsPortGrpCfgActivity,
       "nbsEtherInfo": nbsEtherInfo,
       "nbsEthInfoTable": nbsEthInfoTable,
       "nbsEthInfoEntry": nbsEthInfoEntry,
       "nbsEthInfoIndex": nbsEthInfoIndex,
       "nbsEthInfoCntFctrls": nbsEthInfoCntFctrls,
       "nbsEthInfoCntExcessFctrls": nbsEthInfoCntExcessFctrls,
       "nbsSwitchPerf": nbsSwitchPerf,
       "nbsSwitchPerfTable": nbsSwitchPerfTable,
       "nbsSwitchPerfEntry": nbsSwitchPerfEntry,
       "nbsSwitchPerfIndex": nbsSwitchPerfIndex,
       "nbsSwitchPerfMcastPkts": nbsSwitchPerfMcastPkts,
       "nbsSwitchPerfUnknPkts": nbsSwitchPerfUnknPkts,
       "nbsPortFwdPerfTable": nbsPortFwdPerfTable,
       "nbsPortFwdPerfEntry": nbsPortFwdPerfEntry,
       "nbsPortFwdPerfInPort": nbsPortFwdPerfInPort,
       "nbsPortFwdPerfOutPort": nbsPortFwdPerfOutPort,
       "nbsPortFwdPerfFwdPkts": nbsPortFwdPerfFwdPkts,
       "nbsPortFwdPerfFwdBytes": nbsPortFwdPerfFwdBytes,
       "nbsMgmtPerfStats": nbsMgmtPerfStats,
       "nbsMgmtPerfRcvdPkts": nbsMgmtPerfRcvdPkts,
       "nbsMgmtPerfRcvdBytes": nbsMgmtPerfRcvdBytes,
       "nbsMgmtPerfFilterdPkts": nbsMgmtPerfFilterdPkts,
       "nbsMgmtPerfRcvBcastPkts": nbsMgmtPerfRcvBcastPkts,
       "nbsMgmtPerfXmtPkts": nbsMgmtPerfXmtPkts,
       "nbsMgmtPerfXmtUcastPkts": nbsMgmtPerfXmtUcastPkts,
       "nbsMgmtPerfXmtMcastPkts": nbsMgmtPerfXmtMcastPkts,
       "nbsMgmtPerfXmtBcastPkts": nbsMgmtPerfXmtBcastPkts,
       "nbsMgmtRcvPerfTable": nbsMgmtRcvPerfTable,
       "nbsMgmtRcvPerfEntry": nbsMgmtRcvPerfEntry,
       "nbsMgmtRcvPerfInPort": nbsMgmtRcvPerfInPort,
       "nbsMgmtRcvPerfFwdPkts": nbsMgmtRcvPerfFwdPkts,
       "nbsMgmtRcvPerfFwdBytes": nbsMgmtRcvPerfFwdBytes,
       "nbsMgmtXmtPerfTable": nbsMgmtXmtPerfTable,
       "nbsMgmtXmtPerfEntry": nbsMgmtXmtPerfEntry,
       "nbsMgmtXmtPerfOutPort": nbsMgmtXmtPerfOutPort,
       "nbsMgmtXmtPerfFwdPkts": nbsMgmtXmtPerfFwdPkts,
       "nbsMgmtXmtPerfFwdBytes": nbsMgmtXmtPerfFwdBytes,
       "nbsTraps": nbsTraps,
       "nbsMiniSwDb": nbsMiniSwDb,
       "nbsMegaSwDb": nbsMegaSwDb,
       "nbsMegaSwRunDb": nbsMegaSwRunDb,
       "nbsMegaSwRunDbTable": nbsMegaSwRunDbTable,
       "nbsMegaSwRunDbEntry": nbsMegaSwRunDbEntry,
       "nbsMegaSwRunDbIndex": nbsMegaSwRunDbIndex,
       "nbsMegaSwRunDbStatus": nbsMegaSwRunDbStatus,
       "nbsMegaSwRunDbAddr": nbsMegaSwRunDbAddr,
       "nbsMegaSwRunDbType": nbsMegaSwRunDbType,
       "nbsMegaSwRunDbDport": nbsMegaSwRunDbDport,
       "nbsMegaSwRunFilterTable": nbsMegaSwRunFilterTable,
       "nbsMegaSwRunFilterEntry": nbsMegaSwRunFilterEntry,
       "nbsMegaSwRunFilterStatus": nbsMegaSwRunFilterStatus,
       "nbsMegaSwRunFilterAddr": nbsMegaSwRunFilterAddr,
       "nbsMegaSwRunFilterType": nbsMegaSwRunFilterType,
       "nbsMegaSwRunFilterDport": nbsMegaSwRunFilterDport,
       "nbsMegaSwRunFilterSport": nbsMegaSwRunFilterSport,
       "nbsMegaSwRunFilterDmap": nbsMegaSwRunFilterDmap,
       "nbsMegaSwSvlanConnectTable": nbsMegaSwSvlanConnectTable,
       "nbsMegaSwSvlanConnectEntry": nbsMegaSwSvlanConnectEntry,
       "nbsMegaSwSvlanConnectSport": nbsMegaSwSvlanConnectSport,
       "nbsMegaSwSvlanConnectDport": nbsMegaSwSvlanConnectDport,
       "nbsMegaSwRunSvlanDb": nbsMegaSwRunSvlanDb,
       "nbsMegaSwRunSvlanMaxNum": nbsMegaSwRunSvlanMaxNum,
       "nbsMegaSwRunSvlanTable": nbsMegaSwRunSvlanTable,
       "nbsMegaSwRunSvlanEntry": nbsMegaSwRunSvlanEntry,
       "nbsMegaSwRunSvlanIndex": nbsMegaSwRunSvlanIndex,
       "nbsMegaSwRunSvlanStatus": nbsMegaSwRunSvlanStatus,
       "nbsMegaSwRunSvlanList": nbsMegaSwRunSvlanList,
       "nbsMegaSwRunSvlanIsvlanFlag": nbsMegaSwRunSvlanIsvlanFlag,
       "nbsMegaSwRunIsvlanMaxNum": nbsMegaSwRunIsvlanMaxNum,
       "nbsMegaSwRunIsvlanTable": nbsMegaSwRunIsvlanTable,
       "nbsMegaSwRunIsvlanEntry": nbsMegaSwRunIsvlanEntry,
       "nbsMegaSwRunIsvlanIndex": nbsMegaSwRunIsvlanIndex,
       "nbsMegaSwRunIsvlanStatus": nbsMegaSwRunIsvlanStatus,
       "nbsMegaSwRunIsvlanList": nbsMegaSwRunIsvlanList,
       "nbsMegaSwRunIsvlanName": nbsMegaSwRunIsvlanName,
       "nbsMegaSwRunIsvlanTag": nbsMegaSwRunIsvlanTag,
       "nbsMegaSwRunIsvlanVlanIndex": nbsMegaSwRunIsvlanVlanIndex,
       "nbsMegaSwRunVbcDb": nbsMegaSwRunVbcDb,
       "nbsMegaSwRunVbcMaxNum": nbsMegaSwRunVbcMaxNum,
       "nbsMegaSwRunVbcTable": nbsMegaSwRunVbcTable,
       "nbsMegaSwRunVbcEntry": nbsMegaSwRunVbcEntry,
       "nbsMegaSwRunVbcIndex": nbsMegaSwRunVbcIndex,
       "nbsMegaSwRunVbcStatus": nbsMegaSwRunVbcStatus,
       "nbsMegaSwRunVbcList": nbsMegaSwRunVbcList,
       "nbsMegaSwVmon": nbsMegaSwVmon,
       "nbsMegaSwVmonMonitorPort": nbsMegaSwVmonMonitorPort,
       "nbsMegaSwVmonMonitrdPort": nbsMegaSwVmonMonitrdPort,
       "nbsMegaSwVmonStatus": nbsMegaSwVmonStatus,
       "nbsMegaSwPermDb": nbsMegaSwPermDb,
       "nbsMegaSwPermSvlanDb": nbsMegaSwPermSvlanDb,
       "nbsMegaSwPermSvlanMaxNum": nbsMegaSwPermSvlanMaxNum,
       "nbsMegaSwPermSvlanTable": nbsMegaSwPermSvlanTable,
       "nbsMegaSwPermSvlanEntry": nbsMegaSwPermSvlanEntry,
       "nbsMegaSwPermSvlanIndex": nbsMegaSwPermSvlanIndex,
       "nbsMegaSwPermSvlanStatus": nbsMegaSwPermSvlanStatus,
       "nbsMegaSwPermSvlanList": nbsMegaSwPermSvlanList,
       "nbsMegaSwPermIsvlanMaxNum": nbsMegaSwPermIsvlanMaxNum,
       "nbsMegaSwPermIsvlanTable": nbsMegaSwPermIsvlanTable,
       "nbsMegaSwPermIsvlanEntry": nbsMegaSwPermIsvlanEntry,
       "nbsMegaSwPermIsvlanIndex": nbsMegaSwPermIsvlanIndex,
       "nbsMegaSwPermIsvlanStatus": nbsMegaSwPermIsvlanStatus,
       "nbsMegaSwPermIsvlanList": nbsMegaSwPermIsvlanList,
       "nbsMegaSwPermIsvlanName": nbsMegaSwPermIsvlanName,
       "nbsMegaSwPermIsvlanTag": nbsMegaSwPermIsvlanTag,
       "nbsMegaSwPermVbcDb": nbsMegaSwPermVbcDb,
       "nbsMegaSwPermVbcMaxNum": nbsMegaSwPermVbcMaxNum,
       "nbsMegaSwPermVbcTable": nbsMegaSwPermVbcTable,
       "nbsMegaSwPermVbcEntry": nbsMegaSwPermVbcEntry,
       "nbsMegaSwPermVbcIndex": nbsMegaSwPermVbcIndex,
       "nbsMegaSwPermVbcStatus": nbsMegaSwPermVbcStatus,
       "nbsMegaSwPermVbcList": nbsMegaSwPermVbcList,
       "nbsTpPermAgingTime": nbsTpPermAgingTime}
)
