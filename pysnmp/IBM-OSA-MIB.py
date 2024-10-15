# SNMP MIB module (IBM-OSA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IBM-OSA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:38 2024
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

ibmOSAMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 188)
)
ibmOSAMib.setRevisions(
        ("2002-05-23 00:00",
         "2002-03-26 08:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_IbmOSAMibObjects_ObjectIdentity = ObjectIdentity
ibmOSAMibObjects = _IbmOSAMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1)
)
_IbmOSAExpChannelTable_Object = MibTable
ibmOSAExpChannelTable = _IbmOSAExpChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 1)
)
if mibBuilder.loadTexts:
    ibmOSAExpChannelTable.setStatus("current")
_IbmOSAExpChannelEntry_Object = MibTableRow
ibmOSAExpChannelEntry = _IbmOSAExpChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 1, 1)
)
ibmOSAExpChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ibmOSAExpChannelEntry.setStatus("current")


class _IbmOSAExpChannelNumber_Type(OctetString):
    """Custom type ibmOSAExpChannelNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IbmOSAExpChannelNumber_Type.__name__ = "OctetString"
_IbmOSAExpChannelNumber_Object = MibTableColumn
ibmOSAExpChannelNumber = _IbmOSAExpChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 1, 1, 1),
    _IbmOSAExpChannelNumber_Type()
)
ibmOSAExpChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOSAExpChannelNumber.setStatus("current")


class _IbmOSAExpChannelType_Type(Integer32):
    """Custom type ibmOSAExpChannelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            17
        )
    )
    namedValues = NamedValues(
        ("osaDirectExpress", 17)
    )


_IbmOSAExpChannelType_Type.__name__ = "Integer32"
_IbmOSAExpChannelType_Object = MibTableColumn
ibmOSAExpChannelType = _IbmOSAExpChannelType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 1, 1, 2),
    _IbmOSAExpChannelType_Type()
)
ibmOSAExpChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOSAExpChannelType.setStatus("current")


class _IbmOSAExpChannelHdwLevel_Type(Integer32):
    """Custom type ibmOSAExpChannelHdwLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("osaExp150", 2),
          ("osaExp175", 3),
          ("unknown", 1))
    )


_IbmOSAExpChannelHdwLevel_Type.__name__ = "Integer32"
_IbmOSAExpChannelHdwLevel_Object = MibTableColumn
ibmOSAExpChannelHdwLevel = _IbmOSAExpChannelHdwLevel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 1, 1, 3),
    _IbmOSAExpChannelHdwLevel_Type()
)
ibmOSAExpChannelHdwLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOSAExpChannelHdwLevel.setStatus("current")


class _IbmOSAExpChannelSubType_Type(Integer32):
    """Custom type ibmOSAExpChannelSubType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              65,
              81,
              82,
              2304)
        )
    )
    namedValues = NamedValues(
        *(("atmEmulatedEthernet", 2304),
          ("fastEthernet", 81),
          ("gigabitEthernet", 65),
          ("tokenRing", 82),
          ("unknown", 1))
    )


_IbmOSAExpChannelSubType_Type.__name__ = "Integer32"
_IbmOSAExpChannelSubType_Object = MibTableColumn
ibmOSAExpChannelSubType = _IbmOSAExpChannelSubType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 1, 1, 4),
    _IbmOSAExpChannelSubType_Type()
)
ibmOSAExpChannelSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOSAExpChannelSubType.setStatus("current")


class _IbmOSAExpChannelShared_Type(Integer32):
    """Custom type ibmOSAExpChannelShared based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notShared", 0),
          ("shared", 1))
    )


_IbmOSAExpChannelShared_Type.__name__ = "Integer32"
_IbmOSAExpChannelShared_Object = MibTableColumn
ibmOSAExpChannelShared = _IbmOSAExpChannelShared_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 1, 1, 5),
    _IbmOSAExpChannelShared_Type()
)
ibmOSAExpChannelShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOSAExpChannelShared.setStatus("current")


class _IbmOSAExpChannelNodeDesc_Type(OctetString):
    """Custom type ibmOSAExpChannelNodeDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_IbmOSAExpChannelNodeDesc_Type.__name__ = "OctetString"
_IbmOSAExpChannelNodeDesc_Object = MibTableColumn
ibmOSAExpChannelNodeDesc = _IbmOSAExpChannelNodeDesc_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 1, 1, 6),
    _IbmOSAExpChannelNodeDesc_Type()
)
ibmOSAExpChannelNodeDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOSAExpChannelNodeDesc.setStatus("current")


class _IbmOSAExpChannelProcCodeLevel_Type(OctetString):
    """Custom type ibmOSAExpChannelProcCodeLevel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IbmOSAExpChannelProcCodeLevel_Type.__name__ = "OctetString"
_IbmOSAExpChannelProcCodeLevel_Object = MibTableColumn
ibmOSAExpChannelProcCodeLevel = _IbmOSAExpChannelProcCodeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 1, 1, 8),
    _IbmOSAExpChannelProcCodeLevel_Type()
)
ibmOSAExpChannelProcCodeLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOSAExpChannelProcCodeLevel.setStatus("current")


class _IbmOSAExpChannelPCIBusUtil1Min_Type(Integer32):
    """Custom type ibmOSAExpChannelPCIBusUtil1Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IbmOSAExpChannelPCIBusUtil1Min_Type.__name__ = "Integer32"
_IbmOSAExpChannelPCIBusUtil1Min_Object = MibTableColumn
ibmOSAExpChannelPCIBusUtil1Min = _IbmOSAExpChannelPCIBusUtil1Min_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 1, 1, 9),
    _IbmOSAExpChannelPCIBusUtil1Min_Type()
)
ibmOSAExpChannelPCIBusUtil1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOSAExpChannelPCIBusUtil1Min.setStatus("current")


class _IbmOSAExpChannelProcUtil1Min_Type(Integer32):
    """Custom type ibmOSAExpChannelProcUtil1Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IbmOSAExpChannelProcUtil1Min_Type.__name__ = "Integer32"
_IbmOSAExpChannelProcUtil1Min_Object = MibTableColumn
ibmOSAExpChannelProcUtil1Min = _IbmOSAExpChannelProcUtil1Min_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 1, 1, 10),
    _IbmOSAExpChannelProcUtil1Min_Type()
)
ibmOSAExpChannelProcUtil1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOSAExpChannelProcUtil1Min.setStatus("current")


class _IbmOSAExpChannelPCIBusUtil5Min_Type(Integer32):
    """Custom type ibmOSAExpChannelPCIBusUtil5Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IbmOSAExpChannelPCIBusUtil5Min_Type.__name__ = "Integer32"
_IbmOSAExpChannelPCIBusUtil5Min_Object = MibTableColumn
ibmOSAExpChannelPCIBusUtil5Min = _IbmOSAExpChannelPCIBusUtil5Min_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 1, 1, 11),
    _IbmOSAExpChannelPCIBusUtil5Min_Type()
)
ibmOSAExpChannelPCIBusUtil5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOSAExpChannelPCIBusUtil5Min.setStatus("current")


class _IbmOSAExpChannelProcUtil5Min_Type(Integer32):
    """Custom type ibmOSAExpChannelProcUtil5Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IbmOSAExpChannelProcUtil5Min_Type.__name__ = "Integer32"
_IbmOSAExpChannelProcUtil5Min_Object = MibTableColumn
ibmOSAExpChannelProcUtil5Min = _IbmOSAExpChannelProcUtil5Min_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 1, 1, 12),
    _IbmOSAExpChannelProcUtil5Min_Type()
)
ibmOSAExpChannelProcUtil5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOSAExpChannelProcUtil5Min.setStatus("current")


class _IbmOSAExpChannelPCIBusUtilHour_Type(Integer32):
    """Custom type ibmOSAExpChannelPCIBusUtilHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IbmOSAExpChannelPCIBusUtilHour_Type.__name__ = "Integer32"
_IbmOSAExpChannelPCIBusUtilHour_Object = MibTableColumn
ibmOSAExpChannelPCIBusUtilHour = _IbmOSAExpChannelPCIBusUtilHour_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 1, 1, 13),
    _IbmOSAExpChannelPCIBusUtilHour_Type()
)
ibmOSAExpChannelPCIBusUtilHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOSAExpChannelPCIBusUtilHour.setStatus("current")


class _IbmOSAExpChannelProcUtilHour_Type(Integer32):
    """Custom type ibmOSAExpChannelProcUtilHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IbmOSAExpChannelProcUtilHour_Type.__name__ = "Integer32"
_IbmOSAExpChannelProcUtilHour_Object = MibTableColumn
ibmOSAExpChannelProcUtilHour = _IbmOSAExpChannelProcUtilHour_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 1, 1, 14),
    _IbmOSAExpChannelProcUtilHour_Type()
)
ibmOSAExpChannelProcUtilHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOSAExpChannelProcUtilHour.setStatus("current")
_IbmOSAExpPerfTable_Object = MibTable
ibmOSAExpPerfTable = _IbmOSAExpPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 2)
)
if mibBuilder.loadTexts:
    ibmOSAExpPerfTable.setStatus("current")
_IbmOSAExpPerfEntry_Object = MibTableRow
ibmOSAExpPerfEntry = _IbmOSAExpPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 2, 1)
)
ibmOSAExpPerfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ibmOSAExpPerfEntry.setStatus("current")


class _IbmOSAExpPerfDataLP0_Type(OctetString):
    """Custom type ibmOSAExpPerfDataLP0 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_IbmOSAExpPerfDataLP0_Type.__name__ = "OctetString"
_IbmOSAExpPerfDataLP0_Object = MibTableColumn
ibmOSAExpPerfDataLP0 = _IbmOSAExpPerfDataLP0_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 2, 1, 1),
    _IbmOSAExpPerfDataLP0_Type()
)
ibmOSAExpPerfDataLP0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOSAExpPerfDataLP0.setStatus("current")


class _IbmOSAExpPerfDataLP1_Type(OctetString):
    """Custom type ibmOSAExpPerfDataLP1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_IbmOSAExpPerfDataLP1_Type.__name__ = "OctetString"
_IbmOSAExpPerfDataLP1_Object = MibTableColumn
ibmOSAExpPerfDataLP1 = _IbmOSAExpPerfDataLP1_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 2, 1, 2),
    _IbmOSAExpPerfDataLP1_Type()
)
ibmOSAExpPerfDataLP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOSAExpPerfDataLP1.setStatus("current")


class _IbmOSAExpPerfDataLP2_Type(OctetString):
    """Custom type ibmOSAExpPerfDataLP2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_IbmOSAExpPerfDataLP2_Type.__name__ = "OctetString"
_IbmOSAExpPerfDataLP2_Object = MibTableColumn
ibmOSAExpPerfDataLP2 = _IbmOSAExpPerfDataLP2_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 2, 1, 3),
    _IbmOSAExpPerfDataLP2_Type()
)
ibmOSAExpPerfDataLP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOSAExpPerfDataLP2.setStatus("current")


class _IbmOSAExpPerfDataLP3_Type(OctetString):
    """Custom type ibmOSAExpPerfDataLP3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_IbmOSAExpPerfDataLP3_Type.__name__ = "OctetString"
_IbmOSAExpPerfDataLP3_Object = MibTableColumn
ibmOSAExpPerfDataLP3 = _IbmOSAExpPerfDataLP3_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 2, 1, 4),
    _IbmOSAExpPerfDataLP3_Type()
)
ibmOSAExpPerfDataLP3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOSAExpPerfDataLP3.setStatus("current")


class _IbmOSAExpPerfDataLP4_Type(OctetString):
    """Custom type ibmOSAExpPerfDataLP4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_IbmOSAExpPerfDataLP4_Type.__name__ = "OctetString"
_IbmOSAExpPerfDataLP4_Object = MibTableColumn
ibmOSAExpPerfDataLP4 = _IbmOSAExpPerfDataLP4_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 2, 1, 5),
    _IbmOSAExpPerfDataLP4_Type()
)
ibmOSAExpPerfDataLP4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOSAExpPerfDataLP4.setStatus("current")


class _IbmOSAExpPerfDataLP5_Type(OctetString):
    """Custom type ibmOSAExpPerfDataLP5 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_IbmOSAExpPerfDataLP5_Type.__name__ = "OctetString"
_IbmOSAExpPerfDataLP5_Object = MibTableColumn
ibmOSAExpPerfDataLP5 = _IbmOSAExpPerfDataLP5_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 2, 1, 6),
    _IbmOSAExpPerfDataLP5_Type()
)
ibmOSAExpPerfDataLP5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOSAExpPerfDataLP5.setStatus("current")


class _IbmOSAExpPerfDataLP6_Type(OctetString):
    """Custom type ibmOSAExpPerfDataLP6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_IbmOSAExpPerfDataLP6_Type.__name__ = "OctetString"
_IbmOSAExpPerfDataLP6_Object = MibTableColumn
ibmOSAExpPerfDataLP6 = _IbmOSAExpPerfDataLP6_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 2, 1, 7),
    _IbmOSAExpPerfDataLP6_Type()
)
ibmOSAExpPerfDataLP6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOSAExpPerfDataLP6.setStatus("current")


class _IbmOSAExpPerfDataLP7_Type(OctetString):
    """Custom type ibmOSAExpPerfDataLP7 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_IbmOSAExpPerfDataLP7_Type.__name__ = "OctetString"
_IbmOSAExpPerfDataLP7_Object = MibTableColumn
ibmOSAExpPerfDataLP7 = _IbmOSAExpPerfDataLP7_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 2, 1, 8),
    _IbmOSAExpPerfDataLP7_Type()
)
ibmOSAExpPerfDataLP7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOSAExpPerfDataLP7.setStatus("current")


class _IbmOSAExpPerfDataLP8_Type(OctetString):
    """Custom type ibmOSAExpPerfDataLP8 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_IbmOSAExpPerfDataLP8_Type.__name__ = "OctetString"
_IbmOSAExpPerfDataLP8_Object = MibTableColumn
ibmOSAExpPerfDataLP8 = _IbmOSAExpPerfDataLP8_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 2, 1, 9),
    _IbmOSAExpPerfDataLP8_Type()
)
ibmOSAExpPerfDataLP8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOSAExpPerfDataLP8.setStatus("current")


class _IbmOSAExpPerfDataLP9_Type(OctetString):
    """Custom type ibmOSAExpPerfDataLP9 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_IbmOSAExpPerfDataLP9_Type.__name__ = "OctetString"
_IbmOSAExpPerfDataLP9_Object = MibTableColumn
ibmOSAExpPerfDataLP9 = _IbmOSAExpPerfDataLP9_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 2, 1, 10),
    _IbmOSAExpPerfDataLP9_Type()
)
ibmOSAExpPerfDataLP9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOSAExpPerfDataLP9.setStatus("current")


class _IbmOSAExpPerfDataLP10_Type(OctetString):
    """Custom type ibmOSAExpPerfDataLP10 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_IbmOSAExpPerfDataLP10_Type.__name__ = "OctetString"
_IbmOSAExpPerfDataLP10_Object = MibTableColumn
ibmOSAExpPerfDataLP10 = _IbmOSAExpPerfDataLP10_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 2, 1, 11),
    _IbmOSAExpPerfDataLP10_Type()
)
ibmOSAExpPerfDataLP10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOSAExpPerfDataLP10.setStatus("current")


class _IbmOSAExpPerfDataLP11_Type(OctetString):
    """Custom type ibmOSAExpPerfDataLP11 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_IbmOSAExpPerfDataLP11_Type.__name__ = "OctetString"
_IbmOSAExpPerfDataLP11_Object = MibTableColumn
ibmOSAExpPerfDataLP11 = _IbmOSAExpPerfDataLP11_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 2, 1, 12),
    _IbmOSAExpPerfDataLP11_Type()
)
ibmOSAExpPerfDataLP11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOSAExpPerfDataLP11.setStatus("current")


class _IbmOSAExpPerfDataLP12_Type(OctetString):
    """Custom type ibmOSAExpPerfDataLP12 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_IbmOSAExpPerfDataLP12_Type.__name__ = "OctetString"
_IbmOSAExpPerfDataLP12_Object = MibTableColumn
ibmOSAExpPerfDataLP12 = _IbmOSAExpPerfDataLP12_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 2, 1, 13),
    _IbmOSAExpPerfDataLP12_Type()
)
ibmOSAExpPerfDataLP12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOSAExpPerfDataLP12.setStatus("current")


class _IbmOSAExpPerfDataLP13_Type(OctetString):
    """Custom type ibmOSAExpPerfDataLP13 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_IbmOSAExpPerfDataLP13_Type.__name__ = "OctetString"
_IbmOSAExpPerfDataLP13_Object = MibTableColumn
ibmOSAExpPerfDataLP13 = _IbmOSAExpPerfDataLP13_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 2, 1, 14),
    _IbmOSAExpPerfDataLP13_Type()
)
ibmOSAExpPerfDataLP13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOSAExpPerfDataLP13.setStatus("current")


class _IbmOSAExpPerfDataLP14_Type(OctetString):
    """Custom type ibmOSAExpPerfDataLP14 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_IbmOSAExpPerfDataLP14_Type.__name__ = "OctetString"
