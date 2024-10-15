# SNMP MIB module (CERENT-GLOBAL-REGISTRY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CERENT-GLOBAL-REGISTRY
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:21 2024
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

cerentGlobalRegModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 10, 10)
)
cerentGlobalRegModule.setRevisions(
        ("1904-10-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cerent_ObjectIdentity = ObjectIdentity
cerent = _Cerent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607)
)
if mibBuilder.loadTexts:
    cerent.setStatus("current")
_CerentRegistry_ObjectIdentity = ObjectIdentity
cerentRegistry = _CerentRegistry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1)
)
if mibBuilder.loadTexts:
    cerentRegistry.setStatus("current")
_CerentModules_ObjectIdentity = ObjectIdentity
cerentModules = _CerentModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 10)
)
if mibBuilder.loadTexts:
    cerentModules.setStatus("current")
_CerentCommunicationEquipment_ObjectIdentity = ObjectIdentity
cerentCommunicationEquipment = _CerentCommunicationEquipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 20)
)
if mibBuilder.loadTexts:
    cerentCommunicationEquipment.setStatus("current")
_CerentADMs_ObjectIdentity = ObjectIdentity
cerentADMs = _CerentADMs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 20, 10)
)
if mibBuilder.loadTexts:
    cerentADMs.setStatus("current")
_Cerent454Node_ObjectIdentity = ObjectIdentity
cerent454Node = _Cerent454Node_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 20, 10, 10)
)
if mibBuilder.loadTexts:
    cerent454Node.setStatus("current")
_Cerent327Node_ObjectIdentity = ObjectIdentity
cerent327Node = _Cerent327Node_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 20, 10, 20)
)
if mibBuilder.loadTexts:
    cerent327Node.setStatus("current")
_Cerent600Node_ObjectIdentity = ObjectIdentity
cerent600Node = _Cerent600Node_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 20, 10, 30)
)
if mibBuilder.loadTexts:
    cerent600Node.setStatus("current")
_Cerent310Node_ObjectIdentity = ObjectIdentity
cerent310Node = _Cerent310Node_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 20, 10, 40)
)
if mibBuilder.loadTexts:
    cerent310Node.setStatus("current")
_Cerent310MaAnsiNode_ObjectIdentity = ObjectIdentity
cerent310MaAnsiNode = _Cerent310MaAnsiNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 20, 10, 50)
)
if mibBuilder.loadTexts:
    cerent310MaAnsiNode.setStatus("current")
_Cerent310MaEtsiNode_ObjectIdentity = ObjectIdentity
cerent310MaEtsiNode = _Cerent310MaEtsiNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 20, 10, 60)
)
if mibBuilder.loadTexts:
    cerent310MaEtsiNode.setStatus("current")
_Cerent454M6Node_ObjectIdentity = ObjectIdentity
cerent454M6Node = _Cerent454M6Node_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 20, 10, 70)
)
if mibBuilder.loadTexts:
    cerent454M6Node.setStatus("current")
_Cerent454M2Node_ObjectIdentity = ObjectIdentity
cerent454M2Node = _Cerent454M2Node_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 20, 10, 80)
)
if mibBuilder.loadTexts:
    cerent454M2Node.setStatus("current")
_CerentDwdmDevices_ObjectIdentity = ObjectIdentity
cerentDwdmDevices = _CerentDwdmDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 20, 20)
)
if mibBuilder.loadTexts:
    cerentDwdmDevices.setStatus("current")
_Cerent15216OpmNode_ObjectIdentity = ObjectIdentity
cerent15216OpmNode = _Cerent15216OpmNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 20, 20, 10)
)
if mibBuilder.loadTexts:
    cerent15216OpmNode.setStatus("current")
_Cerent15216EdfaNode_ObjectIdentity = ObjectIdentity
cerent15216EdfaNode = _Cerent15216EdfaNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 20, 20, 20)
)
if mibBuilder.loadTexts:
    cerent15216EdfaNode.setStatus("current")
_CerentComponents_ObjectIdentity = ObjectIdentity
cerentComponents = _CerentComponents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30)
)
if mibBuilder.loadTexts:
    cerentComponents.setStatus("current")
_CerentOtherComponent_ObjectIdentity = ObjectIdentity
cerentOtherComponent = _CerentOtherComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1)
)
if mibBuilder.loadTexts:
    cerentOtherComponent.setStatus("current")
_CerentTcc_ObjectIdentity = ObjectIdentity
cerentTcc = _CerentTcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 10)
)
if mibBuilder.loadTexts:
    cerentTcc.setStatus("current")
_CerentXc_ObjectIdentity = ObjectIdentity
cerentXc = _CerentXc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 20)
)
if mibBuilder.loadTexts:
    cerentXc.setStatus("current")
_CerentDs114_ObjectIdentity = ObjectIdentity
cerentDs114 = _CerentDs114_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 30)
)
if mibBuilder.loadTexts:
    cerentDs114.setStatus("current")
_CerentDs1n14_ObjectIdentity = ObjectIdentity
cerentDs1n14 = _CerentDs1n14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 40)
)
if mibBuilder.loadTexts:
    cerentDs1n14.setStatus("current")
_CerentDs312_ObjectIdentity = ObjectIdentity
cerentDs312 = _CerentDs312_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 50)
)
if mibBuilder.loadTexts:
    cerentDs312.setStatus("current")
_CerentOc3ir_ObjectIdentity = ObjectIdentity
cerentOc3ir = _CerentOc3ir_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 60)
)
if mibBuilder.loadTexts:
    cerentOc3ir.setStatus("current")
_CerentOc12ir_ObjectIdentity = ObjectIdentity
cerentOc12ir = _CerentOc12ir_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 70)
)
if mibBuilder.loadTexts:
    cerentOc12ir.setStatus("current")
_CerentOc12lr1310_ObjectIdentity = ObjectIdentity
cerentOc12lr1310 = _CerentOc12lr1310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 80)
)
if mibBuilder.loadTexts:
    cerentOc12lr1310.setStatus("current")
_CerentOc48ir_ObjectIdentity = ObjectIdentity
cerentOc48ir = _CerentOc48ir_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 90)
)
if mibBuilder.loadTexts:
    cerentOc48ir.setStatus("current")
_CerentOc48lr_ObjectIdentity = ObjectIdentity
cerentOc48lr = _CerentOc48lr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 100)
)
if mibBuilder.loadTexts:
    cerentOc48lr.setStatus("current")
_CerentFanTray_ObjectIdentity = ObjectIdentity
cerentFanTray = _CerentFanTray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 110)
)
if mibBuilder.loadTexts:
    cerentFanTray.setStatus("current")
_CerentFanSlot_ObjectIdentity = ObjectIdentity
cerentFanSlot = _CerentFanSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 120)
)
if mibBuilder.loadTexts:
    cerentFanSlot.setStatus("current")
_CerentIoSlot_ObjectIdentity = ObjectIdentity
cerentIoSlot = _CerentIoSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 130)
)
if mibBuilder.loadTexts:
    cerentIoSlot.setStatus("current")
_CerentXcSlot_ObjectIdentity = ObjectIdentity
cerentXcSlot = _CerentXcSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 140)
)
if mibBuilder.loadTexts:
    cerentXcSlot.setStatus("current")
_CerentAicSlot_ObjectIdentity = ObjectIdentity
cerentAicSlot = _CerentAicSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 150)
)
if mibBuilder.loadTexts:
    cerentAicSlot.setStatus("current")
_CerentTccSlot_ObjectIdentity = ObjectIdentity
cerentTccSlot = _CerentTccSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 160)
)
if mibBuilder.loadTexts:
    cerentTccSlot.setStatus("current")
_CerentBackPlane454_ObjectIdentity = ObjectIdentity
cerentBackPlane454 = _CerentBackPlane454_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 170)
)
if mibBuilder.loadTexts:
    cerentBackPlane454.setStatus("current")
_CerentChassis454_ObjectIdentity = ObjectIdentity
cerentChassis454 = _CerentChassis454_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 180)
)
if mibBuilder.loadTexts:
    cerentChassis454.setStatus("current")
_CerentDs3nCard_ObjectIdentity = ObjectIdentity
cerentDs3nCard = _CerentDs3nCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 190)
)
if mibBuilder.loadTexts:
    cerentDs3nCard.setStatus("current")
_CerentDs3XmCard_ObjectIdentity = ObjectIdentity
cerentDs3XmCard = _CerentDs3XmCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 200)
)
if mibBuilder.loadTexts:
    cerentDs3XmCard.setStatus("current")
_CerentOc3Card_ObjectIdentity = ObjectIdentity
cerentOc3Card = _CerentOc3Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 210)
)
if mibBuilder.loadTexts:
    cerentOc3Card.setStatus("current")
_CerentOc3OctaCard_ObjectIdentity = ObjectIdentity
cerentOc3OctaCard = _CerentOc3OctaCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 212)
)
if mibBuilder.loadTexts:
    cerentOc3OctaCard.setStatus("current")
_CerentOc12Card_ObjectIdentity = ObjectIdentity
cerentOc12Card = _CerentOc12Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 220)
)
if mibBuilder.loadTexts:
    cerentOc12Card.setStatus("current")
_CerentOc48Card_ObjectIdentity = ObjectIdentity
cerentOc48Card = _CerentOc48Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 230)
)
if mibBuilder.loadTexts:
    cerentOc48Card.setStatus("current")
_CerentEc1Card_ObjectIdentity = ObjectIdentity
cerentEc1Card = _CerentEc1Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 240)
)
if mibBuilder.loadTexts:
    cerentEc1Card.setStatus("current")
_CerentEc1nCard_ObjectIdentity = ObjectIdentity
cerentEc1nCard = _CerentEc1nCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 250)
)
if mibBuilder.loadTexts:
    cerentEc1nCard.setStatus("current")
_CerentEpos100Card_ObjectIdentity = ObjectIdentity
cerentEpos100Card = _CerentEpos100Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 260)
)
if mibBuilder.loadTexts:
    cerentEpos100Card.setStatus("current")
_CerentEpos1000Card_ObjectIdentity = ObjectIdentity
cerentEpos1000Card = _CerentEpos1000Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 270)
)
if mibBuilder.loadTexts:
    cerentEpos1000Card.setStatus("current")
_CerentAicCard_ObjectIdentity = ObjectIdentity
cerentAicCard = _CerentAicCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 280)
)
if mibBuilder.loadTexts:
    cerentAicCard.setStatus("current")
_CerentXcVtCard_ObjectIdentity = ObjectIdentity
cerentXcVtCard = _CerentXcVtCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 290)
)
if mibBuilder.loadTexts:
    cerentXcVtCard.setStatus("current")
_CerentEther1000Port_ObjectIdentity = ObjectIdentity
cerentEther1000Port = _CerentEther1000Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 300)
)
if mibBuilder.loadTexts:
    cerentEther1000Port.setStatus("current")
_CerentEther100Port_ObjectIdentity = ObjectIdentity
cerentEther100Port = _CerentEther100Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 310)
)
if mibBuilder.loadTexts:
    cerentEther100Port.setStatus("current")
_CerentDs1VtMappedPort_ObjectIdentity = ObjectIdentity
cerentDs1VtMappedPort = _CerentDs1VtMappedPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 320)
)
if mibBuilder.loadTexts:
    cerentDs1VtMappedPort.setStatus("current")
_CerentDs3XmPort_ObjectIdentity = ObjectIdentity
cerentDs3XmPort = _CerentDs3XmPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 330)
)
if mibBuilder.loadTexts:
    cerentDs3XmPort.setStatus("current")
_CerentDs3Port_ObjectIdentity = ObjectIdentity
cerentDs3Port = _CerentDs3Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 340)
)
if mibBuilder.loadTexts:
    cerentDs3Port.setStatus("current")
_CerentEc1Port_ObjectIdentity = ObjectIdentity
cerentEc1Port = _CerentEc1Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 350)
)
if mibBuilder.loadTexts:
    cerentEc1Port.setStatus("current")
_CerentOc3Port_ObjectIdentity = ObjectIdentity
cerentOc3Port = _CerentOc3Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 360)
)
if mibBuilder.loadTexts:
    cerentOc3Port.setStatus("current")
_CerentOc12Port_ObjectIdentity = ObjectIdentity
cerentOc12Port = _CerentOc12Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 370)
)
if mibBuilder.loadTexts:
    cerentOc12Port.setStatus("current")
_CerentOc48Port_ObjectIdentity = ObjectIdentity
cerentOc48Port = _CerentOc48Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 380)
)
if mibBuilder.loadTexts:
    cerentOc48Port.setStatus("current")
_CerentOrderwirePort_ObjectIdentity = ObjectIdentity
cerentOrderwirePort = _CerentOrderwirePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 390)
)
if mibBuilder.loadTexts:
    cerentOrderwirePort.setStatus("current")
_CerentSensorComponent_ObjectIdentity = ObjectIdentity
cerentSensorComponent = _CerentSensorComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 400)
)
if mibBuilder.loadTexts:
    cerentSensorComponent.setStatus("current")
_CerentChassis15327_ObjectIdentity = ObjectIdentity
cerentChassis15327 = _CerentChassis15327_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 410)
)
if mibBuilder.loadTexts:
    cerentChassis15327.setStatus("current")
_CerentBackPlane15327_ObjectIdentity = ObjectIdentity
cerentBackPlane15327 = _CerentBackPlane15327_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 420)
)
if mibBuilder.loadTexts:
    cerentBackPlane15327.setStatus("current")
_CerentXtcCard_ObjectIdentity = ObjectIdentity
cerentXtcCard = _CerentXtcCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 430)
)
if mibBuilder.loadTexts:
    cerentXtcCard.setStatus("current")
_CerentMicCard_ObjectIdentity = ObjectIdentity
cerentMicCard = _CerentMicCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 440)
)
if mibBuilder.loadTexts:
    cerentMicCard.setStatus("current")
_CerentMicExtCard_ObjectIdentity = ObjectIdentity
cerentMicExtCard = _CerentMicExtCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 450)
)
if mibBuilder.loadTexts:
    cerentMicExtCard.setStatus("current")
_CerentXtcSlot_ObjectIdentity = ObjectIdentity
cerentXtcSlot = _CerentXtcSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 460)
)
if mibBuilder.loadTexts:
    cerentXtcSlot.setStatus("current")
_CerentMicSlot_ObjectIdentity = ObjectIdentity
cerentMicSlot = _CerentMicSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 470)
)
if mibBuilder.loadTexts:
    cerentMicSlot.setStatus("current")
_CerentVicEncoderLineCard_ObjectIdentity = ObjectIdentity
cerentVicEncoderLineCard = _CerentVicEncoderLineCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 480)
)
if mibBuilder.loadTexts:
    cerentVicEncoderLineCard.setStatus("current")
_CerentVicDecoderLineCard_ObjectIdentity = ObjectIdentity
cerentVicDecoderLineCard = _CerentVicDecoderLineCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 490)
)
if mibBuilder.loadTexts:
    cerentVicDecoderLineCard.setStatus("current")
_CerentVicEncoderPort_ObjectIdentity = ObjectIdentity
cerentVicEncoderPort = _CerentVicEncoderPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 500)
)
if mibBuilder.loadTexts:
    cerentVicEncoderPort.setStatus("current")
_CerentVicDecoderPort_ObjectIdentity = ObjectIdentity
cerentVicDecoderPort = _CerentVicDecoderPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 510)
)
if mibBuilder.loadTexts:
    cerentVicDecoderPort.setStatus("current")
_CerentVicTestPort_ObjectIdentity = ObjectIdentity
cerentVicTestPort = _CerentVicTestPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 520)
)
if mibBuilder.loadTexts:
    cerentVicTestPort.setStatus("current")
