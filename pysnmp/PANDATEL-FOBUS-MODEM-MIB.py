# SNMP MIB module (PANDATEL-FOBUS-MODEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PANDATEL-FOBUS-MODEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:47 2024
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

(device_id,
 mdmSpecifics) = mibBuilder.importSymbols(
    "PANDATEL-MODEM-MIB",
    "device-id",
    "mdmSpecifics")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fobus_ObjectIdentity = ObjectIdentity
fobus = _Fobus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 501)
)
_FobusModemTable_Object = MibTable
fobusModemTable = _FobusModemTable_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 501, 1)
)
if mibBuilder.loadTexts:
    fobusModemTable.setStatus("mandatory")
_FobusTableEntry_Object = MibTableRow
fobusTableEntry = _FobusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 501, 1, 1)
)
fobusTableEntry.setIndexNames(
    (0, "PANDATEL-FOBUS-MODEM-MIB", "mdmRack"),
    (0, "PANDATEL-FOBUS-MODEM-MIB", "mdmModem"),
    (0, "PANDATEL-FOBUS-MODEM-MIB", "mdmPosition"),
)
if mibBuilder.loadTexts:
    fobusTableEntry.setStatus("mandatory")
_MdmRack_Type = Integer32
_MdmRack_Object = MibTableColumn
mdmRack = _MdmRack_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 501, 1, 1, 1),
    _MdmRack_Type()
)
mdmRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmRack.setStatus("mandatory")
_MdmModem_Type = Integer32
_MdmModem_Object = MibTableColumn
mdmModem = _MdmModem_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 501, 1, 1, 2),
    _MdmModem_Type()
)
mdmModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmModem.setStatus("mandatory")


class _MdmPosition_Type(Integer32):
    """Custom type mdmPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_MdmPosition_Type.__name__ = "Integer32"
_MdmPosition_Object = MibTableColumn
mdmPosition = _MdmPosition_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 501, 1, 1, 3),
    _MdmPosition_Type()
)
mdmPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmPosition.setStatus("mandatory")
_MdmModemName_Type = DisplayString
_MdmModemName_Object = MibTableColumn
mdmModemName = _MdmModemName_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 501, 1, 1, 5),
    _MdmModemName_Type()
)
mdmModemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmModemName.setStatus("mandatory")


class _MdmBackupStatus_Type(Integer32):
    """Custom type mdmBackupStatus based on Integer32"""
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
        *(("active", 3),
          ("available", 5),
          ("disable", 6),
          ("inactive", 2),
          ("not-available", 4),
          ("other", 1))
    )


_MdmBackupStatus_Type.__name__ = "Integer32"
_MdmBackupStatus_Object = MibTableColumn
mdmBackupStatus = _MdmBackupStatus_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 501, 1, 1, 11),
    _MdmBackupStatus_Type()
)
mdmBackupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmBackupStatus.setStatus("mandatory")


class _MdmActiveLink_Type(Integer32):
    """Custom type mdmActiveLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              90)
        )
    )
    namedValues = NamedValues(
        *(("disable", 90),
          ("line-port-2", 2),
          ("line-port-3", 3))
    )


_MdmActiveLink_Type.__name__ = "Integer32"
_MdmActiveLink_Object = MibTableColumn
mdmActiveLink = _MdmActiveLink_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 501, 1, 1, 12),
    _MdmActiveLink_Type()
)
mdmActiveLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmActiveLink.setStatus("mandatory")


class _MdmOperationMode_Type(Integer32):
    """Custom type mdmOperationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 5),
          ("forced-port2", 3),
          ("forced-port3", 4),
          ("other", 1))
    )


_MdmOperationMode_Type.__name__ = "Integer32"
_MdmOperationMode_Object = MibTableColumn
mdmOperationMode = _MdmOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 501, 1, 1, 66),
    _MdmOperationMode_Type()
)
mdmOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmOperationMode.setStatus("mandatory")


class _MdmAlarmConditionPort1_Type(Integer32):
    """Custom type mdmAlarmConditionPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("link-signal", 3),
          ("other", 1))
    )