_IbmOSAExpPerfDataLP14_Object = MibTableColumn
ibmOSAExpPerfDataLP14 = _IbmOSAExpPerfDataLP14_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 2, 1, 15),
    _IbmOSAExpPerfDataLP14_Type()
)
ibmOSAExpPerfDataLP14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOSAExpPerfDataLP14.setStatus("current")


class _IbmOSAExpPerfDataLP15_Type(OctetString):
    """Custom type ibmOSAExpPerfDataLP15 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_IbmOSAExpPerfDataLP15_Type.__name__ = "OctetString"
_IbmOSAExpPerfDataLP15_Object = MibTableColumn
ibmOSAExpPerfDataLP15 = _IbmOSAExpPerfDataLP15_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 2, 1, 16),
    _IbmOSAExpPerfDataLP15_Type()
)
ibmOSAExpPerfDataLP15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOSAExpPerfDataLP15.setStatus("current")
_IbmOSAExpPETable_Object = MibTable
ibmOSAExpPETable = _IbmOSAExpPETable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 3)
)
if mibBuilder.loadTexts:
    ibmOSAExpPETable.setStatus("current")
_IbmOSAExpPEEntry_Object = MibTableRow
ibmOSAExpPEEntry = _IbmOSAExpPEEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 3, 1)
)
ibmOSAExpPEEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ibmOSAExpPEEntry.setStatus("current")


class _IbmOSAExpPEMaxSizeArpCache_Type(Integer32):
    """Custom type ibmOSAExpPEMaxSizeArpCache based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 214783647),
    )


_IbmOSAExpPEMaxSizeArpCache_Type.__name__ = "Integer32"
_IbmOSAExpPEMaxSizeArpCache_Object = MibTableColumn
ibmOSAExpPEMaxSizeArpCache = _IbmOSAExpPEMaxSizeArpCache_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 3, 1, 1),
    _IbmOSAExpPEMaxSizeArpCache_Type()
)
ibmOSAExpPEMaxSizeArpCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOSAExpPEMaxSizeArpCache.setStatus("current")
_IbmOSAExpPEArpPendingEntries_Type = Gauge32
_IbmOSAExpPEArpPendingEntries_Object = MibTableColumn
ibmOSAExpPEArpPendingEntries = _IbmOSAExpPEArpPendingEntries_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 3, 1, 2),
    _IbmOSAExpPEArpPendingEntries_Type()
)
ibmOSAExpPEArpPendingEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOSAExpPEArpPendingEntries.setStatus("current")
_IbmOSAExpPEArpActiveEntries_Type = Gauge32
_IbmOSAExpPEArpActiveEntries_Object = MibTableColumn
ibmOSAExpPEArpActiveEntries = _IbmOSAExpPEArpActiveEntries_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 3, 1, 3),
    _IbmOSAExpPEArpActiveEntries_Type()
)
ibmOSAExpPEArpActiveEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOSAExpPEArpActiveEntries.setStatus("current")
_IbmOSAExpPEIPEntries_Type = Gauge32
_IbmOSAExpPEIPEntries_Object = MibTableColumn
ibmOSAExpPEIPEntries = _IbmOSAExpPEIPEntries_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 3, 1, 4),
    _IbmOSAExpPEIPEntries_Type()
)
ibmOSAExpPEIPEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOSAExpPEIPEntries.setStatus("current")
_IbmOSAExpPEMulticastEntries_Type = Gauge32
_IbmOSAExpPEMulticastEntries_Object = MibTableColumn
ibmOSAExpPEMulticastEntries = _IbmOSAExpPEMulticastEntries_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 3, 1, 5),
    _IbmOSAExpPEMulticastEntries_Type()
)
ibmOSAExpPEMulticastEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOSAExpPEMulticastEntries.setStatus("current")


class _IbmOSAExpPEMulticastData_Type(OctetString):
    """Custom type ibmOSAExpPEMulticastData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3360, 3360),
    )


_IbmOSAExpPEMulticastData_Type.__name__ = "OctetString"
_IbmOSAExpPEMulticastData_Object = MibTableColumn
ibmOSAExpPEMulticastData = _IbmOSAExpPEMulticastData_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 3, 1, 6),
    _IbmOSAExpPEMulticastData_Type()
)
ibmOSAExpPEMulticastData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOSAExpPEMulticastData.setStatus("current")
_IbmOSAExpEthPortTable_Object = MibTable
ibmOSAExpEthPortTable = _IbmOSAExpEthPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 4)
)
if mibBuilder.loadTexts:
    ibmOSAExpEthPortTable.setStatus("current")
_IbmOSAExpEthPortEntry_Object = MibTableRow
ibmOSAExpEthPortEntry = _IbmOSAExpEthPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 4, 1)
)
ibmOSAExpEthPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ibmOSAExpEthPortEntry.setStatus("current")


class _IbmOsaExpEthPortNumber_Type(Integer32):
    """Custom type ibmOsaExpEthPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_IbmOsaExpEthPortNumber_Type.__name__ = "Integer32"
_IbmOsaExpEthPortNumber_Object = MibTableColumn
ibmOsaExpEthPortNumber = _IbmOsaExpEthPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 4, 1, 1),
    _IbmOsaExpEthPortNumber_Type()
)
ibmOsaExpEthPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpEthPortNumber.setStatus("current")


class _IbmOsaExpEthPortType_Type(Integer32):
    """Custom type ibmOsaExpEthPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(65,
              81)
        )
    )
    namedValues = NamedValues(
        *(("fastEthernet", 81),
          ("gigabitEthernet", 65))
    )


_IbmOsaExpEthPortType_Type.__name__ = "Integer32"
_IbmOsaExpEthPortType_Object = MibTableColumn
ibmOsaExpEthPortType = _IbmOsaExpEthPortType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 4, 1, 2),
    _IbmOsaExpEthPortType_Type()
)
ibmOsaExpEthPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpEthPortType.setStatus("current")


class _IbmOsaExpEthLanTrafficState_Type(Integer32):
    """Custom type ibmOsaExpEthLanTrafficState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("configuredOffline", 8),
          ("definitionError", 7),
          ("disabled", 5),
          ("disabling", 3),
          ("enabled", 4),
          ("enabling", 2),
          ("linkMonitor", 6),
          ("unavailable", 1),
          ("undefined", 0))
    )


_IbmOsaExpEthLanTrafficState_Type.__name__ = "Integer32"
_IbmOsaExpEthLanTrafficState_Object = MibTableColumn
ibmOsaExpEthLanTrafficState = _IbmOsaExpEthLanTrafficState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 4, 1, 3),
    _IbmOsaExpEthLanTrafficState_Type()
)
ibmOsaExpEthLanTrafficState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpEthLanTrafficState.setStatus("current")


class _IbmOsaExpEthServiceMode_Type(Integer32):
    """Custom type ibmOsaExpEthServiceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inServiceMode", 1),
          ("notInServiceMode", 0))
    )


_IbmOsaExpEthServiceMode_Type.__name__ = "Integer32"
_IbmOsaExpEthServiceMode_Object = MibTableColumn
ibmOsaExpEthServiceMode = _IbmOsaExpEthServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 4, 1, 4),
    _IbmOsaExpEthServiceMode_Type()
)
ibmOsaExpEthServiceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpEthServiceMode.setStatus("current")


class _IbmOsaExpEthDisabledStatus_Type(Bits):
    """Custom type ibmOsaExpEthDisabledStatus based on Bits"""
    namedValues = NamedValues(
        *(("configurationChange", 12),
          ("internalPortFailure", 1),
          ("linkFailureThresholdExceeded", 13),
          ("networkRequest", 10),
          ("osasfRequest", 11),
          ("portTemporarilyDisabled", 6),
          ("reserved0", 0),
          ("reserved14", 14),
          ("reserved15", 15),
          ("reserved2", 2),
          ("reserved3", 3),
          ("reserved4", 4),
          ("reserved5", 5),
          ("reserved7", 7),
          ("reserved8", 8),
          ("serviceProcessorRequest", 9))
    )

_IbmOsaExpEthDisabledStatus_Type.__name__ = "Bits"
_IbmOsaExpEthDisabledStatus_Object = MibTableColumn
ibmOsaExpEthDisabledStatus = _IbmOsaExpEthDisabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 4, 1, 5),
    _IbmOsaExpEthDisabledStatus_Type()
)
ibmOsaExpEthDisabledStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpEthDisabledStatus.setStatus("current")


class _IbmOsaExpEthConfigName_Type(DisplayString):
    """Custom type ibmOsaExpEthConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 34),
    )


_IbmOsaExpEthConfigName_Type.__name__ = "DisplayString"
_IbmOsaExpEthConfigName_Object = MibTableColumn
ibmOsaExpEthConfigName = _IbmOsaExpEthConfigName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 4, 1, 6),
    _IbmOsaExpEthConfigName_Type()
)
ibmOsaExpEthConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpEthConfigName.setStatus("current")


class _IbmOsaExpEthConfigSpeedMode_Type(Integer32):
    """Custom type ibmOsaExpEthConfigSpeedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("autoNegotiate", 0),
          ("notValidGigabit", -1),
          ("oneHundredMbFullDuplex", 4),
          ("oneHundredMbHalfDuplex", 3),
          ("oneThousandMbFullDuplex", 6),
          ("tenMbFullDuplex", 2),
          ("tenMbHalfDuplex", 1))
    )


_IbmOsaExpEthConfigSpeedMode_Type.__name__ = "Integer32"
_IbmOsaExpEthConfigSpeedMode_Object = MibTableColumn
ibmOsaExpEthConfigSpeedMode = _IbmOsaExpEthConfigSpeedMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 4, 1, 7),
    _IbmOsaExpEthConfigSpeedMode_Type()
)
ibmOsaExpEthConfigSpeedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpEthConfigSpeedMode.setStatus("current")
if mibBuilder.loadTexts:
    ibmOsaExpEthConfigSpeedMode.setUnits("Megabits per second")


class _IbmOsaExpEthActiveSpeedMode_Type(Integer32):
    """Custom type ibmOsaExpEthActiveSpeedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("oneHundredMbFullDuplex", 4),
          ("oneHundredMbHalfDuplex", 3),
          ("oneThousandMbFullDuplex", 6),
          ("tenMbFullDuplex", 2),
          ("tenMbHalfDuplex", 1),
          ("unknown", 0))
    )


_IbmOsaExpEthActiveSpeedMode_Type.__name__ = "Integer32"
_IbmOsaExpEthActiveSpeedMode_Object = MibTableColumn
ibmOsaExpEthActiveSpeedMode = _IbmOsaExpEthActiveSpeedMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 4, 1, 8),
    _IbmOsaExpEthActiveSpeedMode_Type()
)
ibmOsaExpEthActiveSpeedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpEthActiveSpeedMode.setStatus("current")
if mibBuilder.loadTexts:
    ibmOsaExpEthActiveSpeedMode.setUnits("Megabits per second")


class _IbmOsaExpEthMacAddrActive_Type(OctetString):
    """Custom type ibmOsaExpEthMacAddrActive based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmOsaExpEthMacAddrActive_Type.__name__ = "OctetString"
_IbmOsaExpEthMacAddrActive_Object = MibTableColumn
ibmOsaExpEthMacAddrActive = _IbmOsaExpEthMacAddrActive_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 4, 1, 9),
    _IbmOsaExpEthMacAddrActive_Type()
)
ibmOsaExpEthMacAddrActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpEthMacAddrActive.setStatus("current")


class _IbmOsaExpEthMacAddrBurntIn_Type(OctetString):
    """Custom type ibmOsaExpEthMacAddrBurntIn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmOsaExpEthMacAddrBurntIn_Type.__name__ = "OctetString"
_IbmOsaExpEthMacAddrBurntIn_Object = MibTableColumn
ibmOsaExpEthMacAddrBurntIn = _IbmOsaExpEthMacAddrBurntIn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 4, 1, 10),
    _IbmOsaExpEthMacAddrBurntIn_Type()
)
ibmOsaExpEthMacAddrBurntIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpEthMacAddrBurntIn.setStatus("current")


class _IbmOsaExpEthUserData_Type(DisplayString):
    """Custom type ibmOsaExpEthUserData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IbmOsaExpEthUserData_Type.__name__ = "DisplayString"
_IbmOsaExpEthUserData_Object = MibTableColumn
ibmOsaExpEthUserData = _IbmOsaExpEthUserData_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 4, 1, 11),
    _IbmOsaExpEthUserData_Type()
)
ibmOsaExpEthUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpEthUserData.setStatus("current")
_IbmOsaExpEthOutPackets_Type = Counter32
_IbmOsaExpEthOutPackets_Object = MibTableColumn
ibmOsaExpEthOutPackets = _IbmOsaExpEthOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 4, 1, 12),
    _IbmOsaExpEthOutPackets_Type()
)
ibmOsaExpEthOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpEthOutPackets.setStatus("current")
_IbmOsaExpEthInPackets_Type = Counter32
_IbmOsaExpEthInPackets_Object = MibTableColumn
ibmOsaExpEthInPackets = _IbmOsaExpEthInPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 4, 1, 13),
    _IbmOsaExpEthInPackets_Type()
)
ibmOsaExpEthInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpEthInPackets.setStatus("current")
_IbmOsaExpEthInGroupFrames_Type = Counter32
_IbmOsaExpEthInGroupFrames_Object = MibTableColumn
ibmOsaExpEthInGroupFrames = _IbmOsaExpEthInGroupFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 4, 1, 14),
    _IbmOsaExpEthInGroupFrames_Type()
)
ibmOsaExpEthInGroupFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpEthInGroupFrames.setStatus("current")
_IbmOsaExpEthInBroadcastFrames_Type = Counter32
_IbmOsaExpEthInBroadcastFrames_Object = MibTableColumn
ibmOsaExpEthInBroadcastFrames = _IbmOsaExpEthInBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 4, 1, 15),
    _IbmOsaExpEthInBroadcastFrames_Type()
)
ibmOsaExpEthInBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpEthInBroadcastFrames.setStatus("current")


class _IbmOsaExpEthPortName_Type(DisplayString):
    """Custom type ibmOsaExpEthPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IbmOsaExpEthPortName_Type.__name__ = "DisplayString"
_IbmOsaExpEthPortName_Object = MibTableColumn
ibmOsaExpEthPortName = _IbmOsaExpEthPortName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 4, 1, 16),
    _IbmOsaExpEthPortName_Type()
)
ibmOsaExpEthPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpEthPortName.setStatus("current")
_IbmOsaExpEthInUnknownIPFrames_Type = Counter32
_IbmOsaExpEthInUnknownIPFrames_Object = MibTableColumn
ibmOsaExpEthInUnknownIPFrames = _IbmOsaExpEthInUnknownIPFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 4, 1, 17),
    _IbmOsaExpEthInUnknownIPFrames_Type()
)
ibmOsaExpEthInUnknownIPFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpEthInUnknownIPFrames.setStatus("current")


class _IbmOsaExpEthGroupAddrTable_Type(OctetString):
    """Custom type ibmOsaExpEthGroupAddrTable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_IbmOsaExpEthGroupAddrTable_Type.__name__ = "OctetString"
_IbmOsaExpEthGroupAddrTable_Object = MibTableColumn
ibmOsaExpEthGroupAddrTable = _IbmOsaExpEthGroupAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 4, 1, 18),
    _IbmOsaExpEthGroupAddrTable_Type()
)
ibmOsaExpEthGroupAddrTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpEthGroupAddrTable.setStatus("current")
_IbmOSAExpTRPortTable_Object = MibTable
ibmOSAExpTRPortTable = _IbmOSAExpTRPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5)
)
if mibBuilder.loadTexts:
    ibmOSAExpTRPortTable.setStatus("current")
_IbmOSAExpTRPortEntry_Object = MibTableRow
ibmOSAExpTRPortEntry = _IbmOSAExpTRPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1)
)
ibmOSAExpTRPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ibmOSAExpTRPortEntry.setStatus("current")


class _IbmOsaExpTRPortNumber_Type(Integer32):
    """Custom type ibmOsaExpTRPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_IbmOsaExpTRPortNumber_Type.__name__ = "Integer32"
_IbmOsaExpTRPortNumber_Object = MibTableColumn
ibmOsaExpTRPortNumber = _IbmOsaExpTRPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 1),
    _IbmOsaExpTRPortNumber_Type()
)
ibmOsaExpTRPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRPortNumber.setStatus("current")


class _IbmOsaExpTRPortType_Type(Integer32):
    """Custom type ibmOsaExpTRPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            82
        )
    )
    namedValues = NamedValues(
        ("tokenring", 82)
    )


_IbmOsaExpTRPortType_Type.__name__ = "Integer32"
_IbmOsaExpTRPortType_Object = MibTableColumn
ibmOsaExpTRPortType = _IbmOsaExpTRPortType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 2),
    _IbmOsaExpTRPortType_Type()
)
ibmOsaExpTRPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRPortType.setStatus("current")


class _IbmOsaExpTRLanTrafficState_Type(Integer32):
    """Custom type ibmOsaExpTRLanTrafficState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("configuredOffline", 8),
          ("definitionError", 7),
          ("disabled", 5),
          ("disabling", 3),
          ("enabled", 4),
          ("enabling", 2),
          ("linkMonitor", 6),
          ("unavailable", 1),
          ("undefined", 0))
    )