_CerentAip_ObjectIdentity = ObjectIdentity
cerentAip = _CerentAip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 530)
)
if mibBuilder.loadTexts:
    cerentAip.setStatus("current")
_CerentBicSmb_ObjectIdentity = ObjectIdentity
cerentBicSmb = _CerentBicSmb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 540)
)
if mibBuilder.loadTexts:
    cerentBicSmb.setStatus("current")
_CerentBicBnc_ObjectIdentity = ObjectIdentity
cerentBicBnc = _CerentBicBnc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 550)
)
if mibBuilder.loadTexts:
    cerentBicBnc.setStatus("current")
_CerentFcb_ObjectIdentity = ObjectIdentity
cerentFcb = _CerentFcb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 560)
)
if mibBuilder.loadTexts:
    cerentFcb.setStatus("current")
_CerentEnvironmentControl_ObjectIdentity = ObjectIdentity
cerentEnvironmentControl = _CerentEnvironmentControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 570)
)
if mibBuilder.loadTexts:
    cerentEnvironmentControl.setStatus("current")
_CerentLedIndicator_ObjectIdentity = ObjectIdentity
cerentLedIndicator = _CerentLedIndicator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 580)
)
if mibBuilder.loadTexts:
    cerentLedIndicator.setStatus("current")
_CerentAudibleAlarm_ObjectIdentity = ObjectIdentity
cerentAudibleAlarm = _CerentAudibleAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 590)
)
if mibBuilder.loadTexts:
    cerentAudibleAlarm.setStatus("current")
_CerentXc10g_ObjectIdentity = ObjectIdentity
cerentXc10g = _CerentXc10g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 600)
)
if mibBuilder.loadTexts:
    cerentXc10g.setStatus("current")
_CerentOc192Card_ObjectIdentity = ObjectIdentity
cerentOc192Card = _CerentOc192Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 610)
)
if mibBuilder.loadTexts:
    cerentOc192Card.setStatus("current")
_CerentOc192Port_ObjectIdentity = ObjectIdentity
cerentOc192Port = _CerentOc192Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 620)
)
if mibBuilder.loadTexts:
    cerentOc192Port.setStatus("current")
_CerentDs3eCard_ObjectIdentity = ObjectIdentity
cerentDs3eCard = _CerentDs3eCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 630)
)
if mibBuilder.loadTexts:
    cerentDs3eCard.setStatus("current")
_CerentDs3neCard_ObjectIdentity = ObjectIdentity
cerentDs3neCard = _CerentDs3neCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 640)
)
if mibBuilder.loadTexts:
    cerentDs3neCard.setStatus("current")
_Cerent15216OpmChassis_ObjectIdentity = ObjectIdentity
cerent15216OpmChassis = _Cerent15216OpmChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 650)
)
if mibBuilder.loadTexts:
    cerent15216OpmChassis.setStatus("current")
_Cerent15216OpmBackPlane_ObjectIdentity = ObjectIdentity
cerent15216OpmBackPlane = _Cerent15216OpmBackPlane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 660)
)
if mibBuilder.loadTexts:
    cerent15216OpmBackPlane.setStatus("current")
_Cerent15216OpmSlot_ObjectIdentity = ObjectIdentity
cerent15216OpmSlot = _Cerent15216OpmSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 670)
)
if mibBuilder.loadTexts:
    cerent15216OpmSlot.setStatus("current")
_Cerent15216OpmController_ObjectIdentity = ObjectIdentity
cerent15216OpmController = _Cerent15216OpmController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 680)
)
if mibBuilder.loadTexts:
    cerent15216OpmController.setStatus("current")
_Cerent15216OpmSpectrometer_ObjectIdentity = ObjectIdentity
cerent15216OpmSpectrometer = _Cerent15216OpmSpectrometer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 690)
)
if mibBuilder.loadTexts:
    cerent15216OpmSpectrometer.setStatus("current")
_Cerent15216OpmOpticalSwitch_ObjectIdentity = ObjectIdentity
cerent15216OpmOpticalSwitch = _Cerent15216OpmOpticalSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 700)
)
if mibBuilder.loadTexts:
    cerent15216OpmOpticalSwitch.setStatus("current")
_Cerent15216OpmOpticalPort_ObjectIdentity = ObjectIdentity
cerent15216OpmOpticalPort = _Cerent15216OpmOpticalPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 710)
)
if mibBuilder.loadTexts:
    cerent15216OpmOpticalPort.setStatus("current")
_Cerent15216OpmSerialPort_ObjectIdentity = ObjectIdentity
cerent15216OpmSerialPort = _Cerent15216OpmSerialPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 720)
)
if mibBuilder.loadTexts:
    cerent15216OpmSerialPort.setStatus("current")
_Cerent15216OpmLedIndicator_ObjectIdentity = ObjectIdentity
cerent15216OpmLedIndicator = _Cerent15216OpmLedIndicator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 730)
)
if mibBuilder.loadTexts:
    cerent15216OpmLedIndicator.setStatus("current")
_Cerent15216OpmRelay_ObjectIdentity = ObjectIdentity
cerent15216OpmRelay = _Cerent15216OpmRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 740)
)
if mibBuilder.loadTexts:
    cerent15216OpmRelay.setStatus("current")
_Cerent15216OpmPowerSupply_ObjectIdentity = ObjectIdentity
cerent15216OpmPowerSupply = _Cerent15216OpmPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 750)
)
if mibBuilder.loadTexts:
    cerent15216OpmPowerSupply.setStatus("current")
_Cerent15216OpmPcmciaSlot_ObjectIdentity = ObjectIdentity
cerent15216OpmPcmciaSlot = _Cerent15216OpmPcmciaSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 760)
)
if mibBuilder.loadTexts:
    cerent15216OpmPcmciaSlot.setStatus("current")
_CerentOc12QuadCard_ObjectIdentity = ObjectIdentity
cerentOc12QuadCard = _CerentOc12QuadCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 770)
)
if mibBuilder.loadTexts:
    cerentOc12QuadCard.setStatus("current")
_CerentG1000QuadCard_ObjectIdentity = ObjectIdentity
cerentG1000QuadCard = _CerentG1000QuadCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 780)
)
if mibBuilder.loadTexts:
    cerentG1000QuadCard.setStatus("deprecated")
_CerentG1000Port_ObjectIdentity = ObjectIdentity
cerentG1000Port = _CerentG1000Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 790)
)
if mibBuilder.loadTexts:
    cerentG1000Port.setStatus("current")
_CerentMlEtherPort_ObjectIdentity = ObjectIdentity
cerentMlEtherPort = _CerentMlEtherPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 791)
)
if mibBuilder.loadTexts:
    cerentMlEtherPort.setStatus("current")
_CerentMlPosPort_ObjectIdentity = ObjectIdentity
cerentMlPosPort = _CerentMlPosPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 792)
)
if mibBuilder.loadTexts:
    cerentMlPosPort.setStatus("current")
_CerentG1000GenericCard_ObjectIdentity = ObjectIdentity
cerentG1000GenericCard = _CerentG1000GenericCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 800)
)
if mibBuilder.loadTexts:
    cerentG1000GenericCard.setStatus("current")
_CerentML100GenericCard_ObjectIdentity = ObjectIdentity
cerentML100GenericCard = _CerentML100GenericCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 801)
)
if mibBuilder.loadTexts:
    cerentML100GenericCard.setStatus("current")
_CerentML1000GenericCard_ObjectIdentity = ObjectIdentity
cerentML1000GenericCard = _CerentML1000GenericCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 802)
)
if mibBuilder.loadTexts:
    cerentML1000GenericCard.setStatus("current")
_CerentG1K4Card_ObjectIdentity = ObjectIdentity
cerentG1K4Card = _CerentG1K4Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 810)
)
if mibBuilder.loadTexts:
    cerentG1K4Card.setStatus("current")
_CerentOc192IrCard_ObjectIdentity = ObjectIdentity
cerentOc192IrCard = _CerentOc192IrCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 820)
)
if mibBuilder.loadTexts:
    cerentOc192IrCard.setStatus("current")
_CerentOc192LrCard_ObjectIdentity = ObjectIdentity
cerentOc192LrCard = _CerentOc192LrCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 830)
)
if mibBuilder.loadTexts:
    cerentOc192LrCard.setStatus("current")
_CerentOc192ItuCard_ObjectIdentity = ObjectIdentity
cerentOc192ItuCard = _CerentOc192ItuCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 840)
)
if mibBuilder.loadTexts:
    cerentOc192ItuCard.setStatus("current")
_CerentOc3n1Card_ObjectIdentity = ObjectIdentity
cerentOc3n1Card = _CerentOc3n1Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 850)
)
if mibBuilder.loadTexts:
    cerentOc3n1Card.setStatus("current")
_Ape_ObjectIdentity = ObjectIdentity
ape = _Ape_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 860)
)
if mibBuilder.loadTexts:
    ape.setStatus("current")
_OneGePort_ObjectIdentity = ObjectIdentity
oneGePort = _OneGePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 870)
)
if mibBuilder.loadTexts:
    oneGePort.setStatus("current")
_TenGePort_ObjectIdentity = ObjectIdentity
tenGePort = _TenGePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 880)
)
if mibBuilder.loadTexts:
    tenGePort.setStatus("current")
_EsconPort_ObjectIdentity = ObjectIdentity
esconPort = _EsconPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 890)
)
if mibBuilder.loadTexts:
    esconPort.setStatus("current")
_Dv6000Port_ObjectIdentity = ObjectIdentity
dv6000Port = _Dv6000Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 900)
)
if mibBuilder.loadTexts:
    dv6000Port.setStatus("current")
_CerentE1n14_ObjectIdentity = ObjectIdentity
cerentE1n14 = _CerentE1n14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 910)
)
if mibBuilder.loadTexts:
    cerentE1n14.setStatus("current")
_CerentBackPlane454SDH_ObjectIdentity = ObjectIdentity
cerentBackPlane454SDH = _CerentBackPlane454SDH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 911)
)
if mibBuilder.loadTexts:
    cerentBackPlane454SDH.setStatus("current")
_CerentChassis454SDH_ObjectIdentity = ObjectIdentity
cerentChassis454SDH = _CerentChassis454SDH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 912)
)
if mibBuilder.loadTexts:
    cerentChassis454SDH.setStatus("current")
_CerentDs3inCard_ObjectIdentity = ObjectIdentity
cerentDs3inCard = _CerentDs3inCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 913)
)
if mibBuilder.loadTexts:
    cerentDs3inCard.setStatus("current")
_CerentE312Card_ObjectIdentity = ObjectIdentity
cerentE312Card = _CerentE312Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 914)
)
if mibBuilder.loadTexts:
    cerentE312Card.setStatus("current")
_CerentE1Port_ObjectIdentity = ObjectIdentity
cerentE1Port = _CerentE1Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 915)
)
if mibBuilder.loadTexts:
    cerentE1Port.setStatus("current")
_CerentDs3iPort_ObjectIdentity = ObjectIdentity
cerentDs3iPort = _CerentDs3iPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 916)
)
if mibBuilder.loadTexts:
    cerentDs3iPort.setStatus("current")
_CerentE3Port_ObjectIdentity = ObjectIdentity
cerentE3Port = _CerentE3Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 917)
)
if mibBuilder.loadTexts:
    cerentE3Port.setStatus("current")
_CerentAlmPwrSlot_ObjectIdentity = ObjectIdentity
cerentAlmPwrSlot = _CerentAlmPwrSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 918)
)
if mibBuilder.loadTexts:
    cerentAlmPwrSlot.setStatus("current")
_CerentCrftTmgSlot_ObjectIdentity = ObjectIdentity
cerentCrftTmgSlot = _CerentCrftTmgSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 919)
)
if mibBuilder.loadTexts:
    cerentCrftTmgSlot.setStatus("current")
_CerentAlmPwr_ObjectIdentity = ObjectIdentity
cerentAlmPwr = _CerentAlmPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 920)
)
if mibBuilder.loadTexts:
    cerentAlmPwr.setStatus("current")
_CerentCrftTmg_ObjectIdentity = ObjectIdentity
cerentCrftTmg = _CerentCrftTmg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 921)
)
if mibBuilder.loadTexts:
    cerentCrftTmg.setStatus("current")
_CerentFmecDb_ObjectIdentity = ObjectIdentity
cerentFmecDb = _CerentFmecDb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 922)
)
if mibBuilder.loadTexts:
    cerentFmecDb.setStatus("current")
_CerentFmecSmzE1_ObjectIdentity = ObjectIdentity
cerentFmecSmzE1 = _CerentFmecSmzE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 923)
)
if mibBuilder.loadTexts:
    cerentFmecSmzE1.setStatus("current")
_CerentFmecBlank_ObjectIdentity = ObjectIdentity
cerentFmecBlank = _CerentFmecBlank_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 924)
)
if mibBuilder.loadTexts:
    cerentFmecBlank.setStatus("current")
_CerentXcVxlCard_ObjectIdentity = ObjectIdentity
cerentXcVxlCard = _CerentXcVxlCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 925)
)
if mibBuilder.loadTexts:
    cerentXcVxlCard.setStatus("current")
_CerentEfca454Sdh_ObjectIdentity = ObjectIdentity
cerentEfca454Sdh = _CerentEfca454Sdh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 926)
)
if mibBuilder.loadTexts:
    cerentEfca454Sdh.setStatus("current")
_CerentFmecSlot_ObjectIdentity = ObjectIdentity
cerentFmecSlot = _CerentFmecSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 927)
)
if mibBuilder.loadTexts:
    cerentFmecSlot.setStatus("current")
_CerentFmecSmzE3_ObjectIdentity = ObjectIdentity
cerentFmecSmzE3 = _CerentFmecSmzE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 928)
)
if mibBuilder.loadTexts:
    cerentFmecSmzE3.setStatus("current")
_CerentDs3i_ObjectIdentity = ObjectIdentity
cerentDs3i = _CerentDs3i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 929)
)
if mibBuilder.loadTexts:
    cerentDs3i.setStatus("current")
_Cerent15216EdfaChassis_ObjectIdentity = ObjectIdentity
cerent15216EdfaChassis = _Cerent15216EdfaChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 930)
)
if mibBuilder.loadTexts:
    cerent15216EdfaChassis.setStatus("current")
_CerentAici_ObjectIdentity = ObjectIdentity
cerentAici = _CerentAici_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 931)
)
if mibBuilder.loadTexts:
    cerentAici.setStatus("current")
_CerentFudcPort_ObjectIdentity = ObjectIdentity
cerentFudcPort = _CerentFudcPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 932)
)
if mibBuilder.loadTexts:
    cerentFudcPort.setStatus("current")
_CerentDccPort_ObjectIdentity = ObjectIdentity
cerentDccPort = _CerentDccPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 933)
)
if mibBuilder.loadTexts:
    cerentDccPort.setStatus("current")
_CerentAiciAep_ObjectIdentity = ObjectIdentity
cerentAiciAep = _CerentAiciAep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 934)
)
if mibBuilder.loadTexts:
    cerentAiciAep.setStatus("current")
_CerentAiciAie_ObjectIdentity = ObjectIdentity
cerentAiciAie = _CerentAiciAie_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 935)
)
if mibBuilder.loadTexts:
    cerentAiciAie.setStatus("current")
_CerentXcVxl25GCard_ObjectIdentity = ObjectIdentity
cerentXcVxl25GCard = _CerentXcVxl25GCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 936)
)
if mibBuilder.loadTexts:
    cerentXcVxl25GCard.setStatus("current")
_CerentE114_ObjectIdentity = ObjectIdentity
cerentE114 = _CerentE114_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 937)
)
if mibBuilder.loadTexts:
    cerentE114.setStatus("current")
