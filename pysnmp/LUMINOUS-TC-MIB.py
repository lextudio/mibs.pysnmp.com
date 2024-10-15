# SNMP MIB module (LUMINOUS-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LUMINOUS-TC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:19:29 2024
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
 ObjectName,
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
    "ObjectName",
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

lumTcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4614, 1, 9)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LumShelfType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cSeries", 4),
          ("mSeries", 1),
          ("unused1", 2),
          ("unused2", 3))
    )



class LumChassisPlane(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("back", 2),
          ("front", 1))
    )



class LumSlotNum(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )



class LumPortNum(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )



class LumSimpleIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class LumPercent(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class LumRingDirection(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("east", 3),
          ("none", 1),
          ("west", 2))
    )



class LumAdminStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )



class LumOperStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("dormant", 5),
          ("down", 2),
          ("lowerLayerDown", 7),
          ("misMatch", 8),
          ("notPresent", 6),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )



class LumControl(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("unknown", 1))
    )



class LumServiceMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("policyForwarding", 4),
          ("routing", 3),
          ("wire", 2))
    )



class LumPortType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("physical", 2),
          ("subPortDemux", 3))
    )



class LumPortCreateType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("explicit", 2),
          ("implicit", 1))
    )



class LumPortDemuxType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("mplsTag", 3),
          ("none", 1),
          ("tdmChannel", 4),
          ("vlan", 2))
    )



class LumPortDemuxId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class LumConnectorType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("db9", 5),
          ("miniCoax", 4),
          ("none", 1),
          ("rj45", 2),
          ("scFiber", 3),
          ("sjFiber", 6),
          ("stFiber", 7))
    )



class LumSignalState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("idle", 1))
    )



class LumName(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )



class LumDescr(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )



class LumVersionString(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )



class LumSerialNumString(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 21),
    )



class LumCleiString(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )



class LumManufactureString(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )



class LumDateTimeString(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )



class LumCardBaseType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              21,
              22,
              23,
              28,
              29,
              32,
              33,
              34,
              35,
              36,
              38)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 6),
          ("asi", 34),
          ("asiIOIn", 35),
          ("asiIOOut", 36),
          ("ds3cc12", 28),
          ("ds3cc12IO", 29),
          ("ether", 5),
          ("ether24", 32),
          ("ether24IO", 33),
          ("etherFXIO", 17),
          ("etherIO", 10),
          ("gigE", 14),
          ("gigEIO", 15),
          ("none", 1),
          ("oc12", 12),
          ("oc12IO", 13),
          ("oc12IOAlarm", 16),
          ("present", 38),
          ("ring", 3),
          ("ring2", 22),
          ("ring2IO", 23),
          ("ringIO", 8),
          ("ringIOLR", 21),
          ("sysCon", 2),
          ("t1", 4),
          ("t1IO", 9),
          ("upLink", 7),
          ("utility", 11),
          ("wdm", 18),
          ("wdmIO", 19))
    )



class LumCardType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 6),
          ("asi", 34),
          ("asiIOIn", 35),
          ("asiIOOut", 36),
          ("ds3cc12", 28),
          ("ds3cc12IO", 29),
          ("e3cc12", 31),
          ("ether", 5),
          ("ether24", 32),
          ("ether24IO", 33),
          ("etherFXIO", 17),
          ("etherIO", 10),
          ("gigE", 14),
          ("gigEIO", 15),
          ("gigERouting", 37),
          ("newCardType", 40),
          ("none", 1),
          ("oc12", 12),
          ("oc12IO", 13),
          ("oc12IOAlarm", 16),
          ("present", 38),
          ("ring", 3),
          ("ring2", 22),
          ("ring2IO", 23),
          ("ringIO", 8),
          ("ringIOLR", 21),
          ("sysCon", 2),
          ("sysconR", 20),
          ("sysconU", 39),
          ("t1", 4),
          ("t1IO", 9),
          ("t3cc12", 30),
          ("upLink", 7),
          ("utility", 11),
          ("wdm", 18),
          ("wdmBand1", 24),
          ("wdmBand2", 25),
          ("wdmBand3", 26),
          ("wdmBand4", 27),
          ("wdmIO", 19))
    )



