# SNMP MIB module (Avaya-96xxIPTelephone-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Avaya-96xxIPTelephone-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:11 2024
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

avaya96xxMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Avaya_ObjectIdentity = ObjectIdentity
avaya = _Avaya_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1)
)
_AvayaipEndpointProd_ObjectIdentity = ObjectIdentity
avayaipEndpointProd = _AvayaipEndpointProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 69)
)
_AvayaMibs_ObjectIdentity = ObjectIdentity
avayaMibs = _AvayaMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2)
)
_IpEndpointMIBs_ObjectIdentity = ObjectIdentity
ipEndpointMIBs = _IpEndpointMIBs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69)
)
_EndptID_ObjectIdentity = ObjectIdentity
endptID = _EndptID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1)
)
_EndptAGCHAND_Type = Integer32
_EndptAGCHAND_Object = MibScalar
endptAGCHAND = _EndptAGCHAND_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 1),
    _EndptAGCHAND_Type()
)
endptAGCHAND.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptAGCHAND.setStatus("current")
_EndptAGCHEAD_Type = Integer32
_EndptAGCHEAD_Object = MibScalar
endptAGCHEAD = _EndptAGCHEAD_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 2),
    _EndptAGCHEAD_Type()
)
endptAGCHEAD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptAGCHEAD.setStatus("current")
_EndptAGCSPKR_Type = Integer32
_EndptAGCSPKR_Object = MibScalar
endptAGCSPKR = _EndptAGCSPKR_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 3),
    _EndptAGCSPKR_Type()
)
endptAGCSPKR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptAGCSPKR.setStatus("current")
_EndptAPPINUSE_Type = DisplayString
_EndptAPPINUSE_Object = MibScalar
endptAPPINUSE = _EndptAPPINUSE_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 4),
    _EndptAPPINUSE_Type()
)
endptAPPINUSE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptAPPINUSE.setStatus("current")
_EndptAPPNAME_Type = DisplayString
_EndptAPPNAME_Object = MibScalar
endptAPPNAME = _EndptAPPNAME_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 5),
    _EndptAPPNAME_Type()
)
endptAPPNAME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptAPPNAME.setStatus("current")
_EndptBAKLIGHTOFF_Type = Integer32
_EndptBAKLIGHTOFF_Object = MibScalar
endptBAKLIGHTOFF = _EndptBAKLIGHTOFF_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 6),
    _EndptBAKLIGHTOFF_Type()
)
endptBAKLIGHTOFF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptBAKLIGHTOFF.setStatus("current")
_EndptBOOTNAME_Type = DisplayString
_EndptBOOTNAME_Object = MibScalar
endptBOOTNAME = _EndptBOOTNAME_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 7),
    _EndptBOOTNAME_Type()
)
endptBOOTNAME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptBOOTNAME.setStatus("current")
_EndptBRURI_Type = DisplayString
_EndptBRURI_Object = MibScalar
endptBRURI = _EndptBRURI_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 8),
    _EndptBRURI_Type()
)
endptBRURI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptBRURI.setStatus("current")
_EndptCNAPORT_Type = Integer32
_EndptCNAPORT_Object = MibScalar
endptCNAPORT = _EndptCNAPORT_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 9),
    _EndptCNAPORT_Type()
)
endptCNAPORT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptCNAPORT.setStatus("current")
_EndptCNASRVR_Type = DisplayString
_EndptCNASRVR_Object = MibScalar
endptCNASRVR = _EndptCNASRVR_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 10),
    _EndptCNASRVR_Type()
)
endptCNASRVR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptCNASRVR.setStatus("current")
_EndptCODECR_Type = DisplayString
_EndptCODECR_Object = MibScalar
endptCODECR = _EndptCODECR_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 11),
    _EndptCODECR_Type()
)
endptCODECR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptCODECR.setStatus("current")
_EndptCODECT_Type = DisplayString
_EndptCODECT_Object = MibScalar
endptCODECT = _EndptCODECT_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 12),
    _EndptCODECT_Type()
)
endptCODECT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptCODECT.setStatus("current")
_EndptDHCPLEASEREBIND_Type = Integer32
_EndptDHCPLEASEREBIND_Object = MibScalar
endptDHCPLEASEREBIND = _EndptDHCPLEASEREBIND_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 13),
    _EndptDHCPLEASEREBIND_Type()
)
endptDHCPLEASEREBIND.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptDHCPLEASEREBIND.setStatus("current")
_EndptDHCPLEASERENEW_Type = Integer32
_EndptDHCPLEASERENEW_Object = MibScalar
endptDHCPLEASERENEW = _EndptDHCPLEASERENEW_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 14),
    _EndptDHCPLEASERENEW_Type()
)
endptDHCPLEASERENEW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptDHCPLEASERENEW.setStatus("current")
_EndptDHCPLEASETIME_Type = Integer32
_EndptDHCPLEASETIME_Object = MibScalar
endptDHCPLEASETIME = _EndptDHCPLEASETIME_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 15),
    _EndptDHCPLEASETIME_Type()
)
endptDHCPLEASETIME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptDHCPLEASETIME.setStatus("current")
_EndptDNSSRVR_Type = DisplayString
_EndptDNSSRVR_Object = MibScalar
endptDNSSRVR = _EndptDNSSRVR_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 16),
    _EndptDNSSRVR_Type()
)
endptDNSSRVR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptDNSSRVR.setStatus("current")
_EndptDOMAIN_Type = DisplayString
_EndptDOMAIN_Object = MibScalar
endptDOMAIN = _EndptDOMAIN_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 17),
    _EndptDOMAIN_Type()
)
endptDOMAIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptDOMAIN.setStatus("current")
_EndptDOT1X_Type = Integer32
_EndptDOT1X_Object = MibScalar
endptDOT1X = _EndptDOT1X_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 18),
    _EndptDOT1X_Type()
)
endptDOT1X.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptDOT1X.setStatus("current")
_EndptDSCPAUD_Type = Integer32
_EndptDSCPAUD_Object = MibScalar
endptDSCPAUD = _EndptDSCPAUD_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 19),
    _EndptDSCPAUD_Type()
)
endptDSCPAUD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptDSCPAUD.setStatus("current")
_EndptDSCPBBE_Type = Integer32
_EndptDSCPBBE_Object = MibScalar
endptDSCPBBE = _EndptDSCPBBE_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 20),
    _EndptDSCPBBE_Type()
)
endptDSCPBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptDSCPBBE.setStatus("current")
_EndptDSCPSIG_Type = Integer32
_EndptDSCPSIG_Object = MibScalar
endptDSCPSIG = _EndptDSCPSIG_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 21),
    _EndptDSCPSIG_Type()
)
endptDSCPSIG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptDSCPSIG.setStatus("current")
_EndptDSPVERSION_Type = DisplayString
_EndptDSPVERSION_Object = MibScalar
endptDSPVERSION = _EndptDSPVERSION_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 22),
    _EndptDSPVERSION_Type()
)
endptDSPVERSION.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptDSPVERSION.setStatus("current")
_EndptFEIPADD_Type = IpAddress
_EndptFEIPADD_Object = MibScalar
endptFEIPADD = _EndptFEIPADD_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 23),
    _EndptFEIPADD_Type()
)
endptFEIPADD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptFEIPADD.setStatus("current")
_EndptFEPORT_Type = Integer32
_EndptFEPORT_Object = MibScalar
endptFEPORT = _EndptFEPORT_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 24),
    _EndptFEPORT_Type()
)
endptFEPORT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptFEPORT.setStatus("current")
_EndptGIPADD_Type = DisplayString
_EndptGIPADD_Object = MibScalar
endptGIPADD = _EndptGIPADD_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 25),
    _EndptGIPADD_Type()
)
endptGIPADD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptGIPADD.setStatus("current")
_EndptGIPINUSE_Type = IpAddress
_EndptGIPINUSE_Object = MibScalar
endptGIPINUSE = _EndptGIPINUSE_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 26),
    _EndptGIPINUSE_Type()
)
endptGIPINUSE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptGIPINUSE.setStatus("current")
_EndptGROUP_Type = Integer32
_EndptGROUP_Object = MibScalar
endptGROUP = _EndptGROUP_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 27),
    _EndptGROUP_Type()
)
endptGROUP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptGROUP.setStatus("current")
_EndptHTTPDIR_Type = DisplayString
_EndptHTTPDIR_Object = MibScalar
endptHTTPDIR = _EndptHTTPDIR_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 28),
    _EndptHTTPDIR_Type()
)
endptHTTPDIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptHTTPDIR.setStatus("current")
_EndptHTTPSRVR_Type = DisplayString
_EndptHTTPSRVR_Object = MibScalar
endptHTTPSRVR = _EndptHTTPSRVR_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 29),
    _EndptHTTPSRVR_Type()
)
endptHTTPSRVR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptHTTPSRVR.setStatus("current")
_EndptHTTPUSED_Type = IpAddress
_EndptHTTPUSED_Object = MibScalar
endptHTTPUSED = _EndptHTTPUSED_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 30),
    _EndptHTTPUSED_Type()
)
endptHTTPUSED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptHTTPUSED.setStatus("current")
_EndptICMPDU_Type = Integer32
_EndptICMPDU_Object = MibScalar
endptICMPDU = _EndptICMPDU_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 31),
    _EndptICMPDU_Type()
)
endptICMPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptICMPDU.setStatus("current")
_EndptICMPRED_Type = Integer32
_EndptICMPRED_Object = MibScalar
endptICMPRED = _EndptICMPRED_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 32),
    _EndptICMPRED_Type()
)
endptICMPRED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptICMPRED.setStatus("current")
_EndptIPADD_Type = IpAddress
_EndptIPADD_Object = MibScalar
endptIPADD = _EndptIPADD_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 33),
    _EndptIPADD_Type()
)
endptIPADD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptIPADD.setStatus("current")
_EndptJMSEC_Type = Integer32
_EndptJMSEC_Object = MibScalar
endptJMSEC = _EndptJMSEC_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 34),
    _EndptJMSEC_Type()
)
endptJMSEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptJMSEC.setStatus("current")
_EndptL2Q_Type = Integer32
_EndptL2Q_Object = MibScalar
endptL2Q = _EndptL2Q_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 35),
    _EndptL2Q_Type()
)
endptL2Q.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptL2Q.setStatus("current")
_EndptL2QAUD_Type = Integer32
_EndptL2QAUD_Object = MibScalar
endptL2QAUD = _EndptL2QAUD_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 36),
    _EndptL2QAUD_Type()
)
endptL2QAUD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptL2QAUD.setStatus("current")
_EndptL2QSIG_Type = Integer32
_EndptL2QSIG_Object = MibScalar
endptL2QSIG = _EndptL2QSIG_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 37),
    _EndptL2QSIG_Type()
)
endptL2QSIG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptL2QSIG.setStatus("current")
_EndptL2QSTAT_Type = Integer32
_EndptL2QSTAT_Object = MibScalar
endptL2QSTAT = _EndptL2QSTAT_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 38),
    _EndptL2QSTAT_Type()
)
endptL2QSTAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptL2QSTAT.setStatus("current")
_EndptL2QVLAN_Type = Integer32
_EndptL2QVLAN_Object = MibScalar
endptL2QVLAN = _EndptL2QVLAN_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 39),
    _EndptL2QVLAN_Type()
)
endptL2QVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptL2QVLAN.setStatus("current")
_EndptL2QVLANINUSE_Type = Integer32
_EndptL2QVLANINUSE_Object = MibScalar
endptL2QVLANINUSE = _EndptL2QVLANINUSE_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 40),
    _EndptL2QVLANINUSE_Type()
)
endptL2QVLANINUSE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptL2QVLANINUSE.setStatus("current")
_EndptLOGSRVR_Type = DisplayString
_EndptLOGSRVR_Object = MibScalar
endptLOGSRVR = _EndptLOGSRVR_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 41),
    _EndptLOGSRVR_Type()
)
endptLOGSRVR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptLOGSRVR.setStatus("current")
_EndptMACADDR_Type = DisplayString
_EndptMACADDR_Object = MibScalar
endptMACADDR = _EndptMACADDR_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 42),
    _EndptMACADDR_Type()
)
endptMACADDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptMACADDR.setStatus("current")
_EndptMODEL_Type = DisplayString
_EndptMODEL_Object = MibScalar
endptMODEL = _EndptMODEL_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 43),
    _EndptMODEL_Type()
)
endptMODEL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptMODEL.setStatus("current")
_EndptNETMASK_Type = IpAddress
_EndptNETMASK_Object = MibScalar
endptNETMASK = _EndptNETMASK_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 44),
    _EndptNETMASK_Type()
)
endptNETMASK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptNETMASK.setStatus("current")
_EndptPHONECC_Type = DisplayString
_EndptPHONECC_Object = MibScalar
endptPHONECC = _EndptPHONECC_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 45),
    _EndptPHONECC_Type()
)
endptPHONECC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptPHONECC.setStatus("current")
_EndptPHONESN_Type = DisplayString
_EndptPHONESN_Object = MibScalar
endptPHONESN = _EndptPHONESN_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 46),
    _EndptPHONESN_Type()
)
endptPHONESN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptPHONESN.setStatus("current")
_EndptPHY1DUPLEX_Type = Integer32
_EndptPHY1DUPLEX_Object = MibScalar
endptPHY1DUPLEX = _EndptPHY1DUPLEX_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 47),
    _EndptPHY1DUPLEX_Type()
)
endptPHY1DUPLEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptPHY1DUPLEX.setStatus("current")
_EndptPHY1SPEED_Type = Integer32
_EndptPHY1SPEED_Object = MibScalar
endptPHY1SPEED = _EndptPHY1SPEED_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 48),
    _EndptPHY1SPEED_Type()
)
endptPHY1SPEED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptPHY1SPEED.setStatus("current")
_EndptPHY1STAT_Type = Integer32
_EndptPHY1STAT_Object = MibScalar
endptPHY1STAT = _EndptPHY1STAT_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 49),
    _EndptPHY1STAT_Type()
)
endptPHY1STAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptPHY1STAT.setStatus("current")
_EndptPHY2DUPLEX_Type = Integer32
_EndptPHY2DUPLEX_Object = MibScalar
endptPHY2DUPLEX = _EndptPHY2DUPLEX_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 50),
    _EndptPHY2DUPLEX_Type()
)
endptPHY2DUPLEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptPHY2DUPLEX.setStatus("current")
_EndptPHY2PRIO_Type = Integer32
_EndptPHY2PRIO_Object = MibScalar
endptPHY2PRIO = _EndptPHY2PRIO_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 51),
    _EndptPHY2PRIO_Type()
)
endptPHY2PRIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptPHY2PRIO.setStatus("current")
_EndptPHY2SPEED_Type = Integer32
_EndptPHY2SPEED_Object = MibScalar
endptPHY2SPEED = _EndptPHY2SPEED_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 52),
    _EndptPHY2SPEED_Type()
)
endptPHY2SPEED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptPHY2SPEED.setStatus("current")
_EndptPHY2STAT_Type = Integer32
_EndptPHY2STAT_Object = MibScalar
endptPHY2STAT = _EndptPHY2STAT_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 53),
    _EndptPHY2STAT_Type()
)
endptPHY2STAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptPHY2STAT.setStatus("current")
_EndptPHY2VLAN_Type = Integer32
_EndptPHY2VLAN_Object = MibScalar
endptPHY2VLAN = _EndptPHY2VLAN_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 54),
    _EndptPHY2VLAN_Type()
)
endptPHY2VLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptPHY2VLAN.setStatus("current")
_EndptPORTAUD_Type = Integer32
_EndptPORTAUD_Object = MibScalar
endptPORTAUD = _EndptPORTAUD_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 55),
    _EndptPORTAUD_Type()
)
endptPORTAUD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptPORTAUD.setStatus("current")
_EndptPROCPSWD_Type = Integer32
_EndptPROCPSWD_Object = MibScalar
endptPROCPSWD = _EndptPROCPSWD_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 56),
    _EndptPROCPSWD_Type()
)
endptPROCPSWD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptPROCPSWD.setStatus("current")
_EndptPROCSTAT_Type = Integer32
_EndptPROCSTAT_Object = MibScalar
endptPROCSTAT = _EndptPROCSTAT_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 57),
    _EndptPROCSTAT_Type()
)
endptPROCSTAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptPROCSTAT.setStatus("current")
_EndptPWBCC_Type = DisplayString
_EndptPWBCC_Object = MibScalar
endptPWBCC = _EndptPWBCC_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 58),
    _EndptPWBCC_Type()
)
endptPWBCC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptPWBCC.setStatus("current")
_EndptPWBSN_Type = DisplayString
_EndptPWBSN_Object = MibScalar
endptPWBSN = _EndptPWBSN_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 59),
    _EndptPWBSN_Type()
)
endptPWBSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptPWBSN.setStatus("current")
_EndptRTCPCONT_Type = Integer32
_EndptRTCPCONT_Object = MibScalar
endptRTCPCONT = _EndptRTCPCONT_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 60),
    _EndptRTCPCONT_Type()
)
endptRTCPCONT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptRTCPCONT.setStatus("current")
_EndptRTCPFLOW_Type = Integer32
_EndptRTCPFLOW_Object = MibScalar
endptRTCPFLOW = _EndptRTCPFLOW_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 61),
    _EndptRTCPFLOW_Type()
)
endptRTCPFLOW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptRTCPFLOW.setStatus("current")
_EndptRTCPMON_Type = IpAddress
_EndptRTCPMON_Object = MibScalar
endptRTCPMON = _EndptRTCPMON_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 62),
    _EndptRTCPMON_Type()
)
endptRTCPMON.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptRTCPMON.setStatus("current")
_EndptRSVPCONT_Type = Integer32
_EndptRSVPCONT_Object = MibScalar
endptRSVPCONT = _EndptRSVPCONT_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 63),
    _EndptRSVPCONT_Type()
)
endptRSVPCONT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptRSVPCONT.setStatus("current")
_EndptRSVPRFRSH_Type = Integer32
_EndptRSVPRFRSH_Object = MibScalar
endptRSVPRFRSH = _EndptRSVPRFRSH_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 64),
    _EndptRSVPRFRSH_Type()
)
endptRSVPRFRSH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptRSVPRFRSH.setStatus("current")
_EndptRSVPRTRY_Type = Integer32
_EndptRSVPRTRY_Object = MibScalar
endptRSVPRTRY = _EndptRSVPRTRY_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 65),
    _EndptRSVPRTRY_Type()
)
endptRSVPRTRY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptRSVPRTRY.setStatus("current")
_EndptRSVPPROF_Type = Integer32
_EndptRSVPPROF_Object = MibScalar
endptRSVPPROF = _EndptRSVPPROF_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 66),
    _EndptRSVPPROF_Type()
)
endptRSVPPROF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptRSVPPROF.setStatus("current")
_EndptSIG_Type = Integer32
_EndptSIG_Object = MibScalar
endptSIG = _EndptSIG_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 67),
    _EndptSIG_Type()
)
endptSIG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptSIG.setStatus("current")
_EndptSNMPADD_Type = DisplayString
_EndptSNMPADD_Object = MibScalar
endptSNMPADD = _EndptSNMPADD_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 68),
    _EndptSNMPADD_Type()
)
endptSNMPADD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptSNMPADD.setStatus("current")
_EndptSTATIC_Type = Integer32
_EndptSTATIC_Object = MibScalar
endptSTATIC = _EndptSTATIC_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 69),
    _EndptSTATIC_Type()
)
endptSTATIC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptSTATIC.setStatus("current")
_EndptTLSSRVR_Type = DisplayString
_EndptTLSSRVR_Object = MibScalar
endptTLSSRVR = _EndptTLSSRVR_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 70),
    _EndptTLSSRVR_Type()
)
endptTLSSRVR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptTLSSRVR.setStatus("current")
_EndptTLSUSED_Type = IpAddress
_EndptTLSUSED_Object = MibScalar
endptTLSUSED = _EndptTLSUSED_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 71),
    _EndptTLSUSED_Type()
)
endptTLSUSED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptTLSUSED.setStatus("current")
_EndptTMSEC_Type = Integer32
_EndptTMSEC_Object = MibScalar
endptTMSEC = _EndptTMSEC_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 72),
    _EndptTMSEC_Type()
)
endptTMSEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptTMSEC.setStatus("current")
_EndptVLANLIST_Type = DisplayString
_EndptVLANLIST_Object = MibScalar
endptVLANLIST = _EndptVLANLIST_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 73),
    _EndptVLANLIST_Type()
)
endptVLANLIST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptVLANLIST.setStatus("current")
_EndptVLANSEP_Type = Integer32
_EndptVLANSEP_Object = MibScalar
endptVLANSEP = _EndptVLANSEP_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 74),
    _EndptVLANSEP_Type()
)
endptVLANSEP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptVLANSEP.setStatus("current")
_EndptFONT_Type = DisplayString
_EndptFONT_Object = MibScalar
endptFONT = _EndptFONT_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 75),
    _EndptFONT_Type()
)
endptFONT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptFONT.setStatus("current")
_EndptLANGFILES_Type = DisplayString
_EndptLANGFILES_Object = MibScalar
endptLANGFILES = _EndptLANGFILES_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 76),
    _EndptLANGFILES_Type()
)
endptLANGFILES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptLANGFILES.setStatus("current")
_EndptPHNEMERGNUM_Type = DisplayString
_EndptPHNEMERGNUM_Object = MibScalar
endptPHNEMERGNUM = _EndptPHNEMERGNUM_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 77),
    _EndptPHNEMERGNUM_Type()
)
endptPHNEMERGNUM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptPHNEMERGNUM.setStatus("current")
_EndptAUDIOENV_Type = Integer32
_EndptAUDIOENV_Object = MibScalar
endptAUDIOENV = _EndptAUDIOENV_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 78),
    _EndptAUDIOENV_Type()
)
endptAUDIOENV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptAUDIOENV.setStatus("current")
_EndptAUDIOSTHD_Type = Integer32
_EndptAUDIOSTHD_Object = MibScalar
endptAUDIOSTHD = _EndptAUDIOSTHD_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 79),
    _EndptAUDIOSTHD_Type()
)
endptAUDIOSTHD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptAUDIOSTHD.setStatus("current")
_EndptAUDIOSTHS_Type = Integer32
_EndptAUDIOSTHS_Object = MibScalar
endptAUDIOSTHS = _EndptAUDIOSTHS_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 80),
    _EndptAUDIOSTHS_Type()
)
endptAUDIOSTHS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptAUDIOSTHS.setStatus("current")
_EndptBRAUTH_Type = Integer32
_EndptBRAUTH_Object = MibScalar
endptBRAUTH = _EndptBRAUTH_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 81),
    _EndptBRAUTH_Type()
)
endptBRAUTH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptBRAUTH.setStatus("current")
_EndptDHCPINUSE_Type = IpAddress
_EndptDHCPINUSE_Object = MibScalar
endptDHCPINUSE = _EndptDHCPINUSE_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 82),
    _EndptDHCPINUSE_Type()
)
endptDHCPINUSE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptDHCPINUSE.setStatus("current")
_EndptDHCPLEASEEXP_Type = Integer32
_EndptDHCPLEASEEXP_Object = MibScalar
endptDHCPLEASEEXP = _EndptDHCPLEASEEXP_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 83),
    _EndptDHCPLEASEEXP_Type()
)
endptDHCPLEASEEXP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptDHCPLEASEEXP.setStatus("current")
_EndptDHCPSTD_Type = Integer32
_EndptDHCPSTD_Object = MibScalar
endptDHCPSTD = _EndptDHCPSTD_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 84),
    _EndptDHCPSTD_Type()
)
endptDHCPSTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptDHCPSTD.setStatus("current")
_EndptDHCPT1REM_Type = Integer32
_EndptDHCPT1REM_Object = MibScalar
endptDHCPT1REM = _EndptDHCPT1REM_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 85),
    _EndptDHCPT1REM_Type()
)
endptDHCPT1REM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptDHCPT1REM.setStatus("current")
_EndptDHCPT2REM_Type = Integer32
_EndptDHCPT2REM_Object = MibScalar
endptDHCPT2REM = _EndptDHCPT2REM_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 86),
    _EndptDHCPT2REM_Type()
)
endptDHCPT2REM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptDHCPT2REM.setStatus("current")
_EndptDOT1XSTAT_Type = Integer32
_EndptDOT1XSTAT_Object = MibScalar
endptDOT1XSTAT = _EndptDOT1XSTAT_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 87),
    _EndptDOT1XSTAT_Type()
)
endptDOT1XSTAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptDOT1XSTAT.setStatus("current")
_EndptHTTPPORT_Type = Integer32
_EndptHTTPPORT_Object = MibScalar
endptHTTPPORT = _EndptHTTPPORT_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 88),
    _EndptHTTPPORT_Type()
)
endptHTTPPORT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptHTTPPORT.setStatus("current")
_EndptTLSDIR_Type = DisplayString
_EndptTLSDIR_Object = MibScalar
endptTLSDIR = _EndptTLSDIR_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 89),
    _EndptTLSDIR_Type()
)
endptTLSDIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptTLSDIR.setStatus("current")
_EndptTLSPORT_Type = DisplayString
_EndptTLSPORT_Object = MibScalar
endptTLSPORT = _EndptTLSPORT_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 90),
    _EndptTLSPORT_Type()
)
endptTLSPORT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptTLSPORT.setStatus("current")
_EndptMEMHEAPFREE_Type = Integer32
_EndptMEMHEAPFREE_Object = MibScalar
endptMEMHEAPFREE = _EndptMEMHEAPFREE_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 91),
    _EndptMEMHEAPFREE_Type()
)
endptMEMHEAPFREE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptMEMHEAPFREE.setStatus("current")
_EndptSSONCONTENT_Type = DisplayString
_EndptSSONCONTENT_Object = MibScalar
endptSSONCONTENT = _EndptSSONCONTENT_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 92),
    _EndptSSONCONTENT_Type()
)
endptSSONCONTENT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptSSONCONTENT.setStatus("current")
_EndptTLSSRVRID_Type = Integer32
_EndptTLSSRVRID_Object = MibScalar
endptTLSSRVRID = _EndptTLSSRVRID_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 93),
    _EndptTLSSRVRID_Type()
)
endptTLSSRVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptTLSSRVRID.setStatus("current")
_EndptTRUSTCERTS_Type = DisplayString
_EndptTRUSTCERTS_Object = MibScalar
endptTRUSTCERTS = _EndptTRUSTCERTS_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 94),
    _EndptTRUSTCERTS_Type()
)
endptTRUSTCERTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptTRUSTCERTS.setStatus("current")
_EndptVOXFILES_Type = DisplayString
_EndptVOXFILES_Object = MibScalar
endptVOXFILES = _EndptVOXFILES_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 95),
    _EndptVOXFILES_Type()
)
endptVOXFILES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptVOXFILES.setStatus("current")
_EndptGRATARP_Type = Integer32
_EndptGRATARP_Object = MibScalar
endptGRATARP = _EndptGRATARP_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 1, 96),
    _EndptGRATARP_Type()
)
endptGRATARP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptGRATARP.setStatus("current")
_EndptNVM_ObjectIdentity = ObjectIdentity
endptNVM = _EndptNVM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 2)
)
_EndptNVAGCHAND_Type = Integer32
_EndptNVAGCHAND_Object = MibScalar
endptNVAGCHAND = _EndptNVAGCHAND_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 2, 1),
    _EndptNVAGCHAND_Type()
)
endptNVAGCHAND.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptNVAGCHAND.setStatus("current")
_EndptNVAGCHEAD_Type = Integer32
_EndptNVAGCHEAD_Object = MibScalar
endptNVAGCHEAD = _EndptNVAGCHEAD_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 2, 2),
    _EndptNVAGCHEAD_Type()
)
endptNVAGCHEAD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptNVAGCHEAD.setStatus("current")
_EndptNVAGCSPKR_Type = Integer32
_EndptNVAGCSPKR_Object = MibScalar
endptNVAGCSPKR = _EndptNVAGCSPKR_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 2, 3),
    _EndptNVAGCSPKR_Type()
)
endptNVAGCSPKR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptNVAGCSPKR.setStatus("current")
_EndptNVALERT_Type = Integer32
_EndptNVALERT_Object = MibScalar
endptNVALERT = _EndptNVALERT_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 2, 4),
    _EndptNVALERT_Type()
)
endptNVALERT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptNVALERT.setStatus("obsolete")
_EndptNVAUTH_Type = Integer32
_EndptNVAUTH_Object = MibScalar
endptNVAUTH = _EndptNVAUTH_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 2, 5),
    _EndptNVAUTH_Type()
)
endptNVAUTH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptNVAUTH.setStatus("current")
_EndptNVBRIGHTNESS_Type = Integer32
_EndptNVBRIGHTNESS_Object = MibScalar
endptNVBRIGHTNESS = _EndptNVBRIGHTNESS_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 2, 6),
    _EndptNVBRIGHTNESS_Type()
)
endptNVBRIGHTNESS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptNVBRIGHTNESS.setStatus("current")
_EndptNVCALLSRVR_Type = IpAddress
_EndptNVCALLSRVR_Object = MibScalar
endptNVCALLSRVR = _EndptNVCALLSRVR_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 2, 7),
    _EndptNVCALLSRVR_Type()
)
endptNVCALLSRVR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptNVCALLSRVR.setStatus("obsolete")
_EndptNVCHADDR_Type = Integer32
_EndptNVCHADDR_Object = MibScalar
endptNVCHADDR = _EndptNVCHADDR_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 2, 8),
    _EndptNVCHADDR_Type()
)
endptNVCHADDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptNVCHADDR.setStatus("current")
_EndptNVCONTRAST_Type = Integer32
_EndptNVCONTRAST_Object = MibScalar
endptNVCONTRAST = _EndptNVCONTRAST_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 2, 9),
    _EndptNVCONTRAST_Type()
)
endptNVCONTRAST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptNVCONTRAST.setStatus("current")
_EndptNVFILESRVR_Type = IpAddress
_EndptNVFILESRVR_Object = MibScalar
endptNVFILESRVR = _EndptNVFILESRVR_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 2, 10),
    _EndptNVFILESRVR_Type()
)
endptNVFILESRVR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptNVFILESRVR.setStatus("obsolete")
_EndptNVGIPADD_Type = IpAddress
_EndptNVGIPADD_Object = MibScalar
endptNVGIPADD = _EndptNVGIPADD_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 2, 11),
    _EndptNVGIPADD_Type()
)
endptNVGIPADD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptNVGIPADD.setStatus("current")
_EndptNVIPADD_Type = IpAddress
_EndptNVIPADD_Object = MibScalar
endptNVIPADD = _EndptNVIPADD_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 2, 12),
    _EndptNVIPADD_Type()
)
endptNVIPADD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptNVIPADD.setStatus("current")
_EndptNVL2Q_Type = Integer32
_EndptNVL2Q_Object = MibScalar
endptNVL2Q = _EndptNVL2Q_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 2, 13),
    _EndptNVL2Q_Type()
)
endptNVL2Q.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptNVL2Q.setStatus("current")
_EndptNVL2QVLAN_Type = Integer32
_EndptNVL2QVLAN_Object = MibScalar
endptNVL2QVLAN = _EndptNVL2QVLAN_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 2, 14),
    _EndptNVL2QVLAN_Type()
)
endptNVL2QVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptNVL2QVLAN.setStatus("current")
_EndptNVLOGSTAT_Type = Integer32
_EndptNVLOGSTAT_Object = MibScalar
endptNVLOGSTAT = _EndptNVLOGSTAT_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 2, 15),
    _EndptNVLOGSTAT_Type()
)
endptNVLOGSTAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptNVLOGSTAT.setStatus("current")
_EndptNVNETMASK_Type = IpAddress
_EndptNVNETMASK_Object = MibScalar
endptNVNETMASK = _EndptNVNETMASK_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 2, 16),
    _EndptNVNETMASK_Type()
)
endptNVNETMASK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptNVNETMASK.setStatus("current")
_EndptNVPHY1STAT_Type = Integer32
_EndptNVPHY1STAT_Object = MibScalar
endptNVPHY1STAT = _EndptNVPHY1STAT_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 2, 17),
    _EndptNVPHY1STAT_Type()
)
endptNVPHY1STAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptNVPHY1STAT.setStatus("current")
_EndptNVPHY2STAT_Type = Integer32
_EndptNVPHY2STAT_Object = MibScalar
endptNVPHY2STAT = _EndptNVPHY2STAT_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 2, 18),
    _EndptNVPHY2STAT_Type()
)
endptNVPHY2STAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptNVPHY2STAT.setStatus("current")
_EndptNVSSON_Type = Integer32
_EndptNVSSON_Object = MibScalar
endptNVSSON = _EndptNVSSON_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 2, 19),
    _EndptNVSSON_Type()
)
endptNVSSON.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptNVSSON.setStatus("current")
_EndptNVVLANTEST_Type = Integer32
_EndptNVVLANTEST_Object = MibScalar
endptNVVLANTEST = _EndptNVVLANTEST_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 2, 20),
    _EndptNVVLANTEST_Type()
)
endptNVVLANTEST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptNVVLANTEST.setStatus("current")
_EndptNVLANGFILE_Type = DisplayString
_EndptNVLANGFILE_Object = MibScalar
endptNVLANGFILE = _EndptNVLANGFILE_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 2, 21),
    _EndptNVLANGFILE_Type()
)
endptNVLANGFILE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptNVLANGFILE.setStatus("current")
_EndptNVTRUSTLIST_Type = DisplayString
_EndptNVTRUSTLIST_Object = MibScalar
endptNVTRUSTLIST = _EndptNVTRUSTLIST_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 2, 22),
    _EndptNVTRUSTLIST_Type()
)
endptNVTRUSTLIST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptNVTRUSTLIST.setStatus("current")
_EndptNVVOXFILE_Type = DisplayString
_EndptNVVOXFILE_Object = MibScalar
endptNVVOXFILE = _EndptNVVOXFILE_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 2, 23),
    _EndptNVVOXFILE_Type()
)
endptNVVOXFILE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptNVVOXFILE.setStatus("current")
_EndptNVRINGTONESTYLE_Type = Integer32
_EndptNVRINGTONESTYLE_Object = MibScalar
endptNVRINGTONESTYLE = _EndptNVRINGTONESTYLE_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 2, 24),
    _EndptNVRINGTONESTYLE_Type()
)
endptNVRINGTONESTYLE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptNVRINGTONESTYLE.setStatus("current")
_EndptNVSBM24BRIGHTNESS1_Type = Integer32
_EndptNVSBM24BRIGHTNESS1_Object = MibScalar
endptNVSBM24BRIGHTNESS1 = _EndptNVSBM24BRIGHTNESS1_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 2, 25),
    _EndptNVSBM24BRIGHTNESS1_Type()
)
endptNVSBM24BRIGHTNESS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptNVSBM24BRIGHTNESS1.setStatus("current")
_EndptNVSBM24BRIGHTNESS2_Type = Integer32
_EndptNVSBM24BRIGHTNESS2_Object = MibScalar
endptNVSBM24BRIGHTNESS2 = _EndptNVSBM24BRIGHTNESS2_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 2, 26),
    _EndptNVSBM24BRIGHTNESS2_Type()
)
endptNVSBM24BRIGHTNESS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptNVSBM24BRIGHTNESS2.setStatus("current")
_EndptNVSBM24BRIGHTNESS3_Type = Integer32
_EndptNVSBM24BRIGHTNESS3_Object = MibScalar
endptNVSBM24BRIGHTNESS3 = _EndptNVSBM24BRIGHTNESS3_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 2, 27),
    _EndptNVSBM24BRIGHTNESS3_Type()
)
endptNVSBM24BRIGHTNESS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptNVSBM24BRIGHTNESS3.setStatus("current")
_EndptMaintenance_ObjectIdentity = ObjectIdentity
endptMaintenance = _EndptMaintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 3)
)
_EndptAPPSTAT_Type = Integer32
_EndptAPPSTAT_Object = MibScalar
endptAPPSTAT = _EndptAPPSTAT_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 3, 1),
    _EndptAPPSTAT_Type()
)
endptAPPSTAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptAPPSTAT.setStatus("current")
_EndptUPGRADESTAT_Type = Integer32
_EndptUPGRADESTAT_Object = MibScalar
endptUPGRADESTAT = _EndptUPGRADESTAT_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 3, 2),
    _EndptUPGRADESTAT_Type()
)
endptUPGRADESTAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptUPGRADESTAT.setStatus("current")
_EndptRecentLog_Object = MibTable
endptRecentLog = _EndptRecentLog_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 3, 3)
)
if mibBuilder.loadTexts:
    endptRecentLog.setStatus("current")
