# SNMP MIB module (Modem-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Modem-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:35 2024
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

mdmMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 38, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MdmMib_ObjectIdentity = ObjectIdentity
mdmMib = _MdmMib_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 38)
)
_MdmMIBObjects_ObjectIdentity = ObjectIdentity
mdmMIBObjects = _MdmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 38, 1, 1)
)
_MdmNumber_Type = Integer32
_MdmNumber_Object = MibScalar
mdmNumber = _MdmNumber_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 1),
    _MdmNumber_Type()
)
mdmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmNumber.setStatus("current")
_MdmIDTable_Object = MibTable
mdmIDTable = _MdmIDTable_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mdmIDTable.setStatus("current")
_MdmIDEntry_Object = MibTableRow
mdmIDEntry = _MdmIDEntry_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 2, 1)
)
mdmIDEntry.setIndexNames(
    (0, "Modem-MIB", "mdmIndex"),
)
if mibBuilder.loadTexts:
    mdmIDEntry.setStatus("current")


class _MdmIndex_Type(Integer32):
    """Custom type mdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MdmIndex_Type.__name__ = "Integer32"
_MdmIndex_Object = MibTableColumn
mdmIndex = _MdmIndex_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 2, 1, 1),
    _MdmIndex_Type()
)
mdmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mdmIndex.setStatus("current")
_MdmIDManufacturerOID_Type = ObjectIdentifier
_MdmIDManufacturerOID_Object = MibTableColumn
mdmIDManufacturerOID = _MdmIDManufacturerOID_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 2, 1, 2),
    _MdmIDManufacturerOID_Type()
)
mdmIDManufacturerOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmIDManufacturerOID.setStatus("current")


class _MdmIDProductDetails_Type(DisplayString):
    """Custom type mdmIDProductDetails based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_MdmIDProductDetails_Type.__name__ = "DisplayString"
_MdmIDProductDetails_Object = MibTableColumn
mdmIDProductDetails = _MdmIDProductDetails_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 2, 1, 3),
    _MdmIDProductDetails_Type()
)
mdmIDProductDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmIDProductDetails.setStatus("current")
_MdmLineTable_Object = MibTable
mdmLineTable = _MdmLineTable_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 3)
)
if mibBuilder.loadTexts:
    mdmLineTable.setStatus("current")
_MdmLineEntry_Object = MibTableRow
mdmLineEntry = _MdmLineEntry_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mdmLineEntry.setStatus("current")


class _MdmLineCarrierLossTime_Type(Integer32):
    """Custom type mdmLineCarrierLossTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MdmLineCarrierLossTime_Type.__name__ = "Integer32"
_MdmLineCarrierLossTime_Object = MibTableColumn
mdmLineCarrierLossTime = _MdmLineCarrierLossTime_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 3, 1, 1),
    _MdmLineCarrierLossTime_Type()
)
mdmLineCarrierLossTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmLineCarrierLossTime.setStatus("current")


class _MdmLineState_Type(Integer32):
    """Custom type mdmLineState based on Integer32"""
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
        *(("busiedOut", 5),
          ("connected", 4),
          ("offHook", 3),
          ("onHook", 2),
          ("reset", 6),
          ("unknown", 1))
    )


_MdmLineState_Type.__name__ = "Integer32"
_MdmLineState_Object = MibTableColumn
mdmLineState = _MdmLineState_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 3, 1, 2),
    _MdmLineState_Type()
)
mdmLineState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmLineState.setStatus("current")
_MdmLineCapabilitiesTable_Object = MibTable
mdmLineCapabilitiesTable = _MdmLineCapabilitiesTable_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 4)
)
if mibBuilder.loadTexts:
    mdmLineCapabilitiesTable.setStatus("current")
_MdmLineCapabilitiesEntry_Object = MibTableRow
mdmLineCapabilitiesEntry = _MdmLineCapabilitiesEntry_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 4, 1)
)
mdmLineCapabilitiesEntry.setIndexNames(
    (0, "Modem-MIB", "mdmIndex"),
    (0, "Modem-MIB", "mdmLineCapabilitiesIndex"),
)
if mibBuilder.loadTexts:
    mdmLineCapabilitiesEntry.setStatus("current")
_MdmLineCapabilitiesIndex_Type = Integer32
_MdmLineCapabilitiesIndex_Object = MibTableColumn
mdmLineCapabilitiesIndex = _MdmLineCapabilitiesIndex_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 4, 1, 1),
    _MdmLineCapabilitiesIndex_Type()
)
mdmLineCapabilitiesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mdmLineCapabilitiesIndex.setStatus("current")
_MdmLineCapabilitiesID_Type = ObjectIdentifier
_MdmLineCapabilitiesID_Object = MibTableColumn
mdmLineCapabilitiesID = _MdmLineCapabilitiesID_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 4, 1, 2),
    _MdmLineCapabilitiesID_Type()
)
mdmLineCapabilitiesID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmLineCapabilitiesID.setStatus("current")


class _MdmLineCapabilitiesEnableRequested_Type(Integer32):
    """Custom type mdmLineCapabilitiesEnableRequested based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("optional", 2),
          ("preferred", 3))
    )


_MdmLineCapabilitiesEnableRequested_Type.__name__ = "Integer32"
_MdmLineCapabilitiesEnableRequested_Object = MibTableColumn
mdmLineCapabilitiesEnableRequested = _MdmLineCapabilitiesEnableRequested_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 4, 1, 3),
    _MdmLineCapabilitiesEnableRequested_Type()
)
mdmLineCapabilitiesEnableRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmLineCapabilitiesEnableRequested.setStatus("current")