class LumCardAdminState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("none", 1),
          ("outOfService", 4),
          ("reset", 6),
          ("shutDown", 5),
          ("standby", 3),
          ("switchover", 7))
    )



class LumCardOperState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("down", 6),
          ("failure", 5),
          ("initializing", 8),
          ("none", 1),
          ("outOfService", 4),
          ("present", 7),
          ("standby", 3))
    )



class LumCardFailureState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("criticalFault", 2),
          ("minorAlarm", 4),
          ("minorFault", 3),
          ("none", 1))
    )



class LumOpticalWaveLength(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class LumOpticalFiberType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("multiMode", 3),
          ("singleMode", 2),
          ("unknown", 1))
    )



class LumOpticalMaxLength(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )



class LumOpticalConnector(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lc", 3),
          ("sc", 2),
          ("unknown", 1))
    )



class LumOpticalServiceSupport(Bits, TextualConvention):
    status = "current"


class LumOpticalService(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("fiberChannel1", 4),
          ("fiberChannel2", 5),
          ("gigE1", 2),
          ("gigE2", 3),
          ("none", 1),
          ("oc12", 6),
          ("oc24", 7),
          ("oc3", 11),
          ("oc48", 8),
          ("rpt", 9),
          ("rptE2", 10))
    )



class LumTdmType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("e1", 3),
          ("e3", 5),
          ("t1", 2),
          ("t3", 4),
          ("unknown", 1))
    )



class LumImageState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("accepted", 4),
          ("empty", 1),
          ("trial", 2),
          ("tried", 3),
          ("unknown", 5))
    )



class LumAlarmSeverity(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("critical", 2),
          ("major", 3),
          ("minor", 4),
          ("notAlarmed", 5),
          ("notReported", 6),
          ("undefined", 1))
    )



class LumResetCmd(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("reset", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Luminous_ObjectIdentity = ObjectIdentity
luminous = _Luminous_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4614)
)
_LumADM_ObjectIdentity = ObjectIdentity
lumADM = _LumADM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4614, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUMINOUS-TC-MIB",
    **{"LumShelfType": LumShelfType,
       "LumChassisPlane": LumChassisPlane,
       "LumSlotNum": LumSlotNum,
       "LumPortNum": LumPortNum,
       "LumSimpleIndex": LumSimpleIndex,
       "LumPercent": LumPercent,
       "LumRingDirection": LumRingDirection,
       "LumAdminStatus": LumAdminStatus,
       "LumOperStatus": LumOperStatus,
       "LumControl": LumControl,
       "LumServiceMode": LumServiceMode,
       "LumPortType": LumPortType,
       "LumPortCreateType": LumPortCreateType,
       "LumPortDemuxType": LumPortDemuxType,
       "LumPortDemuxId": LumPortDemuxId,
       "LumConnectorType": LumConnectorType,
       "LumSignalState": LumSignalState,
       "LumName": LumName,
       "LumDescr": LumDescr,
       "LumVersionString": LumVersionString,
       "LumSerialNumString": LumSerialNumString,
       "LumCleiString": LumCleiString,
       "LumManufactureString": LumManufactureString,
       "LumDateTimeString": LumDateTimeString,
       "LumCardBaseType": LumCardBaseType,
       "LumCardType": LumCardType,
       "LumCardAdminState": LumCardAdminState,
       "LumCardOperState": LumCardOperState,
       "LumCardFailureState": LumCardFailureState,
       "LumOpticalWaveLength": LumOpticalWaveLength,
       "LumOpticalFiberType": LumOpticalFiberType,
       "LumOpticalMaxLength": LumOpticalMaxLength,
       "LumOpticalConnector": LumOpticalConnector,
       "LumOpticalServiceSupport": LumOpticalServiceSupport,
       "LumOpticalService": LumOpticalService,
       "LumTdmType": LumTdmType,
       "LumImageState": LumImageState,
       "LumAlarmSeverity": LumAlarmSeverity,
       "LumResetCmd": LumResetCmd,
       "luminous": luminous,
       "lumADM": lumADM,
       "lumTcMIB": lumTcMIB}
)
