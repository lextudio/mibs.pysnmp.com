# SNMP MIB module (ARISTA-MAU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ARISTA-MAU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:22 2024
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

(aristaMibs,) = mibBuilder.importSymbols(
    "ARISTA-SMI-MIB",
    "aristaMibs")

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

aristaMauMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 2)
)
aristaMauMIB.setRevisions(
        ("2016-06-23 00:00",
         "2015-11-30 00:00",
         "2015-09-01 00:00",
         "2015-07-08 00:00",
         "2015-05-29 00:00",
         "2015-04-01 00:00",
         "2015-03-01 00:00",
         "2014-12-09 00:00",
         "2014-11-21 00:00",
         "2014-11-12 00:00",
         "2014-10-21 00:00",
         "2014-08-15 00:00",
         "2014-06-30 00:00",
         "2014-01-13 00:00",
         "2013-12-10 00:00",
         "2013-10-24 00:00",
         "2013-07-17 00:00",
         "2012-10-12 00:00",
         "2012-07-26 00:00",
         "2012-06-29 00:00",
         "2012-05-14 00:00",
         "2012-04-10 00:00",
         "2011-02-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AristaSnmpDot3MauMgt_ObjectIdentity = ObjectIdentity
aristaSnmpDot3MauMgt = _AristaSnmpDot3MauMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4)
)
_AristaDot3MauType_ObjectIdentity = ObjectIdentity
aristaDot3MauType = _AristaDot3MauType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 1)
)
_AristaDot3MauType10GbaseCR_ObjectIdentity = ObjectIdentity
aristaDot3MauType10GbaseCR = _AristaDot3MauType10GbaseCR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 1)
)
if mibBuilder.loadTexts:
    aristaDot3MauType10GbaseCR.setStatus("current")
_AristaDot3MauType10GbaseDwdmER_ObjectIdentity = ObjectIdentity
aristaDot3MauType10GbaseDwdmER = _AristaDot3MauType10GbaseDwdmER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 2)
)
if mibBuilder.loadTexts:
    aristaDot3MauType10GbaseDwdmER.setStatus("current")
_AristaDot3MauType40GbaseSR4_ObjectIdentity = ObjectIdentity
aristaDot3MauType40GbaseSR4 = _AristaDot3MauType40GbaseSR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 3)
)
if mibBuilder.loadTexts:
    aristaDot3MauType40GbaseSR4.setStatus("deprecated")
_AristaDot3MauType40GbaseLR4_ObjectIdentity = ObjectIdentity
aristaDot3MauType40GbaseLR4 = _AristaDot3MauType40GbaseLR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 4)
)
if mibBuilder.loadTexts:
    aristaDot3MauType40GbaseLR4.setStatus("deprecated")
_AristaDot3MauType40GbaseCR4_ObjectIdentity = ObjectIdentity
aristaDot3MauType40GbaseCR4 = _AristaDot3MauType40GbaseCR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 5)
)
if mibBuilder.loadTexts:
    aristaDot3MauType40GbaseCR4.setStatus("deprecated")
_AristaDot3MauType10GbaseDwdmZR_ObjectIdentity = ObjectIdentity
aristaDot3MauType10GbaseDwdmZR = _AristaDot3MauType10GbaseDwdmZR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 6)
)
if mibBuilder.loadTexts:
    aristaDot3MauType10GbaseDwdmZR.setStatus("current")
_AristaDot3MauType10GbaseCRA_ObjectIdentity = ObjectIdentity
aristaDot3MauType10GbaseCRA = _AristaDot3MauType10GbaseCRA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 7)
)
if mibBuilder.loadTexts:
    aristaDot3MauType10GbaseCRA.setStatus("current")
_AristaDot3MauType10GbaseZR_ObjectIdentity = ObjectIdentity
aristaDot3MauType10GbaseZR = _AristaDot3MauType10GbaseZR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 8)
)
if mibBuilder.loadTexts:
    aristaDot3MauType10GbaseZR.setStatus("current")
