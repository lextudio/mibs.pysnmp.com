# SNMP MIB module (CALIX-PRODUCT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CALIX-PRODUCT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:24 2024
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

(calixManagement,
 calixModules,
 calixProducts,
 calixRegistrations) = mibBuilder.importSymbols(
    "CALIX-SMI",
    "calixManagement",
    "calixModules",
    "calixProducts",
    "calixRegistrations")

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

calixProduct = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 1, 1)
)
calixProduct.setRevisions(
        ("2009-12-10 00:00",
         "2007-06-28 00:00",
         "2000-08-31 00:26")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_C7_ObjectIdentity = ObjectIdentity
c7 = _C7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1)
)
if mibBuilder.loadTexts:
    c7.setStatus("current")
_C7ShelfAssembly_ObjectIdentity = ObjectIdentity
c7ShelfAssembly = _C7ShelfAssembly_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    c7ShelfAssembly.setStatus("current")
_C7Backplane_ObjectIdentity = ObjectIdentity
c7Backplane = _C7Backplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    c7Backplane.setStatus("current")
_C7Slot_ObjectIdentity = ObjectIdentity
c7Slot = _C7Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    c7Slot.setStatus("current")
_C7Card_ObjectIdentity = ObjectIdentity
c7Card = _C7Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    c7Card.setStatus("current")
_Amp_ObjectIdentity = ObjectIdentity
amp = _Amp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    amp.setStatus("current")
_Mta_ObjectIdentity = ObjectIdentity
mta = _Mta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    mta.setStatus("current")
_RapOc_ObjectIdentity = ObjectIdentity
rapOc = _RapOc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 4, 3)
)
if mibBuilder.loadTexts:
    rapOc.setStatus("current")
_RapDs3_ObjectIdentity = ObjectIdentity
rapDs3 = _RapDs3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 4, 4)
)
if mibBuilder.loadTexts:
    rapDs3.setStatus("current")
_Rpots24_ObjectIdentity = ObjectIdentity
rpots24 = _Rpots24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 4, 5)
)
if mibBuilder.loadTexts:
    rpots24.setStatus("current")
_Adsl24_ObjectIdentity = ObjectIdentity
adsl24 = _Adsl24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 4, 6)
)
if mibBuilder.loadTexts:
    adsl24.setStatus("current")
_Ds1x12_ObjectIdentity = ObjectIdentity
ds1x12 = _Ds1x12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 4, 7)
)
if mibBuilder.loadTexts:
    ds1x12.setStatus("current")
_Ds3x12s_ObjectIdentity = ObjectIdentity
ds3x12s = _Ds3x12s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 4, 8)
)
if mibBuilder.loadTexts:
    ds3x12s.setStatus("current")
_Ds3x12p_ObjectIdentity = ObjectIdentity
ds3x12p = _Ds3x12p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 4, 9)
)
if mibBuilder.loadTexts:
    ds3x12p.setStatus("current")
_Oc3x4ir_ObjectIdentity = ObjectIdentity
oc3x4ir = _Oc3x4ir_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 4, 10)
)
if mibBuilder.loadTexts:
    oc3x4ir.setStatus("current")
_Oc12x4ir_ObjectIdentity = ObjectIdentity
oc12x4ir = _Oc12x4ir_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 4, 11)
)
if mibBuilder.loadTexts:
    oc12x4ir.setStatus("current")
_Oc48x1lr_ObjectIdentity = ObjectIdentity
oc48x1lr = _Oc48x1lr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 4, 12)
)
if mibBuilder.loadTexts:
    oc48x1lr.setStatus("current")
_Fta_ObjectIdentity = ObjectIdentity
fta = _Fta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 4, 13)
)
if mibBuilder.loadTexts:
    fta.setStatus("current")
_Dfta_ObjectIdentity = ObjectIdentity
dfta = _Dfta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 4, 14)
)
if mibBuilder.loadTexts:
    dfta.setStatus("current")
_Mspa_ObjectIdentity = ObjectIdentity
mspa = _Mspa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 4, 15)
)
if mibBuilder.loadTexts:
    mspa.setStatus("current")
_Mspb_ObjectIdentity = ObjectIdentity
mspb = _Mspb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 4, 16)
)
if mibBuilder.loadTexts:
    mspb.setStatus("current")
