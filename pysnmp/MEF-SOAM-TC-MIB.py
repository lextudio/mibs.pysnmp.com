# SNMP MIB module (MEF-SOAM-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MEF-SOAM-TC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:20:48 2024
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

mefSoamTcMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 1)
)
mefSoamTcMib.setRevisions(
        ("2012-01-10 00:00",
         "2010-10-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MefSoamTcAvailabilityType(Integer32, TextualConvention):
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
        *(("available", 1),
          ("unavailable", 2),
          ("unknown", 3))
    )



class MefSoamTcConnectivityStatusType(Integer32, TextualConvention):
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
        *(("active", 2),
          ("inactive", 1),
          ("partiallyActive", 3))
    )



class MefSoamTcDataPatternType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onesPattern", 2),
          ("zeroPattern", 1))
    )



class MefSoamTcDelayMeasurementBinType(Integer32, TextualConvention):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("backwardFrameDelay", 3),
          ("backwardFrameDelayRange", 9),
          ("backwardIfdv", 6),
          ("forwardFrameDelay", 2),
          ("forwardFrameDelayRange", 8),
          ("forwardIfdv", 5),
          ("twoWayFrameDelay", 1),
          ("twoWayFrameDelayRange", 7),
          ("twoWayIfdv", 4))
    )



class MefSoamTcIntervalTypeAisLck(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneMinute", 2),
          ("oneSecond", 1))
    )



class MefSoamTcMeasurementPeriodType(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 3600000),
    )



class MefSoamTcMegIdType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              32)
        )
    )
    namedValues = NamedValues(
        *(("charString", 2),
          ("iccBased", 32),
          ("primaryVid", 1),
          ("rfc2865VpnId", 4),
          ("unsignedInt16", 3))
    )



class MefSoamTcOperationTimeType(Integer32, TextualConvention):
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
        *(("fixed", 4),
          ("immediate", 2),
          ("none", 1),
          ("relative", 3))
    )



class MefSoamTcSessionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onDemand", 2),
          ("proactive", 1))
    )



class MefSoamTcStatusType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )



class MefSoamTcTestPatternType(Integer32, TextualConvention):
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
        *(("null", 1),
          ("nullCrc32", 2),
          ("prbs", 3),
          ("prbsCrc32", 4))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MEF-SOAM-TC-MIB",
    **{"MefSoamTcAvailabilityType": MefSoamTcAvailabilityType,
       "MefSoamTcConnectivityStatusType": MefSoamTcConnectivityStatusType,
       "MefSoamTcDataPatternType": MefSoamTcDataPatternType,
       "MefSoamTcDelayMeasurementBinType": MefSoamTcDelayMeasurementBinType,
       "MefSoamTcIntervalTypeAisLck": MefSoamTcIntervalTypeAisLck,
       "MefSoamTcMeasurementPeriodType": MefSoamTcMeasurementPeriodType,
       "MefSoamTcMegIdType": MefSoamTcMegIdType,
       "MefSoamTcOperationTimeType": MefSoamTcOperationTimeType,
       "MefSoamTcSessionType": MefSoamTcSessionType,
       "MefSoamTcStatusType": MefSoamTcStatusType,
       "MefSoamTcTestPatternType": MefSoamTcTestPatternType,
       "mefSoamTcMib": mefSoamTcMib}
)
