# SNMP MIB module (MSCR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MSCR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:53 2024
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
 NotificationType,
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
    "NotificationType",
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


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nbase_ObjectIdentity = ObjectIdentity
nbase = _Nbase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629)
)
_NbSwitchG1_ObjectIdentity = ObjectIdentity
nbSwitchG1 = _NbSwitchG1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1)
)
_NbSwitchG1Il_ObjectIdentity = ObjectIdentity
nbSwitchG1Il = _NbSwitchG1Il_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50)
)
_NbMacScr_ObjectIdentity = ObjectIdentity
nbMacScr = _NbMacScr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1)
)
_NbMacScrRun_ObjectIdentity = ObjectIdentity
nbMacScrRun = _NbMacScrRun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1)
)


class _NbMacScrRunSecurityLevel_Type(Integer32):
    """Custom type nbMacScrRunSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("perPort", 2),
          ("perSwitch", 3))
    )


_NbMacScrRunSecurityLevel_Type.__name__ = "Integer32"
_NbMacScrRunSecurityLevel_Object = MibScalar
nbMacScrRunSecurityLevel = _NbMacScrRunSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1, 1),
    _NbMacScrRunSecurityLevel_Type()
)
nbMacScrRunSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbMacScrRunSecurityLevel.setStatus("mandatory")


class _NbMacScrRunSaveMS_Type(Integer32):
    """Custom type nbMacScrRunSaveMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("save", 2))
    )


_NbMacScrRunSaveMS_Type.__name__ = "Integer32"
_NbMacScrRunSaveMS_Object = MibScalar
nbMacScrRunSaveMS = _NbMacScrRunSaveMS_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1, 2),
    _NbMacScrRunSaveMS_Type()
)
nbMacScrRunSaveMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbMacScrRunSaveMS.setStatus("mandatory")


class _NbMacScrRunClearMS_Type(Integer32):
    """Custom type nbMacScrRunClearMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("running", 1))
    )


_NbMacScrRunClearMS_Type.__name__ = "Integer32"
_NbMacScrRunClearMS_Object = MibScalar
nbMacScrRunClearMS = _NbMacScrRunClearMS_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1, 3),
    _NbMacScrRunClearMS_Type()
)
nbMacScrRunClearMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbMacScrRunClearMS.setStatus("mandatory")
_NbMacScrRunPortsTable_Object = MibTable
nbMacScrRunPortsTable = _NbMacScrRunPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1, 4)
)
if mibBuilder.loadTexts:
    nbMacScrRunPortsTable.setStatus("mandatory")
_NbMacScrRunPortsEntry_Object = MibTableRow
nbMacScrRunPortsEntry = _NbMacScrRunPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1, 4, 1)
)
nbMacScrRunPortsEntry.setIndexNames(
    (0, "MSCR-MIB", "nbMacScrRunPort"),
)
if mibBuilder.loadTexts:
    nbMacScrRunPortsEntry.setStatus("mandatory")
_NbMacScrRunPort_Type = Integer32
_NbMacScrRunPort_Object = MibTableColumn
nbMacScrRunPort = _NbMacScrRunPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1, 4, 1, 1),
    _NbMacScrRunPort_Type()
)
nbMacScrRunPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbMacScrRunPort.setStatus("mandatory")


class _NbMacScrRunPortScrStatus_Type(Integer32):
    """Custom type nbMacScrRunPortScrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NbMacScrRunPortScrStatus_Type.__name__ = "Integer32"
_NbMacScrRunPortScrStatus_Object = MibTableColumn
nbMacScrRunPortScrStatus = _NbMacScrRunPortScrStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1, 4, 1, 2),
    _NbMacScrRunPortScrStatus_Type()
)
nbMacScrRunPortScrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbMacScrRunPortScrStatus.setStatus("mandatory")


