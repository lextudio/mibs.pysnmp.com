# SNMP MIB module (BCS-IDENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BCS-IDENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:38 2024
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

gi = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1166)
)


# Types definitions



class EntryStatus(Integer32):
    """Custom type EntryStatus based on Integer32"""
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Giproducts_ObjectIdentity = ObjectIdentity
giproducts = _Giproducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1)
)
_Acc4000d_ObjectIdentity = ObjectIdentity
acc4000d = _Acc4000d_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 1)
)
_Anicd_ObjectIdentity = ObjectIdentity
anicd = _Anicd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 2)
)
_Item1000_ObjectIdentity = ObjectIdentity
item1000 = _Item1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 4)
)
_Irt1000_ObjectIdentity = ObjectIdentity
irt1000 = _Irt1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 5)
)
_Nc1500_ObjectIdentity = ObjectIdentity
nc1500 = _Nc1500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 6)
)
_Om1000_ObjectIdentity = ObjectIdentity
om1000 = _Om1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 7)
)
_Im1000_ObjectIdentity = ObjectIdentity
im1000 = _Im1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 8)
)
_Mps_ObjectIdentity = ObjectIdentity
mps = _Mps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 9)
)
_Rpd1000_ObjectIdentity = ObjectIdentity
rpd1000 = _Rpd1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 10)
)
_AcpStatus_ObjectIdentity = ObjectIdentity
acpStatus = _AcpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 11)
)
_Heartbeat_ObjectIdentity = ObjectIdentity
heartbeat = _Heartbeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 12)
)
_EntitlementKey_ObjectIdentity = ObjectIdentity
entitlementKey = _EntitlementKey_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 13)
)
_Arpd_ObjectIdentity = ObjectIdentity
arpd = _Arpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 14)
)
_Svom_ObjectIdentity = ObjectIdentity
svom = _Svom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 15)
)
_Svm_ObjectIdentity = ObjectIdentity
svm = _Svm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 16)
)
_Erm_ObjectIdentity = ObjectIdentity
erm = _Erm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 17)
)
_SurfBbnh_ObjectIdentity = ObjectIdentity
surfBbnh = _SurfBbnh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 18)
)
_Sb2100_ObjectIdentity = ObjectIdentity
sb2100 = _Sb2100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19)
)
_Sb2100D_ObjectIdentity = ObjectIdentity
sb2100D = _Sb2100D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 20)
)
_Sb2000_ObjectIdentity = ObjectIdentity
sb2000 = _Sb2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 21)
)
_SaDANIS_ObjectIdentity = ObjectIdentity
saDANIS = _SaDANIS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 30)
)
_Apex_ObjectIdentity = ObjectIdentity
apex = _Apex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 31)
)
_Rem_ObjectIdentity = ObjectIdentity
rem = _Rem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 32)
)
_Mpe_ObjectIdentity = ObjectIdentity
mpe = _Mpe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 33)
)
_Spe_ObjectIdentity = ObjectIdentity
spe = _Spe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 34)
)
_Ne2000_ObjectIdentity = ObjectIdentity
ne2000 = _Ne2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 35)
)
_Apex1500_ObjectIdentity = ObjectIdentity
apex1500 = _Apex1500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 36)
)
_Agb_ObjectIdentity = ObjectIdentity
agb = _Agb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 37)
)
_Ne2500_ObjectIdentity = ObjectIdentity
ne2500 = _Ne2500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 38)
)
_Hdd2000_ObjectIdentity = ObjectIdentity
hdd2000 = _Hdd2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 40)
)
_Merlin_ObjectIdentity = ObjectIdentity
merlin = _Merlin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 50)
)
_Rsr_ObjectIdentity = ObjectIdentity
rsr = _Rsr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 60)
)
_Gsrm_ObjectIdentity = ObjectIdentity
gsrm = _Gsrm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 61)
)
_Gom_ObjectIdentity = ObjectIdentity
gom = _Gom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 62)
)
_B3_ObjectIdentity = ObjectIdentity
b3 = _B3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 63)
)
_Adm_ObjectIdentity = ObjectIdentity
adm = _Adm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 64)
)
_Sem_ObjectIdentity = ObjectIdentity
sem = _Sem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 70)
)
_Ecmg_ObjectIdentity = ObjectIdentity
ecmg = _Ecmg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 71)
)
_BsiAdapter_ObjectIdentity = ObjectIdentity
bsiAdapter = _BsiAdapter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 72)
)
_Oles_ObjectIdentity = ObjectIdentity
oles = _Oles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 73)
)
_Ne_ObjectIdentity = ObjectIdentity
ne = _Ne_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 74)
)
_TmxCommTrap_ObjectIdentity = ObjectIdentity
tmxCommTrap = _TmxCommTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 75)
)
_Drmenginekskdc_ObjectIdentity = ObjectIdentity
drmenginekskdc = _Drmenginekskdc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 76)
)
_Drmenginerte_ObjectIdentity = ObjectIdentity
drmenginerte = _Drmenginerte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 77)
)
_Drmengineecmg_ObjectIdentity = ObjectIdentity
drmengineecmg = _Drmengineecmg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 78)
)
_Drmengineskgpkg_ObjectIdentity = ObjectIdentity
drmengineskgpkg = _Drmengineskgpkg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 79)
)
_Tmx_ObjectIdentity = ObjectIdentity
tmx = _Tmx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 80)
)
_Prs_ObjectIdentity = ObjectIdentity
prs = _Prs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 81)
)
_Se2000_ObjectIdentity = ObjectIdentity
se2000 = _Se2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 82)
)
_Dem_ObjectIdentity = ObjectIdentity
dem = _Dem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 83)
)
_Ncs_ObjectIdentity = ObjectIdentity
ncs = _Ncs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 84)
)
_Ucs_ObjectIdentity = ObjectIdentity
ucs = _Ucs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 85)
)
_Lmm_ObjectIdentity = ObjectIdentity
lmm = _Lmm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 86)
)
_Se4000_ObjectIdentity = ObjectIdentity
se4000 = _Se4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 87)
)
_Rc_ObjectIdentity = ObjectIdentity
rc = _Rc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 88)
)
_NetSentry_ObjectIdentity = ObjectIdentity
netSentry = _NetSentry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 99)
)
_Sdm_ObjectIdentity = ObjectIdentity
sdm = _Sdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 100)
)
_HfcEms_ObjectIdentity = ObjectIdentity
hfcEms = _HfcEms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 101)
)
_Bnc_ObjectIdentity = ObjectIdentity
bnc = _Bnc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 102)
)
_Drmenginecm_ObjectIdentity = ObjectIdentity
drmenginecm = _Drmenginecm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 103)
)
_Stdc_ObjectIdentity = ObjectIdentity
stdc = _Stdc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 104)
)
_Tview_ObjectIdentity = ObjectIdentity
tview = _Tview_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 105)
)
_PonOa_ObjectIdentity = ObjectIdentity
ponOa = _PonOa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 150)
)
_Mwtea200_ObjectIdentity = ObjectIdentity
mwtea200 = _Mwtea200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 151)
)
_Bti_ObjectIdentity = ObjectIdentity
bti = _Bti_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 200)
)
_RfModMIB_ObjectIdentity = ObjectIdentity
rfModMIB = _RfModMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 201)
)
_BtiIntMIB_ObjectIdentity = ObjectIdentity
btiIntMIB = _BtiIntMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 202)
)
_Sg4000_ObjectIdentity = ObjectIdentity
sg4000 = _Sg4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 203)
)
_PonEm870_ObjectIdentity = ObjectIdentity
ponEm870 = _PonEm870_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 210)
)
_Rpa_ObjectIdentity = ObjectIdentity
rpa = _Rpa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 250)
)
_Rpc_ObjectIdentity = ObjectIdentity
rpc = _Rpc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 251)
)
_Dct5000_ObjectIdentity = ObjectIdentity
dct5000 = _Dct5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 300)
)
_Dct5100_ObjectIdentity = ObjectIdentity
dct5100 = _Dct5100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 301)
)
_Dct5200_ObjectIdentity = ObjectIdentity
dct5200 = _Dct5200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 302)
)
_EdfaMIB_ObjectIdentity = ObjectIdentity
edfaMIB = _EdfaMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 311)
)
_CorvusMIB_ObjectIdentity = ObjectIdentity
corvusMIB = _CorvusMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 312)
)
_Oa600_ObjectIdentity = ObjectIdentity
oa600 = _Oa600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 313)
)
_Dsr350f_ObjectIdentity = ObjectIdentity
dsr350f = _Dsr350f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 321)
)
_CableCard_ObjectIdentity = ObjectIdentity
cableCard = _CableCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 350)
)
_Radd6000_ObjectIdentity = ObjectIdentity
radd6000 = _Radd6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 400)
)
_Cs1000_ObjectIdentity = ObjectIdentity
cs1000 = _Cs1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 401)
)
_Kls_ObjectIdentity = ObjectIdentity
kls = _Kls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 402)
)
_Dac6000_ObjectIdentity = ObjectIdentity
dac6000 = _Dac6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 403)
)
_Sdi_ObjectIdentity = ObjectIdentity
sdi = _Sdi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 404)
)
_Cpms_ObjectIdentity = ObjectIdentity
cpms = _Cpms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 405)
)
_Ap_ObjectIdentity = ObjectIdentity
ap = _Ap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 406)
)
_Ps_ObjectIdentity = ObjectIdentity
ps = _Ps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 407)
)
_MotoIPNSprodID_ObjectIdentity = ObjectIdentity
motoIPNSprodID = _MotoIPNSprodID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 450)
)
_Ird4500x_ObjectIdentity = ObjectIdentity
ird4500x = _Ird4500x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 610)
)
_Ird4520x_ObjectIdentity = ObjectIdentity
ird4520x = _Ird4520x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 620)
)
_Giproxies_ObjectIdentity = ObjectIdentity
giproxies = _Giproxies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 3)
)
_Gicommon_ObjectIdentity = ObjectIdentity
gicommon = _Gicommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 4)
)
_Identity_ObjectIdentity = ObjectIdentity
identity = _Identity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 4, 1)
)
_State_ObjectIdentity = ObjectIdentity
state = _State_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 4, 2)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 4, 3)
)
_Logs_ObjectIdentity = ObjectIdentity
logs = _Logs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 4, 4)
)
_Motproxies_ObjectIdentity = ObjectIdentity
motproxies = _Motproxies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6)
)
_Bcs_ObjectIdentity = ObjectIdentity
bcs = _Bcs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 7)
)
_BcsIdent_ObjectIdentity = ObjectIdentity
bcsIdent = _BcsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 7, 1)
)
_IdentSerialNumber_Type = DisplayString
_IdentSerialNumber_Object = MibScalar
identSerialNumber = _IdentSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 1, 1),
    _IdentSerialNumber_Type()
)
identSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identSerialNumber.setStatus("current")
_IdentChassisNumber_Type = DisplayString
_IdentChassisNumber_Object = MibScalar
identChassisNumber = _IdentChassisNumber_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 1, 2),
    _IdentChassisNumber_Type()
)
identChassisNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identChassisNumber.setStatus("current")


