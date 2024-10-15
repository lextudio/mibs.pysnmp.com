# SNMP MIB module (CENTILLION-DOT5-EXTENSIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CENTILLION-DOT5-EXTENSIONS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:03 2024
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

(EnableIndicator,
 extensions) = mibBuilder.importSymbols(
    "CENTILLION-ROOT-MIB",
    "EnableIndicator",
    "extensions")

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


# Types definitions



class TrPortConnType(Integer32):
    """Custom type TrPortConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("tr4PortStation", 2),
          ("trPortAutoStationHub", 24),
          ("trPortBay-Ri", 19),
          ("trPortBay-Ro", 18),
          ("trPortDTR", 1),
          ("trPortFdtr-hub", 22),
          ("trPortFdtr-station", 23),
          ("trPortHub", 16),
          ("trPortOther-Ri", 21),
          ("trPortOther-Ro", 20),
          ("trPortRiRoNoPhantom", 4),
          ("trPortRiRoPhantom", 3),
          ("trPortStation", 17))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CnDot5Extensions_ObjectIdentity = ObjectIdentity
cnDot5Extensions = _CnDot5Extensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 3, 3)
)
_CnDot5ExtnTable_Object = MibTable
cnDot5ExtnTable = _CnDot5ExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 3, 1)
)
if mibBuilder.loadTexts:
    cnDot5ExtnTable.setStatus("mandatory")
_CnDot5ExtnEntry_Object = MibTableRow
cnDot5ExtnEntry = _CnDot5ExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 3, 1, 1)
)
cnDot5ExtnEntry.setIndexNames(
    (0, "CENTILLION-DOT5-EXTENSIONS-MIB", "cnDot5ExtnIfIndex"),
)
if mibBuilder.loadTexts:
    cnDot5ExtnEntry.setStatus("mandatory")
_CnDot5ExtnIfIndex_Type = Integer32
_CnDot5ExtnIfIndex_Object = MibTableColumn
cnDot5ExtnIfIndex = _CnDot5ExtnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 3, 1, 1, 1),
    _CnDot5ExtnIfIndex_Type()
)
cnDot5ExtnIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnDot5ExtnIfIndex.setStatus("mandatory")
_CnDot5ExtnPortConnType_Type = TrPortConnType
_CnDot5ExtnPortConnType_Object = MibTableColumn
cnDot5ExtnPortConnType = _CnDot5ExtnPortConnType_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 3, 1, 1, 2),
    _CnDot5ExtnPortConnType_Type()
)
cnDot5ExtnPortConnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDot5ExtnPortConnType.setStatus("mandatory")
_CnDot5ExtnPortSpeedSense_Type = EnableIndicator
_CnDot5ExtnPortSpeedSense_Object = MibTableColumn
cnDot5ExtnPortSpeedSense = _CnDot5ExtnPortSpeedSense_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 3, 1, 1, 3),
    _CnDot5ExtnPortSpeedSense_Type()
)
cnDot5ExtnPortSpeedSense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDot5ExtnPortSpeedSense.setStatus("mandatory")


class _CnDot5ExtnAdminRingSpeed_Type(Integer32):
    """Custom type cnDot5ExtnAdminRingSpeed based on Integer32"""
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
        *(("autoDetect", 1),
          ("autoDetect16or32", 7),
          ("autoDetect4or16or32", 8),
          ("force32Megabit", 6),
          ("forceFourMegabit", 2),
          ("forceSixteenMegabit", 3),
          ("matchFourMegabit", 4),
          ("matchSixteenMegabit", 5))
    )


_CnDot5ExtnAdminRingSpeed_Type.__name__ = "Integer32"
_CnDot5ExtnAdminRingSpeed_Object = MibTableColumn
cnDot5ExtnAdminRingSpeed = _CnDot5ExtnAdminRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 3, 1, 1, 4),
    _CnDot5ExtnAdminRingSpeed_Type()
)
cnDot5ExtnAdminRingSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDot5ExtnAdminRingSpeed.setStatus("mandatory")
_CnS5TrExtnTable_Object = MibTable
cnS5TrExtnTable = _CnS5TrExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 3, 2)
)
if mibBuilder.loadTexts:
    cnS5TrExtnTable.setStatus("mandatory")
_CnS5TrExtnEntry_Object = MibTableRow
cnS5TrExtnEntry = _CnS5TrExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 3, 2, 1)
)
cnS5TrExtnEntry.setIndexNames(
    (0, "CENTILLION-DOT5-EXTENSIONS-MIB", "cnS5TrExtnIfIndex"),
)
if mibBuilder.loadTexts:
    cnS5TrExtnEntry.setStatus("mandatory")
_CnS5TrExtnIfIndex_Type = Integer32
_CnS5TrExtnIfIndex_Object = MibTableColumn
cnS5TrExtnIfIndex = _CnS5TrExtnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 3, 2, 1, 1),
    _CnS5TrExtnIfIndex_Type()
)
cnS5TrExtnIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnS5TrExtnIfIndex.setStatus("mandatory")


class _CnS5TrExtnFrontPortConnect_Type(Integer32):
    """Custom type cnS5TrExtnFrontPortConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_CnS5TrExtnFrontPortConnect_Type.__name__ = "Integer32"
_CnS5TrExtnFrontPortConnect_Object = MibTableColumn
cnS5TrExtnFrontPortConnect = _CnS5TrExtnFrontPortConnect_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 3, 2, 1, 2),
    _CnS5TrExtnFrontPortConnect_Type()
)
cnS5TrExtnFrontPortConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnS5TrExtnFrontPortConnect.setStatus("mandatory")


class _CnS5TrExtnOperBkplaneAtt_Type(Integer32):
    """Custom type cnS5TrExtnOperBkplaneAtt based on Integer32"""
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
        *(("capableAndAttached", 3),
          ("capableAndDetached", 4),
          ("notCapable", 2),
          ("other", 1))
    )


_CnS5TrExtnOperBkplaneAtt_Type.__name__ = "Integer32"
_CnS5TrExtnOperBkplaneAtt_Object = MibTableColumn
cnS5TrExtnOperBkplaneAtt = _CnS5TrExtnOperBkplaneAtt_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 3, 2, 1, 3),
    _CnS5TrExtnOperBkplaneAtt_Type()
)
cnS5TrExtnOperBkplaneAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnS5TrExtnOperBkplaneAtt.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CENTILLION-DOT5-EXTENSIONS-MIB",
    **{"TrPortConnType": TrPortConnType,
       "cnDot5Extensions": cnDot5Extensions,
       "cnDot5ExtnTable": cnDot5ExtnTable,
       "cnDot5ExtnEntry": cnDot5ExtnEntry,
       "cnDot5ExtnIfIndex": cnDot5ExtnIfIndex,
       "cnDot5ExtnPortConnType": cnDot5ExtnPortConnType,
       "cnDot5ExtnPortSpeedSense": cnDot5ExtnPortSpeedSense,
       "cnDot5ExtnAdminRingSpeed": cnDot5ExtnAdminRingSpeed,
       "cnS5TrExtnTable": cnS5TrExtnTable,
       "cnS5TrExtnEntry": cnS5TrExtnEntry,
       "cnS5TrExtnIfIndex": cnS5TrExtnIfIndex,
       "cnS5TrExtnFrontPortConnect": cnS5TrExtnFrontPortConnect,
       "cnS5TrExtnOperBkplaneAtt": cnS5TrExtnOperBkplaneAtt}
)