class _NbMacScrRunPortSaveMS_Type(Integer32):
    """Custom type nbMacScrRunPortSaveMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("save", 2))
    )


_NbMacScrRunPortSaveMS_Type.__name__ = "Integer32"
_NbMacScrRunPortSaveMS_Object = MibTableColumn
nbMacScrRunPortSaveMS = _NbMacScrRunPortSaveMS_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1, 4, 1, 3),
    _NbMacScrRunPortSaveMS_Type()
)
nbMacScrRunPortSaveMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbMacScrRunPortSaveMS.setStatus("mandatory")


class _NbMacScrRunPortClearMS_Type(Integer32):
    """Custom type nbMacScrRunPortClearMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("running", 1))
    )


_NbMacScrRunPortClearMS_Type.__name__ = "Integer32"
_NbMacScrRunPortClearMS_Object = MibTableColumn
nbMacScrRunPortClearMS = _NbMacScrRunPortClearMS_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1, 4, 1, 4),
    _NbMacScrRunPortClearMS_Type()
)
nbMacScrRunPortClearMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbMacScrRunPortClearMS.setStatus("mandatory")
_NbMacScrRunPortLockingMAC_Type = MacAddress
_NbMacScrRunPortLockingMAC_Object = MibTableColumn
nbMacScrRunPortLockingMAC = _NbMacScrRunPortLockingMAC_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1, 4, 1, 5),
    _NbMacScrRunPortLockingMAC_Type()
)
nbMacScrRunPortLockingMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbMacScrRunPortLockingMAC.setStatus("mandatory")
_NbMacScrRunMsTable_Object = MibTable
nbMacScrRunMsTable = _NbMacScrRunMsTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1, 5)
)
if mibBuilder.loadTexts:
    nbMacScrRunMsTable.setStatus("mandatory")
_NbMacScrRunMsEntry_Object = MibTableRow
nbMacScrRunMsEntry = _NbMacScrRunMsEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1, 5, 1)
)
nbMacScrRunMsEntry.setIndexNames(
    (0, "MSCR-MIB", "nbMacScrRunMsIndex"),
)
if mibBuilder.loadTexts:
    nbMacScrRunMsEntry.setStatus("mandatory")
_NbMacScrRunMsIndex_Type = Integer32
_NbMacScrRunMsIndex_Object = MibTableColumn
nbMacScrRunMsIndex = _NbMacScrRunMsIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1, 5, 1, 1),
    _NbMacScrRunMsIndex_Type()
)
nbMacScrRunMsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbMacScrRunMsIndex.setStatus("mandatory")
_NbMacScrRunMsAddress_Type = MacAddress
_NbMacScrRunMsAddress_Object = MibTableColumn
nbMacScrRunMsAddress = _NbMacScrRunMsAddress_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1, 5, 1, 2),
    _NbMacScrRunMsAddress_Type()
)
nbMacScrRunMsAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbMacScrRunMsAddress.setStatus("mandatory")


class _NbMacScrRunMsPort_Type(Integer32):
    """Custom type nbMacScrRunMsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NbMacScrRunMsPort_Type.__name__ = "Integer32"
_NbMacScrRunMsPort_Object = MibTableColumn
nbMacScrRunMsPort = _NbMacScrRunMsPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1, 5, 1, 3),
    _NbMacScrRunMsPort_Type()
)
nbMacScrRunMsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbMacScrRunMsPort.setStatus("mandatory")


class _NbMacScrRunMsState_Type(Integer32):
    """Custom type nbMacScrRunMsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_NbMacScrRunMsState_Type.__name__ = "Integer32"