_IbmOsaExpTRLanTrafficState_Type.__name__ = "Integer32"
_IbmOsaExpTRLanTrafficState_Object = MibTableColumn
ibmOsaExpTRLanTrafficState = _IbmOsaExpTRLanTrafficState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 3),
    _IbmOsaExpTRLanTrafficState_Type()
)
ibmOsaExpTRLanTrafficState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRLanTrafficState.setStatus("current")


class _IbmOsaExpTRServiceMode_Type(Integer32):
    """Custom type ibmOsaExpTRServiceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inServiceMode", 1),
          ("notInServiceMode", 0))
    )


_IbmOsaExpTRServiceMode_Type.__name__ = "Integer32"
_IbmOsaExpTRServiceMode_Object = MibTableColumn
ibmOsaExpTRServiceMode = _IbmOsaExpTRServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 4),
    _IbmOsaExpTRServiceMode_Type()
)
ibmOsaExpTRServiceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRServiceMode.setStatus("current")


class _IbmOsaExpTRDisabledStatus_Type(Bits):
    """Custom type ibmOsaExpTRDisabledStatus based on Bits"""
    namedValues = NamedValues(
        *(("configurationChange", 12),
          ("internalPortFailure", 1),
          ("linkFailureThresholdExceeded", 13),
          ("networkRequest", 10),
          ("osasfRequest", 11),
          ("portTemporarilyDisabled", 6),
          ("reserved0", 0),
          ("reserved14", 14),
          ("reserved15", 15),
          ("reserved2", 2),
          ("reserved3", 3),
          ("reserved4", 4),
          ("reserved5", 5),
          ("reserved7", 7),
          ("reserved8", 8),
          ("serviceProcessorRequest", 9))
    )

_IbmOsaExpTRDisabledStatus_Type.__name__ = "Bits"
_IbmOsaExpTRDisabledStatus_Object = MibTableColumn
ibmOsaExpTRDisabledStatus = _IbmOsaExpTRDisabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 5),
    _IbmOsaExpTRDisabledStatus_Type()
)
ibmOsaExpTRDisabledStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRDisabledStatus.setStatus("current")


class _IbmOsaExpTRConfigName_Type(DisplayString):
    """Custom type ibmOsaExpTRConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 34),
    )


_IbmOsaExpTRConfigName_Type.__name__ = "DisplayString"
_IbmOsaExpTRConfigName_Object = MibTableColumn
ibmOsaExpTRConfigName = _IbmOsaExpTRConfigName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 6),
    _IbmOsaExpTRConfigName_Type()
)
ibmOsaExpTRConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRConfigName.setStatus("current")


class _IbmOsaExpTRMacAddrActive_Type(OctetString):
    """Custom type ibmOsaExpTRMacAddrActive based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmOsaExpTRMacAddrActive_Type.__name__ = "OctetString"
_IbmOsaExpTRMacAddrActive_Object = MibTableColumn
ibmOsaExpTRMacAddrActive = _IbmOsaExpTRMacAddrActive_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 7),
    _IbmOsaExpTRMacAddrActive_Type()
)
ibmOsaExpTRMacAddrActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRMacAddrActive.setStatus("current")


class _IbmOsaExpTRMacAddrBurntIn_Type(OctetString):
    """Custom type ibmOsaExpTRMacAddrBurntIn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmOsaExpTRMacAddrBurntIn_Type.__name__ = "OctetString"
_IbmOsaExpTRMacAddrBurntIn_Object = MibTableColumn
ibmOsaExpTRMacAddrBurntIn = _IbmOsaExpTRMacAddrBurntIn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 8),
    _IbmOsaExpTRMacAddrBurntIn_Type()
)
ibmOsaExpTRMacAddrBurntIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRMacAddrBurntIn.setStatus("current")


class _IbmOsaExpTRConfigSpeedMode_Type(Integer32):
    """Custom type ibmOsaExpTRConfigSpeedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("autoNegotiate", 0),
          ("fourMbFullDuplex", 2),
          ("fourMbHalfDuplex", 1),
          ("oneHundredMbFullDuplex", 6),
          ("sixteenMbFullDuplex", 4),
          ("sixteenMbHalfDuplex", 3))
    )


_IbmOsaExpTRConfigSpeedMode_Type.__name__ = "Integer32"
_IbmOsaExpTRConfigSpeedMode_Object = MibTableColumn
ibmOsaExpTRConfigSpeedMode = _IbmOsaExpTRConfigSpeedMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 9),
    _IbmOsaExpTRConfigSpeedMode_Type()
)
ibmOsaExpTRConfigSpeedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRConfigSpeedMode.setStatus("current")
if mibBuilder.loadTexts:
    ibmOsaExpTRConfigSpeedMode.setUnits("Megabits per second")


class _IbmOsaExpTRActiveSpeedMode_Type(Integer32):
    """Custom type ibmOsaExpTRActiveSpeedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("fourMbFullDuplex", 2),
          ("fourMbHalfDuplex", 1),
          ("oneHundredMbFullDuplex", 6),
          ("sixteenMbFullDuplex", 4),
          ("sixteenMbHalfDuplex", 3),
          ("unknown", 0))
    )


_IbmOsaExpTRActiveSpeedMode_Type.__name__ = "Integer32"
_IbmOsaExpTRActiveSpeedMode_Object = MibTableColumn
ibmOsaExpTRActiveSpeedMode = _IbmOsaExpTRActiveSpeedMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 10),
    _IbmOsaExpTRActiveSpeedMode_Type()
)
ibmOsaExpTRActiveSpeedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRActiveSpeedMode.setStatus("current")
if mibBuilder.loadTexts:
    ibmOsaExpTRActiveSpeedMode.setUnits("Megabits per second")


class _IbmOsaExpTRUserData_Type(DisplayString):
    """Custom type ibmOsaExpTRUserData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IbmOsaExpTRUserData_Type.__name__ = "DisplayString"
_IbmOsaExpTRUserData_Object = MibTableColumn
ibmOsaExpTRUserData = _IbmOsaExpTRUserData_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 11),
    _IbmOsaExpTRUserData_Type()
)
ibmOsaExpTRUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRUserData.setStatus("current")


class _IbmOsaExpTRPortName_Type(DisplayString):
    """Custom type ibmOsaExpTRPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IbmOsaExpTRPortName_Type.__name__ = "DisplayString"
_IbmOsaExpTRPortName_Object = MibTableColumn
ibmOsaExpTRPortName = _IbmOsaExpTRPortName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 12),
    _IbmOsaExpTRPortName_Type()
)
ibmOsaExpTRPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRPortName.setStatus("current")


class _IbmOsaExpTRGroupAddrTable_Type(OctetString):
    """Custom type ibmOsaExpTRGroupAddrTable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_IbmOsaExpTRGroupAddrTable_Type.__name__ = "OctetString"
_IbmOsaExpTRGroupAddrTable_Object = MibTableColumn
ibmOsaExpTRGroupAddrTable = _IbmOsaExpTRGroupAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 13),
    _IbmOsaExpTRGroupAddrTable_Type()
)
ibmOsaExpTRGroupAddrTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRGroupAddrTable.setStatus("current")


class _IbmOsaExpTRFunctionalAddr_Type(OctetString):
    """Custom type ibmOsaExpTRFunctionalAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IbmOsaExpTRFunctionalAddr_Type.__name__ = "OctetString"
_IbmOsaExpTRFunctionalAddr_Object = MibTableColumn
ibmOsaExpTRFunctionalAddr = _IbmOsaExpTRFunctionalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 14),
    _IbmOsaExpTRFunctionalAddr_Type()
)
ibmOsaExpTRFunctionalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRFunctionalAddr.setStatus("current")


class _IbmOsaExpTRRingStatus_Type(Bits):
    """Custom type ibmOsaExpTRRingStatus based on Bits"""
    namedValues = NamedValues(
        *(("autoRemovalError", 21),
          ("counterOverflow", 24),
          ("fdxProtocol", 22),
          ("fourMbFullDuplex", 30),
          ("fourMbHalfDuplex", 31),
          ("hardError", 17),
          ("lobeWireFault", 20),
          ("noStatusOpenNotCompleted", 14),
          ("openInFDXmode", 29),
          ("removeReceived", 23),
          ("reserved0", 0),
          ("reserved1", 1),
          ("reserved10", 10),
          ("reserved11", 11),
          ("reserved12", 12),
          ("reserved13", 13),
          ("reserved15", 15),
          ("reserved19", 19),
          ("reserved2", 2),
          ("reserved29", 28),
          ("reserved3", 3),
          ("reserved4", 4),
          ("reserved5", 5),
          ("reserved6", 6),
          ("reserved7", 7),
          ("reserved8", 8),
          ("reserved9", 9),
          ("ringRecovery", 26),
          ("sRCounterOverflow", 27),
          ("signalLoss", 16),
          ("singleStation", 25),
          ("softError", 18))
    )

_IbmOsaExpTRRingStatus_Type.__name__ = "Bits"
_IbmOsaExpTRRingStatus_Object = MibTableColumn
ibmOsaExpTRRingStatus = _IbmOsaExpTRRingStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 15),
    _IbmOsaExpTRRingStatus_Type()
)
ibmOsaExpTRRingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRRingStatus.setStatus("current")
_IbmOsaExpTRAllowAccessPriority_Type = Integer32
_IbmOsaExpTRAllowAccessPriority_Object = MibTableColumn
ibmOsaExpTRAllowAccessPriority = _IbmOsaExpTRAllowAccessPriority_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 16),
    _IbmOsaExpTRAllowAccessPriority_Type()
)
ibmOsaExpTRAllowAccessPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRAllowAccessPriority.setStatus("current")


class _IbmOsaExpTREarlyTokenRelease_Type(Integer32):
    """Custom type ibmOsaExpTREarlyTokenRelease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 0))
    )


_IbmOsaExpTREarlyTokenRelease_Type.__name__ = "Integer32"
_IbmOsaExpTREarlyTokenRelease_Object = MibTableColumn
ibmOsaExpTREarlyTokenRelease = _IbmOsaExpTREarlyTokenRelease_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 17),
    _IbmOsaExpTREarlyTokenRelease_Type()
)
ibmOsaExpTREarlyTokenRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTREarlyTokenRelease.setStatus("current")


class _IbmOsaExpTRBeaconingAddress_Type(OctetString):
    """Custom type ibmOsaExpTRBeaconingAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmOsaExpTRBeaconingAddress_Type.__name__ = "OctetString"
_IbmOsaExpTRBeaconingAddress_Object = MibTableColumn
ibmOsaExpTRBeaconingAddress = _IbmOsaExpTRBeaconingAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 18),
    _IbmOsaExpTRBeaconingAddress_Type()
)
ibmOsaExpTRBeaconingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRBeaconingAddress.setStatus("current")


class _IbmOsaExpTRUpstreamNeighbor_Type(OctetString):
    """Custom type ibmOsaExpTRUpstreamNeighbor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmOsaExpTRUpstreamNeighbor_Type.__name__ = "OctetString"
_IbmOsaExpTRUpstreamNeighbor_Object = MibTableColumn
ibmOsaExpTRUpstreamNeighbor = _IbmOsaExpTRUpstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 19),
    _IbmOsaExpTRUpstreamNeighbor_Type()
)
ibmOsaExpTRUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRUpstreamNeighbor.setStatus("current")


class _IbmOsaExpTRRingState_Type(Integer32):
    """Custom type ibmOsaExpTRRingState based on Integer32"""
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
        *(("closed", 2),
          ("closing", 4),
          ("openFailure", 5),
          ("opened", 1),
          ("opening", 3),
          ("ringFailure", 6))
    )


_IbmOsaExpTRRingState_Type.__name__ = "Integer32"
_IbmOsaExpTRRingState_Object = MibTableColumn
ibmOsaExpTRRingState = _IbmOsaExpTRRingState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 20),
    _IbmOsaExpTRRingState_Type()
)
ibmOsaExpTRRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRRingState.setStatus("current")


class _IbmOsaExpTRRingOpenStatus_Type(Integer32):
    """Custom type ibmOsaExpTRRingOpenStatus based on Integer32"""
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
              26)
        )
    )
    namedValues = NamedValues(
        *(("accessProtocolDenied", 17),
          ("activeMonPresRec", 15),
          ("badParameter", 2),
          ("beaconBeforeOpen", 20),
          ("beaconing", 7),
          ("claimTokenRec", 13),
          ("duplicateMAC", 8),
          ("fDXInsDeniedDACfailOnBeaconTest", 19),
          ("fDXInsDeniedDACfailOnOpen", 18),
          ("heartbeatFailBeforeOpenCompleted", 24),
          ("heartbeatFailDuringBeaconTest", 25),
          ("insertTimerExpDuringBeaconTest", 22),
          ("insertTimerExpDuringDAC", 21),
          ("insertionTimeout", 5),
          ("lobeFailed", 3),
          ("lobeMedizTestFailure", 23),
          ("noOpen", 1),
          ("open", 11),
          ("recBeaconFrameWithInvalidSA", 26),
          ("removeReceived", 10),
          ("requestFailed", 9),
          ("ringFailed", 6),
          ("ringPurgeFramRec", 14),
          ("sARecFrameNotEqualNAUNs", 12),
          ("signalLoss", 4),
          ("standbyMonPresRec", 16))
    )


_IbmOsaExpTRRingOpenStatus_Type.__name__ = "Integer32"
_IbmOsaExpTRRingOpenStatus_Object = MibTableColumn
ibmOsaExpTRRingOpenStatus = _IbmOsaExpTRRingOpenStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 21),
    _IbmOsaExpTRRingOpenStatus_Type()
)
ibmOsaExpTRRingOpenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRRingOpenStatus.setStatus("current")
_IbmOsaExpTRPacketsTransmitted_Type = Counter32
_IbmOsaExpTRPacketsTransmitted_Object = MibTableColumn
ibmOsaExpTRPacketsTransmitted = _IbmOsaExpTRPacketsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 22),
    _IbmOsaExpTRPacketsTransmitted_Type()
)
ibmOsaExpTRPacketsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRPacketsTransmitted.setStatus("current")
if mibBuilder.loadTexts:
    ibmOsaExpTRPacketsTransmitted.setUnits("packets")
_IbmOsaExpTRPacketsReceived_Type = Counter32
_IbmOsaExpTRPacketsReceived_Object = MibTableColumn
ibmOsaExpTRPacketsReceived = _IbmOsaExpTRPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 23),
    _IbmOsaExpTRPacketsReceived_Type()
)
ibmOsaExpTRPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRPacketsReceived.setStatus("current")
if mibBuilder.loadTexts:
    ibmOsaExpTRPacketsReceived.setUnits("packets")
_IbmOsaExpTRLineErrorCount_Type = Counter32
_IbmOsaExpTRLineErrorCount_Object = MibTableColumn
ibmOsaExpTRLineErrorCount = _IbmOsaExpTRLineErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 24),
    _IbmOsaExpTRLineErrorCount_Type()
)
ibmOsaExpTRLineErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRLineErrorCount.setStatus("current")
_IbmOsaExpTRBurstErrorCount_Type = Counter32
_IbmOsaExpTRBurstErrorCount_Object = MibTableColumn
ibmOsaExpTRBurstErrorCount = _IbmOsaExpTRBurstErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 25),
    _IbmOsaExpTRBurstErrorCount_Type()
)
ibmOsaExpTRBurstErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRBurstErrorCount.setStatus("current")
_IbmOsaExpTRACErrorCount_Type = Counter32
_IbmOsaExpTRACErrorCount_Object = MibTableColumn
ibmOsaExpTRACErrorCount = _IbmOsaExpTRACErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 26),
    _IbmOsaExpTRACErrorCount_Type()
)
ibmOsaExpTRACErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRACErrorCount.setStatus("current")
_IbmOsaExpTRAbortTransErrorCount_Type = Counter32
_IbmOsaExpTRAbortTransErrorCount_Object = MibTableColumn
ibmOsaExpTRAbortTransErrorCount = _IbmOsaExpTRAbortTransErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 27),
    _IbmOsaExpTRAbortTransErrorCount_Type()
)
ibmOsaExpTRAbortTransErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRAbortTransErrorCount.setStatus("current")
_IbmOsaExpTRInternalErrorCount_Type = Counter32
_IbmOsaExpTRInternalErrorCount_Object = MibTableColumn
ibmOsaExpTRInternalErrorCount = _IbmOsaExpTRInternalErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 28),
    _IbmOsaExpTRInternalErrorCount_Type()
)
ibmOsaExpTRInternalErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRInternalErrorCount.setStatus("current")
_IbmOsaExpTRLostFrameErrorCount_Type = Counter32
_IbmOsaExpTRLostFrameErrorCount_Object = MibTableColumn
ibmOsaExpTRLostFrameErrorCount = _IbmOsaExpTRLostFrameErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 29),
    _IbmOsaExpTRLostFrameErrorCount_Type()
)
ibmOsaExpTRLostFrameErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRLostFrameErrorCount.setStatus("current")
_IbmOsaExpTRRcvCongestionCount_Type = Counter32
_IbmOsaExpTRRcvCongestionCount_Object = MibTableColumn
ibmOsaExpTRRcvCongestionCount = _IbmOsaExpTRRcvCongestionCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 30),
    _IbmOsaExpTRRcvCongestionCount_Type()
)
ibmOsaExpTRRcvCongestionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRRcvCongestionCount.setStatus("current")
_IbmOsaExpTRFrameCopyErrorCount_Type = Counter32
_IbmOsaExpTRFrameCopyErrorCount_Object = MibTableColumn
ibmOsaExpTRFrameCopyErrorCount = _IbmOsaExpTRFrameCopyErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 31),
    _IbmOsaExpTRFrameCopyErrorCount_Type()
)
ibmOsaExpTRFrameCopyErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRFrameCopyErrorCount.setStatus("current")
_IbmOsaExpTRTokenErrorCount_Type = Counter32
_IbmOsaExpTRTokenErrorCount_Object = MibTableColumn
ibmOsaExpTRTokenErrorCount = _IbmOsaExpTRTokenErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 32),
    _IbmOsaExpTRTokenErrorCount_Type()
)
ibmOsaExpTRTokenErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRTokenErrorCount.setStatus("current")
_IbmOsaExpTRFullDuplexErrorCount_Type = Counter32
_IbmOsaExpTRFullDuplexErrorCount_Object = MibTableColumn
ibmOsaExpTRFullDuplexErrorCount = _IbmOsaExpTRFullDuplexErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 33),
    _IbmOsaExpTRFullDuplexErrorCount_Type()
)
ibmOsaExpTRFullDuplexErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRFullDuplexErrorCount.setStatus("current")
_IbmOsaExpTRSoftErrorCount_Type = Counter32
_IbmOsaExpTRSoftErrorCount_Object = MibTableColumn
ibmOsaExpTRSoftErrorCount = _IbmOsaExpTRSoftErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 34),
    _IbmOsaExpTRSoftErrorCount_Type()
)
ibmOsaExpTRSoftErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRSoftErrorCount.setStatus("current")
_IbmOsaExpTRHardErrorCount_Type = Counter32
_IbmOsaExpTRHardErrorCount_Object = MibTableColumn
ibmOsaExpTRHardErrorCount = _IbmOsaExpTRHardErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 35),
    _IbmOsaExpTRHardErrorCount_Type()
)
ibmOsaExpTRHardErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRHardErrorCount.setStatus("current")
_IbmOsaExpTRSignalLossErrorCount_Type = Counter32
_IbmOsaExpTRSignalLossErrorCount_Object = MibTableColumn
ibmOsaExpTRSignalLossErrorCount = _IbmOsaExpTRSignalLossErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 36),
    _IbmOsaExpTRSignalLossErrorCount_Type()
)
ibmOsaExpTRSignalLossErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRSignalLossErrorCount.setStatus("current")
_IbmOsaExpTRTransmitBeaconCount_Type = Counter32
_IbmOsaExpTRTransmitBeaconCount_Object = MibTableColumn
ibmOsaExpTRTransmitBeaconCount = _IbmOsaExpTRTransmitBeaconCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 37),
    _IbmOsaExpTRTransmitBeaconCount_Type()
)
ibmOsaExpTRTransmitBeaconCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRTransmitBeaconCount.setStatus("current")
_IbmOsaExpTRRecoveryCounter_Type = Counter32
_IbmOsaExpTRRecoveryCounter_Object = MibTableColumn
ibmOsaExpTRRecoveryCounter = _IbmOsaExpTRRecoveryCounter_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 38),
    _IbmOsaExpTRRecoveryCounter_Type()
)
ibmOsaExpTRRecoveryCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRRecoveryCounter.setStatus("current")
_IbmOsaExpTRLobeWireFaultCount_Type = Counter32
_IbmOsaExpTRLobeWireFaultCount_Object = MibTableColumn
ibmOsaExpTRLobeWireFaultCount = _IbmOsaExpTRLobeWireFaultCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 39),
    _IbmOsaExpTRLobeWireFaultCount_Type()
)
ibmOsaExpTRLobeWireFaultCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRLobeWireFaultCount.setStatus("current")
_IbmOsaExpTRRemoveReceivedCount_Type = Counter32
_IbmOsaExpTRRemoveReceivedCount_Object = MibTableColumn
ibmOsaExpTRRemoveReceivedCount = _IbmOsaExpTRRemoveReceivedCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 40),
    _IbmOsaExpTRRemoveReceivedCount_Type()
)
ibmOsaExpTRRemoveReceivedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRRemoveReceivedCount.setStatus("current")
_IbmOsaExpTRSingleStationCount_Type = Counter32
_IbmOsaExpTRSingleStationCount_Object = MibTableColumn
ibmOsaExpTRSingleStationCount = _IbmOsaExpTRSingleStationCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 5, 1, 41),
    _IbmOsaExpTRSingleStationCount_Type()
)
ibmOsaExpTRSingleStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpTRSingleStationCount.setStatus("current")
_IbmOSAExpATMPortTable_Object = MibTable
ibmOSAExpATMPortTable = _IbmOSAExpATMPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7)
)
if mibBuilder.loadTexts:
    ibmOSAExpATMPortTable.setStatus("current")
_IbmOSAExpATMPortEntry_Object = MibTableRow
ibmOSAExpATMPortEntry = _IbmOSAExpATMPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1)
)
ibmOSAExpATMPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ibmOSAExpATMPortEntry.setStatus("current")


class _IbmOsaExpATMPortNumber_Type(Integer32):
    """Custom type ibmOsaExpATMPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_IbmOsaExpATMPortNumber_Type.__name__ = "Integer32"