_CerentPIMSlot_ObjectIdentity = ObjectIdentity
cerentPIMSlot = _CerentPIMSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 940)
)
if mibBuilder.loadTexts:
    cerentPIMSlot.setStatus("current")
_CerentPIM4PPM_ObjectIdentity = ObjectIdentity
cerentPIM4PPM = _CerentPIM4PPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 950)
)
if mibBuilder.loadTexts:
    cerentPIM4PPM.setStatus("current")
_CerentPPMSlot_ObjectIdentity = ObjectIdentity
cerentPPMSlot = _CerentPPMSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 960)
)
if mibBuilder.loadTexts:
    cerentPPMSlot.setStatus("current")
_CerentPPM1Port_ObjectIdentity = ObjectIdentity
cerentPPM1Port = _CerentPPM1Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 970)
)
if mibBuilder.loadTexts:
    cerentPPM1Port.setStatus("current")
_CerentOptDemux32RChCard_ObjectIdentity = ObjectIdentity
cerentOptDemux32RChCard = _CerentOptDemux32RChCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 980)
)
if mibBuilder.loadTexts:
    cerentOptDemux32RChCard.setStatus("current")
_CerentOptWss32ChCard_ObjectIdentity = ObjectIdentity
cerentOptWss32ChCard = _CerentOptWss32ChCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 990)
)
if mibBuilder.loadTexts:
    cerentOptWss32ChCard.setStatus("current")
_CerentChassis15310ClOid_ObjectIdentity = ObjectIdentity
cerentChassis15310ClOid = _CerentChassis15310ClOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1000)
)
if mibBuilder.loadTexts:
    cerentChassis15310ClOid.setStatus("current")
_CerentChassis15310MaAnsiOid_ObjectIdentity = ObjectIdentity
cerentChassis15310MaAnsiOid = _CerentChassis15310MaAnsiOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1010)
)
if mibBuilder.loadTexts:
    cerentChassis15310MaAnsiOid.setStatus("current")
_CerentChassis15310MaEtsiOid_ObjectIdentity = ObjectIdentity
cerentChassis15310MaEtsiOid = _CerentChassis15310MaEtsiOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1020)
)
if mibBuilder.loadTexts:
    cerentChassis15310MaEtsiOid.setStatus("current")
_CerentBackplane15310ClOid_ObjectIdentity = ObjectIdentity
cerentBackplane15310ClOid = _CerentBackplane15310ClOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1030)
)
if mibBuilder.loadTexts:
    cerentBackplane15310ClOid.setStatus("current")
_CerentBackplane15310MaAnsiOid_ObjectIdentity = ObjectIdentity
cerentBackplane15310MaAnsiOid = _CerentBackplane15310MaAnsiOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1040)
)
if mibBuilder.loadTexts:
    cerentBackplane15310MaAnsiOid.setStatus("current")
_CerentBackplane15310MaEtsiOid_ObjectIdentity = ObjectIdentity
cerentBackplane15310MaEtsiOid = _CerentBackplane15310MaEtsiOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1050)
)
if mibBuilder.loadTexts:
    cerentBackplane15310MaEtsiOid.setStatus("current")
_CerentCtxCardOid_ObjectIdentity = ObjectIdentity
cerentCtxCardOid = _CerentCtxCardOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1060)
)
if mibBuilder.loadTexts:
    cerentCtxCardOid.setStatus("current")
_CerentBbeLineCardOid_ObjectIdentity = ObjectIdentity
cerentBbeLineCardOid = _CerentBbeLineCardOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1070)
)
if mibBuilder.loadTexts:
    cerentBbeLineCardOid.setStatus("current")
_CerentWbeLineCardOid_ObjectIdentity = ObjectIdentity
cerentWbeLineCardOid = _CerentWbeLineCardOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1080)
)
if mibBuilder.loadTexts:
    cerentWbeLineCardOid.setStatus("current")
_CerentCtxSlotOid_ObjectIdentity = ObjectIdentity
cerentCtxSlotOid = _CerentCtxSlotOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1090)
)
if mibBuilder.loadTexts:
    cerentCtxSlotOid.setStatus("current")
_CerentBbeSlotOid_ObjectIdentity = ObjectIdentity
cerentBbeSlotOid = _CerentBbeSlotOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1100)
)
if mibBuilder.loadTexts:
    cerentBbeSlotOid.setStatus("current")
_CerentWbeSlotOid_ObjectIdentity = ObjectIdentity
cerentWbeSlotOid = _CerentWbeSlotOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1110)
)
if mibBuilder.loadTexts:
    cerentWbeSlotOid.setStatus("current")
_CerentAsap4LineCardOid_ObjectIdentity = ObjectIdentity
cerentAsap4LineCardOid = _CerentAsap4LineCardOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1120)
)
if mibBuilder.loadTexts:
    cerentAsap4LineCardOid.setStatus("current")
_CerentMrc4LineCardOid_ObjectIdentity = ObjectIdentity
cerentMrc4LineCardOid = _CerentMrc4LineCardOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1130)
)
if mibBuilder.loadTexts:
    cerentMrc4LineCardOid.setStatus("current")
_Cerent310CE100t8LineCardOid_ObjectIdentity = ObjectIdentity
cerent310CE100t8LineCardOid = _Cerent310CE100t8LineCardOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1140)
)
if mibBuilder.loadTexts:
    cerent310CE100t8LineCardOid.setStatus("current")
_Cerent310ML100t8LineCardOid_ObjectIdentity = ObjectIdentity
cerent310ML100t8LineCardOid = _Cerent310ML100t8LineCardOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1150)
)
if mibBuilder.loadTexts:
    cerent310ML100t8LineCardOid.setStatus("current")
_CerentL1PPosPortOid_ObjectIdentity = ObjectIdentity
cerentL1PPosPortOid = _CerentL1PPosPortOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1160)
)
if mibBuilder.loadTexts:
    cerentL1PPosPortOid.setStatus("current")
_CerentL1PEtherPortOid_ObjectIdentity = ObjectIdentity
cerentL1PEtherPortOid = _CerentL1PEtherPortOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1170)
)
if mibBuilder.loadTexts:
    cerentL1PEtherPortOid.setStatus("current")
_Fc10gPort_ObjectIdentity = ObjectIdentity
fc10gPort = _Fc10gPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1180)
)
if mibBuilder.loadTexts:
    fc10gPort.setStatus("current")
_Ficon1gport_ObjectIdentity = ObjectIdentity
ficon1gport = _Ficon1gport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1190)
)
if mibBuilder.loadTexts:
    ficon1gport.setStatus("current")
_Ficon2gport_ObjectIdentity = ObjectIdentity
ficon2gport = _Ficon2gport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1200)
)
if mibBuilder.loadTexts:
    ficon2gport.setStatus("current")
_CerentOc192Card4Ports_ObjectIdentity = ObjectIdentity
cerentOc192Card4Ports = _CerentOc192Card4Ports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1210)
)
if mibBuilder.loadTexts:
    cerentOc192Card4Ports.setStatus("current")
_CerentOc48Card8Ports_ObjectIdentity = ObjectIdentity
cerentOc48Card8Ports = _CerentOc48Card8Ports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1215)
)
if mibBuilder.loadTexts:
    cerentOc48Card8Ports.setStatus("current")
_CerentOc48Card16Ports_ObjectIdentity = ObjectIdentity
cerentOc48Card16Ports = _CerentOc48Card16Ports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1220)
)
if mibBuilder.loadTexts:
    cerentOc48Card16Ports.setStatus("current")
_Cerent15600ControllerSlot_ObjectIdentity = ObjectIdentity
cerent15600ControllerSlot = _Cerent15600ControllerSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1225)
)
if mibBuilder.loadTexts:
    cerent15600ControllerSlot.setStatus("current")
_CerentTsc_ObjectIdentity = ObjectIdentity
cerentTsc = _CerentTsc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1230)
)
if mibBuilder.loadTexts:
    cerentTsc.setStatus("current")
_CerentChassis600_ObjectIdentity = ObjectIdentity
cerentChassis600 = _CerentChassis600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1235)
)
if mibBuilder.loadTexts:
    cerentChassis600.setStatus("current")
_CerentBackPlane600_ObjectIdentity = ObjectIdentity
cerentBackPlane600 = _CerentBackPlane600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1240)
)
if mibBuilder.loadTexts:
    cerentBackPlane600.setStatus("current")
_CerentCap_ObjectIdentity = ObjectIdentity
cerentCap = _CerentCap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1245)
)
if mibBuilder.loadTexts:
    cerentCap.setStatus("current")
_CerentCxc_ObjectIdentity = ObjectIdentity
cerentCxc = _CerentCxc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1250)
)
if mibBuilder.loadTexts:
    cerentCxc.setStatus("current")
_CerentCxcSlot_ObjectIdentity = ObjectIdentity
cerentCxcSlot = _CerentCxcSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1255)
)
if mibBuilder.loadTexts:
    cerentCxcSlot.setStatus("current")
_CerentFillerCard_ObjectIdentity = ObjectIdentity
cerentFillerCard = _CerentFillerCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1260)
)
if mibBuilder.loadTexts:
    cerentFillerCard.setStatus("current")
_CerentFcmrLineCard_ObjectIdentity = ObjectIdentity
cerentFcmrLineCard = _CerentFcmrLineCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1265)
)
if mibBuilder.loadTexts:
    cerentFcmrLineCard.setStatus("current")
_CerentFcmrPort_ObjectIdentity = ObjectIdentity
cerentFcmrPort = _CerentFcmrPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1270)
)
if mibBuilder.loadTexts:
    cerentFcmrPort.setStatus("current")
_CerentTxpd10ECard_ObjectIdentity = ObjectIdentity
cerentTxpd10ECard = _CerentTxpd10ECard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1275)
)
if mibBuilder.loadTexts:
    cerentTxpd10ECard.setStatus("current")
_CerentMuxpd25G10ECard_ObjectIdentity = ObjectIdentity
cerentMuxpd25G10ECard = _CerentMuxpd25G10ECard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1280)
)
if mibBuilder.loadTexts:
    cerentMuxpd25G10ECard.setStatus("current")
_CerentDs3Xm12Card_ObjectIdentity = ObjectIdentity
cerentDs3Xm12Card = _CerentDs3Xm12Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1285)
)
if mibBuilder.loadTexts:
    cerentDs3Xm12Card.setStatus("current")
_Ds3Ec148LineCard_ObjectIdentity = ObjectIdentity
ds3Ec148LineCard = _Ds3Ec148LineCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1290)
)
if mibBuilder.loadTexts:
    ds3Ec148LineCard.setStatus("current")
_GfpPort_ObjectIdentity = ObjectIdentity
gfpPort = _GfpPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1300)
)
if mibBuilder.loadTexts:
    gfpPort.setStatus("current")
_Cerent454CE100t8LineCardOid_ObjectIdentity = ObjectIdentity
cerent454CE100t8LineCardOid = _Cerent454CE100t8LineCardOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1310)
)
if mibBuilder.loadTexts:
    cerent454CE100t8LineCardOid.setStatus("current")
_BicUniv_ObjectIdentity = ObjectIdentity
bicUniv = _BicUniv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1320)
)
if mibBuilder.loadTexts:
    bicUniv.setStatus("current")
_BicUnknown_ObjectIdentity = ObjectIdentity
bicUnknown = _BicUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1330)
)
if mibBuilder.loadTexts:
    bicUnknown.setStatus("current")
_SdiD1VideoPort_ObjectIdentity = ObjectIdentity
sdiD1VideoPort = _SdiD1VideoPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1340)
)
if mibBuilder.loadTexts:
    sdiD1VideoPort.setStatus("current")
_HdtvPort_ObjectIdentity = ObjectIdentity
hdtvPort = _HdtvPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1350)
)
if mibBuilder.loadTexts:
    hdtvPort.setStatus("current")
_PassThruPort_ObjectIdentity = ObjectIdentity
passThruPort = _PassThruPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1360)
)
if mibBuilder.loadTexts:
    passThruPort.setStatus("current")
_EtrCloPort_ObjectIdentity = ObjectIdentity
etrCloPort = _EtrCloPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1370)
)
if mibBuilder.loadTexts:
    etrCloPort.setStatus("current")
_IscPort_ObjectIdentity = ObjectIdentity
iscPort = _IscPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1380)
)
if mibBuilder.loadTexts:
    iscPort.setStatus("current")
_Fc1gPort_ObjectIdentity = ObjectIdentity
fc1gPort = _Fc1gPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1390)
)
if mibBuilder.loadTexts:
    fc1gPort.setStatus("current")
_Fc2gPort_ObjectIdentity = ObjectIdentity
fc2gPort = _Fc2gPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1400)
)
if mibBuilder.loadTexts:
    fc2gPort.setStatus("current")
_MrSlot_ObjectIdentity = ObjectIdentity
mrSlot = _MrSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1410)
)
if mibBuilder.loadTexts:
    mrSlot.setStatus("current")
_Isc3Port_ObjectIdentity = ObjectIdentity
isc3Port = _Isc3Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1420)
)
if mibBuilder.loadTexts:
    isc3Port.setStatus("current")
_CerentDs1i14_ObjectIdentity = ObjectIdentity
cerentDs1i14 = _CerentDs1i14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1430)
)
if mibBuilder.loadTexts:
    cerentDs1i14.setStatus("current")
_CerentFmecDs1i14_ObjectIdentity = ObjectIdentity
cerentFmecDs1i14 = _CerentFmecDs1i14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1440)
)
if mibBuilder.loadTexts:
    cerentFmecDs1i14.setStatus("current")
_CerentBackPlane454HD_ObjectIdentity = ObjectIdentity
cerentBackPlane454HD = _CerentBackPlane454HD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1450)
)
if mibBuilder.loadTexts:
    cerentBackPlane454HD.setStatus("current")
_CerentDs1E156LineCard_ObjectIdentity = ObjectIdentity
cerentDs1E156LineCard = _CerentDs1E156LineCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1470)
)
if mibBuilder.loadTexts:
    cerentDs1E156LineCard.setStatus("current")
_CerentMrc12LineCard_ObjectIdentity = ObjectIdentity
cerentMrc12LineCard = _CerentMrc12LineCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1480)
)
if mibBuilder.loadTexts:
    cerentMrc12LineCard.setStatus("current")
_CerentOc192XfpLineCard_ObjectIdentity = ObjectIdentity
cerentOc192XfpLineCard = _CerentOc192XfpLineCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1490)
)
if mibBuilder.loadTexts:
    cerentOc192XfpLineCard.setStatus("current")
_CerentPowerSupply_ObjectIdentity = ObjectIdentity
cerentPowerSupply = _CerentPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1500)
)
if mibBuilder.loadTexts:
    cerentPowerSupply.setStatus("current")
_CerentTxpd10GCard_ObjectIdentity = ObjectIdentity
cerentTxpd10GCard = _CerentTxpd10GCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1550)
)
if mibBuilder.loadTexts:
    cerentTxpd10GCard.setStatus("current")
_CerentTxpd25GCard_ObjectIdentity = ObjectIdentity
cerentTxpd25GCard = _CerentTxpd25GCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1560)
)
if mibBuilder.loadTexts:
    cerentTxpd25GCard.setStatus("current")
_CerentTxpdP25GCard_ObjectIdentity = ObjectIdentity
cerentTxpdP25GCard = _CerentTxpdP25GCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1570)
)
if mibBuilder.loadTexts:
    cerentTxpdP25GCard.setStatus("current")
_CerentMuxpd25G10GCard_ObjectIdentity = ObjectIdentity
cerentMuxpd25G10GCard = _CerentMuxpd25G10GCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1580)
)
if mibBuilder.loadTexts:
    cerentMuxpd25G10GCard.setStatus("current")