class _MdmLineCapabilitiesEnableGranted_Type(Integer32):
    """Custom type mdmLineCapabilitiesEnableGranted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("optional", 2),
          ("preferred", 3))
    )


_MdmLineCapabilitiesEnableGranted_Type.__name__ = "Integer32"
_MdmLineCapabilitiesEnableGranted_Object = MibTableColumn
mdmLineCapabilitiesEnableGranted = _MdmLineCapabilitiesEnableGranted_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 4, 1, 4),
    _MdmLineCapabilitiesEnableGranted_Type()
)
mdmLineCapabilitiesEnableGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmLineCapabilitiesEnableGranted.setStatus("current")
_MdmLineCapabilities_ObjectIdentity = ObjectIdentity
mdmLineCapabilities = _MdmLineCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 5)
)
_MdmLineCapabilitiesV21_ObjectIdentity = ObjectIdentity
mdmLineCapabilitiesV21 = _MdmLineCapabilitiesV21_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    mdmLineCapabilitiesV21.setStatus("current")
_MdmLineCapabilitiesV22_ObjectIdentity = ObjectIdentity
mdmLineCapabilitiesV22 = _MdmLineCapabilitiesV22_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    mdmLineCapabilitiesV22.setStatus("current")
_MdmLineCapabilitiesV22bis_ObjectIdentity = ObjectIdentity
mdmLineCapabilitiesV22bis = _MdmLineCapabilitiesV22bis_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 3)
)
if mibBuilder.loadTexts:
    mdmLineCapabilitiesV22bis.setStatus("current")
_MdmLineCapabilitiesV23CC_ObjectIdentity = ObjectIdentity
mdmLineCapabilitiesV23CC = _MdmLineCapabilitiesV23CC_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 4)
)
if mibBuilder.loadTexts:
    mdmLineCapabilitiesV23CC.setStatus("current")
_MdmLineCapabilitiesV23SC_ObjectIdentity = ObjectIdentity
mdmLineCapabilitiesV23SC = _MdmLineCapabilitiesV23SC_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 5)
)
if mibBuilder.loadTexts:
    mdmLineCapabilitiesV23SC.setStatus("current")
_MdmLineCapabilitiesV25bis_ObjectIdentity = ObjectIdentity
mdmLineCapabilitiesV25bis = _MdmLineCapabilitiesV25bis_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 6)
)
if mibBuilder.loadTexts:
    mdmLineCapabilitiesV25bis.setStatus("current")
_MdmLineCapabilitiesV26bis_ObjectIdentity = ObjectIdentity
mdmLineCapabilitiesV26bis = _MdmLineCapabilitiesV26bis_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 7)
)
if mibBuilder.loadTexts:
    mdmLineCapabilitiesV26bis.setStatus("current")
_MdmLineCapabilitiesV26ter_ObjectIdentity = ObjectIdentity
mdmLineCapabilitiesV26ter = _MdmLineCapabilitiesV26ter_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 8)
)
if mibBuilder.loadTexts:
    mdmLineCapabilitiesV26ter.setStatus("current")
_MdmLineCapabilitiesV27ter_ObjectIdentity = ObjectIdentity
mdmLineCapabilitiesV27ter = _MdmLineCapabilitiesV27ter_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 9)
)
if mibBuilder.loadTexts:
    mdmLineCapabilitiesV27ter.setStatus("current")
_MdmLineCapabilitiesV32_ObjectIdentity = ObjectIdentity
mdmLineCapabilitiesV32 = _MdmLineCapabilitiesV32_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 10)
)
if mibBuilder.loadTexts:
    mdmLineCapabilitiesV32.setStatus("current")
_MdmLineCapabilitiesV32bis_ObjectIdentity = ObjectIdentity
mdmLineCapabilitiesV32bis = _MdmLineCapabilitiesV32bis_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 11)
)
if mibBuilder.loadTexts:
    mdmLineCapabilitiesV32bis.setStatus("current")
_MdmLineCapabilitiesV32terbo_ObjectIdentity = ObjectIdentity
mdmLineCapabilitiesV32terbo = _MdmLineCapabilitiesV32terbo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 12)
)
if mibBuilder.loadTexts:
    mdmLineCapabilitiesV32terbo.setStatus("current")
_MdmLineCapabilitiesVFC_ObjectIdentity = ObjectIdentity
mdmLineCapabilitiesVFC = _MdmLineCapabilitiesVFC_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 13)
)
if mibBuilder.loadTexts:
    mdmLineCapabilitiesVFC.setStatus("current")
_MdmLineCapabilitiesV34_ObjectIdentity = ObjectIdentity
mdmLineCapabilitiesV34 = _MdmLineCapabilitiesV34_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 14)
)
if mibBuilder.loadTexts:
    mdmLineCapabilitiesV34.setStatus("current")
_MdmLineCapabilitiesV42_ObjectIdentity = ObjectIdentity
mdmLineCapabilitiesV42 = _MdmLineCapabilitiesV42_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 15)
)
if mibBuilder.loadTexts:
    mdmLineCapabilitiesV42.setStatus("current")
_MdmLineCapabilitiesV42bis_ObjectIdentity = ObjectIdentity
mdmLineCapabilitiesV42bis = _MdmLineCapabilitiesV42bis_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 16)
)
if mibBuilder.loadTexts:
    mdmLineCapabilitiesV42bis.setStatus("current")
_MdmLineCapabilitiesMNP1_ObjectIdentity = ObjectIdentity
mdmLineCapabilitiesMNP1 = _MdmLineCapabilitiesMNP1_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 17)
)
if mibBuilder.loadTexts:
    mdmLineCapabilitiesMNP1.setStatus("current")
_MdmLineCapabilitiesMNP2_ObjectIdentity = ObjectIdentity
mdmLineCapabilitiesMNP2 = _MdmLineCapabilitiesMNP2_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 18)
)
if mibBuilder.loadTexts:
    mdmLineCapabilitiesMNP2.setStatus("current")
_MdmLineCapabilitiesMNP3_ObjectIdentity = ObjectIdentity
mdmLineCapabilitiesMNP3 = _MdmLineCapabilitiesMNP3_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 19)
)
if mibBuilder.loadTexts:
    mdmLineCapabilitiesMNP3.setStatus("current")
_MdmLineCapabilitiesMNP4_ObjectIdentity = ObjectIdentity
mdmLineCapabilitiesMNP4 = _MdmLineCapabilitiesMNP4_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 20)
)
if mibBuilder.loadTexts:
    mdmLineCapabilitiesMNP4.setStatus("current")
_MdmLineCapabilitiesMNP5_ObjectIdentity = ObjectIdentity
mdmLineCapabilitiesMNP5 = _MdmLineCapabilitiesMNP5_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 21)
)
if mibBuilder.loadTexts:
    mdmLineCapabilitiesMNP5.setStatus("current")
_MdmLineCapabilitiesMNP6_ObjectIdentity = ObjectIdentity
mdmLineCapabilitiesMNP6 = _MdmLineCapabilitiesMNP6_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 22)
)
if mibBuilder.loadTexts:
    mdmLineCapabilitiesMNP6.setStatus("current")
_MdmLineCapabilitiesMNP7_ObjectIdentity = ObjectIdentity
mdmLineCapabilitiesMNP7 = _MdmLineCapabilitiesMNP7_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 23)
)
if mibBuilder.loadTexts:
    mdmLineCapabilitiesMNP7.setStatus("current")
_MdmLineCapabilitiesMNP8_ObjectIdentity = ObjectIdentity
mdmLineCapabilitiesMNP8 = _MdmLineCapabilitiesMNP8_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 24)
)
if mibBuilder.loadTexts:
    mdmLineCapabilitiesMNP8.setStatus("current")
_MdmLineCapabilitiesMNP9_ObjectIdentity = ObjectIdentity
mdmLineCapabilitiesMNP9 = _MdmLineCapabilitiesMNP9_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 25)
)
if mibBuilder.loadTexts:
    mdmLineCapabilitiesMNP9.setStatus("current")
_MdmLineCapabilitiesMNP10_ObjectIdentity = ObjectIdentity
mdmLineCapabilitiesMNP10 = _MdmLineCapabilitiesMNP10_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 26)
)
if mibBuilder.loadTexts:
    mdmLineCapabilitiesMNP10.setStatus("current")
_MdmLineCapabilitiesV29_ObjectIdentity = ObjectIdentity
mdmLineCapabilitiesV29 = _MdmLineCapabilitiesV29_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 27)
)
if mibBuilder.loadTexts:
    mdmLineCapabilitiesV29.setStatus("current")
_MdmLineCapabilitiesV33_ObjectIdentity = ObjectIdentity
mdmLineCapabilitiesV33 = _MdmLineCapabilitiesV33_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 28)
)
if mibBuilder.loadTexts:
    mdmLineCapabilitiesV33.setStatus("current")
_MdmLineCapabilitiesBell208_ObjectIdentity = ObjectIdentity
mdmLineCapabilitiesBell208 = _MdmLineCapabilitiesBell208_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 29)
)
if mibBuilder.loadTexts:
    mdmLineCapabilitiesBell208.setStatus("current")
_MdmDTEInterfaceTable_Object = MibTable
mdmDTEInterfaceTable = _MdmDTEInterfaceTable_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 6)
)
if mibBuilder.loadTexts:
    mdmDTEInterfaceTable.setStatus("current")
_MdmDTEInterfaceEntry_Object = MibTableRow
mdmDTEInterfaceEntry = _MdmDTEInterfaceEntry_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    mdmDTEInterfaceEntry.setStatus("current")


class _MdmDTEActionDTROnToOff_Type(Integer32):
    """Custom type mdmDTEActionDTROnToOff based on Integer32"""
    defaultValue = 3

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
        *(("disconnectCall", 3),
          ("escapeToCommandMode", 2),
          ("ignore", 1),
          ("resetModem", 4))
    )


_MdmDTEActionDTROnToOff_Type.__name__ = "Integer32"
_MdmDTEActionDTROnToOff_Object = MibTableColumn
mdmDTEActionDTROnToOff = _MdmDTEActionDTROnToOff_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 6, 1, 1),
    _MdmDTEActionDTROnToOff_Type()
)
mdmDTEActionDTROnToOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDTEActionDTROnToOff.setStatus("current")


class _MdmDTEActionDTROffToOn_Type(Integer32):
    """Custom type mdmDTEActionDTROffToOn based on Integer32"""
    defaultValue = 3

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
        *(("autoAnswerEnable", 3),
          ("enableDial", 2),
          ("establishConnection", 4),
          ("ignore", 1))
    )


_MdmDTEActionDTROffToOn_Type.__name__ = "Integer32"
_MdmDTEActionDTROffToOn_Object = MibTableColumn
mdmDTEActionDTROffToOn = _MdmDTEActionDTROffToOn_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 6, 1, 2),
    _MdmDTEActionDTROffToOn_Type()
)
mdmDTEActionDTROffToOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDTEActionDTROffToOn.setStatus("current")


class _MdmDTESyncTimingSource_Type(Integer32):
    """Custom type mdmDTESyncTimingSource based on Integer32"""
    defaultValue = 1

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
        *(("external", 2),
          ("internal", 1),
          ("loopback", 3),
          ("network", 4))
    )


_MdmDTESyncTimingSource_Type.__name__ = "Integer32"
_MdmDTESyncTimingSource_Object = MibTableColumn
mdmDTESyncTimingSource = _MdmDTESyncTimingSource_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 6, 1, 3),
    _MdmDTESyncTimingSource_Type()
)
mdmDTESyncTimingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDTESyncTimingSource.setStatus("current")


class _MdmDTESyncAsyncMode_Type(Integer32):
    """Custom type mdmDTESyncAsyncMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("async", 1),
          ("sync", 2),
          ("syncAfterDial", 3))
    )


