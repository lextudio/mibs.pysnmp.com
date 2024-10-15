# SNMP MIB module (MIMOSA-NETWORKS-BASE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MIMOSA-NETWORKS-BASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:03 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

mimosa = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43356)
)
mimosa.setRevisions(
        ("2015-06-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MimosaProduct_ObjectIdentity = ObjectIdentity
mimosaProduct = _MimosaProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 1)
)
_MimosaHardware_ObjectIdentity = ObjectIdentity
mimosaHardware = _MimosaHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 1, 1)
)
_MimosaB5_ObjectIdentity = ObjectIdentity
mimosaB5 = _MimosaB5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 1, 1, 1)
)
_MimosaB5Lite_ObjectIdentity = ObjectIdentity
mimosaB5Lite = _MimosaB5Lite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 1, 1, 2)
)
_MimosaA5_ObjectIdentity = ObjectIdentity
mimosaA5 = _MimosaA5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 1, 1, 3)
)
_MimosaC5_ObjectIdentity = ObjectIdentity
mimosaC5 = _MimosaC5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 1, 1, 4)
)
_MimosaSoftware_ObjectIdentity = ObjectIdentity
mimosaSoftware = _MimosaSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 1, 2)
)
_MimosaMgmt_ObjectIdentity = ObjectIdentity
mimosaMgmt = _MimosaMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 2)
)
_MimosaTrap_ObjectIdentity = ObjectIdentity
mimosaTrap = _MimosaTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 2, 0)
)
_MimosaMib_ObjectIdentity = ObjectIdentity
mimosaMib = _MimosaMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1)
)
_MimosaTrapMib_ObjectIdentity = ObjectIdentity
mimosaTrapMib = _MimosaTrapMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 1)
)
_MimosaTrapMessage_Type = OctetString
_MimosaTrapMessage_Object = MibScalar
mimosaTrapMessage = _MimosaTrapMessage_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 1, 1),
    _MimosaTrapMessage_Type()
)
mimosaTrapMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaTrapMessage.setStatus("current")
_MimosaOldSpeed_Type = Integer32
_MimosaOldSpeed_Object = MibScalar
mimosaOldSpeed = _MimosaOldSpeed_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 1, 2),
    _MimosaOldSpeed_Type()
)
mimosaOldSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaOldSpeed.setStatus("current")
_MimosaNewSpeed_Type = Integer32
_MimosaNewSpeed_Object = MibScalar
mimosaNewSpeed = _MimosaNewSpeed_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 1, 3),
    _MimosaNewSpeed_Type()
)
mimosaNewSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaNewSpeed.setStatus("current")
_MimosaWireless_ObjectIdentity = ObjectIdentity
mimosaWireless = _MimosaWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2)
)
_MimosaMIBGroups_ObjectIdentity = ObjectIdentity
mimosaMIBGroups = _MimosaMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 2, 3)
)
_MimosaConformanceGroup_ObjectIdentity = ObjectIdentity
mimosaConformanceGroup = _MimosaConformanceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 2, 4)
)

# Managed Objects groups

mimosaTrapMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43356, 2, 3, 1)
)
mimosaTrapMIBGroup.setObjects(
      *(("MIMOSA-NETWORKS-BASE-MIB", "mimosaTrapMessage"),
        ("MIMOSA-NETWORKS-BASE-MIB", "mimosaOldSpeed"),
        ("MIMOSA-NETWORKS-BASE-MIB", "mimosaNewSpeed"))
)
if mibBuilder.loadTexts:
    mimosaTrapMIBGroup.setStatus("current")


# Notification objects

mimosaCriticalFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 43356, 2, 0, 1)
)
mimosaCriticalFault.setObjects(
    ("MIMOSA-NETWORKS-BASE-MIB", "mimosaTrapMessage")
)
if mibBuilder.loadTexts:
    mimosaCriticalFault.setStatus(
        "current"
    )

mimosaTempWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 43356, 2, 0, 2)
)
mimosaTempWarning.setObjects(
    ("MIMOSA-NETWORKS-BASE-MIB", "mimosaTrapMessage")
)
if mibBuilder.loadTexts:
    mimosaTempWarning.setStatus(
        "current"
    )

mimosaTempNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 43356, 2, 0, 3)
)
mimosaTempNormal.setObjects(
    ("MIMOSA-NETWORKS-BASE-MIB", "mimosaTrapMessage")
)
if mibBuilder.loadTexts:
    mimosaTempNormal.setStatus(
        "current"
    )

mimosaEthernetSpeedChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43356, 2, 0, 4)
)
mimosaEthernetSpeedChange.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("MIMOSA-NETWORKS-BASE-MIB", "mimosaOldSpeed"),
        ("MIMOSA-NETWORKS-BASE-MIB", "mimosaNewSpeed"))
)
if mibBuilder.loadTexts:
    mimosaEthernetSpeedChange.setStatus(
        "current"
    )


# Notifications groups

mimosaGenericNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 43356, 2, 3, 2)
)
mimosaGenericNotificationsGroup.setObjects(
      *(("MIMOSA-NETWORKS-BASE-MIB", "mimosaCriticalFault"),
        ("MIMOSA-NETWORKS-BASE-MIB", "mimosaTempWarning"),
        ("MIMOSA-NETWORKS-BASE-MIB", "mimosaTempNormal"),
        ("MIMOSA-NETWORKS-BASE-MIB", "mimosaEthernetSpeedChange"))
)
if mibBuilder.loadTexts:
    mimosaGenericNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MIMOSA-NETWORKS-BASE-MIB",
    **{"mimosa": mimosa,
       "mimosaProduct": mimosaProduct,
       "mimosaHardware": mimosaHardware,
       "mimosaB5": mimosaB5,
       "mimosaB5Lite": mimosaB5Lite,
       "mimosaA5": mimosaA5,
       "mimosaC5": mimosaC5,
       "mimosaSoftware": mimosaSoftware,
       "mimosaMgmt": mimosaMgmt,
       "mimosaTrap": mimosaTrap,
       "mimosaCriticalFault": mimosaCriticalFault,
       "mimosaTempWarning": mimosaTempWarning,
       "mimosaTempNormal": mimosaTempNormal,
       "mimosaEthernetSpeedChange": mimosaEthernetSpeedChange,
       "mimosaMib": mimosaMib,
       "mimosaTrapMib": mimosaTrapMib,
       "mimosaTrapMessage": mimosaTrapMessage,
       "mimosaOldSpeed": mimosaOldSpeed,
       "mimosaNewSpeed": mimosaNewSpeed,
       "mimosaWireless": mimosaWireless,
       "mimosaMIBGroups": mimosaMIBGroups,
       "mimosaTrapMIBGroup": mimosaTrapMIBGroup,
       "mimosaGenericNotificationsGroup": mimosaGenericNotificationsGroup,
       "mimosaConformanceGroup": mimosaConformanceGroup}
)