_AristaDot3MauType10GbaseLRL_ObjectIdentity = ObjectIdentity
aristaDot3MauType10GbaseLRL = _AristaDot3MauType10GbaseLRL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 9)
)
if mibBuilder.loadTexts:
    aristaDot3MauType10GbaseLRL.setStatus("current")
_AristaDot3MauType100GbaseSR10_ObjectIdentity = ObjectIdentity
aristaDot3MauType100GbaseSR10 = _AristaDot3MauType100GbaseSR10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 10)
)
if mibBuilder.loadTexts:
    aristaDot3MauType100GbaseSR10.setStatus("deprecated")
_AristaDot3MauType100GbaseLR4_ObjectIdentity = ObjectIdentity
aristaDot3MauType100GbaseLR4 = _AristaDot3MauType100GbaseLR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 11)
)
if mibBuilder.loadTexts:
    aristaDot3MauType100GbaseLR4.setStatus("deprecated")
_AristaDot3MauType100GbaseER4_ObjectIdentity = ObjectIdentity
aristaDot3MauType100GbaseER4 = _AristaDot3MauType100GbaseER4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 12)
)
if mibBuilder.loadTexts:
    aristaDot3MauType100GbaseER4.setStatus("deprecated")
_AristaDot3MauType40GbaseXSR4_ObjectIdentity = ObjectIdentity
aristaDot3MauType40GbaseXSR4 = _AristaDot3MauType40GbaseXSR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 13)
)
if mibBuilder.loadTexts:
    aristaDot3MauType40GbaseXSR4.setStatus("current")
_AristaDot3MauType40GbaseAR4_ObjectIdentity = ObjectIdentity
aristaDot3MauType40GbaseAR4 = _AristaDot3MauType40GbaseAR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 14)
)
if mibBuilder.loadTexts:
    aristaDot3MauType40GbaseAR4.setStatus("current")
_AristaDot3MauType40GbasePLR4_ObjectIdentity = ObjectIdentity
aristaDot3MauType40GbasePLR4 = _AristaDot3MauType40GbasePLR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 15)
)
if mibBuilder.loadTexts:
    aristaDot3MauType40GbasePLR4.setStatus("current")
_AristaDot3MauType40GbasePLRL4_ObjectIdentity = ObjectIdentity
aristaDot3MauType40GbasePLRL4 = _AristaDot3MauType40GbasePLRL4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 16)
)
if mibBuilder.loadTexts:
    aristaDot3MauType40GbasePLRL4.setStatus("current")
_AristaDot3MauType40GbasePSM4_ObjectIdentity = ObjectIdentity
aristaDot3MauType40GbasePSM4 = _AristaDot3MauType40GbasePSM4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 17)
)
if mibBuilder.loadTexts:
    aristaDot3MauType40GbasePSM4.setStatus("current")
_AristaDot3MauType40GbaseLRL4_ObjectIdentity = ObjectIdentity
aristaDot3MauType40GbaseLRL4 = _AristaDot3MauType40GbaseLRL4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 18)
)
if mibBuilder.loadTexts:
    aristaDot3MauType40GbaseLRL4.setStatus("current")
_AristaDot3MauType100GbaseSR4_ObjectIdentity = ObjectIdentity
aristaDot3MauType100GbaseSR4 = _AristaDot3MauType100GbaseSR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 19)
)
if mibBuilder.loadTexts:
    aristaDot3MauType100GbaseSR4.setStatus("current")
_AristaDot3MauType40GbaseUniv_ObjectIdentity = ObjectIdentity
aristaDot3MauType40GbaseUniv = _AristaDot3MauType40GbaseUniv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 20)
)
if mibBuilder.loadTexts:
    aristaDot3MauType40GbaseUniv.setStatus("current")
_AristaDot3MauType40GbaseER4_ObjectIdentity = ObjectIdentity
aristaDot3MauType40GbaseER4 = _AristaDot3MauType40GbaseER4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 21)
)
if mibBuilder.loadTexts:
    aristaDot3MauType40GbaseER4.setStatus("current")