_MdmDTESyncAsyncMode_Type.__name__ = "Integer32"
_MdmDTESyncAsyncMode_Object = MibTableColumn
mdmDTESyncAsyncMode = _MdmDTESyncAsyncMode_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 6, 1, 4),
    _MdmDTESyncAsyncMode_Type()
)
mdmDTESyncAsyncMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDTESyncAsyncMode.setStatus("current")


class _MdmDTEInactivityTimeout_Type(Integer32):
    """Custom type mdmDTEInactivityTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MdmDTEInactivityTimeout_Type.__name__ = "Integer32"
_MdmDTEInactivityTimeout_Object = MibTableColumn
mdmDTEInactivityTimeout = _MdmDTEInactivityTimeout_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 6, 1, 5),
    _MdmDTEInactivityTimeout_Type()
)
mdmDTEInactivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDTEInactivityTimeout.setStatus("current")
_MdmCallControlTable_Object = MibTable
mdmCallControlTable = _MdmCallControlTable_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 7)
)
if mibBuilder.loadTexts:
    mdmCallControlTable.setStatus("current")
_MdmCallControlEntry_Object = MibTableRow
mdmCallControlEntry = _MdmCallControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    mdmCallControlEntry.setStatus("current")


class _MdmCCRingsBeforeAnswer_Type(Integer32):
    """Custom type mdmCCRingsBeforeAnswer based on Integer32"""
    defaultValue = 1


_MdmCCRingsBeforeAnswer_Object = MibTableColumn
mdmCCRingsBeforeAnswer = _MdmCCRingsBeforeAnswer_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 7, 1, 1),
    _MdmCCRingsBeforeAnswer_Type()
)
mdmCCRingsBeforeAnswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCCRingsBeforeAnswer.setStatus("current")


class _MdmCCCallSetUpFailTimer_Type(Integer32):
    """Custom type mdmCCCallSetUpFailTimer based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmCCCallSetUpFailTimer_Type.__name__ = "Integer32"