_IbmOsaExpATMPortNumber_Object = MibTableColumn
ibmOsaExpATMPortNumber = _IbmOsaExpATMPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 1),
    _IbmOsaExpATMPortNumber_Type()
)
ibmOsaExpATMPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMPortNumber.setStatus("current")


class _IbmOsaExpATMPortType_Type(Integer32):
    """Custom type ibmOsaExpATMPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            17
        )
    )
    namedValues = NamedValues(
        ("emulatedEthernet", 17)
    )


_IbmOsaExpATMPortType_Type.__name__ = "Integer32"
_IbmOsaExpATMPortType_Object = MibTableColumn
ibmOsaExpATMPortType = _IbmOsaExpATMPortType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 2),
    _IbmOsaExpATMPortType_Type()
)
ibmOsaExpATMPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMPortType.setStatus("current")


class _IbmOsaExpATMLanTrafficState_Type(Integer32):
    """Custom type ibmOsaExpATMLanTrafficState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("configuredOffline", 8),
          ("definitionError", 7),
          ("disabled", 5),
          ("disabling", 3),
          ("enabled", 4),
          ("enabling", 2),
          ("linkMonitor", 6),
          ("unavailable", 1),
          ("undefined", 0))
    )


_IbmOsaExpATMLanTrafficState_Type.__name__ = "Integer32"
_IbmOsaExpATMLanTrafficState_Object = MibTableColumn
ibmOsaExpATMLanTrafficState = _IbmOsaExpATMLanTrafficState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 3),
    _IbmOsaExpATMLanTrafficState_Type()
)
ibmOsaExpATMLanTrafficState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMLanTrafficState.setStatus("current")


class _IbmOsaExpATMServiceMode_Type(Integer32):
    """Custom type ibmOsaExpATMServiceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inServiceMode", 1),
          ("notInServiceMode", 0))
    )


_IbmOsaExpATMServiceMode_Type.__name__ = "Integer32"
_IbmOsaExpATMServiceMode_Object = MibTableColumn
ibmOsaExpATMServiceMode = _IbmOsaExpATMServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 4),
    _IbmOsaExpATMServiceMode_Type()
)
ibmOsaExpATMServiceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMServiceMode.setStatus("current")


class _IbmOsaExpATMDisabledStatus_Type(Bits):
    """Custom type ibmOsaExpATMDisabledStatus based on Bits"""
    namedValues = NamedValues(
        *(("configurationChange", 12),
          ("internalPortFailure", 1),
          ("linkFailureThresholdExceeded", 13),
          ("networkRequest", 10),
          ("osasfRequest", 11),
          ("portTemporarilyDisabled", 6),
          ("reserved0", 0),
          ("reserved14", 14),
          ("reserved15", 15),
          ("reserved2", 2),
          ("reserved3", 3),
          ("reserved4", 4),
          ("reserved5", 5),
          ("reserved7", 7),
          ("reserved8", 8),
          ("serviceProcessorRequest", 9))
    )

_IbmOsaExpATMDisabledStatus_Type.__name__ = "Bits"
_IbmOsaExpATMDisabledStatus_Object = MibTableColumn
ibmOsaExpATMDisabledStatus = _IbmOsaExpATMDisabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 5),
    _IbmOsaExpATMDisabledStatus_Type()
)
ibmOsaExpATMDisabledStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMDisabledStatus.setStatus("current")


class _IbmOsaExpATMConfigName_Type(DisplayString):
    """Custom type ibmOsaExpATMConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 34),
    )


_IbmOsaExpATMConfigName_Type.__name__ = "DisplayString"
_IbmOsaExpATMConfigName_Object = MibTableColumn
ibmOsaExpATMConfigName = _IbmOsaExpATMConfigName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 6),
    _IbmOsaExpATMConfigName_Type()
)
ibmOsaExpATMConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMConfigName.setStatus("current")


class _IbmOsaExpATMMacAddrActive_Type(OctetString):
    """Custom type ibmOsaExpATMMacAddrActive based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmOsaExpATMMacAddrActive_Type.__name__ = "OctetString"
_IbmOsaExpATMMacAddrActive_Object = MibTableColumn
ibmOsaExpATMMacAddrActive = _IbmOsaExpATMMacAddrActive_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 7),
    _IbmOsaExpATMMacAddrActive_Type()
)
ibmOsaExpATMMacAddrActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMMacAddrActive.setStatus("current")


class _IbmOsaExpATMMacAddrBurntIn_Type(OctetString):
    """Custom type ibmOsaExpATMMacAddrBurntIn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmOsaExpATMMacAddrBurntIn_Type.__name__ = "OctetString"
_IbmOsaExpATMMacAddrBurntIn_Object = MibTableColumn
ibmOsaExpATMMacAddrBurntIn = _IbmOsaExpATMMacAddrBurntIn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 8),
    _IbmOsaExpATMMacAddrBurntIn_Type()
)
ibmOsaExpATMMacAddrBurntIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMMacAddrBurntIn.setStatus("current")


class _IbmOsaExpATMUserData_Type(DisplayString):
    """Custom type ibmOsaExpATMUserData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IbmOsaExpATMUserData_Type.__name__ = "DisplayString"
_IbmOsaExpATMUserData_Object = MibTableColumn
ibmOsaExpATMUserData = _IbmOsaExpATMUserData_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 9),
    _IbmOsaExpATMUserData_Type()
)
ibmOsaExpATMUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMUserData.setStatus("current")


class _IbmOsaExpATMPortName_Type(DisplayString):
    """Custom type ibmOsaExpATMPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IbmOsaExpATMPortName_Type.__name__ = "DisplayString"
_IbmOsaExpATMPortName_Object = MibTableColumn
ibmOsaExpATMPortName = _IbmOsaExpATMPortName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 12),
    _IbmOsaExpATMPortName_Type()
)
ibmOsaExpATMPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMPortName.setStatus("current")


class _IbmOsaExpATMGroupMacAddrTable_Type(OctetString):
    """Custom type ibmOsaExpATMGroupMacAddrTable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_IbmOsaExpATMGroupMacAddrTable_Type.__name__ = "OctetString"
_IbmOsaExpATMGroupMacAddrTable_Object = MibTableColumn
ibmOsaExpATMGroupMacAddrTable = _IbmOsaExpATMGroupMacAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 13),
    _IbmOsaExpATMGroupMacAddrTable_Type()
)
ibmOsaExpATMGroupMacAddrTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMGroupMacAddrTable.setStatus("current")


class _IbmOsaExpATMIBMEnhancedMode_Type(Integer32):
    """Custom type ibmOsaExpATMIBMEnhancedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_IbmOsaExpATMIBMEnhancedMode_Type.__name__ = "Integer32"
_IbmOsaExpATMIBMEnhancedMode_Object = MibTableColumn
ibmOsaExpATMIBMEnhancedMode = _IbmOsaExpATMIBMEnhancedMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 14),
    _IbmOsaExpATMIBMEnhancedMode_Type()
)
ibmOsaExpATMIBMEnhancedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMIBMEnhancedMode.setStatus("current")
_IbmOsaExpATMBestEffortPeakRate_Type = Integer32
_IbmOsaExpATMBestEffortPeakRate_Object = MibTableColumn
ibmOsaExpATMBestEffortPeakRate = _IbmOsaExpATMBestEffortPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 15),
    _IbmOsaExpATMBestEffortPeakRate_Type()
)
ibmOsaExpATMBestEffortPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMBestEffortPeakRate.setStatus("current")
if mibBuilder.loadTexts:
    ibmOsaExpATMBestEffortPeakRate.setUnits("Megabytes per second")


class _IbmOsaExpATMConfigMode_Type(Integer32):
    """Custom type ibmOsaExpATMConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_IbmOsaExpATMConfigMode_Type.__name__ = "Integer32"
_IbmOsaExpATMConfigMode_Object = MibTableColumn
ibmOsaExpATMConfigMode = _IbmOsaExpATMConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 16),
    _IbmOsaExpATMConfigMode_Type()
)
ibmOsaExpATMConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMConfigMode.setStatus("current")


class _IbmOsaExpATMConfigLanType_Type(Integer32):
    """Custom type ibmOsaExpATMConfigLanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            17
        )
    )
    namedValues = NamedValues(
        ("emulatedEthernet", 17)
    )


_IbmOsaExpATMConfigLanType_Type.__name__ = "Integer32"
_IbmOsaExpATMConfigLanType_Object = MibTableColumn
ibmOsaExpATMConfigLanType = _IbmOsaExpATMConfigLanType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 17),
    _IbmOsaExpATMConfigLanType_Type()
)
ibmOsaExpATMConfigLanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMConfigLanType.setStatus("current")


class _IbmOsaExpATMActualLanType_Type(Integer32):
    """Custom type ibmOsaExpATMActualLanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            17
        )
    )
    namedValues = NamedValues(
        ("emulatedEthernet", 17)
    )


_IbmOsaExpATMActualLanType_Type.__name__ = "Integer32"
_IbmOsaExpATMActualLanType_Object = MibTableColumn
ibmOsaExpATMActualLanType = _IbmOsaExpATMActualLanType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 18),
    _IbmOsaExpATMActualLanType_Type()
)
ibmOsaExpATMActualLanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMActualLanType.setStatus("current")


class _IbmOsaExpATMConfigMaxDataFrmSz_Type(Integer32):
    """Custom type ibmOsaExpATMConfigMaxDataFrmSz based on Integer32"""
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
        *(("f1516", 2),
          ("f18190", 5),
          ("f4544", 3),
          ("f9234", 4),
          ("unspecified", 1))
    )


_IbmOsaExpATMConfigMaxDataFrmSz_Type.__name__ = "Integer32"
_IbmOsaExpATMConfigMaxDataFrmSz_Object = MibTableColumn
ibmOsaExpATMConfigMaxDataFrmSz = _IbmOsaExpATMConfigMaxDataFrmSz_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 19),
    _IbmOsaExpATMConfigMaxDataFrmSz_Type()
)
ibmOsaExpATMConfigMaxDataFrmSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMConfigMaxDataFrmSz.setStatus("current")
if mibBuilder.loadTexts:
    ibmOsaExpATMConfigMaxDataFrmSz.setUnits("bytes")


class _IbmOsaExpATMActualMaxDataFrmSz_Type(Integer32):
    """Custom type ibmOsaExpATMActualMaxDataFrmSz based on Integer32"""
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
        *(("f1516", 2),
          ("f18190", 5),
          ("f4544", 3),
          ("f9234", 4),
          ("unspecified", 1))
    )


_IbmOsaExpATMActualMaxDataFrmSz_Type.__name__ = "Integer32"
_IbmOsaExpATMActualMaxDataFrmSz_Object = MibTableColumn
ibmOsaExpATMActualMaxDataFrmSz = _IbmOsaExpATMActualMaxDataFrmSz_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 20),
    _IbmOsaExpATMActualMaxDataFrmSz_Type()
)
ibmOsaExpATMActualMaxDataFrmSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMActualMaxDataFrmSz.setStatus("current")


class _IbmOsaExpATMConfigELANName_Type(DisplayString):
    """Custom type ibmOsaExpATMConfigELANName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_IbmOsaExpATMConfigELANName_Type.__name__ = "DisplayString"