_NbMacScrRunMsState_Object = MibTableColumn
nbMacScrRunMsState = _NbMacScrRunMsState_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1, 5, 1, 4),
    _NbMacScrRunMsState_Type()
)
nbMacScrRunMsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbMacScrRunMsState.setStatus("mandatory")
_NbMacScrRunMsMaxNum_Type = Integer32
_NbMacScrRunMsMaxNum_Object = MibScalar
nbMacScrRunMsMaxNum = _NbMacScrRunMsMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1, 6),
    _NbMacScrRunMsMaxNum_Type()
)
nbMacScrRunMsMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbMacScrRunMsMaxNum.setStatus("mandatory")
_NbMacScrRunTableSize_Type = Integer32
_NbMacScrRunTableSize_Object = MibScalar
nbMacScrRunTableSize = _NbMacScrRunTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1, 7),
    _NbMacScrRunTableSize_Type()
)
nbMacScrRunTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbMacScrRunTableSize.setStatus("mandatory")
_NbMacScrPerm_ObjectIdentity = ObjectIdentity
nbMacScrPerm = _NbMacScrPerm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2)
)


class _NbMacScrPermSecurityLevel_Type(Integer32):
    """Custom type nbMacScrPermSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("perPort", 2),
          ("perSwitch", 3))
    )


_NbMacScrPermSecurityLevel_Type.__name__ = "Integer32"
_NbMacScrPermSecurityLevel_Object = MibScalar
nbMacScrPermSecurityLevel = _NbMacScrPermSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2, 1),
    _NbMacScrPermSecurityLevel_Type()
)
nbMacScrPermSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbMacScrPermSecurityLevel.setStatus("mandatory")


class _NbMacScrPermSaveMS_Type(Integer32):
    """Custom type nbMacScrPermSaveMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("save", 2))
    )


_NbMacScrPermSaveMS_Type.__name__ = "Integer32"
_NbMacScrPermSaveMS_Object = MibScalar
nbMacScrPermSaveMS = _NbMacScrPermSaveMS_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2, 2),
    _NbMacScrPermSaveMS_Type()
)
nbMacScrPermSaveMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbMacScrPermSaveMS.setStatus("mandatory")


class _NbMacScrPermClearMS_Type(Integer32):
    """Custom type nbMacScrPermClearMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("running", 1))
    )


_NbMacScrPermClearMS_Type.__name__ = "Integer32"
_NbMacScrPermClearMS_Object = MibScalar
nbMacScrPermClearMS = _NbMacScrPermClearMS_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2, 3),
    _NbMacScrPermClearMS_Type()
)
nbMacScrPermClearMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbMacScrPermClearMS.setStatus("mandatory")
_NbMacScrPermPortsTable_Object = MibTable
nbMacScrPermPortsTable = _NbMacScrPermPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2, 4)
)
if mibBuilder.loadTexts:
    nbMacScrPermPortsTable.setStatus("mandatory")
_NbMacScrPermPortsEntry_Object = MibTableRow
nbMacScrPermPortsEntry = _NbMacScrPermPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2, 4, 1)
)
nbMacScrPermPortsEntry.setIndexNames(
    (0, "MSCR-MIB", "nbMacScrPermPort"),
)
if mibBuilder.loadTexts:
    nbMacScrPermPortsEntry.setStatus("mandatory")
_NbMacScrPermPort_Type = Integer32
_NbMacScrPermPort_Object = MibTableColumn
nbMacScrPermPort = _NbMacScrPermPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2, 4, 1, 1),
    _NbMacScrPermPort_Type()
)
nbMacScrPermPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbMacScrPermPort.setStatus("mandatory")


class _NbMacScrPermPortScrStatus_Type(Integer32):
    """Custom type nbMacScrPermPortScrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NbMacScrPermPortScrStatus_Type.__name__ = "Integer32"
_NbMacScrPermPortScrStatus_Object = MibTableColumn
nbMacScrPermPortScrStatus = _NbMacScrPermPortScrStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2, 4, 1, 2),
    _NbMacScrPermPortScrStatus_Type()
)
nbMacScrPermPortScrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbMacScrPermPortScrStatus.setStatus("mandatory")