_MdmAlarmConditionPort1_Type.__name__ = "Integer32"
_MdmAlarmConditionPort1_Object = MibTableColumn
mdmAlarmConditionPort1 = _MdmAlarmConditionPort1_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 501, 1, 1, 110),
    _MdmAlarmConditionPort1_Type()
)
mdmAlarmConditionPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmAlarmConditionPort1.setStatus("mandatory")


class _MdmAlarmConditionPort2_Type(Integer32):
    """Custom type mdmAlarmConditionPort2 based on Integer32"""
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
        *(("disable", 2),
          ("laser-fail", 4),
          ("no-link-signal", 3),
          ("no-link-signal-or-laser-fail", 5),
          ("other", 1))
    )


_MdmAlarmConditionPort2_Type.__name__ = "Integer32"
_MdmAlarmConditionPort2_Object = MibTableColumn
mdmAlarmConditionPort2 = _MdmAlarmConditionPort2_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 501, 1, 1, 111),
    _MdmAlarmConditionPort2_Type()
)
mdmAlarmConditionPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmAlarmConditionPort2.setStatus("mandatory")


class _MdmAlarmConditionPort3_Type(Integer32):
    """Custom type mdmAlarmConditionPort3 based on Integer32"""
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
        *(("disable", 2),
          ("laser-fail", 4),
          ("no-link-signal", 3),
          ("no-link-signal-or-laser-fail", 5),
          ("other", 1))
    )


_MdmAlarmConditionPort3_Type.__name__ = "Integer32"
_MdmAlarmConditionPort3_Object = MibTableColumn
mdmAlarmConditionPort3 = _MdmAlarmConditionPort3_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 501, 1, 1, 112),
    _MdmAlarmConditionPort3_Type()
)
mdmAlarmConditionPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmAlarmConditionPort3.setStatus("mandatory")


class _MdmTXLaserStatusPort2_Type(Integer32):
    """Custom type mdmTXLaserStatusPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_MdmTXLaserStatusPort2_Type.__name__ = "Integer32"
_MdmTXLaserStatusPort2_Object = MibTableColumn
mdmTXLaserStatusPort2 = _MdmTXLaserStatusPort2_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 501, 1, 1, 121),
    _MdmTXLaserStatusPort2_Type()
)
mdmTXLaserStatusPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTXLaserStatusPort2.setStatus("mandatory")


class _MdmTXLaserStatusPort3_Type(Integer32):
    """Custom type mdmTXLaserStatusPort3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_MdmTXLaserStatusPort3_Type.__name__ = "Integer32"
_MdmTXLaserStatusPort3_Object = MibTableColumn
mdmTXLaserStatusPort3 = _MdmTXLaserStatusPort3_Object(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 501, 1, 1, 122),
    _MdmTXLaserStatusPort3_Type()
)
mdmTXLaserStatusPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTXLaserStatusPort3.setStatus("mandatory")
_Fobus_modem_ObjectIdentity = ObjectIdentity
fobus_modem = _Fobus_modem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 2, 501)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PANDATEL-FOBUS-MODEM-MIB",
    **{"fobus": fobus,
       "fobusModemTable": fobusModemTable,
       "fobusTableEntry": fobusTableEntry,
       "mdmRack": mdmRack,
       "mdmModem": mdmModem,
       "mdmPosition": mdmPosition,
       "mdmModemName": mdmModemName,
       "mdmBackupStatus": mdmBackupStatus,
       "mdmActiveLink": mdmActiveLink,
       "mdmOperationMode": mdmOperationMode,
       "mdmAlarmConditionPort1": mdmAlarmConditionPort1,
       "mdmAlarmConditionPort2": mdmAlarmConditionPort2,
       "mdmAlarmConditionPort3": mdmAlarmConditionPort3,
       "mdmTXLaserStatusPort2": mdmTXLaserStatusPort2,
       "mdmTXLaserStatusPort3": mdmTXLaserStatusPort3,
       "fobus-modem": fobus_modem}
)