_IbmOsaExpATMConfigELANName_Object = MibTableColumn
ibmOsaExpATMConfigELANName = _IbmOsaExpATMConfigELANName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 21),
    _IbmOsaExpATMConfigELANName_Type()
)
ibmOsaExpATMConfigELANName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMConfigELANName.setStatus("current")


class _IbmOsaExpATMActualELANName_Type(DisplayString):
    """Custom type ibmOsaExpATMActualELANName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_IbmOsaExpATMActualELANName_Type.__name__ = "DisplayString"
_IbmOsaExpATMActualELANName_Object = MibTableColumn
ibmOsaExpATMActualELANName = _IbmOsaExpATMActualELANName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 22),
    _IbmOsaExpATMActualELANName_Type()
)
ibmOsaExpATMActualELANName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMActualELANName.setStatus("current")


class _IbmOsaExpATMConfigLESATMAddress_Type(OctetString):
    """Custom type ibmOsaExpATMConfigLESATMAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_IbmOsaExpATMConfigLESATMAddress_Type.__name__ = "OctetString"
_IbmOsaExpATMConfigLESATMAddress_Object = MibTableColumn
ibmOsaExpATMConfigLESATMAddress = _IbmOsaExpATMConfigLESATMAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 23),
    _IbmOsaExpATMConfigLESATMAddress_Type()
)
ibmOsaExpATMConfigLESATMAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMConfigLESATMAddress.setStatus("current")


class _IbmOsaExpATMActualLESATMAddress_Type(OctetString):
    """Custom type ibmOsaExpATMActualLESATMAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_IbmOsaExpATMActualLESATMAddress_Type.__name__ = "OctetString"
_IbmOsaExpATMActualLESATMAddress_Object = MibTableColumn
ibmOsaExpATMActualLESATMAddress = _IbmOsaExpATMActualLESATMAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 24),
    _IbmOsaExpATMActualLESATMAddress_Type()
)
ibmOsaExpATMActualLESATMAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMActualLESATMAddress.setStatus("current")


class _IbmOsaExpATMControlTimeout_Type(Integer32):
    """Custom type ibmOsaExpATMControlTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_IbmOsaExpATMControlTimeout_Type.__name__ = "Integer32"
_IbmOsaExpATMControlTimeout_Object = MibTableColumn
ibmOsaExpATMControlTimeout = _IbmOsaExpATMControlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 25),
    _IbmOsaExpATMControlTimeout_Type()
)
ibmOsaExpATMControlTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMControlTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ibmOsaExpATMControlTimeout.setUnits("seconds")


class _IbmOsaExpATMMaxUnknownFrameCount_Type(Integer32):
    """Custom type ibmOsaExpATMMaxUnknownFrameCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_IbmOsaExpATMMaxUnknownFrameCount_Type.__name__ = "Integer32"
_IbmOsaExpATMMaxUnknownFrameCount_Object = MibTableColumn
ibmOsaExpATMMaxUnknownFrameCount = _IbmOsaExpATMMaxUnknownFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 26),
    _IbmOsaExpATMMaxUnknownFrameCount_Type()
)
ibmOsaExpATMMaxUnknownFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMMaxUnknownFrameCount.setStatus("current")


class _IbmOsaExpATMMaxUnknownFrameTime_Type(Integer32):
    """Custom type ibmOsaExpATMMaxUnknownFrameTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_IbmOsaExpATMMaxUnknownFrameTime_Type.__name__ = "Integer32"
_IbmOsaExpATMMaxUnknownFrameTime_Object = MibTableColumn
ibmOsaExpATMMaxUnknownFrameTime = _IbmOsaExpATMMaxUnknownFrameTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 27),
    _IbmOsaExpATMMaxUnknownFrameTime_Type()
)
ibmOsaExpATMMaxUnknownFrameTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMMaxUnknownFrameTime.setStatus("current")
_IbmOsaExpATMVCCTimeoutPeriod_Type = Integer32
_IbmOsaExpATMVCCTimeoutPeriod_Object = MibTableColumn
ibmOsaExpATMVCCTimeoutPeriod = _IbmOsaExpATMVCCTimeoutPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 28),
    _IbmOsaExpATMVCCTimeoutPeriod_Type()
)
ibmOsaExpATMVCCTimeoutPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMVCCTimeoutPeriod.setStatus("current")
if mibBuilder.loadTexts:
    ibmOsaExpATMVCCTimeoutPeriod.setUnits("seconds")
_IbmOsaExpATMMaxRetryCount_Type = Counter32
_IbmOsaExpATMMaxRetryCount_Object = MibTableColumn
ibmOsaExpATMMaxRetryCount = _IbmOsaExpATMMaxRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 29),
    _IbmOsaExpATMMaxRetryCount_Type()
)
ibmOsaExpATMMaxRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMMaxRetryCount.setStatus("current")


class _IbmOsaExpATMAgingTime_Type(Integer32):
    """Custom type ibmOsaExpATMAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_IbmOsaExpATMAgingTime_Type.__name__ = "Integer32"
_IbmOsaExpATMAgingTime_Object = MibTableColumn
ibmOsaExpATMAgingTime = _IbmOsaExpATMAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 30),
    _IbmOsaExpATMAgingTime_Type()
)
ibmOsaExpATMAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    ibmOsaExpATMAgingTime.setUnits("seconds")


class _IbmOsaExpATMForwardDelayTime_Type(Integer32):
    """Custom type ibmOsaExpATMForwardDelayTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_IbmOsaExpATMForwardDelayTime_Type.__name__ = "Integer32"
_IbmOsaExpATMForwardDelayTime_Object = MibTableColumn
ibmOsaExpATMForwardDelayTime = _IbmOsaExpATMForwardDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 31),
    _IbmOsaExpATMForwardDelayTime_Type()
)
ibmOsaExpATMForwardDelayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMForwardDelayTime.setStatus("current")
if mibBuilder.loadTexts:
    ibmOsaExpATMForwardDelayTime.setUnits("seconds")


class _IbmOsaExpATMExpectedARPRespTime_Type(Integer32):
    """Custom type ibmOsaExpATMExpectedARPRespTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_IbmOsaExpATMExpectedARPRespTime_Type.__name__ = "Integer32"
_IbmOsaExpATMExpectedARPRespTime_Object = MibTableColumn
ibmOsaExpATMExpectedARPRespTime = _IbmOsaExpATMExpectedARPRespTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 32),
    _IbmOsaExpATMExpectedARPRespTime_Type()
)
ibmOsaExpATMExpectedARPRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMExpectedARPRespTime.setStatus("current")
if mibBuilder.loadTexts:
    ibmOsaExpATMExpectedARPRespTime.setUnits("seconds")


class _IbmOsaExpATMFlushTimeout_Type(Integer32):
    """Custom type ibmOsaExpATMFlushTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_IbmOsaExpATMFlushTimeout_Type.__name__ = "Integer32"
_IbmOsaExpATMFlushTimeout_Object = MibTableColumn
ibmOsaExpATMFlushTimeout = _IbmOsaExpATMFlushTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 33),
    _IbmOsaExpATMFlushTimeout_Type()
)
ibmOsaExpATMFlushTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMFlushTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ibmOsaExpATMFlushTimeout.setUnits("seconds")


class _IbmOsaExpATMPathSwitchingDelay_Type(Integer32):
    """Custom type ibmOsaExpATMPathSwitchingDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_IbmOsaExpATMPathSwitchingDelay_Type.__name__ = "Integer32"
_IbmOsaExpATMPathSwitchingDelay_Object = MibTableColumn
ibmOsaExpATMPathSwitchingDelay = _IbmOsaExpATMPathSwitchingDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 34),
    _IbmOsaExpATMPathSwitchingDelay_Type()
)
ibmOsaExpATMPathSwitchingDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMPathSwitchingDelay.setStatus("current")
if mibBuilder.loadTexts:
    ibmOsaExpATMPathSwitchingDelay.setUnits("seconds")


class _IbmOsaExpATMLocalSegmentID_Type(Integer32):
    """Custom type ibmOsaExpATMLocalSegmentID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_IbmOsaExpATMLocalSegmentID_Type.__name__ = "Integer32"
_IbmOsaExpATMLocalSegmentID_Object = MibTableColumn
ibmOsaExpATMLocalSegmentID = _IbmOsaExpATMLocalSegmentID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 35),
    _IbmOsaExpATMLocalSegmentID_Type()
)
ibmOsaExpATMLocalSegmentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMLocalSegmentID.setStatus("current")


class _IbmOsaExpATMMltcstSendVCCType_Type(Integer32):
    """Custom type ibmOsaExpATMMltcstSendVCCType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bestEffort", 1),
          ("constantBitRate", 3),
          ("variableBitRate", 2))
    )


_IbmOsaExpATMMltcstSendVCCType_Type.__name__ = "Integer32"
_IbmOsaExpATMMltcstSendVCCType_Object = MibTableColumn
ibmOsaExpATMMltcstSendVCCType = _IbmOsaExpATMMltcstSendVCCType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 36),
    _IbmOsaExpATMMltcstSendVCCType_Type()
)
ibmOsaExpATMMltcstSendVCCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMMltcstSendVCCType.setStatus("current")
_IbmOsaExpATMMltcstSendVCCAvgRate_Type = Integer32
_IbmOsaExpATMMltcstSendVCCAvgRate_Object = MibTableColumn
ibmOsaExpATMMltcstSendVCCAvgRate = _IbmOsaExpATMMltcstSendVCCAvgRate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 37),
    _IbmOsaExpATMMltcstSendVCCAvgRate_Type()
)
ibmOsaExpATMMltcstSendVCCAvgRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMMltcstSendVCCAvgRate.setStatus("current")
_IbmOsaExpATMMcastSendVCCPeakRate_Type = Integer32
_IbmOsaExpATMMcastSendVCCPeakRate_Object = MibTableColumn
ibmOsaExpATMMcastSendVCCPeakRate = _IbmOsaExpATMMcastSendVCCPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 38),
    _IbmOsaExpATMMcastSendVCCPeakRate_Type()
)
ibmOsaExpATMMcastSendVCCPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMMcastSendVCCPeakRate.setStatus("current")


class _IbmOsaExpATMConnectCompleteTimer_Type(Integer32):
    """Custom type ibmOsaExpATMConnectCompleteTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_IbmOsaExpATMConnectCompleteTimer_Type.__name__ = "Integer32"
_IbmOsaExpATMConnectCompleteTimer_Object = MibTableColumn
ibmOsaExpATMConnectCompleteTimer = _IbmOsaExpATMConnectCompleteTimer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 39),
    _IbmOsaExpATMConnectCompleteTimer_Type()
)
ibmOsaExpATMConnectCompleteTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMConnectCompleteTimer.setStatus("current")
if mibBuilder.loadTexts:
    ibmOsaExpATMConnectCompleteTimer.setUnits("seconds")


class _IbmOsaExpATMClientATMAddress_Type(OctetString):
    """Custom type ibmOsaExpATMClientATMAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_IbmOsaExpATMClientATMAddress_Type.__name__ = "OctetString"
_IbmOsaExpATMClientATMAddress_Object = MibTableColumn
ibmOsaExpATMClientATMAddress = _IbmOsaExpATMClientATMAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 40),
    _IbmOsaExpATMClientATMAddress_Type()
)
ibmOsaExpATMClientATMAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMClientATMAddress.setStatus("current")


class _IbmOsaExpATMClientIdentifier_Type(Integer32):
    """Custom type ibmOsaExpATMClientIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65279),
    )


_IbmOsaExpATMClientIdentifier_Type.__name__ = "Integer32"
_IbmOsaExpATMClientIdentifier_Object = MibTableColumn
ibmOsaExpATMClientIdentifier = _IbmOsaExpATMClientIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 41),
    _IbmOsaExpATMClientIdentifier_Type()
)
ibmOsaExpATMClientIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMClientIdentifier.setStatus("current")


class _IbmOsaExpATMClientCurrentState_Type(Integer32):
    """Custom type ibmOsaExpATMClientCurrentState based on Integer32"""
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
        *(("busConnect", 6),
          ("configure", 3),
          ("initialRegistration", 5),
          ("initialState", 1),
          ("join", 4),
          ("lecsConnect", 2),
          ("operational", 7))
    )


_IbmOsaExpATMClientCurrentState_Type.__name__ = "Integer32"
_IbmOsaExpATMClientCurrentState_Object = MibTableColumn
ibmOsaExpATMClientCurrentState = _IbmOsaExpATMClientCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 42),
    _IbmOsaExpATMClientCurrentState_Type()
)
ibmOsaExpATMClientCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMClientCurrentState.setStatus("current")


class _IbmOsaExpATMLastFailureRespCode_Type(Integer32):
    """Custom type ibmOsaExpATMLastFailureRespCode based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("accessDenied", 9),
          ("duplicateAtmAddress", 7),
          ("duplicateLanDestination", 6),
          ("insufficientInformation", 15),
          ("insufficientResources", 8),
          ("invalidAtmAddress", 12),
          ("invalidLanDestination", 11),
          ("invalidRequestParameters", 5),
          ("invalidRequesterId", 10),
          ("leConfigureError", 14),
          ("noConfiguration", 13),
          ("none", 1),
          ("timeout", 2),
          ("undefinedError", 3),
          ("versionNotSupported", 4))
    )


_IbmOsaExpATMLastFailureRespCode_Type.__name__ = "Integer32"
_IbmOsaExpATMLastFailureRespCode_Object = MibTableColumn
ibmOsaExpATMLastFailureRespCode = _IbmOsaExpATMLastFailureRespCode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 43),
    _IbmOsaExpATMLastFailureRespCode_Type()
)
ibmOsaExpATMLastFailureRespCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMLastFailureRespCode.setStatus("current")


class _IbmOsaExpATMLastFailureState_Type(Integer32):
    """Custom type ibmOsaExpATMLastFailureState based on Integer32"""
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
        *(("busConnect", 6),
          ("configure", 3),
          ("initialRegistration", 5),
          ("initialState", 1),
          ("join", 4),
          ("lecsConnect", 2),
          ("operational", 7))
    )


_IbmOsaExpATMLastFailureState_Type.__name__ = "Integer32"
_IbmOsaExpATMLastFailureState_Object = MibTableColumn
ibmOsaExpATMLastFailureState = _IbmOsaExpATMLastFailureState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 44),
    _IbmOsaExpATMLastFailureState_Type()
)
ibmOsaExpATMLastFailureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMLastFailureState.setStatus("current")


class _IbmOsaExpATMProtocol_Type(Integer32):
    """Custom type ibmOsaExpATMProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IbmOsaExpATMProtocol_Type.__name__ = "Integer32"
_IbmOsaExpATMProtocol_Object = MibTableColumn
ibmOsaExpATMProtocol = _IbmOsaExpATMProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 45),
    _IbmOsaExpATMProtocol_Type()
)
ibmOsaExpATMProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMProtocol.setStatus("current")


class _IbmOsaExpATMLeVersion_Type(Integer32):
    """Custom type ibmOsaExpATMLeVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IbmOsaExpATMLeVersion_Type.__name__ = "Integer32"
_IbmOsaExpATMLeVersion_Object = MibTableColumn
ibmOsaExpATMLeVersion = _IbmOsaExpATMLeVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 46),
    _IbmOsaExpATMLeVersion_Type()
)
ibmOsaExpATMLeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMLeVersion.setStatus("current")


class _IbmOsaExpATMTopologyChange_Type(Integer32):
    """Custom type ibmOsaExpATMTopologyChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_IbmOsaExpATMTopologyChange_Type.__name__ = "Integer32"
_IbmOsaExpATMTopologyChange_Object = MibTableColumn
ibmOsaExpATMTopologyChange = _IbmOsaExpATMTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 47),
    _IbmOsaExpATMTopologyChange_Type()
)
ibmOsaExpATMTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMTopologyChange.setStatus("current")


class _IbmOsaExpATMConfigServerATMAddr_Type(OctetString):
    """Custom type ibmOsaExpATMConfigServerATMAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_IbmOsaExpATMConfigServerATMAddr_Type.__name__ = "OctetString"
_IbmOsaExpATMConfigServerATMAddr_Object = MibTableColumn
ibmOsaExpATMConfigServerATMAddr = _IbmOsaExpATMConfigServerATMAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 48),
    _IbmOsaExpATMConfigServerATMAddr_Type()
)
ibmOsaExpATMConfigServerATMAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMConfigServerATMAddr.setStatus("current")


class _IbmOsaExpATMConfigSource_Type(Integer32):
    """Custom type ibmOsaExpATMConfigSource based on Integer32"""
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
        *(("didNotUseLecs", 4),
          ("gotAddressViaIlmi", 1),
          ("usedLecsPvc", 3),
          ("usedWellKnownAddress", 2))
    )


_IbmOsaExpATMConfigSource_Type.__name__ = "Integer32"
_IbmOsaExpATMConfigSource_Object = MibTableColumn
ibmOsaExpATMConfigSource = _IbmOsaExpATMConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 49),
    _IbmOsaExpATMConfigSource_Type()
)
ibmOsaExpATMConfigSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMConfigSource.setStatus("current")


class _IbmOsaExpATMProxyClient_Type(Integer32):
    """Custom type ibmOsaExpATMProxyClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_IbmOsaExpATMProxyClient_Type.__name__ = "Integer32"