class _NbMacScrPermPortSaveMS_Type(Integer32):
    """Custom type nbMacScrPermPortSaveMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("save", 2))
    )


_NbMacScrPermPortSaveMS_Type.__name__ = "Integer32"
_NbMacScrPermPortSaveMS_Object = MibTableColumn
nbMacScrPermPortSaveMS = _NbMacScrPermPortSaveMS_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2, 4, 1, 3),
    _NbMacScrPermPortSaveMS_Type()
)
nbMacScrPermPortSaveMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbMacScrPermPortSaveMS.setStatus("mandatory")


class _NbMacScrPermPortClearMS_Type(Integer32):
    """Custom type nbMacScrPermPortClearMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("running", 1))
    )


_NbMacScrPermPortClearMS_Type.__name__ = "Integer32"
_NbMacScrPermPortClearMS_Object = MibTableColumn
nbMacScrPermPortClearMS = _NbMacScrPermPortClearMS_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2, 4, 1, 4),
    _NbMacScrPermPortClearMS_Type()
)
nbMacScrPermPortClearMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbMacScrPermPortClearMS.setStatus("mandatory")
_NbMacScrPermMsTable_Object = MibTable
nbMacScrPermMsTable = _NbMacScrPermMsTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2, 5)
)
if mibBuilder.loadTexts:
    nbMacScrPermMsTable.setStatus("mandatory")
_NbMacScrPermMsEntry_Object = MibTableRow
nbMacScrPermMsEntry = _NbMacScrPermMsEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2, 5, 1)
)
nbMacScrPermMsEntry.setIndexNames(
    (0, "MSCR-MIB", "nbMacScrPermMsIndex"),
)
if mibBuilder.loadTexts:
    nbMacScrPermMsEntry.setStatus("mandatory")
_NbMacScrPermMsIndex_Type = Integer32
_NbMacScrPermMsIndex_Object = MibTableColumn
nbMacScrPermMsIndex = _NbMacScrPermMsIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2, 5, 1, 1),
    _NbMacScrPermMsIndex_Type()
)
nbMacScrPermMsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbMacScrPermMsIndex.setStatus("mandatory")
_NbMacScrPermMsAddress_Type = MacAddress
_NbMacScrPermMsAddress_Object = MibTableColumn
nbMacScrPermMsAddress = _NbMacScrPermMsAddress_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2, 5, 1, 2),
    _NbMacScrPermMsAddress_Type()
)
nbMacScrPermMsAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbMacScrPermMsAddress.setStatus("mandatory")


class _NbMacScrPermMsPort_Type(Integer32):
    """Custom type nbMacScrPermMsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NbMacScrPermMsPort_Type.__name__ = "Integer32"
_NbMacScrPermMsPort_Object = MibTableColumn
nbMacScrPermMsPort = _NbMacScrPermMsPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2, 5, 1, 3),
    _NbMacScrPermMsPort_Type()
)
nbMacScrPermMsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbMacScrPermMsPort.setStatus("mandatory")


class _NbMacScrPermMsState_Type(Integer32):
    """Custom type nbMacScrPermMsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_NbMacScrPermMsState_Type.__name__ = "Integer32"
_NbMacScrPermMsState_Object = MibTableColumn
nbMacScrPermMsState = _NbMacScrPermMsState_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2, 5, 1, 4),
    _NbMacScrPermMsState_Type()
)
nbMacScrPermMsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbMacScrPermMsState.setStatus("mandatory")
_NbMacScrPermMsMaxNum_Type = Integer32
_NbMacScrPermMsMaxNum_Object = MibScalar
nbMacScrPermMsMaxNum = _NbMacScrPermMsMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2, 6),
    _NbMacScrPermMsMaxNum_Type()
)
nbMacScrPermMsMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbMacScrPermMsMaxNum.setStatus("mandatory")
_NbMacScrPermTableSize_Type = Integer32
_NbMacScrPermTableSize_Object = MibScalar
nbMacScrPermTableSize = _NbMacScrPermTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2, 7),
    _NbMacScrPermTableSize_Type()
)
nbMacScrPermTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbMacScrPermTableSize.setStatus("mandatory")


