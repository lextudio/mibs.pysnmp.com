# SNMP MIB module (HH3C-EVC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-EVC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:12 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hh3cEvc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106)
)
hh3cEvc.setRevisions(
        ("2009-08-08 10:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cEvcObjects_ObjectIdentity = ObjectIdentity
hh3cEvcObjects = _Hh3cEvcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1)
)
_Hh3cEvcScalarGroup_ObjectIdentity = ObjectIdentity
hh3cEvcScalarGroup = _Hh3cEvcScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 1)
)


class _Hh3cEvcSrvInstEncapCapabilities_Type(Bits):
    """Custom type hh3cEvcSrvInstEncapCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("encapPortBased", 0),
          ("encapSvlanId", 3),
          ("encapSvlanIdList", 4),
          ("encapSvlanIdOnlyTagged", 5),
          ("encapTagged", 2),
          ("encapUntagged", 1))
    )

_Hh3cEvcSrvInstEncapCapabilities_Type.__name__ = "Bits"
_Hh3cEvcSrvInstEncapCapabilities_Object = MibScalar
hh3cEvcSrvInstEncapCapabilities = _Hh3cEvcSrvInstEncapCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 1, 1),
    _Hh3cEvcSrvInstEncapCapabilities_Type()
)
hh3cEvcSrvInstEncapCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEvcSrvInstEncapCapabilities.setStatus("current")
_Hh3cEvcPortMaxSrvInstNum_Type = Integer32
_Hh3cEvcPortMaxSrvInstNum_Object = MibScalar
hh3cEvcPortMaxSrvInstNum = _Hh3cEvcPortMaxSrvInstNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 1, 2),
    _Hh3cEvcPortMaxSrvInstNum_Type()
)
hh3cEvcPortMaxSrvInstNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEvcPortMaxSrvInstNum.setStatus("current")
_Hh3cEvcSrvInstTable_Object = MibTable
hh3cEvcSrvInstTable = _Hh3cEvcSrvInstTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cEvcSrvInstTable.setStatus("current")
_Hh3cEvcSrvInstEntry_Object = MibTableRow
hh3cEvcSrvInstEntry = _Hh3cEvcSrvInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 2, 1)
)
hh3cEvcSrvInstEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EVC-MIB", "hh3cEvcSrvInstId"),
)
if mibBuilder.loadTexts:
    hh3cEvcSrvInstEntry.setStatus("current")
_Hh3cEvcSrvInstId_Type = Integer32
_Hh3cEvcSrvInstId_Object = MibTableColumn
hh3cEvcSrvInstId = _Hh3cEvcSrvInstId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 2, 1, 1),
    _Hh3cEvcSrvInstId_Type()
)
hh3cEvcSrvInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEvcSrvInstId.setStatus("current")


class _Hh3cEvcSrvInstEncap_Type(Integer32):
    """Custom type hh3cEvcSrvInstEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("portBased", 1),
          ("svlanIdList", 4),
          ("svlanIdListOnlyTagged", 5),
          ("tagged", 3),
          ("untagged", 2))
    )


_Hh3cEvcSrvInstEncap_Type.__name__ = "Integer32"
_Hh3cEvcSrvInstEncap_Object = MibTableColumn
hh3cEvcSrvInstEncap = _Hh3cEvcSrvInstEncap_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 2, 1, 2),
    _Hh3cEvcSrvInstEncap_Type()
)
hh3cEvcSrvInstEncap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEvcSrvInstEncap.setStatus("current")


class _Hh3cEvcSrvInstSvlanIdListLow_Type(OctetString):
    """Custom type hh3cEvcSrvInstSvlanIdListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Hh3cEvcSrvInstSvlanIdListLow_Type.__name__ = "OctetString"
_Hh3cEvcSrvInstSvlanIdListLow_Object = MibTableColumn
hh3cEvcSrvInstSvlanIdListLow = _Hh3cEvcSrvInstSvlanIdListLow_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 2, 1, 3),
    _Hh3cEvcSrvInstSvlanIdListLow_Type()
)
hh3cEvcSrvInstSvlanIdListLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEvcSrvInstSvlanIdListLow.setStatus("current")


class _Hh3cEvcSrvInstSvlanIdListHigh_Type(OctetString):
    """Custom type hh3cEvcSrvInstSvlanIdListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Hh3cEvcSrvInstSvlanIdListHigh_Type.__name__ = "OctetString"
_Hh3cEvcSrvInstSvlanIdListHigh_Object = MibTableColumn
hh3cEvcSrvInstSvlanIdListHigh = _Hh3cEvcSrvInstSvlanIdListHigh_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 2, 1, 4),
    _Hh3cEvcSrvInstSvlanIdListHigh_Type()
)
hh3cEvcSrvInstSvlanIdListHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEvcSrvInstSvlanIdListHigh.setStatus("current")
_Hh3cEvcSrvInstRowStatus_Type = RowStatus
_Hh3cEvcSrvInstRowStatus_Object = MibTableColumn
hh3cEvcSrvInstRowStatus = _Hh3cEvcSrvInstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 2, 1, 5),
    _Hh3cEvcSrvInstRowStatus_Type()
)
hh3cEvcSrvInstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEvcSrvInstRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-EVC-MIB",
    **{"hh3cEvc": hh3cEvc,
       "hh3cEvcObjects": hh3cEvcObjects,
       "hh3cEvcScalarGroup": hh3cEvcScalarGroup,
       "hh3cEvcSrvInstEncapCapabilities": hh3cEvcSrvInstEncapCapabilities,
       "hh3cEvcPortMaxSrvInstNum": hh3cEvcPortMaxSrvInstNum,
       "hh3cEvcSrvInstTable": hh3cEvcSrvInstTable,
       "hh3cEvcSrvInstEntry": hh3cEvcSrvInstEntry,
       "hh3cEvcSrvInstId": hh3cEvcSrvInstId,
       "hh3cEvcSrvInstEncap": hh3cEvcSrvInstEncap,
       "hh3cEvcSrvInstSvlanIdListLow": hh3cEvcSrvInstSvlanIdListLow,
       "hh3cEvcSrvInstSvlanIdListHigh": hh3cEvcSrvInstSvlanIdListHigh,
       "hh3cEvcSrvInstRowStatus": hh3cEvcSrvInstRowStatus}
)