_CerentDwdmClientPort_ObjectIdentity = ObjectIdentity
cerentDwdmClientPort = _CerentDwdmClientPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1590)
)
if mibBuilder.loadTexts:
    cerentDwdmClientPort.setStatus("current")
_CerentDwdmTrunkPort_ObjectIdentity = ObjectIdentity
cerentDwdmTrunkPort = _CerentDwdmTrunkPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1600)
)
if mibBuilder.loadTexts:
    cerentDwdmTrunkPort.setStatus("current")
_CerentMuxpdMr25GCard_ObjectIdentity = ObjectIdentity
cerentMuxpdMr25GCard = _CerentMuxpdMr25GCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1610)
)
if mibBuilder.loadTexts:
    cerentMuxpdMr25GCard.setStatus("current")
_CerentMuxpdPMr25GCard_ObjectIdentity = ObjectIdentity
cerentMuxpdPMr25GCard = _CerentMuxpdPMr25GCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1620)
)
if mibBuilder.loadTexts:
    cerentMuxpdPMr25GCard.setStatus("current")
_CerentMm850Port_ObjectIdentity = ObjectIdentity
cerentMm850Port = _CerentMm850Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1630)
)
if mibBuilder.loadTexts:
    cerentMm850Port.setStatus("current")
_CerentSm1310Port_ObjectIdentity = ObjectIdentity
cerentSm1310Port = _CerentSm1310Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1640)
)
if mibBuilder.loadTexts:
    cerentSm1310Port.setStatus("current")
_CerentXcVxcCard_ObjectIdentity = ObjectIdentity
cerentXcVxcCard = _CerentXcVxcCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1670)
)
if mibBuilder.loadTexts:
    cerentXcVxcCard.setStatus("current")
_CerentXcVxc25GCard_ObjectIdentity = ObjectIdentity
cerentXcVxc25GCard = _CerentXcVxc25GCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1680)
)
if mibBuilder.loadTexts:
    cerentXcVxc25GCard.setStatus("current")
_CerentOptBstECard_ObjectIdentity = ObjectIdentity
cerentOptBstECard = _CerentOptBstECard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1690)
)
if mibBuilder.loadTexts:
    cerentOptBstECard.setStatus("current")
_Fc4gPort_ObjectIdentity = ObjectIdentity
fc4gPort = _Fc4gPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1700)
)
if mibBuilder.loadTexts:
    fc4gPort.setStatus("current")
_Ficon4gport_ObjectIdentity = ObjectIdentity
ficon4gport = _Ficon4gport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1710)
)
if mibBuilder.loadTexts:
    ficon4gport.setStatus("current")
_Isc3Peer1gPort_ObjectIdentity = ObjectIdentity
isc3Peer1gPort = _Isc3Peer1gPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1720)
)
if mibBuilder.loadTexts:
    isc3Peer1gPort.setStatus("current")
_Isc3Peer2gPort_ObjectIdentity = ObjectIdentity
isc3Peer2gPort = _Isc3Peer2gPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 1730)
)
if mibBuilder.loadTexts:
    isc3Peer2gPort.setStatus("current")
_CerentOscmCard_ObjectIdentity = ObjectIdentity
cerentOscmCard = _CerentOscmCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 3200)
)
if mibBuilder.loadTexts:
    cerentOscmCard.setStatus("current")
_CerentOscCsmCard_ObjectIdentity = ObjectIdentity
cerentOscCsmCard = _CerentOscCsmCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 3205)
)
if mibBuilder.loadTexts:
    cerentOscCsmCard.setStatus("current")
_CerentOptPreCard_ObjectIdentity = ObjectIdentity
cerentOptPreCard = _CerentOptPreCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 3210)
)
if mibBuilder.loadTexts:
    cerentOptPreCard.setStatus("current")
_CerentOptBstCard_ObjectIdentity = ObjectIdentity
cerentOptBstCard = _CerentOptBstCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 3215)
)
if mibBuilder.loadTexts:
    cerentOptBstCard.setStatus("current")
_CerentOptDemux32ChCard_ObjectIdentity = ObjectIdentity
cerentOptDemux32ChCard = _CerentOptDemux32ChCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 3220)
)
if mibBuilder.loadTexts:
    cerentOptDemux32ChCard.setStatus("current")
_CerentOptMux32ChCard_ObjectIdentity = ObjectIdentity
cerentOptMux32ChCard = _CerentOptMux32ChCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 3225)
)
if mibBuilder.loadTexts:
    cerentOptMux32ChCard.setStatus("current")
_CerentOptMuxDemux4ChCard_ObjectIdentity = ObjectIdentity
cerentOptMuxDemux4ChCard = _CerentOptMuxDemux4ChCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 3230)
)
if mibBuilder.loadTexts:
    cerentOptMuxDemux4ChCard.setStatus("current")
_CerentOadm1ChCard_ObjectIdentity = ObjectIdentity
cerentOadm1ChCard = _CerentOadm1ChCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 3235)
)
if mibBuilder.loadTexts:
    cerentOadm1ChCard.setStatus("current")
_CerentOadm2ChCard_ObjectIdentity = ObjectIdentity
cerentOadm2ChCard = _CerentOadm2ChCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 3240)
)
if mibBuilder.loadTexts:
    cerentOadm2ChCard.setStatus("current")
_CerentOadm4ChCard_ObjectIdentity = ObjectIdentity
cerentOadm4ChCard = _CerentOadm4ChCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 3245)
)
if mibBuilder.loadTexts:
    cerentOadm4ChCard.setStatus("current")
_CerentOadm1BnCard_ObjectIdentity = ObjectIdentity
cerentOadm1BnCard = _CerentOadm1BnCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 3250)
)
if mibBuilder.loadTexts:
    cerentOadm1BnCard.setStatus("current")
_CerentOadm4BnCard_ObjectIdentity = ObjectIdentity
cerentOadm4BnCard = _CerentOadm4BnCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 3255)
)
if mibBuilder.loadTexts:
    cerentOadm4BnCard.setStatus("current")
_CerentOTSPort_ObjectIdentity = ObjectIdentity
cerentOTSPort = _CerentOTSPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 3260)
)
if mibBuilder.loadTexts:
    cerentOTSPort.setStatus("current")
_CerentAOTSPort_ObjectIdentity = ObjectIdentity
cerentAOTSPort = _CerentAOTSPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 3265)
)
if mibBuilder.loadTexts:
    cerentAOTSPort.setStatus("current")
_CerentOMSPort_ObjectIdentity = ObjectIdentity
cerentOMSPort = _CerentOMSPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 3270)
)
if mibBuilder.loadTexts:
    cerentOMSPort.setStatus("current")
_CerentOCHPort_ObjectIdentity = ObjectIdentity
cerentOCHPort = _CerentOCHPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 3275)
)
if mibBuilder.loadTexts:
    cerentOCHPort.setStatus("current")
_CerentE1P42LineCard_ObjectIdentity = ObjectIdentity
cerentE1P42LineCard = _CerentE1P42LineCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4000)
)
if mibBuilder.loadTexts:
    cerentE1P42LineCard.setStatus("current")
_CerentE1nP42LineCard_ObjectIdentity = ObjectIdentity
cerentE1nP42LineCard = _CerentE1nP42LineCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4005)
)
if mibBuilder.loadTexts:
    cerentE1nP42LineCard.setStatus("current")
_CerentFmecE1P42TypeUnprotW120Card_ObjectIdentity = ObjectIdentity
cerentFmecE1P42TypeUnprotW120Card = _CerentFmecE1P42TypeUnprotW120Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4010)
)
if mibBuilder.loadTexts:
    cerentFmecE1P42TypeUnprotW120Card.setStatus("current")
_CerentFmecE1P42Type1To3W120aCard_ObjectIdentity = ObjectIdentity
cerentFmecE1P42Type1To3W120aCard = _CerentFmecE1P42Type1To3W120aCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4015)
)
if mibBuilder.loadTexts:
    cerentFmecE1P42Type1To3W120aCard.setStatus("current")
_CerentFmecE1P42Type1To3W120bCard_ObjectIdentity = ObjectIdentity
cerentFmecE1P42Type1To3W120bCard = _CerentFmecE1P42Type1To3W120bCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4020)
)
if mibBuilder.loadTexts:
    cerentFmecE1P42Type1To3W120bCard.setStatus("current")
_CerentStm1e12LineCard_ObjectIdentity = ObjectIdentity
cerentStm1e12LineCard = _CerentStm1e12LineCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4025)
)
if mibBuilder.loadTexts:
    cerentStm1e12LineCard.setStatus("current")
_CerentStm1ePort_ObjectIdentity = ObjectIdentity
cerentStm1ePort = _CerentStm1ePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4030)
)
if mibBuilder.loadTexts:
    cerentStm1ePort.setStatus("current")
_CerentFmec155eUnprotCard_ObjectIdentity = ObjectIdentity
cerentFmec155eUnprotCard = _CerentFmec155eUnprotCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4035)
)
if mibBuilder.loadTexts:
    cerentFmec155eUnprotCard.setStatus("current")
_CerentFmec155e1To1Card_ObjectIdentity = ObjectIdentity
cerentFmec155e1To1Card = _CerentFmec155e1To1Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4040)
)
if mibBuilder.loadTexts:
    cerentFmec155e1To1Card.setStatus("current")
_CerentFmec155e1To3Card_ObjectIdentity = ObjectIdentity
cerentFmec155e1To3Card = _CerentFmec155e1To3Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4045)
)
if mibBuilder.loadTexts:
    cerentFmec155e1To3Card.setStatus("current")
_Cerent15216Edfa3ShelfController_ObjectIdentity = ObjectIdentity
cerent15216Edfa3ShelfController = _Cerent15216Edfa3ShelfController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4050)
)
if mibBuilder.loadTexts:
    cerent15216Edfa3ShelfController.setStatus("current")
_Cerent15216Edfa3OpticsModule_ObjectIdentity = ObjectIdentity
cerent15216Edfa3OpticsModule = _Cerent15216Edfa3OpticsModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4051)
)
if mibBuilder.loadTexts:
    cerent15216Edfa3OpticsModule.setStatus("current")
_Cerent15216EdfaEtherPort_ObjectIdentity = ObjectIdentity
cerent15216EdfaEtherPort = _Cerent15216EdfaEtherPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4052)
)
if mibBuilder.loadTexts:
    cerent15216EdfaEtherPort.setStatus("current")
_Cerent15216EdfaSerialPort_ObjectIdentity = ObjectIdentity
cerent15216EdfaSerialPort = _Cerent15216EdfaSerialPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4053)
)
if mibBuilder.loadTexts:
    cerent15216EdfaSerialPort.setStatus("current")
_CerentMl100X8LineCard_ObjectIdentity = ObjectIdentity
cerentMl100X8LineCard = _CerentMl100X8LineCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4055)
)
if mibBuilder.loadTexts:
    cerentMl100X8LineCard.setStatus("current")
_CerentOptBstLCard_ObjectIdentity = ObjectIdentity
cerentOptBstLCard = _CerentOptBstLCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4060)
)
if mibBuilder.loadTexts:
    cerentOptBstLCard.setStatus("current")
_CerentOptAmpLCard_ObjectIdentity = ObjectIdentity
cerentOptAmpLCard = _CerentOptAmpLCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4065)
)
if mibBuilder.loadTexts:
    cerentOptAmpLCard.setStatus("current")
_CerentDmx32LCard_ObjectIdentity = ObjectIdentity
cerentDmx32LCard = _CerentDmx32LCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4070)
)
if mibBuilder.loadTexts:
    cerentDmx32LCard.setStatus("current")
_CerentWss32LCard_ObjectIdentity = ObjectIdentity
cerentWss32LCard = _CerentWss32LCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4075)
)
if mibBuilder.loadTexts:
    cerentWss32LCard.setStatus("current")
_CerentMMUCard_ObjectIdentity = ObjectIdentity
cerentMMUCard = _CerentMMUCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4080)
)
if mibBuilder.loadTexts:
    cerentMMUCard.setStatus("current")
_CerentMsIsc100tCard_ObjectIdentity = ObjectIdentity
cerentMsIsc100tCard = _CerentMsIsc100tCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4085)
)
if mibBuilder.loadTexts:
    cerentMsIsc100tCard.setStatus("current")
_CerentMxpMr10DmeCard_ObjectIdentity = ObjectIdentity
cerentMxpMr10DmeCard = _CerentMxpMr10DmeCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4090)
)
if mibBuilder.loadTexts:
    cerentMxpMr10DmeCard.setStatus("current")
_CerentCE1000Card_ObjectIdentity = ObjectIdentity
cerentCE1000Card = _CerentCE1000Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4095)
)
if mibBuilder.loadTexts:
    cerentCE1000Card.setStatus("current")
_CerentCE1000EtherPort_ObjectIdentity = ObjectIdentity
cerentCE1000EtherPort = _CerentCE1000EtherPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4100)
)
if mibBuilder.loadTexts:
    cerentCE1000EtherPort.setStatus("current")
_CerentCE1000PosPort_ObjectIdentity = ObjectIdentity
cerentCE1000PosPort = _CerentCE1000PosPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4105)
)
if mibBuilder.loadTexts:
    cerentCE1000PosPort.setStatus("current")
_CerentPIM1PPM_ObjectIdentity = ObjectIdentity
cerentPIM1PPM = _CerentPIM1PPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4110)
)
if mibBuilder.loadTexts:
    cerentPIM1PPM.setStatus("current")
_CerentCEMR454Card_ObjectIdentity = ObjectIdentity
cerentCEMR454Card = _CerentCEMR454Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4115)
)
if mibBuilder.loadTexts:
    cerentCEMR454Card.setStatus("current")
_CerentCEMR310Card_ObjectIdentity = ObjectIdentity
cerentCEMR310Card = _CerentCEMR310Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4120)
)
if mibBuilder.loadTexts:
    cerentCEMR310Card.setStatus("current")
_CerentCTX2500Card_ObjectIdentity = ObjectIdentity
cerentCTX2500Card = _CerentCTX2500Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4125)
)
if mibBuilder.loadTexts:
    cerentCTX2500Card.setStatus("current")
_CerentDs128Ds3EC13LineCard_ObjectIdentity = ObjectIdentity
cerentDs128Ds3EC13LineCard = _CerentDs128Ds3EC13LineCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4130)
)
if mibBuilder.loadTexts:
    cerentDs128Ds3EC13LineCard.setStatus("current")
_CerentDs184Ds3EC13LineCard_ObjectIdentity = ObjectIdentity
cerentDs184Ds3EC13LineCard = _CerentDs184Ds3EC13LineCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4135)
)
if mibBuilder.loadTexts:
    cerentDs184Ds3EC13LineCard.setStatus("current")
_CerentDs3EC16LineCard_ObjectIdentity = ObjectIdentity
cerentDs3EC16LineCard = _CerentDs3EC16LineCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4140)
)
if mibBuilder.loadTexts:
    cerentDs3EC16LineCard.setStatus("current")
_CerentBicTelco_ObjectIdentity = ObjectIdentity
cerentBicTelco = _CerentBicTelco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4145)
)
if mibBuilder.loadTexts:
    cerentBicTelco.setStatus("current")
_CerentBicCmn_ObjectIdentity = ObjectIdentity
cerentBicCmn = _CerentBicCmn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4150)
)
if mibBuilder.loadTexts:
    cerentBicCmn.setStatus("current")
_CerentRanSvcLineCard_ObjectIdentity = ObjectIdentity
cerentRanSvcLineCard = _CerentRanSvcLineCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4155)
)
if mibBuilder.loadTexts:
    cerentRanSvcLineCard.setStatus("current")