class _NbMacScrPermLoadMS_Type(Integer32):
    """Custom type nbMacScrPermLoadMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("load", 2),
          ("manual", 1))
    )


_NbMacScrPermLoadMS_Type.__name__ = "Integer32"
_NbMacScrPermLoadMS_Object = MibScalar
nbMacScrPermLoadMS = _NbMacScrPermLoadMS_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2, 8),
    _NbMacScrPermLoadMS_Type()
)
nbMacScrPermLoadMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbMacScrPermLoadMS.setStatus("mandatory")

# Managed Objects groups


# Notification objects

unresolvedMAC = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 0, 1)
)
unresolvedMAC.setObjects(
      *(("MSCR-MIB", "nbMacScrRunPort"),
        ("MSCR-MIB", "nbMacScrRunPortLockingMAC"))
)
if mibBuilder.loadTexts:
    unresolvedMAC.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MSCR-MIB",
    **{"MacAddress": MacAddress,
       "nbase": nbase,
       "nbSwitchG1": nbSwitchG1,
       "nbSwitchG1Il": nbSwitchG1Il,
       "nbMacScr": nbMacScr,
       "unresolvedMAC": unresolvedMAC,
       "nbMacScrRun": nbMacScrRun,
       "nbMacScrRunSecurityLevel": nbMacScrRunSecurityLevel,
       "nbMacScrRunSaveMS": nbMacScrRunSaveMS,
       "nbMacScrRunClearMS": nbMacScrRunClearMS,
       "nbMacScrRunPortsTable": nbMacScrRunPortsTable,
       "nbMacScrRunPortsEntry": nbMacScrRunPortsEntry,
       "nbMacScrRunPort": nbMacScrRunPort,
       "nbMacScrRunPortScrStatus": nbMacScrRunPortScrStatus,
       "nbMacScrRunPortSaveMS": nbMacScrRunPortSaveMS,
       "nbMacScrRunPortClearMS": nbMacScrRunPortClearMS,
       "nbMacScrRunPortLockingMAC": nbMacScrRunPortLockingMAC,
       "nbMacScrRunMsTable": nbMacScrRunMsTable,
       "nbMacScrRunMsEntry": nbMacScrRunMsEntry,
       "nbMacScrRunMsIndex": nbMacScrRunMsIndex,
       "nbMacScrRunMsAddress": nbMacScrRunMsAddress,
       "nbMacScrRunMsPort": nbMacScrRunMsPort,
       "nbMacScrRunMsState": nbMacScrRunMsState,
       "nbMacScrRunMsMaxNum": nbMacScrRunMsMaxNum,
       "nbMacScrRunTableSize": nbMacScrRunTableSize,
       "nbMacScrPerm": nbMacScrPerm,
       "nbMacScrPermSecurityLevel": nbMacScrPermSecurityLevel,
       "nbMacScrPermSaveMS": nbMacScrPermSaveMS,
       "nbMacScrPermClearMS": nbMacScrPermClearMS,
       "nbMacScrPermPortsTable": nbMacScrPermPortsTable,
       "nbMacScrPermPortsEntry": nbMacScrPermPortsEntry,
       "nbMacScrPermPort": nbMacScrPermPort,
       "nbMacScrPermPortScrStatus": nbMacScrPermPortScrStatus,
       "nbMacScrPermPortSaveMS": nbMacScrPermPortSaveMS,
       "nbMacScrPermPortClearMS": nbMacScrPermPortClearMS,
       "nbMacScrPermMsTable": nbMacScrPermMsTable,
       "nbMacScrPermMsEntry": nbMacScrPermMsEntry,
       "nbMacScrPermMsIndex": nbMacScrPermMsIndex,
       "nbMacScrPermMsAddress": nbMacScrPermMsAddress,
       "nbMacScrPermMsPort": nbMacScrPermMsPort,
       "nbMacScrPermMsState": nbMacScrPermMsState,
       "nbMacScrPermMsMaxNum": nbMacScrPermMsMaxNum,
       "nbMacScrPermTableSize": nbMacScrPermTableSize,
       "nbMacScrPermLoadMS": nbMacScrPermLoadMS}
)
