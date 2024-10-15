# SNMP MIB module (Wellfleet-WFDOT1D-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-WFDOT1D-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:30 2024
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
 Opaque,
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 mgmt,
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
    "Opaque",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "mgmt",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wfBridgeGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfBridgeGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfDot1d_ObjectIdentity = ObjectIdentity
wfDot1d = _WfDot1d_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 6)
)
_WfDot1dBaseGroup_ObjectIdentity = ObjectIdentity
wfDot1dBaseGroup = _WfDot1dBaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 6, 1)
)
_WfDot1dBaseBridgeAddress_Type = OctetString
_WfDot1dBaseBridgeAddress_Object = MibScalar
wfDot1dBaseBridgeAddress = _WfDot1dBaseBridgeAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 6, 1, 1),
    _WfDot1dBaseBridgeAddress_Type()
)
wfDot1dBaseBridgeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDot1dBaseBridgeAddress.setStatus("mandatory")
_WfDot1dBaseNumPorts_Type = Integer32
_WfDot1dBaseNumPorts_Object = MibScalar
wfDot1dBaseNumPorts = _WfDot1dBaseNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 6, 1, 2),
    _WfDot1dBaseNumPorts_Type()
)
wfDot1dBaseNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDot1dBaseNumPorts.setStatus("mandatory")


class _WfDot1dBaseType_Type(Integer32):
    """Custom type wfDot1dBaseType based on Integer32"""
    defaultValue = 2

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
        *(("only", 2),
          ("sr", 3),
          ("srt", 4),
          ("unk", 1))
    )


_WfDot1dBaseType_Type.__name__ = "Integer32"
_WfDot1dBaseType_Object = MibScalar
wfDot1dBaseType = _WfDot1dBaseType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 6, 1, 3),
    _WfDot1dBaseType_Type()
)
wfDot1dBaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDot1dBaseType.setStatus("mandatory")
_WfDot1dStaticGroup_ObjectIdentity = ObjectIdentity
wfDot1dStaticGroup = _WfDot1dStaticGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 6, 5)
)
_WfDot1dStaticTable_Object = MibTable
wfDot1dStaticTable = _WfDot1dStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 6, 5, 1)
)
if mibBuilder.loadTexts:
    wfDot1dStaticTable.setStatus("mandatory")
_WfDot1dStaticTableEntry_Object = MibTableRow
wfDot1dStaticTableEntry = _WfDot1dStaticTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 6, 5, 1, 1)
)
wfDot1dStaticTableEntry.setIndexNames(
    (0, "Wellfleet-WFDOT1D-MIB", "wfDot1dStaticAddress"),
    (0, "Wellfleet-WFDOT1D-MIB", "wfDot1dStaticReceivePort"),
)
if mibBuilder.loadTexts:
    wfDot1dStaticTableEntry.setStatus("mandatory")


class _WfDot1dStaticAddress_Type(OctetString):
    """Custom type wfDot1dStaticAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WfDot1dStaticAddress_Type.__name__ = "OctetString"
_WfDot1dStaticAddress_Object = MibTableColumn
wfDot1dStaticAddress = _WfDot1dStaticAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 6, 5, 1, 1, 1),
    _WfDot1dStaticAddress_Type()
)
wfDot1dStaticAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDot1dStaticAddress.setStatus("mandatory")
_WfDot1dStaticReceivePort_Type = Integer32
_WfDot1dStaticReceivePort_Object = MibTableColumn
wfDot1dStaticReceivePort = _WfDot1dStaticReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 6, 5, 1, 1, 2),
    _WfDot1dStaticReceivePort_Type()
)
wfDot1dStaticReceivePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDot1dStaticReceivePort.setStatus("mandatory")
_WfDot1dStaticAllowedToGoTo_Type = OctetString
_WfDot1dStaticAllowedToGoTo_Object = MibTableColumn
wfDot1dStaticAllowedToGoTo = _WfDot1dStaticAllowedToGoTo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 6, 5, 1, 1, 3),
    _WfDot1dStaticAllowedToGoTo_Type()
)
wfDot1dStaticAllowedToGoTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDot1dStaticAllowedToGoTo.setStatus("mandatory")


class _WfDot1dStaticStatus_Type(Integer32):
    """Custom type wfDot1dStaticStatus based on Integer32"""
    defaultValue = 2

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
        *(("invalid", 2),
          ("other", 1),
          ("permanent", 3),
          ("reset", 4),
          ("timeout", 5))
    )


_WfDot1dStaticStatus_Type.__name__ = "Integer32"
_WfDot1dStaticStatus_Object = MibTableColumn
wfDot1dStaticStatus = _WfDot1dStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 6, 5, 1, 1, 4),
    _WfDot1dStaticStatus_Type()
)
wfDot1dStaticStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDot1dStaticStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-WFDOT1D-MIB",
    **{"wfDot1d": wfDot1d,
       "wfDot1dBaseGroup": wfDot1dBaseGroup,
       "wfDot1dBaseBridgeAddress": wfDot1dBaseBridgeAddress,
       "wfDot1dBaseNumPorts": wfDot1dBaseNumPorts,
       "wfDot1dBaseType": wfDot1dBaseType,
       "wfDot1dStaticGroup": wfDot1dStaticGroup,
       "wfDot1dStaticTable": wfDot1dStaticTable,
       "wfDot1dStaticTableEntry": wfDot1dStaticTableEntry,
       "wfDot1dStaticAddress": wfDot1dStaticAddress,
       "wfDot1dStaticReceivePort": wfDot1dStaticReceivePort,
       "wfDot1dStaticAllowedToGoTo": wfDot1dStaticAllowedToGoTo,
       "wfDot1dStaticStatus": wfDot1dStaticStatus}
)
