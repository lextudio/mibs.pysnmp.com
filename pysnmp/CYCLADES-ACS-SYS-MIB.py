# SNMP MIB module (CYCLADES-ACS-SYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CYCLADES-ACS-SYS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:26 2024
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

(cyACSMgmt,) = mibBuilder.importSymbols(
    "CYCLADES-ACS-MIB",
    "cyACSMgmt")

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

cyACSSys = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2925, 4, 1)
)
cyACSSys.setRevisions(
        ("2005-08-29 00:00",
         "2005-08-29 00:00",
         "2003-06-30 00:00",
         "2002-10-10 00:00",
         "2002-09-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CyACSpname_Type = DisplayString
_CyACSpname_Object = MibScalar
cyACSpname = _CyACSpname_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 1, 1),
    _CyACSpname_Type()
)
cyACSpname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyACSpname.setStatus("current")
_CyACSversion_Type = DisplayString
_CyACSversion_Object = MibScalar
cyACSversion = _CyACSversion_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 1, 2),
    _CyACSversion_Type()
)
cyACSversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyACSversion.setStatus("current")
_CyACSPower_ObjectIdentity = ObjectIdentity
cyACSPower = _CyACSPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2925, 4, 1, 3)
)
if mibBuilder.loadTexts:
    cyACSPower.setStatus("current")
_CyACSPwNum_Type = Integer32
_CyACSPwNum_Object = MibScalar
cyACSPwNum = _CyACSPwNum_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 1, 3, 1),
    _CyACSPwNum_Type()
)
cyACSPwNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyACSPwNum.setStatus("current")


class _CyACSPw1_Type(Integer32):
    """Custom type cyACSPw1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noinstalled", 0),
          ("powerOFF", 2),
          ("powerON", 1))
    )


_CyACSPw1_Type.__name__ = "Integer32"
_CyACSPw1_Object = MibScalar
cyACSPw1 = _CyACSPw1_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 1, 3, 2),
    _CyACSPw1_Type()
)
cyACSPw1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyACSPw1.setStatus("current")


class _CyACSPw2_Type(Integer32):
    """Custom type cyACSPw2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noinstalled", 0),
          ("powerOFF", 2),
          ("powerON", 1))
    )


_CyACSPw2_Type.__name__ = "Integer32"
_CyACSPw2_Object = MibScalar
cyACSPw2 = _CyACSPw2_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 1, 3, 3),
    _CyACSPw2_Type()
)
cyACSPw2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyACSPw2.setStatus("current")
_CyACSPcmcia_ObjectIdentity = ObjectIdentity
cyACSPcmcia = _CyACSPcmcia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2925, 4, 1, 4)
)
if mibBuilder.loadTexts:
    cyACSPcmcia.setStatus("current")
_CyACSNPcmcia_Type = Integer32
_CyACSNPcmcia_Object = MibScalar
cyACSNPcmcia = _CyACSNPcmcia_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 1, 4, 1),
    _CyACSNPcmcia_Type()
)
cyACSNPcmcia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyACSNPcmcia.setStatus("current")
_CyCardIdentTable_Object = MibTable
cyCardIdentTable = _CyCardIdentTable_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cyCardIdentTable.setStatus("current")
_CyCardIdentEntry_Object = MibTableRow
cyCardIdentEntry = _CyCardIdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 1, 4, 2, 1)
)
cyCardIdentEntry.setIndexNames(
    (0, "CYCLADES-ACS-SYS-MIB", "cyCardIdentIndex"),
)
if mibBuilder.loadTexts:
    cyCardIdentEntry.setStatus("current")