_CerentTxpd10EXCard_ObjectIdentity = ObjectIdentity
cerentTxpd10EXCard = _CerentTxpd10EXCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4160)
)
if mibBuilder.loadTexts:
    cerentTxpd10EXCard.setStatus("current")
_CerentTxpdP10EXCard_ObjectIdentity = ObjectIdentity
cerentTxpdP10EXCard = _CerentTxpdP10EXCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4165)
)
if mibBuilder.loadTexts:
    cerentTxpdP10EXCard.setStatus("current")
_CerentMuxpd25G10XCard_ObjectIdentity = ObjectIdentity
cerentMuxpd25G10XCard = _CerentMuxpd25G10XCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4170)
)
if mibBuilder.loadTexts:
    cerentMuxpd25G10XCard.setStatus("current")
_CerentOptAmp17Card_ObjectIdentity = ObjectIdentity
cerentOptAmp17Card = _CerentOptAmp17Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4175)
)
if mibBuilder.loadTexts:
    cerentOptAmp17Card.setStatus("current")
_CerentOptAmp23Card_ObjectIdentity = ObjectIdentity
cerentOptAmp23Card = _CerentOptAmp23Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4180)
)
if mibBuilder.loadTexts:
    cerentOptAmp23Card.setStatus("current")
_CerentOptWss40ChCard_ObjectIdentity = ObjectIdentity
cerentOptWss40ChCard = _CerentOptWss40ChCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4185)
)
if mibBuilder.loadTexts:
    cerentOptWss40ChCard.setStatus("current")
_CerentOptMux40ChCard_ObjectIdentity = ObjectIdentity
cerentOptMux40ChCard = _CerentOptMux40ChCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4190)
)
if mibBuilder.loadTexts:
    cerentOptMux40ChCard.setStatus("current")
_CerentOptDemux40ChCard_ObjectIdentity = ObjectIdentity
cerentOptDemux40ChCard = _CerentOptDemux40ChCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4195)
)
if mibBuilder.loadTexts:
    cerentOptDemux40ChCard.setStatus("current")
_CerentOptWxc40ChCard_ObjectIdentity = ObjectIdentity
cerentOptWxc40ChCard = _CerentOptWxc40ChCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4200)
)
if mibBuilder.loadTexts:
    cerentOptWxc40ChCard.setStatus("current")
_CerentXpd10GECard_ObjectIdentity = ObjectIdentity
cerentXpd10GECard = _CerentXpd10GECard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4205)
)
if mibBuilder.loadTexts:
    cerentXpd10GECard.setStatus("current")
_CerentXpdGECard_ObjectIdentity = ObjectIdentity
cerentXpdGECard = _CerentXpdGECard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4210)
)
if mibBuilder.loadTexts:
    cerentXpdGECard.setStatus("current")
_CerentOadm10GCard_ObjectIdentity = ObjectIdentity
cerentOadm10GCard = _CerentOadm10GCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4215)
)
if mibBuilder.loadTexts:
    cerentOadm10GCard.setStatus("current")
_CerentOtu2Port_ObjectIdentity = ObjectIdentity
cerentOtu2Port = _CerentOtu2Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4220)
)
if mibBuilder.loadTexts:
    cerentOtu2Port.setStatus("current")
_CerentWss40LCard_ObjectIdentity = ObjectIdentity
cerentWss40LCard = _CerentWss40LCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4225)
)
if mibBuilder.loadTexts:
    cerentWss40LCard.setStatus("current")
_CerentMux40LCard_ObjectIdentity = ObjectIdentity
cerentMux40LCard = _CerentMux40LCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4230)
)
if mibBuilder.loadTexts:
    cerentMux40LCard.setStatus("current")
_CerentDmx40LCard_ObjectIdentity = ObjectIdentity
cerentDmx40LCard = _CerentDmx40LCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4235)
)
if mibBuilder.loadTexts:
    cerentDmx40LCard.setStatus("current")
_CerentWxc40LCard_ObjectIdentity = ObjectIdentity
cerentWxc40LCard = _CerentWxc40LCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4240)
)
if mibBuilder.loadTexts:
    cerentWxc40LCard.setStatus("current")
_CerentIlkPort_ObjectIdentity = ObjectIdentity
cerentIlkPort = _CerentIlkPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4245)
)
if mibBuilder.loadTexts:
    cerentIlkPort.setStatus("current")
_CerentOc192Card4PortsDwdm_ObjectIdentity = ObjectIdentity
cerentOc192Card4PortsDwdm = _CerentOc192Card4PortsDwdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4250)
)
if mibBuilder.loadTexts:
    cerentOc192Card4PortsDwdm.setStatus("current")
_CerentOptAmpCCard_ObjectIdentity = ObjectIdentity
cerentOptAmpCCard = _CerentOptAmpCCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4255)
)
if mibBuilder.loadTexts:
    cerentOptAmpCCard.setStatus("current")
_CerentWssCE40Card_ObjectIdentity = ObjectIdentity
cerentWssCE40Card = _CerentWssCE40Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4260)
)
if mibBuilder.loadTexts:
    cerentWssCE40Card.setStatus("current")
_CerentDmxCE40Card_ObjectIdentity = ObjectIdentity
cerentDmxCE40Card = _CerentDmxCE40Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4265)
)
if mibBuilder.loadTexts:
    cerentDmxCE40Card.setStatus("current")
_CerentMxpMr10DmexCard_ObjectIdentity = ObjectIdentity
cerentMxpMr10DmexCard = _CerentMxpMr10DmexCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4270)
)
if mibBuilder.loadTexts:
    cerentMxpMr10DmexCard.setStatus("current")
_CerentMrc25G12LineCard_ObjectIdentity = ObjectIdentity
cerentMrc25G12LineCard = _CerentMrc25G12LineCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4275)
)
if mibBuilder.loadTexts:
    cerentMrc25G12LineCard.setStatus("current")
_CerentMrc25G4LineCard_ObjectIdentity = ObjectIdentity
cerentMrc25G4LineCard = _CerentMrc25G4LineCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4280)
)
if mibBuilder.loadTexts:
    cerentMrc25G4LineCard.setStatus("current")
_CerentPSMCard_ObjectIdentity = ObjectIdentity
cerentPSMCard = _CerentPSMCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4282)
)
if mibBuilder.loadTexts:
    cerentPSMCard.setStatus("current")
_CerentOptRAmpCCard_ObjectIdentity = ObjectIdentity
cerentOptRAmpCCard = _CerentOptRAmpCCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4285)
)
if mibBuilder.loadTexts:
    cerentOptRAmpCCard.setStatus("current")
_CerentOptRAmpECard_ObjectIdentity = ObjectIdentity
cerentOptRAmpECard = _CerentOptRAmpECard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4287)
)
if mibBuilder.loadTexts:
    cerentOptRAmpECard.setStatus("current")
_CerentXP10G4LineCard_ObjectIdentity = ObjectIdentity
cerentXP10G4LineCard = _CerentXP10G4LineCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4290)
)
if mibBuilder.loadTexts:
    cerentXP10G4LineCard.setStatus("current")
_CerentE121E3DS33LineCard_ObjectIdentity = ObjectIdentity
cerentE121E3DS33LineCard = _CerentE121E3DS33LineCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4295)
)
if mibBuilder.loadTexts:
    cerentE121E3DS33LineCard.setStatus("current")
_CerentE163E3DS33LineCard_ObjectIdentity = ObjectIdentity
cerentE163E3DS33LineCard = _CerentE163E3DS33LineCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4300)
)
if mibBuilder.loadTexts:
    cerentE163E3DS33LineCard.setStatus("current")
_Cerent40SMR1Card_ObjectIdentity = ObjectIdentity
cerent40SMR1Card = _Cerent40SMR1Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4305)
)
if mibBuilder.loadTexts:
    cerent40SMR1Card.setStatus("current")
_Cerent40SMR2Card_ObjectIdentity = ObjectIdentity
cerent40SMR2Card = _Cerent40SMR2Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4310)
)
if mibBuilder.loadTexts:
    cerent40SMR2Card.setStatus("current")
_CerentOptWxc80ChCard_ObjectIdentity = ObjectIdentity
cerentOptWxc80ChCard = _CerentOptWxc80ChCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4315)
)
if mibBuilder.loadTexts:
    cerentOptWxc80ChCard.setStatus("current")
_CerentMd40OddPassiveUnit_ObjectIdentity = ObjectIdentity
cerentMd40OddPassiveUnit = _CerentMd40OddPassiveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4320)
)
if mibBuilder.loadTexts:
    cerentMd40OddPassiveUnit.setStatus("current")
_CerentMd40EvenPassiveUnit_ObjectIdentity = ObjectIdentity
cerentMd40EvenPassiveUnit = _CerentMd40EvenPassiveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4325)
)
if mibBuilder.loadTexts:
    cerentMd40EvenPassiveUnit.setStatus("current")
_CerentMdId50PassiveUnit_ObjectIdentity = ObjectIdentity
cerentMdId50PassiveUnit = _CerentMdId50PassiveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4330)
)
if mibBuilder.loadTexts:
    cerentMdId50PassiveUnit.setStatus("current")
_CerentPP4SMRPassiveUnit_ObjectIdentity = ObjectIdentity
cerentPP4SMRPassiveUnit = _CerentPP4SMRPassiveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4335)
)
if mibBuilder.loadTexts:
    cerentPP4SMRPassiveUnit.setStatus("current")
_CerentPPMESH4PassiveUnit_ObjectIdentity = ObjectIdentity
cerentPPMESH4PassiveUnit = _CerentPPMESH4PassiveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4340)
)
if mibBuilder.loadTexts:
    cerentPPMESH4PassiveUnit.setStatus("current")
_CerentPPMESH8PassiveUnit_ObjectIdentity = ObjectIdentity
cerentPPMESH8PassiveUnit = _CerentPPMESH8PassiveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4345)
)
if mibBuilder.loadTexts:
    cerentPPMESH8PassiveUnit.setStatus("current")
_CerentDcuPassiveUnit_ObjectIdentity = ObjectIdentity
cerentDcuPassiveUnit = _CerentDcuPassiveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4350)
)
if mibBuilder.loadTexts:
    cerentDcuPassiveUnit.setStatus("current")
_CerentCTDcuPassiveUnit_ObjectIdentity = ObjectIdentity
cerentCTDcuPassiveUnit = _CerentCTDcuPassiveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4355)
)
if mibBuilder.loadTexts:
    cerentCTDcuPassiveUnit.setStatus("current")
_CerentFTDcuPassiveUnit_ObjectIdentity = ObjectIdentity
cerentFTDcuPassiveUnit = _CerentFTDcuPassiveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4360)
)
if mibBuilder.loadTexts:
    cerentFTDcuPassiveUnit.setStatus("current")
_FortyGePort_ObjectIdentity = ObjectIdentity
fortyGePort = _FortyGePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4365)
)
if mibBuilder.loadTexts:
    fortyGePort.setStatus("current")
_Fc8gPort_ObjectIdentity = ObjectIdentity
fc8gPort = _Fc8gPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4370)
)
if mibBuilder.loadTexts:
    fc8gPort.setStatus("current")
_CerentOtu3Port_ObjectIdentity = ObjectIdentity
cerentOtu3Port = _CerentOtu3Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4375)
)
if mibBuilder.loadTexts:
    cerentOtu3Port.setStatus("current")
_CerentOc768Port_ObjectIdentity = ObjectIdentity
cerentOc768Port = _CerentOc768Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4380)
)
if mibBuilder.loadTexts:
    cerentOc768Port.setStatus("current")
_CerentMechanicalUnit_ObjectIdentity = ObjectIdentity
cerentMechanicalUnit = _CerentMechanicalUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4385)
)
if mibBuilder.loadTexts:
    cerentMechanicalUnit.setStatus("current")
_Cerent40GTxpCard_ObjectIdentity = ObjectIdentity
cerent40GTxpCard = _Cerent40GTxpCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4390)
)
if mibBuilder.loadTexts:
    cerent40GTxpCard.setStatus("current")
_Cerent40GMxpCard_ObjectIdentity = ObjectIdentity
cerent40GMxpCard = _Cerent40GMxpCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4395)
)
if mibBuilder.loadTexts:
    cerent40GMxpCard.setStatus("current")
_Cerent40EMxpCard_ObjectIdentity = ObjectIdentity
cerent40EMxpCard = _Cerent40EMxpCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4400)
)
if mibBuilder.loadTexts:
    cerent40EMxpCard.setStatus("current")
_Cerent15216ID50PassiveUnit_ObjectIdentity = ObjectIdentity
cerent15216ID50PassiveUnit = _Cerent15216ID50PassiveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4405)
)
if mibBuilder.loadTexts:
    cerent15216ID50PassiveUnit.setStatus("current")
_Cerent40ETxpCard_ObjectIdentity = ObjectIdentity
cerent40ETxpCard = _Cerent40ETxpCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4415)
)
if mibBuilder.loadTexts:
    cerent40ETxpCard.setStatus("current")
_CerentOptEdfa17Card_ObjectIdentity = ObjectIdentity
cerentOptEdfa17Card = _CerentOptEdfa17Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4420)
)
if mibBuilder.loadTexts:
    cerentOptEdfa17Card.setStatus("current")
_CerentOptEdfa24Card_ObjectIdentity = ObjectIdentity
cerentOptEdfa24Card = _CerentOptEdfa24Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4425)
)
if mibBuilder.loadTexts:
    cerentOptEdfa24Card.setStatus("current")
_CerentBackPlaneM2_ObjectIdentity = ObjectIdentity
cerentBackPlaneM2 = _CerentBackPlaneM2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4510)
)
if mibBuilder.loadTexts:
    cerentBackPlaneM2.setStatus("current")
_CerentChassisM2Ansi_ObjectIdentity = ObjectIdentity
cerentChassisM2Ansi = _CerentChassisM2Ansi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4520)
)
if mibBuilder.loadTexts:
    cerentChassisM2Ansi.setStatus("current")
_CerentChassisM2Etsi_ObjectIdentity = ObjectIdentity
cerentChassisM2Etsi = _CerentChassisM2Etsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4530)
)
if mibBuilder.loadTexts:
    cerentChassisM2Etsi.setStatus("current")
_CerentArXpCard_ObjectIdentity = ObjectIdentity
cerentArXpCard = _CerentArXpCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4535)
)
if mibBuilder.loadTexts:
    cerentArXpCard.setStatus("current")
_CerentBackPlaneM6_ObjectIdentity = ObjectIdentity
cerentBackPlaneM6 = _CerentBackPlaneM6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4540)
)
if mibBuilder.loadTexts:
    cerentBackPlaneM6.setStatus("current")
_CerentArMxpCard_ObjectIdentity = ObjectIdentity
cerentArMxpCard = _CerentArMxpCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4545)
)
if mibBuilder.loadTexts:
    cerentArMxpCard.setStatus("current")
_CerentChassisM6Ansi_ObjectIdentity = ObjectIdentity
cerentChassisM6Ansi = _CerentChassisM6Ansi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4550)
)
if mibBuilder.loadTexts:
    cerentChassisM6Ansi.setStatus("current")
_CerentChassisM6Etsi_ObjectIdentity = ObjectIdentity
cerentChassisM6Etsi = _CerentChassisM6Etsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4560)
)
if mibBuilder.loadTexts:
    cerentChassisM6Etsi.setStatus("current")
_CerentPowerSupplyUts_ObjectIdentity = ObjectIdentity
cerentPowerSupplyUts = _CerentPowerSupplyUts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4570)
)
if mibBuilder.loadTexts:
    cerentPowerSupplyUts.setStatus("current")
_CerentFlashUts_ObjectIdentity = ObjectIdentity
cerentFlashUts = _CerentFlashUts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4580)
)
if mibBuilder.loadTexts:
    cerentFlashUts.setStatus("current")
