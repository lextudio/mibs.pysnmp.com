# SNMP MIB module (CADANT-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-PRODUCTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:21 2024
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

cadant = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998)
)
cadant.setRevisions(
        ("2014-06-25 00:00",
         "2010-04-06 00:00",
         "2007-06-04 00:00",
         "2003-06-30 00:00",
         "2002-12-10 00:00",
         "2002-06-26 00:00",
         "2002-05-07 00:00",
         "2002-02-01 00:00",
         "2000-11-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CadObjects_ObjectIdentity = ObjectIdentity
cadObjects = _CadObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1)
)
_CadCable_ObjectIdentity = ObjectIdentity
cadCable = _CadCable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1)
)
_CadSystem_ObjectIdentity = ObjectIdentity
cadSystem = _CadSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5)
)
_CadNotification_ObjectIdentity = ObjectIdentity
cadNotification = _CadNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 6)
)
_CadEquipment_ObjectIdentity = ObjectIdentity
cadEquipment = _CadEquipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10)
)
_CadSpectrum_ObjectIdentity = ObjectIdentity
cadSpectrum = _CadSpectrum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15)
)
_CadLayer2_ObjectIdentity = ObjectIdentity
cadLayer2 = _CadLayer2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20)
)
_CadLayer3_ObjectIdentity = ObjectIdentity
cadLayer3 = _CadLayer3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25)
)
_CadSubscriber_ObjectIdentity = ObjectIdentity
cadSubscriber = _CadSubscriber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 30)
)
_CadPolicy_ObjectIdentity = ObjectIdentity
cadPolicy = _CadPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 35)
)
_CadAuthentication_ObjectIdentity = ObjectIdentity
cadAuthentication = _CadAuthentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 40)
)
_CadIke_ObjectIdentity = ObjectIdentity
cadIke = _CadIke_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 45)
)
_CadSchema_ObjectIdentity = ObjectIdentity
cadSchema = _CadSchema_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 50)
)
_CadCmRemoteQuery_ObjectIdentity = ObjectIdentity
cadCmRemoteQuery = _CadCmRemoteQuery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 55)
)
_CadExperimental_ObjectIdentity = ObjectIdentity
cadExperimental = _CadExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100)
)
_CadTopology_ObjectIdentity = ObjectIdentity
cadTopology = _CadTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 105)
)
_CadCmtsIf3_ObjectIdentity = ObjectIdentity
cadCmtsIf3 = _CadCmtsIf3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110)
)
_CadL2vpn_ObjectIdentity = ObjectIdentity
cadL2vpn = _CadL2vpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 120)
)
_CadCmtsIpVideo_ObjectIdentity = ObjectIdentity
cadCmtsIpVideo = _CadCmtsIpVideo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 125)
)
_CadMpls_ObjectIdentity = ObjectIdentity
cadMpls = _CadMpls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 130)
)
_CadLicense_ObjectIdentity = ObjectIdentity
cadLicense = _CadLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 135)
)
_CadNms_ObjectIdentity = ObjectIdentity
cadNms = _CadNms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 2)
)
_CadProducts_ObjectIdentity = ObjectIdentity
cadProducts = _CadProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 2)
)
_C4cmts_ObjectIdentity = ObjectIdentity
c4cmts = _C4cmts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 2, 1)
)
_C4ccmts_ObjectIdentity = ObjectIdentity
c4ccmts = _C4ccmts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 2, 2)
)
_G2ims_ObjectIdentity = ObjectIdentity
g2ims = _G2ims_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 2, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-PRODUCTS-MIB",
    **{"cadant": cadant,
       "cadObjects": cadObjects,
       "cadCable": cadCable,
       "cadSystem": cadSystem,
       "cadNotification": cadNotification,
       "cadEquipment": cadEquipment,
       "cadSpectrum": cadSpectrum,
       "cadLayer2": cadLayer2,
       "cadLayer3": cadLayer3,
       "cadSubscriber": cadSubscriber,
       "cadPolicy": cadPolicy,
       "cadAuthentication": cadAuthentication,
       "cadIke": cadIke,
       "cadSchema": cadSchema,
       "cadCmRemoteQuery": cadCmRemoteQuery,
       "cadExperimental": cadExperimental,
       "cadTopology": cadTopology,
       "cadCmtsIf3": cadCmtsIf3,
       "cadL2vpn": cadL2vpn,
       "cadCmtsIpVideo": cadCmtsIpVideo,
       "cadMpls": cadMpls,
       "cadLicense": cadLicense,
       "cadNms": cadNms,
       "cadProducts": cadProducts,
       "c4cmts": c4cmts,
       "c4ccmts": c4ccmts,
       "g2ims": g2ims}
)
