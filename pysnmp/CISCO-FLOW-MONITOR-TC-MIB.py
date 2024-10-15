# SNMP MIB module (CISCO-FLOW-MONITOR-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FLOW-MONITOR-TC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:41 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoFlowMonitorTcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 688)
)
ciscoFlowMonitorTcMIB.setRevisions(
        ("2008-12-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FlowMonitorIdentifier(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class FlowIdentifier(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class FlowPointType(Integer32, TextualConvention):
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
        *(("dot1qVlan", 5),
          ("interface", 4),
          ("none", 3),
          ("other", 1),
          ("unknown", 2))
    )



class FlowPointIdentifier(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class FlowPointInterface(OctetString, TextualConvention):
    status = "current"
    displayHint = "4d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class FlowPointDot1qVlan(OctetString, TextualConvention):
    status = "current"
    displayHint = "4d,2d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )



class FlowMetrics(Bits, TextualConvention):
    status = "current"


class FlowCfgRateType(Integer32, TextualConvention):
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
        *(("auto", 1),
          ("ipBitRate", 3),
          ("ipPktRate", 2),
          ("mediaRate", 4))
    )



class FlowBitRateUnits(Integer32, TextualConvention):
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
        *(("bps", 1),
          ("gbps", 4),
          ("kbps", 2),
          ("mbps", 3))
    )



class FlowMetricScale(Integer32, TextualConvention):
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("atto", 3),
          ("exa", 14),
          ("femto", 4),
          ("giga", 12),
          ("kilo", 10),
          ("mega", 11),
          ("micro", 7),
          ("milli", 8),
          ("nano", 6),
          ("peta", 15),
          ("pico", 5),
          ("tera", 13),
          ("units", 9),
          ("yocto", 1),
          ("yotta", 17),
          ("zepto", 2),
          ("zetta", 16))
    )



class FlowMetricPrecision(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-8, -1),
        ValueRangeConstraint(1, 9),
    )



class FlowMetricValue(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000000, 1000000000),
    )



class FlowMonitorConditions(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class FlowMonitorConditionsProfile(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class FlowMonitorConditionsProfileOrZero(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class FlowMonitorConditionIdentifier(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2039),
    )



class FlowMonitorAlarmGroupIdentifier(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class FlowSetIdentifier(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FLOW-MONITOR-TC-MIB",
    **{"FlowMonitorIdentifier": FlowMonitorIdentifier,
       "FlowIdentifier": FlowIdentifier,
       "FlowPointType": FlowPointType,
       "FlowPointIdentifier": FlowPointIdentifier,
       "FlowPointInterface": FlowPointInterface,
       "FlowPointDot1qVlan": FlowPointDot1qVlan,
       "FlowMetrics": FlowMetrics,
       "FlowCfgRateType": FlowCfgRateType,
       "FlowBitRateUnits": FlowBitRateUnits,
       "FlowMetricScale": FlowMetricScale,
       "FlowMetricPrecision": FlowMetricPrecision,
       "FlowMetricValue": FlowMetricValue,
       "FlowMonitorConditions": FlowMonitorConditions,
       "FlowMonitorConditionsProfile": FlowMonitorConditionsProfile,
       "FlowMonitorConditionsProfileOrZero": FlowMonitorConditionsProfileOrZero,
       "FlowMonitorConditionIdentifier": FlowMonitorConditionIdentifier,
       "FlowMonitorAlarmGroupIdentifier": FlowMonitorAlarmGroupIdentifier,
       "FlowSetIdentifier": FlowSetIdentifier,
       "ciscoFlowMonitorTcMIB": ciscoFlowMonitorTcMIB}
)