_CerentAicInUts_ObjectIdentity = ObjectIdentity
cerentAicInUts = _CerentAicInUts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4590)
)
if mibBuilder.loadTexts:
    cerentAicInUts.setStatus("current")
_CerentAicOutUts_ObjectIdentity = ObjectIdentity
cerentAicOutUts = _CerentAicOutUts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4600)
)
if mibBuilder.loadTexts:
    cerentAicOutUts.setStatus("current")
_CerentIscEqptUts_ObjectIdentity = ObjectIdentity
cerentIscEqptUts = _CerentIscEqptUts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4610)
)
if mibBuilder.loadTexts:
    cerentIscEqptUts.setStatus("current")
_CerentUdcVoipEmsUts_ObjectIdentity = ObjectIdentity
cerentUdcVoipEmsUts = _CerentUdcVoipEmsUts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4620)
)
if mibBuilder.loadTexts:
    cerentUdcVoipEmsUts.setStatus("current")
_CerentBitsUts_ObjectIdentity = ObjectIdentity
cerentBitsUts = _CerentBitsUts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4630)
)
if mibBuilder.loadTexts:
    cerentBitsUts.setStatus("current")
_CerentFanTrayUts_ObjectIdentity = ObjectIdentity
cerentFanTrayUts = _CerentFanTrayUts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4640)
)
if mibBuilder.loadTexts:
    cerentFanTrayUts.setStatus("current")
_CerentAlarmDryContactUts_ObjectIdentity = ObjectIdentity
cerentAlarmDryContactUts = _CerentAlarmDryContactUts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4645)
)
if mibBuilder.loadTexts:
    cerentAlarmDryContactUts.setStatus("current")
_CerentUsbUts_ObjectIdentity = ObjectIdentity
cerentUsbUts = _CerentUsbUts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4650)
)
if mibBuilder.loadTexts:
    cerentUsbUts.setStatus("current")
_CerentUsbUtsPortCard_ObjectIdentity = ObjectIdentity
cerentUsbUtsPortCard = _CerentUsbUtsPortCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4655)
)
if mibBuilder.loadTexts:
    cerentUsbUtsPortCard.setStatus("current")
_CerentIoUts_ObjectIdentity = ObjectIdentity
cerentIoUts = _CerentIoUts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4660)
)
if mibBuilder.loadTexts:
    cerentIoUts.setStatus("current")
_CerentEcuTray_ObjectIdentity = ObjectIdentity
cerentEcuTray = _CerentEcuTray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4670)
)
if mibBuilder.loadTexts:
    cerentEcuTray.setStatus("current")
_CerentTncUtsCard_ObjectIdentity = ObjectIdentity
cerentTncUtsCard = _CerentTncUtsCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4680)
)
if mibBuilder.loadTexts:
    cerentTncUtsCard.setStatus("current")
_CerentTscUtsCard_ObjectIdentity = ObjectIdentity
cerentTscUtsCard = _CerentTscUtsCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4690)
)
if mibBuilder.loadTexts:
    cerentTscUtsCard.setStatus("current")
_CerentTncTscUtsSlot_ObjectIdentity = ObjectIdentity
cerentTncTscUtsSlot = _CerentTncTscUtsSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4700)
)
if mibBuilder.loadTexts:
    cerentTncTscUtsSlot.setStatus("current")
_CerentEcuSlot_ObjectIdentity = ObjectIdentity
cerentEcuSlot = _CerentEcuSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4710)
)
if mibBuilder.loadTexts:
    cerentEcuSlot.setStatus("current")
_CerentMscIscUtsPort_ObjectIdentity = ObjectIdentity
cerentMscIscUtsPort = _CerentMscIscUtsPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4720)
)
if mibBuilder.loadTexts:
    cerentMscIscUtsPort.setStatus("current")
_CerentOtu1Port_ObjectIdentity = ObjectIdentity
cerentOtu1Port = _CerentOtu1Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4725)
)
if mibBuilder.loadTexts:
    cerentOtu1Port.setStatus("current")
_CerentTncFePort_ObjectIdentity = ObjectIdentity
cerentTncFePort = _CerentTncFePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4730)
)
if mibBuilder.loadTexts:
    cerentTncFePort.setStatus("current")
_CerentIsc3stp1gPort_ObjectIdentity = ObjectIdentity
cerentIsc3stp1gPort = _CerentIsc3stp1gPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4732)
)
if mibBuilder.loadTexts:
    cerentIsc3stp1gPort.setStatus("current")
_CerentIsc3stp2gPort_ObjectIdentity = ObjectIdentity
cerentIsc3stp2gPort = _CerentIsc3stp2gPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4735)
)
if mibBuilder.loadTexts:
    cerentIsc3stp2gPort.setStatus("current")
_CerentPtSystem_ObjectIdentity = ObjectIdentity
cerentPtSystem = _CerentPtSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4740)
)
if mibBuilder.loadTexts:
    cerentPtSystem.setStatus("current")
_CerentSdi3gvideoPort_ObjectIdentity = ObjectIdentity
cerentSdi3gvideoPort = _CerentSdi3gvideoPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4742)
)
if mibBuilder.loadTexts:
    cerentSdi3gvideoPort.setStatus("current")
_CerentPtf10GECard_ObjectIdentity = ObjectIdentity
cerentPtf10GECard = _CerentPtf10GECard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4745)
)
if mibBuilder.loadTexts:
    cerentPtf10GECard.setStatus("current")
_CerentAutoPort_ObjectIdentity = ObjectIdentity
cerentAutoPort = _CerentAutoPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4747)
)
if mibBuilder.loadTexts:
    cerentAutoPort.setStatus("current")
_CerentPt10GECard_ObjectIdentity = ObjectIdentity
cerentPt10GECard = _CerentPt10GECard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4750)
)
if mibBuilder.loadTexts:
    cerentPt10GECard.setStatus("current")
_CerentPtsaGECard_ObjectIdentity = ObjectIdentity
cerentPtsaGECard = _CerentPtsaGECard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4755)
)
if mibBuilder.loadTexts:
    cerentPtsaGECard.setStatus("current")
_CerentFld303PassiveUnit_ObjectIdentity = ObjectIdentity
cerentFld303PassiveUnit = _CerentFld303PassiveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4760)
)
if mibBuilder.loadTexts:
    cerentFld303PassiveUnit.setStatus("current")
_CerentFld334PassiveUnit_ObjectIdentity = ObjectIdentity
cerentFld334PassiveUnit = _CerentFld334PassiveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4765)
)
if mibBuilder.loadTexts:
    cerentFld334PassiveUnit.setStatus("current")
_CerentFld366PassiveUnit_ObjectIdentity = ObjectIdentity
cerentFld366PassiveUnit = _CerentFld366PassiveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4770)
)
if mibBuilder.loadTexts:
    cerentFld366PassiveUnit.setStatus("current")
_CerentFld397PassiveUnit_ObjectIdentity = ObjectIdentity
cerentFld397PassiveUnit = _CerentFld397PassiveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4775)
)
if mibBuilder.loadTexts:
    cerentFld397PassiveUnit.setStatus("current")
_CerentFld429PassiveUnit_ObjectIdentity = ObjectIdentity
cerentFld429PassiveUnit = _CerentFld429PassiveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4780)
)
if mibBuilder.loadTexts:
    cerentFld429PassiveUnit.setStatus("current")
_CerentFld461PassiveUnit_ObjectIdentity = ObjectIdentity
cerentFld461PassiveUnit = _CerentFld461PassiveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4785)
)
if mibBuilder.loadTexts:
    cerentFld461PassiveUnit.setStatus("current")
_CerentFld493PassiveUnit_ObjectIdentity = ObjectIdentity
cerentFld493PassiveUnit = _CerentFld493PassiveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4790)
)
if mibBuilder.loadTexts:
    cerentFld493PassiveUnit.setStatus("current")
_CerentFld525PassiveUnit_ObjectIdentity = ObjectIdentity
cerentFld525PassiveUnit = _CerentFld525PassiveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4795)
)
if mibBuilder.loadTexts:
    cerentFld525PassiveUnit.setStatus("current")
_CerentFld557PassiveUnit_ObjectIdentity = ObjectIdentity
cerentFld557PassiveUnit = _CerentFld557PassiveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4800)
)
if mibBuilder.loadTexts:
    cerentFld557PassiveUnit.setStatus("current")
_CerentFld589PassiveUnit_ObjectIdentity = ObjectIdentity
cerentFld589PassiveUnit = _CerentFld589PassiveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4805)
)
if mibBuilder.loadTexts:
    cerentFld589PassiveUnit.setStatus("current")
_CerentFldOscPassiveUnit_ObjectIdentity = ObjectIdentity
cerentFldOscPassiveUnit = _CerentFldOscPassiveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4810)
)
if mibBuilder.loadTexts:
    cerentFldOscPassiveUnit.setStatus("current")
_CerentFlcCwdm8PassiveUnit_ObjectIdentity = ObjectIdentity
cerentFlcCwdm8PassiveUnit = _CerentFlcCwdm8PassiveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4815)
)
if mibBuilder.loadTexts:
    cerentFlcCwdm8PassiveUnit.setStatus("current")
_CerentSdsdiPort_ObjectIdentity = ObjectIdentity
cerentSdsdiPort = _CerentSdsdiPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4820)
)
if mibBuilder.loadTexts:
    cerentSdsdiPort.setStatus("current")
_CerentHdsdiPort_ObjectIdentity = ObjectIdentity
cerentHdsdiPort = _CerentHdsdiPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4825)
)
if mibBuilder.loadTexts:
    cerentHdsdiPort.setStatus("current")
_CerentOptRampCTPCard_ObjectIdentity = ObjectIdentity
cerentOptRampCTPCard = _CerentOptRampCTPCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4830)
)
if mibBuilder.loadTexts:
    cerentOptRampCTPCard.setStatus("current")
_CerentOptRampCOPCard_ObjectIdentity = ObjectIdentity
cerentOptRampCOPCard = _CerentOptRampCOPCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4835)
)
if mibBuilder.loadTexts:
    cerentOptRampCOPCard.setStatus("current")
_CerentFbgdcu165PassiveUnit_ObjectIdentity = ObjectIdentity
cerentFbgdcu165PassiveUnit = _CerentFbgdcu165PassiveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4840)
)
if mibBuilder.loadTexts:
    cerentFbgdcu165PassiveUnit.setStatus("current")
_CerentFbgdcu331PassiveUnit_ObjectIdentity = ObjectIdentity
cerentFbgdcu331PassiveUnit = _CerentFbgdcu331PassiveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4845)
)
if mibBuilder.loadTexts:
    cerentFbgdcu331PassiveUnit.setStatus("current")
_CerentFbgdcu496PassiveUnit_ObjectIdentity = ObjectIdentity
cerentFbgdcu496PassiveUnit = _CerentFbgdcu496PassiveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4850)
)
if mibBuilder.loadTexts:
    cerentFbgdcu496PassiveUnit.setStatus("current")
_CerentFbgdcu661PassiveUnit_ObjectIdentity = ObjectIdentity
cerentFbgdcu661PassiveUnit = _CerentFbgdcu661PassiveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4855)
)
if mibBuilder.loadTexts:
    cerentFbgdcu661PassiveUnit.setStatus("current")
_CerentFbgdcu826PassiveUnit_ObjectIdentity = ObjectIdentity
cerentFbgdcu826PassiveUnit = _CerentFbgdcu826PassiveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4860)
)
if mibBuilder.loadTexts:
    cerentFbgdcu826PassiveUnit.setStatus("current")
_CerentFbgdcu992PassiveUnit_ObjectIdentity = ObjectIdentity
cerentFbgdcu992PassiveUnit = _CerentFbgdcu992PassiveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4865)
)
if mibBuilder.loadTexts:
    cerentFbgdcu992PassiveUnit.setStatus("current")
_CerentFbgdcu1157PassiveUnit_ObjectIdentity = ObjectIdentity
cerentFbgdcu1157PassiveUnit = _CerentFbgdcu1157PassiveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4870)
)
if mibBuilder.loadTexts:
    cerentFbgdcu1157PassiveUnit.setStatus("current")
_CerentFbgdcu1322PassiveUnit_ObjectIdentity = ObjectIdentity
cerentFbgdcu1322PassiveUnit = _CerentFbgdcu1322PassiveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4875)
)
if mibBuilder.loadTexts:
    cerentFbgdcu1322PassiveUnit.setStatus("current")
_CerentFbgdcu1653PassiveUnit_ObjectIdentity = ObjectIdentity
cerentFbgdcu1653PassiveUnit = _CerentFbgdcu1653PassiveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4880)
)
if mibBuilder.loadTexts:
    cerentFbgdcu1653PassiveUnit.setStatus("current")
_CerentFbgdcu1983PassiveUnit_ObjectIdentity = ObjectIdentity
cerentFbgdcu1983PassiveUnit = _CerentFbgdcu1983PassiveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4885)
)
if mibBuilder.loadTexts:
    cerentFbgdcu1983PassiveUnit.setStatus("current")
_CerentMd48OddPassiveUnit_ObjectIdentity = ObjectIdentity
cerentMd48OddPassiveUnit = _CerentMd48OddPassiveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4900)
)
if mibBuilder.loadTexts:
    cerentMd48OddPassiveUnit.setStatus("current")
_CerentMd48EvenPassiveUnit_ObjectIdentity = ObjectIdentity
cerentMd48EvenPassiveUnit = _CerentMd48EvenPassiveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4905)
)
if mibBuilder.loadTexts:
    cerentMd48EvenPassiveUnit.setStatus("current")
_CerentMd48CmPassiveUnit_ObjectIdentity = ObjectIdentity
cerentMd48CmPassiveUnit = _CerentMd48CmPassiveUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4910)
)
if mibBuilder.loadTexts:
    cerentMd48CmPassiveUnit.setStatus("current")
_CerentOtu4Port_ObjectIdentity = ObjectIdentity
cerentOtu4Port = _CerentOtu4Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4915)
)
if mibBuilder.loadTexts:
    cerentOtu4Port.setStatus("current")
_CerentOneHundredGePort_ObjectIdentity = ObjectIdentity
cerentOneHundredGePort = _CerentOneHundredGePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4920)
)
if mibBuilder.loadTexts:
    cerentOneHundredGePort.setStatus("current")
_CerentHundredGigLineCard_ObjectIdentity = ObjectIdentity
cerentHundredGigLineCard = _CerentHundredGigLineCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4925)
)
if mibBuilder.loadTexts:
    cerentHundredGigLineCard.setStatus("current")
_CerentTENxTENGigLineCard_ObjectIdentity = ObjectIdentity
cerentTENxTENGigLineCard = _CerentTENxTENGigLineCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4930)
)
if mibBuilder.loadTexts:
    cerentTENxTENGigLineCard.setStatus("current")
_CerentCfpLineCard_ObjectIdentity = ObjectIdentity
cerentCfpLineCard = _CerentCfpLineCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4935)
)
if mibBuilder.loadTexts:
    cerentCfpLineCard.setStatus("current")
_CerentOTLPort_ObjectIdentity = ObjectIdentity
cerentOTLPort = _CerentOTLPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4940)
)
if mibBuilder.loadTexts:
    cerentOTLPort.setStatus("current")
_CerentHundredgigPlim_ObjectIdentity = ObjectIdentity
cerentHundredgigPlim = _CerentHundredgigPlim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4945)
)
if mibBuilder.loadTexts:
    cerentHundredgigPlim.setStatus("current")
_CerentWseLineCard_ObjectIdentity = ObjectIdentity
cerentWseLineCard = _CerentWseLineCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4947)
)
if mibBuilder.loadTexts:
    cerentWseLineCard.setStatus("current")
