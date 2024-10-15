# SNMP MIB module (HPIPF02TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPIPF02TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:21 2024
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
 NotificationType,
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
    "NotificationType",
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

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_Hpnsa_ObjectIdentity = ObjectIdentity
hpnsa = _Hpnsa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23)
)
_HpIpfE0Events_ObjectIdentity = ObjectIdentity
hpIpfE0Events = _HpIpfE0Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35)
)
_HpIpf02Events_ObjectIdentity = ObjectIdentity
hpIpf02Events = _HpIpf02Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45)
)
_HpIpfEvtDetailStr_Type = DisplayString
_HpIpfEvtDetailStr_Object = MibScalar
hpIpfEvtDetailStr = _HpIpfEvtDetailStr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 1),
    _HpIpfEvtDetailStr_Type()
)
hpIpfEvtDetailStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpIpfEvtDetailStr.setStatus("mandatory")

# Managed Objects groups


# Notification objects

hpTemperature4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 4)
)
hpTemperature4.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpTemperature4.setStatus(
        ""
    )

hpTemperature5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 5)
)
hpTemperature5.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpTemperature5.setStatus(
        ""
    )

hpTemperature6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 6)
)
hpTemperature6.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpTemperature6.setStatus(
        ""
    )

hpEnvironment8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 8)
)
hpEnvironment8.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpEnvironment8.setStatus(
        ""
    )

hpEnvironment9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 9)
)
hpEnvironment9.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpEnvironment9.setStatus(
        ""
    )

hpEnvironment10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 10)
)
hpEnvironment10.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpEnvironment10.setStatus(
        ""
    )

hpEnvironment12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 12)
)
hpEnvironment12.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpEnvironment12.setStatus(
        ""
    )

hpChassis26 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 26)
)
hpChassis26.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpChassis26.setStatus(
        ""
    )

hpSystemHW113 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 113)
)
hpSystemHW113.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpSystemHW113.setStatus(
        ""
    )

hpECCMemory518 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 518)
)
hpECCMemory518.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpECCMemory518.setStatus(
        ""
    )

hpSystemFW699 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 699)
)
hpSystemFW699.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpSystemFW699.setStatus(
        ""
    )

hpSystemFW700 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 700)
)
hpSystemFW700.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpSystemFW700.setStatus(
        ""
    )

hpEnvironment704 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 704)
)
hpEnvironment704.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpEnvironment704.setStatus(
        ""
    )

hpEnvironment705 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 705)
)
hpEnvironment705.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpEnvironment705.setStatus(
        ""
    )

hpEnvironment706 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 706)
)
hpEnvironment706.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpEnvironment706.setStatus(
        ""
    )

hpEnvironment707 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 707)
)
hpEnvironment707.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpEnvironment707.setStatus(
        ""
    )

hpFan710 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 710)
)
hpFan710.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpFan710.setStatus(
        ""
    )

hpRedundantPower720 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 720)
)
hpRedundantPower720.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpRedundantPower720.setStatus(
        ""
    )

hpRedundantPower722 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 722)
)
hpRedundantPower722.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpRedundantPower722.setStatus(
        ""
    )

hpPowerSupply726 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 726)
)
hpPowerSupply726.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpPowerSupply726.setStatus(
        ""
    )

hpEnvironment728 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 728)
)
hpEnvironment728.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpEnvironment728.setStatus(
        ""
    )

hpSystemHW729 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 729)
)
hpSystemHW729.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpSystemHW729.setStatus(
        ""
    )

hpBmcFirmware730 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 730)
)
hpBmcFirmware730.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpBmcFirmware730.setStatus(
        ""
    )

hpPowerSupply731 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 731)
)
hpPowerSupply731.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpPowerSupply731.setStatus(
        ""
    )

hpRedundantPower732 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 732)
)
hpRedundantPower732.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpRedundantPower732.setStatus(
        ""
    )

hpSystemHW733 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 733)
)
hpSystemHW733.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpSystemHW733.setStatus(
        ""
    )

hpSystemHW734 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 734)
)
hpSystemHW734.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpSystemHW734.setStatus(
        ""
    )

hpSystemHW735 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 735)
)
hpSystemHW735.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpSystemHW735.setStatus(
        ""
    )

hpSystemHW736 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 736)
)
hpSystemHW736.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpSystemHW736.setStatus(
        ""
    )

hpSystemHW737 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 737)
)
hpSystemHW737.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpSystemHW737.setStatus(
        ""
    )

hpSystemHW738 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 738)
)
hpSystemHW738.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpSystemHW738.setStatus(
        ""
    )

hpSystemHW739 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 739)
)
hpSystemHW739.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpSystemHW739.setStatus(
        ""
    )