_IbmOsaExpATMProxyClient_Object = MibTableColumn
ibmOsaExpATMProxyClient = _IbmOsaExpATMProxyClient_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 50),
    _IbmOsaExpATMProxyClient_Type()
)
ibmOsaExpATMProxyClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMProxyClient.setStatus("current")
_IbmOsaExpATMLePDUOctetsInbound_Type = Counter64
_IbmOsaExpATMLePDUOctetsInbound_Object = MibTableColumn
ibmOsaExpATMLePDUOctetsInbound = _IbmOsaExpATMLePDUOctetsInbound_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 51),
    _IbmOsaExpATMLePDUOctetsInbound_Type()
)
ibmOsaExpATMLePDUOctetsInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMLePDUOctetsInbound.setStatus("current")
if mibBuilder.loadTexts:
    ibmOsaExpATMLePDUOctetsInbound.setUnits("octets")
_IbmOsaExpATMNonErrLePDUDiscIn_Type = Counter32
_IbmOsaExpATMNonErrLePDUDiscIn_Object = MibTableColumn
ibmOsaExpATMNonErrLePDUDiscIn = _IbmOsaExpATMNonErrLePDUDiscIn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 52),
    _IbmOsaExpATMNonErrLePDUDiscIn_Type()
)
ibmOsaExpATMNonErrLePDUDiscIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMNonErrLePDUDiscIn.setStatus("current")
if mibBuilder.loadTexts:
    ibmOsaExpATMNonErrLePDUDiscIn.setUnits("octets")
_IbmOsaExpATMErrLePDUDiscIn_Type = Counter32
_IbmOsaExpATMErrLePDUDiscIn_Object = MibTableColumn
ibmOsaExpATMErrLePDUDiscIn = _IbmOsaExpATMErrLePDUDiscIn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 53),
    _IbmOsaExpATMErrLePDUDiscIn_Type()
)
ibmOsaExpATMErrLePDUDiscIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMErrLePDUDiscIn.setStatus("current")
_IbmOsaExpATMLePDUOctetsOutbound_Type = Counter64
_IbmOsaExpATMLePDUOctetsOutbound_Object = MibTableColumn
ibmOsaExpATMLePDUOctetsOutbound = _IbmOsaExpATMLePDUOctetsOutbound_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 54),
    _IbmOsaExpATMLePDUOctetsOutbound_Type()
)
ibmOsaExpATMLePDUOctetsOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMLePDUOctetsOutbound.setStatus("current")
if mibBuilder.loadTexts:
    ibmOsaExpATMLePDUOctetsOutbound.setUnits("octets")
_IbmOsaExpATMNonErrLePDUDiscOut_Type = Counter32
_IbmOsaExpATMNonErrLePDUDiscOut_Object = MibTableColumn
ibmOsaExpATMNonErrLePDUDiscOut = _IbmOsaExpATMNonErrLePDUDiscOut_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 55),
    _IbmOsaExpATMNonErrLePDUDiscOut_Type()
)
ibmOsaExpATMNonErrLePDUDiscOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMNonErrLePDUDiscOut.setStatus("current")
_IbmOsaExpATMErrLePDUDiscOut_Type = Counter32
_IbmOsaExpATMErrLePDUDiscOut_Object = MibTableColumn
ibmOsaExpATMErrLePDUDiscOut = _IbmOsaExpATMErrLePDUDiscOut_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 56),
    _IbmOsaExpATMErrLePDUDiscOut_Type()
)
ibmOsaExpATMErrLePDUDiscOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMErrLePDUDiscOut.setStatus("current")
_IbmOsaExpATMLeARPRequestsOut_Type = Counter32
_IbmOsaExpATMLeARPRequestsOut_Object = MibTableColumn
ibmOsaExpATMLeARPRequestsOut = _IbmOsaExpATMLeARPRequestsOut_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 57),
    _IbmOsaExpATMLeARPRequestsOut_Type()
)
ibmOsaExpATMLeARPRequestsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMLeARPRequestsOut.setStatus("current")
_IbmOsaExpATMLeARPRequestsIn_Type = Counter32
_IbmOsaExpATMLeARPRequestsIn_Object = MibTableColumn
ibmOsaExpATMLeARPRequestsIn = _IbmOsaExpATMLeARPRequestsIn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 58),
    _IbmOsaExpATMLeARPRequestsIn_Type()
)
ibmOsaExpATMLeARPRequestsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMLeARPRequestsIn.setStatus("current")
_IbmOsaExpATMLeARPRepliesOut_Type = Counter32
_IbmOsaExpATMLeARPRepliesOut_Object = MibTableColumn
ibmOsaExpATMLeARPRepliesOut = _IbmOsaExpATMLeARPRepliesOut_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 59),
    _IbmOsaExpATMLeARPRepliesOut_Type()
)
ibmOsaExpATMLeARPRepliesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMLeARPRepliesOut.setStatus("current")
_IbmOsaExpATMLeARPRepliesIn_Type = Counter32
_IbmOsaExpATMLeARPRepliesIn_Object = MibTableColumn
ibmOsaExpATMLeARPRepliesIn = _IbmOsaExpATMLeARPRepliesIn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 60),
    _IbmOsaExpATMLeARPRepliesIn_Type()
)
ibmOsaExpATMLeARPRepliesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMLeARPRepliesIn.setStatus("current")
_IbmOsaExpATMControlFramesOut_Type = Counter32
_IbmOsaExpATMControlFramesOut_Object = MibTableColumn
ibmOsaExpATMControlFramesOut = _IbmOsaExpATMControlFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 61),
    _IbmOsaExpATMControlFramesOut_Type()
)
ibmOsaExpATMControlFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMControlFramesOut.setStatus("current")
if mibBuilder.loadTexts:
    ibmOsaExpATMControlFramesOut.setUnits("packets")
_IbmOsaExpATMControlFramesIn_Type = Counter32
_IbmOsaExpATMControlFramesIn_Object = MibTableColumn
ibmOsaExpATMControlFramesIn = _IbmOsaExpATMControlFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 62),
    _IbmOsaExpATMControlFramesIn_Type()
)
ibmOsaExpATMControlFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMControlFramesIn.setStatus("current")
if mibBuilder.loadTexts:
    ibmOsaExpATMControlFramesIn.setUnits("packets")
_IbmOsaExpATMSVCFailures_Type = Counter32
_IbmOsaExpATMSVCFailures_Object = MibTableColumn
ibmOsaExpATMSVCFailures = _IbmOsaExpATMSVCFailures_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 63),
    _IbmOsaExpATMSVCFailures_Type()
)
ibmOsaExpATMSVCFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMSVCFailures.setStatus("current")


class _IbmOsaExpATMConfigDirectIntfc_Type(Integer32):
    """Custom type ibmOsaExpATMConfigDirectIntfc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IbmOsaExpATMConfigDirectIntfc_Type.__name__ = "Integer32"
_IbmOsaExpATMConfigDirectIntfc_Object = MibTableColumn
ibmOsaExpATMConfigDirectIntfc = _IbmOsaExpATMConfigDirectIntfc_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 64),
    _IbmOsaExpATMConfigDirectIntfc_Type()
)
ibmOsaExpATMConfigDirectIntfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMConfigDirectIntfc.setStatus("current")


class _IbmOsaExpATMConfigDirectVPI_Type(Integer32):
    """Custom type ibmOsaExpATMConfigDirectVPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmOsaExpATMConfigDirectVPI_Type.__name__ = "Integer32"
_IbmOsaExpATMConfigDirectVPI_Object = MibTableColumn
ibmOsaExpATMConfigDirectVPI = _IbmOsaExpATMConfigDirectVPI_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 65),
    _IbmOsaExpATMConfigDirectVPI_Type()
)
ibmOsaExpATMConfigDirectVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMConfigDirectVPI.setStatus("current")


class _IbmOsaExpATMConfigDirectVCI_Type(Integer32):
    """Custom type ibmOsaExpATMConfigDirectVCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmOsaExpATMConfigDirectVCI_Type.__name__ = "Integer32"
_IbmOsaExpATMConfigDirectVCI_Object = MibTableColumn
ibmOsaExpATMConfigDirectVCI = _IbmOsaExpATMConfigDirectVCI_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 66),
    _IbmOsaExpATMConfigDirectVCI_Type()
)
ibmOsaExpATMConfigDirectVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMConfigDirectVCI.setStatus("current")


class _IbmOsaExpATMControlDirectIntfc_Type(Integer32):
    """Custom type ibmOsaExpATMControlDirectIntfc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IbmOsaExpATMControlDirectIntfc_Type.__name__ = "Integer32"
_IbmOsaExpATMControlDirectIntfc_Object = MibTableColumn
ibmOsaExpATMControlDirectIntfc = _IbmOsaExpATMControlDirectIntfc_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 67),
    _IbmOsaExpATMControlDirectIntfc_Type()
)
ibmOsaExpATMControlDirectIntfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMControlDirectIntfc.setStatus("current")


class _IbmOsaExpATMControlDirectVPI_Type(Integer32):
    """Custom type ibmOsaExpATMControlDirectVPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmOsaExpATMControlDirectVPI_Type.__name__ = "Integer32"
_IbmOsaExpATMControlDirectVPI_Object = MibTableColumn
ibmOsaExpATMControlDirectVPI = _IbmOsaExpATMControlDirectVPI_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 68),
    _IbmOsaExpATMControlDirectVPI_Type()
)
ibmOsaExpATMControlDirectVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMControlDirectVPI.setStatus("current")


class _IbmOsaExpATMControlDirectVCI_Type(Integer32):
    """Custom type ibmOsaExpATMControlDirectVCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmOsaExpATMControlDirectVCI_Type.__name__ = "Integer32"
_IbmOsaExpATMControlDirectVCI_Object = MibTableColumn
ibmOsaExpATMControlDirectVCI = _IbmOsaExpATMControlDirectVCI_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 69),
    _IbmOsaExpATMControlDirectVCI_Type()
)
ibmOsaExpATMControlDirectVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMControlDirectVCI.setStatus("current")


class _IbmOsaExpATMControlDistIntfc_Type(Integer32):
    """Custom type ibmOsaExpATMControlDistIntfc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IbmOsaExpATMControlDistIntfc_Type.__name__ = "Integer32"
_IbmOsaExpATMControlDistIntfc_Object = MibTableColumn
ibmOsaExpATMControlDistIntfc = _IbmOsaExpATMControlDistIntfc_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 70),
    _IbmOsaExpATMControlDistIntfc_Type()
)
ibmOsaExpATMControlDistIntfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMControlDistIntfc.setStatus("current")


class _IbmOsaExpATMControlDistributeVPI_Type(Integer32):
    """Custom type ibmOsaExpATMControlDistributeVPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmOsaExpATMControlDistributeVPI_Type.__name__ = "Integer32"
_IbmOsaExpATMControlDistributeVPI_Object = MibTableColumn
ibmOsaExpATMControlDistributeVPI = _IbmOsaExpATMControlDistributeVPI_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 71),
    _IbmOsaExpATMControlDistributeVPI_Type()
)
ibmOsaExpATMControlDistributeVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMControlDistributeVPI.setStatus("current")


class _IbmOsaExpATMControlDistributeVCI_Type(Integer32):
    """Custom type ibmOsaExpATMControlDistributeVCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmOsaExpATMControlDistributeVCI_Type.__name__ = "Integer32"
_IbmOsaExpATMControlDistributeVCI_Object = MibTableColumn
ibmOsaExpATMControlDistributeVCI = _IbmOsaExpATMControlDistributeVCI_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 72),
    _IbmOsaExpATMControlDistributeVCI_Type()
)
ibmOsaExpATMControlDistributeVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMControlDistributeVCI.setStatus("current")


class _IbmOsaExpATMMulticastSendIntfc_Type(Integer32):
    """Custom type ibmOsaExpATMMulticastSendIntfc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IbmOsaExpATMMulticastSendIntfc_Type.__name__ = "Integer32"
_IbmOsaExpATMMulticastSendIntfc_Object = MibTableColumn
ibmOsaExpATMMulticastSendIntfc = _IbmOsaExpATMMulticastSendIntfc_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 73),
    _IbmOsaExpATMMulticastSendIntfc_Type()
)
ibmOsaExpATMMulticastSendIntfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMMulticastSendIntfc.setStatus("current")


class _IbmOsaExpATMMulticastSendVPI_Type(Integer32):
    """Custom type ibmOsaExpATMMulticastSendVPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmOsaExpATMMulticastSendVPI_Type.__name__ = "Integer32"
_IbmOsaExpATMMulticastSendVPI_Object = MibTableColumn
ibmOsaExpATMMulticastSendVPI = _IbmOsaExpATMMulticastSendVPI_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 74),
    _IbmOsaExpATMMulticastSendVPI_Type()
)
ibmOsaExpATMMulticastSendVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMMulticastSendVPI.setStatus("current")


class _IbmOsaExpATMMulticastSendVCI_Type(Integer32):
    """Custom type ibmOsaExpATMMulticastSendVCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmOsaExpATMMulticastSendVCI_Type.__name__ = "Integer32"
_IbmOsaExpATMMulticastSendVCI_Object = MibTableColumn
ibmOsaExpATMMulticastSendVCI = _IbmOsaExpATMMulticastSendVCI_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 75),
    _IbmOsaExpATMMulticastSendVCI_Type()
)
ibmOsaExpATMMulticastSendVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMMulticastSendVCI.setStatus("current")


class _IbmOsaExpATMMulticastFwdIntfc_Type(Integer32):
    """Custom type ibmOsaExpATMMulticastFwdIntfc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IbmOsaExpATMMulticastFwdIntfc_Type.__name__ = "Integer32"
_IbmOsaExpATMMulticastFwdIntfc_Object = MibTableColumn
ibmOsaExpATMMulticastFwdIntfc = _IbmOsaExpATMMulticastFwdIntfc_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 76),
    _IbmOsaExpATMMulticastFwdIntfc_Type()
)
ibmOsaExpATMMulticastFwdIntfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMMulticastFwdIntfc.setStatus("current")


class _IbmOsaExpATMMulticastForwardVPI_Type(Integer32):
    """Custom type ibmOsaExpATMMulticastForwardVPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmOsaExpATMMulticastForwardVPI_Type.__name__ = "Integer32"
_IbmOsaExpATMMulticastForwardVPI_Object = MibTableColumn
ibmOsaExpATMMulticastForwardVPI = _IbmOsaExpATMMulticastForwardVPI_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 77),
    _IbmOsaExpATMMulticastForwardVPI_Type()
)
ibmOsaExpATMMulticastForwardVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMMulticastForwardVPI.setStatus("current")


