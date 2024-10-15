# SNMP MIB module (CLAB-DEF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CLAB-DEF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:51:58 2024
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

(DocsX509ASN1DEREncodedCertificate,) = mibBuilder.importSymbols(
    "DOCS-IETF-BPI2-MIB",
    "DocsX509ASN1DEREncodedCertificate")

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

cableLabs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491)
)
cableLabs.setRevisions(
        ("2017-04-13 00:00",
         "2016-07-28 00:00",
         "2016-03-16 00:00",
         "2012-08-09 00:00",
         "2011-02-10 00:00",
         "2009-08-11 00:00",
         "2008-03-06 00:00",
         "2007-01-19 17:00",
         "2005-04-08 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DocsL2vpnIfList(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_ClabFunction_ObjectIdentity = ObjectIdentity
clabFunction = _ClabFunction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 1)
)
_ClabFuncMib2_ObjectIdentity = ObjectIdentity
clabFuncMib2 = _ClabFuncMib2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 1, 1)
)
_ClabFuncProprietary_ObjectIdentity = ObjectIdentity
clabFuncProprietary = _ClabFuncProprietary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 1, 2)
)
_ClabProject_ObjectIdentity = ObjectIdentity
clabProject = _ClabProject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2)
)
_ClabProjDocsis_ObjectIdentity = ObjectIdentity
clabProjDocsis = _ClabProjDocsis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1)
)
_ClabProjPacketCable_ObjectIdentity = ObjectIdentity
clabProjPacketCable = _ClabProjPacketCable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2)
)
_PktcSecurity_ObjectIdentity = ObjectIdentity
pktcSecurity = _PktcSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 4)
)
_PktcLawfulIntercept_ObjectIdentity = ObjectIdentity
pktcLawfulIntercept = _PktcLawfulIntercept_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 5)
)
_PktcEnhancements_ObjectIdentity = ObjectIdentity
pktcEnhancements = _PktcEnhancements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6)
)
_PktcPACMMibs_ObjectIdentity = ObjectIdentity
pktcPACMMibs = _PktcPACMMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 7)
)
_PktcPACMTC_ObjectIdentity = ObjectIdentity
pktcPACMTC = _PktcPACMTC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 7, 1)
)
_PktcPACMUEMib_ObjectIdentity = ObjectIdentity
pktcPACMUEMib = _PktcPACMUEMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 7, 2)
)
_PktcPACMUserMib_ObjectIdentity = ObjectIdentity
pktcPACMUserMib = _PktcPACMUserMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 7, 3)
)
_PktcApplicationMibs_ObjectIdentity = ObjectIdentity
pktcApplicationMibs = _PktcApplicationMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8)
)
_PktcSupportMibs_ObjectIdentity = ObjectIdentity
pktcSupportMibs = _PktcSupportMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9)
)
_PktcESSupportMibs_ObjectIdentity = ObjectIdentity
pktcESSupportMibs = _PktcESSupportMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1)
)
_PktcEUEMibs_ObjectIdentity = ObjectIdentity
pktcEUEMibs = _PktcEUEMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10)
)
_PktcEUEDeviceMibs_ObjectIdentity = ObjectIdentity
pktcEUEDeviceMibs = _PktcEUEDeviceMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1)
)
_PktcSMAMibs_ObjectIdentity = ObjectIdentity
pktcSMAMibs = _PktcSMAMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 11)
)
_ClabProjOpenCable_ObjectIdentity = ObjectIdentity
clabProjOpenCable = _ClabProjOpenCable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3)
)
_ClabProjCableHome_ObjectIdentity = ObjectIdentity
clabProjCableHome = _ClabProjCableHome_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4)
)
_ClabProjWireless_ObjectIdentity = ObjectIdentity
clabProjWireless = _ClabProjWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5)
)
_ClabSecurity_ObjectIdentity = ObjectIdentity
clabSecurity = _ClabSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 3)
)
_ClabSecCertObject_ObjectIdentity = ObjectIdentity
clabSecCertObject = _ClabSecCertObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 3, 1)
)
_ClabSrvcPrvdrRootCACert_Type = DocsX509ASN1DEREncodedCertificate
_ClabSrvcPrvdrRootCACert_Object = MibScalar
clabSrvcPrvdrRootCACert = _ClabSrvcPrvdrRootCACert_Object(
    (1, 3, 6, 1, 4, 1, 4491, 3, 1, 1),
    _ClabSrvcPrvdrRootCACert_Type()
)
clabSrvcPrvdrRootCACert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabSrvcPrvdrRootCACert.setStatus("current")
_ClabCVCRootCACert_Type = DocsX509ASN1DEREncodedCertificate
_ClabCVCRootCACert_Object = MibScalar
clabCVCRootCACert = _ClabCVCRootCACert_Object(
    (1, 3, 6, 1, 4, 1, 4491, 3, 1, 2),
    _ClabCVCRootCACert_Type()
)
clabCVCRootCACert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabCVCRootCACert.setStatus("current")
_ClabCVCCACert_Type = DocsX509ASN1DEREncodedCertificate
_ClabCVCCACert_Object = MibScalar
clabCVCCACert = _ClabCVCCACert_Object(
    (1, 3, 6, 1, 4, 1, 4491, 3, 1, 3),
    _ClabCVCCACert_Type()
)
clabCVCCACert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabCVCCACert.setStatus("current")
_ClabMfgCVCCert_Type = DocsX509ASN1DEREncodedCertificate
_ClabMfgCVCCert_Object = MibScalar
clabMfgCVCCert = _ClabMfgCVCCert_Object(
    (1, 3, 6, 1, 4, 1, 4491, 3, 1, 4),
    _ClabMfgCVCCert_Type()
)
clabMfgCVCCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabMfgCVCCert.setStatus("current")
_ClabMfgCACert_Type = DocsX509ASN1DEREncodedCertificate
_ClabMfgCACert_Object = MibScalar
clabMfgCACert = _ClabMfgCACert_Object(
    (1, 3, 6, 1, 4, 1, 4491, 3, 1, 5),
    _ClabMfgCACert_Type()
)
clabMfgCACert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabMfgCACert.setStatus("current")
_ClabSecOlcaObject_ObjectIdentity = ObjectIdentity
clabSecOlcaObject = _ClabSecOlcaObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 3, 2)
)
_ClabCommonMibs_ObjectIdentity = ObjectIdentity
clabCommonMibs = _ClabCommonMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4)
)
_ClabUpsMib_ObjectIdentity = ObjectIdentity
clabUpsMib = _ClabUpsMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 1)
)
_ClabTopoMib_ObjectIdentity = ObjectIdentity
clabTopoMib = _ClabTopoMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 2)
)
_ClabGREMib_ObjectIdentity = ObjectIdentity
clabGREMib = _ClabGREMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 3)
)
_ClabMAPMib_ObjectIdentity = ObjectIdentity
clabMAPMib = _ClabMAPMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 4)
)
_ClabDNSMib_ObjectIdentity = ObjectIdentity
clabDNSMib = _ClabDNSMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 5)
)
_ClabGWMib_ObjectIdentity = ObjectIdentity
clabGWMib = _ClabGWMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 6)
)
_ClabAniDevMib_ObjectIdentity = ObjectIdentity
clabAniDevMib = _ClabAniDevMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 7)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CLAB-DEF-MIB",
    **{"DocsL2vpnIfList": DocsL2vpnIfList,
       "cableLabs": cableLabs,
       "clabFunction": clabFunction,
       "clabFuncMib2": clabFuncMib2,
       "clabFuncProprietary": clabFuncProprietary,
       "clabProject": clabProject,
       "clabProjDocsis": clabProjDocsis,
       "clabProjPacketCable": clabProjPacketCable,
       "pktcSecurity": pktcSecurity,
       "pktcLawfulIntercept": pktcLawfulIntercept,
       "pktcEnhancements": pktcEnhancements,
       "pktcPACMMibs": pktcPACMMibs,
       "pktcPACMTC": pktcPACMTC,
       "pktcPACMUEMib": pktcPACMUEMib,
       "pktcPACMUserMib": pktcPACMUserMib,
       "pktcApplicationMibs": pktcApplicationMibs,
       "pktcSupportMibs": pktcSupportMibs,
       "pktcESSupportMibs": pktcESSupportMibs,
       "pktcEUEMibs": pktcEUEMibs,
       "pktcEUEDeviceMibs": pktcEUEDeviceMibs,
       "pktcSMAMibs": pktcSMAMibs,
       "clabProjOpenCable": clabProjOpenCable,
       "clabProjCableHome": clabProjCableHome,
       "clabProjWireless": clabProjWireless,
       "clabSecurity": clabSecurity,
       "clabSecCertObject": clabSecCertObject,
       "clabSrvcPrvdrRootCACert": clabSrvcPrvdrRootCACert,
       "clabCVCRootCACert": clabCVCRootCACert,
       "clabCVCCACert": clabCVCCACert,
       "clabMfgCVCCert": clabMfgCVCCert,
       "clabMfgCACert": clabMfgCACert,
       "clabSecOlcaObject": clabSecOlcaObject,
       "clabCommonMibs": clabCommonMibs,
       "clabUpsMib": clabUpsMib,
       "clabTopoMib": clabTopoMib,
       "clabGREMib": clabGREMib,
       "clabMAPMib": clabMAPMib,
       "clabDNSMib": clabDNSMib,
       "clabGWMib": clabGWMib,
       "clabAniDevMib": clabAniDevMib}
)