hpSystemHW740 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 740)
)
hpSystemHW740.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpSystemHW740.setStatus(
        ""
    )

hpSystemHW744 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 744)
)
hpSystemHW744.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpSystemHW744.setStatus(
        ""
    )

hpSystemHW745 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 745)
)
hpSystemHW745.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpSystemHW745.setStatus(
        ""
    )

hpSystemHW746 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 746)
)
hpSystemHW746.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpSystemHW746.setStatus(
        ""
    )

hpSystemHW747 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 747)
)
hpSystemHW747.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpSystemHW747.setStatus(
        ""
    )

hpSystemHW748 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 748)
)
hpSystemHW748.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpSystemHW748.setStatus(
        ""
    )

hpSystemHW749 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 749)
)
hpSystemHW749.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpSystemHW749.setStatus(
        ""
    )

hpSystemHW751 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 751)
)
hpSystemHW751.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpSystemHW751.setStatus(
        ""
    )

hpTempHighWarning752 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 752)
)
hpTempHighWarning752.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpTempHighWarning752.setStatus(
        ""
    )

hpTempHighCritical753 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 753)
)
hpTempHighCritical753.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpTempHighCritical753.setStatus(
        ""
    )

hpTempHighNonRecoverable754 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 754)
)
hpTempHighNonRecoverable754.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpTempHighNonRecoverable754.setStatus(
        ""
    )

hpTemperature755 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 755)
)
hpTemperature755.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpTemperature755.setStatus(
        ""
    )

hpTemperature756 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 756)
)
hpTemperature756.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpTemperature756.setStatus(
        ""
    )

hpRedundantPower757 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 757)
)
hpRedundantPower757.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpRedundantPower757.setStatus(
        ""
    )

hpRedundantPower758 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45, 0, 758)
)
hpRedundantPower758.setObjects(
    ("HPIPF02TRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpRedundantPower758.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPIPF02TRAP-MIB",
    **{"hp": hp,
       "nm": nm,
       "hpnsa": hpnsa,
       "hpIpfE0Events": hpIpfE0Events,
       "hpIpf02Events": hpIpf02Events,
       "hpTemperature4": hpTemperature4,
       "hpTemperature5": hpTemperature5,
       "hpTemperature6": hpTemperature6,
       "hpEnvironment8": hpEnvironment8,
       "hpEnvironment9": hpEnvironment9,
       "hpEnvironment10": hpEnvironment10,
       "hpEnvironment12": hpEnvironment12,
       "hpChassis26": hpChassis26,
       "hpSystemHW113": hpSystemHW113,
       "hpECCMemory518": hpECCMemory518,
       "hpSystemFW699": hpSystemFW699,
       "hpSystemFW700": hpSystemFW700,
       "hpEnvironment704": hpEnvironment704,
       "hpEnvironment705": hpEnvironment705,
       "hpEnvironment706": hpEnvironment706,
       "hpEnvironment707": hpEnvironment707,
       "hpFan710": hpFan710,
       "hpRedundantPower720": hpRedundantPower720,
       "hpRedundantPower722": hpRedundantPower722,
       "hpPowerSupply726": hpPowerSupply726,
       "hpEnvironment728": hpEnvironment728,
       "hpSystemHW729": hpSystemHW729,
       "hpBmcFirmware730": hpBmcFirmware730,
       "hpPowerSupply731": hpPowerSupply731,
       "hpRedundantPower732": hpRedundantPower732,
       "hpSystemHW733": hpSystemHW733,
       "hpSystemHW734": hpSystemHW734,
       "hpSystemHW735": hpSystemHW735,
       "hpSystemHW736": hpSystemHW736,
       "hpSystemHW737": hpSystemHW737,
       "hpSystemHW738": hpSystemHW738,
       "hpSystemHW739": hpSystemHW739,
       "hpSystemHW740": hpSystemHW740,
       "hpSystemHW744": hpSystemHW744,
       "hpSystemHW745": hpSystemHW745,
       "hpSystemHW746": hpSystemHW746,
       "hpSystemHW747": hpSystemHW747,
       "hpSystemHW748": hpSystemHW748,
       "hpSystemHW749": hpSystemHW749,
       "hpSystemHW751": hpSystemHW751,
       "hpTempHighWarning752": hpTempHighWarning752,
       "hpTempHighCritical753": hpTempHighCritical753,
       "hpTempHighNonRecoverable754": hpTempHighNonRecoverable754,
       "hpTemperature755": hpTemperature755,
       "hpTemperature756": hpTemperature756,
       "hpRedundantPower757": hpRedundantPower757,
       "hpRedundantPower758": hpRedundantPower758,
       "hpIpfEvtDetailStr": hpIpfEvtDetailStr}
)
