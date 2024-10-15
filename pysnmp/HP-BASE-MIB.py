# SNMP MIB module (HP-BASE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-BASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:55 2024
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

hpicfAccess = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 6)
)
hpicfAccess.setRevisions(
        ("2005-01-31 13:55",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_HpSystem_ObjectIdentity = ObjectIdentity
hpSystem = _HpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3)
)
_NetElement_ObjectIdentity = ObjectIdentity
netElement = _NetElement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7)
)
_HpEtherSwitch_ObjectIdentity = ObjectIdentity
hpEtherSwitch = _HpEtherSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11)
)
_HpSwitchJ4819A_ObjectIdentity = ObjectIdentity
hpSwitchJ4819A = _HpSwitchJ4819A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17)
)
_HpSwitchModuleJ8162A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ8162A = _HpSwitchModuleJ8162A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7)
)
_HpProcurveCommon_ObjectIdentity = ObjectIdentity
hpProcurveCommon = _HpProcurveCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1)
)
_Icf_ObjectIdentity = ObjectIdentity
icf = _Icf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14)
)
_HpicfObjects_ObjectIdentity = ObjectIdentity
hpicfObjects = _HpicfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-BASE-MIB",
    **{"hp": hp,
       "nm": nm,
       "hpSystem": hpSystem,
       "netElement": netElement,
       "hpEtherSwitch": hpEtherSwitch,
       "hpSwitchJ4819A": hpSwitchJ4819A,
       "hpSwitchModuleJ8162A": hpSwitchModuleJ8162A,
       "hpProcurveCommon": hpProcurveCommon,
       "icf": icf,
       "hpicfObjects": hpicfObjects,
       "hpicfAccess": hpicfAccess}
)