class _IdentIfIndex_Type(Integer32):
    """Custom type identIfIndex based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IdentIfIndex_Type.__name__ = "Integer32"
_IdentIfIndex_Object = MibScalar
identIfIndex = _IdentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 1, 3),
    _IdentIfIndex_Type()
)
identIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identIfIndex.setStatus("current")
_IdentHardwareVersion_Type = DisplayString
_IdentHardwareVersion_Object = MibScalar
identHardwareVersion = _IdentHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 1, 4),
    _IdentHardwareVersion_Type()
)
identHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identHardwareVersion.setStatus("current")
_IdentHardwareFeatures_Type = DisplayString
_IdentHardwareFeatures_Object = MibScalar
identHardwareFeatures = _IdentHardwareFeatures_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 1, 5),
    _IdentHardwareFeatures_Type()
)
identHardwareFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identHardwareFeatures.setStatus("current")
_IdentInventoryCode_Type = DisplayString
_IdentInventoryCode_Object = MibScalar
identInventoryCode = _IdentInventoryCode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 1, 6),
    _IdentInventoryCode_Type()
)
identInventoryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    identInventoryCode.setStatus("current")
_IdentSoftwareVersion_Type = DisplayString
_IdentSoftwareVersion_Object = MibScalar
identSoftwareVersion = _IdentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 1, 7),
    _IdentSoftwareVersion_Type()
)
identSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identSoftwareVersion.setStatus("current")
_IdentLocationArea_Type = DisplayString
_IdentLocationArea_Object = MibScalar
identLocationArea = _IdentLocationArea_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 1, 8),
    _IdentLocationArea_Type()
)
identLocationArea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    identLocationArea.setStatus("current")
_IdentLocationRack_Type = DisplayString
_IdentLocationRack_Object = MibScalar
identLocationRack = _IdentLocationRack_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 1, 9),
    _IdentLocationRack_Type()
)
identLocationRack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    identLocationRack.setStatus("current")
_IdentLocationShelf_Type = DisplayString
_IdentLocationShelf_Object = MibScalar
identLocationShelf = _IdentLocationShelf_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 1, 10),
    _IdentLocationShelf_Type()
)
identLocationShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    identLocationShelf.setStatus("current")
_IdentMIBVersion_Type = DisplayString
_IdentMIBVersion_Object = MibScalar
identMIBVersion = _IdentMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 1, 11),
    _IdentMIBVersion_Type()
)
identMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identMIBVersion.setStatus("current")
_IdentAgentVersion_Type = DisplayString
_IdentAgentVersion_Object = MibScalar
identAgentVersion = _IdentAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 1, 12),
    _IdentAgentVersion_Type()
)
identAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identAgentVersion.setStatus("current")


class _IdentCommand_Type(Integer32):
    """Custom type identCommand based on Integer32"""
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
        *(("currentlyPurgingAndRestarting", 5),
          ("currentlyPurgingNvramAndRestarting", 7),
          ("currentlyRestarting", 2),
          ("purgeAndRestart", 4),
          ("purgeNvramAndRestart", 6),
          ("restart", 1),
          ("unspecified", 3))
    )


_IdentCommand_Type.__name__ = "Integer32"
_IdentCommand_Object = MibScalar
identCommand = _IdentCommand_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 1, 13),
    _IdentCommand_Type()
)
identCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    identCommand.setStatus("current")
_IdentIfExtensionTable_Object = MibTable
identIfExtensionTable = _IdentIfExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 1, 14)
)
if mibBuilder.loadTexts:
    identIfExtensionTable.setStatus("current")
_IdentIfExtensionEntry_Object = MibTableRow
identIfExtensionEntry = _IdentIfExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 1, 14, 1)
)
identIfExtensionEntry.setIndexNames(
    (0, "BCS-IDENT-MIB", "identIfExtensionIndex"),
)
if mibBuilder.loadTexts:
    identIfExtensionEntry.setStatus("current")


class _IdentIfExtensionIndex_Type(Integer32):
    """Custom type identIfExtensionIndex based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IdentIfExtensionIndex_Type.__name__ = "Integer32"