class _CyCardIdentIndex_Type(Integer32):
    """Custom type cyCardIdentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_CyCardIdentIndex_Type.__name__ = "Integer32"
_CyCardIdentIndex_Object = MibTableColumn
cyCardIdentIndex = _CyCardIdentIndex_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 1, 4, 2, 1, 1),
    _CyCardIdentIndex_Type()
)
cyCardIdentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyCardIdentIndex.setStatus("current")
_CyCardIdentProd_Type = DisplayString
_CyCardIdentProd_Object = MibTableColumn
cyCardIdentProd = _CyCardIdentProd_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 1, 4, 2, 1, 2),
    _CyCardIdentProd_Type()
)
cyCardIdentProd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyCardIdentProd.setStatus("current")
_CyCardIdentMan_Type = DisplayString
_CyCardIdentMan_Object = MibTableColumn
cyCardIdentMan = _CyCardIdentMan_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 1, 4, 2, 1, 3),
    _CyCardIdentMan_Type()
)
cyCardIdentMan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyCardIdentMan.setStatus("current")
_CyCardIdentFunc_Type = DisplayString
_CyCardIdentFunc_Object = MibTableColumn
cyCardIdentFunc = _CyCardIdentFunc_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 1, 4, 2, 1, 4),
    _CyCardIdentFunc_Type()
)
cyCardIdentFunc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyCardIdentFunc.setStatus("current")
_CyCardIdentPCI_Type = DisplayString
_CyCardIdentPCI_Object = MibTableColumn
cyCardIdentPCI = _CyCardIdentPCI_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 1, 4, 2, 1, 5),
    _CyCardIdentPCI_Type()
)
cyCardIdentPCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyCardIdentPCI.setStatus("current")
_CyCardConfTable_Object = MibTable
cyCardConfTable = _CyCardConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 1, 4, 3)
)
if mibBuilder.loadTexts:
    cyCardConfTable.setStatus("current")
_CyCardConfEntry_Object = MibTableRow
cyCardConfEntry = _CyCardConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 1, 4, 3, 1)
)
cyCardConfEntry.setIndexNames(
    (0, "CYCLADES-ACS-SYS-MIB", "cyCardConfIndex"),
)
if mibBuilder.loadTexts:
    cyCardConfEntry.setStatus("current")


class _CyCardConfIndex_Type(Integer32):
    """Custom type cyCardConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_CyCardConfIndex_Type.__name__ = "Integer32"
_CyCardConfIndex_Object = MibTableColumn
cyCardConfIndex = _CyCardConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 1, 4, 3, 1, 1),
    _CyCardConfIndex_Type()
)
cyCardConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyCardConfIndex.setStatus("current")
_CyCardConfPower_Type = DisplayString
_CyCardConfPower_Object = MibTableColumn
cyCardConfPower = _CyCardConfPower_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 1, 4, 3, 1, 2),
    _CyCardConfPower_Type()
)
cyCardConfPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyCardConfPower.setStatus("current")
_CyCardConfType_Type = DisplayString
_CyCardConfType_Object = MibTableColumn
cyCardConfType = _CyCardConfType_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 1, 4, 3, 1, 3),
    _CyCardConfType_Type()
)
cyCardConfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyCardConfType.setStatus("current")
_CyCardConfInter_Type = DisplayString
_CyCardConfInter_Object = MibTableColumn
cyCardConfInter = _CyCardConfInter_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 1, 4, 3, 1, 4),
    _CyCardConfInter_Type()
)
cyCardConfInter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyCardConfInter.setStatus("current")
_CyCardConfFunc_Type = DisplayString
_CyCardConfFunc_Object = MibTableColumn
cyCardConfFunc = _CyCardConfFunc_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 1, 4, 3, 1, 5),
    _CyCardConfFunc_Type()
)
cyCardConfFunc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyCardConfFunc.setStatus("current")
_CyCardConfCardv_Type = DisplayString
_CyCardConfCardv_Object = MibTableColumn
cyCardConfCardv = _CyCardConfCardv_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 1, 4, 3, 1, 6),
    _CyCardConfCardv_Type()
)
cyCardConfCardv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyCardConfCardv.setStatus("current")
_CyCardConfPort1_Type = DisplayString
_CyCardConfPort1_Object = MibTableColumn
cyCardConfPort1 = _CyCardConfPort1_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 1, 4, 3, 1, 7),
    _CyCardConfPort1_Type()
)
cyCardConfPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyCardConfPort1.setStatus("current")
_CyCardConfPort2_Type = DisplayString
_CyCardConfPort2_Object = MibTableColumn
cyCardConfPort2 = _CyCardConfPort2_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 1, 4, 3, 1, 8),
    _CyCardConfPort2_Type()
)
cyCardConfPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyCardConfPort2.setStatus("current")
_CyCardStatusTable_Object = MibTable
cyCardStatusTable = _CyCardStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 1, 4, 4)
)
if mibBuilder.loadTexts:
    cyCardStatusTable.setStatus("current")
