# SNMP MIB module (BASIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BASIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:41 2024
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

(ciscoWan,
 stratacom) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan",
    "stratacom")

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

basisMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 67)
)
basisMIB.setRevisions(
        ("2003-04-04 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Basis_ObjectIdentity = ObjectIdentity
basis = _Basis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110)
)
_BasisSystem_ObjectIdentity = ObjectIdentity
basisSystem = _BasisSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 1)
)
_BasisShelf_ObjectIdentity = ObjectIdentity
basisShelf = _BasisShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 1)
)
_BasisAsm_ObjectIdentity = ObjectIdentity
basisAsm = _BasisAsm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 2)
)
_AxisRedundancy_ObjectIdentity = ObjectIdentity
axisRedundancy = _AxisRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 3)
)
_AxisSvc_ObjectIdentity = ObjectIdentity
axisSvc = _AxisSvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 4)
)
_AtmAddressRegistration_ObjectIdentity = ObjectIdentity
atmAddressRegistration = _AtmAddressRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 1, 4, 1)
)
_CardGeneric_ObjectIdentity = ObjectIdentity
cardGeneric = _CardGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 2)
)
_CardSpecific_ObjectIdentity = ObjectIdentity
cardSpecific = _CardSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 3)
)
_AtmLmiSignaling_ObjectIdentity = ObjectIdentity
atmLmiSignaling = _AtmLmiSignaling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 3, 4)
)
_BasisLines_ObjectIdentity = ObjectIdentity
basisLines = _BasisLines_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4)
)
_Dsx1_ObjectIdentity = ObjectIdentity
dsx1 = _Dsx1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3)
)
_Dsx1Line_ObjectIdentity = ObjectIdentity
dsx1Line = _Dsx1Line_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1)
)
_Dsx1Framing_ObjectIdentity = ObjectIdentity
dsx1Framing = _Dsx1Framing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 2)
)
_Dsx1Plcp_ObjectIdentity = ObjectIdentity
dsx1Plcp = _Dsx1Plcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 3)
)
_Dsx3_ObjectIdentity = ObjectIdentity
dsx3 = _Dsx3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4)
)
_Dsx3Line_ObjectIdentity = ObjectIdentity
dsx3Line = _Dsx3Line_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1)
)
_Dsx3Framing_ObjectIdentity = ObjectIdentity
dsx3Framing = _Dsx3Framing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2)
)
_Plcp_ObjectIdentity = ObjectIdentity
plcp = _Plcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 3)
)
_X21_ObjectIdentity = ObjectIdentity
x21 = _X21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 5)
)
_Sonet_ObjectIdentity = ObjectIdentity
sonet = _Sonet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6)
)
_CwsonetObjects_ObjectIdentity = ObjectIdentity
cwsonetObjects = _CwsonetObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1)
)
_Dsx0Vism_ObjectIdentity = ObjectIdentity
dsx0Vism = _Dsx0Vism_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 7)
)
_BasisServices_ObjectIdentity = ObjectIdentity
basisServices = _BasisServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5)
)
_FrameRelay_ObjectIdentity = ObjectIdentity
frameRelay = _FrameRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1)
)
_FrPort_ObjectIdentity = ObjectIdentity
frPort = _FrPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1)
)
_FrPortCnf_ObjectIdentity = ObjectIdentity
frPortCnf = _FrPortCnf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1)
)
_FrPortCnfSig_ObjectIdentity = ObjectIdentity
frPortCnfSig = _FrPortCnfSig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 2)
)
_FrPortCnfX21PortGrp_ObjectIdentity = ObjectIdentity
frPortCnfX21PortGrp = _FrPortCnfX21PortGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3)
)
_FrPortServiceQueGrp_ObjectIdentity = ObjectIdentity
frPortServiceQueGrp = _FrPortServiceQueGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 4)
)
_FrPortCnfResPartGrp_ObjectIdentity = ObjectIdentity
frPortCnfResPartGrp = _FrPortCnfResPartGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 5)
)
_FrPortCnt_ObjectIdentity = ObjectIdentity
frPortCnt = _FrPortCnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2)
)
_FrPortCntSig_ObjectIdentity = ObjectIdentity
frPortCntSig = _FrPortCntSig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 2)
)
_FrChan_ObjectIdentity = ObjectIdentity
frChan = _FrChan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2)
)
_Atm_ObjectIdentity = ObjectIdentity
atm = _Atm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2)
)
_AusmPort_ObjectIdentity = ObjectIdentity
ausmPort = _AusmPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 1)
)
_AusmPortCnf_ObjectIdentity = ObjectIdentity
ausmPortCnf = _AusmPortCnf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 1, 1)
)
_AusmPortCnt_ObjectIdentity = ObjectIdentity
ausmPortCnt = _AusmPortCnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 1, 3)
)
_AusmChan_ObjectIdentity = ObjectIdentity
ausmChan = _AusmChan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 2)
)
_AtmLines_ObjectIdentity = ObjectIdentity
atmLines = _AtmLines_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 5)
)
_AtmLineCnfGrp_ObjectIdentity = ObjectIdentity
atmLineCnfGrp = _AtmLineCnfGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 5, 1)
)
_AtmLineCntGrp_ObjectIdentity = ObjectIdentity
atmLineCntGrp = _AtmLineCntGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 5, 2)
)
_BbInterface_ObjectIdentity = ObjectIdentity
bbInterface = _BbInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6)
)
_BbIfCnf_ObjectIdentity = ObjectIdentity
bbIfCnf = _BbIfCnf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 1)
)
_BbIfCnfResPartGrp_ObjectIdentity = ObjectIdentity
bbIfCnfResPartGrp = _BbIfCnfResPartGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 2)
)
_BbIfStateGrp_ObjectIdentity = ObjectIdentity
bbIfStateGrp = _BbIfStateGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 3)
)
_BbIfCnt_ObjectIdentity = ObjectIdentity
bbIfCnt = _BbIfCnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4)
)
_BbChan_ObjectIdentity = ObjectIdentity
bbChan = _BbChan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7)
)
_BbChanCnfGrp_ObjectIdentity = ObjectIdentity
bbChanCnfGrp = _BbChanCnfGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1)
)
_BbChanStateGrp_ObjectIdentity = ObjectIdentity
bbChanStateGrp = _BbChanStateGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 2)
)
_BbChanCntGrp_ObjectIdentity = ObjectIdentity
bbChanCntGrp = _BbChanCntGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 3)
)
_VirtualInterface_ObjectIdentity = ObjectIdentity
virtualInterface = _VirtualInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8)
)
_RpmInterface_ObjectIdentity = ObjectIdentity
rpmInterface = _RpmInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9)
)
_RpmPort_ObjectIdentity = ObjectIdentity
rpmPort = _RpmPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1)
)
_RpmChan_ObjectIdentity = ObjectIdentity
rpmChan = _RpmChan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10)
)
_RpmChanGrp_ObjectIdentity = ObjectIdentity
rpmChanGrp = _RpmChanGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1)
)
_CircuitEmulation_ObjectIdentity = ObjectIdentity
circuitEmulation = _CircuitEmulation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3)
)
_CesmChan_ObjectIdentity = ObjectIdentity
cesmChan = _CesmChan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2)
)
_Sna_ObjectIdentity = ObjectIdentity
sna = _Sna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 4)
)
_Snaport_ObjectIdentity = ObjectIdentity
snaport = _Snaport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 4, 1)
)
_SnaportCnf_ObjectIdentity = ObjectIdentity
snaportCnf = _SnaportCnf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 4, 1, 1)
)
_SnaportCnfSig_ObjectIdentity = ObjectIdentity
snaportCnfSig = _SnaportCnfSig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 4, 1, 1, 2)
)
_SnaportCnt_ObjectIdentity = ObjectIdentity
snaportCnt = _SnaportCnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 4, 1, 2)
)
_SnaPortCntSig_ObjectIdentity = ObjectIdentity
snaPortCntSig = _SnaPortCntSig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 4, 1, 2, 2)
)
_Voice_ObjectIdentity = ObjectIdentity
voice = _Voice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5)
)
_VismPort_ObjectIdentity = ObjectIdentity
vismPort = _VismPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2)
)
_VismChanGrp_ObjectIdentity = ObjectIdentity
vismChanGrp = _VismChanGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3)
)
_VismChanCnfGrp_ObjectIdentity = ObjectIdentity
vismChanCnfGrp = _VismChanCnfGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1)
)
_AxisDiagnostics_ObjectIdentity = ObjectIdentity
axisDiagnostics = _AxisDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 6)
)
_Par_ObjectIdentity = ObjectIdentity
par = _Par_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 130)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BASIS-MIB",
    **{"basis": basis,
       "basisSystem": basisSystem,
       "basisShelf": basisShelf,
       "basisAsm": basisAsm,
       "axisRedundancy": axisRedundancy,
       "axisSvc": axisSvc,
       "atmAddressRegistration": atmAddressRegistration,
       "cardGeneric": cardGeneric,
       "cardSpecific": cardSpecific,
       "atmLmiSignaling": atmLmiSignaling,
       "basisLines": basisLines,
       "dsx1": dsx1,
       "dsx1Line": dsx1Line,
       "dsx1Framing": dsx1Framing,
       "dsx1Plcp": dsx1Plcp,
       "dsx3": dsx3,
       "dsx3Line": dsx3Line,
       "dsx3Framing": dsx3Framing,
       "plcp": plcp,
       "x21": x21,
       "sonet": sonet,
       "cwsonetObjects": cwsonetObjects,
       "dsx0Vism": dsx0Vism,
       "basisServices": basisServices,
       "frameRelay": frameRelay,
       "frPort": frPort,
       "frPortCnf": frPortCnf,
       "frPortCnfSig": frPortCnfSig,
       "frPortCnfX21PortGrp": frPortCnfX21PortGrp,
       "frPortServiceQueGrp": frPortServiceQueGrp,
       "frPortCnfResPartGrp": frPortCnfResPartGrp,
       "frPortCnt": frPortCnt,
       "frPortCntSig": frPortCntSig,
       "frChan": frChan,
       "atm": atm,
       "ausmPort": ausmPort,
       "ausmPortCnf": ausmPortCnf,
       "ausmPortCnt": ausmPortCnt,
       "ausmChan": ausmChan,
       "atmLines": atmLines,
       "atmLineCnfGrp": atmLineCnfGrp,
       "atmLineCntGrp": atmLineCntGrp,
       "bbInterface": bbInterface,
       "bbIfCnf": bbIfCnf,
       "bbIfCnfResPartGrp": bbIfCnfResPartGrp,
       "bbIfStateGrp": bbIfStateGrp,
       "bbIfCnt": bbIfCnt,
       "bbChan": bbChan,
       "bbChanCnfGrp": bbChanCnfGrp,
       "bbChanStateGrp": bbChanStateGrp,
       "bbChanCntGrp": bbChanCntGrp,
       "virtualInterface": virtualInterface,
       "rpmInterface": rpmInterface,
       "rpmPort": rpmPort,
       "rpmChan": rpmChan,
       "rpmChanGrp": rpmChanGrp,
       "circuitEmulation": circuitEmulation,
       "cesmChan": cesmChan,
       "sna": sna,
       "snaport": snaport,
       "snaportCnf": snaportCnf,
       "snaportCnfSig": snaportCnfSig,
       "snaportCnt": snaportCnt,
       "snaPortCntSig": snaPortCntSig,
       "voice": voice,
       "vismPort": vismPort,
       "vismChanGrp": vismChanGrp,
       "vismChanCnfGrp": vismChanCnfGrp,
       "axisDiagnostics": axisDiagnostics,
       "par": par,
       "basisMIB": basisMIB}
)
