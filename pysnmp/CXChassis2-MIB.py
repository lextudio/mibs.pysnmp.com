# SNMP MIB module (CXChassis2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXChassis2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:14 2024
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

(cxChassis2,) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "cxChassis2")

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



class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CxChassIfAdmGroup_ObjectIdentity = ObjectIdentity
cxChassIfAdmGroup = _CxChassIfAdmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 9, 5)
)
_CxChassLogIfAdmTable_Object = MibTable
cxChassLogIfAdmTable = _CxChassLogIfAdmTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 9, 5, 2)
)
if mibBuilder.loadTexts:
    cxChassLogIfAdmTable.setStatus("mandatory")
_CxChassLogIfAdmEntry_Object = MibTableRow
cxChassLogIfAdmEntry = _CxChassLogIfAdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 9, 5, 2, 1)
)
cxChassLogIfAdmEntry.setIndexNames(
    (0, "CXChassis2-MIB", "cxChassLogIfAdmCpuIndex"),
    (0, "CXChassis2-MIB", "cxChassLogIfAdmIfType"),
    (0, "CXChassis2-MIB", "cxChassLogIfAdmChannelIndex"),
)
if mibBuilder.loadTexts:
    cxChassLogIfAdmEntry.setStatus("mandatory")


class _CxChassLogIfAdmCpuIndex_Type(Integer32):
    """Custom type cxChassLogIfAdmCpuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CxChassLogIfAdmCpuIndex_Type.__name__ = "Integer32"
_CxChassLogIfAdmCpuIndex_Object = MibTableColumn
cxChassLogIfAdmCpuIndex = _CxChassLogIfAdmCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 9, 5, 2, 1, 1),
    _CxChassLogIfAdmCpuIndex_Type()
)
cxChassLogIfAdmCpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxChassLogIfAdmCpuIndex.setStatus("mandatory")


class _CxChassLogIfAdmIfType_Type(Integer32):
    """Custom type cxChassLogIfAdmIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CxChassLogIfAdmIfType_Type.__name__ = "Integer32"
_CxChassLogIfAdmIfType_Object = MibTableColumn
cxChassLogIfAdmIfType = _CxChassLogIfAdmIfType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 9, 5, 2, 1, 2),
    _CxChassLogIfAdmIfType_Type()
)
cxChassLogIfAdmIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxChassLogIfAdmIfType.setStatus("mandatory")
_CxChassLogIfAdmChannelIndex_Type = Integer32
_CxChassLogIfAdmChannelIndex_Object = MibTableColumn
cxChassLogIfAdmChannelIndex = _CxChassLogIfAdmChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 9, 5, 2, 1, 3),
    _CxChassLogIfAdmChannelIndex_Type()
)
cxChassLogIfAdmChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxChassLogIfAdmChannelIndex.setStatus("mandatory")


class _CxChassLogIfAdmIfIndex_Type(Integer32):
    """Custom type cxChassLogIfAdmIfIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CxChassLogIfAdmIfIndex_Type.__name__ = "Integer32"
_CxChassLogIfAdmIfIndex_Object = MibTableColumn
cxChassLogIfAdmIfIndex = _CxChassLogIfAdmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 9, 5, 2, 1, 4),
    _CxChassLogIfAdmIfIndex_Type()
)
cxChassLogIfAdmIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxChassLogIfAdmIfIndex.setStatus("mandatory")


class _CxChassLogIfAdmRowStatus_Type(RowStatus):
    """Custom type cxChassLogIfAdmRowStatus based on RowStatus"""


_CxChassLogIfAdmRowStatus_Object = MibTableColumn
cxChassLogIfAdmRowStatus = _CxChassLogIfAdmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 9, 5, 2, 1, 5),
    _CxChassLogIfAdmRowStatus_Type()
)
cxChassLogIfAdmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxChassLogIfAdmRowStatus.setStatus("mandatory")
_IfMIB_ObjectIdentity = ObjectIdentity
ifMIB = _IfMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 9, 6)
)
_IfMIBObjects_ObjectIdentity = ObjectIdentity
ifMIBObjects = _IfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 9, 6, 1)
)
_IfStackTable_Object = MibTable
ifStackTable = _IfStackTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 9, 6, 1, 2)
)
if mibBuilder.loadTexts:
    ifStackTable.setStatus("mandatory")
_IfStackEntry_Object = MibTableRow
ifStackEntry = _IfStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 9, 6, 1, 2, 1)
)
ifStackEntry.setIndexNames(
    (0, "CXChassis2-MIB", "ifStackHigherLayer"),
    (0, "CXChassis2-MIB", "ifStackLowerLayer"),
)
if mibBuilder.loadTexts:
    ifStackEntry.setStatus("mandatory")
_IfStackHigherLayer_Type = Integer32
_IfStackHigherLayer_Object = MibTableColumn
ifStackHigherLayer = _IfStackHigherLayer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 9, 6, 1, 2, 1, 1),
    _IfStackHigherLayer_Type()
)
ifStackHigherLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStackHigherLayer.setStatus("mandatory")
_IfStackLowerLayer_Type = Integer32
_IfStackLowerLayer_Object = MibTableColumn
ifStackLowerLayer = _IfStackLowerLayer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 9, 6, 1, 2, 1, 2),
    _IfStackLowerLayer_Type()
)
ifStackLowerLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStackLowerLayer.setStatus("mandatory")
_IfStackStatus_Type = RowStatus
_IfStackStatus_Object = MibTableColumn
ifStackStatus = _IfStackStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 9, 6, 1, 2, 1, 3),
    _IfStackStatus_Type()
)
ifStackStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifStackStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXChassis2-MIB",
    **{"RowStatus": RowStatus,
       "cxChassIfAdmGroup": cxChassIfAdmGroup,
       "cxChassLogIfAdmTable": cxChassLogIfAdmTable,
       "cxChassLogIfAdmEntry": cxChassLogIfAdmEntry,
       "cxChassLogIfAdmCpuIndex": cxChassLogIfAdmCpuIndex,
       "cxChassLogIfAdmIfType": cxChassLogIfAdmIfType,
       "cxChassLogIfAdmChannelIndex": cxChassLogIfAdmChannelIndex,
       "cxChassLogIfAdmIfIndex": cxChassLogIfAdmIfIndex,
       "cxChassLogIfAdmRowStatus": cxChassLogIfAdmRowStatus,
       "ifMIB": ifMIB,
       "ifMIBObjects": ifMIBObjects,
       "ifStackTable": ifStackTable,
       "ifStackEntry": ifStackEntry,
       "ifStackHigherLayer": ifStackHigherLayer,
       "ifStackLowerLayer": ifStackLowerLayer,
       "ifStackStatus": ifStackStatus}
)