_EndptRecentLogEntry_Object = MibTableRow
endptRecentLogEntry = _EndptRecentLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 3, 3, 1)
)
endptRecentLogEntry.setIndexNames(
    (0, "Avaya-96xxIPTelephone-MIB", "endptRecentLogText"),
)
if mibBuilder.loadTexts:
    endptRecentLogEntry.setStatus("current")
_EndptRecentLogText_Type = DisplayString
_EndptRecentLogText_Object = MibTableColumn
endptRecentLogText = _EndptRecentLogText_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 3, 3, 1, 1),
    _EndptRecentLogText_Type()
)
endptRecentLogText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptRecentLogText.setStatus("current")
_EndptResetLog_Object = MibTable
endptResetLog = _EndptResetLog_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 3, 4)
)
if mibBuilder.loadTexts:
    endptResetLog.setStatus("current")
_EndptResetLogEntry_Object = MibTableRow
endptResetLogEntry = _EndptResetLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 3, 4, 1)
)
endptResetLogEntry.setIndexNames(
    (0, "Avaya-96xxIPTelephone-MIB", "endptResetLogText"),
)
if mibBuilder.loadTexts:
    endptResetLogEntry.setStatus("current")
_EndptResetLogText_Type = DisplayString
_EndptResetLogText_Object = MibTableColumn
endptResetLogText = _EndptResetLogText_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 3, 4, 1, 1),
    _EndptResetLogText_Type()
)
endptResetLogText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptResetLogText.setStatus("current")
_EndptApps_ObjectIdentity = ObjectIdentity
endptApps = _EndptApps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 4)
)
_EndptAUDIOPATH_Type = Integer32
_EndptAUDIOPATH_Object = MibScalar
endptAUDIOPATH = _EndptAUDIOPATH_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 4, 1),
    _EndptAUDIOPATH_Type()
)
endptAUDIOPATH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptAUDIOPATH.setStatus("current")
_EndptENHDIALSTAT_Type = Integer32
_EndptENHDIALSTAT_Object = MibScalar
endptENHDIALSTAT = _EndptENHDIALSTAT_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 4, 2),
    _EndptENHDIALSTAT_Type()
)
endptENHDIALSTAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptENHDIALSTAT.setStatus("current")
_EndptSUBSCRIBELIST_Type = DisplayString
_EndptSUBSCRIBELIST_Object = MibScalar
endptSUBSCRIBELIST = _EndptSUBSCRIBELIST_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 4, 3),
    _EndptSUBSCRIBELIST_Type()
)
endptSUBSCRIBELIST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptSUBSCRIBELIST.setStatus("current")
_EndptTPSLIST_Type = DisplayString
_EndptTPSLIST_Object = MibScalar
endptTPSLIST = _EndptTPSLIST_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 4, 4),
    _EndptTPSLIST_Type()
)
endptTPSLIST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptTPSLIST.setStatus("current")
_EndptWMLEXCEPT_Type = DisplayString
_EndptWMLEXCEPT_Object = MibScalar
endptWMLEXCEPT = _EndptWMLEXCEPT_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 4, 5),
    _EndptWMLEXCEPT_Type()
)
endptWMLEXCEPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptWMLEXCEPT.setStatus("current")
_EndptWMLHOME_Type = DisplayString
_EndptWMLHOME_Object = MibScalar
endptWMLHOME = _EndptWMLHOME_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 4, 6),
    _EndptWMLHOME_Type()
)
endptWMLHOME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptWMLHOME.setStatus("current")
_EndptWMLIDLETIME_Type = Integer32
_EndptWMLIDLETIME_Object = MibScalar
endptWMLIDLETIME = _EndptWMLIDLETIME_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 4, 7),
    _EndptWMLIDLETIME_Type()
)
endptWMLIDLETIME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptWMLIDLETIME.setStatus("current")
_EndptWMLIDLEURI_Type = DisplayString
_EndptWMLIDLEURI_Object = MibScalar
endptWMLIDLEURI = _EndptWMLIDLEURI_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 4, 8),
    _EndptWMLIDLEURI_Type()
)
endptWMLIDLEURI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptWMLIDLEURI.setStatus("current")
_EndptWMLPORT_Type = Integer32
_EndptWMLPORT_Object = MibScalar
endptWMLPORT = _EndptWMLPORT_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 4, 9),
    _EndptWMLPORT_Type()
)
endptWMLPORT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptWMLPORT.setStatus("current")
_EndptWMLPROXY_Type = IpAddress
_EndptWMLPROXY_Object = MibScalar
endptWMLPROXY = _EndptWMLPROXY_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 4, 10),
    _EndptWMLPROXY_Type()
)
endptWMLPROXY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptWMLPROXY.setStatus("current")
_EndptGUESTDURATION_Type = Integer32
_EndptGUESTDURATION_Object = MibScalar
endptGUESTDURATION = _EndptGUESTDURATION_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 4, 11),
    _EndptGUESTDURATION_Type()
)
endptGUESTDURATION.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptGUESTDURATION.setStatus("current")
_EndptGUESTLOGINSTAT_Type = Integer32
_EndptGUESTLOGINSTAT_Object = MibScalar
endptGUESTLOGINSTAT = _EndptGUESTLOGINSTAT_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 4, 12),
    _EndptGUESTLOGINSTAT_Type()
)
endptGUESTLOGINSTAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptGUESTLOGINSTAT.setStatus("current")
_EndptGUESTWARNING_Type = Integer32
_EndptGUESTWARNING_Object = MibScalar
endptGUESTWARNING = _EndptGUESTWARNING_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 4, 13),
    _EndptGUESTWARNING_Type()
)
endptGUESTWARNING.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptGUESTWARNING.setStatus("current")
_EndptPUSHCAP_Type = DisplayString
_EndptPUSHCAP_Object = MibScalar
endptPUSHCAP = _EndptPUSHCAP_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 4, 14),
    _EndptPUSHCAP_Type()
)
endptPUSHCAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptPUSHCAP.setStatus("current")
_EndptPUSHPORT_Type = Integer32
_EndptPUSHPORT_Object = MibScalar
endptPUSHPORT = _EndptPUSHPORT_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 4, 15),
    _EndptPUSHPORT_Type()
)
endptPUSHPORT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptPUSHPORT.setStatus("current")
_EndptQKLOGINSTAT_Type = Integer32
_EndptQKLOGINSTAT_Object = MibScalar
endptQKLOGINSTAT = _EndptQKLOGINSTAT_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 4, 16),
    _EndptQKLOGINSTAT_Type()
)
endptQKLOGINSTAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptQKLOGINSTAT.setStatus("current")
_EndptSCREENSAVER_Type = DisplayString
_EndptSCREENSAVER_Object = MibScalar
endptSCREENSAVER = _EndptSCREENSAVER_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 4, 17),
    _EndptSCREENSAVER_Type()
)
endptSCREENSAVER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptSCREENSAVER.setStatus("current")
_EndptWMLSMALL_Type = DisplayString
_EndptWMLSMALL_Object = MibScalar
endptWMLSMALL = _EndptWMLSMALL_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 4, 18),
    _EndptWMLSMALL_Type()
)
endptWMLSMALL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptWMLSMALL.setStatus("current")
_EndptCLDELCALLBK_Type = Integer32
_EndptCLDELCALLBK_Object = MibScalar
endptCLDELCALLBK = _EndptCLDELCALLBK_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 4, 19),
    _EndptCLDELCALLBK_Type()
)
endptCLDELCALLBK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptCLDELCALLBK.setStatus("current")
_EndptFBONCASCREEN_Type = Integer32
_EndptFBONCASCREEN_Object = MibScalar
endptFBONCASCREEN = _EndptFBONCASCREEN_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 4, 20),
    _EndptFBONCASCREEN_Type()
)
endptFBONCASCREEN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptFBONCASCREEN.setStatus("current")
_EndptLOGBACKUP_Type = Integer32
_EndptLOGBACKUP_Object = MibScalar
endptLOGBACKUP = _EndptLOGBACKUP_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 4, 21),
    _EndptLOGBACKUP_Type()
)
endptLOGBACKUP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptLOGBACKUP.setStatus("current")
_EndptLOGMISSEDONCE_Type = Integer32
_EndptLOGMISSEDONCE_Object = MibScalar
endptLOGMISSEDONCE = _EndptLOGMISSEDONCE_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 4, 22),
    _EndptLOGMISSEDONCE_Type()
)
endptLOGMISSEDONCE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptLOGMISSEDONCE.setStatus("current")
_EndptLOGUNSEEN_Type = Integer32
_EndptLOGUNSEEN_Object = MibScalar
endptLOGUNSEEN = _EndptLOGUNSEEN_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 4, 23),
    _EndptLOGUNSEEN_Type()
)
endptLOGUNSEEN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptLOGUNSEEN.setStatus("current")
_EndptAPPSTATVALUE_Type = Integer32
_EndptAPPSTATVALUE_Object = MibScalar
endptAPPSTATVALUE = _EndptAPPSTATVALUE_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 4, 24),
    _EndptAPPSTATVALUE_Type()
)
endptAPPSTATVALUE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptAPPSTATVALUE.setStatus("current")
_EndptOPSTAT_Type = Integer32
_EndptOPSTAT_Object = MibScalar
endptOPSTAT = _EndptOPSTAT_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 4, 25),
    _EndptOPSTAT_Type()
)
endptOPSTAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptOPSTAT.setStatus("current")
_EndptOPSTAT2_Type = Integer32
_EndptOPSTAT2_Object = MibScalar
endptOPSTAT2 = _EndptOPSTAT2_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 4, 26),
    _EndptOPSTAT2_Type()
)
endptOPSTAT2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptOPSTAT2.setStatus("current")
_EndptAdjuncts_ObjectIdentity = ObjectIdentity
endptAdjuncts = _EndptAdjuncts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 5)
)
_EndptBMODS_Type = Integer32
_EndptBMODS_Object = MibScalar
endptBMODS = _EndptBMODS_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 5, 1),
    _EndptBMODS_Type()
)
endptBMODS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptBMODS.setStatus("current")
_EndptBTADHWVER_Type = DisplayString
_EndptBTADHWVER_Object = MibScalar
endptBTADHWVER = _EndptBTADHWVER_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 5, 2),
    _EndptBTADHWVER_Type()
)
endptBTADHWVER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptBTADHWVER.setStatus("current")
_EndptBTADSTAT_Type = Integer32
_EndptBTADSTAT_Object = MibScalar
endptBTADSTAT = _EndptBTADSTAT_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 5, 3),
    _EndptBTADSTAT_Type()
)
endptBTADSTAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptBTADSTAT.setStatus("current")
_EndptBTADSWVER_Type = DisplayString
_EndptBTADSWVER_Object = MibScalar
endptBTADSWVER = _EndptBTADSWVER_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 5, 4),
    _EndptBTADSWVER_Type()
)
endptBTADSWVER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptBTADSWVER.setStatus("current")
_EndptGIGEHWVER_Type = DisplayString
_EndptGIGEHWVER_Object = MibScalar
endptGIGEHWVER = _EndptGIGEHWVER_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 5, 5),
    _EndptGIGEHWVER_Type()
)
endptGIGEHWVER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptGIGEHWVER.setStatus("current")
_EndptGIGESTAT_Type = Integer32
_EndptGIGESTAT_Object = MibScalar
endptGIGESTAT = _EndptGIGESTAT_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 5, 6),
    _EndptGIGESTAT_Type()
)
endptGIGESTAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptGIGESTAT.setStatus("current")
_EndptGIGESWVER_Type = DisplayString
_EndptGIGESWVER_Object = MibScalar
endptGIGESWVER = _EndptGIGESWVER_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 5, 7),
    _EndptGIGESWVER_Type()
)
endptGIGESWVER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptGIGESWVER.setStatus("current")
_EndptSBM1HWVER_Type = DisplayString
_EndptSBM1HWVER_Object = MibScalar
endptSBM1HWVER = _EndptSBM1HWVER_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 5, 8),
    _EndptSBM1HWVER_Type()
)
endptSBM1HWVER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptSBM1HWVER.setStatus("current")
_EndptSBM1SWVER_Type = DisplayString
_EndptSBM1SWVER_Object = MibScalar
endptSBM1SWVER = _EndptSBM1SWVER_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 5, 9),
    _EndptSBM1SWVER_Type()
)
endptSBM1SWVER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptSBM1SWVER.setStatus("current")
_EndptSBM2HWVER_Type = DisplayString
_EndptSBM2HWVER_Object = MibScalar
endptSBM2HWVER = _EndptSBM2HWVER_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 5, 10),
    _EndptSBM2HWVER_Type()
)
endptSBM2HWVER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptSBM2HWVER.setStatus("current")
_EndptSBM2SWVER_Type = DisplayString
_EndptSBM2SWVER_Object = MibScalar
endptSBM2SWVER = _EndptSBM2SWVER_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 5, 11),
    _EndptSBM2SWVER_Type()
)
endptSBM2SWVER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptSBM2SWVER.setStatus("current")
_EndptSBM3HWVER_Type = DisplayString
_EndptSBM3HWVER_Object = MibScalar
endptSBM3HWVER = _EndptSBM3HWVER_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 5, 12),
    _EndptSBM3HWVER_Type()
)
endptSBM3HWVER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptSBM3HWVER.setStatus("current")
_EndptSBM3SWVER_Type = DisplayString
_EndptSBM3SWVER_Object = MibScalar
endptSBM3SWVER = _EndptSBM3SWVER_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 5, 13),
    _EndptSBM3SWVER_Type()
)
endptSBM3SWVER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptSBM3SWVER.setStatus("current")
_EndptSBMSTAT_Type = Integer32
_EndptSBMSTAT_Object = MibScalar
endptSBMSTAT = _EndptSBMSTAT_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 5, 14),
    _EndptSBMSTAT_Type()
)
endptSBMSTAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptSBMSTAT.setStatus("current")
_EndptUSBPOWER_Type = Integer32
_EndptUSBPOWER_Object = MibScalar
endptUSBPOWER = _EndptUSBPOWER_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 5, 15),
    _EndptUSBPOWER_Type()
)
endptUSBPOWER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptUSBPOWER.setStatus("current")
_EndptH323_ObjectIdentity = ObjectIdentity
endptH323 = _EndptH323_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 6)
)
_EndptMCIPADD_Type = DisplayString
_EndptMCIPADD_Object = MibScalar
endptMCIPADD = _EndptMCIPADD_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 6, 1),
    _EndptMCIPADD_Type()
)
endptMCIPADD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptMCIPADD.setStatus("current")
_EndptGKINUSE_Type = IpAddress
_EndptGKINUSE_Object = MibScalar
endptGKINUSE = _EndptGKINUSE_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 6, 2),
    _EndptGKINUSE_Type()
)
endptGKINUSE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptGKINUSE.setStatus("current")
_EndptNVPHONEXT_Type = DisplayString
_EndptNVPHONEXT_Object = MibScalar
endptNVPHONEXT = _EndptNVPHONEXT_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 6, 3),
    _EndptNVPHONEXT_Type()
)
endptNVPHONEXT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptNVPHONEXT.setStatus("current")
_EndptRASGkList_Object = MibTable
endptRASGkList = _EndptRASGkList_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 6, 4)
)
if mibBuilder.loadTexts:
    endptRASGkList.setStatus("current")
