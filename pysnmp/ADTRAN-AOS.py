# SNMP MIB module (ADTRAN-AOS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-AOS
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:03 2024
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

(adIdentityShared,
 adShared) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentityShared",
    "adShared")

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

adGenAOSMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 53)
)
adGenAOSMib.setRevisions(
        ("2014-09-10 00:00",
         "2012-04-27 00:00",
         "2010-07-05 00:00",
         "2004-10-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenAOS_ObjectIdentity = ObjectIdentity
adGenAOS = _AdGenAOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53)
)
_AdGenAOSCommon_ObjectIdentity = ObjectIdentity
adGenAOSCommon = _AdGenAOSCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1)
)
_AdGenAOSRouter_ObjectIdentity = ObjectIdentity
adGenAOSRouter = _AdGenAOSRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 2)
)
_AdGenAOSSecurity_ObjectIdentity = ObjectIdentity
adGenAOSSecurity = _AdGenAOSSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 3)
)
_AdGenAOSSwitch_ObjectIdentity = ObjectIdentity
adGenAOSSwitch = _AdGenAOSSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4)
)
_AdGenAOSVoice_ObjectIdentity = ObjectIdentity
adGenAOSVoice = _AdGenAOSVoice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5)
)
_AdGenAOSWan_ObjectIdentity = ObjectIdentity
adGenAOSWan = _AdGenAOSWan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6)
)
_AdGenAOSPower_ObjectIdentity = ObjectIdentity
adGenAOSPower = _AdGenAOSPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 7)
)
_AdGenAOSApplications_ObjectIdentity = ObjectIdentity
adGenAOSApplications = _AdGenAOSApplications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 8)
)
_AdGenAOSMef_ObjectIdentity = ObjectIdentity
adGenAOSMef = _AdGenAOSMef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9)
)
_AdGenAOSConformance_ObjectIdentity = ObjectIdentity
adGenAOSConformance = _AdGenAOSConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-AOS",
    **{"adGenAOS": adGenAOS,
       "adGenAOSCommon": adGenAOSCommon,
       "adGenAOSRouter": adGenAOSRouter,
       "adGenAOSSecurity": adGenAOSSecurity,
       "adGenAOSSwitch": adGenAOSSwitch,
       "adGenAOSVoice": adGenAOSVoice,
       "adGenAOSWan": adGenAOSWan,
       "adGenAOSPower": adGenAOSPower,
       "adGenAOSApplications": adGenAOSApplications,
       "adGenAOSMef": adGenAOSMef,
       "adGenAOSConformance": adGenAOSConformance,
       "adGenAOSMib": adGenAOSMib}
)