_AristaDot3MauType100GbaseXSR10_ObjectIdentity = ObjectIdentity
aristaDot3MauType100GbaseXSR10 = _AristaDot3MauType100GbaseXSR10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 22)
)
if mibBuilder.loadTexts:
    aristaDot3MauType100GbaseXSR10.setStatus("current")
_AristaDot3MauType10GbaseAR_ObjectIdentity = ObjectIdentity
aristaDot3MauType10GbaseAR = _AristaDot3MauType10GbaseAR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 23)
)
if mibBuilder.loadTexts:
    aristaDot3MauType10GbaseAR.setStatus("current")
_AristaDot3MauType100GbaseAR4_ObjectIdentity = ObjectIdentity
aristaDot3MauType100GbaseAR4 = _AristaDot3MauType100GbaseAR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 24)
)
if mibBuilder.loadTexts:
    aristaDot3MauType100GbaseAR4.setStatus("current")
_AristaDot3MauType100GbaseCR4_ObjectIdentity = ObjectIdentity
aristaDot3MauType100GbaseCR4 = _AristaDot3MauType100GbaseCR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 25)
)
if mibBuilder.loadTexts:
    aristaDot3MauType100GbaseCR4.setStatus("current")
_AristaDot3MauType100GbaseLRL4_ObjectIdentity = ObjectIdentity
aristaDot3MauType100GbaseLRL4 = _AristaDot3MauType100GbaseLRL4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 26)
)
if mibBuilder.loadTexts:
    aristaDot3MauType100GbaseLRL4.setStatus("current")
_AristaDot3MauType100GDwdmCoherent_ObjectIdentity = ObjectIdentity
aristaDot3MauType100GDwdmCoherent = _AristaDot3MauType100GDwdmCoherent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 27)
)
if mibBuilder.loadTexts:
    aristaDot3MauType100GDwdmCoherent.setStatus("current")
_AristaDot3MauType10GbaseDwdmZT_ObjectIdentity = ObjectIdentity
aristaDot3MauType10GbaseDwdmZT = _AristaDot3MauType10GbaseDwdmZT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 28)
)
if mibBuilder.loadTexts:
    aristaDot3MauType10GbaseDwdmZT.setStatus("current")
_AristaDot3MauType40GbaseSRBD_ObjectIdentity = ObjectIdentity
aristaDot3MauType40GbaseSRBD = _AristaDot3MauType40GbaseSRBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 29)
)
if mibBuilder.loadTexts:
    aristaDot3MauType40GbaseSRBD.setStatus("current")
_AristaDot3MauType40GbaseSR4D_ObjectIdentity = ObjectIdentity
aristaDot3MauType40GbaseSR4D = _AristaDot3MauType40GbaseSR4D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 30)
)
if mibBuilder.loadTexts:
    aristaDot3MauType40GbaseSR4D.setStatus("current")
_AristaDot3MauType100GbasePSM4_ObjectIdentity = ObjectIdentity
aristaDot3MauType100GbasePSM4 = _AristaDot3MauType100GbasePSM4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 31)
)
if mibBuilder.loadTexts:
    aristaDot3MauType100GbasePSM4.setStatus("current")
_AristaDot3MauType100GbaseCLR4_ObjectIdentity = ObjectIdentity
aristaDot3MauType100GbaseCLR4 = _AristaDot3MauType100GbaseCLR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 32)
)
if mibBuilder.loadTexts:
    aristaDot3MauType100GbaseCLR4.setStatus("current")
_AristaDot3MauType100GDwdmCoherentE_ObjectIdentity = ObjectIdentity
aristaDot3MauType100GDwdmCoherentE = _AristaDot3MauType100GDwdmCoherentE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 33)
)
if mibBuilder.loadTexts:
    aristaDot3MauType100GDwdmCoherentE.setStatus("current")
_AristaDot3MauType100GbaseCWDM4_ObjectIdentity = ObjectIdentity
aristaDot3MauType100GbaseCWDM4 = _AristaDot3MauType100GbaseCWDM4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 35)
)
if mibBuilder.loadTexts:
    aristaDot3MauType100GbaseCWDM4.setStatus("current")
