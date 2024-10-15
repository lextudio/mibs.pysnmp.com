# SNMP MIB module (DLB-GENERIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLB-GENERIC-MIB
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

(dlbMgmt,) = mibBuilder.importSymbols(
    "DELIBERANT-MIB",
    "dlbMgmt")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysLocation,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysLocation")

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

dlbGenericMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 32761, 3, 1)
)
dlbGenericMIB.setRevisions(
        ("2009-02-13 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DlbGenericMIBObjects_ObjectIdentity = ObjectIdentity
dlbGenericMIBObjects = _DlbGenericMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32761, 3, 1, 1)
)
_DlbGenericNotifs_ObjectIdentity = ObjectIdentity
dlbGenericNotifs = _DlbGenericNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32761, 3, 1, 1, 0)
)
_DlbGenericInfo_ObjectIdentity = ObjectIdentity
dlbGenericInfo = _DlbGenericInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32761, 3, 1, 1, 1)
)

# Managed Objects groups


# Notification objects

dlbPowerLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 32761, 3, 1, 1, 0, 1)
)
dlbPowerLoss.setObjects(
    ("SNMPv2-MIB", "sysLocation")
)
if mibBuilder.loadTexts:
    dlbPowerLoss.setStatus(
        "current"
    )

dlbAdministrativeReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 32761, 3, 1, 1, 0, 2)
)
dlbAdministrativeReboot.setObjects(
    ("SNMPv2-MIB", "sysLocation")
)
if mibBuilder.loadTexts:
    dlbAdministrativeReboot.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLB-GENERIC-MIB",
    **{"dlbGenericMIB": dlbGenericMIB,
       "dlbGenericMIBObjects": dlbGenericMIBObjects,
       "dlbGenericNotifs": dlbGenericNotifs,
       "dlbPowerLoss": dlbPowerLoss,
       "dlbAdministrativeReboot": dlbAdministrativeReboot,
       "dlbGenericInfo": dlbGenericInfo}
)