_IdentIfExtensionIndex_Object = MibTableColumn
identIfExtensionIndex = _IdentIfExtensionIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 1, 14, 1, 1),
    _IdentIfExtensionIndex_Type()
)
identIfExtensionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identIfExtensionIndex.setStatus("current")
_IdentIfSerialNumber_Type = DisplayString
_IdentIfSerialNumber_Object = MibTableColumn
identIfSerialNumber = _IdentIfSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 1, 14, 1, 2),
    _IdentIfSerialNumber_Type()
)
identIfSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identIfSerialNumber.setStatus("current")
_IdentIfHardwareVersion_Type = DisplayString
_IdentIfHardwareVersion_Object = MibTableColumn
identIfHardwareVersion = _IdentIfHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 1, 14, 1, 3),
    _IdentIfHardwareVersion_Type()
)
identIfHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identIfHardwareVersion.setStatus("current")
_IdentIfHardwareFeatures_Type = DisplayString
_IdentIfHardwareFeatures_Object = MibTableColumn
identIfHardwareFeatures = _IdentIfHardwareFeatures_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 1, 14, 1, 4),
    _IdentIfHardwareFeatures_Type()
)
identIfHardwareFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identIfHardwareFeatures.setStatus("current")
_IdentIfInventoryCode_Type = DisplayString
_IdentIfInventoryCode_Object = MibTableColumn
identIfInventoryCode = _IdentIfInventoryCode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 1, 14, 1, 5),
    _IdentIfInventoryCode_Type()
)
identIfInventoryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    identIfInventoryCode.setStatus("current")
_IdentIfFirmwareVersion1_Type = DisplayString
_IdentIfFirmwareVersion1_Object = MibTableColumn
identIfFirmwareVersion1 = _IdentIfFirmwareVersion1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 1, 14, 1, 6),
    _IdentIfFirmwareVersion1_Type()
)
identIfFirmwareVersion1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identIfFirmwareVersion1.setStatus("current")
_IdentIfFirmwareVersion2_Type = DisplayString
_IdentIfFirmwareVersion2_Object = MibTableColumn
identIfFirmwareVersion2 = _IdentIfFirmwareVersion2_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 1, 14, 1, 7),
    _IdentIfFirmwareVersion2_Type()
)
identIfFirmwareVersion2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identIfFirmwareVersion2.setStatus("current")
_IdentIfFirmwareVersion3_Type = DisplayString
_IdentIfFirmwareVersion3_Object = MibTableColumn
identIfFirmwareVersion3 = _IdentIfFirmwareVersion3_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 1, 14, 1, 8),
    _IdentIfFirmwareVersion3_Type()
)
identIfFirmwareVersion3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identIfFirmwareVersion3.setStatus("current")
_IdentIfFirmwareVersion4_Type = DisplayString
_IdentIfFirmwareVersion4_Object = MibTableColumn
identIfFirmwareVersion4 = _IdentIfFirmwareVersion4_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 1, 14, 1, 9),
    _IdentIfFirmwareVersion4_Type()
)
identIfFirmwareVersion4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identIfFirmwareVersion4.setStatus("current")


