# SNMP MIB module (H3C-EVC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-EVC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:50:31 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cEvc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 106)
)
h3cEvc.setRevisions(
        ("2009-08-08 10:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cEvcObjects_ObjectIdentity = ObjectIdentity
h3cEvcObjects = _H3cEvcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 106, 1)
)
_H3cEvcScalarGroup_ObjectIdentity = ObjectIdentity
h3cEvcScalarGroup = _H3cEvcScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 106, 1, 1)
)


class _H3cEvcSrvInstEncapCapabilities_Type(Bits):
    """Custom type h3cEvcSrvInstEncapCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("encapPortBased", 0),
          ("encapSvlanId", 3),
          ("encapSvlanIdList", 4),
          ("encapSvlanIdOnlyTagged", 5),
          ("encapTagged", 2),
          ("encapUntagged", 1))
    )

_H3cEvcSrvInstEncapCapabilities_Type.__name__ = "Bits"
_H3cEvcSrvInstEncapCapabilities_Object = MibScalar
h3cEvcSrvInstEncapCapabilities = _H3cEvcSrvInstEncapCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 106, 1, 1, 1),
    _H3cEvcSrvInstEncapCapabilities_Type()
)
h3cEvcSrvInstEncapCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEvcSrvInstEncapCapabilities.setStatus("current")
_H3cEvcPortMaxSrvInstNum_Type = Integer32
_H3cEvcPortMaxSrvInstNum_Object = MibScalar
h3cEvcPortMaxSrvInstNum = _H3cEvcPortMaxSrvInstNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 106, 1, 1, 2),
    _H3cEvcPortMaxSrvInstNum_Type()
)
h3cEvcPortMaxSrvInstNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEvcPortMaxSrvInstNum.setStatus("current")
_H3cEvcSrvInstTable_Object = MibTable
h3cEvcSrvInstTable = _H3cEvcSrvInstTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 106, 1, 2)
)
if mibBuilder.loadTexts:
    h3cEvcSrvInstTable.setStatus("current")
_H3cEvcSrvInstEntry_Object = MibTableRow
h3cEvcSrvInstEntry = _H3cEvcSrvInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 106, 1, 2, 1)
)
h3cEvcSrvInstEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H3C-EVC-MIB", "h3cEvcSrvInstId"),
)
if mibBuilder.loadTexts:
    h3cEvcSrvInstEntry.setStatus("current")
_H3cEvcSrvInstId_Type = Integer32
_H3cEvcSrvInstId_Object = MibTableColumn
h3cEvcSrvInstId = _H3cEvcSrvInstId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 106, 1, 2, 1, 1),
    _H3cEvcSrvInstId_Type()
)
h3cEvcSrvInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEvcSrvInstId.setStatus("current")


class _H3cEvcSrvInstEncap_Type(Integer32):
    """Custom type h3cEvcSrvInstEncap based on Integer32"""
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


_H3cEvcSrvInstEncap_Type.__name__ = "Integer32"
_H3cEvcSrvInstEncap_Object = MibTableColumn
h3cEvcSrvInstEncap = _H3cEvcSrvInstEncap_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 106, 1, 2, 1, 2),
    _H3cEvcSrvInstEncap_Type()
)
h3cEvcSrvInstEncap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEvcSrvInstEncap.setStatus("current")


class _H3cEvcSrvInstSvlanIdListLow_Type(OctetString):
    """Custom type h3cEvcSrvInstSvlanIdListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_H3cEvcSrvInstSvlanIdListLow_Type.__name__ = "OctetString"
_H3cEvcSrvInstSvlanIdListLow_Object = MibTableColumn
h3cEvcSrvInstSvlanIdListLow = _H3cEvcSrvInstSvlanIdListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 106, 1, 2, 1, 3),
    _H3cEvcSrvInstSvlanIdListLow_Type()
)
h3cEvcSrvInstSvlanIdListLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEvcSrvInstSvlanIdListLow.setStatus("current")


class _H3cEvcSrvInstSvlanIdListHigh_Type(OctetString):
    """Custom type h3cEvcSrvInstSvlanIdListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_H3cEvcSrvInstSvlanIdListHigh_Type.__name__ = "OctetString"
_H3cEvcSrvInstSvlanIdListHigh_Object = MibTableColumn
h3cEvcSrvInstSvlanIdListHigh = _H3cEvcSrvInstSvlanIdListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 106, 1, 2, 1, 4),
    _H3cEvcSrvInstSvlanIdListHigh_Type()
)
h3cEvcSrvInstSvlanIdListHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEvcSrvInstSvlanIdListHigh.setStatus("current")
_H3cEvcSrvInstRowStatus_Type = RowStatus
_H3cEvcSrvInstRowStatus_Object = MibTableColumn
h3cEvcSrvInstRowStatus = _H3cEvcSrvInstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 106, 1, 2, 1, 5),
    _H3cEvcSrvInstRowStatus_Type()
)
h3cEvcSrvInstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEvcSrvInstRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-EVC-MIB",
    **{"h3cEvc": h3cEvc,
       "h3cEvcObjects": h3cEvcObjects,
       "h3cEvcScalarGroup": h3cEvcScalarGroup,
       "h3cEvcSrvInstEncapCapabilities": h3cEvcSrvInstEncapCapabilities,
       "h3cEvcPortMaxSrvInstNum": h3cEvcPortMaxSrvInstNum,
       "h3cEvcSrvInstTable": h3cEvcSrvInstTable,
       "h3cEvcSrvInstEntry": h3cEvcSrvInstEntry,
       "h3cEvcSrvInstId": h3cEvcSrvInstId,
       "h3cEvcSrvInstEncap": h3cEvcSrvInstEncap,
       "h3cEvcSrvInstSvlanIdListLow": h3cEvcSrvInstSvlanIdListLow,
       "h3cEvcSrvInstSvlanIdListHigh": h3cEvcSrvInstSvlanIdListHigh,
       "h3cEvcSrvInstRowStatus": h3cEvcSrvInstRowStatus}
)