_MdmCCCallSetUpFailTimer_Object = MibTableColumn
mdmCCCallSetUpFailTimer = _MdmCCCallSetUpFailTimer_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 7, 1, 2),
    _MdmCCCallSetUpFailTimer_Type()
)
mdmCCCallSetUpFailTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCCCallSetUpFailTimer.setStatus("current")


class _MdmCCResultCodeEnable_Type(Integer32):
    """Custom type mdmCCResultCodeEnable based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("numericEnabled", 2),
          ("verboseEnabled", 3))
    )


_MdmCCResultCodeEnable_Type.__name__ = "Integer32"
_MdmCCResultCodeEnable_Object = MibTableColumn
mdmCCResultCodeEnable = _MdmCCResultCodeEnable_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 7, 1, 3),
    _MdmCCResultCodeEnable_Type()
)
mdmCCResultCodeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCCResultCodeEnable.setStatus("current")


class _MdmCCEscapeAction_Type(Integer32):
    """Custom type mdmCCEscapeAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enterCommandMode", 3),
          ("hangUp", 2),
          ("ignoreEscape", 1))
    )


_MdmCCEscapeAction_Type.__name__ = "Integer32"
_MdmCCEscapeAction_Object = MibTableColumn
mdmCCEscapeAction = _MdmCCEscapeAction_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 7, 1, 4),
    _MdmCCEscapeAction_Type()
)
mdmCCEscapeAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCCEscapeAction.setStatus("current")
_MdmCCCallDuration_Type = Integer32
_MdmCCCallDuration_Object = MibTableColumn
mdmCCCallDuration = _MdmCCCallDuration_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 7, 1, 5),
    _MdmCCCallDuration_Type()
)
mdmCCCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCCCallDuration.setStatus("current")


class _MdmCCConnectionFailReason_Type(Integer32):
    """Custom type mdmCCConnectionFailReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              10,
              11,
              20,
              30,
              31,
              32,
              33,
              40,
              41,
              42)
        )
    )
    namedValues = NamedValues(
        *(("carrierLost", 40),
          ("dtrDrop", 20),
          ("equipmentFailure", 11),
          ("faxDetected", 42),
          ("inactivityTimeout", 4),
          ("lineBusy", 31),
          ("managementCommand", 3),
          ("mnpIncompatibility", 5),
          ("noAnswer", 32),
          ("noDialTone", 30),
          ("other", 2),
          ("powerLoss", 10),
          ("protocolError", 6),
          ("trainingFailed", 41),
          ("unknown", 1),
          ("voiceDetected", 33))
    )


_MdmCCConnectionFailReason_Type.__name__ = "Integer32"
_MdmCCConnectionFailReason_Object = MibTableColumn
mdmCCConnectionFailReason = _MdmCCConnectionFailReason_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 7, 1, 6),
    _MdmCCConnectionFailReason_Type()
)
mdmCCConnectionFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCCConnectionFailReason.setStatus("current")
_MdmCCStoredDialStringTable_Object = MibTable
mdmCCStoredDialStringTable = _MdmCCStoredDialStringTable_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 8)
)
if mibBuilder.loadTexts:
    mdmCCStoredDialStringTable.setStatus("current")
_MdmCCStoredDialStringEntry_Object = MibTableRow
mdmCCStoredDialStringEntry = _MdmCCStoredDialStringEntry_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 8, 1)
)
mdmCCStoredDialStringEntry.setIndexNames(
    (0, "Modem-MIB", "mdmIndex"),
    (0, "Modem-MIB", "mdmCCStoredDialStringIndex"),
)
if mibBuilder.loadTexts:
    mdmCCStoredDialStringEntry.setStatus("current")


class _MdmCCStoredDialStringIndex_Type(Integer32):
    """Custom type mdmCCStoredDialStringIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MdmCCStoredDialStringIndex_Type.__name__ = "Integer32"
_MdmCCStoredDialStringIndex_Object = MibTableColumn
mdmCCStoredDialStringIndex = _MdmCCStoredDialStringIndex_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 8, 1, 1),
    _MdmCCStoredDialStringIndex_Type()
)
mdmCCStoredDialStringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mdmCCStoredDialStringIndex.setStatus("current")