class _IdentIfSlotId_Type(Integer32):
    """Custom type identIfSlotId based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IdentIfSlotId_Type.__name__ = "Integer32"
_IdentIfSlotId_Object = MibTableColumn
identIfSlotId = _IdentIfSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 1, 14, 1, 10),
    _IdentIfSlotId_Type()
)
identIfSlotId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    identIfSlotId.setStatus("current")


class _IdentIfCommand_Type(Integer32):
    """Custom type identIfCommand based on Integer32"""
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
        *(("halt", 4),
          ("reset", 2),
          ("restart", 3),
          ("unspecified", 1))
    )


_IdentIfCommand_Type.__name__ = "Integer32"
_IdentIfCommand_Object = MibTableColumn
identIfCommand = _IdentIfCommand_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 1, 14, 1, 11),
    _IdentIfCommand_Type()
)
identIfCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    identIfCommand.setStatus("current")


class _IdentIfAdministrativeState_Type(Integer32):
    """Custom type identIfAdministrativeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("shuttingDown", 3),
          ("unlocked", 2))
    )


_IdentIfAdministrativeState_Type.__name__ = "Integer32"
_IdentIfAdministrativeState_Object = MibTableColumn
identIfAdministrativeState = _IdentIfAdministrativeState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 1, 14, 1, 12),
    _IdentIfAdministrativeState_Type()
)
identIfAdministrativeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    identIfAdministrativeState.setStatus("current")