class _IbmOsaExpATMMulticastForwardVCI_Type(Integer32):
    """Custom type ibmOsaExpATMMulticastForwardVCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmOsaExpATMMulticastForwardVCI_Type.__name__ = "Integer32"
_IbmOsaExpATMMulticastForwardVCI_Object = MibTableColumn
ibmOsaExpATMMulticastForwardVCI = _IbmOsaExpATMMulticastForwardVCI_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 1, 7, 1, 78),
    _IbmOsaExpATMMulticastForwardVCI_Type()
)
ibmOsaExpATMMulticastForwardVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmOsaExpATMMulticastForwardVCI.setStatus("current")
_IbmOSAMibConformance_ObjectIdentity = ObjectIdentity
ibmOSAMibConformance = _IbmOSAMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 2)
)
_IbmOSAMibCompliances_ObjectIdentity = ObjectIdentity
ibmOSAMibCompliances = _IbmOSAMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 2, 1)
)
_IbmOSAMibGroups_ObjectIdentity = ObjectIdentity
ibmOSAMibGroups = _IbmOSAMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 2, 2)
)

# Managed Objects groups

ibmOSAExpChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 2, 2, 1)
)
ibmOSAExpChannelGroup.setObjects(
      *(("IBM-OSA-MIB", "ibmOSAExpChannelNumber"),
        ("IBM-OSA-MIB", "ibmOSAExpChannelType"),
        ("IBM-OSA-MIB", "ibmOSAExpChannelHdwLevel"),
        ("IBM-OSA-MIB", "ibmOSAExpChannelSubType"),
        ("IBM-OSA-MIB", "ibmOSAExpChannelShared"),
        ("IBM-OSA-MIB", "ibmOSAExpChannelNodeDesc"),
        ("IBM-OSA-MIB", "ibmOSAExpChannelProcCodeLevel"),
        ("IBM-OSA-MIB", "ibmOSAExpChannelPCIBusUtil1Min"),
        ("IBM-OSA-MIB", "ibmOSAExpChannelProcUtil1Min"),
        ("IBM-OSA-MIB", "ibmOSAExpChannelPCIBusUtil5Min"),
        ("IBM-OSA-MIB", "ibmOSAExpChannelProcUtil5Min"),
        ("IBM-OSA-MIB", "ibmOSAExpChannelPCIBusUtilHour"),
        ("IBM-OSA-MIB", "ibmOSAExpChannelProcUtilHour"))
)
if mibBuilder.loadTexts:
    ibmOSAExpChannelGroup.setStatus("current")

ibmOSAExpPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 2, 2, 2)
)
ibmOSAExpPerfGroup.setObjects(
      *(("IBM-OSA-MIB", "ibmOSAExpPerfDataLP0"),
        ("IBM-OSA-MIB", "ibmOSAExpPerfDataLP1"),
        ("IBM-OSA-MIB", "ibmOSAExpPerfDataLP2"),
        ("IBM-OSA-MIB", "ibmOSAExpPerfDataLP3"),
        ("IBM-OSA-MIB", "ibmOSAExpPerfDataLP4"),
        ("IBM-OSA-MIB", "ibmOSAExpPerfDataLP5"),
        ("IBM-OSA-MIB", "ibmOSAExpPerfDataLP6"),
        ("IBM-OSA-MIB", "ibmOSAExpPerfDataLP7"),
        ("IBM-OSA-MIB", "ibmOSAExpPerfDataLP8"),
        ("IBM-OSA-MIB", "ibmOSAExpPerfDataLP9"),
        ("IBM-OSA-MIB", "ibmOSAExpPerfDataLP10"),
        ("IBM-OSA-MIB", "ibmOSAExpPerfDataLP11"),
        ("IBM-OSA-MIB", "ibmOSAExpPerfDataLP12"),
        ("IBM-OSA-MIB", "ibmOSAExpPerfDataLP13"),
        ("IBM-OSA-MIB", "ibmOSAExpPerfDataLP14"),
        ("IBM-OSA-MIB", "ibmOSAExpPerfDataLP15"))
)
if mibBuilder.loadTexts:
    ibmOSAExpPerfGroup.setStatus("current")

ibmOSAExpPEGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 2, 2, 3)
)
ibmOSAExpPEGroup.setObjects(
      *(("IBM-OSA-MIB", "ibmOSAExpPEMaxSizeArpCache"),
        ("IBM-OSA-MIB", "ibmOSAExpPEArpPendingEntries"),
        ("IBM-OSA-MIB", "ibmOSAExpPEArpActiveEntries"),
        ("IBM-OSA-MIB", "ibmOSAExpPEIPEntries"),
        ("IBM-OSA-MIB", "ibmOSAExpPEMulticastEntries"),
        ("IBM-OSA-MIB", "ibmOSAExpPEMulticastData"))
)
if mibBuilder.loadTexts:
    ibmOSAExpPEGroup.setStatus("current")

ibmOSAExpEthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 2, 2, 4)
)
ibmOSAExpEthGroup.setObjects(
      *(("IBM-OSA-MIB", "ibmOsaExpEthPortNumber"),
        ("IBM-OSA-MIB", "ibmOsaExpEthPortType"),
        ("IBM-OSA-MIB", "ibmOsaExpEthLanTrafficState"),
        ("IBM-OSA-MIB", "ibmOsaExpEthServiceMode"),
        ("IBM-OSA-MIB", "ibmOsaExpEthDisabledStatus"),
        ("IBM-OSA-MIB", "ibmOsaExpEthConfigName"),
        ("IBM-OSA-MIB", "ibmOsaExpEthConfigSpeedMode"),
        ("IBM-OSA-MIB", "ibmOsaExpEthActiveSpeedMode"),
        ("IBM-OSA-MIB", "ibmOsaExpEthMacAddrActive"),
        ("IBM-OSA-MIB", "ibmOsaExpEthMacAddrBurntIn"),
        ("IBM-OSA-MIB", "ibmOsaExpEthUserData"),
        ("IBM-OSA-MIB", "ibmOsaExpEthOutPackets"),
        ("IBM-OSA-MIB", "ibmOsaExpEthInPackets"),
        ("IBM-OSA-MIB", "ibmOsaExpEthInGroupFrames"),
        ("IBM-OSA-MIB", "ibmOsaExpEthInBroadcastFrames"),
        ("IBM-OSA-MIB", "ibmOsaExpEthPortName"),
        ("IBM-OSA-MIB", "ibmOsaExpEthInUnknownIPFrames"),
        ("IBM-OSA-MIB", "ibmOsaExpEthGroupAddrTable"))
)
if mibBuilder.loadTexts:
    ibmOSAExpEthGroup.setStatus("current")

ibmOSAExpTRGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 2, 2, 5)
)
ibmOSAExpTRGroup.setObjects(
      *(("IBM-OSA-MIB", "ibmOsaExpTRPortNumber"),
        ("IBM-OSA-MIB", "ibmOsaExpTRPortType"),
        ("IBM-OSA-MIB", "ibmOsaExpTRLanTrafficState"),
        ("IBM-OSA-MIB", "ibmOsaExpTRServiceMode"),
        ("IBM-OSA-MIB", "ibmOsaExpTRDisabledStatus"),
        ("IBM-OSA-MIB", "ibmOsaExpTRConfigName"),
        ("IBM-OSA-MIB", "ibmOsaExpTRMacAddrActive"),
        ("IBM-OSA-MIB", "ibmOsaExpTRMacAddrBurntIn"),
        ("IBM-OSA-MIB", "ibmOsaExpTRConfigSpeedMode"),
        ("IBM-OSA-MIB", "ibmOsaExpTRActiveSpeedMode"),
        ("IBM-OSA-MIB", "ibmOsaExpTRUserData"),
        ("IBM-OSA-MIB", "ibmOsaExpTRPortName"),
        ("IBM-OSA-MIB", "ibmOsaExpTRGroupAddrTable"),
        ("IBM-OSA-MIB", "ibmOsaExpTRFunctionalAddr"),
        ("IBM-OSA-MIB", "ibmOsaExpTRRingStatus"),
        ("IBM-OSA-MIB", "ibmOsaExpTRAllowAccessPriority"),
        ("IBM-OSA-MIB", "ibmOsaExpTREarlyTokenRelease"),
        ("IBM-OSA-MIB", "ibmOsaExpTRBeaconingAddress"),
        ("IBM-OSA-MIB", "ibmOsaExpTRUpstreamNeighbor"),
        ("IBM-OSA-MIB", "ibmOsaExpTRRingState"),
        ("IBM-OSA-MIB", "ibmOsaExpTRRingOpenStatus"),
        ("IBM-OSA-MIB", "ibmOsaExpTRPacketsTransmitted"),
        ("IBM-OSA-MIB", "ibmOsaExpTRPacketsReceived"),
        ("IBM-OSA-MIB", "ibmOsaExpTRLineErrorCount"),
        ("IBM-OSA-MIB", "ibmOsaExpTRBurstErrorCount"),
        ("IBM-OSA-MIB", "ibmOsaExpTRACErrorCount"),
        ("IBM-OSA-MIB", "ibmOsaExpTRAbortTransErrorCount"),
        ("IBM-OSA-MIB", "ibmOsaExpTRInternalErrorCount"),
        ("IBM-OSA-MIB", "ibmOsaExpTRLostFrameErrorCount"),
        ("IBM-OSA-MIB", "ibmOsaExpTRRcvCongestionCount"),
        ("IBM-OSA-MIB", "ibmOsaExpTRFrameCopyErrorCount"),
        ("IBM-OSA-MIB", "ibmOsaExpTRTokenErrorCount"),
        ("IBM-OSA-MIB", "ibmOsaExpTRFullDuplexErrorCount"),
        ("IBM-OSA-MIB", "ibmOsaExpTRSoftErrorCount"),
        ("IBM-OSA-MIB", "ibmOsaExpTRHardErrorCount"),
        ("IBM-OSA-MIB", "ibmOsaExpTRSignalLossErrorCount"),
        ("IBM-OSA-MIB", "ibmOsaExpTRTransmitBeaconCount"),
        ("IBM-OSA-MIB", "ibmOsaExpTRRecoveryCounter"),
        ("IBM-OSA-MIB", "ibmOsaExpTRLobeWireFaultCount"),
        ("IBM-OSA-MIB", "ibmOsaExpTRRemoveReceivedCount"),
        ("IBM-OSA-MIB", "ibmOsaExpTRSingleStationCount"))
)
if mibBuilder.loadTexts:
    ibmOSAExpTRGroup.setStatus("current")

ibmOSAExpATMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 2, 2, 7)
)
ibmOSAExpATMGroup.setObjects(
      *(("IBM-OSA-MIB", "ibmOsaExpATMPortNumber"),
        ("IBM-OSA-MIB", "ibmOsaExpATMPortType"),
        ("IBM-OSA-MIB", "ibmOsaExpATMLanTrafficState"),
        ("IBM-OSA-MIB", "ibmOsaExpATMServiceMode"),
        ("IBM-OSA-MIB", "ibmOsaExpATMDisabledStatus"),
        ("IBM-OSA-MIB", "ibmOsaExpATMConfigName"),
        ("IBM-OSA-MIB", "ibmOsaExpATMMacAddrActive"),
        ("IBM-OSA-MIB", "ibmOsaExpATMMacAddrBurntIn"),
        ("IBM-OSA-MIB", "ibmOsaExpATMUserData"),
        ("IBM-OSA-MIB", "ibmOsaExpATMPortName"),
        ("IBM-OSA-MIB", "ibmOsaExpATMGroupMacAddrTable"),
        ("IBM-OSA-MIB", "ibmOsaExpATMIBMEnhancedMode"),
        ("IBM-OSA-MIB", "ibmOsaExpATMBestEffortPeakRate"),
        ("IBM-OSA-MIB", "ibmOsaExpATMConfigMode"),
        ("IBM-OSA-MIB", "ibmOsaExpATMConfigLanType"),
        ("IBM-OSA-MIB", "ibmOsaExpATMActualLanType"),
        ("IBM-OSA-MIB", "ibmOsaExpATMConfigMaxDataFrmSz"),
        ("IBM-OSA-MIB", "ibmOsaExpATMActualMaxDataFrmSz"),
        ("IBM-OSA-MIB", "ibmOsaExpATMConfigELANName"),
        ("IBM-OSA-MIB", "ibmOsaExpATMActualELANName"),
        ("IBM-OSA-MIB", "ibmOsaExpATMConfigLESATMAddress"),
        ("IBM-OSA-MIB", "ibmOsaExpATMActualLESATMAddress"),
        ("IBM-OSA-MIB", "ibmOsaExpATMControlTimeout"),
        ("IBM-OSA-MIB", "ibmOsaExpATMMaxUnknownFrameCount"),
        ("IBM-OSA-MIB", "ibmOsaExpATMMaxUnknownFrameTime"),
        ("IBM-OSA-MIB", "ibmOsaExpATMVCCTimeoutPeriod"),
        ("IBM-OSA-MIB", "ibmOsaExpATMMaxRetryCount"),
        ("IBM-OSA-MIB", "ibmOsaExpATMAgingTime"),
        ("IBM-OSA-MIB", "ibmOsaExpATMForwardDelayTime"),
        ("IBM-OSA-MIB", "ibmOsaExpATMExpectedARPRespTime"),
        ("IBM-OSA-MIB", "ibmOsaExpATMFlushTimeout"),
        ("IBM-OSA-MIB", "ibmOsaExpATMPathSwitchingDelay"),
        ("IBM-OSA-MIB", "ibmOsaExpATMLocalSegmentID"),
        ("IBM-OSA-MIB", "ibmOsaExpATMMltcstSendVCCType"),
        ("IBM-OSA-MIB", "ibmOsaExpATMMltcstSendVCCAvgRate"),
        ("IBM-OSA-MIB", "ibmOsaExpATMMcastSendVCCPeakRate"),
        ("IBM-OSA-MIB", "ibmOsaExpATMConnectCompleteTimer"),
        ("IBM-OSA-MIB", "ibmOsaExpATMClientATMAddress"),
        ("IBM-OSA-MIB", "ibmOsaExpATMClientIdentifier"),
        ("IBM-OSA-MIB", "ibmOsaExpATMClientCurrentState"),
        ("IBM-OSA-MIB", "ibmOsaExpATMLastFailureRespCode"),
        ("IBM-OSA-MIB", "ibmOsaExpATMLastFailureState"),
        ("IBM-OSA-MIB", "ibmOsaExpATMProtocol"),
        ("IBM-OSA-MIB", "ibmOsaExpATMLeVersion"),
        ("IBM-OSA-MIB", "ibmOsaExpATMTopologyChange"),
        ("IBM-OSA-MIB", "ibmOsaExpATMConfigServerATMAddr"),
        ("IBM-OSA-MIB", "ibmOsaExpATMConfigSource"),
        ("IBM-OSA-MIB", "ibmOsaExpATMProxyClient"),
        ("IBM-OSA-MIB", "ibmOsaExpATMLePDUOctetsInbound"),
        ("IBM-OSA-MIB", "ibmOsaExpATMNonErrLePDUDiscIn"),
        ("IBM-OSA-MIB", "ibmOsaExpATMErrLePDUDiscIn"),
        ("IBM-OSA-MIB", "ibmOsaExpATMLePDUOctetsOutbound"),
        ("IBM-OSA-MIB", "ibmOsaExpATMNonErrLePDUDiscOut"),
        ("IBM-OSA-MIB", "ibmOsaExpATMErrLePDUDiscOut"),
        ("IBM-OSA-MIB", "ibmOsaExpATMLeARPRequestsOut"),
        ("IBM-OSA-MIB", "ibmOsaExpATMLeARPRequestsIn"),
        ("IBM-OSA-MIB", "ibmOsaExpATMLeARPRepliesOut"),
        ("IBM-OSA-MIB", "ibmOsaExpATMLeARPRepliesIn"),
        ("IBM-OSA-MIB", "ibmOsaExpATMControlFramesOut"),
        ("IBM-OSA-MIB", "ibmOsaExpATMControlFramesIn"),
        ("IBM-OSA-MIB", "ibmOsaExpATMSVCFailures"),
        ("IBM-OSA-MIB", "ibmOsaExpATMConfigDirectIntfc"),
        ("IBM-OSA-MIB", "ibmOsaExpATMConfigDirectVPI"),
        ("IBM-OSA-MIB", "ibmOsaExpATMConfigDirectVCI"),
        ("IBM-OSA-MIB", "ibmOsaExpATMControlDirectIntfc"),
        ("IBM-OSA-MIB", "ibmOsaExpATMControlDirectVPI"),
        ("IBM-OSA-MIB", "ibmOsaExpATMControlDirectVCI"),
        ("IBM-OSA-MIB", "ibmOsaExpATMControlDistIntfc"),
        ("IBM-OSA-MIB", "ibmOsaExpATMControlDistributeVPI"),
        ("IBM-OSA-MIB", "ibmOsaExpATMControlDistributeVCI"),
        ("IBM-OSA-MIB", "ibmOsaExpATMMulticastSendIntfc"),
        ("IBM-OSA-MIB", "ibmOsaExpATMMulticastSendVPI"),
        ("IBM-OSA-MIB", "ibmOsaExpATMMulticastSendVCI"),
        ("IBM-OSA-MIB", "ibmOsaExpATMMulticastFwdIntfc"),
        ("IBM-OSA-MIB", "ibmOsaExpATMMulticastForwardVPI"),
        ("IBM-OSA-MIB", "ibmOsaExpATMMulticastForwardVCI"))
)
if mibBuilder.loadTexts:
    ibmOSAExpATMGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ibmOSAMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2, 6, 188, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ibmOSAMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBM-OSA-MIB",
    **{"ibm": ibm,
       "ibmProd": ibmProd,
       "ibmOSAMib": ibmOSAMib,
       "ibmOSAMibObjects": ibmOSAMibObjects,
       "ibmOSAExpChannelTable": ibmOSAExpChannelTable,
       "ibmOSAExpChannelEntry": ibmOSAExpChannelEntry,
       "ibmOSAExpChannelNumber": ibmOSAExpChannelNumber,
       "ibmOSAExpChannelType": ibmOSAExpChannelType,
       "ibmOSAExpChannelHdwLevel": ibmOSAExpChannelHdwLevel,
       "ibmOSAExpChannelSubType": ibmOSAExpChannelSubType,
       "ibmOSAExpChannelShared": ibmOSAExpChannelShared,
       "ibmOSAExpChannelNodeDesc": ibmOSAExpChannelNodeDesc,
       "ibmOSAExpChannelProcCodeLevel": ibmOSAExpChannelProcCodeLevel,
       "ibmOSAExpChannelPCIBusUtil1Min": ibmOSAExpChannelPCIBusUtil1Min,
       "ibmOSAExpChannelProcUtil1Min": ibmOSAExpChannelProcUtil1Min,
       "ibmOSAExpChannelPCIBusUtil5Min": ibmOSAExpChannelPCIBusUtil5Min,
       "ibmOSAExpChannelProcUtil5Min": ibmOSAExpChannelProcUtil5Min,
       "ibmOSAExpChannelPCIBusUtilHour": ibmOSAExpChannelPCIBusUtilHour,
       "ibmOSAExpChannelProcUtilHour": ibmOSAExpChannelProcUtilHour,
       "ibmOSAExpPerfTable": ibmOSAExpPerfTable,
       "ibmOSAExpPerfEntry": ibmOSAExpPerfEntry,
       "ibmOSAExpPerfDataLP0": ibmOSAExpPerfDataLP0,
       "ibmOSAExpPerfDataLP1": ibmOSAExpPerfDataLP1,
       "ibmOSAExpPerfDataLP2": ibmOSAExpPerfDataLP2,
       "ibmOSAExpPerfDataLP3": ibmOSAExpPerfDataLP3,
       "ibmOSAExpPerfDataLP4": ibmOSAExpPerfDataLP4,
       "ibmOSAExpPerfDataLP5": ibmOSAExpPerfDataLP5,
       "ibmOSAExpPerfDataLP6": ibmOSAExpPerfDataLP6,
       "ibmOSAExpPerfDataLP7": ibmOSAExpPerfDataLP7,
       "ibmOSAExpPerfDataLP8": ibmOSAExpPerfDataLP8,
       "ibmOSAExpPerfDataLP9": ibmOSAExpPerfDataLP9,
       "ibmOSAExpPerfDataLP10": ibmOSAExpPerfDataLP10,
       "ibmOSAExpPerfDataLP11": ibmOSAExpPerfDataLP11,
       "ibmOSAExpPerfDataLP12": ibmOSAExpPerfDataLP12,
       "ibmOSAExpPerfDataLP13": ibmOSAExpPerfDataLP13,
       "ibmOSAExpPerfDataLP14": ibmOSAExpPerfDataLP14,
       "ibmOSAExpPerfDataLP15": ibmOSAExpPerfDataLP15,
       "ibmOSAExpPETable": ibmOSAExpPETable,
       "ibmOSAExpPEEntry": ibmOSAExpPEEntry,
       "ibmOSAExpPEMaxSizeArpCache": ibmOSAExpPEMaxSizeArpCache,
       "ibmOSAExpPEArpPendingEntries": ibmOSAExpPEArpPendingEntries,
       "ibmOSAExpPEArpActiveEntries": ibmOSAExpPEArpActiveEntries,
       "ibmOSAExpPEIPEntries": ibmOSAExpPEIPEntries,
       "ibmOSAExpPEMulticastEntries": ibmOSAExpPEMulticastEntries,
       "ibmOSAExpPEMulticastData": ibmOSAExpPEMulticastData,
       "ibmOSAExpEthPortTable": ibmOSAExpEthPortTable,
       "ibmOSAExpEthPortEntry": ibmOSAExpEthPortEntry,
       "ibmOsaExpEthPortNumber": ibmOsaExpEthPortNumber,
       "ibmOsaExpEthPortType": ibmOsaExpEthPortType,
       "ibmOsaExpEthLanTrafficState": ibmOsaExpEthLanTrafficState,
       "ibmOsaExpEthServiceMode": ibmOsaExpEthServiceMode,
       "ibmOsaExpEthDisabledStatus": ibmOsaExpEthDisabledStatus,
       "ibmOsaExpEthConfigName": ibmOsaExpEthConfigName,
       "ibmOsaExpEthConfigSpeedMode": ibmOsaExpEthConfigSpeedMode,
       "ibmOsaExpEthActiveSpeedMode": ibmOsaExpEthActiveSpeedMode,
       "ibmOsaExpEthMacAddrActive": ibmOsaExpEthMacAddrActive,
       "ibmOsaExpEthMacAddrBurntIn": ibmOsaExpEthMacAddrBurntIn,
       "ibmOsaExpEthUserData": ibmOsaExpEthUserData,
       "ibmOsaExpEthOutPackets": ibmOsaExpEthOutPackets,
       "ibmOsaExpEthInPackets": ibmOsaExpEthInPackets,
       "ibmOsaExpEthInGroupFrames": ibmOsaExpEthInGroupFrames,
       "ibmOsaExpEthInBroadcastFrames": ibmOsaExpEthInBroadcastFrames,
       "ibmOsaExpEthPortName": ibmOsaExpEthPortName,
       "ibmOsaExpEthInUnknownIPFrames": ibmOsaExpEthInUnknownIPFrames,
       "ibmOsaExpEthGroupAddrTable": ibmOsaExpEthGroupAddrTable,
       "ibmOSAExpTRPortTable": ibmOSAExpTRPortTable,
       "ibmOSAExpTRPortEntry": ibmOSAExpTRPortEntry,
       "ibmOsaExpTRPortNumber": ibmOsaExpTRPortNumber,
       "ibmOsaExpTRPortType": ibmOsaExpTRPortType,
       "ibmOsaExpTRLanTrafficState": ibmOsaExpTRLanTrafficState,
       "ibmOsaExpTRServiceMode": ibmOsaExpTRServiceMode,
       "ibmOsaExpTRDisabledStatus": ibmOsaExpTRDisabledStatus,
       "ibmOsaExpTRConfigName": ibmOsaExpTRConfigName,
       "ibmOsaExpTRMacAddrActive": ibmOsaExpTRMacAddrActive,
       "ibmOsaExpTRMacAddrBurntIn": ibmOsaExpTRMacAddrBurntIn,
       "ibmOsaExpTRConfigSpeedMode": ibmOsaExpTRConfigSpeedMode,
       "ibmOsaExpTRActiveSpeedMode": ibmOsaExpTRActiveSpeedMode,
       "ibmOsaExpTRUserData": ibmOsaExpTRUserData,
       "ibmOsaExpTRPortName": ibmOsaExpTRPortName,
       "ibmOsaExpTRGroupAddrTable": ibmOsaExpTRGroupAddrTable,
       "ibmOsaExpTRFunctionalAddr": ibmOsaExpTRFunctionalAddr,
       "ibmOsaExpTRRingStatus": ibmOsaExpTRRingStatus,
       "ibmOsaExpTRAllowAccessPriority": ibmOsaExpTRAllowAccessPriority,
       "ibmOsaExpTREarlyTokenRelease": ibmOsaExpTREarlyTokenRelease,
       "ibmOsaExpTRBeaconingAddress": ibmOsaExpTRBeaconingAddress,
       "ibmOsaExpTRUpstreamNeighbor": ibmOsaExpTRUpstreamNeighbor,
       "ibmOsaExpTRRingState": ibmOsaExpTRRingState,
       "ibmOsaExpTRRingOpenStatus": ibmOsaExpTRRingOpenStatus,
       "ibmOsaExpTRPacketsTransmitted": ibmOsaExpTRPacketsTransmitted,
       "ibmOsaExpTRPacketsReceived": ibmOsaExpTRPacketsReceived,
       "ibmOsaExpTRLineErrorCount": ibmOsaExpTRLineErrorCount,
       "ibmOsaExpTRBurstErrorCount": ibmOsaExpTRBurstErrorCount,
       "ibmOsaExpTRACErrorCount": ibmOsaExpTRACErrorCount,
       "ibmOsaExpTRAbortTransErrorCount": ibmOsaExpTRAbortTransErrorCount,
       "ibmOsaExpTRInternalErrorCount": ibmOsaExpTRInternalErrorCount,
       "ibmOsaExpTRLostFrameErrorCount": ibmOsaExpTRLostFrameErrorCount,
       "ibmOsaExpTRRcvCongestionCount": ibmOsaExpTRRcvCongestionCount,
       "ibmOsaExpTRFrameCopyErrorCount": ibmOsaExpTRFrameCopyErrorCount,
       "ibmOsaExpTRTokenErrorCount": ibmOsaExpTRTokenErrorCount,
       "ibmOsaExpTRFullDuplexErrorCount": ibmOsaExpTRFullDuplexErrorCount,
       "ibmOsaExpTRSoftErrorCount": ibmOsaExpTRSoftErrorCount,
       "ibmOsaExpTRHardErrorCount": ibmOsaExpTRHardErrorCount,
       "ibmOsaExpTRSignalLossErrorCount": ibmOsaExpTRSignalLossErrorCount,
       "ibmOsaExpTRTransmitBeaconCount": ibmOsaExpTRTransmitBeaconCount,
       "ibmOsaExpTRRecoveryCounter": ibmOsaExpTRRecoveryCounter,
       "ibmOsaExpTRLobeWireFaultCount": ibmOsaExpTRLobeWireFaultCount,
       "ibmOsaExpTRRemoveReceivedCount": ibmOsaExpTRRemoveReceivedCount,
       "ibmOsaExpTRSingleStationCount": ibmOsaExpTRSingleStationCount,
       "ibmOSAExpATMPortTable": ibmOSAExpATMPortTable,
       "ibmOSAExpATMPortEntry": ibmOSAExpATMPortEntry,
       "ibmOsaExpATMPortNumber": ibmOsaExpATMPortNumber,
       "ibmOsaExpATMPortType": ibmOsaExpATMPortType,
       "ibmOsaExpATMLanTrafficState": ibmOsaExpATMLanTrafficState,
       "ibmOsaExpATMServiceMode": ibmOsaExpATMServiceMode,
       "ibmOsaExpATMDisabledStatus": ibmOsaExpATMDisabledStatus,
       "ibmOsaExpATMConfigName": ibmOsaExpATMConfigName,
       "ibmOsaExpATMMacAddrActive": ibmOsaExpATMMacAddrActive,
       "ibmOsaExpATMMacAddrBurntIn": ibmOsaExpATMMacAddrBurntIn,
       "ibmOsaExpATMUserData": ibmOsaExpATMUserData,
       "ibmOsaExpATMPortName": ibmOsaExpATMPortName,
       "ibmOsaExpATMGroupMacAddrTable": ibmOsaExpATMGroupMacAddrTable,
       "ibmOsaExpATMIBMEnhancedMode": ibmOsaExpATMIBMEnhancedMode,
       "ibmOsaExpATMBestEffortPeakRate": ibmOsaExpATMBestEffortPeakRate,
       "ibmOsaExpATMConfigMode": ibmOsaExpATMConfigMode,
       "ibmOsaExpATMConfigLanType": ibmOsaExpATMConfigLanType,
       "ibmOsaExpATMActualLanType": ibmOsaExpATMActualLanType,
       "ibmOsaExpATMConfigMaxDataFrmSz": ibmOsaExpATMConfigMaxDataFrmSz,
       "ibmOsaExpATMActualMaxDataFrmSz": ibmOsaExpATMActualMaxDataFrmSz,
       "ibmOsaExpATMConfigELANName": ibmOsaExpATMConfigELANName,
       "ibmOsaExpATMActualELANName": ibmOsaExpATMActualELANName,
       "ibmOsaExpATMConfigLESATMAddress": ibmOsaExpATMConfigLESATMAddress,
       "ibmOsaExpATMActualLESATMAddress": ibmOsaExpATMActualLESATMAddress,
       "ibmOsaExpATMControlTimeout": ibmOsaExpATMControlTimeout,
       "ibmOsaExpATMMaxUnknownFrameCount": ibmOsaExpATMMaxUnknownFrameCount,
       "ibmOsaExpATMMaxUnknownFrameTime": ibmOsaExpATMMaxUnknownFrameTime,
       "ibmOsaExpATMVCCTimeoutPeriod": ibmOsaExpATMVCCTimeoutPeriod,
       "ibmOsaExpATMMaxRetryCount": ibmOsaExpATMMaxRetryCount,
       "ibmOsaExpATMAgingTime": ibmOsaExpATMAgingTime,
       "ibmOsaExpATMForwardDelayTime": ibmOsaExpATMForwardDelayTime,
       "ibmOsaExpATMExpectedARPRespTime": ibmOsaExpATMExpectedARPRespTime,
       "ibmOsaExpATMFlushTimeout": ibmOsaExpATMFlushTimeout,
       "ibmOsaExpATMPathSwitchingDelay": ibmOsaExpATMPathSwitchingDelay,
       "ibmOsaExpATMLocalSegmentID": ibmOsaExpATMLocalSegmentID,
       "ibmOsaExpATMMltcstSendVCCType": ibmOsaExpATMMltcstSendVCCType,
       "ibmOsaExpATMMltcstSendVCCAvgRate": ibmOsaExpATMMltcstSendVCCAvgRate,
       "ibmOsaExpATMMcastSendVCCPeakRate": ibmOsaExpATMMcastSendVCCPeakRate,
       "ibmOsaExpATMConnectCompleteTimer": ibmOsaExpATMConnectCompleteTimer,
       "ibmOsaExpATMClientATMAddress": ibmOsaExpATMClientATMAddress,
       "ibmOsaExpATMClientIdentifier": ibmOsaExpATMClientIdentifier,
       "ibmOsaExpATMClientCurrentState": ibmOsaExpATMClientCurrentState,
       "ibmOsaExpATMLastFailureRespCode": ibmOsaExpATMLastFailureRespCode,
       "ibmOsaExpATMLastFailureState": ibmOsaExpATMLastFailureState,
       "ibmOsaExpATMProtocol": ibmOsaExpATMProtocol,
       "ibmOsaExpATMLeVersion": ibmOsaExpATMLeVersion,
       "ibmOsaExpATMTopologyChange": ibmOsaExpATMTopologyChange,
       "ibmOsaExpATMConfigServerATMAddr": ibmOsaExpATMConfigServerATMAddr,
       "ibmOsaExpATMConfigSource": ibmOsaExpATMConfigSource,
       "ibmOsaExpATMProxyClient": ibmOsaExpATMProxyClient,
       "ibmOsaExpATMLePDUOctetsInbound": ibmOsaExpATMLePDUOctetsInbound,
       "ibmOsaExpATMNonErrLePDUDiscIn": ibmOsaExpATMNonErrLePDUDiscIn,
       "ibmOsaExpATMErrLePDUDiscIn": ibmOsaExpATMErrLePDUDiscIn,
       "ibmOsaExpATMLePDUOctetsOutbound": ibmOsaExpATMLePDUOctetsOutbound,
       "ibmOsaExpATMNonErrLePDUDiscOut": ibmOsaExpATMNonErrLePDUDiscOut,
       "ibmOsaExpATMErrLePDUDiscOut": ibmOsaExpATMErrLePDUDiscOut,
       "ibmOsaExpATMLeARPRequestsOut": ibmOsaExpATMLeARPRequestsOut,
       "ibmOsaExpATMLeARPRequestsIn": ibmOsaExpATMLeARPRequestsIn,
       "ibmOsaExpATMLeARPRepliesOut": ibmOsaExpATMLeARPRepliesOut,
       "ibmOsaExpATMLeARPRepliesIn": ibmOsaExpATMLeARPRepliesIn,
       "ibmOsaExpATMControlFramesOut": ibmOsaExpATMControlFramesOut,
       "ibmOsaExpATMControlFramesIn": ibmOsaExpATMControlFramesIn,
       "ibmOsaExpATMSVCFailures": ibmOsaExpATMSVCFailures,
       "ibmOsaExpATMConfigDirectIntfc": ibmOsaExpATMConfigDirectIntfc,
       "ibmOsaExpATMConfigDirectVPI": ibmOsaExpATMConfigDirectVPI,
       "ibmOsaExpATMConfigDirectVCI": ibmOsaExpATMConfigDirectVCI,
       "ibmOsaExpATMControlDirectIntfc": ibmOsaExpATMControlDirectIntfc,
       "ibmOsaExpATMControlDirectVPI": ibmOsaExpATMControlDirectVPI,
       "ibmOsaExpATMControlDirectVCI": ibmOsaExpATMControlDirectVCI,
       "ibmOsaExpATMControlDistIntfc": ibmOsaExpATMControlDistIntfc,
       "ibmOsaExpATMControlDistributeVPI": ibmOsaExpATMControlDistributeVPI,
       "ibmOsaExpATMControlDistributeVCI": ibmOsaExpATMControlDistributeVCI,
       "ibmOsaExpATMMulticastSendIntfc": ibmOsaExpATMMulticastSendIntfc,
       "ibmOsaExpATMMulticastSendVPI": ibmOsaExpATMMulticastSendVPI,
       "ibmOsaExpATMMulticastSendVCI": ibmOsaExpATMMulticastSendVCI,
       "ibmOsaExpATMMulticastFwdIntfc": ibmOsaExpATMMulticastFwdIntfc,
       "ibmOsaExpATMMulticastForwardVPI": ibmOsaExpATMMulticastForwardVPI,
       "ibmOsaExpATMMulticastForwardVCI": ibmOsaExpATMMulticastForwardVCI,
       "ibmOSAMibConformance": ibmOSAMibConformance,
       "ibmOSAMibCompliances": ibmOSAMibCompliances,
       "ibmOSAMibCompliance": ibmOSAMibCompliance,
       "ibmOSAMibGroups": ibmOSAMibGroups,
       "ibmOSAExpChannelGroup": ibmOSAExpChannelGroup,
       "ibmOSAExpPerfGroup": ibmOSAExpPerfGroup,
       "ibmOSAExpPEGroup": ibmOSAExpPEGroup,
       "ibmOSAExpEthGroup": ibmOSAExpEthGroup,
       "ibmOSAExpTRGroup": ibmOSAExpTRGroup,
       "ibmOSAExpATMGroup": ibmOSAExpATMGroup}
)