_C7Port_ObjectIdentity = ObjectIdentity
c7Port = _C7Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 5)
)
if mibBuilder.loadTexts:
    c7Port.setStatus("current")
_Ds0_ObjectIdentity = ObjectIdentity
ds0 = _Ds0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ds0.setStatus("current")
_C7Ds1_ObjectIdentity = ObjectIdentity
c7Ds1 = _C7Ds1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 5, 2)
)
if mibBuilder.loadTexts:
    c7Ds1.setStatus("current")
_C7Ds3_ObjectIdentity = ObjectIdentity
c7Ds3 = _C7Ds3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 5, 3)
)
if mibBuilder.loadTexts:
    c7Ds3.setStatus("current")
_Adsl_ObjectIdentity = ObjectIdentity
adsl = _Adsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 5, 4)
)
if mibBuilder.loadTexts:
    adsl.setStatus("current")
_Oc3_ObjectIdentity = ObjectIdentity
oc3 = _Oc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 5, 5)
)
if mibBuilder.loadTexts:
    oc3.setStatus("current")
_Oc12_ObjectIdentity = ObjectIdentity
oc12 = _Oc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 5, 6)
)
if mibBuilder.loadTexts:
    oc12.setStatus("current")
_Oc48_ObjectIdentity = ObjectIdentity
oc48 = _Oc48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 1, 5, 7)
)
if mibBuilder.loadTexts:
    oc48.setStatus("current")
_E7_ObjectIdentity = ObjectIdentity
e7 = _E7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2)
)
if mibBuilder.loadTexts:
    e7.setStatus("current")
_E7Modules_ObjectIdentity = ObjectIdentity
e7Modules = _E7Modules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    e7Modules.setStatus("current")
_E7Devices_ObjectIdentity = ObjectIdentity
e7Devices = _E7Devices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 5)
)
if mibBuilder.loadTexts:
    e7Devices.setStatus("current")
_E5x312_ObjectIdentity = ObjectIdentity
e5x312 = _E5x312_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 5, 1)
)
if mibBuilder.loadTexts:
    e5x312.setStatus("current")
_E5x400_ObjectIdentity = ObjectIdentity
e5x400 = _E5x400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 5, 2)
)
if mibBuilder.loadTexts:
    e5x400.setStatus("current")
_E7x2_ObjectIdentity = ObjectIdentity
e7x2 = _E7x2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 5, 3)
)
if mibBuilder.loadTexts:
    e7x2.setStatus("current")
_E7x20_ObjectIdentity = ObjectIdentity
e7x20 = _E7x20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 5, 4)
)
if mibBuilder.loadTexts:
    e7x20.setStatus("current")
_E5x100_ObjectIdentity = ObjectIdentity
e5x100 = _E5x100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3)
)
if mibBuilder.loadTexts:
    e5x100.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CALIX-PRODUCT-MIB",
    **{"calixProduct": calixProduct,
       "c7": c7,
       "c7ShelfAssembly": c7ShelfAssembly,
       "c7Backplane": c7Backplane,
       "c7Slot": c7Slot,
       "c7Card": c7Card,
       "amp": amp,
       "mta": mta,
       "rapOc": rapOc,
       "rapDs3": rapDs3,
       "rpots24": rpots24,
       "adsl24": adsl24,
       "ds1x12": ds1x12,
       "ds3x12s": ds3x12s,
       "ds3x12p": ds3x12p,
       "oc3x4ir": oc3x4ir,
       "oc12x4ir": oc12x4ir,
       "oc48x1lr": oc48x1lr,
       "fta": fta,
       "dfta": dfta,
       "mspa": mspa,
       "mspb": mspb,
       "c7Port": c7Port,
       "ds0": ds0,
       "c7Ds1": c7Ds1,
       "c7Ds3": c7Ds3,
       "adsl": adsl,
       "oc3": oc3,
       "oc12": oc12,
       "oc48": oc48,
       "e7": e7,
       "e7Modules": e7Modules,
       "e7Devices": e7Devices,
       "e5x312": e5x312,
       "e5x400": e5x400,
       "e7x2": e7x2,
       "e7x20": e7x20,
       "e5x100": e5x100}
)