class _IdentIfOperationalState_Type(Integer32):
    """Custom type identIfOperationalState based on Integer32"""
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


_IdentIfOperationalState_Type.__name__ = "Integer32"
_IdentIfOperationalState_Object = MibTableColumn
identIfOperationalState = _IdentIfOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 1, 14, 1, 13),
    _IdentIfOperationalState_Type()
)
identIfOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identIfOperationalState.setStatus("current")


class _IdentIfAlarmStatus_Type(Integer32):
    """Custom type identIfAlarmStatus based on Integer32"""
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
        *(("alarmOutstanding", 5),
          ("critical", 2),
          ("idle", 6),
          ("major", 3),
          ("minor", 4),
          ("underRepair", 1))
    )


_IdentIfAlarmStatus_Type.__name__ = "Integer32"
_IdentIfAlarmStatus_Object = MibTableColumn
identIfAlarmStatus = _IdentIfAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 1, 14, 1, 14),
    _IdentIfAlarmStatus_Type()
)
identIfAlarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    identIfAlarmStatus.setStatus("current")


class _IdentIfAvailabilityStatus_Type(Integer32):
    """Custom type identIfAvailabilityStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("available", 10),
          ("degraded", 7),
          ("dependency", 6),
          ("failed", 2),
          ("inTest", 1),
          ("logFull", 9),
          ("notInstalled", 8),
          ("offDuty", 5),
          ("offLine", 4),
          ("powerOff", 3))
    )


_IdentIfAvailabilityStatus_Type.__name__ = "Integer32"
_IdentIfAvailabilityStatus_Object = MibTableColumn
identIfAvailabilityStatus = _IdentIfAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 1, 14, 1, 15),
    _IdentIfAvailabilityStatus_Type()
)
identIfAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identIfAvailabilityStatus.setStatus("current")
_IdentIfSpecific_Type = ObjectIdentifier
_IdentIfSpecific_Object = MibTableColumn
identIfSpecific = _IdentIfSpecific_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 1, 14, 1, 16),
    _IdentIfSpecific_Type()
)
identIfSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identIfSpecific.setStatus("current")


class _IdentIfEntryStatus_Type(EntryStatus):
    """Custom type identIfEntryStatus based on EntryStatus"""


_IdentIfEntryStatus_Object = MibTableColumn
identIfEntryStatus = _IdentIfEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 1, 14, 1, 17),
    _IdentIfEntryStatus_Type()
)
identIfEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    identIfEntryStatus.setStatus("current")
_IdentUnitModel_Type = DisplayString
_IdentUnitModel_Object = MibScalar
identUnitModel = _IdentUnitModel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 1, 15),
    _IdentUnitModel_Type()
)
identUnitModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identUnitModel.setStatus("current")
_BcsLogs_ObjectIdentity = ObjectIdentity
bcsLogs = _BcsLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 7, 4)
)
_BcsSimulcryptScs_ObjectIdentity = ObjectIdentity
bcsSimulcryptScs = _BcsSimulcryptScs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 7, 7)
)
_BcsSimulcryptMux_ObjectIdentity = ObjectIdentity
bcsSimulcryptMux = _BcsSimulcryptMux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 7, 8)
)
_BcsSimulcrypt_ObjectIdentity = ObjectIdentity
bcsSimulcrypt = _BcsSimulcrypt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 7, 9)
)
_BcsDatabase_ObjectIdentity = ObjectIdentity
bcsDatabase = _BcsDatabase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 7, 11)
)
_BcsRedundancy_ObjectIdentity = ObjectIdentity
bcsRedundancy = _BcsRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 7, 12)
)
_BcsMsgGeneration_ObjectIdentity = ObjectIdentity
bcsMsgGeneration = _BcsMsgGeneration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 7, 21)
)
_Mea_ObjectIdentity = ObjectIdentity
mea = _Mea_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 8)
)
_Addressablecontrol_ObjectIdentity = ObjectIdentity
addressablecontrol = _Addressablecontrol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 9)
)
_AcCommon_ObjectIdentity = ObjectIdentity
acCommon = _AcCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 9, 1)
)
_AcSecurity_ObjectIdentity = ObjectIdentity
acSecurity = _AcSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 9, 2)
)
_AcServices_ObjectIdentity = ObjectIdentity
acServices = _AcServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 9, 3)
)
_AcBsi_ObjectIdentity = ObjectIdentity
acBsi = _AcBsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 9, 4)
)
_AcOperations_ObjectIdentity = ObjectIdentity
acOperations = _AcOperations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 9, 5)
)
_AcTopology_ObjectIdentity = ObjectIdentity
acTopology = _AcTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 9, 6)
)
_ChsInternal_ObjectIdentity = ObjectIdentity
chsInternal = _ChsInternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 10)
)
_EmLogin_ObjectIdentity = ObjectIdentity
emLogin = _EmLogin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 10, 1)
)
_RadiusClient_ObjectIdentity = ObjectIdentity
radiusClient = _RadiusClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 10, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BCS-IDENT-MIB",
    **{"EntryStatus": EntryStatus,
       "gi": gi,
       "giproducts": giproducts,
       "acc4000d": acc4000d,
       "anicd": anicd,
       "item1000": item1000,
       "irt1000": irt1000,
       "nc1500": nc1500,
       "om1000": om1000,
       "im1000": im1000,
       "mps": mps,
       "rpd1000": rpd1000,
       "acpStatus": acpStatus,
       "heartbeat": heartbeat,
       "entitlementKey": entitlementKey,
       "arpd": arpd,
       "svom": svom,
       "svm": svm,
       "erm": erm,
       "surfBbnh": surfBbnh,
       "sb2100": sb2100,
       "sb2100D": sb2100D,
       "sb2000": sb2000,
       "saDANIS": saDANIS,
       "apex": apex,
       "rem": rem,
       "mpe": mpe,
       "spe": spe,
       "ne2000": ne2000,
       "apex1500": apex1500,
       "agb": agb,
       "ne2500": ne2500,
       "hdd2000": hdd2000,
       "merlin": merlin,
       "rsr": rsr,
       "gsrm": gsrm,
       "gom": gom,
       "b3": b3,
       "adm": adm,
       "sem": sem,
       "ecmg": ecmg,
       "bsiAdapter": bsiAdapter,
       "oles": oles,
       "ne": ne,
       "tmxCommTrap": tmxCommTrap,
       "drmenginekskdc": drmenginekskdc,
       "drmenginerte": drmenginerte,
       "drmengineecmg": drmengineecmg,
       "drmengineskgpkg": drmengineskgpkg,
       "tmx": tmx,
       "prs": prs,
       "se2000": se2000,
       "dem": dem,
       "ncs": ncs,
       "ucs": ucs,
       "lmm": lmm,
       "se4000": se4000,
       "rc": rc,
       "netSentry": netSentry,
       "sdm": sdm,
       "hfcEms": hfcEms,
       "bnc": bnc,
       "drmenginecm": drmenginecm,
       "stdc": stdc,
       "tview": tview,
       "ponOa": ponOa,
       "mwtea200": mwtea200,
       "bti": bti,
       "rfModMIB": rfModMIB,
       "btiIntMIB": btiIntMIB,
       "sg4000": sg4000,
       "ponEm870": ponEm870,
       "rpa": rpa,
       "rpc": rpc,
       "dct5000": dct5000,
       "dct5100": dct5100,
       "dct5200": dct5200,
       "edfaMIB": edfaMIB,
       "corvusMIB": corvusMIB,
       "oa600": oa600,
       "dsr350f": dsr350f,
       "cableCard": cableCard,
       "radd6000": radd6000,
       "cs1000": cs1000,
       "kls": kls,
       "dac6000": dac6000,
       "sdi": sdi,
       "cpms": cpms,
       "ap": ap,
       "ps": ps,
       "motoIPNSprodID": motoIPNSprodID,
       "ird4500x": ird4500x,
       "ird4520x": ird4520x,
       "giproxies": giproxies,
       "gicommon": gicommon,
       "identity": identity,
       "state": state,
       "traps": traps,
       "logs": logs,
       "motproxies": motproxies,
       "bcs": bcs,
       "bcsIdent": bcsIdent,
       "identSerialNumber": identSerialNumber,
       "identChassisNumber": identChassisNumber,
       "identIfIndex": identIfIndex,
       "identHardwareVersion": identHardwareVersion,
       "identHardwareFeatures": identHardwareFeatures,
       "identInventoryCode": identInventoryCode,
       "identSoftwareVersion": identSoftwareVersion,
       "identLocationArea": identLocationArea,
       "identLocationRack": identLocationRack,
       "identLocationShelf": identLocationShelf,
       "identMIBVersion": identMIBVersion,
       "identAgentVersion": identAgentVersion,
       "identCommand": identCommand,
       "identIfExtensionTable": identIfExtensionTable,
       "identIfExtensionEntry": identIfExtensionEntry,
       "identIfExtensionIndex": identIfExtensionIndex,
       "identIfSerialNumber": identIfSerialNumber,
       "identIfHardwareVersion": identIfHardwareVersion,
       "identIfHardwareFeatures": identIfHardwareFeatures,
       "identIfInventoryCode": identIfInventoryCode,
       "identIfFirmwareVersion1": identIfFirmwareVersion1,
       "identIfFirmwareVersion2": identIfFirmwareVersion2,
       "identIfFirmwareVersion3": identIfFirmwareVersion3,
       "identIfFirmwareVersion4": identIfFirmwareVersion4,
       "identIfSlotId": identIfSlotId,
       "identIfCommand": identIfCommand,
       "identIfAdministrativeState": identIfAdministrativeState,
       "identIfOperationalState": identIfOperationalState,
       "identIfAlarmStatus": identIfAlarmStatus,
       "identIfAvailabilityStatus": identIfAvailabilityStatus,
       "identIfSpecific": identIfSpecific,
       "identIfEntryStatus": identIfEntryStatus,
       "identUnitModel": identUnitModel,
       "bcsLogs": bcsLogs,
       "bcsSimulcryptScs": bcsSimulcryptScs,
       "bcsSimulcryptMux": bcsSimulcryptMux,
       "bcsSimulcrypt": bcsSimulcrypt,
       "bcsDatabase": bcsDatabase,
       "bcsRedundancy": bcsRedundancy,
       "bcsMsgGeneration": bcsMsgGeneration,
       "mea": mea,
       "addressablecontrol": addressablecontrol,
       "acCommon": acCommon,
       "acSecurity": acSecurity,
       "acServices": acServices,
       "acBsi": acBsi,
       "acOperations": acOperations,
       "acTopology": acTopology,
       "chsInternal": chsInternal,
       "emLogin": emLogin,
       "radiusClient": radiusClient}
)