_EndptRASGkEntry_Object = MibTableRow
endptRASGkEntry = _EndptRASGkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 6, 4, 1)
)
endptRASGkEntry.setIndexNames(
    (0, "Avaya-96xxIPTelephone-MIB", "endptRASGkEntryData"),
)
if mibBuilder.loadTexts:
    endptRASGkEntry.setStatus("current")
_EndptRASGkEntryData_Type = DisplayString
_EndptRASGkEntryData_Object = MibTableColumn
endptRASGkEntryData = _EndptRASGkEntryData_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 6, 4, 1, 1),
    _EndptRASGkEntryData_Type()
)
endptRASGkEntryData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptRASGkEntryData.setStatus("current")
_EndptREREGISTER_Type = Integer32
_EndptREREGISTER_Object = MibScalar
endptREREGISTER = _EndptREREGISTER_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 6, 5),
    _EndptREREGISTER_Type()
)
endptREREGISTER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptREREGISTER.setStatus("current")
_EndptSERVICESTAT_Type = Integer32
_EndptSERVICESTAT_Object = MibScalar
endptSERVICESTAT = _EndptSERVICESTAT_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 6, 6),
    _EndptSERVICESTAT_Type()
)
endptSERVICESTAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptSERVICESTAT.setStatus("current")
_EndptGKTCPPORT_Type = Integer32
_EndptGKTCPPORT_Object = MibScalar
endptGKTCPPORT = _EndptGKTCPPORT_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 6, 7),
    _EndptGKTCPPORT_Type()
)
endptGKTCPPORT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptGKTCPPORT.setStatus("current")
_EndptCERT_ObjectIdentity = ObjectIdentity
endptCERT = _EndptCERT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 8)
)
_EndptMYCERTCAID_Type = DisplayString
_EndptMYCERTCAID_Object = MibScalar
endptMYCERTCAID = _EndptMYCERTCAID_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 8, 1),
    _EndptMYCERTCAID_Type()
)
endptMYCERTCAID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptMYCERTCAID.setStatus("current")
_EndptMYCERTCN_Type = DisplayString
_EndptMYCERTCN_Object = MibScalar
endptMYCERTCN = _EndptMYCERTCN_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 8, 2),
    _EndptMYCERTCN_Type()
)
endptMYCERTCN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptMYCERTCN.setStatus("current")
_EndptMYCERTDN_Type = DisplayString
_EndptMYCERTDN_Object = MibScalar
endptMYCERTDN = _EndptMYCERTDN_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 8, 3),
    _EndptMYCERTDN_Type()
)
endptMYCERTDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptMYCERTDN.setStatus("current")
_EndptMYCERTKEYLEN_Type = Integer32
_EndptMYCERTKEYLEN_Object = MibScalar
endptMYCERTKEYLEN = _EndptMYCERTKEYLEN_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 8, 4),
    _EndptMYCERTKEYLEN_Type()
)
endptMYCERTKEYLEN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptMYCERTKEYLEN.setStatus("current")
_EndptMYCERTRENEW_Type = Integer32
_EndptMYCERTRENEW_Object = MibScalar
endptMYCERTRENEW = _EndptMYCERTRENEW_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 8, 5),
    _EndptMYCERTRENEW_Type()
)
endptMYCERTRENEW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptMYCERTRENEW.setStatus("current")
_EndptMYCERTURL_Type = DisplayString
_EndptMYCERTURL_Object = MibScalar
endptMYCERTURL = _EndptMYCERTURL_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 8, 6),
    _EndptMYCERTURL_Type()
)
endptMYCERTURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptMYCERTURL.setStatus("current")
_EndptMYCERTWAIT_Type = Integer32
_EndptMYCERTWAIT_Object = MibScalar
endptMYCERTWAIT = _EndptMYCERTWAIT_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 8, 7),
    _EndptMYCERTWAIT_Type()
)
endptMYCERTWAIT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptMYCERTWAIT.setStatus("current")
_EndptVPN_ObjectIdentity = ObjectIdentity
endptVPN = _EndptVPN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9)
)
_EndptALWCLRNOTIFY_Type = Integer32
_EndptALWCLRNOTIFY_Object = MibScalar
endptALWCLRNOTIFY = _EndptALWCLRNOTIFY_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 1),
    _EndptALWCLRNOTIFY_Type()
)
endptALWCLRNOTIFY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptALWCLRNOTIFY.setStatus("current")
_EndptAUTHTYPE_Type = Integer32
_EndptAUTHTYPE_Object = MibScalar
endptAUTHTYPE = _EndptAUTHTYPE_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 2),
    _EndptAUTHTYPE_Type()
)
endptAUTHTYPE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptAUTHTYPE.setStatus("current")
_EndptCFGPROF_Type = Integer32
_EndptCFGPROF_Object = MibScalar
endptCFGPROF = _EndptCFGPROF_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 3),
    _EndptCFGPROF_Type()
)
endptCFGPROF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptCFGPROF.setStatus("current")
_EndptCOPYTOS_Type = Integer32
_EndptCOPYTOS_Object = MibScalar
endptCOPYTOS = _EndptCOPYTOS_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 4),
    _EndptCOPYTOS_Type()
)
endptCOPYTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptCOPYTOS.setStatus("current")
_EndptDHCPSRVR_Type = DisplayString
_EndptDHCPSRVR_Object = MibScalar
endptDHCPSRVR = _EndptDHCPSRVR_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 5),
    _EndptDHCPSRVR_Type()
)
endptDHCPSRVR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptDHCPSRVR.setStatus("current")
_EndptDROPCLEAR_Type = Integer32
_EndptDROPCLEAR_Object = MibScalar
endptDROPCLEAR = _EndptDROPCLEAR_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 6),
    _EndptDROPCLEAR_Type()
)
endptDROPCLEAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptDROPCLEAR.setStatus("current")
_EndptENCAPS_Type = Integer32
_EndptENCAPS_Object = MibScalar
endptENCAPS = _EndptENCAPS_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 7),
    _EndptENCAPS_Type()
)
endptENCAPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptENCAPS.setStatus("current")
_EndptEXTDNSSRVR_Type = DisplayString
_EndptEXTDNSSRVR_Object = MibScalar
endptEXTDNSSRVR = _EndptEXTDNSSRVR_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 8),
    _EndptEXTDNSSRVR_Type()
)
endptEXTDNSSRVR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptEXTDNSSRVR.setStatus("current")
_EndptEXTGIPADD_Type = DisplayString
_EndptEXTGIPADD_Object = MibScalar
endptEXTGIPADD = _EndptEXTGIPADD_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 9),
    _EndptEXTGIPADD_Type()
)
endptEXTGIPADD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptEXTGIPADD.setStatus("current")
_EndptEXTIPADD_Type = DisplayString
_EndptEXTIPADD_Object = MibScalar
endptEXTIPADD = _EndptEXTIPADD_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 10),
    _EndptEXTIPADD_Type()
)
endptEXTIPADD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptEXTIPADD.setStatus("current")
_EndptEXTNETMASK_Type = DisplayString
_EndptEXTNETMASK_Object = MibScalar
endptEXTNETMASK = _EndptEXTNETMASK_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 11),
    _EndptEXTNETMASK_Type()
)
endptEXTNETMASK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptEXTNETMASK.setStatus("current")
_EndptIKECONFIGMODE_Type = Integer32
_EndptIKECONFIGMODE_Object = MibScalar
endptIKECONFIGMODE = _EndptIKECONFIGMODE_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 12),
    _EndptIKECONFIGMODE_Type()
)
endptIKECONFIGMODE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptIKECONFIGMODE.setStatus("current")
_EndptIKEDH_Type = Integer32
_EndptIKEDH_Object = MibScalar
endptIKEDH = _EndptIKEDH_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 13),
    _EndptIKEDH_Type()
)
endptIKEDH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptIKEDH.setStatus("current")
_EndptIKEDHGRP_Type = Integer32
_EndptIKEDHGRP_Object = MibScalar
endptIKEDHGRP = _EndptIKEDHGRP_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 14),
    _EndptIKEDHGRP_Type()
)
endptIKEDHGRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptIKEDHGRP.setStatus("current")
_EndptIKEID_Type = DisplayString
_EndptIKEID_Object = MibScalar
endptIKEID = _EndptIKEID_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 15),
    _EndptIKEID_Type()
)
endptIKEID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptIKEID.setStatus("current")
_EndptIKEIDTYPE_Type = Integer32
_EndptIKEIDTYPE_Object = MibScalar
endptIKEIDTYPE = _EndptIKEIDTYPE_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 16),
    _EndptIKEIDTYPE_Type()
)
endptIKEIDTYPE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptIKEIDTYPE.setStatus("current")
_EndptIKEOVERTCP_Type = Integer32
_EndptIKEOVERTCP_Object = MibScalar
endptIKEOVERTCP = _EndptIKEOVERTCP_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 17),
    _EndptIKEOVERTCP_Type()
)
endptIKEOVERTCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptIKEOVERTCP.setStatus("current")
_EndptIKEP1AUTH_Type = Integer32
_EndptIKEP1AUTH_Object = MibScalar
endptIKEP1AUTH = _EndptIKEP1AUTH_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 18),
    _EndptIKEP1AUTH_Type()
)
endptIKEP1AUTH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptIKEP1AUTH.setStatus("current")
_EndptIKEP1AUTHALG_Type = Integer32
_EndptIKEP1AUTHALG_Object = MibScalar
endptIKEP1AUTHALG = _EndptIKEP1AUTHALG_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 19),
    _EndptIKEP1AUTHALG_Type()
)
endptIKEP1AUTHALG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptIKEP1AUTHALG.setStatus("current")
_EndptIKEP1ENC_Type = Integer32
_EndptIKEP1ENC_Object = MibScalar
endptIKEP1ENC = _EndptIKEP1ENC_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 20),
    _EndptIKEP1ENC_Type()
)
endptIKEP1ENC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptIKEP1ENC.setStatus("current")
_EndptIKEP1ENCALG_Type = Integer32
_EndptIKEP1ENCALG_Object = MibScalar
endptIKEP1ENCALG = _EndptIKEP1ENCALG_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 21),
    _EndptIKEP1ENCALG_Type()
)
endptIKEP1ENCALG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptIKEP1ENCALG.setStatus("current")
_EndptIKEP1LIFESEC_Type = Integer32
_EndptIKEP1LIFESEC_Object = MibScalar
endptIKEP1LIFESEC = _EndptIKEP1LIFESEC_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 22),
    _EndptIKEP1LIFESEC_Type()
)
endptIKEP1LIFESEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptIKEP1LIFESEC.setStatus("current")
_EndptIKEP2AUTH_Type = Integer32
_EndptIKEP2AUTH_Object = MibScalar
endptIKEP2AUTH = _EndptIKEP2AUTH_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 23),
    _EndptIKEP2AUTH_Type()
)
endptIKEP2AUTH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptIKEP2AUTH.setStatus("current")
_EndptIKEP2AUTHALG_Type = Integer32
_EndptIKEP2AUTHALG_Object = MibScalar
endptIKEP2AUTHALG = _EndptIKEP2AUTHALG_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 24),
    _EndptIKEP2AUTHALG_Type()
)
endptIKEP2AUTHALG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptIKEP2AUTHALG.setStatus("current")
_EndptIKEP2ENC_Type = Integer32
_EndptIKEP2ENC_Object = MibScalar
endptIKEP2ENC = _EndptIKEP2ENC_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 25),
    _EndptIKEP2ENC_Type()
)
endptIKEP2ENC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptIKEP2ENC.setStatus("current")
_EndptIKEP2ENCALG_Type = Integer32
_EndptIKEP2ENCALG_Object = MibScalar
endptIKEP2ENCALG = _EndptIKEP2ENCALG_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 26),
    _EndptIKEP2ENCALG_Type()
)
endptIKEP2ENCALG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptIKEP2ENCALG.setStatus("current")
_EndptIKEP2LIFESEC_Type = Integer32
_EndptIKEP2LIFESEC_Object = MibScalar
endptIKEP2LIFESEC = _EndptIKEP2LIFESEC_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 27),
    _EndptIKEP2LIFESEC_Type()
)
endptIKEP2LIFESEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptIKEP2LIFESEC.setStatus("current")
_EndptIKESALIFEKB_Type = Integer32
_EndptIKESALIFEKB_Object = MibScalar
endptIKESALIFEKB = _EndptIKESALIFEKB_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 28),
    _EndptIKESALIFEKB_Type()
)
endptIKESALIFEKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptIKESALIFEKB.setStatus("current")
_EndptIKESALIFESEC_Type = Integer32
_EndptIKESALIFESEC_Object = MibScalar
endptIKESALIFESEC = _EndptIKESALIFESEC_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 29),
    _EndptIKESALIFESEC_Type()
)
endptIKESALIFESEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptIKESALIFESEC.setStatus("current")
_EndptIKETRANSPORT_Type = Integer32
_EndptIKETRANSPORT_Object = MibScalar
endptIKETRANSPORT = _EndptIKETRANSPORT_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 30),
    _EndptIKETRANSPORT_Type()
)
endptIKETRANSPORT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptIKETRANSPORT.setStatus("current")
_EndptIKEXCHGMODE_Type = Integer32
_EndptIKEXCHGMODE_Object = MibScalar
endptIKEXCHGMODE = _EndptIKEXCHGMODE_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 31),
    _EndptIKEXCHGMODE_Type()
)
endptIKEXCHGMODE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptIKEXCHGMODE.setStatus("current")
_EndptIPSECSALIFEKB_Type = Integer32
_EndptIPSECSALIFEKB_Object = MibScalar
endptIPSECSALIFEKB = _EndptIPSECSALIFEKB_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 32),
    _EndptIPSECSALIFEKB_Type()
)
endptIPSECSALIFEKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptIPSECSALIFEKB.setStatus("current")
_EndptIPSECSALIFESEC_Type = Integer32
_EndptIPSECSALIFESEC_Object = MibScalar
endptIPSECSALIFESEC = _EndptIPSECSALIFESEC_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 33),
    _EndptIPSECSALIFESEC_Type()
)
endptIPSECSALIFESEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptIPSECSALIFESEC.setStatus("current")
_EndptIPSECSUBNET_Type = DisplayString
_EndptIPSECSUBNET_Object = MibScalar
endptIPSECSUBNET = _EndptIPSECSUBNET_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 34),
    _EndptIPSECSUBNET_Type()
)
endptIPSECSUBNET.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptIPSECSUBNET.setStatus("current")
_EndptNORTELAUTH_Type = Integer32
_EndptNORTELAUTH_Object = MibScalar
endptNORTELAUTH = _EndptNORTELAUTH_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 35),
    _EndptNORTELAUTH_Type()
)
endptNORTELAUTH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptNORTELAUTH.setStatus("current")
_EndptPFSDH_Type = Integer32
_EndptPFSDH_Object = MibScalar
endptPFSDH = _EndptPFSDH_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 36),
    _EndptPFSDH_Type()
)
endptPFSDH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptPFSDH.setStatus("current")
_EndptPFSDHGRP_Type = Integer32
_EndptPFSDHGRP_Object = MibScalar
endptPFSDHGRP = _EndptPFSDHGRP_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 37),
    _EndptPFSDHGRP_Type()
)
endptPFSDHGRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptPFSDHGRP.setStatus("current")
_EndptPSWDTYPE_Type = Integer32
_EndptPSWDTYPE_Object = MibScalar
endptPSWDTYPE = _EndptPSWDTYPE_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 38),
    _EndptPSWDTYPE_Type()
)
endptPSWDTYPE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptPSWDTYPE.setStatus("current")
_EndptSGINUSE_Type = DisplayString
_EndptSGINUSE_Object = MibScalar
endptSGINUSE = _EndptSGINUSE_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 39),
    _EndptSGINUSE_Type()
)
endptSGINUSE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptSGINUSE.setStatus("current")
_EndptSGIP_Type = DisplayString
_EndptSGIP_Object = MibScalar
endptSGIP = _EndptSGIP_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 40),
    _EndptSGIP_Type()
)
endptSGIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptSGIP.setStatus("current")
_EndptSGVENDOR_Type = Integer32
_EndptSGVENDOR_Object = MibScalar
endptSGVENDOR = _EndptSGVENDOR_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 41),
    _EndptSGVENDOR_Type()
)
endptSGVENDOR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptSGVENDOR.setStatus("current")
_EndptSGVERSION_Type = DisplayString
_EndptSGVERSION_Object = MibScalar
endptSGVERSION = _EndptSGVERSION_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 42),
    _EndptSGVERSION_Type()
)
endptSGVERSION.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptSGVERSION.setStatus("current")
_EndptVPNMODE_Type = Integer32
_EndptVPNMODE_Object = MibScalar
endptVPNMODE = _EndptVPNMODE_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 43),
    _EndptVPNMODE_Type()
)
endptVPNMODE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptVPNMODE.setStatus("current")
_EndptVPNUSER_Type = DisplayString
_EndptVPNUSER_Object = MibScalar
endptVPNUSER = _EndptVPNUSER_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 44),
    _EndptVPNUSER_Type()
)
endptVPNUSER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptVPNUSER.setStatus("current")
_EndptVPNUSERTYPE_Type = Integer32
_EndptVPNUSERTYPE_Object = MibScalar
endptVPNUSERTYPE = _EndptVPNUSERTYPE_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 45),
    _EndptVPNUSERTYPE_Type()
)
endptVPNUSERTYPE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptVPNUSERTYPE.setStatus("current")
_EndptXAUTH_Type = Integer32
_EndptXAUTH_Object = MibScalar
endptXAUTH = _EndptXAUTH_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 69, 2, 9, 46),
    _EndptXAUTH_Type()
)
endptXAUTH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endptXAUTH.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Avaya-96xxIPTelephone-MIB",
    **{"avaya": avaya,
       "products": products,
       "avayaipEndpointProd": avayaipEndpointProd,
       "avayaMibs": avayaMibs,
       "ipEndpointMIBs": ipEndpointMIBs,
       "avaya96xxMIB": avaya96xxMIB,
       "endptID": endptID,
       "endptAGCHAND": endptAGCHAND,
       "endptAGCHEAD": endptAGCHEAD,
       "endptAGCSPKR": endptAGCSPKR,
       "endptAPPINUSE": endptAPPINUSE,
       "endptAPPNAME": endptAPPNAME,
       "endptBAKLIGHTOFF": endptBAKLIGHTOFF,
       "endptBOOTNAME": endptBOOTNAME,
       "endptBRURI": endptBRURI,
       "endptCNAPORT": endptCNAPORT,
       "endptCNASRVR": endptCNASRVR,
       "endptCODECR": endptCODECR,
       "endptCODECT": endptCODECT,
       "endptDHCPLEASEREBIND": endptDHCPLEASEREBIND,
       "endptDHCPLEASERENEW": endptDHCPLEASERENEW,
       "endptDHCPLEASETIME": endptDHCPLEASETIME,
       "endptDNSSRVR": endptDNSSRVR,
       "endptDOMAIN": endptDOMAIN,
       "endptDOT1X": endptDOT1X,
       "endptDSCPAUD": endptDSCPAUD,
       "endptDSCPBBE": endptDSCPBBE,
       "endptDSCPSIG": endptDSCPSIG,
       "endptDSPVERSION": endptDSPVERSION,
       "endptFEIPADD": endptFEIPADD,
       "endptFEPORT": endptFEPORT,
       "endptGIPADD": endptGIPADD,
       "endptGIPINUSE": endptGIPINUSE,
       "endptGROUP": endptGROUP,
       "endptHTTPDIR": endptHTTPDIR,
       "endptHTTPSRVR": endptHTTPSRVR,
       "endptHTTPUSED": endptHTTPUSED,
       "endptICMPDU": endptICMPDU,
       "endptICMPRED": endptICMPRED,
       "endptIPADD": endptIPADD,
       "endptJMSEC": endptJMSEC,
       "endptL2Q": endptL2Q,
       "endptL2QAUD": endptL2QAUD,
       "endptL2QSIG": endptL2QSIG,
       "endptL2QSTAT": endptL2QSTAT,
       "endptL2QVLAN": endptL2QVLAN,
       "endptL2QVLANINUSE": endptL2QVLANINUSE,
       "endptLOGSRVR": endptLOGSRVR,
       "endptMACADDR": endptMACADDR,
       "endptMODEL": endptMODEL,
       "endptNETMASK": endptNETMASK,
       "endptPHONECC": endptPHONECC,
       "endptPHONESN": endptPHONESN,
       "endptPHY1DUPLEX": endptPHY1DUPLEX,
       "endptPHY1SPEED": endptPHY1SPEED,
       "endptPHY1STAT": endptPHY1STAT,
       "endptPHY2DUPLEX": endptPHY2DUPLEX,
       "endptPHY2PRIO": endptPHY2PRIO,
       "endptPHY2SPEED": endptPHY2SPEED,
       "endptPHY2STAT": endptPHY2STAT,
       "endptPHY2VLAN": endptPHY2VLAN,
       "endptPORTAUD": endptPORTAUD,
       "endptPROCPSWD": endptPROCPSWD,
       "endptPROCSTAT": endptPROCSTAT,
       "endptPWBCC": endptPWBCC,
       "endptPWBSN": endptPWBSN,
       "endptRTCPCONT": endptRTCPCONT,
       "endptRTCPFLOW": endptRTCPFLOW,
       "endptRTCPMON": endptRTCPMON,
       "endptRSVPCONT": endptRSVPCONT,
       "endptRSVPRFRSH": endptRSVPRFRSH,
       "endptRSVPRTRY": endptRSVPRTRY,
       "endptRSVPPROF": endptRSVPPROF,
       "endptSIG": endptSIG,
       "endptSNMPADD": endptSNMPADD,
       "endptSTATIC": endptSTATIC,
       "endptTLSSRVR": endptTLSSRVR,
       "endptTLSUSED": endptTLSUSED,
       "endptTMSEC": endptTMSEC,
       "endptVLANLIST": endptVLANLIST,
       "endptVLANSEP": endptVLANSEP,
       "endptFONT": endptFONT,
       "endptLANGFILES": endptLANGFILES,
       "endptPHNEMERGNUM": endptPHNEMERGNUM,
       "endptAUDIOENV": endptAUDIOENV,
       "endptAUDIOSTHD": endptAUDIOSTHD,
       "endptAUDIOSTHS": endptAUDIOSTHS,
       "endptBRAUTH": endptBRAUTH,
       "endptDHCPINUSE": endptDHCPINUSE,
       "endptDHCPLEASEEXP": endptDHCPLEASEEXP,
       "endptDHCPSTD": endptDHCPSTD,
       "endptDHCPT1REM": endptDHCPT1REM,
       "endptDHCPT2REM": endptDHCPT2REM,
       "endptDOT1XSTAT": endptDOT1XSTAT,
       "endptHTTPPORT": endptHTTPPORT,
       "endptTLSDIR": endptTLSDIR,
       "endptTLSPORT": endptTLSPORT,
       "endptMEMHEAPFREE": endptMEMHEAPFREE,
       "endptSSONCONTENT": endptSSONCONTENT,
       "endptTLSSRVRID": endptTLSSRVRID,
       "endptTRUSTCERTS": endptTRUSTCERTS,
       "endptVOXFILES": endptVOXFILES,
       "endptGRATARP": endptGRATARP,
       "endptNVM": endptNVM,
       "endptNVAGCHAND": endptNVAGCHAND,
       "endptNVAGCHEAD": endptNVAGCHEAD,
       "endptNVAGCSPKR": endptNVAGCSPKR,
       "endptNVALERT": endptNVALERT,
       "endptNVAUTH": endptNVAUTH,
       "endptNVBRIGHTNESS": endptNVBRIGHTNESS,
       "endptNVCALLSRVR": endptNVCALLSRVR,
       "endptNVCHADDR": endptNVCHADDR,
       "endptNVCONTRAST": endptNVCONTRAST,
       "endptNVFILESRVR": endptNVFILESRVR,
       "endptNVGIPADD": endptNVGIPADD,
       "endptNVIPADD": endptNVIPADD,
       "endptNVL2Q": endptNVL2Q,
       "endptNVL2QVLAN": endptNVL2QVLAN,
       "endptNVLOGSTAT": endptNVLOGSTAT,
       "endptNVNETMASK": endptNVNETMASK,
       "endptNVPHY1STAT": endptNVPHY1STAT,
       "endptNVPHY2STAT": endptNVPHY2STAT,
       "endptNVSSON": endptNVSSON,
       "endptNVVLANTEST": endptNVVLANTEST,
       "endptNVLANGFILE": endptNVLANGFILE,
       "endptNVTRUSTLIST": endptNVTRUSTLIST,
       "endptNVVOXFILE": endptNVVOXFILE,
       "endptNVRINGTONESTYLE": endptNVRINGTONESTYLE,
       "endptNVSBM24BRIGHTNESS1": endptNVSBM24BRIGHTNESS1,
       "endptNVSBM24BRIGHTNESS2": endptNVSBM24BRIGHTNESS2,
       "endptNVSBM24BRIGHTNESS3": endptNVSBM24BRIGHTNESS3,
       "endptMaintenance": endptMaintenance,
       "endptAPPSTAT": endptAPPSTAT,
       "endptUPGRADESTAT": endptUPGRADESTAT,
       "endptRecentLog": endptRecentLog,
       "endptRecentLogEntry": endptRecentLogEntry,
       "endptRecentLogText": endptRecentLogText,
       "endptResetLog": endptResetLog,
       "endptResetLogEntry": endptResetLogEntry,
       "endptResetLogText": endptResetLogText,
       "endptApps": endptApps,
       "endptAUDIOPATH": endptAUDIOPATH,
       "endptENHDIALSTAT": endptENHDIALSTAT,
       "endptSUBSCRIBELIST": endptSUBSCRIBELIST,
       "endptTPSLIST": endptTPSLIST,
       "endptWMLEXCEPT": endptWMLEXCEPT,
       "endptWMLHOME": endptWMLHOME,
       "endptWMLIDLETIME": endptWMLIDLETIME,
       "endptWMLIDLEURI": endptWMLIDLEURI,
       "endptWMLPORT": endptWMLPORT,
       "endptWMLPROXY": endptWMLPROXY,
       "endptGUESTDURATION": endptGUESTDURATION,
       "endptGUESTLOGINSTAT": endptGUESTLOGINSTAT,
       "endptGUESTWARNING": endptGUESTWARNING,
       "endptPUSHCAP": endptPUSHCAP,
       "endptPUSHPORT": endptPUSHPORT,
       "endptQKLOGINSTAT": endptQKLOGINSTAT,
       "endptSCREENSAVER": endptSCREENSAVER,
       "endptWMLSMALL": endptWMLSMALL,
       "endptCLDELCALLBK": endptCLDELCALLBK,
       "endptFBONCASCREEN": endptFBONCASCREEN,
       "endptLOGBACKUP": endptLOGBACKUP,
       "endptLOGMISSEDONCE": endptLOGMISSEDONCE,
       "endptLOGUNSEEN": endptLOGUNSEEN,
       "endptAPPSTATVALUE": endptAPPSTATVALUE,
       "endptOPSTAT": endptOPSTAT,
       "endptOPSTAT2": endptOPSTAT2,
       "endptAdjuncts": endptAdjuncts,
       "endptBMODS": endptBMODS,
       "endptBTADHWVER": endptBTADHWVER,
       "endptBTADSTAT": endptBTADSTAT,
       "endptBTADSWVER": endptBTADSWVER,
       "endptGIGEHWVER": endptGIGEHWVER,
       "endptGIGESTAT": endptGIGESTAT,
       "endptGIGESWVER": endptGIGESWVER,
       "endptSBM1HWVER": endptSBM1HWVER,
       "endptSBM1SWVER": endptSBM1SWVER,
       "endptSBM2HWVER": endptSBM2HWVER,
       "endptSBM2SWVER": endptSBM2SWVER,
       "endptSBM3HWVER": endptSBM3HWVER,
       "endptSBM3SWVER": endptSBM3SWVER,
       "endptSBMSTAT": endptSBMSTAT,
       "endptUSBPOWER": endptUSBPOWER,
       "endptH323": endptH323,
       "endptMCIPADD": endptMCIPADD,
       "endptGKINUSE": endptGKINUSE,
       "endptNVPHONEXT": endptNVPHONEXT,
       "endptRASGkList": endptRASGkList,
       "endptRASGkEntry": endptRASGkEntry,
       "endptRASGkEntryData": endptRASGkEntryData,
       "endptREREGISTER": endptREREGISTER,
       "endptSERVICESTAT": endptSERVICESTAT,
       "endptGKTCPPORT": endptGKTCPPORT,
       "endptCERT": endptCERT,
       "endptMYCERTCAID": endptMYCERTCAID,
       "endptMYCERTCN": endptMYCERTCN,
       "endptMYCERTDN": endptMYCERTDN,
       "endptMYCERTKEYLEN": endptMYCERTKEYLEN,
       "endptMYCERTRENEW": endptMYCERTRENEW,
       "endptMYCERTURL": endptMYCERTURL,
       "endptMYCERTWAIT": endptMYCERTWAIT,
       "endptVPN": endptVPN,
       "endptALWCLRNOTIFY": endptALWCLRNOTIFY,
       "endptAUTHTYPE": endptAUTHTYPE,
       "endptCFGPROF": endptCFGPROF,
       "endptCOPYTOS": endptCOPYTOS,
       "endptDHCPSRVR": endptDHCPSRVR,
       "endptDROPCLEAR": endptDROPCLEAR,
       "endptENCAPS": endptENCAPS,
       "endptEXTDNSSRVR": endptEXTDNSSRVR,
       "endptEXTGIPADD": endptEXTGIPADD,
       "endptEXTIPADD": endptEXTIPADD,
       "endptEXTNETMASK": endptEXTNETMASK,
       "endptIKECONFIGMODE": endptIKECONFIGMODE,
       "endptIKEDH": endptIKEDH,
       "endptIKEDHGRP": endptIKEDHGRP,
       "endptIKEID": endptIKEID,
       "endptIKEIDTYPE": endptIKEIDTYPE,
       "endptIKEOVERTCP": endptIKEOVERTCP,
       "endptIKEP1AUTH": endptIKEP1AUTH,
       "endptIKEP1AUTHALG": endptIKEP1AUTHALG,
       "endptIKEP1ENC": endptIKEP1ENC,
       "endptIKEP1ENCALG": endptIKEP1ENCALG,
       "endptIKEP1LIFESEC": endptIKEP1LIFESEC,
       "endptIKEP2AUTH": endptIKEP2AUTH,
       "endptIKEP2AUTHALG": endptIKEP2AUTHALG,
       "endptIKEP2ENC": endptIKEP2ENC,
       "endptIKEP2ENCALG": endptIKEP2ENCALG,
       "endptIKEP2LIFESEC": endptIKEP2LIFESEC,
       "endptIKESALIFEKB": endptIKESALIFEKB,
       "endptIKESALIFESEC": endptIKESALIFESEC,
       "endptIKETRANSPORT": endptIKETRANSPORT,
       "endptIKEXCHGMODE": endptIKEXCHGMODE,
       "endptIPSECSALIFEKB": endptIPSECSALIFEKB,
       "endptIPSECSALIFESEC": endptIPSECSALIFESEC,
       "endptIPSECSUBNET": endptIPSECSUBNET,
       "endptNORTELAUTH": endptNORTELAUTH,
       "endptPFSDH": endptPFSDH,
       "endptPFSDHGRP": endptPFSDHGRP,
       "endptPSWDTYPE": endptPSWDTYPE,
       "endptSGINUSE": endptSGINUSE,
       "endptSGIP": endptSGIP,
       "endptSGVENDOR": endptSGVENDOR,
       "endptSGVERSION": endptSGVERSION,
       "endptVPNMODE": endptVPNMODE,
       "endptVPNUSER": endptVPNUSER,
       "endptVPNUSERTYPE": endptVPNUSERTYPE,
       "endptXAUTH": endptXAUTH}
)