_CerentArXpeCard_ObjectIdentity = ObjectIdentity
cerentArXpeCard = _CerentArXpeCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4950)
)
if mibBuilder.loadTexts:
    cerentArXpeCard.setStatus("current")
_CerentEDRA126C_ObjectIdentity = ObjectIdentity
cerentEDRA126C = _CerentEDRA126C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4955)
)
if mibBuilder.loadTexts:
    cerentEDRA126C.setStatus("current")
_CerentEDRA135C_ObjectIdentity = ObjectIdentity
cerentEDRA135C = _CerentEDRA135C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4960)
)
if mibBuilder.loadTexts:
    cerentEDRA135C.setStatus("current")
_CerentEDRA226C_ObjectIdentity = ObjectIdentity
cerentEDRA226C = _CerentEDRA226C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4965)
)
if mibBuilder.loadTexts:
    cerentEDRA226C.setStatus("current")
_CerentEDRA235C_ObjectIdentity = ObjectIdentity
cerentEDRA235C = _CerentEDRA235C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4970)
)
if mibBuilder.loadTexts:
    cerentEDRA235C.setStatus("current")
_CerentWXC16FSLineCard_ObjectIdentity = ObjectIdentity
cerentWXC16FSLineCard = _CerentWXC16FSLineCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4975)
)
if mibBuilder.loadTexts:
    cerentWXC16FSLineCard.setStatus("current")
_CerentPassiv1x16COFSC_ObjectIdentity = ObjectIdentity
cerentPassiv1x16COFSC = _CerentPassiv1x16COFSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4980)
)
if mibBuilder.loadTexts:
    cerentPassiv1x16COFSC.setStatus("current")
_CerentPassive4x4COFSC_ObjectIdentity = ObjectIdentity
cerentPassive4x4COFSC = _CerentPassive4x4COFSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4985)
)
if mibBuilder.loadTexts:
    cerentPassive4x4COFSC.setStatus("current")
_CerentPassiveMODDEG5_ObjectIdentity = ObjectIdentity
cerentPassiveMODDEG5 = _CerentPassiveMODDEG5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4990)
)
if mibBuilder.loadTexts:
    cerentPassiveMODDEG5.setStatus("current")
_CerentPassiveMODUPG4_ObjectIdentity = ObjectIdentity
cerentPassiveMODUPG4 = _CerentPassiveMODUPG4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 4995)
)
if mibBuilder.loadTexts:
    cerentPassiveMODUPG4.setStatus("current")
_CerentPassiveMPO8LCADPT_ObjectIdentity = ObjectIdentity
cerentPassiveMPO8LCADPT = _CerentPassiveMPO8LCADPT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 5000)
)
if mibBuilder.loadTexts:
    cerentPassiveMPO8LCADPT.setStatus("current")
_CerentPassiveASTEDFA_ObjectIdentity = ObjectIdentity
cerentPassiveASTEDFA = _CerentPassiveASTEDFA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 5005)
)
if mibBuilder.loadTexts:
    cerentPassiveASTEDFA.setStatus("current")
_CerentCPAK100GLineCard_ObjectIdentity = ObjectIdentity
cerentCPAK100GLineCard = _CerentCPAK100GLineCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 30, 5010)
)
if mibBuilder.loadTexts:
    cerentCPAK100GLineCard.setStatus("current")
_CerentGeneric_ObjectIdentity = ObjectIdentity
cerentGeneric = _CerentGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 2)
)
if mibBuilder.loadTexts:
    cerentGeneric.setStatus("current")
_CerentGenericDummyObjects_ObjectIdentity = ObjectIdentity
cerentGenericDummyObjects = _CerentGenericDummyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 2, 1)
)
if mibBuilder.loadTexts:
    cerentGenericDummyObjects.setStatus("current")
_CerentExperimental_ObjectIdentity = ObjectIdentity
cerentExperimental = _CerentExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 3)
)
if mibBuilder.loadTexts:
    cerentExperimental.setStatus("current")
_CerentAgentCapabilities_ObjectIdentity = ObjectIdentity
cerentAgentCapabilities = _CerentAgentCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 4)
)
if mibBuilder.loadTexts:
    cerentAgentCapabilities.setStatus("current")
_CerentRequirements_ObjectIdentity = ObjectIdentity
cerentRequirements = _CerentRequirements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 5)
)
if mibBuilder.loadTexts:
    cerentRequirements.setStatus("current")
