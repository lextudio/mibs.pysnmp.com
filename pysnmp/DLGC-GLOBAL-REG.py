# SNMP MIB module (DLGC-GLOBAL-REG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLGC-GLOBAL-REG
# Produced by pysmi-1.5.4 at Mon Oct 14 21:29:35 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dialogic_ObjectIdentity = ObjectIdentity
dialogic = _Dialogic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3028)
)
_DlgPlatform_ObjectIdentity = ObjectIdentity
dlgPlatform = _DlgPlatform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3028, 1)
)
_DlgHardwareInfo_ObjectIdentity = ObjectIdentity
dlgHardwareInfo = _DlgHardwareInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1)
)
_DlgPerformanceInfo_ObjectIdentity = ObjectIdentity
dlgPerformanceInfo = _DlgPerformanceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3028, 1, 2)
)
_DlgResources_ObjectIdentity = ObjectIdentity
dlgResources = _DlgResources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3028, 2)
)
_DlgR4Resources_ObjectIdentity = ObjectIdentity
dlgR4Resources = _DlgR4Resources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1)
)
_DlgDM3Resources_ObjectIdentity = ObjectIdentity
dlgDM3Resources = _DlgDM3Resources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3028, 2, 2)
)
_DlgNetworkInterfaces_ObjectIdentity = ObjectIdentity
dlgNetworkInterfaces = _DlgNetworkInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3028, 3)
)
_DlgTransmissions_ObjectIdentity = ObjectIdentity
dlgTransmissions = _DlgTransmissions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3028, 3, 1)
)
_DlgServiceProviders_ObjectIdentity = ObjectIdentity
dlgServiceProviders = _DlgServiceProviders_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3028, 4)
)
_DlgTapi_ObjectIdentity = ObjectIdentity
dlgTapi = _DlgTapi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3028, 4, 1)
)
_DlgApplications_ObjectIdentity = ObjectIdentity
dlgApplications = _DlgApplications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3028, 5)
)
_DlgProducts_ObjectIdentity = ObjectIdentity
dlgProducts = _DlgProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3028, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLGC-GLOBAL-REG",
    **{"dialogic": dialogic,
       "dlgPlatform": dlgPlatform,
       "dlgHardwareInfo": dlgHardwareInfo,
       "dlgPerformanceInfo": dlgPerformanceInfo,
       "dlgResources": dlgResources,
       "dlgR4Resources": dlgR4Resources,
       "dlgDM3Resources": dlgDM3Resources,
       "dlgNetworkInterfaces": dlgNetworkInterfaces,
       "dlgTransmissions": dlgTransmissions,
       "dlgServiceProviders": dlgServiceProviders,
       "dlgTapi": dlgTapi,
       "dlgApplications": dlgApplications,
       "dlgProducts": dlgProducts}
)