_CyCardStatusEntry_Object = MibTableRow
cyCardStatusEntry = _CyCardStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 1, 4, 4, 1)
)
cyCardStatusEntry.setIndexNames(
    (0, "CYCLADES-ACS-SYS-MIB", "cyCardStatusIndex"),
)
if mibBuilder.loadTexts:
    cyCardStatusEntry.setStatus("current")


class _CyCardStatusIndex_Type(Integer32):
    """Custom type cyCardStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_CyCardStatusIndex_Type.__name__ = "Integer32"
_CyCardStatusIndex_Object = MibTableColumn
cyCardStatusIndex = _CyCardStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 1, 4, 4, 1, 1),
    _CyCardStatusIndex_Type()
)
cyCardStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyCardStatusIndex.setStatus("current")
_CyCardStatusCard_Type = DisplayString
_CyCardStatusCard_Object = MibTableColumn
cyCardStatusCard = _CyCardStatusCard_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 1, 4, 4, 1, 2),
    _CyCardStatusCard_Type()
)
cyCardStatusCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyCardStatusCard.setStatus("current")
_CyCardStatusFunc_Type = DisplayString
_CyCardStatusFunc_Object = MibTableColumn
cyCardStatusFunc = _CyCardStatusFunc_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 1, 4, 4, 1, 3),
    _CyCardStatusFunc_Type()
)
cyCardStatusFunc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyCardStatusFunc.setStatus("current")
_CyACSFlashSize_Type = Integer32
_CyACSFlashSize_Object = MibScalar
cyACSFlashSize = _CyACSFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 1, 5),
    _CyACSFlashSize_Type()
)
cyACSFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyACSFlashSize.setStatus("current")
_CyACSRAMSize_Type = Integer32
_CyACSRAMSize_Object = MibScalar
cyACSRAMSize = _CyACSRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 1, 6),
    _CyACSRAMSize_Type()
)
cyACSRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyACSRAMSize.setStatus("current")
_CyACSCPUfreq_Type = Integer32
_CyACSCPUfreq_Object = MibScalar
cyACSCPUfreq = _CyACSCPUfreq_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 1, 7),
    _CyACSCPUfreq_Type()
)
cyACSCPUfreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyACSCPUfreq.setStatus("current")
_CyACSDevId_Type = DisplayString
_CyACSDevId_Object = MibScalar
cyACSDevId = _CyACSDevId_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 1, 8),
    _CyACSDevId_Type()
)
cyACSDevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyACSDevId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CYCLADES-ACS-SYS-MIB",
    **{"cyACSSys": cyACSSys,
       "cyACSpname": cyACSpname,
       "cyACSversion": cyACSversion,
       "cyACSPower": cyACSPower,
       "cyACSPwNum": cyACSPwNum,
       "cyACSPw1": cyACSPw1,
       "cyACSPw2": cyACSPw2,
       "cyACSPcmcia": cyACSPcmcia,
       "cyACSNPcmcia": cyACSNPcmcia,
       "cyCardIdentTable": cyCardIdentTable,
       "cyCardIdentEntry": cyCardIdentEntry,
       "cyCardIdentIndex": cyCardIdentIndex,
       "cyCardIdentProd": cyCardIdentProd,
       "cyCardIdentMan": cyCardIdentMan,
       "cyCardIdentFunc": cyCardIdentFunc,
       "cyCardIdentPCI": cyCardIdentPCI,
       "cyCardConfTable": cyCardConfTable,
       "cyCardConfEntry": cyCardConfEntry,
       "cyCardConfIndex": cyCardConfIndex,
       "cyCardConfPower": cyCardConfPower,
       "cyCardConfType": cyCardConfType,
       "cyCardConfInter": cyCardConfInter,
       "cyCardConfFunc": cyCardConfFunc,
       "cyCardConfCardv": cyCardConfCardv,
       "cyCardConfPort1": cyCardConfPort1,
       "cyCardConfPort2": cyCardConfPort2,
       "cyCardStatusTable": cyCardStatusTable,
       "cyCardStatusEntry": cyCardStatusEntry,
       "cyCardStatusIndex": cyCardStatusIndex,
       "cyCardStatusCard": cyCardStatusCard,
       "cyCardStatusFunc": cyCardStatusFunc,
       "cyACSFlashSize": cyACSFlashSize,
       "cyACSRAMSize": cyACSRAMSize,
       "cyACSCPUfreq": cyACSCPUfreq,
       "cyACSDevId": cyACSDevId}
)