class _MdmCCStoredDialString_Type(DisplayString):
    """Custom type mdmCCStoredDialString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MdmCCStoredDialString_Type.__name__ = "DisplayString"
_MdmCCStoredDialString_Object = MibTableColumn
mdmCCStoredDialString = _MdmCCStoredDialString_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 8, 1, 2),
    _MdmCCStoredDialString_Type()
)
mdmCCStoredDialString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCCStoredDialString.setStatus("current")
_MdmECTable_Object = MibTable
mdmECTable = _MdmECTable_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 9)
)
if mibBuilder.loadTexts:
    mdmECTable.setStatus("current")
_MdmECEntry_Object = MibTableRow
mdmECEntry = _MdmECEntry_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    mdmECEntry.setStatus("current")
_MdmECErrorControlUsed_Type = ObjectIdentifier
_MdmECErrorControlUsed_Object = MibTableColumn
mdmECErrorControlUsed = _MdmECErrorControlUsed_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 9, 1, 1),
    _MdmECErrorControlUsed_Type()
)
mdmECErrorControlUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmECErrorControlUsed.setStatus("current")
_MdmDCTable_Object = MibTable
mdmDCTable = _MdmDCTable_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 10)
)
if mibBuilder.loadTexts:
    mdmDCTable.setStatus("current")
_MdmDCEntry_Object = MibTableRow
mdmDCEntry = _MdmDCEntry_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    mdmDCEntry.setStatus("current")
_MdmDCCompressionTypeUsed_Type = ObjectIdentifier
_MdmDCCompressionTypeUsed_Object = MibTableColumn
mdmDCCompressionTypeUsed = _MdmDCCompressionTypeUsed_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 10, 1, 1),
    _MdmDCCompressionTypeUsed_Type()
)
mdmDCCompressionTypeUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmDCCompressionTypeUsed.setStatus("current")
_MdmSCTable_Object = MibTable
mdmSCTable = _MdmSCTable_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 11)
)
if mibBuilder.loadTexts:
    mdmSCTable.setStatus("current")
_MdmSCEntry_Object = MibTableRow
mdmSCEntry = _MdmSCEntry_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 11, 1)
)
if mibBuilder.loadTexts:
    mdmSCEntry.setStatus("current")
_MdmSCCurrentLineTransmitRate_Type = Integer32
_MdmSCCurrentLineTransmitRate_Object = MibTableColumn
mdmSCCurrentLineTransmitRate = _MdmSCCurrentLineTransmitRate_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 11, 1, 1),
    _MdmSCCurrentLineTransmitRate_Type()
)
mdmSCCurrentLineTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmSCCurrentLineTransmitRate.setStatus("current")
_MdmSCCurrentLineReceiveRate_Type = Integer32
_MdmSCCurrentLineReceiveRate_Object = MibTableColumn
mdmSCCurrentLineReceiveRate = _MdmSCCurrentLineReceiveRate_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 11, 1, 2),
    _MdmSCCurrentLineReceiveRate_Type()
)
mdmSCCurrentLineReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmSCCurrentLineReceiveRate.setStatus("current")
_MdmSCInitialLineTransmitRate_Type = Integer32
_MdmSCInitialLineTransmitRate_Object = MibTableColumn
mdmSCInitialLineTransmitRate = _MdmSCInitialLineTransmitRate_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 11, 1, 3),
    _MdmSCInitialLineTransmitRate_Type()
)
mdmSCInitialLineTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmSCInitialLineTransmitRate.setStatus("current")
_MdmSCInitialLineReceiveRate_Type = Integer32
_MdmSCInitialLineReceiveRate_Object = MibTableColumn
mdmSCInitialLineReceiveRate = _MdmSCInitialLineReceiveRate_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 11, 1, 4),
    _MdmSCInitialLineReceiveRate_Type()
)
mdmSCInitialLineReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmSCInitialLineReceiveRate.setStatus("current")
_MdmSCModulationSchemeUsed_Type = ObjectIdentifier
_MdmSCModulationSchemeUsed_Object = MibTableColumn
mdmSCModulationSchemeUsed = _MdmSCModulationSchemeUsed_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 11, 1, 5),
    _MdmSCModulationSchemeUsed_Type()
)
mdmSCModulationSchemeUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmSCModulationSchemeUsed.setStatus("current")
_MdmStatsTable_Object = MibTable
mdmStatsTable = _MdmStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 12)
)
if mibBuilder.loadTexts:
    mdmStatsTable.setStatus("current")
_MdmStatsEntry_Object = MibTableRow
mdmStatsEntry = _MdmStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1)
)
if mibBuilder.loadTexts:
    mdmStatsEntry.setStatus("current")
_MdmStatsRingNoAnswers_Type = Counter32
_MdmStatsRingNoAnswers_Object = MibTableColumn
mdmStatsRingNoAnswers = _MdmStatsRingNoAnswers_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 1),
    _MdmStatsRingNoAnswers_Type()
)
mdmStatsRingNoAnswers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmStatsRingNoAnswers.setStatus("current")
_MdmStatsIncomingConnectionFailures_Type = Counter32
_MdmStatsIncomingConnectionFailures_Object = MibTableColumn
mdmStatsIncomingConnectionFailures = _MdmStatsIncomingConnectionFailures_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 2),
    _MdmStatsIncomingConnectionFailures_Type()
)
mdmStatsIncomingConnectionFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmStatsIncomingConnectionFailures.setStatus("current")
_MdmStatsIncomingConnectionCompletions_Type = Counter32
_MdmStatsIncomingConnectionCompletions_Object = MibTableColumn
mdmStatsIncomingConnectionCompletions = _MdmStatsIncomingConnectionCompletions_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 3),
    _MdmStatsIncomingConnectionCompletions_Type()
)
mdmStatsIncomingConnectionCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmStatsIncomingConnectionCompletions.setStatus("current")
_MdmStatsFailedDialAttempts_Type = Counter32
_MdmStatsFailedDialAttempts_Object = MibTableColumn
mdmStatsFailedDialAttempts = _MdmStatsFailedDialAttempts_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 4),
    _MdmStatsFailedDialAttempts_Type()
)
mdmStatsFailedDialAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmStatsFailedDialAttempts.setStatus("current")
_MdmStatsOutgoingConnectionFailures_Type = Counter32
_MdmStatsOutgoingConnectionFailures_Object = MibTableColumn
mdmStatsOutgoingConnectionFailures = _MdmStatsOutgoingConnectionFailures_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 5),
    _MdmStatsOutgoingConnectionFailures_Type()
)
mdmStatsOutgoingConnectionFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmStatsOutgoingConnectionFailures.setStatus("current")
_MdmStatsOutgoingConnectionCompletions_Type = Counter32
_MdmStatsOutgoingConnectionCompletions_Object = MibTableColumn
mdmStatsOutgoingConnectionCompletions = _MdmStatsOutgoingConnectionCompletions_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 6),
    _MdmStatsOutgoingConnectionCompletions_Type()
)
mdmStatsOutgoingConnectionCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmStatsOutgoingConnectionCompletions.setStatus("current")
_MdmStatsRetrains_Type = Counter32
_MdmStatsRetrains_Object = MibTableColumn
mdmStatsRetrains = _MdmStatsRetrains_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 7),
    _MdmStatsRetrains_Type()
)
mdmStatsRetrains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmStatsRetrains.setStatus("current")
_MdmStats2400OrLessConnections_Type = Counter32
_MdmStats2400OrLessConnections_Object = MibTableColumn
mdmStats2400OrLessConnections = _MdmStats2400OrLessConnections_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 8),
    _MdmStats2400OrLessConnections_Type()
)
mdmStats2400OrLessConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmStats2400OrLessConnections.setStatus("current")
_MdmStats2400To14400Connections_Type = Counter32
_MdmStats2400To14400Connections_Object = MibTableColumn
mdmStats2400To14400Connections = _MdmStats2400To14400Connections_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 9),
    _MdmStats2400To14400Connections_Type()
)
mdmStats2400To14400Connections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmStats2400To14400Connections.setStatus("current")
_MdmStatsGreaterThan14400Connections_Type = Counter32
_MdmStatsGreaterThan14400Connections_Object = MibTableColumn
mdmStatsGreaterThan14400Connections = _MdmStatsGreaterThan14400Connections_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 10),
    _MdmStatsGreaterThan14400Connections_Type()
)
mdmStatsGreaterThan14400Connections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmStatsGreaterThan14400Connections.setStatus("current")
_MdmStatsErrorControlledConnections_Type = Counter32
_MdmStatsErrorControlledConnections_Object = MibTableColumn
mdmStatsErrorControlledConnections = _MdmStatsErrorControlledConnections_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 11),
    _MdmStatsErrorControlledConnections_Type()
)
mdmStatsErrorControlledConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmStatsErrorControlledConnections.setStatus("current")
_MdmStatsCompressedConnections_Type = Counter32
_MdmStatsCompressedConnections_Object = MibTableColumn
mdmStatsCompressedConnections = _MdmStatsCompressedConnections_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 12),
    _MdmStatsCompressedConnections_Type()
)
mdmStatsCompressedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmStatsCompressedConnections.setStatus("current")


class _MdmStatsCompressionEfficiency_Type(Integer32):
    """Custom type mdmStatsCompressionEfficiency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MdmStatsCompressionEfficiency_Type.__name__ = "Integer32"
