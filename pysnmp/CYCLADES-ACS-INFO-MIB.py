# SNMP MIB module (CYCLADES-ACS-INFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CYCLADES-ACS-INFO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:24 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

cyACSInfo = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2925, 4, 3)
)
cyACSInfo.setRevisions(
        ("2005-08-29 00:00",
         "2002-09-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CyInfoSerialTable_Object = MibTable
cyInfoSerialTable = _CyInfoSerialTable_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 3, 1)
)
if mibBuilder.loadTexts:
    cyInfoSerialTable.setStatus("current")
_CyisPortEntry_Object = MibTableRow
cyisPortEntry = _CyisPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 3, 1, 1)
)
cyisPortEntry.setIndexNames(
    (0, "CYCLADES-ACS-INFO-MIB", "cyISPortNumber"),
)
if mibBuilder.loadTexts:
    cyisPortEntry.setStatus("current")
_CyISPortNumber_Type = InterfaceIndex
_CyISPortNumber_Object = MibTableColumn
cyISPortNumber = _CyISPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 3, 1, 1, 1),
    _CyISPortNumber_Type()
)
cyISPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyISPortNumber.setStatus("current")
_CyISPortTty_Type = DisplayString
_CyISPortTty_Object = MibTableColumn
cyISPortTty = _CyISPortTty_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 3, 1, 1, 2),
    _CyISPortTty_Type()
)
cyISPortTty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyISPortTty.setStatus("current")
_CyISPortName_Type = DisplayString
_CyISPortName_Object = MibTableColumn
cyISPortName = _CyISPortName_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 3, 1, 1, 3),
    _CyISPortName_Type()
)
cyISPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyISPortName.setStatus("current")
_CyISPortSpeed_Type = Integer32
_CyISPortSpeed_Object = MibTableColumn
cyISPortSpeed = _CyISPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 3, 1, 1, 4),
    _CyISPortSpeed_Type()
)
cyISPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyISPortSpeed.setStatus("current")
_CyISPortTxBytes_Type = Counter32
_CyISPortTxBytes_Object = MibTableColumn
cyISPortTxBytes = _CyISPortTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 3, 1, 1, 5),
    _CyISPortTxBytes_Type()
)
cyISPortTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyISPortTxBytes.setStatus("current")
_CyISPortRXBytes_Type = Counter32
_CyISPortRXBytes_Object = MibTableColumn
cyISPortRXBytes = _CyISPortRXBytes_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 3, 1, 1, 6),
    _CyISPortRXBytes_Type()
)
cyISPortRXBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyISPortRXBytes.setStatus("current")
_CyISPortErrFrame_Type = Counter32
_CyISPortErrFrame_Object = MibTableColumn
cyISPortErrFrame = _CyISPortErrFrame_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 3, 1, 1, 7),
    _CyISPortErrFrame_Type()
)
cyISPortErrFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyISPortErrFrame.setStatus("current")
_CyISPortErrParity_Type = Counter32
_CyISPortErrParity_Object = MibTableColumn
cyISPortErrParity = _CyISPortErrParity_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 3, 1, 1, 8),
    _CyISPortErrParity_Type()
)
cyISPortErrParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyISPortErrParity.setStatus("current")
_CyISPortErrBreaks_Type = Counter32
_CyISPortErrBreaks_Object = MibTableColumn
cyISPortErrBreaks = _CyISPortErrBreaks_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 3, 1, 1, 9),
    _CyISPortErrBreaks_Type()
)
cyISPortErrBreaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyISPortErrBreaks.setStatus("current")
_CyISPortErrOverrun_Type = Counter32
_CyISPortErrOverrun_Object = MibTableColumn
cyISPortErrOverrun = _CyISPortErrOverrun_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 3, 1, 1, 10),
    _CyISPortErrOverrun_Type()
)
cyISPortErrOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyISPortErrOverrun.setStatus("current")


class _CyISPortSigDTR_Type(Integer32):
    """Custom type cyISPortSigDTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_CyISPortSigDTR_Type.__name__ = "Integer32"
_CyISPortSigDTR_Object = MibTableColumn
cyISPortSigDTR = _CyISPortSigDTR_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 3, 1, 1, 11),
    _CyISPortSigDTR_Type()
)
cyISPortSigDTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyISPortSigDTR.setStatus("current")


class _CyISPortSigCD_Type(Integer32):
    """Custom type cyISPortSigCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_CyISPortSigCD_Type.__name__ = "Integer32"
_CyISPortSigCD_Object = MibTableColumn
cyISPortSigCD = _CyISPortSigCD_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 3, 1, 1, 12),
    _CyISPortSigCD_Type()
)
cyISPortSigCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyISPortSigCD.setStatus("current")


class _CyISPortSigDSR_Type(Integer32):
    """Custom type cyISPortSigDSR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_CyISPortSigDSR_Type.__name__ = "Integer32"
_CyISPortSigDSR_Object = MibTableColumn
cyISPortSigDSR = _CyISPortSigDSR_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 3, 1, 1, 13),
    _CyISPortSigDSR_Type()
)
cyISPortSigDSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyISPortSigDSR.setStatus("current")


class _CyISPortSigRTS_Type(Integer32):
    """Custom type cyISPortSigRTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_CyISPortSigRTS_Type.__name__ = "Integer32"
_CyISPortSigRTS_Object = MibTableColumn
cyISPortSigRTS = _CyISPortSigRTS_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 3, 1, 1, 14),
    _CyISPortSigRTS_Type()
)
cyISPortSigRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyISPortSigRTS.setStatus("current")


class _CyISPortSigCTS_Type(Integer32):
    """Custom type cyISPortSigCTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_CyISPortSigCTS_Type.__name__ = "Integer32"
_CyISPortSigCTS_Object = MibTableColumn
cyISPortSigCTS = _CyISPortSigCTS_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 3, 1, 1, 15),
    _CyISPortSigCTS_Type()
)
cyISPortSigCTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyISPortSigCTS.setStatus("current")


class _CyISPortSigRI_Type(Integer32):
    """Custom type cyISPortSigRI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_CyISPortSigRI_Type.__name__ = "Integer32"
_CyISPortSigRI_Object = MibTableColumn
cyISPortSigRI = _CyISPortSigRI_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 3, 1, 1, 16),
    _CyISPortSigRI_Type()
)
cyISPortSigRI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyISPortSigRI.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CYCLADES-ACS-INFO-MIB",
    **{"cyACSInfo": cyACSInfo,
       "cyInfoSerialTable": cyInfoSerialTable,
       "cyisPortEntry": cyisPortEntry,
       "cyISPortNumber": cyISPortNumber,
       "cyISPortTty": cyISPortTty,
       "cyISPortName": cyISPortName,
       "cyISPortSpeed": cyISPortSpeed,
       "cyISPortTxBytes": cyISPortTxBytes,
       "cyISPortRXBytes": cyISPortRXBytes,
       "cyISPortErrFrame": cyISPortErrFrame,
       "cyISPortErrParity": cyISPortErrParity,
       "cyISPortErrBreaks": cyISPortErrBreaks,
       "cyISPortErrOverrun": cyISPortErrOverrun,
       "cyISPortSigDTR": cyISPortSigDTR,
       "cyISPortSigCD": cyISPortSigCD,
       "cyISPortSigDSR": cyISPortSigDSR,
       "cyISPortSigRTS": cyISPortSigRTS,
       "cyISPortSigCTS": cyISPortSigCTS,
       "cyISPortSigRI": cyISPortSigRI}
)
