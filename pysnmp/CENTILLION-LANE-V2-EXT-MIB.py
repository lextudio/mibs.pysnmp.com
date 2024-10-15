# SNMP MIB module (CENTILLION-LANE-V2-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CENTILLION-LANE-V2-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:07 2024
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

(atmLane,) = mibBuilder.importSymbols(
    "CENTILLION-ROOT-MIB",
    "atmLane")

(AtmLaneAddress,) = mibBuilder.importSymbols(
    "LAN-EMULATION-CLIENT-MIB",
    "AtmLaneAddress")

(elanConfIndex,
 lecsConfIndex) = mibBuilder.importSymbols(
    "LAN-EMULATION-ELAN-MIB",
    "elanConfIndex",
    "lecsConfIndex")

(lesConfIndex,) = mibBuilder.importSymbols(
    "LAN-EMULATION-LES-MIB",
    "lesConfIndex")

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

(TruthValue,) = mibBuilder.importSymbols(
    "SNMPv2-TC-v1",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions



class CnLesLecDataFrameSize(Integer32):
    """Custom type CnLesLecDataFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("max1516", 2),
          ("max1580", 6),
          ("max18190", 5),
          ("max4544", 3),
          ("max9234", 4))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CnLesV2ExtnGroup_ObjectIdentity = ObjectIdentity
cnLesV2ExtnGroup = _CnLesV2ExtnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 7)
)
_CnLesV2ExtnTable_Object = MibTable
cnLesV2ExtnTable = _CnLesV2ExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 7, 1)
)
if mibBuilder.loadTexts:
    cnLesV2ExtnTable.setStatus("mandatory")
_CnLesV2ExtnEntry_Object = MibTableRow
cnLesV2ExtnEntry = _CnLesV2ExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 7, 1, 1)
)
cnLesV2ExtnEntry.setIndexNames(
    (0, "LAN-EMULATION-LES-MIB", "lesConfIndex"),
)
if mibBuilder.loadTexts:
    cnLesV2ExtnEntry.setStatus("mandatory")


class _CnLesV2ExtnV2Capable_Type(TruthValue):
    """Custom type cnLesV2ExtnV2Capable based on TruthValue"""


_CnLesV2ExtnV2Capable_Object = MibTableColumn
cnLesV2ExtnV2Capable = _CnLesV2ExtnV2Capable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 7, 1, 1, 1),
    _CnLesV2ExtnV2Capable_Type()
)
cnLesV2ExtnV2Capable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLesV2ExtnV2Capable.setStatus("mandatory")


class _CnLesV2ExtnElanID_Type(Integer32):
    """Custom type cnLesV2ExtnElanID based on Integer32"""
    defaultValue = 0


_CnLesV2ExtnElanID_Object = MibTableColumn
cnLesV2ExtnElanID = _CnLesV2ExtnElanID_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 7, 1, 1, 2),
    _CnLesV2ExtnElanID_Type()
)
cnLesV2ExtnElanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLesV2ExtnElanID.setStatus("mandatory")
_CnLesV2ExtnMaxFrameSize_Type = CnLesLecDataFrameSize
_CnLesV2ExtnMaxFrameSize_Object = MibTableColumn
cnLesV2ExtnMaxFrameSize = _CnLesV2ExtnMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 7, 1, 1, 3),
    _CnLesV2ExtnMaxFrameSize_Type()
)
cnLesV2ExtnMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLesV2ExtnMaxFrameSize.setStatus("mandatory")
_CnLecsV2ExtnGroup_ObjectIdentity = ObjectIdentity
cnLecsV2ExtnGroup = _CnLecsV2ExtnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 8)
)
_CnLecsV2ExtnTable_Object = MibTable
cnLecsV2ExtnTable = _CnLecsV2ExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 8, 1)
)
if mibBuilder.loadTexts:
    cnLecsV2ExtnTable.setStatus("mandatory")
_CnLecsV2ExtnEntry_Object = MibTableRow
cnLecsV2ExtnEntry = _CnLecsV2ExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 8, 1, 1)
)
cnLecsV2ExtnEntry.setIndexNames(
    (0, "LAN-EMULATION-ELAN-MIB", "lecsConfIndex"),
)
if mibBuilder.loadTexts:
    cnLecsV2ExtnEntry.setStatus("mandatory")
_CnLecsV2ExtnWellKnownAtmAddress_Type = AtmLaneAddress
_CnLecsV2ExtnWellKnownAtmAddress_Object = MibTableColumn
cnLecsV2ExtnWellKnownAtmAddress = _CnLecsV2ExtnWellKnownAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 8, 1, 1, 1),
    _CnLecsV2ExtnWellKnownAtmAddress_Type()
)
cnLecsV2ExtnWellKnownAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnLecsV2ExtnWellKnownAtmAddress.setStatus("mandatory")
_CnElanV2ExtnGroup_ObjectIdentity = ObjectIdentity
cnElanV2ExtnGroup = _CnElanV2ExtnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 9)
)
_CnElanV2ExtnTable_Object = MibTable
cnElanV2ExtnTable = _CnElanV2ExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 9, 1)
)
if mibBuilder.loadTexts:
    cnElanV2ExtnTable.setStatus("mandatory")
_CnElanV2ExtnEntry_Object = MibTableRow
cnElanV2ExtnEntry = _CnElanV2ExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 9, 1, 1)
)
cnElanV2ExtnEntry.setIndexNames(
    (0, "LAN-EMULATION-ELAN-MIB", "elanConfIndex"),
)
if mibBuilder.loadTexts:
    cnElanV2ExtnEntry.setStatus("mandatory")


class _CnElanV2ExtnV2Capable_Type(TruthValue):
    """Custom type cnElanV2ExtnV2Capable based on TruthValue"""


_CnElanV2ExtnV2Capable_Object = MibTableColumn
cnElanV2ExtnV2Capable = _CnElanV2ExtnV2Capable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 9, 1, 1, 1),
    _CnElanV2ExtnV2Capable_Type()
)
cnElanV2ExtnV2Capable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnElanV2ExtnV2Capable.setStatus("mandatory")


class _CnElanV2ExtnElanID_Type(Integer32):
    """Custom type cnElanV2ExtnElanID based on Integer32"""
    defaultValue = 0


_CnElanV2ExtnElanID_Object = MibTableColumn
cnElanV2ExtnElanID = _CnElanV2ExtnElanID_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 9, 1, 1, 2),
    _CnElanV2ExtnElanID_Type()
)
cnElanV2ExtnElanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnElanV2ExtnElanID.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CENTILLION-LANE-V2-EXT-MIB",
    **{"CnLesLecDataFrameSize": CnLesLecDataFrameSize,
       "cnLesV2ExtnGroup": cnLesV2ExtnGroup,
       "cnLesV2ExtnTable": cnLesV2ExtnTable,
       "cnLesV2ExtnEntry": cnLesV2ExtnEntry,
       "cnLesV2ExtnV2Capable": cnLesV2ExtnV2Capable,
       "cnLesV2ExtnElanID": cnLesV2ExtnElanID,
       "cnLesV2ExtnMaxFrameSize": cnLesV2ExtnMaxFrameSize,
       "cnLecsV2ExtnGroup": cnLecsV2ExtnGroup,
       "cnLecsV2ExtnTable": cnLecsV2ExtnTable,
       "cnLecsV2ExtnEntry": cnLecsV2ExtnEntry,
       "cnLecsV2ExtnWellKnownAtmAddress": cnLecsV2ExtnWellKnownAtmAddress,
       "cnElanV2ExtnGroup": cnElanV2ExtnGroup,
       "cnElanV2ExtnTable": cnElanV2ExtnTable,
       "cnElanV2ExtnEntry": cnElanV2ExtnEntry,
       "cnElanV2ExtnV2Capable": cnElanV2ExtnV2Capable,
       "cnElanV2ExtnElanID": cnElanV2ExtnElanID}
)