_CerentProducts_ObjectIdentity = ObjectIdentity
cerentProducts = _CerentProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 6)
)
if mibBuilder.loadTexts:
    cerentProducts.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CERENT-GLOBAL-REGISTRY",
    **{"cerent": cerent,
       "cerentRegistry": cerentRegistry,
       "cerentModules": cerentModules,
       "cerentGlobalRegModule": cerentGlobalRegModule,
       "cerentCommunicationEquipment": cerentCommunicationEquipment,
       "cerentADMs": cerentADMs,
       "cerent454Node": cerent454Node,
       "cerent327Node": cerent327Node,
       "cerent600Node": cerent600Node,
       "cerent310Node": cerent310Node,
       "cerent310MaAnsiNode": cerent310MaAnsiNode,
       "cerent310MaEtsiNode": cerent310MaEtsiNode,
       "cerent454M6Node": cerent454M6Node,
       "cerent454M2Node": cerent454M2Node,
       "cerentDwdmDevices": cerentDwdmDevices,
       "cerent15216OpmNode": cerent15216OpmNode,
       "cerent15216EdfaNode": cerent15216EdfaNode,
       "cerentComponents": cerentComponents,
       "cerentOtherComponent": cerentOtherComponent,
       "cerentTcc": cerentTcc,
       "cerentXc": cerentXc,
       "cerentDs114": cerentDs114,
       "cerentDs1n14": cerentDs1n14,
       "cerentDs312": cerentDs312,
       "cerentOc3ir": cerentOc3ir,
       "cerentOc12ir": cerentOc12ir,
       "cerentOc12lr1310": cerentOc12lr1310,
       "cerentOc48ir": cerentOc48ir,
       "cerentOc48lr": cerentOc48lr,
       "cerentFanTray": cerentFanTray,
       "cerentFanSlot": cerentFanSlot,
       "cerentIoSlot": cerentIoSlot,
       "cerentXcSlot": cerentXcSlot,
       "cerentAicSlot": cerentAicSlot,
       "cerentTccSlot": cerentTccSlot,
       "cerentBackPlane454": cerentBackPlane454,
       "cerentChassis454": cerentChassis454,
       "cerentDs3nCard": cerentDs3nCard,
       "cerentDs3XmCard": cerentDs3XmCard,
       "cerentOc3Card": cerentOc3Card,
       "cerentOc3OctaCard": cerentOc3OctaCard,
       "cerentOc12Card": cerentOc12Card,
       "cerentOc48Card": cerentOc48Card,
       "cerentEc1Card": cerentEc1Card,
       "cerentEc1nCard": cerentEc1nCard,
       "cerentEpos100Card": cerentEpos100Card,
       "cerentEpos1000Card": cerentEpos1000Card,
       "cerentAicCard": cerentAicCard,
       "cerentXcVtCard": cerentXcVtCard,
       "cerentEther1000Port": cerentEther1000Port,
       "cerentEther100Port": cerentEther100Port,
       "cerentDs1VtMappedPort": cerentDs1VtMappedPort,
       "cerentDs3XmPort": cerentDs3XmPort,
       "cerentDs3Port": cerentDs3Port,
       "cerentEc1Port": cerentEc1Port,
       "cerentOc3Port": cerentOc3Port,
       "cerentOc12Port": cerentOc12Port,
       "cerentOc48Port": cerentOc48Port,
       "cerentOrderwirePort": cerentOrderwirePort,
       "cerentSensorComponent": cerentSensorComponent,
       "cerentChassis15327": cerentChassis15327,
       "cerentBackPlane15327": cerentBackPlane15327,
       "cerentXtcCard": cerentXtcCard,
       "cerentMicCard": cerentMicCard,
       "cerentMicExtCard": cerentMicExtCard,
       "cerentXtcSlot": cerentXtcSlot,
       "cerentMicSlot": cerentMicSlot,
       "cerentVicEncoderLineCard": cerentVicEncoderLineCard,
       "cerentVicDecoderLineCard": cerentVicDecoderLineCard,
       "cerentVicEncoderPort": cerentVicEncoderPort,
       "cerentVicDecoderPort": cerentVicDecoderPort,
       "cerentVicTestPort": cerentVicTestPort,
       "cerentAip": cerentAip,
       "cerentBicSmb": cerentBicSmb,
       "cerentBicBnc": cerentBicBnc,
       "cerentFcb": cerentFcb,
       "cerentEnvironmentControl": cerentEnvironmentControl,
       "cerentLedIndicator": cerentLedIndicator,
       "cerentAudibleAlarm": cerentAudibleAlarm,
       "cerentXc10g": cerentXc10g,
       "cerentOc192Card": cerentOc192Card,
       "cerentOc192Port": cerentOc192Port,
       "cerentDs3eCard": cerentDs3eCard,
       "cerentDs3neCard": cerentDs3neCard,
       "cerent15216OpmChassis": cerent15216OpmChassis,
       "cerent15216OpmBackPlane": cerent15216OpmBackPlane,
       "cerent15216OpmSlot": cerent15216OpmSlot,
       "cerent15216OpmController": cerent15216OpmController,
       "cerent15216OpmSpectrometer": cerent15216OpmSpectrometer,
       "cerent15216OpmOpticalSwitch": cerent15216OpmOpticalSwitch,
       "cerent15216OpmOpticalPort": cerent15216OpmOpticalPort,
       "cerent15216OpmSerialPort": cerent15216OpmSerialPort,
       "cerent15216OpmLedIndicator": cerent15216OpmLedIndicator,
       "cerent15216OpmRelay": cerent15216OpmRelay,
       "cerent15216OpmPowerSupply": cerent15216OpmPowerSupply,
       "cerent15216OpmPcmciaSlot": cerent15216OpmPcmciaSlot,
       "cerentOc12QuadCard": cerentOc12QuadCard,
       "cerentG1000QuadCard": cerentG1000QuadCard,
       "cerentG1000Port": cerentG1000Port,
       "cerentMlEtherPort": cerentMlEtherPort,
       "cerentMlPosPort": cerentMlPosPort,
       "cerentG1000GenericCard": cerentG1000GenericCard,
       "cerentML100GenericCard": cerentML100GenericCard,
       "cerentML1000GenericCard": cerentML1000GenericCard,
       "cerentG1K4Card": cerentG1K4Card,
       "cerentOc192IrCard": cerentOc192IrCard,
       "cerentOc192LrCard": cerentOc192LrCard,
       "cerentOc192ItuCard": cerentOc192ItuCard,
       "cerentOc3n1Card": cerentOc3n1Card,
       "ape": ape,
       "oneGePort": oneGePort,
       "tenGePort": tenGePort,
       "esconPort": esconPort,
       "dv6000Port": dv6000Port,
       "cerentE1n14": cerentE1n14,
       "cerentBackPlane454SDH": cerentBackPlane454SDH,
       "cerentChassis454SDH": cerentChassis454SDH,
       "cerentDs3inCard": cerentDs3inCard,
       "cerentE312Card": cerentE312Card,
       "cerentE1Port": cerentE1Port,
       "cerentDs3iPort": cerentDs3iPort,
       "cerentE3Port": cerentE3Port,
       "cerentAlmPwrSlot": cerentAlmPwrSlot,
       "cerentCrftTmgSlot": cerentCrftTmgSlot,
       "cerentAlmPwr": cerentAlmPwr,
       "cerentCrftTmg": cerentCrftTmg,
       "cerentFmecDb": cerentFmecDb,
       "cerentFmecSmzE1": cerentFmecSmzE1,
       "cerentFmecBlank": cerentFmecBlank,
       "cerentXcVxlCard": cerentXcVxlCard,
       "cerentEfca454Sdh": cerentEfca454Sdh,
       "cerentFmecSlot": cerentFmecSlot,
       "cerentFmecSmzE3": cerentFmecSmzE3,
       "cerentDs3i": cerentDs3i,
       "cerent15216EdfaChassis": cerent15216EdfaChassis,
       "cerentAici": cerentAici,
       "cerentFudcPort": cerentFudcPort,
       "cerentDccPort": cerentDccPort,
       "cerentAiciAep": cerentAiciAep,
       "cerentAiciAie": cerentAiciAie,
       "cerentXcVxl25GCard": cerentXcVxl25GCard,
       "cerentE114": cerentE114,
       "cerentPIMSlot": cerentPIMSlot,
       "cerentPIM4PPM": cerentPIM4PPM,
       "cerentPPMSlot": cerentPPMSlot,
       "cerentPPM1Port": cerentPPM1Port,
       "cerentOptDemux32RChCard": cerentOptDemux32RChCard,
       "cerentOptWss32ChCard": cerentOptWss32ChCard,
       "cerentChassis15310ClOid": cerentChassis15310ClOid,
       "cerentChassis15310MaAnsiOid": cerentChassis15310MaAnsiOid,
       "cerentChassis15310MaEtsiOid": cerentChassis15310MaEtsiOid,
       "cerentBackplane15310ClOid": cerentBackplane15310ClOid,
       "cerentBackplane15310MaAnsiOid": cerentBackplane15310MaAnsiOid,
       "cerentBackplane15310MaEtsiOid": cerentBackplane15310MaEtsiOid,
       "cerentCtxCardOid": cerentCtxCardOid,
       "cerentBbeLineCardOid": cerentBbeLineCardOid,
       "cerentWbeLineCardOid": cerentWbeLineCardOid,
       "cerentCtxSlotOid": cerentCtxSlotOid,
       "cerentBbeSlotOid": cerentBbeSlotOid,
       "cerentWbeSlotOid": cerentWbeSlotOid,
       "cerentAsap4LineCardOid": cerentAsap4LineCardOid,
       "cerentMrc4LineCardOid": cerentMrc4LineCardOid,
       "cerent310CE100t8LineCardOid": cerent310CE100t8LineCardOid,
       "cerent310ML100t8LineCardOid": cerent310ML100t8LineCardOid,
       "cerentL1PPosPortOid": cerentL1PPosPortOid,
       "cerentL1PEtherPortOid": cerentL1PEtherPortOid,
       "fc10gPort": fc10gPort,
       "ficon1gport": ficon1gport,
       "ficon2gport": ficon2gport,
       "cerentOc192Card4Ports": cerentOc192Card4Ports,
       "cerentOc48Card8Ports": cerentOc48Card8Ports,
       "cerentOc48Card16Ports": cerentOc48Card16Ports,
       "cerent15600ControllerSlot": cerent15600ControllerSlot,
       "cerentTsc": cerentTsc,
       "cerentChassis600": cerentChassis600,
       "cerentBackPlane600": cerentBackPlane600,
       "cerentCap": cerentCap,
       "cerentCxc": cerentCxc,
       "cerentCxcSlot": cerentCxcSlot,
       "cerentFillerCard": cerentFillerCard,
       "cerentFcmrLineCard": cerentFcmrLineCard,
       "cerentFcmrPort": cerentFcmrPort,
       "cerentTxpd10ECard": cerentTxpd10ECard,
       "cerentMuxpd25G10ECard": cerentMuxpd25G10ECard,
       "cerentDs3Xm12Card": cerentDs3Xm12Card,
       "ds3Ec148LineCard": ds3Ec148LineCard,
       "gfpPort": gfpPort,
       "cerent454CE100t8LineCardOid": cerent454CE100t8LineCardOid,
       "bicUniv": bicUniv,
       "bicUnknown": bicUnknown,
       "sdiD1VideoPort": sdiD1VideoPort,
       "hdtvPort": hdtvPort,
       "passThruPort": passThruPort,
       "etrCloPort": etrCloPort,
       "iscPort": iscPort,
       "fc1gPort": fc1gPort,
       "fc2gPort": fc2gPort,
       "mrSlot": mrSlot,
       "isc3Port": isc3Port,
       "cerentDs1i14": cerentDs1i14,
       "cerentFmecDs1i14": cerentFmecDs1i14,
       "cerentBackPlane454HD": cerentBackPlane454HD,
       "cerentDs1E156LineCard": cerentDs1E156LineCard,
       "cerentMrc12LineCard": cerentMrc12LineCard,
       "cerentOc192XfpLineCard": cerentOc192XfpLineCard,
       "cerentPowerSupply": cerentPowerSupply,
       "cerentTxpd10GCard": cerentTxpd10GCard,
       "cerentTxpd25GCard": cerentTxpd25GCard,
       "cerentTxpdP25GCard": cerentTxpdP25GCard,
       "cerentMuxpd25G10GCard": cerentMuxpd25G10GCard,
       "cerentDwdmClientPort": cerentDwdmClientPort,
       "cerentDwdmTrunkPort": cerentDwdmTrunkPort,
       "cerentMuxpdMr25GCard": cerentMuxpdMr25GCard,
       "cerentMuxpdPMr25GCard": cerentMuxpdPMr25GCard,
       "cerentMm850Port": cerentMm850Port,
       "cerentSm1310Port": cerentSm1310Port,
       "cerentXcVxcCard": cerentXcVxcCard,
       "cerentXcVxc25GCard": cerentXcVxc25GCard,
       "cerentOptBstECard": cerentOptBstECard,
       "fc4gPort": fc4gPort,
       "ficon4gport": ficon4gport,
       "isc3Peer1gPort": isc3Peer1gPort,
       "isc3Peer2gPort": isc3Peer2gPort,
       "cerentOscmCard": cerentOscmCard,
       "cerentOscCsmCard": cerentOscCsmCard,
       "cerentOptPreCard": cerentOptPreCard,
       "cerentOptBstCard": cerentOptBstCard,
       "cerentOptDemux32ChCard": cerentOptDemux32ChCard,
       "cerentOptMux32ChCard": cerentOptMux32ChCard,
       "cerentOptMuxDemux4ChCard": cerentOptMuxDemux4ChCard,
       "cerentOadm1ChCard": cerentOadm1ChCard,
       "cerentOadm2ChCard": cerentOadm2ChCard,
       "cerentOadm4ChCard": cerentOadm4ChCard,
       "cerentOadm1BnCard": cerentOadm1BnCard,
       "cerentOadm4BnCard": cerentOadm4BnCard,
       "cerentOTSPort": cerentOTSPort,
       "cerentAOTSPort": cerentAOTSPort,
       "cerentOMSPort": cerentOMSPort,
       "cerentOCHPort": cerentOCHPort,
       "cerentE1P42LineCard": cerentE1P42LineCard,
       "cerentE1nP42LineCard": cerentE1nP42LineCard,
       "cerentFmecE1P42TypeUnprotW120Card": cerentFmecE1P42TypeUnprotW120Card,
       "cerentFmecE1P42Type1To3W120aCard": cerentFmecE1P42Type1To3W120aCard,
       "cerentFmecE1P42Type1To3W120bCard": cerentFmecE1P42Type1To3W120bCard,
       "cerentStm1e12LineCard": cerentStm1e12LineCard,
       "cerentStm1ePort": cerentStm1ePort,
       "cerentFmec155eUnprotCard": cerentFmec155eUnprotCard,
       "cerentFmec155e1To1Card": cerentFmec155e1To1Card,
       "cerentFmec155e1To3Card": cerentFmec155e1To3Card,
       "cerent15216Edfa3ShelfController": cerent15216Edfa3ShelfController,
       "cerent15216Edfa3OpticsModule": cerent15216Edfa3OpticsModule,
       "cerent15216EdfaEtherPort": cerent15216EdfaEtherPort,
       "cerent15216EdfaSerialPort": cerent15216EdfaSerialPort,
       "cerentMl100X8LineCard": cerentMl100X8LineCard,
       "cerentOptBstLCard": cerentOptBstLCard,
       "cerentOptAmpLCard": cerentOptAmpLCard,
       "cerentDmx32LCard": cerentDmx32LCard,
       "cerentWss32LCard": cerentWss32LCard,
       "cerentMMUCard": cerentMMUCard,
       "cerentMsIsc100tCard": cerentMsIsc100tCard,
       "cerentMxpMr10DmeCard": cerentMxpMr10DmeCard,
       "cerentCE1000Card": cerentCE1000Card,
       "cerentCE1000EtherPort": cerentCE1000EtherPort,
       "cerentCE1000PosPort": cerentCE1000PosPort,
       "cerentPIM1PPM": cerentPIM1PPM,
       "cerentCEMR454Card": cerentCEMR454Card,
       "cerentCEMR310Card": cerentCEMR310Card,
       "cerentCTX2500Card": cerentCTX2500Card,
       "cerentDs128Ds3EC13LineCard": cerentDs128Ds3EC13LineCard,
       "cerentDs184Ds3EC13LineCard": cerentDs184Ds3EC13LineCard,
       "cerentDs3EC16LineCard": cerentDs3EC16LineCard,
       "cerentBicTelco": cerentBicTelco,
       "cerentBicCmn": cerentBicCmn,
       "cerentRanSvcLineCard": cerentRanSvcLineCard,
       "cerentTxpd10EXCard": cerentTxpd10EXCard,
       "cerentTxpdP10EXCard": cerentTxpdP10EXCard,
       "cerentMuxpd25G10XCard": cerentMuxpd25G10XCard,
       "cerentOptAmp17Card": cerentOptAmp17Card,
       "cerentOptAmp23Card": cerentOptAmp23Card,
       "cerentOptWss40ChCard": cerentOptWss40ChCard,
       "cerentOptMux40ChCard": cerentOptMux40ChCard,
       "cerentOptDemux40ChCard": cerentOptDemux40ChCard,
       "cerentOptWxc40ChCard": cerentOptWxc40ChCard,
       "cerentXpd10GECard": cerentXpd10GECard,
       "cerentXpdGECard": cerentXpdGECard,
       "cerentOadm10GCard": cerentOadm10GCard,
       "cerentOtu2Port": cerentOtu2Port,
       "cerentWss40LCard": cerentWss40LCard,
       "cerentMux40LCard": cerentMux40LCard,
       "cerentDmx40LCard": cerentDmx40LCard,
       "cerentWxc40LCard": cerentWxc40LCard,
       "cerentIlkPort": cerentIlkPort,
       "cerentOc192Card4PortsDwdm": cerentOc192Card4PortsDwdm,
       "cerentOptAmpCCard": cerentOptAmpCCard,
       "cerentWssCE40Card": cerentWssCE40Card,
       "cerentDmxCE40Card": cerentDmxCE40Card,
       "cerentMxpMr10DmexCard": cerentMxpMr10DmexCard,
       "cerentMrc25G12LineCard": cerentMrc25G12LineCard,
       "cerentMrc25G4LineCard": cerentMrc25G4LineCard,
       "cerentPSMCard": cerentPSMCard,
       "cerentOptRAmpCCard": cerentOptRAmpCCard,
       "cerentOptRAmpECard": cerentOptRAmpECard,
       "cerentXP10G4LineCard": cerentXP10G4LineCard,
       "cerentE121E3DS33LineCard": cerentE121E3DS33LineCard,
       "cerentE163E3DS33LineCard": cerentE163E3DS33LineCard,
       "cerent40SMR1Card": cerent40SMR1Card,
       "cerent40SMR2Card": cerent40SMR2Card,
       "cerentOptWxc80ChCard": cerentOptWxc80ChCard,
       "cerentMd40OddPassiveUnit": cerentMd40OddPassiveUnit,
       "cerentMd40EvenPassiveUnit": cerentMd40EvenPassiveUnit,
       "cerentMdId50PassiveUnit": cerentMdId50PassiveUnit,
       "cerentPP4SMRPassiveUnit": cerentPP4SMRPassiveUnit,
       "cerentPPMESH4PassiveUnit": cerentPPMESH4PassiveUnit,
       "cerentPPMESH8PassiveUnit": cerentPPMESH8PassiveUnit,
       "cerentDcuPassiveUnit": cerentDcuPassiveUnit,
       "cerentCTDcuPassiveUnit": cerentCTDcuPassiveUnit,
       "cerentFTDcuPassiveUnit": cerentFTDcuPassiveUnit,
       "fortyGePort": fortyGePort,
       "fc8gPort": fc8gPort,
       "cerentOtu3Port": cerentOtu3Port,
       "cerentOc768Port": cerentOc768Port,
       "cerentMechanicalUnit": cerentMechanicalUnit,
       "cerent40GTxpCard": cerent40GTxpCard,
       "cerent40GMxpCard": cerent40GMxpCard,
       "cerent40EMxpCard": cerent40EMxpCard,
       "cerent15216ID50PassiveUnit": cerent15216ID50PassiveUnit,
       "cerent40ETxpCard": cerent40ETxpCard,
       "cerentOptEdfa17Card": cerentOptEdfa17Card,
       "cerentOptEdfa24Card": cerentOptEdfa24Card,
       "cerentBackPlaneM2": cerentBackPlaneM2,
       "cerentChassisM2Ansi": cerentChassisM2Ansi,
       "cerentChassisM2Etsi": cerentChassisM2Etsi,
       "cerentArXpCard": cerentArXpCard,
       "cerentBackPlaneM6": cerentBackPlaneM6,
       "cerentArMxpCard": cerentArMxpCard,
       "cerentChassisM6Ansi": cerentChassisM6Ansi,
       "cerentChassisM6Etsi": cerentChassisM6Etsi,
       "cerentPowerSupplyUts": cerentPowerSupplyUts,
       "cerentFlashUts": cerentFlashUts,
       "cerentAicInUts": cerentAicInUts,
       "cerentAicOutUts": cerentAicOutUts,
       "cerentIscEqptUts": cerentIscEqptUts,
       "cerentUdcVoipEmsUts": cerentUdcVoipEmsUts,
       "cerentBitsUts": cerentBitsUts,
       "cerentFanTrayUts": cerentFanTrayUts,
       "cerentAlarmDryContactUts": cerentAlarmDryContactUts,
       "cerentUsbUts": cerentUsbUts,
       "cerentUsbUtsPortCard": cerentUsbUtsPortCard,
       "cerentIoUts": cerentIoUts,
       "cerentEcuTray": cerentEcuTray,
       "cerentTncUtsCard": cerentTncUtsCard,
       "cerentTscUtsCard": cerentTscUtsCard,
       "cerentTncTscUtsSlot": cerentTncTscUtsSlot,
       "cerentEcuSlot": cerentEcuSlot,
       "cerentMscIscUtsPort": cerentMscIscUtsPort,
       "cerentOtu1Port": cerentOtu1Port,
       "cerentTncFePort": cerentTncFePort,
       "cerentIsc3stp1gPort": cerentIsc3stp1gPort,
       "cerentIsc3stp2gPort": cerentIsc3stp2gPort,
       "cerentPtSystem": cerentPtSystem,
       "cerentSdi3gvideoPort": cerentSdi3gvideoPort,
       "cerentPtf10GECard": cerentPtf10GECard,
       "cerentAutoPort": cerentAutoPort,
       "cerentPt10GECard": cerentPt10GECard,
       "cerentPtsaGECard": cerentPtsaGECard,
       "cerentFld303PassiveUnit": cerentFld303PassiveUnit,
       "cerentFld334PassiveUnit": cerentFld334PassiveUnit,
       "cerentFld366PassiveUnit": cerentFld366PassiveUnit,
       "cerentFld397PassiveUnit": cerentFld397PassiveUnit,
       "cerentFld429PassiveUnit": cerentFld429PassiveUnit,
       "cerentFld461PassiveUnit": cerentFld461PassiveUnit,
       "cerentFld493PassiveUnit": cerentFld493PassiveUnit,
       "cerentFld525PassiveUnit": cerentFld525PassiveUnit,
       "cerentFld557PassiveUnit": cerentFld557PassiveUnit,
       "cerentFld589PassiveUnit": cerentFld589PassiveUnit,
       "cerentFldOscPassiveUnit": cerentFldOscPassiveUnit,
       "cerentFlcCwdm8PassiveUnit": cerentFlcCwdm8PassiveUnit,
       "cerentSdsdiPort": cerentSdsdiPort,
       "cerentHdsdiPort": cerentHdsdiPort,
       "cerentOptRampCTPCard": cerentOptRampCTPCard,
       "cerentOptRampCOPCard": cerentOptRampCOPCard,
       "cerentFbgdcu165PassiveUnit": cerentFbgdcu165PassiveUnit,
       "cerentFbgdcu331PassiveUnit": cerentFbgdcu331PassiveUnit,
       "cerentFbgdcu496PassiveUnit": cerentFbgdcu496PassiveUnit,
       "cerentFbgdcu661PassiveUnit": cerentFbgdcu661PassiveUnit,
       "cerentFbgdcu826PassiveUnit": cerentFbgdcu826PassiveUnit,
       "cerentFbgdcu992PassiveUnit": cerentFbgdcu992PassiveUnit,
       "cerentFbgdcu1157PassiveUnit": cerentFbgdcu1157PassiveUnit,
       "cerentFbgdcu1322PassiveUnit": cerentFbgdcu1322PassiveUnit,
       "cerentFbgdcu1653PassiveUnit": cerentFbgdcu1653PassiveUnit,
       "cerentFbgdcu1983PassiveUnit": cerentFbgdcu1983PassiveUnit,
       "cerentMd48OddPassiveUnit": cerentMd48OddPassiveUnit,
       "cerentMd48EvenPassiveUnit": cerentMd48EvenPassiveUnit,
       "cerentMd48CmPassiveUnit": cerentMd48CmPassiveUnit,
       "cerentOtu4Port": cerentOtu4Port,
       "cerentOneHundredGePort": cerentOneHundredGePort,
       "cerentHundredGigLineCard": cerentHundredGigLineCard,
       "cerentTENxTENGigLineCard": cerentTENxTENGigLineCard,
       "cerentCfpLineCard": cerentCfpLineCard,
       "cerentOTLPort": cerentOTLPort,
       "cerentHundredgigPlim": cerentHundredgigPlim,
       "cerentWseLineCard": cerentWseLineCard,
       "cerentArXpeCard": cerentArXpeCard,
       "cerentEDRA126C": cerentEDRA126C,
       "cerentEDRA135C": cerentEDRA135C,
       "cerentEDRA226C": cerentEDRA226C,
       "cerentEDRA235C": cerentEDRA235C,
       "cerentWXC16FSLineCard": cerentWXC16FSLineCard,
       "cerentPassiv1x16COFSC": cerentPassiv1x16COFSC,
       "cerentPassive4x4COFSC": cerentPassive4x4COFSC,
       "cerentPassiveMODDEG5": cerentPassiveMODDEG5,
       "cerentPassiveMODUPG4": cerentPassiveMODUPG4,
       "cerentPassiveMPO8LCADPT": cerentPassiveMPO8LCADPT,
       "cerentPassiveASTEDFA": cerentPassiveASTEDFA,
       "cerentCPAK100GLineCard": cerentCPAK100GLineCard,
       "cerentGeneric": cerentGeneric,
       "cerentGenericDummyObjects": cerentGenericDummyObjects,
       "cerentExperimental": cerentExperimental,
       "cerentAgentCapabilities": cerentAgentCapabilities,
       "cerentRequirements": cerentRequirements,
       "cerentProducts": cerentProducts}
)