_MdmStatsCompressionEfficiency_Object = MibTableColumn
mdmStatsCompressionEfficiency = _MdmStatsCompressionEfficiency_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 13),
    _MdmStatsCompressionEfficiency_Type()
)
mdmStatsCompressionEfficiency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmStatsCompressionEfficiency.setStatus("current")
_MdmStatsSentOctets_Type = Counter32
_MdmStatsSentOctets_Object = MibTableColumn
mdmStatsSentOctets = _MdmStatsSentOctets_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 14),
    _MdmStatsSentOctets_Type()
)
mdmStatsSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmStatsSentOctets.setStatus("current")
_MdmStatsReceivedOctets_Type = Counter32
_MdmStatsReceivedOctets_Object = MibTableColumn
mdmStatsReceivedOctets = _MdmStatsReceivedOctets_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 15),
    _MdmStatsReceivedOctets_Type()
)
mdmStatsReceivedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmStatsReceivedOctets.setStatus("current")
_MdmStatsSentDataFrames_Type = Counter32
_MdmStatsSentDataFrames_Object = MibTableColumn
mdmStatsSentDataFrames = _MdmStatsSentDataFrames_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 16),
    _MdmStatsSentDataFrames_Type()
)
mdmStatsSentDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmStatsSentDataFrames.setStatus("current")
_MdmStatsReceivedDataFrames_Type = Counter32
_MdmStatsReceivedDataFrames_Object = MibTableColumn
mdmStatsReceivedDataFrames = _MdmStatsReceivedDataFrames_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 17),
    _MdmStatsReceivedDataFrames_Type()
)
mdmStatsReceivedDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmStatsReceivedDataFrames.setStatus("current")
_MdmStatsResentFrames_Type = Counter32
_MdmStatsResentFrames_Object = MibTableColumn
mdmStatsResentFrames = _MdmStatsResentFrames_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 18),
    _MdmStatsResentFrames_Type()
)
mdmStatsResentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmStatsResentFrames.setStatus("current")
_MdmStatsErrorFrames_Type = Counter32
_MdmStatsErrorFrames_Object = MibTableColumn
mdmStatsErrorFrames = _MdmStatsErrorFrames_Object(
    (1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 19),
    _MdmStatsErrorFrames_Type()
)
mdmStatsErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmStatsErrorFrames.setStatus("current")
_MdmConformance_ObjectIdentity = ObjectIdentity
mdmConformance = _MdmConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 38, 1, 2)
)
_MdmCompliances_ObjectIdentity = ObjectIdentity
mdmCompliances = _MdmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 38, 1, 2, 1)
)
_MdmGroups_ObjectIdentity = ObjectIdentity
mdmGroups = _MdmGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 38, 1, 2, 2)
)
mdmIDEntry.registerAugmentions(
    ("Modem-MIB",
     "mdmLineEntry")
)
mdmLineEntry.setIndexNames(*mdmIDEntry.getIndexNames())
mdmIDEntry.registerAugmentions(
    ("Modem-MIB",
     "mdmDTEInterfaceEntry")
)
mdmDTEInterfaceEntry.setIndexNames(*mdmIDEntry.getIndexNames())
mdmIDEntry.registerAugmentions(
    ("Modem-MIB",
     "mdmCallControlEntry")
)
mdmCallControlEntry.setIndexNames(*mdmIDEntry.getIndexNames())
mdmIDEntry.registerAugmentions(
    ("Modem-MIB",
     "mdmECEntry")
)
mdmECEntry.setIndexNames(*mdmIDEntry.getIndexNames())
mdmIDEntry.registerAugmentions(
    ("Modem-MIB",
     "mdmDCEntry")
)
mdmDCEntry.setIndexNames(*mdmIDEntry.getIndexNames())
mdmIDEntry.registerAugmentions(
    ("Modem-MIB",
     "mdmSCEntry")
)
mdmSCEntry.setIndexNames(*mdmIDEntry.getIndexNames())
mdmIDEntry.registerAugmentions(
    ("Modem-MIB",
     "mdmStatsEntry")
)
mdmStatsEntry.setIndexNames(*mdmIDEntry.getIndexNames())

# Managed Objects groups

mdmIDGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 38, 1, 2, 2, 1)
)
mdmIDGroup.setObjects(
      *(("Modem-MIB", "mdmIDManufacturerOID"),
        ("Modem-MIB", "mdmIDProductDetails"))
)
if mibBuilder.loadTexts:
    mdmIDGroup.setStatus("current")

mdmLineInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 38, 1, 2, 2, 2)
)
mdmLineInterfaceGroup.setObjects(
      *(("Modem-MIB", "mdmLineCarrierLossTime"),
        ("Modem-MIB", "mdmLineState"),
        ("Modem-MIB", "mdmLineCapabilitiesID"),
        ("Modem-MIB", "mdmLineCapabilitiesEnableRequested"),
        ("Modem-MIB", "mdmLineCapabilitiesEnableGranted"))
)
if mibBuilder.loadTexts:
    mdmLineInterfaceGroup.setStatus("current")

mdmDTEInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 38, 1, 2, 2, 3)
)
mdmDTEInterfaceGroup.setObjects(
      *(("Modem-MIB", "mdmDTEActionDTROnToOff"),
        ("Modem-MIB", "mdmDTEActionDTROffToOn"),
        ("Modem-MIB", "mdmDTESyncTimingSource"),
        ("Modem-MIB", "mdmDTESyncAsyncMode"),
        ("Modem-MIB", "mdmDTEInactivityTimeout"))
)
if mibBuilder.loadTexts:
    mdmDTEInterfaceGroup.setStatus("current")

mdmCallControlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 38, 1, 2, 2, 4)
)
mdmCallControlGroup.setObjects(
      *(("Modem-MIB", "mdmCCRingsBeforeAnswer"),
        ("Modem-MIB", "mdmCCCallSetUpFailTimer"),
        ("Modem-MIB", "mdmCCResultCodeEnable"),
        ("Modem-MIB", "mdmCCEscapeAction"),
        ("Modem-MIB", "mdmCCCallDuration"),
        ("Modem-MIB", "mdmCCConnectionFailReason"),
        ("Modem-MIB", "mdmCCStoredDialString"))
)
if mibBuilder.loadTexts:
    mdmCallControlGroup.setStatus("current")

mdmErrorControlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 38, 1, 2, 2, 5)
)
mdmErrorControlGroup.setObjects(
    ("Modem-MIB", "mdmECErrorControlUsed")
)
if mibBuilder.loadTexts:
    mdmErrorControlGroup.setStatus("current")

mdmDataCompressionGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 38, 1, 2, 2, 6)
)
mdmDataCompressionGroup.setObjects(
    ("Modem-MIB", "mdmDCCompressionTypeUsed")
)
if mibBuilder.loadTexts:
    mdmDataCompressionGroup.setStatus("current")

mdmSignalConvertorGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 38, 1, 2, 2, 7)
)
mdmSignalConvertorGroup.setObjects(
      *(("Modem-MIB", "mdmSCCurrentLineReceiveRate"),
        ("Modem-MIB", "mdmSCCurrentLineTransmitRate"),
        ("Modem-MIB", "mdmSCInitialLineReceiveRate"),
        ("Modem-MIB", "mdmSCInitialLineTransmitRate"),
        ("Modem-MIB", "mdmSCModulationSchemeUsed"))
)
if mibBuilder.loadTexts:
    mdmSignalConvertorGroup.setStatus("current")

mdmStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 38, 1, 2, 2, 8)
)
mdmStatisticsGroup.setObjects(
      *(("Modem-MIB", "mdmStatsRingNoAnswers"),
        ("Modem-MIB", "mdmStatsIncomingConnectionFailures"),
        ("Modem-MIB", "mdmStatsIncomingConnectionCompletions"),
        ("Modem-MIB", "mdmStatsFailedDialAttempts"),
        ("Modem-MIB", "mdmStatsOutgoingConnectionFailures"),
        ("Modem-MIB", "mdmStatsOutgoingConnectionCompletions"),
        ("Modem-MIB", "mdmStatsRetrains"),
        ("Modem-MIB", "mdmStats2400OrLessConnections"),
        ("Modem-MIB", "mdmStats2400To14400Connections"),
        ("Modem-MIB", "mdmStatsGreaterThan14400Connections"),
        ("Modem-MIB", "mdmStatsErrorControlledConnections"),
        ("Modem-MIB", "mdmStatsCompressedConnections"),
        ("Modem-MIB", "mdmStatsCompressionEfficiency"),
        ("Modem-MIB", "mdmStatsSentOctets"),
        ("Modem-MIB", "mdmStatsReceivedOctets"),
        ("Modem-MIB", "mdmStatsSentDataFrames"),
        ("Modem-MIB", "mdmStatsReceivedDataFrames"),
        ("Modem-MIB", "mdmStatsResentFrames"),
        ("Modem-MIB", "mdmStatsErrorFrames"))
)
if mibBuilder.loadTexts:
    mdmStatisticsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mdmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 38, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    mdmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Modem-MIB",
    **{"mdmMib": mdmMib,
       "mdmMIB": mdmMIB,
       "mdmMIBObjects": mdmMIBObjects,
       "mdmNumber": mdmNumber,
       "mdmIDTable": mdmIDTable,
       "mdmIDEntry": mdmIDEntry,
       "mdmIndex": mdmIndex,
       "mdmIDManufacturerOID": mdmIDManufacturerOID,
       "mdmIDProductDetails": mdmIDProductDetails,
       "mdmLineTable": mdmLineTable,
       "mdmLineEntry": mdmLineEntry,
       "mdmLineCarrierLossTime": mdmLineCarrierLossTime,
       "mdmLineState": mdmLineState,
       "mdmLineCapabilitiesTable": mdmLineCapabilitiesTable,
       "mdmLineCapabilitiesEntry": mdmLineCapabilitiesEntry,
       "mdmLineCapabilitiesIndex": mdmLineCapabilitiesIndex,
       "mdmLineCapabilitiesID": mdmLineCapabilitiesID,
       "mdmLineCapabilitiesEnableRequested": mdmLineCapabilitiesEnableRequested,
       "mdmLineCapabilitiesEnableGranted": mdmLineCapabilitiesEnableGranted,
       "mdmLineCapabilities": mdmLineCapabilities,
       "mdmLineCapabilitiesV21": mdmLineCapabilitiesV21,
       "mdmLineCapabilitiesV22": mdmLineCapabilitiesV22,
       "mdmLineCapabilitiesV22bis": mdmLineCapabilitiesV22bis,
       "mdmLineCapabilitiesV23CC": mdmLineCapabilitiesV23CC,
       "mdmLineCapabilitiesV23SC": mdmLineCapabilitiesV23SC,
       "mdmLineCapabilitiesV25bis": mdmLineCapabilitiesV25bis,
       "mdmLineCapabilitiesV26bis": mdmLineCapabilitiesV26bis,
       "mdmLineCapabilitiesV26ter": mdmLineCapabilitiesV26ter,
       "mdmLineCapabilitiesV27ter": mdmLineCapabilitiesV27ter,
       "mdmLineCapabilitiesV32": mdmLineCapabilitiesV32,
       "mdmLineCapabilitiesV32bis": mdmLineCapabilitiesV32bis,
       "mdmLineCapabilitiesV32terbo": mdmLineCapabilitiesV32terbo,
       "mdmLineCapabilitiesVFC": mdmLineCapabilitiesVFC,
       "mdmLineCapabilitiesV34": mdmLineCapabilitiesV34,
       "mdmLineCapabilitiesV42": mdmLineCapabilitiesV42,
       "mdmLineCapabilitiesV42bis": mdmLineCapabilitiesV42bis,
       "mdmLineCapabilitiesMNP1": mdmLineCapabilitiesMNP1,
       "mdmLineCapabilitiesMNP2": mdmLineCapabilitiesMNP2,
       "mdmLineCapabilitiesMNP3": mdmLineCapabilitiesMNP3,
       "mdmLineCapabilitiesMNP4": mdmLineCapabilitiesMNP4,
       "mdmLineCapabilitiesMNP5": mdmLineCapabilitiesMNP5,
       "mdmLineCapabilitiesMNP6": mdmLineCapabilitiesMNP6,
       "mdmLineCapabilitiesMNP7": mdmLineCapabilitiesMNP7,
       "mdmLineCapabilitiesMNP8": mdmLineCapabilitiesMNP8,
       "mdmLineCapabilitiesMNP9": mdmLineCapabilitiesMNP9,
       "mdmLineCapabilitiesMNP10": mdmLineCapabilitiesMNP10,
       "mdmLineCapabilitiesV29": mdmLineCapabilitiesV29,
       "mdmLineCapabilitiesV33": mdmLineCapabilitiesV33,
       "mdmLineCapabilitiesBell208": mdmLineCapabilitiesBell208,
       "mdmDTEInterfaceTable": mdmDTEInterfaceTable,
       "mdmDTEInterfaceEntry": mdmDTEInterfaceEntry,
       "mdmDTEActionDTROnToOff": mdmDTEActionDTROnToOff,
       "mdmDTEActionDTROffToOn": mdmDTEActionDTROffToOn,
       "mdmDTESyncTimingSource": mdmDTESyncTimingSource,
       "mdmDTESyncAsyncMode": mdmDTESyncAsyncMode,
       "mdmDTEInactivityTimeout": mdmDTEInactivityTimeout,
       "mdmCallControlTable": mdmCallControlTable,
       "mdmCallControlEntry": mdmCallControlEntry,
       "mdmCCRingsBeforeAnswer": mdmCCRingsBeforeAnswer,
       "mdmCCCallSetUpFailTimer": mdmCCCallSetUpFailTimer,
       "mdmCCResultCodeEnable": mdmCCResultCodeEnable,
       "mdmCCEscapeAction": mdmCCEscapeAction,
       "mdmCCCallDuration": mdmCCCallDuration,
       "mdmCCConnectionFailReason": mdmCCConnectionFailReason,
       "mdmCCStoredDialStringTable": mdmCCStoredDialStringTable,
       "mdmCCStoredDialStringEntry": mdmCCStoredDialStringEntry,
       "mdmCCStoredDialStringIndex": mdmCCStoredDialStringIndex,
       "mdmCCStoredDialString": mdmCCStoredDialString,
       "mdmECTable": mdmECTable,
       "mdmECEntry": mdmECEntry,
       "mdmECErrorControlUsed": mdmECErrorControlUsed,
       "mdmDCTable": mdmDCTable,
       "mdmDCEntry": mdmDCEntry,
       "mdmDCCompressionTypeUsed": mdmDCCompressionTypeUsed,
       "mdmSCTable": mdmSCTable,
       "mdmSCEntry": mdmSCEntry,
       "mdmSCCurrentLineTransmitRate": mdmSCCurrentLineTransmitRate,
       "mdmSCCurrentLineReceiveRate": mdmSCCurrentLineReceiveRate,
       "mdmSCInitialLineTransmitRate": mdmSCInitialLineTransmitRate,
       "mdmSCInitialLineReceiveRate": mdmSCInitialLineReceiveRate,
       "mdmSCModulationSchemeUsed": mdmSCModulationSchemeUsed,
       "mdmStatsTable": mdmStatsTable,
       "mdmStatsEntry": mdmStatsEntry,
       "mdmStatsRingNoAnswers": mdmStatsRingNoAnswers,
       "mdmStatsIncomingConnectionFailures": mdmStatsIncomingConnectionFailures,
       "mdmStatsIncomingConnectionCompletions": mdmStatsIncomingConnectionCompletions,
       "mdmStatsFailedDialAttempts": mdmStatsFailedDialAttempts,
       "mdmStatsOutgoingConnectionFailures": mdmStatsOutgoingConnectionFailures,
       "mdmStatsOutgoingConnectionCompletions": mdmStatsOutgoingConnectionCompletions,
       "mdmStatsRetrains": mdmStatsRetrains,
       "mdmStats2400OrLessConnections": mdmStats2400OrLessConnections,
       "mdmStats2400To14400Connections": mdmStats2400To14400Connections,
       "mdmStatsGreaterThan14400Connections": mdmStatsGreaterThan14400Connections,
       "mdmStatsErrorControlledConnections": mdmStatsErrorControlledConnections,
       "mdmStatsCompressedConnections": mdmStatsCompressedConnections,
       "mdmStatsCompressionEfficiency": mdmStatsCompressionEfficiency,
       "mdmStatsSentOctets": mdmStatsSentOctets,
       "mdmStatsReceivedOctets": mdmStatsReceivedOctets,
       "mdmStatsSentDataFrames": mdmStatsSentDataFrames,
       "mdmStatsReceivedDataFrames": mdmStatsReceivedDataFrames,
       "mdmStatsResentFrames": mdmStatsResentFrames,
       "mdmStatsErrorFrames": mdmStatsErrorFrames,
       "mdmConformance": mdmConformance,
       "mdmCompliances": mdmCompliances,
       "mdmCompliance": mdmCompliance,
       "mdmGroups": mdmGroups,
       "mdmIDGroup": mdmIDGroup,
       "mdmLineInterfaceGroup": mdmLineInterfaceGroup,
       "mdmDTEInterfaceGroup": mdmDTEInterfaceGroup,
       "mdmCallControlGroup": mdmCallControlGroup,
       "mdmErrorControlGroup": mdmErrorControlGroup,
       "mdmDataCompressionGroup": mdmDataCompressionGroup,
       "mdmSignalConvertorGroup": mdmSignalConvertorGroup,
       "mdmStatisticsGroup": mdmStatisticsGroup}
)