_AristaDot3MauType100GEDwdm2_ObjectIdentity = ObjectIdentity
aristaDot3MauType100GEDwdm2 = _AristaDot3MauType100GEDwdm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 36)
)
if mibBuilder.loadTexts:
    aristaDot3MauType100GEDwdm2.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-MAU-MIB",
    **{"aristaSnmpDot3MauMgt": aristaSnmpDot3MauMgt,
       "aristaDot3MauType": aristaDot3MauType,
       "aristaDot3MauType10GbaseCR": aristaDot3MauType10GbaseCR,
       "aristaDot3MauType10GbaseDwdmER": aristaDot3MauType10GbaseDwdmER,
       "aristaDot3MauType40GbaseSR4": aristaDot3MauType40GbaseSR4,
       "aristaDot3MauType40GbaseLR4": aristaDot3MauType40GbaseLR4,
       "aristaDot3MauType40GbaseCR4": aristaDot3MauType40GbaseCR4,
       "aristaDot3MauType10GbaseDwdmZR": aristaDot3MauType10GbaseDwdmZR,
       "aristaDot3MauType10GbaseCRA": aristaDot3MauType10GbaseCRA,
       "aristaDot3MauType10GbaseZR": aristaDot3MauType10GbaseZR,
       "aristaDot3MauType10GbaseLRL": aristaDot3MauType10GbaseLRL,
       "aristaDot3MauType100GbaseSR10": aristaDot3MauType100GbaseSR10,
       "aristaDot3MauType100GbaseLR4": aristaDot3MauType100GbaseLR4,
       "aristaDot3MauType100GbaseER4": aristaDot3MauType100GbaseER4,
       "aristaDot3MauType40GbaseXSR4": aristaDot3MauType40GbaseXSR4,
       "aristaDot3MauType40GbaseAR4": aristaDot3MauType40GbaseAR4,
       "aristaDot3MauType40GbasePLR4": aristaDot3MauType40GbasePLR4,
       "aristaDot3MauType40GbasePLRL4": aristaDot3MauType40GbasePLRL4,
       "aristaDot3MauType40GbasePSM4": aristaDot3MauType40GbasePSM4,
       "aristaDot3MauType40GbaseLRL4": aristaDot3MauType40GbaseLRL4,
       "aristaDot3MauType100GbaseSR4": aristaDot3MauType100GbaseSR4,
       "aristaDot3MauType40GbaseUniv": aristaDot3MauType40GbaseUniv,
       "aristaDot3MauType40GbaseER4": aristaDot3MauType40GbaseER4,
       "aristaDot3MauType100GbaseXSR10": aristaDot3MauType100GbaseXSR10,
       "aristaDot3MauType10GbaseAR": aristaDot3MauType10GbaseAR,
       "aristaDot3MauType100GbaseAR4": aristaDot3MauType100GbaseAR4,
       "aristaDot3MauType100GbaseCR4": aristaDot3MauType100GbaseCR4,
       "aristaDot3MauType100GbaseLRL4": aristaDot3MauType100GbaseLRL4,
       "aristaDot3MauType100GDwdmCoherent": aristaDot3MauType100GDwdmCoherent,
       "aristaDot3MauType10GbaseDwdmZT": aristaDot3MauType10GbaseDwdmZT,
       "aristaDot3MauType40GbaseSRBD": aristaDot3MauType40GbaseSRBD,
       "aristaDot3MauType40GbaseSR4D": aristaDot3MauType40GbaseSR4D,
       "aristaDot3MauType100GbasePSM4": aristaDot3MauType100GbasePSM4,
       "aristaDot3MauType100GbaseCLR4": aristaDot3MauType100GbaseCLR4,
       "aristaDot3MauType100GDwdmCoherentE": aristaDot3MauType100GDwdmCoherentE,
       "aristaDot3MauType100GbaseCWDM4": aristaDot3MauType100GbaseCWDM4,
       "aristaDot3MauType100GEDwdm2": aristaDot3MauType100GEDwdm2,
       "aristaMauMIB": aristaMauMIB}
)
