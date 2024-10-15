# SNMP MIB module (HPIPFTRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPIPFTRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:21 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_Hpnsa_ObjectIdentity = ObjectIdentity
hpnsa = _Hpnsa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23)
)
_HpIpfE0Events_ObjectIdentity = ObjectIdentity
hpIpfE0Events = _HpIpfE0Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35)
)
_HpIpfEvtDetailStr_Type = DisplayString
_HpIpfEvtDetailStr_Object = MibScalar
hpIpfEvtDetailStr = _HpIpfEvtDetailStr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 1),
    _HpIpfEvtDetailStr_Type()
)
hpIpfEvtDetailStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpIpfEvtDetailStr.setStatus("mandatory")
_HpIpf02Events_ObjectIdentity = ObjectIdentity
hpIpf02Events = _HpIpf02Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 45)
)

# Managed Objects groups


# Notification objects

hpevtBadOsInitChecksum = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5001)
)
hpevtBadOsInitChecksum.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBadOsInitChecksum.setStatus(
        ""
    )

hpevtBadOsMcaChecksum = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5002)
)
hpevtBadOsMcaChecksum.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBadOsMcaChecksum.setStatus(
        ""
    )

hpevtBootBmcFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5003)
)
hpevtBootBmcFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootBmcFailed.setStatus(
        ""
    )

hpevtBootCellLaunchEfiFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5010)
)
hpevtBootCellLaunchEfiFailure.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootCellLaunchEfiFailure.setStatus(
        ""
    )

hpevtBootCellMonSelFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5011)
)
hpevtBootCellMonSelFailure.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootCellMonSelFailure.setStatus(
        ""
    )

hpevtBootCellMonarchCollision = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5013)
)
hpevtBootCellMonarchCollision.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootCellMonarchCollision.setStatus(
        ""
    )

hpevtBootCellVirtualizeEfiFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5023)
)
hpevtBootCellVirtualizeEfiFailure.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootCellVirtualizeEfiFailure.setStatus(
        ""
    )

hpevtBootCellVirtualizePalFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5025)
)
hpevtBootCellVirtualizePalFailure.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootCellVirtualizePalFailure.setStatus(
        ""
    )

hpevtBootCellVirtualizeSalFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5027)
)
hpevtBootCellVirtualizeSalFailure.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootCellVirtualizeSalFailure.setStatus(
        ""
    )

hpevtBootCellVirtualizeSalprocFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5028)
)
hpevtBootCellVirtualizeSalprocFailure.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootCellVirtualizeSalprocFailure.setStatus(
        ""
    )

hpevtBootCpuConfigFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5030)
)
hpevtBootCpuConfigFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootCpuConfigFail.setStatus(
        ""
    )

hpevtBootCpuEarlyConfigFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5031)
)
hpevtBootCpuEarlyConfigFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootCpuEarlyConfigFail.setStatus(
        ""
    )

hpevtBootCpuEarlyTestFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5033)
)
hpevtBootCpuEarlyTestFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootCpuEarlyTestFail.setStatus(
        ""
    )

hpevtBootCpuFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5034)
)
hpevtBootCpuFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootCpuFailed.setStatus(
        ""
    )

hpevtBootCpuLateTestFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5036)
)
hpevtBootCpuLateTestFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootCpuLateTestFail.setStatus(
        ""
    )

hpevtBootCpuLateTestInsufficientMem = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5037)
)
hpevtBootCpuLateTestInsufficientMem.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootCpuLateTestInsufficientMem.setStatus(
        ""
    )

hpevtBootEfiAllocateError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5040)
)
hpevtBootEfiAllocateError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootEfiAllocateError.setStatus(
        ""
    )

hpevtBootEfiImageCorrupt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5041)
)
hpevtBootEfiImageCorrupt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootEfiImageCorrupt.setStatus(
        ""
    )

hpevtBootEfiNotInFit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5042)
)
hpevtBootEfiNotInFit.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootEfiNotInFit.setStatus(
        ""
    )

hpevtBootEfiNvmFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5045)
)
hpevtBootEfiNvmFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootEfiNvmFail.setStatus(
        ""
    )

hpevtBootEfiRomBadSize = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5048)
)
hpevtBootEfiRomBadSize.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootEfiRomBadSize.setStatus(
        ""
    )

hpevtBootEfiRomXsumError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5049)
)
hpevtBootEfiRomXsumError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootEfiRomXsumError.setStatus(
        ""
    )

hpevtBootExtIntNestLimitedExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5050)
)
hpevtBootExtIntNestLimitedExceeded.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootExtIntNestLimitedExceeded.setStatus(
        ""
    )

hpevtBootExtIntNotServiced = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5051)
)
hpevtBootExtIntNotServiced.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootExtIntNotServiced.setStatus(
        ""
    )

hpevtBootExtIntTaken = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5052)
)
hpevtBootExtIntTaken.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootExtIntTaken.setStatus(
        ""
    )

hpevtBootFplFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5053)
)
hpevtBootFplFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootFplFailed.setStatus(
        ""
    )

hpevtBootGetPsrFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5054)
)
hpevtBootGetPsrFailure.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootGetPsrFailure.setStatus(
        ""
    )

hpevtBootHaltCell = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5055)
)
hpevtBootHaltCell.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootHaltCell.setStatus(
        ""
    )

hpevtBootIncompatiblePal = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5056)
)
hpevtBootIncompatiblePal.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootIncompatiblePal.setStatus(
        ""
    )

hpevtBootIncompatibleSlave = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5057)
)
hpevtBootIncompatibleSlave.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootIncompatibleSlave.setStatus(
        ""
    )

hpevtBootIntrptClearFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5058)
)
hpevtBootIntrptClearFailure.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootIntrptClearFailure.setStatus(
        ""
    )

hpevtBootIpmiEventFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5059)
)
hpevtBootIpmiEventFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootIpmiEventFailed.setStatus(
        ""
    )

hpevtBootIvtOffset = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5060)
)
hpevtBootIvtOffset.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootIvtOffset.setStatus(
        ""
    )

hpevtBootLdbStateBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5063)
)
hpevtBootLdbStateBad.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootLdbStateBad.setStatus(
        ""
    )

hpevtBootLostContextInt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5064)
)
hpevtBootLostContextInt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootLostContextInt.setStatus(
        ""
    )

hpevtBootMinStateRegError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5065)
)
hpevtBootMinStateRegError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootMinStateRegError.setStatus(
        ""
    )

hpevtBootMonarchTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5067)
)
hpevtBootMonarchTimeout.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootMonarchTimeout.setStatus(
        ""
    )

hpevtBootNoPalBInFit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5069)
)
hpevtBootNoPalBInFit.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootNoPalBInFit.setStatus(
        ""
    )

hpevtBootNoSalBInFit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5070)
)
hpevtBootNoSalBInFit.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootNoSalBInFit.setStatus(
        ""
    )

hpevtBootNvmFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5073)
)
hpevtBootNvmFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootNvmFail.setStatus(
        ""
    )

hpevtBootOutOfRangeVector = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5076)
)
hpevtBootOutOfRangeVector.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootOutOfRangeVector.setStatus(
        ""
    )

hpevtBootPalCopyInfoError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5077)
)
hpevtBootPalCopyInfoError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootPalCopyInfoError.setStatus(
        ""
    )

hpevtBootPalCopyPalError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5078)
)
hpevtBootPalCopyPalError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootPalCopyPalError.setStatus(
        ""
    )

hpevtBootPalProcFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5079)
)
hpevtBootPalProcFailure.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootPalProcFailure.setStatus(
        ""
    )

hpevtBootPlatConsoleDevFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5080)
)
hpevtBootPlatConsoleDevFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootPlatConsoleDevFailed.setStatus(
        ""
    )

hpevtBootPlatIntfcDevFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5081)
)
hpevtBootPlatIntfcDevFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootPlatIntfcDevFailed.setStatus(
        ""
    )

hpevtBootPlatScrBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5082)
)
hpevtBootPlatScrBad.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootPlatScrBad.setStatus(
        ""
    )

hpevtBootRendezFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5083)
)
hpevtBootRendezFailure.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootRendezFailure.setStatus(
        ""
    )

hpevtBootSalExtractError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5084)
)
hpevtBootSalExtractError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootSalExtractError.setStatus(
        ""
    )

hpevtBootScrFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5085)
)
hpevtBootScrFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootScrFail.setStatus(
        ""
    )

hpevtBootSelFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5087)
)
hpevtBootSelFull.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootSelFull.setStatus(
        ""
    )

hpevtBootSlaveNoFinalWakeupVector = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5091)
)
hpevtBootSlaveNoFinalWakeupVector.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootSlaveNoFinalWakeupVector.setStatus(
        ""
    )

hpevtBootSlaveRendezHandlerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5092)
)
hpevtBootSlaveRendezHandlerFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootSlaveRendezHandlerFail.setStatus(
        ""
    )

hpevtBootSmbiosBuildError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5098)
)
hpevtBootSmbiosBuildError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootSmbiosBuildError.setStatus(
        ""
    )

hpevtBootTrapNestLimitedExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5100)
)
hpevtBootTrapNestLimitedExceeded.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootTrapNestLimitedExceeded.setStatus(
        ""
    )

hpevtBootTrapNotServiced = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5101)
)
hpevtBootTrapNotServiced.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootTrapNotServiced.setStatus(
        ""
    )

hpevtBootTrapTaken = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5102)
)
hpevtBootTrapTaken.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootTrapTaken.setStatus(
        ""
    )

hpevtBootUnclearedInt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5103)
)
hpevtBootUnclearedInt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootUnclearedInt.setStatus(
        ""
    )

hpevtBootUnexpectedExtIntPostRedirTable = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5104)
)
hpevtBootUnexpectedExtIntPostRedirTable.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootUnexpectedExtIntPostRedirTable.setStatus(
        ""
    )

hpevtBootUnexpectedIntPreRedirTable = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5105)
)
hpevtBootUnexpectedIntPreRedirTable.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootUnexpectedIntPreRedirTable.setStatus(
        ""
    )

hpevtBootUnexpectedMca = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5106)
)
hpevtBootUnexpectedMca.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootUnexpectedMca.setStatus(
        ""
    )

hpevtBootUnexpectedTrapPostRedirTable = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5107)
)
hpevtBootUnexpectedTrapPostRedirTable.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootUnexpectedTrapPostRedirTable.setStatus(
        ""
    )

hpevtBootUnknownFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5108)
)
hpevtBootUnknownFailure.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootUnknownFailure.setStatus(
        ""
    )

hpevtErrorsPalFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5118)
)
hpevtErrorsPalFailure.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtErrorsPalFailure.setStatus(
        ""
    )

hpevtExpMcNotRegistered = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5119)
)
hpevtExpMcNotRegistered.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtExpMcNotRegistered.setStatus(
        ""
    )

hpevtInitInitiated = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5121)
)
hpevtInitInitiated.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtInitInitiated.setStatus(
        ""
    )

hpevtIoCheckLbaMissingErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5123)
)
hpevtIoCheckLbaMissingErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoCheckLbaMissingErr.setStatus(
        ""
    )

hpevtIoCheckNumSlotsErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5124)
)
hpevtIoCheckNumSlotsErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoCheckNumSlotsErr.setStatus(
        ""
    )

hpevtIoCheckRopeWidthErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5125)
)
hpevtIoCheckRopeWidthErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoCheckRopeWidthErr.setStatus(
        ""
    )

hpevtIoCheckXtraLbaFoundErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5127)
)
hpevtIoCheckXtraLbaFoundErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoCheckXtraLbaFoundErr.setStatus(
        ""
    )

hpevtIoDllError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5130)
)
hpevtIoDllError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoDllError.setStatus(
        ""
    )

hpevtIoHotPlugCtrlFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5131)
)
hpevtIoHotPlugCtrlFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoHotPlugCtrlFailed.setStatus(
        ""
    )

hpevtIoInvalidRopeBundle = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5132)
)
hpevtIoInvalidRopeBundle.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoInvalidRopeBundle.setStatus(
        ""
    )

hpevtIoLbaClearErrFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5133)
)
hpevtIoLbaClearErrFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoLbaClearErrFailed.setStatus(
        ""
    )

hpevtIoLbaResetError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5136)
)
hpevtIoLbaResetError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoLbaResetError.setStatus(
        ""
    )

hpevtIoNotEnoughPowerError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5137)
)
hpevtIoNotEnoughPowerError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoNotEnoughPowerError.setStatus(
        ""
    )

hpevtIoPciMappingFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5138)
)
hpevtIoPciMappingFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoPciMappingFailed.setStatus(
        ""
    )

hpevtIoPciMappingTooBig = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5139)
)
hpevtIoPciMappingTooBig.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoPciMappingTooBig.setStatus(
        ""
    )

hpevtIoPciUnmappingFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5140)
)
hpevtIoPciUnmappingFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoPciUnmappingFailed.setStatus(
        ""
    )

hpevtIoPcixcapSampleError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5141)
)
hpevtIoPcixcapSampleError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoPcixcapSampleError.setStatus(
        ""
    )

hpevtIoPmNotRespondingError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5142)
)
hpevtIoPmNotRespondingError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoPmNotRespondingError.setStatus(
        ""
    )

hpevtIoRopeResetError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5143)
)
hpevtIoRopeResetError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoRopeResetError.setStatus(
        ""
    )

hpevtIoSbaClearErrFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5144)
)
hpevtIoSbaClearErrFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoSbaClearErrFailed.setStatus(
        ""
    )

hpevtIoSlotPowerDefaultError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5145)
)
hpevtIoSlotPowerDefaultError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoSlotPowerDefaultError.setStatus(
        ""
    )

hpevtIoSlotPowerOnError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5146)
)
hpevtIoSlotPowerOnError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoSlotPowerOnError.setStatus(
        ""
    )

hpevtIoSlotStandbyPowerError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5147)
)
hpevtIoSlotStandbyPowerError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoSlotStandbyPowerError.setStatus(
        ""
    )

hpevtIoUnknownPcixcapVal = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5148)
)
hpevtIoUnknownPcixcapVal.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoUnknownPcixcapVal.setStatus(
        ""
    )

hpevtIoUnsupRopeFreq = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5149)
)
hpevtIoUnsupRopeFreq.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoUnsupRopeFreq.setStatus(
        ""
    )

hpevtIoUnsupportedLba = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5150)
)
hpevtIoUnsupportedLba.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoUnsupportedLba.setStatus(
        ""
    )

hpevtMcInitiated = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5152)
)
hpevtMcInitiated.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMcInitiated.setStatus(
        ""
    )

hpevtMdtConstructAreaBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5155)
)
hpevtMdtConstructAreaBad.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMdtConstructAreaBad.setStatus(
        ""
    )

hpevtMdtLmmioEntryNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5156)
)
hpevtMdtLmmioEntryNotFound.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMdtLmmioEntryNotFound.setStatus(
        ""
    )

hpevtMdtPageZeroBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5157)
)
hpevtMdtPageZeroBad.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMdtPageZeroBad.setStatus(
        ""
    )

hpevtMdtUnableToFindSpace = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5158)
)
hpevtMdtUnableToFindSpace.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMdtUnableToFindSpace.setStatus(
        ""
    )

hpevtMediaFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5159)
)
hpevtMediaFailure.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMediaFailure.setStatus(
        ""
    )

hpevtMemBibRegFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5160)
)
hpevtMemBibRegFailure.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemBibRegFailure.setStatus(
        ""
    )

hpevtMemCacheLine0WrRdFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5161)
)
hpevtMemCacheLine0WrRdFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemCacheLine0WrRdFailed.setStatus(
        ""
    )

hpevtMemDimmLoadOrderErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5171)
)
hpevtMemDimmLoadOrderErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemDimmLoadOrderErr.setStatus(
        ""
    )

hpevtMemDimmSpdChecksum = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5172)
)
hpevtMemDimmSpdChecksum.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemDimmSpdChecksum.setStatus(
        ""
    )

hpevtMemDimmSpdFatal = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5173)
)
hpevtMemDimmSpdFatal.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemDimmSpdFatal.setStatus(
        ""
    )

hpevtMemDimmTypeIncompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5174)
)
hpevtMemDimmTypeIncompatible.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemDimmTypeIncompatible.setStatus(
        ""
    )

hpevtMemDimmTypeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5175)
)
hpevtMemDimmTypeMismatch.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemDimmTypeMismatch.setStatus(
        ""
    )

hpevtMemDimmTypeTableFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5176)
)
hpevtMemDimmTypeTableFull.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemDimmTypeTableFull.setStatus(
        ""
    )

hpevtMemDmtEntryNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5179)
)
hpevtMemDmtEntryNotFound.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemDmtEntryNotFound.setStatus(
        ""
    )

hpevtMemEccMbeDataTstFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5180)
)
hpevtMemEccMbeDataTstFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemEccMbeDataTstFailed.setStatus(
        ""
    )

hpevtMemEccMbeSignalTstFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5181)
)
hpevtMemEccMbeSignalTstFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemEccMbeSignalTstFailed.setStatus(
        ""
    )

hpevtMemEccSbeDataTstFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5182)
)
hpevtMemEccSbeDataTstFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemEccSbeDataTstFailed.setStatus(
        ""
    )

hpevtMemEccSbeEccTstFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5183)
)
hpevtMemEccSbeEccTstFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemEccSbeEccTstFailed.setStatus(
        ""
    )

hpevtMemEnoughMemFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5185)
)
hpevtMemEnoughMemFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemEnoughMemFailed.setStatus(
        ""
    )

hpevtMemErrAddrNotInMbat = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5186)
)
hpevtMemErrAddrNotInMbat.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemErrAddrNotInMbat.setStatus(
        ""
    )

hpevtMemErrClearFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5187)
)
hpevtMemErrClearFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemErrClearFail.setStatus(
        ""
    )

hpevtMemErrLogFailedToClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5189)
)
hpevtMemErrLogFailedToClear.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemErrLogFailedToClear.setStatus(
        ""
    )

hpevtMemErrorRegClearFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5190)
)
hpevtMemErrorRegClearFailure.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemErrorRegClearFailure.setStatus(
        ""
    )

hpevtMemExtFatalLoadOrdErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5191)
)
hpevtMemExtFatalLoadOrdErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemExtFatalLoadOrdErr.setStatus(
        ""
    )

hpevtMemFirmwareProb = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5193)
)
hpevtMemFirmwareProb.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemFirmwareProb.setStatus(
        ""
    )

hpevtMemInterleaveCodeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5199)
)
hpevtMemInterleaveCodeFailure.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemInterleaveCodeFailure.setStatus(
        ""
    )

hpevtMemMainMemFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5202)
)
hpevtMemMainMemFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemMainMemFailed.setStatus(
        ""
    )

hpevtMemMbeInRank = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5204)
)
hpevtMemMbeInRank.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemMbeInRank.setStatus(
        ""
    )

hpevtMemMcRegFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5205)
)
hpevtMemMcRegFailure.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemMcRegFailure.setStatus(
        ""
    )

hpevtMemNoDimmsInstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5208)
)
hpevtMemNoDimmsInstalled.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemNoDimmsInstalled.setStatus(
        ""
    )

hpevtMemNoMemFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5209)
)
hpevtMemNoMemFound.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemNoMemFound.setStatus(
        ""
    )

hpevtMemPdtDisabledHalt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5211)
)
hpevtMemPdtDisabledHalt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemPdtDisabledHalt.setStatus(
        ""
    )

hpevtMemPdtDisabledWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5212)
)
hpevtMemPdtDisabledWarning.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemPdtDisabledWarning.setStatus(
        ""
    )

hpevtMemPdtNvmErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5214)
)
hpevtMemPdtNvmErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemPdtNvmErr.setStatus(
        ""
    )

hpevtMemPdtTableFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5216)
)
hpevtMemPdtTableFull.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemPdtTableFull.setStatus(
        ""
    )

hpevtMemPlatformInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5218)
)
hpevtMemPlatformInitFailure.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemPlatformInitFailure.setStatus(
        ""
    )

hpevtMemRankEntryNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5219)
)
hpevtMemRankEntryNotFound.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemRankEntryNotFound.setStatus(
        ""
    )

hpevtMemTestExcessMcBits = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5237)
)
hpevtMemTestExcessMcBits.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemTestExcessMcBits.setStatus(
        ""
    )

hpevtMemTestFwdProgBitsInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5238)
)
hpevtMemTestFwdProgBitsInvalid.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemTestFwdProgBitsInvalid.setStatus(
        ""
    )

hpevtMemTestStatusBitsInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5244)
)
hpevtMemTestStatusBitsInvalid.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemTestStatusBitsInvalid.setStatus(
        ""
    )

hpevtMemTestSummaryBitsInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5245)
)
hpevtMemTestSummaryBitsInvalid.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemTestSummaryBitsInvalid.setStatus(
        ""
    )

hpevtMemUnexpectedMca = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5248)
)
hpevtMemUnexpectedMca.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemUnexpectedMca.setStatus(
        ""
    )

hpevtMemWarnDistributionCheckBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5250)
)
hpevtMemWarnDistributionCheckBypass.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemWarnDistributionCheckBypass.setStatus(
        ""
    )

hpevtMemWarnLoadingOrderBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5252)
)
hpevtMemWarnLoadingOrderBypass.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemWarnLoadingOrderBypass.setStatus(
        ""
    )

hpevtMemWarnLoopOnDestTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5253)
)
hpevtMemWarnLoopOnDestTest.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemWarnLoopOnDestTest.setStatus(
        ""
    )

hpevtMemWarnSetCheckBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5255)
)
hpevtMemWarnSetCheckBypass.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemWarnSetCheckBypass.setStatus(
        ""
    )

hpevtMemWarnSpdBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5256)
)
hpevtMemWarnSpdBypass.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemWarnSpdBypass.setStatus(
        ""
    )

hpevtMemWarnUsingAltConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5257)
)
hpevtMemWarnUsingAltConfig.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemWarnUsingAltConfig.setStatus(
        ""
    )

hpevtOsInitNotRegistered = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5260)
)
hpevtOsInitNotRegistered.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtOsInitNotRegistered.setStatus(
        ""
    )

hpevtOsMcaNotRegistered = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5263)
)
hpevtOsMcaNotRegistered.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtOsMcaNotRegistered.setStatus(
        ""
    )

hpevtOsMcaUncorrectedMc = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5264)
)
hpevtOsMcaUncorrectedMc.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtOsMcaUncorrectedMc.setStatus(
        ""
    )

hpevtPdhMiscRegFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5266)
)
hpevtPdhMiscRegFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdhMiscRegFail.setStatus(
        ""
    )

hpevtSalCheckUnknownFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5268)
)
hpevtSalCheckUnknownFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSalCheckUnknownFail.setStatus(
        ""
    )

hpevtSalInitUnknownFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5270)
)
hpevtSalInitUnknownFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSalInitUnknownFail.setStatus(
        ""
    )

hpevtUndefinedSmcInterleaveErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5278)
)
hpevtUndefinedSmcInterleaveErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUndefinedSmcInterleaveErr.setStatus(
        ""
    )

hpevtUnexpectedRetToSalCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5279)
)
hpevtUnexpectedRetToSalCheck.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUnexpectedRetToSalCheck.setStatus(
        ""
    )

hpevtUnexpectedRetToSalInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5280)
)
hpevtUnexpectedRetToSalInit.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUnexpectedRetToSalInit.setStatus(
        ""
    )

hpevtFwInstalledCpuDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5335)
)
hpevtFwInstalledCpuDegraded.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFwInstalledCpuDegraded.setStatus(
        ""
    )

hpevtPdRendezTreeError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5354)
)
hpevtPdRendezTreeError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdRendezTreeError.setStatus(
        ""
    )

hpevtPdCellConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5359)
)
hpevtPdCellConfigError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdCellConfigError.setStatus(
        ""
    )

hpevtPdRemoteCsrReadError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5360)
)
hpevtPdRemoteCsrReadError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdRemoteCsrReadError.setStatus(
        ""
    )

hpevtPdCellLateForRendez = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5361)
)
hpevtPdCellLateForRendez.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdCellLateForRendez.setStatus(
        ""
    )

hpevtPdIncompatibleCpuTypes = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5365)
)
hpevtPdIncompatibleCpuTypes.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdIncompatibleCpuTypes.setStatus(
        ""
    )

hpevtPdCellLateLocalRendezSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5366)
)
hpevtPdCellLateLocalRendezSet.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdCellLateLocalRendezSet.setStatus(
        ""
    )

hpevtCellNotInGlobalSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5376)
)
hpevtCellNotInGlobalSet.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCellNotInGlobalSet.setStatus(
        ""
    )

hpevtNoViableCoreCellInPd = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5380)
)
hpevtNoViableCoreCellInPd.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtNoViableCoreCellInPd.setStatus(
        ""
    )

hpevtErrorPromotingCoreCell = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5383)
)
hpevtErrorPromotingCoreCell.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtErrorPromotingCoreCell.setStatus(
        ""
    )

hpevtFabricNoServiceProviders = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5403)
)
hpevtFabricNoServiceProviders.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricNoServiceProviders.setStatus(
        ""
    )

hpevtFabricPortError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5404)
)
hpevtFabricPortError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricPortError.setStatus(
        ""
    )

hpevtFabricReadError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5405)
)
hpevtFabricReadError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricReadError.setStatus(
        ""
    )

hpevtFabricWriteError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5406)
)
hpevtFabricWriteError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricWriteError.setStatus(
        ""
    )

hpevtXbcSlicesHwVersionDiffer = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5407)
)
hpevtXbcSlicesHwVersionDiffer.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXbcSlicesHwVersionDiffer.setStatus(
        ""
    )

hpevtXbcSlicesInDiffLocation = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5408)
)
hpevtXbcSlicesInDiffLocation.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXbcSlicesInDiffLocation.setStatus(
        ""
    )

hpevtMonarchTakeover = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5411)
)
hpevtMonarchTakeover.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMonarchTakeover.setStatus(
        ""
    )

hpevtDeadSram = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5416)
)
hpevtDeadSram.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtDeadSram.setStatus(
        ""
    )

hpevtDeadDillon = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5417)
)
hpevtDeadDillon.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtDeadDillon.setStatus(
        ""
    )

hpevtDeadPdhHw = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5418)
)
hpevtDeadPdhHw.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtDeadPdhHw.setStatus(
        ""
    )

hpevtIoPciBusMixedSpeeds = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5419)
)
hpevtIoPciBusMixedSpeeds.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoPciBusMixedSpeeds.setStatus(
        ""
    )

hpevtIoPciBusDepthExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5420)
)
hpevtIoPciBusDepthExceeded.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoPciBusDepthExceeded.setStatus(
        ""
    )

hpevtlotimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5432)
)
hpevtlotimeout.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtlotimeout.setStatus(
        ""
    )

hpevtIoBuswalkSuperio = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5438)
)
hpevtIoBuswalkSuperio.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoBuswalkSuperio.setStatus(
        ""
    )

hpevtIoSbaCorrDataParityErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5440)
)
hpevtIoSbaCorrDataParityErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoSbaCorrDataParityErr.setStatus(
        ""
    )

hpevtIoSbaFatalDataParityErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5442)
)
hpevtIoSbaFatalDataParityErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoSbaFatalDataParityErr.setStatus(
        ""
    )

hpevtIoSbaUncFunctionErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5443)
)
hpevtIoSbaUncFunctionErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoSbaUncFunctionErr.setStatus(
        ""
    )

hpevtIoSbaFatalFunctionErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5444)
)
hpevtIoSbaFatalFunctionErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoSbaFatalFunctionErr.setStatus(
        ""
    )

hpevtIoSbaFatalParityErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5445)
)
hpevtIoSbaFatalParityErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoSbaFatalParityErr.setStatus(
        ""
    )

hpevtIoSbaFatalMapErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5446)
)
hpevtIoSbaFatalMapErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoSbaFatalMapErr.setStatus(
        ""
    )

hpevtIoSbaFatalTimeoutErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5447)
)
hpevtIoSbaFatalTimeoutErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoSbaFatalTimeoutErr.setStatus(
        ""
    )

hpevtIoLbaInitErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5448)
)
hpevtIoLbaInitErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoLbaInitErr.setStatus(
        ""
    )

hpevtIoLbaCorrTimeoutErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5449)
)
hpevtIoLbaCorrTimeoutErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoLbaCorrTimeoutErr.setStatus(
        ""
    )

hpevtIoLbaUncFunctionErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5450)
)
hpevtIoLbaUncFunctionErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoLbaUncFunctionErr.setStatus(
        ""
    )

hpevtIoLbaUncTimeoutErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5451)
)
hpevtIoLbaUncTimeoutErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoLbaUncTimeoutErr.setStatus(
        ""
    )

hpevtIoLbaMiscUncErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5452)
)
hpevtIoLbaMiscUncErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoLbaMiscUncErr.setStatus(
        ""
    )

hpevtIoLbaUncParityErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5453)
)
hpevtIoLbaUncParityErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoLbaUncParityErr.setStatus(
        ""
    )

hpevtIoLbaMiscFatalErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5454)
)
hpevtIoLbaMiscFatalErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoLbaMiscFatalErr.setStatus(
        ""
    )

hpevtIoLbaFatalFunctionErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5455)
)
hpevtIoLbaFatalFunctionErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoLbaFatalFunctionErr.setStatus(
        ""
    )

hpevtIoLbaFatalParityErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5456)
)
hpevtIoLbaFatalParityErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoLbaFatalParityErr.setStatus(
        ""
    )

hpevtIoLbaFatalTimeoutErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5457)
)
hpevtIoLbaFatalTimeoutErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoLbaFatalTimeoutErr.setStatus(
        ""
    )

hpevtIoDevAdapterMiscUncErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5458)
)
hpevtIoDevAdapterMiscUncErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoDevAdapterMiscUncErr.setStatus(
        ""
    )

hpevtIoDevAdapterMiscFatalErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5459)
)
hpevtIoDevAdapterMiscFatalErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoDevAdapterMiscFatalErr.setStatus(
        ""
    )

hpevtMemDimmSpdExtendedChecksum = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5464)
)
hpevtMemDimmSpdExtendedChecksum.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemDimmSpdExtendedChecksum.setStatus(
        ""
    )

hpevtOptsHdrCksumError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5467)
)
hpevtOptsHdrCksumError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtOptsHdrCksumError.setStatus(
        ""
    )

hpevtOptsDataCksumError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5468)
)
hpevtOptsDataCksumError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtOptsDataCksumError.setStatus(
        ""
    )

hpevtPdMemIntlvWaysMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5473)
)
hpevtPdMemIntlvWaysMismatch.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdMemIntlvWaysMismatch.setStatus(
        ""
    )

hpevtPdMemUnintlvdMemory = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5474)
)
hpevtPdMemUnintlvdMemory.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdMemUnintlvdMemory.setStatus(
        ""
    )

hpevtPdMemNoMemoryDesc = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5478)
)
hpevtPdMemNoMemoryDesc.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdMemNoMemoryDesc.setStatus(
        ""
    )

hpevtPdMemUpdateLocalCellFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5479)
)
hpevtPdMemUpdateLocalCellFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdMemUpdateLocalCellFailed.setStatus(
        ""
    )

hpevtPdMemPdtAddrNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5483)
)
hpevtPdMemPdtAddrNotFound.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdMemPdtAddrNotFound.setStatus(
        ""
    )

hpevtPdMemPdtInstallFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5485)
)
hpevtPdMemPdtInstallFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdMemPdtInstallFail.setStatus(
        ""
    )

hpevtUnusableResource = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5490)
)
hpevtUnusableResource.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUnusableResource.setStatus(
        ""
    )

hpevtFwError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5491)
)
hpevtFwError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFwError.setStatus(
        ""
    )

hpevtNvramDataCmpError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5492)
)
hpevtNvramDataCmpError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtNvramDataCmpError.setStatus(
        ""
    )

hpevtNvramCrcError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5493)
)
hpevtNvramCrcError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtNvramCrcError.setStatus(
        ""
    )

hpevtErm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5494)
)
hpevtErm.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtErm.setStatus(
        ""
    )

hpevtErrorObtainingSemaphore = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5496)
)
hpevtErrorObtainingSemaphore.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtErrorObtainingSemaphore.setStatus(
        ""
    )

hpevtNvramBlockRevMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5498)
)
hpevtNvramBlockRevMismatch.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtNvramBlockRevMismatch.setStatus(
        ""
    )

hpevtNvramBlockNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5499)
)
hpevtNvramBlockNotFound.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtNvramBlockNotFound.setStatus(
        ""
    )

hpevtNvramBlockLocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5500)
)
hpevtNvramBlockLocked.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtNvramBlockLocked.setStatus(
        ""
    )

hpevtNvramBlockUnlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5501)
)
hpevtNvramBlockUnlocked.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtNvramBlockUnlocked.setStatus(
        ""
    )

hpevtNvramHeaderNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5502)
)
hpevtNvramHeaderNotFound.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtNvramHeaderNotFound.setStatus(
        ""
    )

hpevtNvmFreelistCorrupt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5503)
)
hpevtNvmFreelistCorrupt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtNvmFreelistCorrupt.setStatus(
        ""
    )

hpevtResetForReconfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5505)
)
hpevtResetForReconfig.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtResetForReconfig.setStatus(
        ""
    )

hpevtPdRendezUtilityError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5507)
)
hpevtPdRendezUtilityError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdRendezUtilityError.setStatus(
        ""
    )

hpevtHalt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5509)
)
hpevtHalt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtHalt.setStatus(
        ""
    )

hpevtDuiNoConsole = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5510)
)
hpevtDuiNoConsole.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtDuiNoConsole.setStatus(
        ""
    )

hpevtErrorProcFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5511)
)
hpevtErrorProcFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtErrorProcFailed.setStatus(
        ""
    )

hpevtReconfigResetFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5514)
)
hpevtReconfigResetFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtReconfigResetFail.setStatus(
        ""
    )

hpevtPdErrorReachableSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5515)
)
hpevtPdErrorReachableSet.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdErrorReachableSet.setStatus(
        ""
    )

hpevtIoBridgeDepthExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5518)
)
hpevtIoBridgeDepthExceeded.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoBridgeDepthExceeded.setStatus(
        ""
    )

hpevtEfiConsoleDriverError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5521)
)
hpevtEfiConsoleDriverError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiConsoleDriverError.setStatus(
        ""
    )

hpevtMemTestCodeInPage0Corrupt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5525)
)
hpevtMemTestCodeInPage0Corrupt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemTestCodeInPage0Corrupt.setStatus(
        ""
    )

hpevtRemoteCellStateUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5527)
)
hpevtRemoteCellStateUnknown.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtRemoteCellStateUnknown.setStatus(
        ""
    )

hpevtPdMltplCoreCells = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5528)
)
hpevtPdMltplCoreCells.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdMltplCoreCells.setStatus(
        ""
    )

hpevtUtilSendCommandError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5529)
)
hpevtUtilSendCommandError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUtilSendCommandError.setStatus(
        ""
    )

hpevtUtilCellSlotError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5530)
)
hpevtUtilCellSlotError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUtilCellSlotError.setStatus(
        ""
    )

hpevtMcCellRendezFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5546)
)
hpevtMcCellRendezFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMcCellRendezFailed.setStatus(
        ""
    )

hpevtMcNoAccessToPd = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5547)
)
hpevtMcNoAccessToPd.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMcNoAccessToPd.setStatus(
        ""
    )

hpevtMcLossOfLockstep = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5548)
)
hpevtMcLossOfLockstep.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMcLossOfLockstep.setStatus(
        ""
    )

hpevtMcPdCellRendezFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5550)
)
hpevtMcPdCellRendezFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMcPdCellRendezFailed.setStatus(
        ""
    )

hpevtMcProcErrHalt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5556)
)
hpevtMcProcErrHalt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMcProcErrHalt.setStatus(
        ""
    )

hpevtMcCellMonarchTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5557)
)
hpevtMcCellMonarchTimeout.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMcCellMonarchTimeout.setStatus(
        ""
    )

hpevtMcPdCellMissedRendez = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5558)
)
hpevtMcPdCellMissedRendez.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMcPdCellMissedRendez.setStatus(
        ""
    )

hpevtMcPdMonarchTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5559)
)
hpevtMcPdMonarchTimeout.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMcPdMonarchTimeout.setStatus(
        ""
    )

hpevtRemoteSetViewRootError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5560)
)
hpevtRemoteSetViewRootError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtRemoteSetViewRootError.setStatus(
        ""
    )

hpevtCsrTestFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5566)
)
hpevtCsrTestFailure.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCsrTestFailure.setStatus(
        ""
    )

hpevtPdMemGetIcmInfoFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5567)
)
hpevtPdMemGetIcmInfoFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdMemGetIcmInfoFailed.setStatus(
        ""
    )

hpevtPdMemGetCellInfoFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5568)
)
hpevtPdMemGetCellInfoFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdMemGetCellInfoFailed.setStatus(
        ""
    )

hpevtPdMemUpdateCellGniFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5569)
)
hpevtPdMemUpdateCellGniFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdMemUpdateCellGniFailed.setStatus(
        ""
    )

hpevtPdMemAdjustMinZiFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5570)
)
hpevtPdMemAdjustMinZiFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdMemAdjustMinZiFailed.setStatus(
        ""
    )

hpevtStableProfileXsumError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5572)
)
hpevtStableProfileXsumError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtStableProfileXsumError.setStatus(
        ""
    )

hpevtDynamicProfileXsumError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5573)
)
hpevtDynamicProfileXsumError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtDynamicProfileXsumError.setStatus(
        ""
    )

hpevtPartitionProfileXsumError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5574)
)
hpevtPartitionProfileXsumError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPartitionProfileXsumError.setStatus(
        ""
    )

hpevtStableProfileSeqidInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5575)
)
hpevtStableProfileSeqidInvalid.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtStableProfileSeqidInvalid.setStatus(
        ""
    )

hpevtDynamicProfileSeqidInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5577)
)
hpevtDynamicProfileSeqidInvalid.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtDynamicProfileSeqidInvalid.setStatus(
        ""
    )

hpevtPartitionProfileSeqidInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5578)
)
hpevtPartitionProfileSeqidInvalid.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPartitionProfileSeqidInvalid.setStatus(
        ""
    )

hpevtEfiFwError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5579)
)
hpevtEfiFwError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiFwError.setStatus(
        ""
    )

hpevtCmplxProfilePdNumMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5580)
)
hpevtCmplxProfilePdNumMismatch.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCmplxProfilePdNumMismatch.setStatus(
        ""
    )

hpevtCmplxProfilePdNumInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5581)
)
hpevtCmplxProfilePdNumInvalid.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCmplxProfilePdNumInvalid.setStatus(
        ""
    )

hpevtXbcPortSm4Error = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5583)
)
hpevtXbcPortSm4Error.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXbcPortSm4Error.setStatus(
        ""
    )

hpevtXbcPortSm4NotReleased = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5584)
)
hpevtXbcPortSm4NotReleased.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXbcPortSm4NotReleased.setStatus(
        ""
    )

hpevtBootBmcTokenUploadFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5594)
)
hpevtBootBmcTokenUploadFailure.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootBmcTokenUploadFailure.setStatus(
        ""
    )

hpevtBootNvmTokenAccessFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5595)
)
hpevtBootNvmTokenAccessFailure.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootNvmTokenAccessFailure.setStatus(
        ""
    )

hpevtBootBmcTokenDownloadError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5596)
)
hpevtBootBmcTokenDownloadError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootBmcTokenDownloadError.setStatus(
        ""
    )

hpevtBootErrorWritingFirstBootToken = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5597)
)
hpevtBootErrorWritingFirstBootToken.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootErrorWritingFirstBootToken.setStatus(
        ""
    )

hpevtBootFruReadError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5598)
)
hpevtBootFruReadError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootFruReadError.setStatus(
        ""
    )

hpevtBootFruXsumError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5599)
)
hpevtBootFruXsumError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootFruXsumError.setStatus(
        ""
    )

hpevtBootFruVersionError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5600)
)
hpevtBootFruVersionError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootFruVersionError.setStatus(
        ""
    )

hpevtBootRomRevToFitRevWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5601)
)
hpevtBootRomRevToFitRevWarning.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootRomRevToFitRevWarning.setStatus(
        ""
    )

hpevtBootRomRevToRevBlockWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5602)
)
hpevtBootRomRevToRevBlockWarning.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootRomRevToRevBlockWarning.setStatus(
        ""
    )

hpevtBootPrimaryFitBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5603)
)
hpevtBootPrimaryFitBad.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootPrimaryFitBad.setStatus(
        ""
    )

hpevtBootSecondaryFitBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5604)
)
hpevtBootSecondaryFitBad.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootSecondaryFitBad.setStatus(
        ""
    )

hpevtBootPalARomWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5605)
)
hpevtBootPalARomWarning.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootPalARomWarning.setStatus(
        ""
    )

hpevtBootPalBRomWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5606)
)
hpevtBootPalBRomWarning.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootPalBRomWarning.setStatus(
        ""
    )

hpevtErrorUpdatingGroupBProfile = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5607)
)
hpevtErrorUpdatingGroupBProfile.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtErrorUpdatingGroupBProfile.setStatus(
        ""
    )

hpevtIoPciPerr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5617)
)
hpevtIoPciPerr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoPciPerr.setStatus(
        ""
    )

hpevtIoPciSerr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5618)
)
hpevtIoPciSerr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoPciSerr.setStatus(
        ""
    )

hpevtIoCheckLbaDeconfigErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5619)
)
hpevtIoCheckLbaDeconfigErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoCheckLbaDeconfigErr.setStatus(
        ""
    )

hpevtErrorUpdatingGroupCProfile = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5621)
)
hpevtErrorUpdatingGroupCProfile.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtErrorUpdatingGroupCProfile.setStatus(
        ""
    )

hpevtCellNotInAPd = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5622)
)
hpevtCellNotInAPd.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCellNotInAPd.setStatus(
        ""
    )

hpevtMemDimmThermalLoadOrderWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5623)
)
hpevtMemDimmThermalLoadOrderWarn.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemDimmThermalLoadOrderWarn.setStatus(
        ""
    )

hpevtCellMajorityNotPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5626)
)
hpevtCellMajorityNotPresent.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCellMajorityNotPresent.setStatus(
        ""
    )

hpevtInitRendezvousSlavesFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5638)
)
hpevtInitRendezvousSlavesFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtInitRendezvousSlavesFail.setStatus(
        ""
    )

hpevtMcIoClearFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5646)
)
hpevtMcIoClearFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMcIoClearFail.setStatus(
        ""
    )

hpevtMcPalCantEscalateToBerr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5655)
)
hpevtMcPalCantEscalateToBerr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMcPalCantEscalateToBerr.setStatus(
        ""
    )

hpevtMcPalCantEscalateToBinit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5656)
)
hpevtMcPalCantEscalateToBinit.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMcPalCantEscalateToBinit.setStatus(
        ""
    )

hpevtMcPalGetFeatFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5657)
)
hpevtMcPalGetFeatFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMcPalGetFeatFail.setStatus(
        ""
    )

hpevtMcPalRendFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5658)
)
hpevtMcPalRendFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMcPalRendFail.setStatus(
        ""
    )

hpevtMcPalSetFeatFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5659)
)
hpevtMcPalSetFeatFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMcPalSetFeatFail.setStatus(
        ""
    )

hpevtMcRendezvousSlavesFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5677)
)
hpevtMcRendezvousSlavesFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMcRendezvousSlavesFail.setStatus(
        ""
    )

hpevtMcRendezBadVectRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5679)
)
hpevtMcRendezBadVectRange.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMcRendezBadVectRange.setStatus(
        ""
    )

hpevtMcRendezNoMonarch = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5682)
)
hpevtMcRendezNoMonarch.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMcRendezNoMonarch.setStatus(
        ""
    )

hpevtMcRendezNoWakeup = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5683)
)
hpevtMcRendezNoWakeup.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMcRendezNoWakeup.setStatus(
        ""
    )

hpevtMcRendezPalCantEscalate = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5684)
)
hpevtMcRendezPalCantEscalate.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMcRendezPalCantEscalate.setStatus(
        ""
    )

hpevtMcRendezPalGetFeatFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5685)
)
hpevtMcRendezPalGetFeatFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMcRendezPalGetFeatFail.setStatus(
        ""
    )

hpevtMcRendezPalSetFeatFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5686)
)
hpevtMcRendezPalSetFeatFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMcRendezPalSetFeatFail.setStatus(
        ""
    )

hpevtSalAbiFwError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5692)
)
hpevtSalAbiFwError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSalAbiFwError.setStatus(
        ""
    )

hpevtMemExtLoadOrdErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5696)
)
hpevtMemExtLoadOrdErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemExtLoadOrdErr.setStatus(
        ""
    )

hpevtEfiEsiTableLengthErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5698)
)
hpevtEfiEsiTableLengthErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiEsiTableLengthErr.setStatus(
        ""
    )

hpevtEfiEsiTableChecksumErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5700)
)
hpevtEfiEsiTableChecksumErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiEsiTableChecksumErr.setStatus(
        ""
    )

hpevtEfiEsiTableUnsupportedEntryType = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5701)
)
hpevtEfiEsiTableUnsupportedEntryType.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiEsiTableUnsupportedEntryType.setStatus(
        ""
    )

hpevtEfiGuidTooLarge = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5704)
)
hpevtEfiGuidTooLarge.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiGuidTooLarge.setStatus(
        ""
    )

hpevtEfiHalt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5708)
)
hpevtEfiHalt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiHalt.setStatus(
        ""
    )

hpevtMemChipspareNotSupported = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5711)
)
hpevtMemChipspareNotSupported.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemChipspareNotSupported.setStatus(
        ""
    )

hpevtEfiAssertError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5712)
)
hpevtEfiAssertError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiAssertError.setStatus(
        ""
    )

hpevtEfiEfiBreakpoint = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5713)
)
hpevtEfiEfiBreakpoint.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiEfiBreakpoint.setStatus(
        ""
    )

hpevtEfiHcdHostHung = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5714)
)
hpevtEfiHcdHostHung.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiHcdHostHung.setStatus(
        ""
    )

hpevtEfiSalHandoffVerMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5715)
)
hpevtEfiSalHandoffVerMismatch.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiSalHandoffVerMismatch.setStatus(
        ""
    )

hpevtEfiSalRtcServiceNotInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5717)
)
hpevtEfiSalRtcServiceNotInit.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiSalRtcServiceNotInit.setStatus(
        ""
    )

hpevtEfiSalTimerServiceNotInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5718)
)
hpevtEfiSalTimerServiceNotInit.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiSalTimerServiceNotInit.setStatus(
        ""
    )

hpevtEfiSalStarttimerServiceNotInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5719)
)
hpevtEfiSalStarttimerServiceNotInit.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiSalStarttimerServiceNotInit.setStatus(
        ""
    )

hpevtEfiNoIoPortSpaceRegionFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5720)
)
hpevtEfiNoIoPortSpaceRegionFound.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiNoIoPortSpaceRegionFound.setStatus(
        ""
    )

hpevtEfiBreakpoint = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5721)
)
hpevtEfiBreakpoint.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiBreakpoint.setStatus(
        ""
    )

hpevtEfiSpeedyBootTokenNotRead = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5722)
)
hpevtEfiSpeedyBootTokenNotRead.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiSpeedyBootTokenNotRead.setStatus(
        ""
    )

hpevtEfiSalCallbackAttempted = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5723)
)
hpevtEfiSalCallbackAttempted.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiSalCallbackAttempted.setStatus(
        ""
    )

hpevtEfiSalFreqBaseUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5724)
)
hpevtEfiSalFreqBaseUnknown.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiSalFreqBaseUnknown.setStatus(
        ""
    )

hpevtEfiSysEventAlreadyInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5725)
)
hpevtEfiSysEventAlreadyInit.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiSysEventAlreadyInit.setStatus(
        ""
    )

hpevtEfiSysEventCreateEventFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5726)
)
hpevtEfiSysEventCreateEventFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiSysEventCreateEventFail.setStatus(
        ""
    )

hpevtFpgaNodeInitError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5728)
)
hpevtFpgaNodeInitError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFpgaNodeInitError.setStatus(
        ""
    )

hpevtIoconfigNodeInitError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5729)
)
hpevtIoconfigNodeInitError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoconfigNodeInitError.setStatus(
        ""
    )

hpevtDillonPdhNodeInitError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5730)
)
hpevtDillonPdhNodeInitError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtDillonPdhNodeInitError.setStatus(
        ""
    )

hpevtPdhPropertyError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5731)
)
hpevtPdhPropertyError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdhPropertyError.setStatus(
        ""
    )

hpevtPdhAcpihwNodeError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5732)
)
hpevtPdhAcpihwNodeError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdhAcpihwNodeError.setStatus(
        ""
    )

hpevtPdhIpmiNodeError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5733)
)
hpevtPdhIpmiNodeError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdhIpmiNodeError.setStatus(
        ""
    )

hpevtBootCpusNotCompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5734)
)
hpevtBootCpusNotCompatible.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootCpusNotCompatible.setStatus(
        ""
    )

hpevtBootCacheSizesInconsistant = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5735)
)
hpevtBootCacheSizesInconsistant.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootCacheSizesInconsistant.setStatus(
        ""
    )

hpevtBootSelectingNewMonarch = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5737)
)
hpevtBootSelectingNewMonarch.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootSelectingNewMonarch.setStatus(
        ""
    )

hpevtBootMonSelSteppingsNoEqual = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5738)
)
hpevtBootMonSelSteppingsNoEqual.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootMonSelSteppingsNoEqual.setStatus(
        ""
    )

hpevtBootCpuOverClocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5740)
)
hpevtBootCpuOverClocked.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootCpuOverClocked.setStatus(
        ""
    )

hpevtBootCpuInfoRomAccessError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5741)
)
hpevtBootCpuInfoRomAccessError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootCpuInfoRomAccessError.setStatus(
        ""
    )

hpevtBootPalANotExecuted = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5742)
)
hpevtBootPalANotExecuted.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootPalANotExecuted.setStatus(
        ""
    )

hpevtBootPalBNotExecuted = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5743)
)
hpevtBootPalBNotExecuted.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootPalBNotExecuted.setStatus(
        ""
    )

hpevtBootProtoTypeCpuInstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5744)
)
hpevtBootProtoTypeCpuInstalled.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootProtoTypeCpuInstalled.setStatus(
        ""
    )

hpevtBootFinalRendezWatchdogFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5745)
)
hpevtBootFinalRendezWatchdogFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootFinalRendezWatchdogFail.setStatus(
        ""
    )

hpevtCpuSupplementalTestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5746)
)
hpevtCpuSupplementalTestFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCpuSupplementalTestFailed.setStatus(
        ""
    )

hpevtFabricReadMbeError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5747)
)
hpevtFabricReadMbeError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricReadMbeError.setStatus(
        ""
    )

hpevtFabricUnexpectedStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5749)
)
hpevtFabricUnexpectedStatus.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricUnexpectedStatus.setStatus(
        ""
    )

hpevtEfiSysidBmcWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5750)
)
hpevtEfiSysidBmcWarning.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiSysidBmcWarning.setStatus(
        ""
    )

hpevtEfiSysidBmcReadError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5751)
)
hpevtEfiSysidBmcReadError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiSysidBmcReadError.setStatus(
        ""
    )

hpevtEfiSysidBmcWriteError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5752)
)
hpevtEfiSysidBmcWriteError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiSysidBmcWriteError.setStatus(
        ""
    )

hpevtEfiSysidInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5753)
)
hpevtEfiSysidInvalid.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiSysidInvalid.setStatus(
        ""
    )

hpevtEfiRtIvtEsiTableErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5755)
)
hpevtEfiRtIvtEsiTableErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiRtIvtEsiTableErr.setStatus(
        ""
    )

hpevtEfiRtIvtEsiQueryErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5756)
)
hpevtEfiRtIvtEsiQueryErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiRtIvtEsiQueryErr.setStatus(
        ""
    )

hpevtEfiBootIvtEsiTableErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5757)
)
hpevtEfiBootIvtEsiTableErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiBootIvtEsiTableErr.setStatus(
        ""
    )

hpevtEfiBootIvtEsiQueryErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5758)
)
hpevtEfiBootIvtEsiQueryErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiBootIvtEsiQueryErr.setStatus(
        ""
    )

hpevtUtilitiesParmListTooLarge = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5760)
)
hpevtUtilitiesParmListTooLarge.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUtilitiesParmListTooLarge.setStatus(
        ""
    )

hpevtXbcPortPresenceError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5762)
)
hpevtXbcPortPresenceError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXbcPortPresenceError.setStatus(
        ""
    )

hpevtXbcPortHwLinkError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5763)
)
hpevtXbcPortHwLinkError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXbcPortHwLinkError.setStatus(
        ""
    )

hpevtXbcPortFeError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5764)
)
hpevtXbcPortFeError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXbcPortFeError.setStatus(
        ""
    )

hpevtXinLinkInitError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5766)
)
hpevtXinLinkInitError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXinLinkInitError.setStatus(
        ""
    )

hpevtXinLinkInitFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5767)
)
hpevtXinLinkInitFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXinLinkInitFailed.setStatus(
        ""
    )

hpevtEfiGetMfgModeNotInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5768)
)
hpevtEfiGetMfgModeNotInit.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiGetMfgModeNotInit.setStatus(
        ""
    )

hpevtEfiBmcMfgModeInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5769)
)
hpevtEfiBmcMfgModeInvalid.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiBmcMfgModeInvalid.setStatus(
        ""
    )

hpevtEfiEnterMfgModeNotInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5770)
)
hpevtEfiEnterMfgModeNotInit.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiEnterMfgModeNotInit.setStatus(
        ""
    )

hpevtEfiExitMfgModeNotInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5771)
)
hpevtEfiExitMfgModeNotInit.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiExitMfgModeNotInit.setStatus(
        ""
    )

hpevtEfiTaccessServiceNotInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5772)
)
hpevtEfiTaccessServiceNotInit.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiTaccessServiceNotInit.setStatus(
        ""
    )

hpevtTreeNodeNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5774)
)
hpevtTreeNodeNotFound.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtTreeNodeNotFound.setStatus(
        ""
    )

hpevtEfiSystemStateRunningErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5776)
)
hpevtEfiSystemStateRunningErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiSystemStateRunningErr.setStatus(
        ""
    )

hpevtPalBusConfigIncompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5777)
)
hpevtPalBusConfigIncompatible.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPalBusConfigIncompatible.setStatus(
        ""
    )

hpevtPalGetBusFeaturesFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5778)
)
hpevtPalGetBusFeaturesFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPalGetBusFeaturesFailed.setStatus(
        ""
    )

hpevtMemDimmPairMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5779)
)
hpevtMemDimmPairMismatch.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemDimmPairMismatch.setStatus(
        ""
    )

hpevtEfiPosseLibNotInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5784)
)
hpevtEfiPosseLibNotInit.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiPosseLibNotInit.setStatus(
        ""
    )

hpevtEfiSecurityNotInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5785)
)
hpevtEfiSecurityNotInit.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiSecurityNotInit.setStatus(
        ""
    )

hpevtEfiSecInvalidSysmode = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5786)
)
hpevtEfiSecInvalidSysmode.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiSecInvalidSysmode.setStatus(
        ""
    )

hpevtEfiSecSetPassLevelErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5787)
)
hpevtEfiSecSetPassLevelErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiSecSetPassLevelErr.setStatus(
        ""
    )

hpevtMdtBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5788)
)
hpevtMdtBad.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMdtBad.setStatus(
        ""
    )

hpevtBootCpuBadCoreFixedRatio = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5790)
)
hpevtBootCpuBadCoreFixedRatio.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootCpuBadCoreFixedRatio.setStatus(
        ""
    )

hpevtBootAllCpusSlatedForCompatDeconfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5791)
)
hpevtBootAllCpusSlatedForCompatDeconfig.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootAllCpusSlatedForCompatDeconfig.setStatus(
        ""
    )

hpevtXbcReadRemoteRouteError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5793)
)
hpevtXbcReadRemoteRouteError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXbcReadRemoteRouteError.setStatus(
        ""
    )

hpevtXbcReadNeighborInfoError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5794)
)
hpevtXbcReadNeighborInfoError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXbcReadNeighborInfoError.setStatus(
        ""
    )

hpevtMemDimmQuadMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5795)
)
hpevtMemDimmQuadMismatch.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemDimmQuadMismatch.setStatus(
        ""
    )

hpevtMemDimmFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5796)
)
hpevtMemDimmFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemDimmFailed.setStatus(
        ""
    )

hpevtXbcPortOeError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5797)
)
hpevtXbcPortOeError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXbcPortOeError.setStatus(
        ""
    )

hpevtXbcPortStatusError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5798)
)
hpevtXbcPortStatusError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXbcPortStatusError.setStatus(
        ""
    )

hpevtXbcPortLandmined = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5799)
)
hpevtXbcPortLandmined.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXbcPortLandmined.setStatus(
        ""
    )

hpevtPdIncompatibleCpuSpeeds = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5800)
)
hpevtPdIncompatibleCpuSpeeds.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdIncompatibleCpuSpeeds.setStatus(
        ""
    )

hpevtFabricCellLinkNotInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5802)
)
hpevtFabricCellLinkNotInit.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricCellLinkNotInit.setStatus(
        ""
    )

hpevtFabricInvalidXbcNum = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5803)
)
hpevtFabricInvalidXbcNum.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricInvalidXbcNum.setStatus(
        ""
    )

hpevtFabricInvalidXbcPortNum = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5804)
)
hpevtFabricInvalidXbcPortNum.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricInvalidXbcPortNum.setStatus(
        ""
    )

hpevtUtilitiesLedParamError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5805)
)
hpevtUtilitiesLedParamError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUtilitiesLedParamError.setStatus(
        ""
    )

hpevtFabricUnexpectedNtype = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5806)
)
hpevtFabricUnexpectedNtype.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricUnexpectedNtype.setStatus(
        ""
    )

hpevtFabricPortNotCc = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5807)
)
hpevtFabricPortNotCc.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricPortNotCc.setStatus(
        ""
    )

hpevtFabricPortNotXbc = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5808)
)
hpevtFabricPortNotXbc.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricPortNotXbc.setStatus(
        ""
    )

hpevtFabricUnexpectedNChip = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5809)
)
hpevtFabricUnexpectedNChip.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricUnexpectedNChip.setStatus(
        ""
    )

hpevtFabricUnexpectedNPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5810)
)
hpevtFabricUnexpectedNPort.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricUnexpectedNPort.setStatus(
        ""
    )

hpevtBootNvmWriteToBmcTokenFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5811)
)
hpevtBootNvmWriteToBmcTokenFailure.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootNvmWriteToBmcTokenFailure.setStatus(
        ""
    )

hpevtUtilitiesLedError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5812)
)
hpevtUtilitiesLedError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUtilitiesLedError.setStatus(
        ""
    )

hpevtDuplicateCpuIds = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5813)
)
hpevtDuplicateCpuIds.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtDuplicateCpuIds.setStatus(
        ""
    )

hpevtHp_uxCrashdumpStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5823)
)
hpevtHp_uxCrashdumpStarted.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtHp_uxCrashdumpStarted.setStatus(
        ""
    )

hpevtHp_uxHexFaultCode = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5824)
)
hpevtHp_uxHexFaultCode.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtHp_uxHexFaultCode.setStatus(
        ""
    )

hpevtHp_uxDumpStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5825)
)
hpevtHp_uxDumpStatus.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtHp_uxDumpStatus.setStatus(
        ""
    )

hpevtSettingProcTimeoutFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5827)
)
hpevtSettingProcTimeoutFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSettingProcTimeoutFail.setStatus(
        ""
    )

hpevtEfiSecInitVerifyErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5832)
)
hpevtEfiSecInitVerifyErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiSecInitVerifyErr.setStatus(
        ""
    )

hpevtEfiSecInitCloseErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5833)
)
hpevtEfiSecInitCloseErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiSecInitCloseErr.setStatus(
        ""
    )

hpevtEfiSecInitOpenErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5834)
)
hpevtEfiSecInitOpenErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiSecInitOpenErr.setStatus(
        ""
    )

hpevtEfiSecInitWriteErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5836)
)
hpevtEfiSecInitWriteErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiSecInitWriteErr.setStatus(
        ""
    )

hpevtEfiSecInitWriteDenied = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5837)
)
hpevtEfiSecInitWriteDenied.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiSecInitWriteDenied.setStatus(
        ""
    )

hpevtHp_uxDumpWriteError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5853)
)
hpevtHp_uxDumpWriteError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtHp_uxDumpWriteError.setStatus(
        ""
    )

hpevtErrDeadlockResetDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 5896)
)
hpevtErrDeadlockResetDetected.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtErrDeadlockResetDetected.setStatus(
        ""
    )

hpevtMemParityErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 6002)
)
hpevtMemParityErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemParityErr.setStatus(
        ""
    )

hpevtMemDimmLoadOrdErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 6074)
)
hpevtMemDimmLoadOrdErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemDimmLoadOrdErr.setStatus(
        ""
    )

hpevtMemRefreshStartError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 6146)
)
hpevtMemRefreshStartError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemRefreshStartError.setStatus(
        ""
    )

hpevtMemExtBaseboardIncompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 6180)
)
hpevtMemExtBaseboardIncompatible.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemExtBaseboardIncompatible.setStatus(
        ""
    )

hpevtFabricDifferentTopologies = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 6730)
)
hpevtFabricDifferentTopologies.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricDifferentTopologies.setStatus(
        ""
    )

hpevtFabricInvalidXbc2XbcPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 6795)
)
hpevtFabricInvalidXbc2XbcPort.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricInvalidXbc2XbcPort.setStatus(
        ""
    )

hpevtFabricGetNeighborInfoError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7652)
)
hpevtFabricGetNeighborInfoError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricGetNeighborInfoError.setStatus(
        ""
    )

hpevtXbcRoutingErrorState = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7653)
)
hpevtXbcRoutingErrorState.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXbcRoutingErrorState.setStatus(
        ""
    )

hpevtNoNvmErrLogSpace = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7655)
)
hpevtNoNvmErrLogSpace.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtNoNvmErrLogSpace.setStatus(
        ""
    )

hpevtXbcPortError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7657)
)
hpevtXbcPortError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXbcPortError.setStatus(
        ""
    )

hpevtXbcPortRouteAround = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7658)
)
hpevtXbcPortRouteAround.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXbcPortRouteAround.setStatus(
        ""
    )

hpevtXbcUnexpectedState = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7660)
)
hpevtXbcUnexpectedState.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXbcUnexpectedState.setStatus(
        ""
    )

hpevtXbcRoutingStateTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7661)
)
hpevtXbcRoutingStateTimeout.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXbcRoutingStateTimeout.setStatus(
        ""
    )

hpevtXbcNeighborPortNotRoutable = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7663)
)
hpevtXbcNeighborPortNotRoutable.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXbcNeighborPortNotRoutable.setStatus(
        ""
    )

hpevtFabricCcToXbcError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7664)
)
hpevtFabricCcToXbcError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricCcToXbcError.setStatus(
        ""
    )

hpevtFabricRouteXbcError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7666)
)
hpevtFabricRouteXbcError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricRouteXbcError.setStatus(
        ""
    )

hpevtFabricMaxBrokenLinks = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7667)
)
hpevtFabricMaxBrokenLinks.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricMaxBrokenLinks.setStatus(
        ""
    )

hpevtXbcSemaphoreTakeoverFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7669)
)
hpevtXbcSemaphoreTakeoverFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXbcSemaphoreTakeoverFailed.setStatus(
        ""
    )

hpevtXbcForceUnlockSm4Timeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7671)
)
hpevtXbcForceUnlockSm4Timeout.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXbcForceUnlockSm4Timeout.setStatus(
        ""
    )

hpevtXbcGetGlobalSm4Timeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7673)
)
hpevtXbcGetGlobalSm4Timeout.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXbcGetGlobalSm4Timeout.setStatus(
        ""
    )

hpevtXbcReleaseSm4Timeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7674)
)
hpevtXbcReleaseSm4Timeout.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXbcReleaseSm4Timeout.setStatus(
        ""
    )

hpevtMpBatteryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7684)
)
hpevtMpBatteryFailure.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMpBatteryFailure.setStatus(
        ""
    )

hpevtMpSoftwareError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7685)
)
hpevtMpSoftwareError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMpSoftwareError.setStatus(
        ""
    )

hpevtMpI2cCommError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7686)
)
hpevtMpI2cCommError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMpI2cCommError.setStatus(
        ""
    )

hpevtRomCrcError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7690)
)
hpevtRomCrcError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtRomCrcError.setStatus(
        ""
    )

hpevtIoIdentifyIoBpFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7718)
)
hpevtIoIdentifyIoBpFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoIdentifyIoBpFailed.setStatus(
        ""
    )

hpevtCpuRevisionMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7732)
)
hpevtCpuRevisionMismatch.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCpuRevisionMismatch.setStatus(
        ""
    )

hpevtCpuFreqMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7733)
)
hpevtCpuFreqMismatch.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCpuFreqMismatch.setStatus(
        ""
    )

hpevtCpuOverclocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7734)
)
hpevtCpuOverclocked.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCpuOverclocked.setStatus(
        ""
    )

hpevtCmplxProfilIncoherent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7758)
)
hpevtCmplxProfilIncoherent.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCmplxProfilIncoherent.setStatus(
        ""
    )

hpevtDuplicateCabinet = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7760)
)
hpevtDuplicateCabinet.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtDuplicateCabinet.setStatus(
        ""
    )

hpevtIdCommandRequired = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7767)
)
hpevtIdCommandRequired.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIdCommandRequired.setStatus(
        ""
    )

hpevtNvramBatteryFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7771)
)
hpevtNvramBatteryFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtNvramBatteryFail.setStatus(
        ""
    )

hpevtPartitionTimeoutReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7773)
)
hpevtPartitionTimeoutReset.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPartitionTimeoutReset.setStatus(
        ""
    )

hpevtPdhcWatchdogTimedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7774)
)
hpevtPdhcWatchdogTimedOut.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdhcWatchdogTimedOut.setStatus(
        ""
    )

hpevtAbortPowerupOth = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7781)
)
hpevtAbortPowerupOth.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtAbortPowerupOth.setStatus(
        ""
    )

hpevtAbortPwrupBps = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7782)
)
hpevtAbortPwrupBps.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtAbortPwrupBps.setStatus(
        ""
    )

hpevtAbortStartBlowr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7783)
)
hpevtAbortStartBlowr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtAbortStartBlowr.setStatus(
        ""
    )

hpevtAbortStartIofan = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7784)
)
hpevtAbortStartIofan.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtAbortStartIofan.setStatus(
        ""
    )

hpevtAcDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7786)
)
hpevtAcDeleted.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtAcDeleted.setStatus(
        ""
    )

hpevtBlowrFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7791)
)
hpevtBlowrFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBlowrFail.setStatus(
        ""
    )

hpevtBpsFail48flt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7793)
)
hpevtBpsFail48flt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBpsFail48flt.setStatus(
        ""
    )

hpevtBpsFailFanflt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7795)
)
hpevtBpsFailFanflt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBpsFailFanflt.setStatus(
        ""
    )

hpevtBpsFailOt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7796)
)
hpevtBpsFailOt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBpsFailOt.setStatus(
        ""
    )

hpevtBpsNotRedundant = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7798)
)
hpevtBpsNotRedundant.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBpsNotRedundant.setStatus(
        ""
    )

hpevtBpsOvervoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7799)
)
hpevtBpsOvervoltage.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBpsOvervoltage.setStatus(
        ""
    )

hpevtBpsUndervoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7803)
)
hpevtBpsUndervoltage.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBpsUndervoltage.setStatus(
        ""
    )

hpevtCabFanFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7806)
)
hpevtCabFanFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCabFanFail.setStatus(
        ""
    )

hpevtHkpOvervoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7822)
)
hpevtHkpOvervoltage.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtHkpOvervoltage.setStatus(
        ""
    )

hpevtHkpUndervoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7823)
)
hpevtHkpUndervoltage.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtHkpUndervoltage.setStatus(
        ""
    )

hpevtIllegalBpsCfgOrPhaseFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7824)
)
hpevtIllegalBpsCfgOrPhaseFlt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIllegalBpsCfgOrPhaseFlt.setStatus(
        ""
    )

hpevtIllegalBpsid = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7825)
)
hpevtIllegalBpsid.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIllegalBpsid.setStatus(
        ""
    )

hpevtInletOvertempHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7827)
)
hpevtInletOvertempHi.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtInletOvertempHi.setStatus(
        ""
    )

hpevtInletOvertempLo = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7828)
)
hpevtInletOvertempLo.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtInletOvertempLo.setStatus(
        ""
    )

hpevtInletOvertempMid = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7829)
)
hpevtInletOvertempMid.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtInletOvertempMid.setStatus(
        ""
    )

hpevtIofanFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7836)
)
hpevtIofanFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIofanFail.setStatus(
        ""
    )

hpevtPowerOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7842)
)
hpevtPowerOverload.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPowerOverload.setStatus(
        ""
    )

hpevtShutdownBlowr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7845)
)
hpevtShutdownBlowr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtShutdownBlowr.setStatus(
        ""
    )

hpevtShutdownIofan = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7846)
)
hpevtShutdownIofan.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtShutdownIofan.setStatus(
        ""
    )

hpevtXucFanFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7849)
)
hpevtXucFanFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXucFanFail.setStatus(
        ""
    )

hpevtCluWatchdogReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7855)
)
hpevtCluWatchdogReset.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCluWatchdogReset.setStatus(
        ""
    )

hpevtEepromInvalidCksm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7856)
)
hpevtEepromInvalidCksm.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEepromInvalidCksm.setStatus(
        ""
    )

hpevtHbpbBoardPowerFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7858)
)
hpevtHbpbBoardPowerFault.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtHbpbBoardPowerFault.setStatus(
        ""
    )

hpevtHiobEepromRdFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7863)
)
hpevtHiobEepromRdFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtHiobEepromRdFail.setStatus(
        ""
    )

hpevtHiopbEepromRdFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7864)
)
hpevtHiopbEepromRdFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtHiopbEepromRdFail.setStatus(
        ""
    )

hpevtHiopbLpmFltRdFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7865)
)
hpevtHiopbLpmFltRdFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtHiopbLpmFltRdFail.setStatus(
        ""
    )

hpevtHiopbOvertemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7866)
)
hpevtHiopbOvertemp.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtHiopbOvertemp.setStatus(
        ""
    )

hpevtHiopbPowerFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7867)
)
hpevtHiopbPowerFault.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtHiopbPowerFault.setStatus(
        ""
    )

hpevtHiopbVoltMrgnFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7871)
)
hpevtHiopbVoltMrgnFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtHiopbVoltMrgnFail.setStatus(
        ""
    )

hpevtSbchEepromRdFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7873)
)
hpevtSbchEepromRdFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSbchEepromRdFail.setStatus(
        ""
    )

hpevtUguyEepromRdFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7874)
)
hpevtUguyEepromRdFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUguyEepromRdFail.setStatus(
        ""
    )

hpevtSysBkpEepromRdFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7875)
)
hpevtSysBkpEepromRdFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSysBkpEepromRdFail.setStatus(
        ""
    )

hpevtSysBkpI2cRdFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7877)
)
hpevtSysBkpI2cRdFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSysBkpI2cRdFail.setStatus(
        ""
    )

hpevtSysBkpI2cWrFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7878)
)
hpevtSysBkpI2cWrFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSysBkpI2cWrFail.setStatus(
        ""
    )

hpevtSysBkpPowerFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7879)
)
hpevtSysBkpPowerFault.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSysBkpPowerFault.setStatus(
        ""
    )

hpevtSysBkpVoltMrgnFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7880)
)
hpevtSysBkpVoltMrgnFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSysBkpVoltMrgnFail.setStatus(
        ""
    )

hpevtWriteFruDataFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7891)
)
hpevtWriteFruDataFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtWriteFruDataFail.setStatus(
        ""
    )

hpevtCpuFanFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7892)
)
hpevtCpuFanFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCpuFanFail.setStatus(
        ""
    )

hpevtCpuFanSlow = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7893)
)
hpevtCpuFanSlow.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCpuFanSlow.setStatus(
        ""
    )

hpevtDnaFanFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7894)
)
hpevtDnaFanFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtDnaFanFail.setStatus(
        ""
    )

hpevtDnaFanSlow = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7895)
)
hpevtDnaFanSlow.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtDnaFanSlow.setStatus(
        ""
    )

hpevtPdhcToSysfwRevMismtch = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7896)
)
hpevtPdhcToSysfwRevMismtch.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdhcToSysfwRevMismtch.setStatus(
        ""
    )

hpevtPdhCtrlrFwMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7902)
)
hpevtPdhCtrlrFwMismatch.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdhCtrlrFwMismatch.setStatus(
        ""
    )

hpevtCellPowerFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7903)
)
hpevtCellPowerFault.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCellPowerFault.setStatus(
        ""
    )

hpevtCpuInitNodeError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7938)
)
hpevtCpuInitNodeError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCpuInitNodeError.setStatus(
        ""
    )

hpevtCpuExecuteCmdError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7939)
)
hpevtCpuExecuteCmdError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCpuExecuteCmdError.setStatus(
        ""
    )

hpevtCpuCmdStateInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7940)
)
hpevtCpuCmdStateInvalid.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCpuCmdStateInvalid.setStatus(
        ""
    )

hpevtCpuPalProcError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7948)
)
hpevtCpuPalProcError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCpuPalProcError.setStatus(
        ""
    )

hpevtBootCpuLoadingError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7953)
)
hpevtBootCpuLoadingError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootCpuLoadingError.setStatus(
        ""
    )

hpevtXbcPersistantError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7963)
)
hpevtXbcPersistantError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXbcPersistantError.setStatus(
        ""
    )

hpevtXbcLinkTestError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7964)
)
hpevtXbcLinkTestError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXbcLinkTestError.setStatus(
        ""
    )

hpevtPltfrmStorageReadErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7965)
)
hpevtPltfrmStorageReadErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPltfrmStorageReadErr.setStatus(
        ""
    )

hpevtPltfrmStorageWriteErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7966)
)
hpevtPltfrmStorageWriteErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPltfrmStorageWriteErr.setStatus(
        ""
    )

hpevtTreeNodeErrorSequencer = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7973)
)
hpevtTreeNodeErrorSequencer.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtTreeNodeErrorSequencer.setStatus(
        ""
    )

hpevtPartitionVariableError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7974)
)
hpevtPartitionVariableError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPartitionVariableError.setStatus(
        ""
    )

hpevtCellRedundtPowerFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 7975)
)
hpevtCellRedundtPowerFault.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCellRedundtPowerFault.setStatus(
        ""
    )

hpevtPalProcConfigIncompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8009)
)
hpevtPalProcConfigIncompatible.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPalProcConfigIncompatible.setStatus(
        ""
    )

hpevtPalGetProcFeaturesFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8010)
)
hpevtPalGetProcFeaturesFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPalGetProcFeaturesFailed.setStatus(
        ""
    )

hpevtPdhcCriticalDebug = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8127)
)
hpevtPdhcCriticalDebug.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdhcCriticalDebug.setStatus(
        ""
    )

hpevtCluUndefinedCase = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8128)
)
hpevtCluUndefinedCase.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCluUndefinedCase.setStatus(
        ""
    )

hpevtCellVoltageMarginUnkn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8130)
)
hpevtCellVoltageMarginUnkn.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCellVoltageMarginUnkn.setStatus(
        ""
    )

hpevtPdhcAssertionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8131)
)
hpevtPdhcAssertionFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdhcAssertionFailed.setStatus(
        ""
    )

hpevtPdhcFirmwareUnknownErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8132)
)
hpevtPdhcFirmwareUnknownErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdhcFirmwareUnknownErr.setStatus(
        ""
    )

hpevtPdhcI2cWriteFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8133)
)
hpevtPdhcI2cWriteFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdhcI2cWriteFailed.setStatus(
        ""
    )

hpevtPdhcI2cReadFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8134)
)
hpevtPdhcI2cReadFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdhcI2cReadFailed.setStatus(
        ""
    )

hpevtPdhcSmbusWriteFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8135)
)
hpevtPdhcSmbusWriteFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdhcSmbusWriteFailed.setStatus(
        ""
    )

hpevtPdhcSmbusReadFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8136)
)
hpevtPdhcSmbusReadFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdhcSmbusReadFailed.setStatus(
        ""
    )

hpevtFrequencyProgramFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8137)
)
hpevtFrequencyProgramFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFrequencyProgramFailed.setStatus(
        ""
    )

hpevtSysFwFlashUpdateError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8138)
)
hpevtSysFwFlashUpdateError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSysFwFlashUpdateError.setStatus(
        ""
    )

hpevtPdhcUnexpectedReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8139)
)
hpevtPdhcUnexpectedReset.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdhcUnexpectedReset.setStatus(
        ""
    )

hpevtCpuTmpSensorSetupFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8140)
)
hpevtCpuTmpSensorSetupFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCpuTmpSensorSetupFail.setStatus(
        ""
    )

hpevtCpuModuleThermalert = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8141)
)
hpevtCpuModuleThermalert.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCpuModuleThermalert.setStatus(
        ""
    )

hpevtPdhcFlashUpdateError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8143)
)
hpevtPdhcFlashUpdateError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdhcFlashUpdateError.setStatus(
        ""
    )

hpevtCellTypMismatchWSysfw = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8147)
)
hpevtCellTypMismatchWSysfw.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCellTypMismatchWSysfw.setStatus(
        ""
    )

hpevtPdhcPdhArbiterTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8149)
)
hpevtPdhcPdhArbiterTimeout.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdhcPdhArbiterTimeout.setStatus(
        ""
    )

hpevtPdhcGetSm4Timeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8151)
)
hpevtPdhcGetSm4Timeout.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdhcGetSm4Timeout.setStatus(
        ""
    )

hpevtIpmiBmc2hostMsgFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8153)
)
hpevtIpmiBmc2hostMsgFailure.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIpmiBmc2hostMsgFailure.setStatus(
        ""
    )

hpevtEfiDebugLevelTokenErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8154)
)
hpevtEfiDebugLevelTokenErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEfiDebugLevelTokenErr.setStatus(
        ""
    )

hpevtXbcPortNotLandmined = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8156)
)
hpevtXbcPortNotLandmined.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXbcPortNotLandmined.setStatus(
        ""
    )

hpevtFabricValidateError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8159)
)
hpevtFabricValidateError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricValidateError.setStatus(
        ""
    )

hpevtFabricISRInvalidBkp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8184)
)
hpevtFabricISRInvalidBkp.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricISRInvalidBkp.setStatus(
        ""
    )

hpevtFabricXinWrZeroErrMaskError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8186)
)
hpevtFabricXinWrZeroErrMaskError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricXinWrZeroErrMaskError.setStatus(
        ""
    )

hpevtFabricCcPriModeRegRdStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8187)
)
hpevtFabricCcPriModeRegRdStatus.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricCcPriModeRegRdStatus.setStatus(
        ""
    )

hpevtFabricCcPriModeRegRdData = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8188)
)
hpevtFabricCcPriModeRegRdData.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricCcPriModeRegRdData.setStatus(
        ""
    )

hpevtFabricCcErrMaskRegRdStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8189)
)
hpevtFabricCcErrMaskRegRdStatus.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricCcErrMaskRegRdStatus.setStatus(
        ""
    )

hpevtFabricCcErrMaskRegRdData = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8190)
)
hpevtFabricCcErrMaskRegRdData.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricCcErrMaskRegRdData.setStatus(
        ""
    )

hpevtFabricXingNeighborPortBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8194)
)
hpevtFabricXingNeighborPortBad.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricXingNeighborPortBad.setStatus(
        ""
    )

hpevtFabricISRRdFwdProgErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8195)
)
hpevtFabricISRRdFwdProgErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricISRRdFwdProgErr.setStatus(
        ""
    )

hpevtFabricGetNeighborMaxLinksBroken = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8198)
)
hpevtFabricGetNeighborMaxLinksBroken.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricGetNeighborMaxLinksBroken.setStatus(
        ""
    )

hpevtPmAssertionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8199)
)
hpevtPmAssertionFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPmAssertionFailed.setStatus(
        ""
    )

hpevtPmFirmwareUnknownErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8200)
)
hpevtPmFirmwareUnknownErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPmFirmwareUnknownErr.setStatus(
        ""
    )

hpevtPmCriticalDebug = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8202)
)
hpevtPmCriticalDebug.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPmCriticalDebug.setStatus(
        ""
    )

hpevtFabricLinkCorErrTestFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8205)
)
hpevtFabricLinkCorErrTestFailure.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricLinkCorErrTestFailure.setStatus(
        ""
    )

hpevtInvalidCabinetNumber = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8206)
)
hpevtInvalidCabinetNumber.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtInvalidCabinetNumber.setStatus(
        ""
    )

hpevtPdIncompatibleFwRevs = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8207)
)
hpevtPdIncompatibleFwRevs.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdIncompatibleFwRevs.setStatus(
        ""
    )

hpevtPmI2cWriteFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8212)
)
hpevtPmI2cWriteFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPmI2cWriteFailed.setStatus(
        ""
    )

hpevtPmI2cReadFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8214)
)
hpevtPmI2cReadFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPmI2cReadFailed.setStatus(
        ""
    )

hpevtCellInfoError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8216)
)
hpevtCellInfoError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCellInfoError.setStatus(
        ""
    )

hpevtSlaveConsoleSetupError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8218)
)
hpevtSlaveConsoleSetupError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSlaveConsoleSetupError.setStatus(
        ""
    )

hpevtRegistryMoveToCoreCellError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8219)
)
hpevtRegistryMoveToCoreCellError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtRegistryMoveToCoreCellError.setStatus(
        ""
    )

hpevtProfileGroupCCrcError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8220)
)
hpevtProfileGroupCCrcError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtProfileGroupCCrcError.setStatus(
        ""
    )

hpevtMcCoreCellSelectFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8238)
)
hpevtMcCoreCellSelectFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMcCoreCellSelectFail.setStatus(
        ""
    )

hpevtFabricAssertFabricUtils = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8239)
)
hpevtFabricAssertFabricUtils.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricAssertFabricUtils.setStatus(
        ""
    )

hpevtSalPmiFwError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8240)
)
hpevtSalPmiFwError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSalPmiFwError.setStatus(
        ""
    )

hpevtOlaWrongNumberCells = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8243)
)
hpevtOlaWrongNumberCells.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtOlaWrongNumberCells.setStatus(
        ""
    )

hpevtFabricXbcRouteSourceCellPortErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8257)
)
hpevtFabricXbcRouteSourceCellPortErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricXbcRouteSourceCellPortErr.setStatus(
        ""
    )

hpevtBootOlaCellIncompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8261)
)
hpevtBootOlaCellIncompatible.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootOlaCellIncompatible.setStatus(
        ""
    )

hpevtBootOlaCellDidNotReachRendezvous = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8263)
)
hpevtBootOlaCellDidNotReachRendezvous.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootOlaCellDidNotReachRendezvous.setStatus(
        ""
    )

hpevtBootOlaCellStillAtBib = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8264)
)
hpevtBootOlaCellStillAtBib.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootOlaCellStillAtBib.setStatus(
        ""
    )

hpevtBootOlaCellUnexpectedCellState = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8265)
)
hpevtBootOlaCellUnexpectedCellState.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootOlaCellUnexpectedCellState.setStatus(
        ""
    )

hpevtBootOlaCellCantReachAliveCells = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8267)
)
hpevtBootOlaCellCantReachAliveCells.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootOlaCellCantReachAliveCells.setStatus(
        ""
    )

hpevtBootMixedCpuCoreFreqInstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8269)
)
hpevtBootMixedCpuCoreFreqInstalled.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootMixedCpuCoreFreqInstalled.setStatus(
        ""
    )

hpevtXinInitIntermittentFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8271)
)
hpevtXinInitIntermittentFailure.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXinInitIntermittentFailure.setStatus(
        ""
    )

hpevtPdhErrClearOlaSteeringBit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8643)
)
hpevtPdhErrClearOlaSteeringBit.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdhErrClearOlaSteeringBit.setStatus(
        ""
    )

hpevtBootOlaFailedUpdatePdAddrMap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8645)
)
hpevtBootOlaFailedUpdatePdAddrMap.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootOlaFailedUpdatePdAddrMap.setStatus(
        ""
    )

hpevtBootOlaFailedUpdatePdPdt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8646)
)
hpevtBootOlaFailedUpdatePdPdt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootOlaFailedUpdatePdPdt.setStatus(
        ""
    )

hpevtBootOlaFailedUpdateCellMap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8647)
)
hpevtBootOlaFailedUpdateCellMap.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootOlaFailedUpdateCellMap.setStatus(
        ""
    )

hpevtFabricCc2XbcLinkInitFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8648)
)
hpevtFabricCc2XbcLinkInitFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricCc2XbcLinkInitFailed.setStatus(
        ""
    )

hpevtFwVirtualMappingError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8652)
)
hpevtFwVirtualMappingError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFwVirtualMappingError.setStatus(
        ""
    )

hpevtFabricXinInitWriteErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8676)
)
hpevtFabricXinInitWriteErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricXinInitWriteErr.setStatus(
        ""
    )

hpevtFabricXinInitReadErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8677)
)
hpevtFabricXinInitReadErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricXinInitReadErr.setStatus(
        ""
    )

hpevtFabricLinkInitIntermittentFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8679)
)
hpevtFabricLinkInitIntermittentFailure.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricLinkInitIntermittentFailure.setStatus(
        ""
    )

hpevtIodiscPciInitnodeError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8690)
)
hpevtIodiscPciInitnodeError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIodiscPciInitnodeError.setStatus(
        ""
    )

hpevtIodiscPciBusscanError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8691)
)
hpevtIodiscPciBusscanError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIodiscPciBusscanError.setStatus(
        ""
    )

hpevtIodiscPciInitbridgeError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8692)
)
hpevtIodiscPciInitbridgeError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIodiscPciInitbridgeError.setStatus(
        ""
    )

hpevtIodiscPciIomapError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8693)
)
hpevtIodiscPciIomapError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIodiscPciIomapError.setStatus(
        ""
    )

hpevtIodiscPciMmiomapError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8694)
)
hpevtIodiscPciMmiomapError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIodiscPciMmiomapError.setStatus(
        ""
    )

hpevtIodiscSbaInitnodeError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8709)
)
hpevtIodiscSbaInitnodeError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIodiscSbaInitnodeError.setStatus(
        ""
    )

hpevtIodiscSbaDiscoverError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8710)
)
hpevtIodiscSbaDiscoverError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIodiscSbaDiscoverError.setStatus(
        ""
    )

hpevtIodiscSbaResetError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8711)
)
hpevtIodiscSbaResetError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIodiscSbaResetError.setStatus(
        ""
    )

hpevtIodiscIolinkError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8712)
)
hpevtIodiscIolinkError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIodiscIolinkError.setStatus(
        ""
    )

hpevtIodiscCableError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8713)
)
hpevtIodiscCableError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIodiscCableError.setStatus(
        ""
    )

hpevtIodiscIoChassisPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8714)
)
hpevtIodiscIoChassisPower.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIodiscIoChassisPower.setStatus(
        ""
    )

hpevtIodiscLbaInitnodeError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8715)
)
hpevtIodiscLbaInitnodeError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIodiscLbaInitnodeError.setStatus(
        ""
    )

hpevtIodiscLbaWidthError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8716)
)
hpevtIodiscLbaWidthError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIodiscLbaWidthError.setStatus(
        ""
    )

hpevtIodiscLbaPhaseError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8717)
)
hpevtIodiscLbaPhaseError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIodiscLbaPhaseError.setStatus(
        ""
    )

hpevtIodiscLbaClearError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8718)
)
hpevtIodiscLbaClearError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIodiscLbaClearError.setStatus(
        ""
    )

hpevtIodiscLbaLogError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8719)
)
hpevtIodiscLbaLogError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIodiscLbaLogError.setStatus(
        ""
    )

hpevtIodiscLbaDiscoverError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8720)
)
hpevtIodiscLbaDiscoverError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIodiscLbaDiscoverError.setStatus(
        ""
    )

hpevtIodiscLbaConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8721)
)
hpevtIodiscLbaConfigError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIodiscLbaConfigError.setStatus(
        ""
    )

hpevtIodiscLbaPciscanError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8722)
)
hpevtIodiscLbaPciscanError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIodiscLbaPciscanError.setStatus(
        ""
    )

hpevtIodiscLbaPciconfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8723)
)
hpevtIodiscLbaPciconfigError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIodiscLbaPciconfigError.setStatus(
        ""
    )

hpevtBootOlaCellErrAccessCmplxProfile = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8745)
)
hpevtBootOlaCellErrAccessCmplxProfile.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootOlaCellErrAccessCmplxProfile.setStatus(
        ""
    )

hpevtBootFwRelocMemErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8747)
)
hpevtBootFwRelocMemErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootFwRelocMemErr.setStatus(
        ""
    )

hpevtBootOlaCellNotConfigInCmplxProfile = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8752)
)
hpevtBootOlaCellNotConfigInCmplxProfile.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootOlaCellNotConfigInCmplxProfile.setStatus(
        ""
    )

hpevtOptsNvmAllocError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8756)
)
hpevtOptsNvmAllocError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtOptsNvmAllocError.setStatus(
        ""
    )

hpevtBootOlaUpdateRtcFailedOlaCell = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8757)
)
hpevtBootOlaUpdateRtcFailedOlaCell.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootOlaUpdateRtcFailedOlaCell.setStatus(
        ""
    )

hpevtSalInfoTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8758)
)
hpevtSalInfoTimeout.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSalInfoTimeout.setStatus(
        ""
    )

hpevtPdhIprNotClearedOnCell = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8761)
)
hpevtPdhIprNotClearedOnCell.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdhIprNotClearedOnCell.setStatus(
        ""
    )

hpevtPdhIprClearAttempts = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8762)
)
hpevtPdhIprClearAttempts.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdhIprClearAttempts.setStatus(
        ""
    )

hpevtBootOlaUpdateRtcFailedExistingCell = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8763)
)
hpevtBootOlaUpdateRtcFailedExistingCell.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootOlaUpdateRtcFailedExistingCell.setStatus(
        ""
    )

hpevtMemIncompleteEchelon = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8768)
)
hpevtMemIncompleteEchelon.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemIncompleteEchelon.setStatus(
        ""
    )

hpevtFabricRdPortStatePortInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8771)
)
hpevtFabricRdPortStatePortInvalid.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricRdPortStatePortInvalid.setStatus(
        ""
    )

hpevtFabricWrPortStatePortInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8772)
)
hpevtFabricWrPortStatePortInvalid.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricWrPortStatePortInvalid.setStatus(
        ""
    )

hpevtMainBpLpmFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8784)
)
hpevtMainBpLpmFlt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMainBpLpmFlt.setStatus(
        ""
    )

hpevtIoBpLpmFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8787)
)
hpevtIoBpLpmFlt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoBpLpmFlt.setStatus(
        ""
    )

hpevtCmplxProfileInitFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8797)
)
hpevtCmplxProfileInitFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCmplxProfileInitFailed.setStatus(
        ""
    )

hpevtPalSetProcFeaturesFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8798)
)
hpevtPalSetProcFeaturesFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPalSetProcFeaturesFailed.setStatus(
        ""
    )

hpevtActiveLogNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8806)
)
hpevtActiveLogNotFound.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtActiveLogNotFound.setStatus(
        ""
    )

hpevtReachedMaxErrorLogs = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8807)
)
hpevtReachedMaxErrorLogs.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtReachedMaxErrorLogs.setStatus(
        ""
    )

hpevtOldNoCellToDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8814)
)
hpevtOldNoCellToDelete.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtOldNoCellToDelete.setStatus(
        ""
    )

hpevtBpsOvercurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8817)
)
hpevtBpsOvercurrent.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBpsOvercurrent.setStatus(
        ""
    )

hpevtBpsWarnOt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8818)
)
hpevtBpsWarnOt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBpsWarnOt.setStatus(
        ""
    )

hpevtErmOutOfHeap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8819)
)
hpevtErmOutOfHeap.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtErmOutOfHeap.setStatus(
        ""
    )

hpevtMemDimmUnsupported = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8821)
)
hpevtMemDimmUnsupported.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemDimmUnsupported.setStatus(
        ""
    )

hpevtOptsMallocError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8828)
)
hpevtOptsMallocError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtOptsMallocError.setStatus(
        ""
    )

hpevtCellHwDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8837)
)
hpevtCellHwDegraded.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCellHwDegraded.setStatus(
        ""
    )

hpevtNotIntegratingCell = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8839)
)
hpevtNotIntegratingCell.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtNotIntegratingCell.setStatus(
        ""
    )

hpevtIoContextCorruptErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8842)
)
hpevtIoContextCorruptErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoContextCorruptErr.setStatus(
        ""
    )

hpevtIoRopeFatal = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8843)
)
hpevtIoRopeFatal.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoRopeFatal.setStatus(
        ""
    )

hpevtIoBusFatal = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8844)
)
hpevtIoBusFatal.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoBusFatal.setStatus(
        ""
    )

hpevtIoRopeUnitFatal = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8845)
)
hpevtIoRopeUnitFatal.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoRopeUnitFatal.setStatus(
        ""
    )

hpevtPdhFlashWriteEnableBitSetNowCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8851)
)
hpevtPdhFlashWriteEnableBitSetNowCleared.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdhFlashWriteEnableBitSetNowCleared.setStatus(
        ""
    )

hpevtFirmwareInitError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8855)
)
hpevtFirmwareInitError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFirmwareInitError.setStatus(
        ""
    )

hpevtMcIncompleteCpuSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8857)
)
hpevtMcIncompleteCpuSet.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMcIncompleteCpuSet.setStatus(
        ""
    )

hpevtMcIncompleteCellSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8858)
)
hpevtMcIncompleteCellSet.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMcIncompleteCellSet.setStatus(
        ""
    )

hpevtMcTreeCheckFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8859)
)
hpevtMcTreeCheckFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMcTreeCheckFailed.setStatus(
        ""
    )

hpevtMcRegistryCheckFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8860)
)
hpevtMcRegistryCheckFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMcRegistryCheckFailed.setStatus(
        ""
    )

hpevtMcDuringOsMca = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8861)
)
hpevtMcDuringOsMca.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMcDuringOsMca.setStatus(
        ""
    )

hpevtMcMemDumpAbandon = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8864)
)
hpevtMcMemDumpAbandon.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMcMemDumpAbandon.setStatus(
        ""
    )

hpevtMcFwTreeNotComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8865)
)
hpevtMcFwTreeNotComplete.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMcFwTreeNotComplete.setStatus(
        ""
    )

hpevtAcpiConfigMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8872)
)
hpevtAcpiConfigMismatch.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtAcpiConfigMismatch.setStatus(
        ""
    )

hpevtFabricXinErrOrderStatusClrFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8873)
)
hpevtFabricXinErrOrderStatusClrFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricXinErrOrderStatusClrFailed.setStatus(
        ""
    )

hpevtFabricAssertFabricInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8876)
)
hpevtFabricAssertFabricInit.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricAssertFabricInit.setStatus(
        ""
    )

hpevtInvalidPiromData = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8877)
)
hpevtInvalidPiromData.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtInvalidPiromData.setStatus(
        ""
    )

hpevtSettingFreqRatiosError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8882)
)
hpevtSettingFreqRatiosError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSettingFreqRatiosError.setStatus(
        ""
    )

hpevtOptsBlockCksumError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8883)
)
hpevtOptsBlockCksumError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtOptsBlockCksumError.setStatus(
        ""
    )

hpevtFabricColaLocalCcLinkNotInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8894)
)
hpevtFabricColaLocalCcLinkNotInit.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricColaLocalCcLinkNotInit.setStatus(
        ""
    )

hpevtFabricXinInitDisableWrError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8895)
)
hpevtFabricXinInitDisableWrError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricXinInitDisableWrError.setStatus(
        ""
    )

hpevtFabricXinErrMaskUnknownBkp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8896)
)
hpevtFabricXinErrMaskUnknownBkp.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricXinErrMaskUnknownBkp.setStatus(
        ""
    )

hpevtFabricXinWrErrMaskError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8897)
)
hpevtFabricXinWrErrMaskError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricXinWrErrMaskError.setStatus(
        ""
    )

hpevtFabricXinRdErrMaskError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8898)
)
hpevtFabricXinRdErrMaskError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricXinRdErrMaskError.setStatus(
        ""
    )

hpevtFabricInitCcLinkFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8900)
)
hpevtFabricInitCcLinkFailure.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricInitCcLinkFailure.setStatus(
        ""
    )

hpevtResetCommandError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8906)
)
hpevtResetCommandError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtResetCommandError.setStatus(
        ""
    )

hpevtFabricInitCcLinkDisableErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8926)
)
hpevtFabricInitCcLinkDisableErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricInitCcLinkDisableErr.setStatus(
        ""
    )

hpevtFabricSetPortStateGetSm4Err = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8930)
)
hpevtFabricSetPortStateGetSm4Err.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricSetPortStateGetSm4Err.setStatus(
        ""
    )

hpevtFabricSetPortStateRlsSm4Err = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8931)
)
hpevtFabricSetPortStateRlsSm4Err.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricSetPortStateRlsSm4Err.setStatus(
        ""
    )

hpevtFabricAssertFabricErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8936)
)
hpevtFabricAssertFabricErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricAssertFabricErr.setStatus(
        ""
    )

hpevtFabricXinLinkAlreadyInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8939)
)
hpevtFabricXinLinkAlreadyInit.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricXinLinkAlreadyInit.setStatus(
        ""
    )

hpevtNoCpuModulesFoundByPdhc = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8940)
)
hpevtNoCpuModulesFoundByPdhc.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtNoCpuModulesFoundByPdhc.setStatus(
        ""
    )

hpevtCpuModCompatMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8941)
)
hpevtCpuModCompatMismatch.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCpuModCompatMismatch.setStatus(
        ""
    )

hpevtBadCpuModScratchCksum = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8942)
)
hpevtBadCpuModScratchCksum.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBadCpuModScratchCksum.setStatus(
        ""
    )

hpevtPdhBatteryLowWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8954)
)
hpevtPdhBatteryLowWarning.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdhBatteryLowWarning.setStatus(
        ""
    )

hpevtFabricRouteXbcCopyRoutingErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8959)
)
hpevtFabricRouteXbcCopyRoutingErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricRouteXbcCopyRoutingErr.setStatus(
        ""
    )

hpevtFabricCopyRdBackFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8960)
)
hpevtFabricCopyRdBackFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricCopyRdBackFailed.setStatus(
        ""
    )

hpevtFabricRtgCompleteSm4RlsErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8962)
)
hpevtFabricRtgCompleteSm4RlsErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricRtgCompleteSm4RlsErr.setStatus(
        ""
    )

hpevtFabricRtgCompleteWrFwdPrgErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8964)
)
hpevtFabricRtgCompleteWrFwdPrgErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricRtgCompleteWrFwdPrgErr.setStatus(
        ""
    )

hpevtFabricRtgCompleteSm4AccessErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8965)
)
hpevtFabricRtgCompleteSm4AccessErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricRtgCompleteSm4AccessErr.setStatus(
        ""
    )

hpevtFabricRtgCompleteTopologyErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8966)
)
hpevtFabricRtgCompleteTopologyErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricRtgCompleteTopologyErr.setStatus(
        ""
    )

hpevtFabricRouteTraversableCc2CcErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8968)
)
hpevtFabricRouteTraversableCc2CcErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricRouteTraversableCc2CcErr.setStatus(
        ""
    )

hpevtFabricDataRouteTraversableCc2CcErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8969)
)
hpevtFabricDataRouteTraversableCc2CcErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricDataRouteTraversableCc2CcErr.setStatus(
        ""
    )

hpevtFabricCc2ccTraverseLclXinRdErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8970)
)
hpevtFabricCc2ccTraverseLclXinRdErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricCc2ccTraverseLclXinRdErr.setStatus(
        ""
    )

hpevtFabricCc2ccTraverseRmtXinRdErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8971)
)
hpevtFabricCc2ccTraverseRmtXinRdErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricCc2ccTraverseRmtXinRdErr.setStatus(
        ""
    )

hpevtFabricCc2ccTraverseLclNotInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8972)
)
hpevtFabricCc2ccTraverseLclNotInit.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricCc2ccTraverseLclNotInit.setStatus(
        ""
    )

hpevtFabricCc2ccTraverseRmtNotInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8973)
)
hpevtFabricCc2ccTraverseRmtNotInit.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricCc2ccTraverseRmtNotInit.setStatus(
        ""
    )

hpevtFabricDisableXinLinkReadErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8974)
)
hpevtFabricDisableXinLinkReadErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricDisableXinLinkReadErr.setStatus(
        ""
    )

hpevtFabricXinInitRetryReadErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8975)
)
hpevtFabricXinInitRetryReadErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricXinInitRetryReadErr.setStatus(
        ""
    )

hpevtFabricAssertFabricCc = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8976)
)
hpevtFabricAssertFabricCc.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricAssertFabricCc.setStatus(
        ""
    )

hpevtCpuRestricted = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8979)
)
hpevtCpuRestricted.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCpuRestricted.setStatus(
        ""
    )

hpevtPdhInvalidRtcCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8981)
)
hpevtPdhInvalidRtcCleared.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdhInvalidRtcCleared.setStatus(
        ""
    )

hpevtLstNotRun = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8982)
)
hpevtLstNotRun.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtLstNotRun.setStatus(
        ""
    )

hpevtBootSetCellStateFabricFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8983)
)
hpevtBootSetCellStateFabricFailure.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootSetCellStateFabricFailure.setStatus(
        ""
    )

hpevtBootResetCellStateFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 8984)
)
hpevtBootResetCellStateFailure.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootResetCellStateFailure.setStatus(
        ""
    )

hpevtMemChipspareDeallocRank = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9000)
)
hpevtMemChipspareDeallocRank.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemChipspareDeallocRank.setStatus(
        ""
    )

hpevtClockFreqError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9019)
)
hpevtClockFreqError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtClockFreqError.setStatus(
        ""
    )

hpevtFabricColaInitTraversableErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9020)
)
hpevtFabricColaInitTraversableErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricColaInitTraversableErr.setStatus(
        ""
    )

hpevtFabricAttemptFocusedReroute = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9021)
)
hpevtFabricAttemptFocusedReroute.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricAttemptFocusedReroute.setStatus(
        ""
    )

hpevtFabricCellRerouteNinfoErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9022)
)
hpevtFabricCellRerouteNinfoErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricCellRerouteNinfoErr.setStatus(
        ""
    )

hpevtBootWakeCpuIsCpuDeconfigErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9038)
)
hpevtBootWakeCpuIsCpuDeconfigErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootWakeCpuIsCpuDeconfigErr.setStatus(
        ""
    )

hpevtBootWakeCpuGetCountersErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9039)
)
hpevtBootWakeCpuGetCountersErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootWakeCpuGetCountersErr.setStatus(
        ""
    )

hpevtBootWakeCpuGetStructAddrErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9040)
)
hpevtBootWakeCpuGetStructAddrErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootWakeCpuGetStructAddrErr.setStatus(
        ""
    )

hpevtBootCheckCpu4CompletionErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9041)
)
hpevtBootCheckCpu4CompletionErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootCheckCpu4CompletionErr.setStatus(
        ""
    )

hpevtBootCheckCpuGetStructAddrErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9042)
)
hpevtBootCheckCpuGetStructAddrErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootCheckCpuGetStructAddrErr.setStatus(
        ""
    )

hpevtReconfigResetScheduled = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9043)
)
hpevtReconfigResetScheduled.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtReconfigResetScheduled.setStatus(
        ""
    )

hpevtProfileWrongArchType = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9045)
)
hpevtProfileWrongArchType.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtProfileWrongArchType.setStatus(
        ""
    )

hpevtBootCheckCpuIsDeconfigErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9046)
)
hpevtBootCheckCpuIsDeconfigErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootCheckCpuIsDeconfigErr.setStatus(
        ""
    )

hpevtBootCheckCpuGetCountersErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9047)
)
hpevtBootCheckCpuGetCountersErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootCheckCpuGetCountersErr.setStatus(
        ""
    )

hpevtBootPdMonarchRtnFromSwSetFpErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9049)
)
hpevtBootPdMonarchRtnFromSwSetFpErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootPdMonarchRtnFromSwSetFpErr.setStatus(
        ""
    )

hpevtBootSlaveRtnFromFwSetFpErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9051)
)
hpevtBootSlaveRtnFromFwSetFpErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootSlaveRtnFromFwSetFpErr.setStatus(
        ""
    )

hpevtBootProblemBranchingToPgzLocation = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9052)
)
hpevtBootProblemBranchingToPgzLocation.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootProblemBranchingToPgzLocation.setStatus(
        ""
    )

hpevtBootBadCpuOrder = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9084)
)
hpevtBootBadCpuOrder.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootBadCpuOrder.setStatus(
        ""
    )

hpevtBootSlpWakeCntrsStructAddrErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9364)
)
hpevtBootSlpWakeCntrsStructAddrErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootSlpWakeCntrsStructAddrErr.setStatus(
        ""
    )

hpevtBootGetSleepTimeoutStructAddrErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9365)
)
hpevtBootGetSleepTimeoutStructAddrErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootGetSleepTimeoutStructAddrErr.setStatus(
        ""
    )

hpevtBootMoveSlavesDispatcherAddrErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9367)
)
hpevtBootMoveSlavesDispatcherAddrErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootMoveSlavesDispatcherAddrErr.setStatus(
        ""
    )

hpevtBootMoveSlavesCheckSlaveErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9368)
)
hpevtBootMoveSlavesCheckSlaveErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootMoveSlavesCheckSlaveErr.setStatus(
        ""
    )

hpevtBootMoveSlavesFpSetAddrErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9370)
)
hpevtBootMoveSlavesFpSetAddrErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootMoveSlavesFpSetAddrErr.setStatus(
        ""
    )

hpevtBootMoveSlavesFpSetErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9371)
)
hpevtBootMoveSlavesFpSetErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootMoveSlavesFpSetErr.setStatus(
        ""
    )

hpevtBootMoveCellMonarchsStructAddrErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9372)
)
hpevtBootMoveCellMonarchsStructAddrErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootMoveCellMonarchsStructAddrErr.setStatus(
        ""
    )

hpevtBootMoveCellMonarchsCheckSlaveErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9373)
)
hpevtBootMoveCellMonarchsCheckSlaveErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootMoveCellMonarchsCheckSlaveErr.setStatus(
        ""
    )

hpevtBootMoveCellMonarchsFpSetAddrErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9375)
)
hpevtBootMoveCellMonarchsFpSetAddrErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootMoveCellMonarchsFpSetAddrErr.setStatus(
        ""
    )

hpevtBootMoveCellMonarchsFpSetErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9376)
)
hpevtBootMoveCellMonarchsFpSetErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootMoveCellMonarchsFpSetErr.setStatus(
        ""
    )

hpevtBootDualCoreInitFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9379)
)
hpevtBootDualCoreInitFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootDualCoreInitFail.setStatus(
        ""
    )

hpevtBootDeconfigCpuModulePair = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9380)
)
hpevtBootDeconfigCpuModulePair.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootDeconfigCpuModulePair.setStatus(
        ""
    )

hpevtBootVirtualizeDualCoreRegistersFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9382)
)
hpevtBootVirtualizeDualCoreRegistersFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootVirtualizeDualCoreRegistersFail.setStatus(
        ""
    )

hpevtBootVirtualizeDualCoreInterposerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9383)
)
hpevtBootVirtualizeDualCoreInterposerFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootVirtualizeDualCoreInterposerFail.setStatus(
        ""
    )

hpevtBootInstallPmiHandlerFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9385)
)
hpevtBootInstallPmiHandlerFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootInstallPmiHandlerFailed.setStatus(
        ""
    )

hpevtPdhcCellIncompatable = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9388)
)
hpevtPdhcCellIncompatable.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdhcCellIncompatable.setStatus(
        ""
    )

hpevtPdhcPdhNotAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9389)
)
hpevtPdhcPdhNotAvailable.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdhcPdhNotAvailable.setStatus(
        ""
    )

hpevtPdhcMponFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9390)
)
hpevtPdhcMponFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdhcMponFailed.setStatus(
        ""
    )

hpevtPdhcDillonResetFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9391)
)
hpevtPdhcDillonResetFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdhcDillonResetFailed.setStatus(
        ""
    )

hpevtPdhcDmdClockFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9392)
)
hpevtPdhcDmdClockFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdhcDmdClockFailed.setStatus(
        ""
    )

hpevtAllCpusDeconfOnCell = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9394)
)
hpevtAllCpusDeconfOnCell.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtAllCpusDeconfOnCell.setStatus(
        ""
    )

hpevtFabricLogRoutingRdErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9403)
)
hpevtFabricLogRoutingRdErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricLogRoutingRdErr.setStatus(
        ""
    )

hpevtFabricLinkRendezDisableErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9412)
)
hpevtFabricLinkRendezDisableErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricLinkRendezDisableErr.setStatus(
        ""
    )

hpevtAcDeletedA0 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9417)
)
hpevtAcDeletedA0.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtAcDeletedA0.setStatus(
        ""
    )

hpevtAcDeletedA1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9418)
)
hpevtAcDeletedA1.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtAcDeletedA1.setStatus(
        ""
    )

hpevtAcDeletedB0 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9419)
)
hpevtAcDeletedB0.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtAcDeletedB0.setStatus(
        ""
    )

hpevtAcDeletedB1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9420)
)
hpevtAcDeletedB1.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtAcDeletedB1.setStatus(
        ""
    )

hpevtFabricCc2CcLinkDisableErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9428)
)
hpevtFabricCc2CcLinkDisableErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricCc2CcLinkDisableErr.setStatus(
        ""
    )

hpevtFabricISREarlyCopyRoutingErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9430)
)
hpevtFabricISREarlyCopyRoutingErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricISREarlyCopyRoutingErr.setStatus(
        ""
    )

hpevtFabricClrLinkInitBitErrMaskRd = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9431)
)
hpevtFabricClrLinkInitBitErrMaskRd.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricClrLinkInitBitErrMaskRd.setStatus(
        ""
    )

hpevtFabricClrLinkInitBitErrMaskWr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9432)
)
hpevtFabricClrLinkInitBitErrMaskWr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricClrLinkInitBitErrMaskWr.setStatus(
        ""
    )

hpevtFabricPortPairRdPstatusErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9433)
)
hpevtFabricPortPairRdPstatusErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricPortPairRdPstatusErr.setStatus(
        ""
    )

hpevtPdhBatteryPowerLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9438)
)
hpevtPdhBatteryPowerLow.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPdhBatteryPowerLow.setStatus(
        ""
    )

hpevtNoHandoffToOsMca = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9440)
)
hpevtNoHandoffToOsMca.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtNoHandoffToOsMca.setStatus(
        ""
    )

hpevtBootRtnFromSwCantGetCounters = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9441)
)
hpevtBootRtnFromSwCantGetCounters.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootRtnFromSwCantGetCounters.setStatus(
        ""
    )

hpevtBootRtnFromSwCpuNotAsleep = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9442)
)
hpevtBootRtnFromSwCpuNotAsleep.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootRtnFromSwCpuNotAsleep.setStatus(
        ""
    )

hpevtBootDeconfigAbsentCantSetCpuState = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9445)
)
hpevtBootDeconfigAbsentCantSetCpuState.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootDeconfigAbsentCantSetCpuState.setStatus(
        ""
    )

hpevtNvramBlockTableCorrupt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9448)
)
hpevtNvramBlockTableCorrupt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtNvramBlockTableCorrupt.setStatus(
        ""
    )

hpevtBootMoveSlavesSetTimeoutErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9450)
)
hpevtBootMoveSlavesSetTimeoutErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootMoveSlavesSetTimeoutErr.setStatus(
        ""
    )

hpevtBootReconfigAllCpus = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9460)
)
hpevtBootReconfigAllCpus.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootReconfigAllCpus.setStatus(
        ""
    )

hpevtBootGetNumcoresFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9461)
)
hpevtBootGetNumcoresFailure.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootGetNumcoresFailure.setStatus(
        ""
    )

hpevtFabricRmtRoutePortTopoErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9465)
)
hpevtFabricRmtRoutePortTopoErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricRmtRoutePortTopoErr.setStatus(
        ""
    )

hpevtFabricCellRerouteFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9466)
)
hpevtFabricCellRerouteFailure.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricCellRerouteFailure.setStatus(
        ""
    )

hpevtFabricRdFailedLinksError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9468)
)
hpevtFabricRdFailedLinksError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricRdFailedLinksError.setStatus(
        ""
    )

hpevtFabricWrFailedLinksRdError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9469)
)
hpevtFabricWrFailedLinksRdError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricWrFailedLinksRdError.setStatus(
        ""
    )

hpevtFabricWrFailedLinksWrError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9470)
)
hpevtFabricWrFailedLinksWrError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricWrFailedLinksWrError.setStatus(
        ""
    )

hpevtFabricIncFailedLinksRdError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9471)
)
hpevtFabricIncFailedLinksRdError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricIncFailedLinksRdError.setStatus(
        ""
    )

hpevtFabricIncFailedLinksWrError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9472)
)
hpevtFabricIncFailedLinksWrError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricIncFailedLinksWrError.setStatus(
        ""
    )

hpevtFabricIncFailedLinksHitLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9473)
)
hpevtFabricIncFailedLinksHitLimit.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricIncFailedLinksHitLimit.setStatus(
        ""
    )

hpevtFabricRtgCompleteRdFldLinksErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9474)
)
hpevtFabricRtgCompleteRdFldLinksErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricRtgCompleteRdFldLinksErr.setStatus(
        ""
    )

hpevtFabricRtgCompleteWrFldLinksErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9475)
)
hpevtFabricRtgCompleteWrFldLinksErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricRtgCompleteWrFldLinksErr.setStatus(
        ""
    )

hpevtFabricCellRerouteRdXbcErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9476)
)
hpevtFabricCellRerouteRdXbcErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricCellRerouteRdXbcErr.setStatus(
        ""
    )

hpevtFabricCellRerouteNbrNotReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9477)
)
hpevtFabricCellRerouteNbrNotReachable.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricCellRerouteNbrNotReachable.setStatus(
        ""
    )

hpevtFabricCellRerouteSm4RlsErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9479)
)
hpevtFabricCellRerouteSm4RlsErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricCellRerouteSm4RlsErr.setStatus(
        ""
    )

hpevtFabricRmtRoutePortBcastWrErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9480)
)
hpevtFabricRmtRoutePortBcastWrErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricRmtRoutePortBcastWrErr.setStatus(
        ""
    )

hpevtFabricRmtRoutePortRdErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9481)
)
hpevtFabricRmtRoutePortRdErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricRmtRoutePortRdErr.setStatus(
        ""
    )

hpevtFabricRmtRoutePortWrErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9482)
)
hpevtFabricRmtRoutePortWrErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricRmtRoutePortWrErr.setStatus(
        ""
    )

hpevtIoLinkSubsystemFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9484)
)
hpevtIoLinkSubsystemFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoLinkSubsystemFailed.setStatus(
        ""
    )

hpevtIoSbaSubsystemFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9485)
)
hpevtIoSbaSubsystemFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoSbaSubsystemFailed.setStatus(
        ""
    )

hpevtIoErrengineError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9486)
)
hpevtIoErrengineError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoErrengineError.setStatus(
        ""
    )

hpevtIoDiscEeMallocErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9487)
)
hpevtIoDiscEeMallocErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoDiscEeMallocErr.setStatus(
        ""
    )

hpevtIoDiscEeCreatetreeErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9488)
)
hpevtIoDiscEeCreatetreeErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoDiscEeCreatetreeErr.setStatus(
        ""
    )

hpevtIoDiscEeAttachserviceErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9489)
)
hpevtIoDiscEeAttachserviceErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoDiscEeAttachserviceErr.setStatus(
        ""
    )

hpevtIoDiscEeInitErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9490)
)
hpevtIoDiscEeInitErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoDiscEeInitErr.setStatus(
        ""
    )

hpevtIoDiscEeInitializationErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9491)
)
hpevtIoDiscEeInitializationErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoDiscEeInitializationErr.setStatus(
        ""
    )

hpevtIoDiscEeContextErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9492)
)
hpevtIoDiscEeContextErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoDiscEeContextErr.setStatus(
        ""
    )

hpevtIoDiscCreateSbaNodeErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9493)
)
hpevtIoDiscCreateSbaNodeErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoDiscCreateSbaNodeErr.setStatus(
        ""
    )

hpevtIoDiscSbaAttachserviceErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9494)
)
hpevtIoDiscSbaAttachserviceErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoDiscSbaAttachserviceErr.setStatus(
        ""
    )

hpevtIoDiscSbaInitnodeErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9495)
)
hpevtIoDiscSbaInitnodeErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoDiscSbaInitnodeErr.setStatus(
        ""
    )

hpevtIoDiscSbaUnknownErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9496)
)
hpevtIoDiscSbaUnknownErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoDiscSbaUnknownErr.setStatus(
        ""
    )

hpevtIoDeviceMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9497)
)
hpevtIoDeviceMissing.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoDeviceMissing.setStatus(
        ""
    )

hpevtFabricRmtRoutePortBadReroute = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9498)
)
hpevtFabricRmtRoutePortBadReroute.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricRmtRoutePortBadReroute.setStatus(
        ""
    )

hpevtAgtPredictMemFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9652)
)
hpevtAgtPredictMemFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtAgtPredictMemFail.setStatus(
        ""
    )

hpevtWinAgtLockedProperty = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9653)
)
hpevtWinAgtLockedProperty.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtWinAgtLockedProperty.setStatus(
        ""
    )

hpevtIoPciPowerOverloadErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9658)
)
hpevtIoPciPowerOverloadErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIoPciPowerOverloadErr.setStatus(
        ""
    )

hpevtMemSbeSeedingEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9659)
)
hpevtMemSbeSeedingEnabled.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemSbeSeedingEnabled.setStatus(
        ""
    )

hpevtFabricWrFailedLinksTopoErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9661)
)
hpevtFabricWrFailedLinksTopoErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricWrFailedLinksTopoErr.setStatus(
        ""
    )

hpevtBootErrInitGroupCPaFields = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9663)
)
hpevtBootErrInitGroupCPaFields.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootErrInitGroupCPaFields.setStatus(
        ""
    )

hpevtFabricAssertFabricHop = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9666)
)
hpevtFabricAssertFabricHop.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricAssertFabricHop.setStatus(
        ""
    )

hpevtBootFailedReadingProfileCInIcm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9668)
)
hpevtBootFailedReadingProfileCInIcm.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootFailedReadingProfileCInIcm.setStatus(
        ""
    )

hpevtFabricHaltLinkDisableErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9670)
)
hpevtFabricHaltLinkDisableErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricHaltLinkDisableErr.setStatus(
        ""
    )

hpevtBootGetSpiromGetSiblingErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9674)
)
hpevtBootGetSpiromGetSiblingErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootGetSpiromGetSiblingErr.setStatus(
        ""
    )

hpevtCpuClockRatioMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9678)
)
hpevtCpuClockRatioMismatch.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCpuClockRatioMismatch.setStatus(
        ""
    )

hpevtBootStopBootOverride = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9681)
)
hpevtBootStopBootOverride.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootStopBootOverride.setStatus(
        ""
    )

hpevtVgaBiosRelocFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9682)
)
hpevtVgaBiosRelocFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtVgaBiosRelocFail.setStatus(
        ""
    )

hpevtCompMatrixXsumError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9685)
)
hpevtCompMatrixXsumError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCompMatrixXsumError.setStatus(
        ""
    )

hpevtBootGetDefaultRdrsFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9695)
)
hpevtBootGetDefaultRdrsFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootGetDefaultRdrsFailed.setStatus(
        ""
    )

hpevtBootGetCurrentRdrsFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9696)
)
hpevtBootGetCurrentRdrsFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootGetCurrentRdrsFailed.setStatus(
        ""
    )

hpevtBootReadPrefetchFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9697)
)
hpevtBootReadPrefetchFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootReadPrefetchFailed.setStatus(
        ""
    )

hpevtBootReadZlcoFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9698)
)
hpevtBootReadZlcoFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootReadZlcoFailed.setStatus(
        ""
    )

hpevtBootUpdateZlcoAndPrefetchFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9700)
)
hpevtBootUpdateZlcoAndPrefetchFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootUpdateZlcoAndPrefetchFailed.setStatus(
        ""
    )

hpevtBootErrorReadingZlcoFlagInPdProfile = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9701)
)
hpevtBootErrorReadingZlcoFlagInPdProfile.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootErrorReadingZlcoFlagInPdProfile.setStatus(
        ""
    )

hpevtBootFindCoreCellCmplxProfileAcErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9706)
)
hpevtBootFindCoreCellCmplxProfileAcErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootFindCoreCellCmplxProfileAcErr.setStatus(
        ""
    )

hpevtBootFindCoreCellConfigSelectErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9707)
)
hpevtBootFindCoreCellConfigSelectErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootFindCoreCellConfigSelectErr.setStatus(
        ""
    )

hpevtBootCellLclCantFindViable = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9708)
)
hpevtBootCellLclCantFindViable.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootCellLclCantFindViable.setStatus(
        ""
    )

hpevtBootCellRmtCantFindViable = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9709)
)
hpevtBootCellRmtCantFindViable.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootCellRmtCantFindViable.setStatus(
        ""
    )

hpevtBootFindCoreCellNotInRendez = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9710)
)
hpevtBootFindCoreCellNotInRendez.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootFindCoreCellNotInRendez.setStatus(
        ""
    )

hpevtBootFindCoreCellLclNotViable = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9711)
)
hpevtBootFindCoreCellLclNotViable.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootFindCoreCellLclNotViable.setStatus(
        ""
    )

hpevtBootFindCoreCellFabriclessPdErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9712)
)
hpevtBootFindCoreCellFabriclessPdErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootFindCoreCellFabriclessPdErr.setStatus(
        ""
    )

hpevtRtcAccessError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9719)
)
hpevtRtcAccessError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtRtcAccessError.setStatus(
        ""
    )

hpevtBootAccessCellArchErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9727)
)
hpevtBootAccessCellArchErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootAccessCellArchErr.setStatus(
        ""
    )

hpevtXbcLogSizeErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9740)
)
hpevtXbcLogSizeErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXbcLogSizeErr.setStatus(
        ""
    )

hpevtXbcLogClearErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9741)
)
hpevtXbcLogClearErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXbcLogClearErr.setStatus(
        ""
    )

hpevtIodiscPciLogError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9744)
)
hpevtIodiscPciLogError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIodiscPciLogError.setStatus(
        ""
    )

hpevtIodiscSbaLogError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9745)
)
hpevtIodiscSbaLogError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIodiscSbaLogError.setStatus(
        ""
    )

hpevtXbcInitMaxRetries = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9746)
)
hpevtXbcInitMaxRetries.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXbcInitMaxRetries.setStatus(
        ""
    )

hpevtWinAgtPredictMemFailWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9750)
)
hpevtWinAgtPredictMemFailWarning.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtWinAgtPredictMemFailWarning.setStatus(
        ""
    )

hpevtWinAgtPredictMemFailCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9751)
)
hpevtWinAgtPredictMemFailCritical.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtWinAgtPredictMemFailCritical.setStatus(
        ""
    )

hpevtPciFatalRopeParityErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9753)
)
hpevtPciFatalRopeParityErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPciFatalRopeParityErr.setStatus(
        ""
    )

hpevtPciFatalBusError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9754)
)
hpevtPciFatalBusError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPciFatalBusError.setStatus(
        ""
    )

hpevtPciFatalDeviceError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9755)
)
hpevtPciFatalDeviceError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPciFatalDeviceError.setStatus(
        ""
    )

hpevtBootErrorReadingFirstBootToken = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9768)
)
hpevtBootErrorReadingFirstBootToken.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootErrorReadingFirstBootToken.setStatus(
        ""
    )

hpevtBootNonPaCellDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9769)
)
hpevtBootNonPaCellDetected.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBootNonPaCellDetected.setStatus(
        ""
    )

hpevtFabricErrorsXbcClearWrErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9774)
)
hpevtFabricErrorsXbcClearWrErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricErrorsXbcClearWrErr.setStatus(
        ""
    )

hpevtFabricErrorsXbcClearRdGlblErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9775)
)
hpevtFabricErrorsXbcClearRdGlblErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricErrorsXbcClearRdGlblErr.setStatus(
        ""
    )

hpevtFabricErrorsXbcClrLoSevErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9776)
)
hpevtFabricErrorsXbcClrLoSevErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricErrorsXbcClrLoSevErr.setStatus(
        ""
    )

hpevtFabricErrorsXbcClrHiSevErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9777)
)
hpevtFabricErrorsXbcClrHiSevErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricErrorsXbcClrHiSevErr.setStatus(
        ""
    )

hpevtFabricErrorsXbcClearRdPortErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9778)
)
hpevtFabricErrorsXbcClearRdPortErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricErrorsXbcClearRdPortErr.setStatus(
        ""
    )

hpevtFabricErrsCsrLogClrRdSlicesErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9780)
)
hpevtFabricErrsCsrLogClrRdSlicesErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricErrsCsrLogClrRdSlicesErr.setStatus(
        ""
    )

hpevtFabricErrsCsrLogClrCopyBlk0Err = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9781)
)
hpevtFabricErrsCsrLogClrCopyBlk0Err.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricErrsCsrLogClrCopyBlk0Err.setStatus(
        ""
    )

hpevtFabricErrsCsrLogClrCopyBlk2Err = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9782)
)
hpevtFabricErrsCsrLogClrCopyBlk2Err.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricErrsCsrLogClrCopyBlk2Err.setStatus(
        ""
    )

hpevtFabricXbcLoStateResetErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9783)
)
hpevtFabricXbcLoStateResetErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricXbcLoStateResetErr.setStatus(
        ""
    )

hpevtFabricClrXbcSym01Failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9784)
)
hpevtFabricClrXbcSym01Failure.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricClrXbcSym01Failure.setStatus(
        ""
    )

hpevtFabricClrXbcIsLoCsrErrErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9785)
)
hpevtFabricClrXbcIsLoCsrErrErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricClrXbcIsLoCsrErrErr.setStatus(
        ""
    )

hpevtFabricClrXbcRdLoLogStateErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9786)
)
hpevtFabricClrXbcRdLoLogStateErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricClrXbcRdLoLogStateErr.setStatus(
        ""
    )

hpevtFabricXbcHiStateResetErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9787)
)
hpevtFabricXbcHiStateResetErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricXbcHiStateResetErr.setStatus(
        ""
    )

hpevtFabricClrXbcIsHiCsrErrErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9788)
)
hpevtFabricClrXbcIsHiCsrErrErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricClrXbcIsHiCsrErrErr.setStatus(
        ""
    )

hpevtFabricClrXbcRdHiLogStateErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9789)
)
hpevtFabricClrXbcRdHiLogStateErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricClrXbcRdHiLogStateErr.setStatus(
        ""
    )

hpevtPlatformCacheHashingError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9801)
)
hpevtPlatformCacheHashingError.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPlatformCacheHashingError.setStatus(
        ""
    )

hpevtFabricXbcWriteableInvalidCsr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9827)
)
hpevtFabricXbcWriteableInvalidCsr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabricXbcWriteableInvalidCsr.setStatus(
        ""
    )

hpevtMcCellsLostConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9832)
)
hpevtMcCellsLostConnection.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMcCellsLostConnection.setStatus(
        ""
    )

hpevtBuildErrCellDevTree = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9849)
)
hpevtBuildErrCellDevTree.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBuildErrCellDevTree.setStatus(
        ""
    )

hpevtDcnfgFsbInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9867)
)
hpevtDcnfgFsbInit.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtDcnfgFsbInit.setStatus(
        ""
    )

hpevtDcnfgCpuParams = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9868)
)
hpevtDcnfgCpuParams.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtDcnfgCpuParams.setStatus(
        ""
    )

hpevtDcnfgCpuIcache = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9869)
)
hpevtDcnfgCpuIcache.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtDcnfgCpuIcache.setStatus(
        ""
    )

hpevtDcnfgCpuDcache = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9870)
)
hpevtDcnfgCpuDcache.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtDcnfgCpuDcache.setStatus(
        ""
    )

hpevtDcnfgCpuCacheState = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9871)
)
hpevtDcnfgCpuCacheState.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtDcnfgCpuCacheState.setStatus(
        ""
    )

hpevtDcnfgCpuCacheMonitor = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9872)
)
hpevtDcnfgCpuCacheMonitor.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtDcnfgCpuCacheMonitor.setStatus(
        ""
    )

hpevtDcnfgCpuMca = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9873)
)
hpevtDcnfgCpuMca.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtDcnfgCpuMca.setStatus(
        ""
    )

hpevtDcnfgCpuDisableMca = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9874)
)
hpevtDcnfgCpuDisableMca.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtDcnfgCpuDisableMca.setStatus(
        ""
    )

hpevtDcnfgCpuSelfTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9875)
)
hpevtDcnfgCpuSelfTest.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtDcnfgCpuSelfTest.setStatus(
        ""
    )

hpevtDcnfgCpuL2Cache = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9876)
)
hpevtDcnfgCpuL2Cache.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtDcnfgCpuL2Cache.setStatus(
        ""
    )

hpevtDcnfgCpuDefValue = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9877)
)
hpevtDcnfgCpuDefValue.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtDcnfgCpuDefValue.setStatus(
        ""
    )

hpevtDcnfgCpuInReg = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9878)
)
hpevtDcnfgCpuInReg.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtDcnfgCpuInReg.setStatus(
        ""
    )

hpevtDcnfgCpuProgReg = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9879)
)
hpevtDcnfgCpuProgReg.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtDcnfgCpuProgReg.setStatus(
        ""
    )

hpevtNoMemSelfTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 9896)
)
hpevtNoMemSelfTest.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtNoMemSelfTest.setStatus(
        ""
    )

hpevtCellLatchOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10060)
)
hpevtCellLatchOpen.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCellLatchOpen.setStatus(
        ""
    )

hpevtDcnfgRightCellLatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10061)
)
hpevtDcnfgRightCellLatch.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtDcnfgRightCellLatch.setStatus(
        ""
    )

hpevtCellLatchSensorBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10062)
)
hpevtCellLatchSensorBad.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCellLatchSensorBad.setStatus(
        ""
    )

hpevtVrmVltFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10063)
)
hpevtVrmVltFault.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtVrmVltFault.setStatus(
        ""
    )

hpevtVrmTempFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10064)
)
hpevtVrmTempFlt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtVrmTempFlt.setStatus(
        ""
    )

hpevtVrmFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10065)
)
hpevtVrmFlt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtVrmFlt.setStatus(
        ""
    )

hpevtVrmIoVltFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10068)
)
hpevtVrmIoVltFlt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtVrmIoVltFlt.setStatus(
        ""
    )

hpevtPwrBrickVltFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10069)
)
hpevtPwrBrickVltFlt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPwrBrickVltFlt.setStatus(
        ""
    )

hpevtVrmBkPlaneTempFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10070)
)
hpevtVrmBkPlaneTempFlt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtVrmBkPlaneTempFlt.setStatus(
        ""
    )

hpevtBkPlanePwrBrickTempFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10071)
)
hpevtBkPlanePwrBrickTempFlt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBkPlanePwrBrickTempFlt.setStatus(
        ""
    )

hpevtBkPlanVrmRailFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10072)
)
hpevtBkPlanVrmRailFlt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBkPlanVrmRailFlt.setStatus(
        ""
    )

hpevtBkPlanePwrBrkFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10073)
)
hpevtBkPlanePwrBrkFlt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBkPlanePwrBrkFlt.setStatus(
        ""
    )

hpevtBkPlaneVrmVltFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10103)
)
hpevtBkPlaneVrmVltFlt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBkPlaneVrmVltFlt.setStatus(
        ""
    )

hpevtBkPlaneVrmTempFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10104)
)
hpevtBkPlaneVrmTempFlt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBkPlaneVrmTempFlt.setStatus(
        ""
    )

hpevtBkPlaneFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10105)
)
hpevtBkPlaneFlt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBkPlaneFlt.setStatus(
        ""
    )

hpevtMstrMpFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10115)
)
hpevtMstrMpFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMstrMpFailed.setStatus(
        ""
    )

hpevtNvramAlloc = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10116)
)
hpevtNvramAlloc.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtNvramAlloc.setStatus(
        ""
    )

hpevtRtcTimeReg = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10132)
)
hpevtRtcTimeReg.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtRtcTimeReg.setStatus(
        ""
    )

hpevtPAAFltMx2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10159)
)
hpevtPAAFltMx2.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPAAFltMx2.setStatus(
        ""
    )

hpevtAPIopenLnkLocCell = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10209)
)
hpevtAPIopenLnkLocCell.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtAPIopenLnkLocCell.setStatus(
        ""
    )

hpevtCSRreadUnsuccessTimeOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10272)
)
hpevtCSRreadUnsuccessTimeOut.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCSRreadUnsuccessTimeOut.setStatus(
        ""
    )

hpevtCSRWriteUnsuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10273)
)
hpevtCSRWriteUnsuccess.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCSRWriteUnsuccess.setStatus(
        ""
    )

hpevtDataErrEncount = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10343)
)
hpevtDataErrEncount.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtDataErrEncount.setStatus(
        ""
    )

hpevtConfigMaxMemory = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10351)
)
hpevtConfigMaxMemory.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtConfigMaxMemory.setStatus(
        ""
    )

hpevtFailDelBadPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10357)
)
hpevtFailDelBadPort.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFailDelBadPort.setStatus(
        ""
    )

hpevtFailDelBadEdge = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10358)
)
hpevtFailDelBadEdge.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFailDelBadEdge.setStatus(
        ""
    )

hpevtCommandMemBuf = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10361)
)
hpevtCommandMemBuf.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCommandMemBuf.setStatus(
        ""
    )

hpevtUnsupprtArflsCsrRouteTravsble = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10375)
)
hpevtUnsupprtArflsCsrRouteTravsble.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUnsupprtArflsCsrRouteTravsble.setStatus(
        ""
    )

hpevtInvalidPortToTravsble = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10376)
)
hpevtInvalidPortToTravsble.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtInvalidPortToTravsble.setStatus(
        ""
    )

hpevtUnbleRdXBCPortNghbr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10377)
)
hpevtUnbleRdXBCPortNghbr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUnbleRdXBCPortNghbr.setStatus(
        ""
    )

hpevtXBCPortUnexpctNghbrChip = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10378)
)
hpevtXBCPortUnexpctNghbrChip.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXBCPortUnexpctNghbrChip.setStatus(
        ""
    )

hpevtXBCPortHaveUnxpctNghbrID = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10379)
)
hpevtXBCPortHaveUnxpctNghbrID.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXBCPortHaveUnxpctNghbrID.setStatus(
        ""
    )

hpevtXBCHaveUnexpctNghbrPrtConn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10380)
)
hpevtXBCHaveUnexpctNghbrPrtConn.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXBCHaveUnexpctNghbrPrtConn.setStatus(
        ""
    )

hpevtDataNotFndEdgLst = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10381)
)
hpevtDataNotFndEdgLst.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtDataNotFndEdgLst.setStatus(
        ""
    )

hpevtXBCPrtUnxpctNgbrChip = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10382)
)
hpevtXBCPrtUnxpctNgbrChip.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXBCPrtUnxpctNgbrChip.setStatus(
        ""
    )

hpevtXBCtoXBCLnkDwn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10384)
)
hpevtXBCtoXBCLnkDwn.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXBCtoXBCLnkDwn.setStatus(
        ""
    )

hpevtXBCprtFndErrTravsbl = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10385)
)
hpevtXBCprtFndErrTravsbl.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXBCprtFndErrTravsbl.setStatus(
        ""
    )

hpevtUnblRdLnkCelFabCSR = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10386)
)
hpevtUnblRdLnkCelFabCSR.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUnblRdLnkCelFabCSR.setStatus(
        ""
    )

hpevtUblRdXBCrouteTbl = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10387)
)
hpevtUblRdXBCrouteTbl.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUblRdXBCrouteTbl.setStatus(
        ""
    )

hpevtXBCLnkNotConnCSRTravsbl = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10388)
)
hpevtXBCLnkNotConnCSRTravsbl.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXBCLnkNotConnCSRTravsbl.setStatus(
        ""
    )

hpevtErrRdAlrecAlbIdCsr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10389)
)
hpevtErrRdAlrecAlbIdCsr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtErrRdAlrecAlbIdCsr.setStatus(
        ""
    )

hpevtCirRoutFndTstXbcCsr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10390)
)
hpevtCirRoutFndTstXbcCsr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCirRoutFndTstXbcCsr.setStatus(
        ""
    )

hpevtXBCRdErrAlrecAlbIdCsr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10391)
)
hpevtXBCRdErrAlrecAlbIdCsr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXBCRdErrAlrecAlbIdCsr.setStatus(
        ""
    )

hpevtXBC_XBCPrtHavInvldChipCnn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10392)
)
hpevtXBC_XBCPrtHavInvldChipCnn.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXBC_XBCPrtHavInvldChipCnn.setStatus(
        ""
    )

hpevtArflsXbcRotTravrsblCalBakToBak = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10393)
)
hpevtArflsXbcRotTravrsblCalBakToBak.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtArflsXbcRotTravrsblCalBakToBak.setStatus(
        ""
    )

hpevtXBCToXBClnkFndFatErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10394)
)
hpevtXBCToXBClnkFndFatErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXBCToXBClnkFndFatErr.setStatus(
        ""
    )

hpevtUnablRdXbcRotTblEnblMskCsr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10395)
)
hpevtUnablRdXbcRotTblEnblMskCsr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUnablRdXbcRotTblEnblMskCsr.setStatus(
        ""
    )

hpevtErrRdXbcRotTablCsr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10396)
)
hpevtErrRdXbcRotTablCsr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtErrRdXbcRotTablCsr.setStatus(
        ""
    )

hpevtXbcPrtErrRdAlrecAlbIDCsr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10397)
)
hpevtXbcPrtErrRdAlrecAlbIDCsr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXbcPrtErrRdAlrecAlbIDCsr.setStatus(
        ""
    )

hpevtXbcPrtFndUnxpctNgbrChip = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10398)
)
hpevtXbcPrtFndUnxpctNgbrChip.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXbcPrtFndUnxpctNgbrChip.setStatus(
        ""
    )

hpevtCelPrtPairNotFndGrphDat = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10401)
)
hpevtCelPrtPairNotFndGrphDat.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCelPrtPairNotFndGrphDat.setStatus(
        ""
    )

hpevtArchFabFndLocCelLnkNotConn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10402)
)
hpevtArchFabFndLocCelLnkNotConn.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtArchFabFndLocCelLnkNotConn.setStatus(
        ""
    )

hpevtXbcErrRdRoutCsr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10403)
)
hpevtXbcErrRdRoutCsr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXbcErrRdRoutCsr.setStatus(
        ""
    )

hpevtXbcUnablRdAlrecAlbIdCsr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10404)
)
hpevtXbcUnablRdAlrecAlbIdCsr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXbcUnablRdAlrecAlbIdCsr.setStatus(
        ""
    )

hpevtXbcPrtHasUnxpctNgbrChptype = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10405)
)
hpevtXbcPrtHasUnxpctNgbrChptype.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtXbcPrtHasUnxpctNgbrChptype.setStatus(
        ""
    )

hpevtCelToCelLnkHasUnxpctNgbrChpType = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10406)
)
hpevtCelToCelLnkHasUnxpctNgbrChpType.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCelToCelLnkHasUnxpctNgbrChpType.setStatus(
        ""
    )

hpevtCelPrtPairNotExstGrphDat = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10407)
)
hpevtCelPrtPairNotExstGrphDat.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCelPrtPairNotExstGrphDat.setStatus(
        ""
    )

hpevtCelToCelLnkConnUnxpctNgbrPrt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10408)
)
hpevtCelToCelLnkConnUnxpctNgbrPrt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCelToCelLnkConnUnxpctNgbrPrt.setStatus(
        ""
    )

hpevtCelToCelLnkConnUnxpctCel = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10409)
)
hpevtCelToCelLnkConnUnxpctCel.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCelToCelLnkConnUnxpctCel.setStatus(
        ""
    )

hpevtEFIDrvrFailLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10412)
)
hpevtEFIDrvrFailLoad.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEFIDrvrFailLoad.setStatus(
        ""
    )

hpevtVmRetErrNonCohTbl = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10413)
)
hpevtVmRetErrNonCohTbl.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtVmRetErrNonCohTbl.setStatus(
        ""
    )

hpevtNctTblWrtGlobLnkSelNonCohFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10414)
)
hpevtNctTblWrtGlobLnkSelNonCohFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtNctTblWrtGlobLnkSelNonCohFail.setStatus(
        ""
    )

hpevtNctTblFailArfPhs3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10415)
)
hpevtNctTblFailArfPhs3.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtNctTblFailArfPhs3.setStatus(
        ""
    )

hpevtPostRndevzFailPrepBckToBckSys = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10427)
)
hpevtPostRndevzFailPrepBckToBckSys.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPostRndevzFailPrepBckToBckSys.setStatus(
        ""
    )

hpevtArfPhs4UnablSetNonCohLnk = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10429)
)
hpevtArfPhs4UnablSetNonCohLnk.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtArfPhs4UnablSetNonCohLnk.setStatus(
        ""
    )

hpevtUnablSetNonCohRout = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10431)
)
hpevtUnablSetNonCohRout.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUnablSetNonCohRout.setStatus(
        ""
    )

hpevtUnableSetCohRoutCel = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10432)
)
hpevtUnableSetCohRoutCel.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUnableSetCohRoutCel.setStatus(
        ""
    )

hpevtErrWrtXbcRoutTblEnblMskCsr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10435)
)
hpevtErrWrtXbcRoutTblEnblMskCsr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtErrWrtXbcRoutTblEnblMskCsr.setStatus(
        ""
    )

hpevtVertxRetUnxpctErrNonCohTbl = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10436)
)
hpevtVertxRetUnxpctErrNonCohTbl.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtVertxRetUnxpctErrNonCohTbl.setStatus(
        ""
    )

hpevtWrtSkyGlobLnkSelCohFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10439)
)
hpevtWrtSkyGlobLnkSelCohFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtWrtSkyGlobLnkSelCohFail.setStatus(
        ""
    )

hpevtUnablWrtXbcPrtCsr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10475)
)
hpevtUnablWrtXbcPrtCsr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUnablWrtXbcPrtCsr.setStatus(
        ""
    )

hpevtSysFwUnAccesComplxProf = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10481)
)
hpevtSysFwUnAccesComplxProf.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSysFwUnAccesComplxProf.setStatus(
        ""
    )

hpevtSysFwDetctErrFabInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10482)
)
hpevtSysFwDetctErrFabInit.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSysFwDetctErrFabInit.setStatus(
        ""
    )

hpevtSysFwDetctFailFabInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10483)
)
hpevtSysFwDetctFailFabInit.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSysFwDetctFailFabInit.setStatus(
        ""
    )

hpevtSysFwDetctErrFabOptimz = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10487)
)
hpevtSysFwDetctErrFabOptimz.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSysFwDetctErrFabOptimz.setStatus(
        ""
    )

hpevtInPwrUPSFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10489)
)
hpevtInPwrUPSFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtInPwrUPSFail.setStatus(
        ""
    )

hpevtUpsRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10490)
)
hpevtUpsRestored.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUpsRestored.setStatus(
        ""
    )

hpevtUpsExhausted = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10495)
)
hpevtUpsExhausted.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUpsExhausted.setStatus(
        ""
    )

hpevtSALFailRedzvsProcs = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10509)
)
hpevtSALFailRedzvsProcs.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSALFailRedzvsProcs.setStatus(
        ""
    )

hpevtSALFailClrCECLog = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10510)
)
hpevtSALFailClrCECLog.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSALFailClrCECLog.setStatus(
        ""
    )

hpevtSysFwUnAccesXBCSemphr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10516)
)
hpevtSysFwUnAccesXBCSemphr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSysFwUnAccesXBCSemphr.setStatus(
        ""
    )

hpevtSysFwDetctErrRelXBCGlobSemphr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10518)
)
hpevtSysFwDetctErrRelXBCGlobSemphr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSysFwDetctErrRelXBCGlobSemphr.setStatus(
        ""
    )

hpevtSysFwDetctErrOwnXBCGlobSemphr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10519)
)
hpevtSysFwDetctErrOwnXBCGlobSemphr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSysFwDetctErrOwnXBCGlobSemphr.setStatus(
        ""
    )

hpevtErrFormXbcSemphrAddr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10520)
)
hpevtErrFormXbcSemphrAddr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtErrFormXbcSemphrAddr.setStatus(
        ""
    )

hpevtErrRdXbcGlobSemphr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10521)
)
hpevtErrRdXbcGlobSemphr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtErrRdXbcGlobSemphr.setStatus(
        ""
    )

hpevtFailGetXbcGlobSemphrAddr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10523)
)
hpevtFailGetXbcGlobSemphrAddr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFailGetXbcGlobSemphrAddr.setStatus(
        ""
    )

hpevtFailWrtXbcGlobSemphr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10524)
)
hpevtFailWrtXbcGlobSemphr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFailWrtXbcGlobSemphr.setStatus(
        ""
    )

hpevtFailRdXbcGlobSemphr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10528)
)
hpevtFailRdXbcGlobSemphr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFailRdXbcGlobSemphr.setStatus(
        ""
    )

hpevtFailGetAddrXbcGlobSemphr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10529)
)
hpevtFailGetAddrXbcGlobSemphr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFailGetAddrXbcGlobSemphr.setStatus(
        ""
    )

hpevtFailWrtXbcGlobSemphrAfrRls = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10530)
)
hpevtFailWrtXbcGlobSemphrAfrRls.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFailWrtXbcGlobSemphrAfrRls.setStatus(
        ""
    )

hpevtFailRelXbcGlobSemphr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10532)
)
hpevtFailRelXbcGlobSemphr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFailRelXbcGlobSemphr.setStatus(
        ""
    )

hpevtFabPhsExeInvlOrdr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10534)
)
hpevtFabPhsExeInvlOrdr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabPhsExeInvlOrdr.setStatus(
        ""
    )

hpevtFabPhsExeInvlOrdrDatExpctPhs = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10535)
)
hpevtFabPhsExeInvlOrdrDatExpctPhs.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabPhsExeInvlOrdrDatExpctPhs.setStatus(
        ""
    )

hpevtFailGetAddrXbcToXbcLnk = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10558)
)
hpevtFailGetAddrXbcToXbcLnk.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFailGetAddrXbcToXbcLnk.setStatus(
        ""
    )

hpevtFailOpnFabLnk = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10559)
)
hpevtFailOpnFabLnk.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFailOpnFabLnk.setStatus(
        ""
    )

hpevtErrWrtXbcRetRout = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10560)
)
hpevtErrWrtXbcRetRout.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtErrWrtXbcRetRout.setStatus(
        ""
    )

hpevtErrEnblXbcRetRout = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10561)
)
hpevtErrEnblXbcRetRout.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtErrEnblXbcRetRout.setStatus(
        ""
    )

hpevtFailDisprsRoutAcrssLnk = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10564)
)
hpevtFailDisprsRoutAcrssLnk.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFailDisprsRoutAcrssLnk.setStatus(
        ""
    )

hpevtErrSetXbcToXbcLnkRoutX = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10565)
)
hpevtErrSetXbcToXbcLnkRoutX.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtErrSetXbcToXbcLnkRoutX.setStatus(
        ""
    )

hpevtErrRoutRemtside = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10566)
)
hpevtErrRoutRemtside.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtErrRoutRemtside.setStatus(
        ""
    )

hpevtErrGetAddrRoutRemtXbc = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10567)
)
hpevtErrGetAddrRoutRemtXbc.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtErrGetAddrRoutRemtXbc.setStatus(
        ""
    )

hpevtErrGetNgbrInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10568)
)
hpevtErrGetNgbrInfo.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtErrGetNgbrInfo.setStatus(
        ""
    )

hpevtErrFindShrtRout = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10569)
)
hpevtErrFindShrtRout.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtErrFindShrtRout.setStatus(
        ""
    )

hpevtErrWrtRemtXbcRoutReg = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10570)
)
hpevtErrWrtRemtXbcRoutReg.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtErrWrtRemtXbcRoutReg.setStatus(
        ""
    )

hpevtErrEnblRoutRemtXbc = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10571)
)
hpevtErrEnblRoutRemtXbc.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtErrEnblRoutRemtXbc.setStatus(
        ""
    )

hpevtErrWrtRoutRegLocXbc = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10572)
)
hpevtErrWrtRoutRegLocXbc.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtErrWrtRoutRegLocXbc.setStatus(
        ""
    )

hpevtErrWrtLocXbcRoutRegRchRemtCel = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10573)
)
hpevtErrWrtLocXbcRoutRegRchRemtCel.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtErrWrtLocXbcRoutRegRchRemtCel.setStatus(
        ""
    )

hpevtErrEnblLocXbcRout = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10574)
)
hpevtErrEnblLocXbcRout.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtErrEnblLocXbcRout.setStatus(
        ""
    )

hpevtSynGrphFailPhs4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10617)
)
hpevtSynGrphFailPhs4.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSynGrphFailPhs4.setStatus(
        ""
    )

hpevtVmVertxFailSyncGrph = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10619)
)
hpevtVmVertxFailSyncGrph.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtVmVertxFailSyncGrph.setStatus(
        ""
    )

hpevtVmEdgFailFncSyncGrph = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10620)
)
hpevtVmEdgFailFncSyncGrph.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtVmEdgFailFncSyncGrph.setStatus(
        ""
    )

hpevtUnexpctErrCalVertxMod = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10621)
)
hpevtUnexpctErrCalVertxMod.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUnexpctErrCalVertxMod.setStatus(
        ""
    )

hpevtUnexpctRetVertxModCopCelGrph = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10622)
)
hpevtUnexpctRetVertxModCopCelGrph.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUnexpctRetVertxModCopCelGrph.setStatus(
        ""
    )

hpevtChecksumPdtFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10623)
)
hpevtChecksumPdtFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtChecksumPdtFailed.setStatus(
        ""
    )

hpevtChecksumNvmBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10625)
)
hpevtChecksumNvmBad.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtChecksumNvmBad.setStatus(
        ""
    )

hpevtChecksumCalcFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10626)
)
hpevtChecksumCalcFailed.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtChecksumCalcFailed.setStatus(
        ""
    )

hpevtSalandBmcTokenBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10628)
)
hpevtSalandBmcTokenBad.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSalandBmcTokenBad.setStatus(
        ""
    )

hpevtBkPlaneCable = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10629)
)
hpevtBkPlaneCable.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBkPlaneCable.setStatus(
        ""
    )

hpevtFparUnusable = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10698)
)
hpevtFparUnusable.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFparUnusable.setStatus(
        ""
    )

hpevtFWoutOfNvram = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10702)
)
hpevtFWoutOfNvram.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFWoutOfNvram.setStatus(
        ""
    )

hpevtNvramCPUCorrupt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10703)
)
hpevtNvramCPUCorrupt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtNvramCPUCorrupt.setStatus(
        ""
    )

hpevtNvramIOCorrupt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10704)
)
hpevtNvramIOCorrupt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtNvramIOCorrupt.setStatus(
        ""
    )

hpevtNvramLocMemCorrupt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10705)
)
hpevtNvramLocMemCorrupt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtNvramLocMemCorrupt.setStatus(
        ""
    )

hpevtFWInconsistExist = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10706)
)
hpevtFWInconsistExist.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFWInconsistExist.setStatus(
        ""
    )

hpevtFWUnableCreatefParsIO = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10707)
)
hpevtFWUnableCreatefParsIO.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFWUnableCreatefParsIO.setStatus(
        ""
    )

hpevtFWUnableCreatefParsCLM = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10708)
)
hpevtFWUnableCreatefParsCLM.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFWUnableCreatefParsCLM.setStatus(
        ""
    )

hpevtFWOutOfNvram = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10771)
)
hpevtFWOutOfNvram.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFWOutOfNvram.setStatus(
        ""
    )

hpevtFWLbaReconfigFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10772)
)
hpevtFWLbaReconfigFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFWLbaReconfigFail.setStatus(
        ""
    )

hpevtCpuModuleBadConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10779)
)
hpevtCpuModuleBadConfig.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCpuModuleBadConfig.setStatus(
        ""
    )

hpevtCpuInvalidTerminator = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10780)
)
hpevtCpuInvalidTerminator.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCpuInvalidTerminator.setStatus(
        ""
    )

hpevtInvocationSoftResetCode = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10793)
)
hpevtInvocationSoftResetCode.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtInvocationSoftResetCode.setStatus(
        ""
    )

hpevtDataSm4SelfReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10794)
)
hpevtDataSm4SelfReset.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtDataSm4SelfReset.setStatus(
        ""
    )

hpevtfParsfailRelseResrce = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10795)
)
hpevtfParsfailRelseResrce.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtfParsfailRelseResrce.setStatus(
        ""
    )

hpevtPFMManyErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10814)
)
hpevtPFMManyErrors.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPFMManyErrors.setStatus(
        ""
    )

hpevtPFMOverTempProc = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10822)
)
hpevtPFMOverTempProc.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPFMOverTempProc.setStatus(
        ""
    )

hpevtPFMCacheErrorProc = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10823)
)
hpevtPFMCacheErrorProc.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPFMCacheErrorProc.setStatus(
        ""
    )

hpevtPFMCorrecErrorCache = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10824)
)
hpevtPFMCorrecErrorCache.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPFMCorrecErrorCache.setStatus(
        ""
    )

hpevtPFMCorrErrSysBus = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10825)
)
hpevtPFMCorrErrSysBus.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPFMCorrErrSysBus.setStatus(
        ""
    )

hpevtPFMCorrErrProcBus = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10826)
)
hpevtPFMCorrErrProcBus.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPFMCorrErrProcBus.setStatus(
        ""
    )

hpevtPFMErrTagMemProc = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10827)
)
hpevtPFMErrTagMemProc.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPFMErrTagMemProc.setStatus(
        ""
    )

hpevtfParsNotEnableBoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10830)
)
hpevtfParsNotEnableBoot.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtfParsNotEnableBoot.setStatus(
        ""
    )

hpevtfParsNotRecveOwnShip = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10832)
)
hpevtfParsNotRecveOwnShip.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtfParsNotRecveOwnShip.setStatus(
        ""
    )

hpevtFWErrSetNvramVal = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10833)
)
hpevtFWErrSetNvramVal.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFWErrSetNvramVal.setStatus(
        ""
    )

hpevtUnablWrtXbcPrtRoutTblEnblMsk = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10842)
)
hpevtUnablWrtXbcPrtRoutTblEnblMsk.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUnablWrtXbcPrtRoutTblEnblMsk.setStatus(
        ""
    )

hpevtProcessIntrptUnRecoverble = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10853)
)
hpevtProcessIntrptUnRecoverble.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtProcessIntrptUnRecoverble.setStatus(
        ""
    )

hpevtSBASetDevMaskFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10871)
)
hpevtSBASetDevMaskFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSBASetDevMaskFail.setStatus(
        ""
    )

hpevtLBASlotDevScanErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10927)
)
hpevtLBASlotDevScanErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtLBASlotDevScanErr.setStatus(
        ""
    )

hpevtInadequateMemTofPar = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10936)
)
hpevtInadequateMemTofPar.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtInadequateMemTofPar.setStatus(
        ""
    )

hpevtFailCollVertxInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10937)
)
hpevtFailCollVertxInfo.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFailCollVertxInfo.setStatus(
        ""
    )

hpevtFailCollVertxFabInfoCall = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10938)
)
hpevtFailCollVertxFabInfoCall.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFailCollVertxFabInfoCall.setStatus(
        ""
    )

hpevtFailFndEdgeProcCall = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10939)
)
hpevtFailFndEdgeProcCall.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFailFndEdgeProcCall.setStatus(
        ""
    )

hpevtFailFndEdgProcCall = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10940)
)
hpevtFailFndEdgProcCall.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFailFndEdgProcCall.setStatus(
        ""
    )

hpevtManyEdgEncntProcCall = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10941)
)
hpevtManyEdgEncntProcCall.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtManyEdgEncntProcCall.setStatus(
        ""
    )

hpevtFailGetAddrProcCall = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10943)
)
hpevtFailGetAddrProcCall.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFailGetAddrProcCall.setStatus(
        ""
    )

hpevtUnexpctStatEncntProcCall = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10944)
)
hpevtUnexpctStatEncntProcCall.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUnexpctStatEncntProcCall.setStatus(
        ""
    )

hpevtUnablGetLnkHlthStatProcCall = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10945)
)
hpevtUnablGetLnkHlthStatProcCall.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUnablGetLnkHlthStatProcCall.setStatus(
        ""
    )

hpevtFabDatFailCrcChk = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 10946)
)
hpevtFabDatFailCrcChk.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabDatFailCrcChk.setStatus(
        ""
    )

hpevtVmCollVertcFailUnexpct = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11032)
)
hpevtVmCollVertcFailUnexpct.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtVmCollVertcFailUnexpct.setStatus(
        ""
    )

hpevtUnablGenAlbArfSetCsr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11033)
)
hpevtUnablGenAlbArfSetCsr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUnablGenAlbArfSetCsr.setStatus(
        ""
    )

hpevtSetDefCsrFailUnexpct = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11034)
)
hpevtSetDefCsrFailUnexpct.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSetDefCsrFailUnexpct.setStatus(
        ""
    )

hpevtEncntErrRout = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11038)
)
hpevtEncntErrRout.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEncntErrRout.setStatus(
        ""
    )

hpevtEncntErrRoutFab = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11039)
)
hpevtEncntErrRoutFab.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEncntErrRoutFab.setStatus(
        ""
    )

hpevtErrEncntRoutFabPrvntRoutSel = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11040)
)
hpevtErrEncntRoutFabPrvntRoutSel.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtErrEncntRoutFabPrvntRoutSel.setStatus(
        ""
    )

hpevtInvlPrtRetRoutXbcCcLnk = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11041)
)
hpevtInvlPrtRetRoutXbcCcLnk.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtInvlPrtRetRoutXbcCcLnk.setStatus(
        ""
    )

hpevtErrEncntRoutFabPrvntRoutSelSw = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11042)
)
hpevtErrEncntRoutFabPrvntRoutSelSw.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtErrEncntRoutFabPrvntRoutSelSw.setStatus(
        ""
    )

hpevtSecndFlshNotProgrmValidImg = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11052)
)
hpevtSecndFlshNotProgrmValidImg.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSecndFlshNotProgrmValidImg.setStatus(
        ""
    )

hpevtSysBckPlnPwr1p2LDOFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11452)
)
hpevtSysBckPlnPwr1p2LDOFault.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSysBckPlnPwr1p2LDOFault.setStatus(
        ""
    )

hpevtSysBckPlnPwr2p5LDOFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11454)
)
hpevtSysBckPlnPwr2p5LDOFault.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSysBckPlnPwr2p5LDOFault.setStatus(
        ""
    )

hpevtSysBckPlnPwr3p3HseFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11456)
)
hpevtSysBckPlnPwr3p3HseFault.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSysBckPlnPwr3p3HseFault.setStatus(
        ""
    )

hpevtSysBckPlnPwr12Fault = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11459)
)
hpevtSysBckPlnPwr12Fault.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSysBckPlnPwr12Fault.setStatus(
        ""
    )

hpevtSysBckPlnPwr3p3Fault = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11461)
)
hpevtSysBckPlnPwr3p3Fault.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSysBckPlnPwr3p3Fault.setStatus(
        ""
    )

hpevtSysBckPlnPwr1p5Fault = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11463)
)
hpevtSysBckPlnPwr1p5Fault.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSysBckPlnPwr1p5Fault.setStatus(
        ""
    )

hpevtSysBckPlnPwr2p5Fault = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11465)
)
hpevtSysBckPlnPwr2p5Fault.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSysBckPlnPwr2p5Fault.setStatus(
        ""
    )

hpevtPwrRailPrvInsuffPwrToBckPln = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11467)
)
hpevtPwrRailPrvInsuffPwrToBckPln.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPwrRailPrvInsuffPwrToBckPln.setStatus(
        ""
    )

hpevtRcsNoProvClkBckPln = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11468)
)
hpevtRcsNoProvClkBckPln.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtRcsNoProvClkBckPln.setStatus(
        ""
    )

hpevtHsoFaultOrRemv = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11471)
)
hpevtHsoFaultOrRemv.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtHsoFaultOrRemv.setStatus(
        ""
    )

hpevtOpClkNoMtchRcsHso = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11478)
)
hpevtOpClkNoMtchRcsHso.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtOpClkNoMtchRcsHso.setStatus(
        ""
    )

hpevtClkMrgnBckPlnFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11479)
)
hpevtClkMrgnBckPlnFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtClkMrgnBckPlnFail.setStatus(
        ""
    )

hpevtHsoNoRedund = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11481)
)
hpevtHsoNoRedund.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtHsoNoRedund.setStatus(
        ""
    )

hpevtHsoInsuff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11482)
)
hpevtHsoInsuff.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtHsoInsuff.setStatus(
        ""
    )

hpevtFailRdRcsHso = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11483)
)
hpevtFailRdRcsHso.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFailRdRcsHso.setStatus(
        ""
    )

hpevtFailWrtRcsHso = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11484)
)
hpevtFailWrtRcsHso.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFailWrtRcsHso.setStatus(
        ""
    )

hpevtFailRdRpm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11485)
)
hpevtFailRdRpm.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFailRdRpm.setStatus(
        ""
    )

hpevtFailWrtRpm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11486)
)
hpevtFailWrtRpm.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFailWrtRpm.setStatus(
        ""
    )

hpevtFailRdOsp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11487)
)
hpevtFailRdOsp.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFailRdOsp.setStatus(
        ""
    )

hpevtFailWrtOsp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11488)
)
hpevtFailWrtOsp.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFailWrtOsp.setStatus(
        ""
    )

hpevtSbsFaultStrt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11489)
)
hpevtSbsFaultStrt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSbsFaultStrt.setStatus(
        ""
    )

hpevtFailRdIObckPlnLpm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11495)
)
hpevtFailRdIObckPlnLpm.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFailRdIObckPlnLpm.setStatus(
        ""
    )

hpevtFailWrtIOBckPlnLpm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11496)
)
hpevtFailWrtIOBckPlnLpm.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFailWrtIOBckPlnLpm.setStatus(
        ""
    )

hpevtSysSoftViolateWellBhaveRule = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11515)
)
hpevtSysSoftViolateWellBhaveRule.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSysSoftViolateWellBhaveRule.setStatus(
        ""
    )

hpevtAlbInitPrepUnablRdAlrecConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11521)
)
hpevtAlbInitPrepUnablRdAlrecConfig.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtAlbInitPrepUnablRdAlrecConfig.setStatus(
        ""
    )

hpevtfParIsDisbleFrmBoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11529)
)
hpevtfParIsDisbleFrmBoot.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtfParIsDisbleFrmBoot.setStatus(
        ""
    )

hpevtfParNotInstantiateFW = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11530)
)
hpevtfParNotInstantiateFW.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtfParNotInstantiateFW.setStatus(
        ""
    )

hpevtfParNotHaveIOResrc = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11531)
)
hpevtfParNotHaveIOResrc.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtfParNotHaveIOResrc.setStatus(
        ""
    )

hpevtCPUsDeconfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11537)
)
hpevtCPUsDeconfig.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCPUsDeconfig.setStatus(
        ""
    )

hpevtCPUsReconfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11538)
)
hpevtCPUsReconfig.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCPUsReconfig.setStatus(
        ""
    )

hpevtIOBckPln33VFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11566)
)
hpevtIOBckPln33VFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIOBckPln33VFail.setStatus(
        ""
    )

hpevtBckPln5VFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11567)
)
hpevtBckPln5VFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBckPln5VFail.setStatus(
        ""
    )

hpevtIOBckPlnNeg12VFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11568)
)
hpevtIOBckPlnNeg12VFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIOBckPlnNeg12VFail.setStatus(
        ""
    )

hpevtIOBckPln12VFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11569)
)
hpevtIOBckPln12VFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIOBckPln12VFail.setStatus(
        ""
    )

hpevtIOBckPln15VTempFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11575)
)
hpevtIOBckPln15VTempFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIOBckPln15VTempFail.setStatus(
        ""
    )

hpevtIOBckPln33VTempFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11576)
)
hpevtIOBckPln33VTempFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIOBckPln33VTempFail.setStatus(
        ""
    )

hpevtIOBckPlnNeg12VTempFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11578)
)
hpevtIOBckPlnNeg12VTempFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIOBckPlnNeg12VTempFail.setStatus(
        ""
    )

hpevtIOBckPln12VTempFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11579)
)
hpevtIOBckPln12VTempFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIOBckPln12VTempFail.setStatus(
        ""
    )

hpevtLocCelUnablClrLnkOffBit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11580)
)
hpevtLocCelUnablClrLnkOffBit.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtLocCelUnablClrLnkOffBit.setStatus(
        ""
    )

hpevtArfOlaPreRendezUnablRchCel = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11581)
)
hpevtArfOlaPreRendezUnablRchCel.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtArfOlaPreRendezUnablRchCel.setStatus(
        ""
    )

hpevtUnexpctErrSetNctTbl = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11582)
)
hpevtUnexpctErrSetNctTbl.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUnexpctErrSetNctTbl.setStatus(
        ""
    )

hpevtPhs4UnexpctFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11583)
)
hpevtPhs4UnexpctFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPhs4UnexpctFail.setStatus(
        ""
    )

hpevtUnablSyncGrphCell = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11584)
)
hpevtUnablSyncGrphCell.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUnablSyncGrphCell.setStatus(
        ""
    )

hpevtBitMapUnrchCel = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11585)
)
hpevtBitMapUnrchCel.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBitMapUnrchCel.setStatus(
        ""
    )

hpevtRetValNctCohTbl = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11586)
)
hpevtRetValNctCohTbl.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtRetValNctCohTbl.setStatus(
        ""
    )

hpevtArfRoutEnblRetErrLocCel = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11597)
)
hpevtArfRoutEnblRetErrLocCel.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtArfRoutEnblRetErrLocCel.setStatus(
        ""
    )

hpevtArfRoutDisRetErrOla = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11598)
)
hpevtArfRoutDisRetErrOla.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtArfRoutDisRetErrOla.setStatus(
        ""
    )

hpevtArfRoutDisRetErrArfPhs4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11599)
)
hpevtArfRoutDisRetErrArfPhs4.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtArfRoutDisRetErrArfPhs4.setStatus(
        ""
    )

hpevtMemAlloctFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11603)
)
hpevtMemAlloctFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemAlloctFail.setStatus(
        ""
    )

hpevtMemLockFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11604)
)
hpevtMemLockFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemLockFail.setStatus(
        ""
    )

hpevtMinProcReqMoreThanAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11605)
)
hpevtMinProcReqMoreThanAvail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMinProcReqMoreThanAvail.setStatus(
        ""
    )

hpevtVMNotHandlGuestOSPerf = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11607)
)
hpevtVMNotHandlGuestOSPerf.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtVMNotHandlGuestOSPerf.setStatus(
        ""
    )

hpevtKernlDrvFailLckMem = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11696)
)
hpevtKernlDrvFailLckMem.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtKernlDrvFailLckMem.setStatus(
        ""
    )

hpevtMMIOmapFndInfoInTble = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11700)
)
hpevtMMIOmapFndInfoInTble.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMMIOmapFndInfoInTble.setStatus(
        ""
    )

hpevtAttmptAddPCImoreThanAllow = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11702)
)
hpevtAttmptAddPCImoreThanAllow.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtAttmptAddPCImoreThanAllow.setStatus(
        ""
    )

hpevtCPUConfigNotSupprt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11703)
)
hpevtCPUConfigNotSupprt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCPUConfigNotSupprt.setStatus(
        ""
    )

hpevtISAUARTcreatWithoutDatStrct = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11705)
)
hpevtISAUARTcreatWithoutDatStrct.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtISAUARTcreatWithoutDatStrct.setStatus(
        ""
    )

hpevtTCGETorIOCTLFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11706)
)
hpevtTCGETorIOCTLFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtTCGETorIOCTLFail.setStatus(
        ""
    )

hpevtStatCallPMANFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11707)
)
hpevtStatCallPMANFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtStatCallPMANFail.setStatus(
        ""
    )

hpevtVMDrvNotOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11708)
)
hpevtVMDrvNotOpen.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtVMDrvNotOpen.setStatus(
        ""
    )

hpevtVMDrvNotCreatVM = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11709)
)
hpevtVMDrvNotCreatVM.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtVMDrvNotCreatVM.setStatus(
        ""
    )

hpevtNotAbleCreatNodeForComm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11710)
)
hpevtNotAbleCreatNodeForComm.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtNotAbleCreatNodeForComm.setStatus(
        ""
    )

hpevtVMNotOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11711)
)
hpevtVMNotOpen.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtVMNotOpen.setStatus(
        ""
    )

hpevtVMDrvNotLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11712)
)
hpevtVMDrvNotLoad.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtVMDrvNotLoad.setStatus(
        ""
    )

hpevtCreatThreadPMANFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11718)
)
hpevtCreatThreadPMANFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCreatThreadPMANFail.setStatus(
        ""
    )

hpevtVMDrvUnableCommVM = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11719)
)
hpevtVMDrvUnableCommVM.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtVMDrvUnableCommVM.setStatus(
        ""
    )

hpevtConfigUnableToRd = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11720)
)
hpevtConfigUnableToRd.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtConfigUnableToRd.setStatus(
        ""
    )

hpevtMemAllocFWTblFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11721)
)
hpevtMemAllocFWTblFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMemAllocFWTblFail.setStatus(
        ""
    )

hpevtDrvUnableBldMapTbl = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11723)
)
hpevtDrvUnableBldMapTbl.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtDrvUnableBldMapTbl.setStatus(
        ""
    )

hpevtVMRebootFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11724)
)
hpevtVMRebootFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtVMRebootFail.setStatus(
        ""
    )

hpevtSetIntlCohTblRetErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11775)
)
hpevtSetIntlCohTblRetErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSetIntlCohTblRetErr.setStatus(
        ""
    )

hpBootStblStoreFlashErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11780)
)
hpBootStblStoreFlashErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpBootStblStoreFlashErr.setStatus(
        ""
    )

hpBootStblStoreNvMErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11783)
)
hpBootStblStoreNvMErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpBootStblStoreNvMErr.setStatus(
        ""
    )

hpevtFWDetectilleglMemConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11784)
)
hpevtFWDetectilleglMemConfig.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFWDetectilleglMemConfig.setStatus(
        ""
    )

hpevtSFWFailAllotNVM = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11788)
)
hpevtSFWFailAllotNVM.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSFWFailAllotNVM.setStatus(
        ""
    )

hpevtSFWFailAllotSCRRAM = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11789)
)
hpevtSFWFailAllotSCRRAM.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSFWFailAllotSCRRAM.setStatus(
        ""
    )

hpevtSetIntlCohRetErrArfPhs3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11797)
)
hpevtSetIntlCohRetErrArfPhs3.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSetIntlCohRetErrArfPhs3.setStatus(
        ""
    )

hpevtErrWrtErrMskAlrecAlTran = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11807)
)
hpevtErrWrtErrMskAlrecAlTran.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtErrWrtErrMskAlrecAlTran.setStatus(
        ""
    )

hpevtFwUnexpctIntrnlErrVertx = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11840)
)
hpevtFwUnexpctIntrnlErrVertx.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFwUnexpctIntrnlErrVertx.setStatus(
        ""
    )

hpOsUnsupportedWmixedCpuRevs = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11850)
)
hpOsUnsupportedWmixedCpuRevs.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpOsUnsupportedWmixedCpuRevs.setStatus(
        ""
    )

hpevtFwUnexpctErrSetLnk = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11851)
)
hpevtFwUnexpctErrSetLnk.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFwUnexpctErrSetLnk.setStatus(
        ""
    )

hpevtFwUnbleWrtSkyGlobLnkSelCoh = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11863)
)
hpevtFwUnbleWrtSkyGlobLnkSelCoh.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFwUnbleWrtSkyGlobLnkSelCoh.setStatus(
        ""
    )

hpOsBootDisabledWmixedCpuKeys = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11870)
)
hpOsBootDisabledWmixedCpuKeys.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpOsBootDisabledWmixedCpuKeys.setStatus(
        ""
    )

hpevtSysFwErrUpdtLnk = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11885)
)
hpevtSysFwErrUpdtLnk.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSysFwErrUpdtLnk.setStatus(
        ""
    )

hpevtFabUnablGenSkyCsrAddr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11904)
)
hpevtFabUnablGenSkyCsrAddr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFabUnablGenSkyCsrAddr.setStatus(
        ""
    )

hpevtFwUnablGenSkyCsrAdrr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11905)
)
hpevtFwUnablGenSkyCsrAdrr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFwUnablGenSkyCsrAdrr.setStatus(
        ""
    )

hpevtNoOSBootRendez = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11932)
)
hpevtNoOSBootRendez.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtNoOSBootRendez.setStatus(
        ""
    )

hpevtChksmFailOSBootRendez = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11933)
)
hpevtChksmFailOSBootRendez.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtChksmFailOSBootRendez.setStatus(
        ""
    )

hpevtSysFWCallPalCopyInfoFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11960)
)
hpevtSysFWCallPalCopyInfoFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSysFWCallPalCopyInfoFail.setStatus(
        ""
    )

hpevtSysFWCallPalCopyPalFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11961)
)
hpevtSysFWCallPalCopyPalFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSysFWCallPalCopyPalFail.setStatus(
        ""
    )

hpevtSysFWCallPalCacFlusFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11962)
)
hpevtSysFWCallPalCacFlusFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSysFWCallPalCacFlusFail.setStatus(
        ""
    )

hpevtCellNotInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11964)
)
hpevtCellNotInit.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCellNotInit.setStatus(
        ""
    )

hpevtFPARsCompBroke = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11966)
)
hpevtFPARsCompBroke.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFPARsCompBroke.setStatus(
        ""
    )

hpevtFailGetFPARsSemphr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11967)
)
hpevtFailGetFPARsSemphr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFailGetFPARsSemphr.setStatus(
        ""
    )

hpevtMorThnOneProcCallCell = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11968)
)
hpevtMorThnOneProcCallCell.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMorThnOneProcCallCell.setStatus(
        ""
    )

hpevtFPARsProcFailRendez = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11969)
)
hpevtFPARsProcFailRendez.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFPARsProcFailRendez.setStatus(
        ""
    )

hpevtEncntUnexptErrOLA = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11970)
)
hpevtEncntUnexptErrOLA.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtEncntUnexptErrOLA.setStatus(
        ""
    )

hpevtMCAOccPriorPreMCA = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11971)
)
hpevtMCAOccPriorPreMCA.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMCAOccPriorPreMCA.setStatus(
        ""
    )

hpevtMCAInitEvtProc = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11972)
)
hpevtMCAInitEvtProc.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMCAInitEvtProc.setStatus(
        ""
    )

hpevtUnablFndBadEdg = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11974)
)
hpevtUnablFndBadEdg.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUnablFndBadEdg.setStatus(
        ""
    )

hpevtUnknEntityDrwPwrBus = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 11989)
)
hpevtUnknEntityDrwPwrBus.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUnknEntityDrwPwrBus.setStatus(
        ""
    )

hpevtSoftPartNotBoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12001)
)
hpevtSoftPartNotBoot.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSoftPartNotBoot.setStatus(
        ""
    )

hpevtUnablRotArndBrkLnk = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12008)
)
hpevtUnablRotArndBrkLnk.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUnablRotArndBrkLnk.setStatus(
        ""
    )

hpevtUnablSetAPERLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12013)
)
hpevtUnablSetAPERLock.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUnablSetAPERLock.setStatus(
        ""
    )

hpevtUncorrtMemEccErrOccr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12017)
)
hpevtUncorrtMemEccErrOccr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUncorrtMemEccErrOccr.setStatus(
        ""
    )

hpevtErrRetrvCrssbarLnk = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12025)
)
hpevtErrRetrvCrssbarLnk.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtErrRetrvCrssbarLnk.setStatus(
        ""
    )

hpevtUnablRdCrssbar = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12028)
)
hpevtUnablRdCrssbar.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUnablRdCrssbar.setStatus(
        ""
    )

hpevtUnablEstbshCrssbar = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12029)
)
hpevtUnablEstbshCrssbar.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUnablEstbshCrssbar.setStatus(
        ""
    )

hpevtNoRoutLocCrssBar = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12047)
)
hpevtNoRoutLocCrssBar.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtNoRoutLocCrssBar.setStatus(
        ""
    )

hpevtInvalidTPM = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12048)
)
hpevtInvalidTPM.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtInvalidTPM.setStatus(
        ""
    )

hpevtTPMFailInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12049)
)
hpevtTPMFailInit.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtTPMFailInit.setStatus(
        ""
    )

hpevtCpuTempExceedHiThres = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12050)
)
hpevtCpuTempExceedHiThres.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCpuTempExceedHiThres.setStatus(
        ""
    )

hpevtSFWDetErrStablStorFlsh = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12069)
)
hpevtSFWDetErrStablStorFlsh.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSFWDetErrStablStorFlsh.setStatus(
        ""
    )

hpevtInlckOpenPCIPwr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12091)
)
hpevtInlckOpenPCIPwr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtInlckOpenPCIPwr.setStatus(
        ""
    )

hpevtFaltDetDropRegIO = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12101)
)
hpevtFaltDetDropRegIO.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFaltDetDropRegIO.setStatus(
        ""
    )

hpevtFaltDetDropRegManBckPlne = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12102)
)
hpevtFaltDetDropRegManBckPlne.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFaltDetDropRegManBckPlne.setStatus(
        ""
    )

hpevtFaltDetHotswpCoreIO = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12103)
)
hpevtFaltDetHotswpCoreIO.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFaltDetHotswpCoreIO.setStatus(
        ""
    )

hpevtErrRetrvCrssbarChipNmbr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12109)
)
hpevtErrRetrvCrssbarChipNmbr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtErrRetrvCrssbarChipNmbr.setStatus(
        ""
    )

hpevtCellNotCfgCLMMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12119)
)
hpevtCellNotCfgCLMMode.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCellNotCfgCLMMode.setStatus(
        ""
    )

hpevttDoblDramInvoke = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12120)
)
hpevttDoblDramInvoke.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevttDoblDramInvoke.setStatus(
        ""
    )

hpevtErrCrssbarCrctByHW = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12121)
)
hpevtErrCrssbarCrctByHW.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtErrCrssbarCrctByHW.setStatus(
        ""
    )

hpevtErrCrssChipBckPln = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12127)
)
hpevtErrCrssChipBckPln.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtErrCrssChipBckPln.setStatus(
        ""
    )

hpevtErrCeLLIO = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12128)
)
hpevtErrCeLLIO.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtErrCeLLIO.setStatus(
        ""
    )

hpevtMltPltFrmErrCellBckPln = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12129)
)
hpevtMltPltFrmErrCellBckPln.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMltPltFrmErrCellBckPln.setStatus(
        ""
    )

hpevtMultPltFrmErrCrssChpBckPln = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12130)
)
hpevtMultPltFrmErrCrssChpBckPln.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMultPltFrmErrCrssChpBckPln.setStatus(
        ""
    )

hpevtMultPltFrmErrCeLLIO = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12131)
)
hpevtMultPltFrmErrCeLLIO.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMultPltFrmErrCeLLIO.setStatus(
        ""
    )

hpevtServIDNotMatchCab = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12132)
)
hpevtServIDNotMatchCab.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtServIDNotMatchCab.setStatus(
        ""
    )

hpevtDupDimNumDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12135)
)
hpevtDupDimNumDetect.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtDupDimNumDetect.setStatus(
        ""
    )

hpevtMPLostUPS = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12143)
)
hpevtMPLostUPS.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMPLostUPS.setStatus(
        ""
    )

hpevtMPGainLanCommUPS = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12144)
)
hpevtMPGainLanCommUPS.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMPGainLanCommUPS.setStatus(
        ""
    )

hpevtUnrecovProcIFAinterptInFW = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12149)
)
hpevtUnrecovProcIFAinterptInFW.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUnrecovProcIFAinterptInFW.setStatus(
        ""
    )

hpevtUnrecovProcISRinterptInFW = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12150)
)
hpevtUnrecovProcISRinterptInFW.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUnrecovProcISRinterptInFW.setStatus(
        ""
    )

hpevtDblChipSpareInvoked = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12153)
)
hpevtDblChipSpareInvoked.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtDblChipSpareInvoked.setStatus(
        ""
    )

hpevtExtClkCablRemvFrmCPUCab = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12155)
)
hpevtExtClkCablRemvFrmCPUCab.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtExtClkCablRemvFrmCPUCab.setStatus(
        ""
    )

hpevtSysFabEncntLnkErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12156)
)
hpevtSysFabEncntLnkErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSysFabEncntLnkErr.setStatus(
        ""
    )

hpevtFatErrOnCelToFabPrt44I32I1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12157)
)
hpevtFatErrOnCelToFabPrt44I32I1.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFatErrOnCelToFabPrt44I32I1.setStatus(
        ""
    )

hpevtSysFWgetFabProblm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12159)
)
hpevtSysFWgetFabProblm.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSysFWgetFabProblm.setStatus(
        ""
    )

hpevtFatErrCelLnkToFabPrt44I32 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12160)
)
hpevtFatErrCelLnkToFabPrt44I32.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFatErrCelLnkToFabPrt44I32.setStatus(
        ""
    )

hpevtSysOSRecovFrmPCIErrL1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12161)
)
hpevtSysOSRecovFrmPCIErrL1.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSysOSRecovFrmPCIErrL1.setStatus(
        ""
    )

hpevtSysOSRecovFrmPCIErrL2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12162)
)
hpevtSysOSRecovFrmPCIErrL2.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSysOSRecovFrmPCIErrL2.setStatus(
        ""
    )

hpevtSysOSRecovFrmPCIErrL5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12163)
)
hpevtSysOSRecovFrmPCIErrL5.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSysOSRecovFrmPCIErrL5.setStatus(
        ""
    )

hpevtReqPwrOnDenied = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12164)
)
hpevtReqPwrOnDenied.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtReqPwrOnDenied.setStatus(
        ""
    )

hpevtBladeFrcPWon = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12165)
)
hpevtBladeFrcPWon.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBladeFrcPWon.setStatus(
        ""
    )

hpevtMPNotRecvRespEnclMangr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12168)
)
hpevtMPNotRecvRespEnclMangr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMPNotRecvRespEnclMangr.setStatus(
        ""
    )

hpevtIntrnlSwErr7193 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12193)
)
hpevtIntrnlSwErr7193.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIntrnlSwErr7193.setStatus(
        ""
    )

hpevtIntrnlSwErr7194 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12194)
)
hpevtIntrnlSwErr7194.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIntrnlSwErr7194.setStatus(
        ""
    )

hpevtIntrnlSwErr7195 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12195)
)
hpevtIntrnlSwErr7195.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIntrnlSwErr7195.setStatus(
        ""
    )

hpevtIntrnlSwErr7196 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12196)
)
hpevtIntrnlSwErr7196.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIntrnlSwErr7196.setStatus(
        ""
    )

hpevtComplxProfNoMtch = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12199)
)
hpevtComplxProfNoMtch.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtComplxProfNoMtch.setStatus(
        ""
    )

hpevtIODevMissCore = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12204)
)
hpevtIODevMissCore.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIODevMissCore.setStatus(
        ""
    )

hpevtFparUnablNotiCPU = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12207)
)
hpevtFparUnablNotiCPU.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFparUnablNotiCPU.setStatus(
        ""
    )

hpevtFparUnablNotiCpuIOSAPICredir = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12208)
)
hpevtFparUnablNotiCpuIOSAPICredir.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFparUnablNotiCpuIOSAPICredir.setStatus(
        ""
    )

hpevtOSSetWtchDogTimerToTimeOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12210)
)
hpevtOSSetWtchDogTimerToTimeOut.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtOSSetWtchDogTimerToTimeOut.setStatus(
        ""
    )

hpevtOSShtDwnDueMCA = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12217)
)
hpevtOSShtDwnDueMCA.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtOSShtDwnDueMCA.setStatus(
        ""
    )

hpevtOSShtDwnDuePanic = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12218)
)
hpevtOSShtDwnDuePanic.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtOSShtDwnDuePanic.setStatus(
        ""
    )

hpevtCLUFWIncomptblSysType = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12222)
)
hpevtCLUFWIncomptblSysType.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCLUFWIncomptblSysType.setStatus(
        ""
    )

hpevtOnlnIdentHWProb = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12227)
)
hpevtOnlnIdentHWProb.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtOnlnIdentHWProb.setStatus(
        ""
    )

hpevtProcOvTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12228)
)
hpevtProcOvTemp.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtProcOvTemp.setStatus(
        ""
    )

hpevtErrChkFabBootStat = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12229)
)
hpevtErrChkFabBootStat.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtErrChkFabBootStat.setStatus(
        ""
    )

hpevtSysFwUnblClrLnkErrMsk = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12230)
)
hpevtSysFwUnblClrLnkErrMsk.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSysFwUnblClrLnkErrMsk.setStatus(
        ""
    )

hpevtSysFwNotDetLnkAdrr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12231)
)
hpevtSysFwNotDetLnkAdrr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSysFwNotDetLnkAdrr.setStatus(
        ""
    )

hpevtSysFwUnblTurnBadLnkOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12232)
)
hpevtSysFwUnblTurnBadLnkOff.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSysFwUnblTurnBadLnkOff.setStatus(
        ""
    )

hpevtWindWtchDogXpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12244)
)
hpevtWindWtchDogXpired.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtWindWtchDogXpired.setStatus(
        ""
    )

hpevtMPCtrlReprtMPBusCommFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12251)
)
hpevtMPCtrlReprtMPBusCommFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMPCtrlReprtMPBusCommFail.setStatus(
        ""
    )

hpevt12VPCIFailonIOChass = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12255)
)
hpevt12VPCIFailonIOChass.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevt12VPCIFailonIOChass.setStatus(
        ""
    )

hpevtSFWDetFailOptmzFab = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12289)
)
hpevtSFWDetFailOptmzFab.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtSFWDetFailOptmzFab.setStatus(
        ""
    )

hpevtCritFailCellOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12291)
)
hpevtCritFailCellOnline.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCritFailCellOnline.setStatus(
        ""
    )

hpevtCellHasIncomptbleHwFW = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12296)
)
hpevtCellHasIncomptbleHwFW.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCellHasIncomptbleHwFW.setStatus(
        ""
    )

hpevtCellFWnotMatchPartFW = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12297)
)
hpevtCellFWnotMatchPartFW.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCellFWnotMatchPartFW.setStatus(
        ""
    )

hpevtVMSDetctUnrecvrdEvnt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12319)
)
hpevtVMSDetctUnrecvrdEvnt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtVMSDetctUnrecvrdEvnt.setStatus(
        ""
    )

hpevtBadCellBrdOrBadProcBrd = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12324)
)
hpevtBadCellBrdOrBadProcBrd.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBadCellBrdOrBadProcBrd.setStatus(
        ""
    )

hpevtCPUDegradErrThirdCache = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12343)
)
hpevtCPUDegradErrThirdCache.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCPUDegradErrThirdCache.setStatus(
        ""
    )

hpevtROMFailAuthentc = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12352)
)
hpevtROMFailAuthentc.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtROMFailAuthentc.setStatus(
        ""
    )

hpevtAltrntROMUnblSwap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12354)
)
hpevtAltrntROMUnblSwap.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtAltrntROMUnblSwap.setStatus(
        ""
    )

hpevtPciSlotErrDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12358)
)
hpevtPciSlotErrDetect.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPciSlotErrDetect.setStatus(
        ""
    )

hpevtCCLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12394)
)
hpevtCCLinkDown.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtCCLinkDown.setStatus(
        ""
    )

hpevtUnrecovProcIntOccr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12395)
)
hpevtUnrecovProcIntOccr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUnrecovProcIntOccr.setStatus(
        ""
    )

hpevtElectrncKeyProblm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12399)
)
hpevtElectrncKeyProblm.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtElectrncKeyProblm.setStatus(
        ""
    )

hpevtBldeInstImproperLoc = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12400)
)
hpevtBldeInstImproperLoc.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBldeInstImproperLoc.setStatus(
        ""
    )

hpevtbldeInstViolateEnclre = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12401)
)
hpevtbldeInstViolateEnclre.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtbldeInstViolateEnclre.setStatus(
        ""
    )

hpevtsx2000FabRprtUnexpctErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12403)
)
hpevtsx2000FabRprtUnexpctErr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtsx2000FabRprtUnexpctErr.setStatus(
        ""
    )

hpevtOANotServPwrOnReqst = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12408)
)
hpevtOANotServPwrOnReqst.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtOANotServPwrOnReqst.setStatus(
        ""
    )

hpevtIOBckPlnReprtNonRedundncyPCIPwr = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12411)
)
hpevtIOBckPlnReprtNonRedundncyPCIPwr.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtIOBckPlnReprtNonRedundncyPCIPwr.setStatus(
        ""
    )

hpevtUSBStorAttch = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12503)
)
hpevtUSBStorAttch.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUSBStorAttch.setStatus(
        ""
    )

hpevtUSBStorRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12504)
)
hpevtUSBStorRemoved.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUSBStorRemoved.setStatus(
        ""
    )

hpevtMigratSrcNotConnt = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12547)
)
hpevtMigratSrcNotConnt.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMigratSrcNotConnt.setStatus(
        ""
    )

hpevtMigratFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12548)
)
hpevtMigratFail.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMigratFail.setStatus(
        ""
    )

hpevtMigratNotSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12550)
)
hpevtMigratNotSuccess.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtMigratNotSuccess.setStatus(
        ""
    )

hpevtVMNotAlloctMemForIO = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12551)
)
hpevtVMNotAlloctMemForIO.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtVMNotAlloctMemForIO.setStatus(
        ""
    )

hpevtUnSupprtDimmInPartition = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12557)
)
hpevtUnSupprtDimmInPartition.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtUnSupprtDimmInPartition.setStatus(
        ""
    )

hpevtRuntimeCritShtDwn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12560)
)
hpevtRuntimeCritShtDwn.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtRuntimeCritShtDwn.setStatus(
        ""
    )

hpevtPwrExptGreatrPwrBulk = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12586)
)
hpevtPwrExptGreatrPwrBulk.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtPwrExptGreatrPwrBulk.setStatus(
        ""
    )

hpevtBulkPwrReduncLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12589)
)
hpevtBulkPwrReduncLost.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtBulkPwrReduncLost.setStatus(
        ""
    )

hpevtACReduncLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12591)
)
hpevtACReduncLost.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtACReduncLost.setStatus(
        ""
    )

hpevtFanCoolNotRedunc = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12593)
)
hpevtFanCoolNotRedunc.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFanCoolNotRedunc.setStatus(
        ""
    )

hpevtFanInsufficientInCoolDomain = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12595)
)
hpevtFanInsufficientInCoolDomain.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFanInsufficientInCoolDomain.setStatus(
        ""
    )

hpevtOSNotUseAllProcs = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12627)
)
hpevtOSNotUseAllProcs.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtOSNotUseAllProcs.setStatus(
        ""
    )

hpevtFMPUnexpctRstHasRcv = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 35, 0, 12863)
)
hpevtFMPUnexpctRstHasRcv.setObjects(
    ("HPIPFTRAP-MIB", "hpIpfEvtDetailStr")
)
if mibBuilder.loadTexts:
    hpevtFMPUnexpctRstHasRcv.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPIPFTRAP-MIB",
    **{"hp": hp,
       "nm": nm,
       "hpnsa": hpnsa,
       "hpIpfE0Events": hpIpfE0Events,
       "hpevtBadOsInitChecksum": hpevtBadOsInitChecksum,
       "hpevtBadOsMcaChecksum": hpevtBadOsMcaChecksum,
       "hpevtBootBmcFailed": hpevtBootBmcFailed,
       "hpevtBootCellLaunchEfiFailure": hpevtBootCellLaunchEfiFailure,
       "hpevtBootCellMonSelFailure": hpevtBootCellMonSelFailure,
       "hpevtBootCellMonarchCollision": hpevtBootCellMonarchCollision,
       "hpevtBootCellVirtualizeEfiFailure": hpevtBootCellVirtualizeEfiFailure,
       "hpevtBootCellVirtualizePalFailure": hpevtBootCellVirtualizePalFailure,
       "hpevtBootCellVirtualizeSalFailure": hpevtBootCellVirtualizeSalFailure,
       "hpevtBootCellVirtualizeSalprocFailure": hpevtBootCellVirtualizeSalprocFailure,
       "hpevtBootCpuConfigFail": hpevtBootCpuConfigFail,
       "hpevtBootCpuEarlyConfigFail": hpevtBootCpuEarlyConfigFail,
       "hpevtBootCpuEarlyTestFail": hpevtBootCpuEarlyTestFail,
       "hpevtBootCpuFailed": hpevtBootCpuFailed,
       "hpevtBootCpuLateTestFail": hpevtBootCpuLateTestFail,
       "hpevtBootCpuLateTestInsufficientMem": hpevtBootCpuLateTestInsufficientMem,
       "hpevtBootEfiAllocateError": hpevtBootEfiAllocateError,
       "hpevtBootEfiImageCorrupt": hpevtBootEfiImageCorrupt,
       "hpevtBootEfiNotInFit": hpevtBootEfiNotInFit,
       "hpevtBootEfiNvmFail": hpevtBootEfiNvmFail,
       "hpevtBootEfiRomBadSize": hpevtBootEfiRomBadSize,
       "hpevtBootEfiRomXsumError": hpevtBootEfiRomXsumError,
       "hpevtBootExtIntNestLimitedExceeded": hpevtBootExtIntNestLimitedExceeded,
       "hpevtBootExtIntNotServiced": hpevtBootExtIntNotServiced,
       "hpevtBootExtIntTaken": hpevtBootExtIntTaken,
       "hpevtBootFplFailed": hpevtBootFplFailed,
       "hpevtBootGetPsrFailure": hpevtBootGetPsrFailure,
       "hpevtBootHaltCell": hpevtBootHaltCell,
       "hpevtBootIncompatiblePal": hpevtBootIncompatiblePal,
       "hpevtBootIncompatibleSlave": hpevtBootIncompatibleSlave,
       "hpevtBootIntrptClearFailure": hpevtBootIntrptClearFailure,
       "hpevtBootIpmiEventFailed": hpevtBootIpmiEventFailed,
       "hpevtBootIvtOffset": hpevtBootIvtOffset,
       "hpevtBootLdbStateBad": hpevtBootLdbStateBad,
       "hpevtBootLostContextInt": hpevtBootLostContextInt,
       "hpevtBootMinStateRegError": hpevtBootMinStateRegError,
       "hpevtBootMonarchTimeout": hpevtBootMonarchTimeout,
       "hpevtBootNoPalBInFit": hpevtBootNoPalBInFit,
       "hpevtBootNoSalBInFit": hpevtBootNoSalBInFit,
       "hpevtBootNvmFail": hpevtBootNvmFail,
       "hpevtBootOutOfRangeVector": hpevtBootOutOfRangeVector,
       "hpevtBootPalCopyInfoError": hpevtBootPalCopyInfoError,
       "hpevtBootPalCopyPalError": hpevtBootPalCopyPalError,
       "hpevtBootPalProcFailure": hpevtBootPalProcFailure,
       "hpevtBootPlatConsoleDevFailed": hpevtBootPlatConsoleDevFailed,
       "hpevtBootPlatIntfcDevFailed": hpevtBootPlatIntfcDevFailed,
       "hpevtBootPlatScrBad": hpevtBootPlatScrBad,
       "hpevtBootRendezFailure": hpevtBootRendezFailure,
       "hpevtBootSalExtractError": hpevtBootSalExtractError,
       "hpevtBootScrFail": hpevtBootScrFail,
       "hpevtBootSelFull": hpevtBootSelFull,
       "hpevtBootSlaveNoFinalWakeupVector": hpevtBootSlaveNoFinalWakeupVector,
       "hpevtBootSlaveRendezHandlerFail": hpevtBootSlaveRendezHandlerFail,
       "hpevtBootSmbiosBuildError": hpevtBootSmbiosBuildError,
       "hpevtBootTrapNestLimitedExceeded": hpevtBootTrapNestLimitedExceeded,
       "hpevtBootTrapNotServiced": hpevtBootTrapNotServiced,
       "hpevtBootTrapTaken": hpevtBootTrapTaken,
       "hpevtBootUnclearedInt": hpevtBootUnclearedInt,
       "hpevtBootUnexpectedExtIntPostRedirTable": hpevtBootUnexpectedExtIntPostRedirTable,
       "hpevtBootUnexpectedIntPreRedirTable": hpevtBootUnexpectedIntPreRedirTable,
       "hpevtBootUnexpectedMca": hpevtBootUnexpectedMca,
       "hpevtBootUnexpectedTrapPostRedirTable": hpevtBootUnexpectedTrapPostRedirTable,
       "hpevtBootUnknownFailure": hpevtBootUnknownFailure,
       "hpevtErrorsPalFailure": hpevtErrorsPalFailure,
       "hpevtExpMcNotRegistered": hpevtExpMcNotRegistered,
       "hpevtInitInitiated": hpevtInitInitiated,
       "hpevtIoCheckLbaMissingErr": hpevtIoCheckLbaMissingErr,
       "hpevtIoCheckNumSlotsErr": hpevtIoCheckNumSlotsErr,
       "hpevtIoCheckRopeWidthErr": hpevtIoCheckRopeWidthErr,
       "hpevtIoCheckXtraLbaFoundErr": hpevtIoCheckXtraLbaFoundErr,
       "hpevtIoDllError": hpevtIoDllError,
       "hpevtIoHotPlugCtrlFailed": hpevtIoHotPlugCtrlFailed,
       "hpevtIoInvalidRopeBundle": hpevtIoInvalidRopeBundle,
       "hpevtIoLbaClearErrFailed": hpevtIoLbaClearErrFailed,
       "hpevtIoLbaResetError": hpevtIoLbaResetError,
       "hpevtIoNotEnoughPowerError": hpevtIoNotEnoughPowerError,
       "hpevtIoPciMappingFailed": hpevtIoPciMappingFailed,
       "hpevtIoPciMappingTooBig": hpevtIoPciMappingTooBig,
       "hpevtIoPciUnmappingFailed": hpevtIoPciUnmappingFailed,
       "hpevtIoPcixcapSampleError": hpevtIoPcixcapSampleError,
       "hpevtIoPmNotRespondingError": hpevtIoPmNotRespondingError,
       "hpevtIoRopeResetError": hpevtIoRopeResetError,
       "hpevtIoSbaClearErrFailed": hpevtIoSbaClearErrFailed,
       "hpevtIoSlotPowerDefaultError": hpevtIoSlotPowerDefaultError,
       "hpevtIoSlotPowerOnError": hpevtIoSlotPowerOnError,
       "hpevtIoSlotStandbyPowerError": hpevtIoSlotStandbyPowerError,
       "hpevtIoUnknownPcixcapVal": hpevtIoUnknownPcixcapVal,
       "hpevtIoUnsupRopeFreq": hpevtIoUnsupRopeFreq,
       "hpevtIoUnsupportedLba": hpevtIoUnsupportedLba,
       "hpevtMcInitiated": hpevtMcInitiated,
       "hpevtMdtConstructAreaBad": hpevtMdtConstructAreaBad,
       "hpevtMdtLmmioEntryNotFound": hpevtMdtLmmioEntryNotFound,
       "hpevtMdtPageZeroBad": hpevtMdtPageZeroBad,
       "hpevtMdtUnableToFindSpace": hpevtMdtUnableToFindSpace,
       "hpevtMediaFailure": hpevtMediaFailure,
       "hpevtMemBibRegFailure": hpevtMemBibRegFailure,
       "hpevtMemCacheLine0WrRdFailed": hpevtMemCacheLine0WrRdFailed,
       "hpevtMemDimmLoadOrderErr": hpevtMemDimmLoadOrderErr,
       "hpevtMemDimmSpdChecksum": hpevtMemDimmSpdChecksum,
       "hpevtMemDimmSpdFatal": hpevtMemDimmSpdFatal,
       "hpevtMemDimmTypeIncompatible": hpevtMemDimmTypeIncompatible,
       "hpevtMemDimmTypeMismatch": hpevtMemDimmTypeMismatch,
       "hpevtMemDimmTypeTableFull": hpevtMemDimmTypeTableFull,
       "hpevtMemDmtEntryNotFound": hpevtMemDmtEntryNotFound,
       "hpevtMemEccMbeDataTstFailed": hpevtMemEccMbeDataTstFailed,
       "hpevtMemEccMbeSignalTstFailed": hpevtMemEccMbeSignalTstFailed,
       "hpevtMemEccSbeDataTstFailed": hpevtMemEccSbeDataTstFailed,
       "hpevtMemEccSbeEccTstFailed": hpevtMemEccSbeEccTstFailed,
       "hpevtMemEnoughMemFailed": hpevtMemEnoughMemFailed,
       "hpevtMemErrAddrNotInMbat": hpevtMemErrAddrNotInMbat,
       "hpevtMemErrClearFail": hpevtMemErrClearFail,
       "hpevtMemErrLogFailedToClear": hpevtMemErrLogFailedToClear,
       "hpevtMemErrorRegClearFailure": hpevtMemErrorRegClearFailure,
       "hpevtMemExtFatalLoadOrdErr": hpevtMemExtFatalLoadOrdErr,
       "hpevtMemFirmwareProb": hpevtMemFirmwareProb,
       "hpevtMemInterleaveCodeFailure": hpevtMemInterleaveCodeFailure,
       "hpevtMemMainMemFailed": hpevtMemMainMemFailed,
       "hpevtMemMbeInRank": hpevtMemMbeInRank,
       "hpevtMemMcRegFailure": hpevtMemMcRegFailure,
       "hpevtMemNoDimmsInstalled": hpevtMemNoDimmsInstalled,
       "hpevtMemNoMemFound": hpevtMemNoMemFound,
       "hpevtMemPdtDisabledHalt": hpevtMemPdtDisabledHalt,
       "hpevtMemPdtDisabledWarning": hpevtMemPdtDisabledWarning,
       "hpevtMemPdtNvmErr": hpevtMemPdtNvmErr,
       "hpevtMemPdtTableFull": hpevtMemPdtTableFull,
       "hpevtMemPlatformInitFailure": hpevtMemPlatformInitFailure,
       "hpevtMemRankEntryNotFound": hpevtMemRankEntryNotFound,
       "hpevtMemTestExcessMcBits": hpevtMemTestExcessMcBits,
       "hpevtMemTestFwdProgBitsInvalid": hpevtMemTestFwdProgBitsInvalid,
       "hpevtMemTestStatusBitsInvalid": hpevtMemTestStatusBitsInvalid,
       "hpevtMemTestSummaryBitsInvalid": hpevtMemTestSummaryBitsInvalid,
       "hpevtMemUnexpectedMca": hpevtMemUnexpectedMca,
       "hpevtMemWarnDistributionCheckBypass": hpevtMemWarnDistributionCheckBypass,
       "hpevtMemWarnLoadingOrderBypass": hpevtMemWarnLoadingOrderBypass,
       "hpevtMemWarnLoopOnDestTest": hpevtMemWarnLoopOnDestTest,
       "hpevtMemWarnSetCheckBypass": hpevtMemWarnSetCheckBypass,
       "hpevtMemWarnSpdBypass": hpevtMemWarnSpdBypass,
       "hpevtMemWarnUsingAltConfig": hpevtMemWarnUsingAltConfig,
       "hpevtOsInitNotRegistered": hpevtOsInitNotRegistered,
       "hpevtOsMcaNotRegistered": hpevtOsMcaNotRegistered,
       "hpevtOsMcaUncorrectedMc": hpevtOsMcaUncorrectedMc,
       "hpevtPdhMiscRegFail": hpevtPdhMiscRegFail,
       "hpevtSalCheckUnknownFail": hpevtSalCheckUnknownFail,
       "hpevtSalInitUnknownFail": hpevtSalInitUnknownFail,
       "hpevtUndefinedSmcInterleaveErr": hpevtUndefinedSmcInterleaveErr,
       "hpevtUnexpectedRetToSalCheck": hpevtUnexpectedRetToSalCheck,
       "hpevtUnexpectedRetToSalInit": hpevtUnexpectedRetToSalInit,
       "hpevtFwInstalledCpuDegraded": hpevtFwInstalledCpuDegraded,
       "hpevtPdRendezTreeError": hpevtPdRendezTreeError,
       "hpevtPdCellConfigError": hpevtPdCellConfigError,
       "hpevtPdRemoteCsrReadError": hpevtPdRemoteCsrReadError,
       "hpevtPdCellLateForRendez": hpevtPdCellLateForRendez,
       "hpevtPdIncompatibleCpuTypes": hpevtPdIncompatibleCpuTypes,
       "hpevtPdCellLateLocalRendezSet": hpevtPdCellLateLocalRendezSet,
       "hpevtCellNotInGlobalSet": hpevtCellNotInGlobalSet,
       "hpevtNoViableCoreCellInPd": hpevtNoViableCoreCellInPd,
       "hpevtErrorPromotingCoreCell": hpevtErrorPromotingCoreCell,
       "hpevtFabricNoServiceProviders": hpevtFabricNoServiceProviders,
       "hpevtFabricPortError": hpevtFabricPortError,
       "hpevtFabricReadError": hpevtFabricReadError,
       "hpevtFabricWriteError": hpevtFabricWriteError,
       "hpevtXbcSlicesHwVersionDiffer": hpevtXbcSlicesHwVersionDiffer,
       "hpevtXbcSlicesInDiffLocation": hpevtXbcSlicesInDiffLocation,
       "hpevtMonarchTakeover": hpevtMonarchTakeover,
       "hpevtDeadSram": hpevtDeadSram,
       "hpevtDeadDillon": hpevtDeadDillon,
       "hpevtDeadPdhHw": hpevtDeadPdhHw,
       "hpevtIoPciBusMixedSpeeds": hpevtIoPciBusMixedSpeeds,
       "hpevtIoPciBusDepthExceeded": hpevtIoPciBusDepthExceeded,
       "hpevtlotimeout": hpevtlotimeout,
       "hpevtIoBuswalkSuperio": hpevtIoBuswalkSuperio,
       "hpevtIoSbaCorrDataParityErr": hpevtIoSbaCorrDataParityErr,
       "hpevtIoSbaFatalDataParityErr": hpevtIoSbaFatalDataParityErr,
       "hpevtIoSbaUncFunctionErr": hpevtIoSbaUncFunctionErr,
       "hpevtIoSbaFatalFunctionErr": hpevtIoSbaFatalFunctionErr,
       "hpevtIoSbaFatalParityErr": hpevtIoSbaFatalParityErr,
       "hpevtIoSbaFatalMapErr": hpevtIoSbaFatalMapErr,
       "hpevtIoSbaFatalTimeoutErr": hpevtIoSbaFatalTimeoutErr,
       "hpevtIoLbaInitErr": hpevtIoLbaInitErr,
       "hpevtIoLbaCorrTimeoutErr": hpevtIoLbaCorrTimeoutErr,
       "hpevtIoLbaUncFunctionErr": hpevtIoLbaUncFunctionErr,
       "hpevtIoLbaUncTimeoutErr": hpevtIoLbaUncTimeoutErr,
       "hpevtIoLbaMiscUncErr": hpevtIoLbaMiscUncErr,
       "hpevtIoLbaUncParityErr": hpevtIoLbaUncParityErr,
       "hpevtIoLbaMiscFatalErr": hpevtIoLbaMiscFatalErr,
       "hpevtIoLbaFatalFunctionErr": hpevtIoLbaFatalFunctionErr,
       "hpevtIoLbaFatalParityErr": hpevtIoLbaFatalParityErr,
       "hpevtIoLbaFatalTimeoutErr": hpevtIoLbaFatalTimeoutErr,
       "hpevtIoDevAdapterMiscUncErr": hpevtIoDevAdapterMiscUncErr,
       "hpevtIoDevAdapterMiscFatalErr": hpevtIoDevAdapterMiscFatalErr,
       "hpevtMemDimmSpdExtendedChecksum": hpevtMemDimmSpdExtendedChecksum,
       "hpevtOptsHdrCksumError": hpevtOptsHdrCksumError,
       "hpevtOptsDataCksumError": hpevtOptsDataCksumError,
       "hpevtPdMemIntlvWaysMismatch": hpevtPdMemIntlvWaysMismatch,
       "hpevtPdMemUnintlvdMemory": hpevtPdMemUnintlvdMemory,
       "hpevtPdMemNoMemoryDesc": hpevtPdMemNoMemoryDesc,
       "hpevtPdMemUpdateLocalCellFailed": hpevtPdMemUpdateLocalCellFailed,
       "hpevtPdMemPdtAddrNotFound": hpevtPdMemPdtAddrNotFound,
       "hpevtPdMemPdtInstallFail": hpevtPdMemPdtInstallFail,
       "hpevtUnusableResource": hpevtUnusableResource,
       "hpevtFwError": hpevtFwError,
       "hpevtNvramDataCmpError": hpevtNvramDataCmpError,
       "hpevtNvramCrcError": hpevtNvramCrcError,
       "hpevtErm": hpevtErm,
       "hpevtErrorObtainingSemaphore": hpevtErrorObtainingSemaphore,
       "hpevtNvramBlockRevMismatch": hpevtNvramBlockRevMismatch,
       "hpevtNvramBlockNotFound": hpevtNvramBlockNotFound,
       "hpevtNvramBlockLocked": hpevtNvramBlockLocked,
       "hpevtNvramBlockUnlocked": hpevtNvramBlockUnlocked,
       "hpevtNvramHeaderNotFound": hpevtNvramHeaderNotFound,
       "hpevtNvmFreelistCorrupt": hpevtNvmFreelistCorrupt,
       "hpevtResetForReconfig": hpevtResetForReconfig,
       "hpevtPdRendezUtilityError": hpevtPdRendezUtilityError,
       "hpevtHalt": hpevtHalt,
       "hpevtDuiNoConsole": hpevtDuiNoConsole,
       "hpevtErrorProcFailed": hpevtErrorProcFailed,
       "hpevtReconfigResetFail": hpevtReconfigResetFail,
       "hpevtPdErrorReachableSet": hpevtPdErrorReachableSet,
       "hpevtIoBridgeDepthExceeded": hpevtIoBridgeDepthExceeded,
       "hpevtEfiConsoleDriverError": hpevtEfiConsoleDriverError,
       "hpevtMemTestCodeInPage0Corrupt": hpevtMemTestCodeInPage0Corrupt,
       "hpevtRemoteCellStateUnknown": hpevtRemoteCellStateUnknown,
       "hpevtPdMltplCoreCells": hpevtPdMltplCoreCells,
       "hpevtUtilSendCommandError": hpevtUtilSendCommandError,
       "hpevtUtilCellSlotError": hpevtUtilCellSlotError,
       "hpevtMcCellRendezFailed": hpevtMcCellRendezFailed,
       "hpevtMcNoAccessToPd": hpevtMcNoAccessToPd,
       "hpevtMcLossOfLockstep": hpevtMcLossOfLockstep,
       "hpevtMcPdCellRendezFailed": hpevtMcPdCellRendezFailed,
       "hpevtMcProcErrHalt": hpevtMcProcErrHalt,
       "hpevtMcCellMonarchTimeout": hpevtMcCellMonarchTimeout,
       "hpevtMcPdCellMissedRendez": hpevtMcPdCellMissedRendez,
       "hpevtMcPdMonarchTimeout": hpevtMcPdMonarchTimeout,
       "hpevtRemoteSetViewRootError": hpevtRemoteSetViewRootError,
       "hpevtCsrTestFailure": hpevtCsrTestFailure,
       "hpevtPdMemGetIcmInfoFailed": hpevtPdMemGetIcmInfoFailed,
       "hpevtPdMemGetCellInfoFailed": hpevtPdMemGetCellInfoFailed,
       "hpevtPdMemUpdateCellGniFailed": hpevtPdMemUpdateCellGniFailed,
       "hpevtPdMemAdjustMinZiFailed": hpevtPdMemAdjustMinZiFailed,
       "hpevtStableProfileXsumError": hpevtStableProfileXsumError,
       "hpevtDynamicProfileXsumError": hpevtDynamicProfileXsumError,
       "hpevtPartitionProfileXsumError": hpevtPartitionProfileXsumError,
       "hpevtStableProfileSeqidInvalid": hpevtStableProfileSeqidInvalid,
       "hpevtDynamicProfileSeqidInvalid": hpevtDynamicProfileSeqidInvalid,
       "hpevtPartitionProfileSeqidInvalid": hpevtPartitionProfileSeqidInvalid,
       "hpevtEfiFwError": hpevtEfiFwError,
       "hpevtCmplxProfilePdNumMismatch": hpevtCmplxProfilePdNumMismatch,
       "hpevtCmplxProfilePdNumInvalid": hpevtCmplxProfilePdNumInvalid,
       "hpevtXbcPortSm4Error": hpevtXbcPortSm4Error,
       "hpevtXbcPortSm4NotReleased": hpevtXbcPortSm4NotReleased,
       "hpevtBootBmcTokenUploadFailure": hpevtBootBmcTokenUploadFailure,
       "hpevtBootNvmTokenAccessFailure": hpevtBootNvmTokenAccessFailure,
       "hpevtBootBmcTokenDownloadError": hpevtBootBmcTokenDownloadError,
       "hpevtBootErrorWritingFirstBootToken": hpevtBootErrorWritingFirstBootToken,
       "hpevtBootFruReadError": hpevtBootFruReadError,
       "hpevtBootFruXsumError": hpevtBootFruXsumError,
       "hpevtBootFruVersionError": hpevtBootFruVersionError,
       "hpevtBootRomRevToFitRevWarning": hpevtBootRomRevToFitRevWarning,
       "hpevtBootRomRevToRevBlockWarning": hpevtBootRomRevToRevBlockWarning,
       "hpevtBootPrimaryFitBad": hpevtBootPrimaryFitBad,
       "hpevtBootSecondaryFitBad": hpevtBootSecondaryFitBad,
       "hpevtBootPalARomWarning": hpevtBootPalARomWarning,
       "hpevtBootPalBRomWarning": hpevtBootPalBRomWarning,
       "hpevtErrorUpdatingGroupBProfile": hpevtErrorUpdatingGroupBProfile,
       "hpevtIoPciPerr": hpevtIoPciPerr,
       "hpevtIoPciSerr": hpevtIoPciSerr,
       "hpevtIoCheckLbaDeconfigErr": hpevtIoCheckLbaDeconfigErr,
       "hpevtErrorUpdatingGroupCProfile": hpevtErrorUpdatingGroupCProfile,
       "hpevtCellNotInAPd": hpevtCellNotInAPd,
       "hpevtMemDimmThermalLoadOrderWarn": hpevtMemDimmThermalLoadOrderWarn,
       "hpevtCellMajorityNotPresent": hpevtCellMajorityNotPresent,
       "hpevtInitRendezvousSlavesFail": hpevtInitRendezvousSlavesFail,
       "hpevtMcIoClearFail": hpevtMcIoClearFail,
       "hpevtMcPalCantEscalateToBerr": hpevtMcPalCantEscalateToBerr,
       "hpevtMcPalCantEscalateToBinit": hpevtMcPalCantEscalateToBinit,
       "hpevtMcPalGetFeatFail": hpevtMcPalGetFeatFail,
       "hpevtMcPalRendFail": hpevtMcPalRendFail,
       "hpevtMcPalSetFeatFail": hpevtMcPalSetFeatFail,
       "hpevtMcRendezvousSlavesFail": hpevtMcRendezvousSlavesFail,
       "hpevtMcRendezBadVectRange": hpevtMcRendezBadVectRange,
       "hpevtMcRendezNoMonarch": hpevtMcRendezNoMonarch,
       "hpevtMcRendezNoWakeup": hpevtMcRendezNoWakeup,
       "hpevtMcRendezPalCantEscalate": hpevtMcRendezPalCantEscalate,
       "hpevtMcRendezPalGetFeatFail": hpevtMcRendezPalGetFeatFail,
       "hpevtMcRendezPalSetFeatFail": hpevtMcRendezPalSetFeatFail,
       "hpevtSalAbiFwError": hpevtSalAbiFwError,
       "hpevtMemExtLoadOrdErr": hpevtMemExtLoadOrdErr,
       "hpevtEfiEsiTableLengthErr": hpevtEfiEsiTableLengthErr,
       "hpevtEfiEsiTableChecksumErr": hpevtEfiEsiTableChecksumErr,
       "hpevtEfiEsiTableUnsupportedEntryType": hpevtEfiEsiTableUnsupportedEntryType,
       "hpevtEfiGuidTooLarge": hpevtEfiGuidTooLarge,
       "hpevtEfiHalt": hpevtEfiHalt,
       "hpevtMemChipspareNotSupported": hpevtMemChipspareNotSupported,
       "hpevtEfiAssertError": hpevtEfiAssertError,
       "hpevtEfiEfiBreakpoint": hpevtEfiEfiBreakpoint,
       "hpevtEfiHcdHostHung": hpevtEfiHcdHostHung,
       "hpevtEfiSalHandoffVerMismatch": hpevtEfiSalHandoffVerMismatch,
       "hpevtEfiSalRtcServiceNotInit": hpevtEfiSalRtcServiceNotInit,
       "hpevtEfiSalTimerServiceNotInit": hpevtEfiSalTimerServiceNotInit,
       "hpevtEfiSalStarttimerServiceNotInit": hpevtEfiSalStarttimerServiceNotInit,
       "hpevtEfiNoIoPortSpaceRegionFound": hpevtEfiNoIoPortSpaceRegionFound,
       "hpevtEfiBreakpoint": hpevtEfiBreakpoint,
       "hpevtEfiSpeedyBootTokenNotRead": hpevtEfiSpeedyBootTokenNotRead,
       "hpevtEfiSalCallbackAttempted": hpevtEfiSalCallbackAttempted,
       "hpevtEfiSalFreqBaseUnknown": hpevtEfiSalFreqBaseUnknown,
       "hpevtEfiSysEventAlreadyInit": hpevtEfiSysEventAlreadyInit,
       "hpevtEfiSysEventCreateEventFail": hpevtEfiSysEventCreateEventFail,
       "hpevtFpgaNodeInitError": hpevtFpgaNodeInitError,
       "hpevtIoconfigNodeInitError": hpevtIoconfigNodeInitError,
       "hpevtDillonPdhNodeInitError": hpevtDillonPdhNodeInitError,
       "hpevtPdhPropertyError": hpevtPdhPropertyError,
       "hpevtPdhAcpihwNodeError": hpevtPdhAcpihwNodeError,
       "hpevtPdhIpmiNodeError": hpevtPdhIpmiNodeError,
       "hpevtBootCpusNotCompatible": hpevtBootCpusNotCompatible,
       "hpevtBootCacheSizesInconsistant": hpevtBootCacheSizesInconsistant,
       "hpevtBootSelectingNewMonarch": hpevtBootSelectingNewMonarch,
       "hpevtBootMonSelSteppingsNoEqual": hpevtBootMonSelSteppingsNoEqual,
       "hpevtBootCpuOverClocked": hpevtBootCpuOverClocked,
       "hpevtBootCpuInfoRomAccessError": hpevtBootCpuInfoRomAccessError,
       "hpevtBootPalANotExecuted": hpevtBootPalANotExecuted,
       "hpevtBootPalBNotExecuted": hpevtBootPalBNotExecuted,
       "hpevtBootProtoTypeCpuInstalled": hpevtBootProtoTypeCpuInstalled,
       "hpevtBootFinalRendezWatchdogFail": hpevtBootFinalRendezWatchdogFail,
       "hpevtCpuSupplementalTestFailed": hpevtCpuSupplementalTestFailed,
       "hpevtFabricReadMbeError": hpevtFabricReadMbeError,
       "hpevtFabricUnexpectedStatus": hpevtFabricUnexpectedStatus,
       "hpevtEfiSysidBmcWarning": hpevtEfiSysidBmcWarning,
       "hpevtEfiSysidBmcReadError": hpevtEfiSysidBmcReadError,
       "hpevtEfiSysidBmcWriteError": hpevtEfiSysidBmcWriteError,
       "hpevtEfiSysidInvalid": hpevtEfiSysidInvalid,
       "hpevtEfiRtIvtEsiTableErr": hpevtEfiRtIvtEsiTableErr,
       "hpevtEfiRtIvtEsiQueryErr": hpevtEfiRtIvtEsiQueryErr,
       "hpevtEfiBootIvtEsiTableErr": hpevtEfiBootIvtEsiTableErr,
       "hpevtEfiBootIvtEsiQueryErr": hpevtEfiBootIvtEsiQueryErr,
       "hpevtUtilitiesParmListTooLarge": hpevtUtilitiesParmListTooLarge,
       "hpevtXbcPortPresenceError": hpevtXbcPortPresenceError,
       "hpevtXbcPortHwLinkError": hpevtXbcPortHwLinkError,
       "hpevtXbcPortFeError": hpevtXbcPortFeError,
       "hpevtXinLinkInitError": hpevtXinLinkInitError,
       "hpevtXinLinkInitFailed": hpevtXinLinkInitFailed,
       "hpevtEfiGetMfgModeNotInit": hpevtEfiGetMfgModeNotInit,
       "hpevtEfiBmcMfgModeInvalid": hpevtEfiBmcMfgModeInvalid,
       "hpevtEfiEnterMfgModeNotInit": hpevtEfiEnterMfgModeNotInit,
       "hpevtEfiExitMfgModeNotInit": hpevtEfiExitMfgModeNotInit,
       "hpevtEfiTaccessServiceNotInit": hpevtEfiTaccessServiceNotInit,
       "hpevtTreeNodeNotFound": hpevtTreeNodeNotFound,
       "hpevtEfiSystemStateRunningErr": hpevtEfiSystemStateRunningErr,
       "hpevtPalBusConfigIncompatible": hpevtPalBusConfigIncompatible,
       "hpevtPalGetBusFeaturesFailed": hpevtPalGetBusFeaturesFailed,
       "hpevtMemDimmPairMismatch": hpevtMemDimmPairMismatch,
       "hpevtEfiPosseLibNotInit": hpevtEfiPosseLibNotInit,
       "hpevtEfiSecurityNotInit": hpevtEfiSecurityNotInit,
       "hpevtEfiSecInvalidSysmode": hpevtEfiSecInvalidSysmode,
       "hpevtEfiSecSetPassLevelErr": hpevtEfiSecSetPassLevelErr,
       "hpevtMdtBad": hpevtMdtBad,
       "hpevtBootCpuBadCoreFixedRatio": hpevtBootCpuBadCoreFixedRatio,
       "hpevtBootAllCpusSlatedForCompatDeconfig": hpevtBootAllCpusSlatedForCompatDeconfig,
       "hpevtXbcReadRemoteRouteError": hpevtXbcReadRemoteRouteError,
       "hpevtXbcReadNeighborInfoError": hpevtXbcReadNeighborInfoError,
       "hpevtMemDimmQuadMismatch": hpevtMemDimmQuadMismatch,
       "hpevtMemDimmFailed": hpevtMemDimmFailed,
       "hpevtXbcPortOeError": hpevtXbcPortOeError,
       "hpevtXbcPortStatusError": hpevtXbcPortStatusError,
       "hpevtXbcPortLandmined": hpevtXbcPortLandmined,
       "hpevtPdIncompatibleCpuSpeeds": hpevtPdIncompatibleCpuSpeeds,
       "hpevtFabricCellLinkNotInit": hpevtFabricCellLinkNotInit,
       "hpevtFabricInvalidXbcNum": hpevtFabricInvalidXbcNum,
       "hpevtFabricInvalidXbcPortNum": hpevtFabricInvalidXbcPortNum,
       "hpevtUtilitiesLedParamError": hpevtUtilitiesLedParamError,
       "hpevtFabricUnexpectedNtype": hpevtFabricUnexpectedNtype,
       "hpevtFabricPortNotCc": hpevtFabricPortNotCc,
       "hpevtFabricPortNotXbc": hpevtFabricPortNotXbc,
       "hpevtFabricUnexpectedNChip": hpevtFabricUnexpectedNChip,
       "hpevtFabricUnexpectedNPort": hpevtFabricUnexpectedNPort,
       "hpevtBootNvmWriteToBmcTokenFailure": hpevtBootNvmWriteToBmcTokenFailure,
       "hpevtUtilitiesLedError": hpevtUtilitiesLedError,
       "hpevtDuplicateCpuIds": hpevtDuplicateCpuIds,
       "hpevtHp-uxCrashdumpStarted": hpevtHp_uxCrashdumpStarted,
       "hpevtHp-uxHexFaultCode": hpevtHp_uxHexFaultCode,
       "hpevtHp-uxDumpStatus": hpevtHp_uxDumpStatus,
       "hpevtSettingProcTimeoutFail": hpevtSettingProcTimeoutFail,
       "hpevtEfiSecInitVerifyErr": hpevtEfiSecInitVerifyErr,
       "hpevtEfiSecInitCloseErr": hpevtEfiSecInitCloseErr,
       "hpevtEfiSecInitOpenErr": hpevtEfiSecInitOpenErr,
       "hpevtEfiSecInitWriteErr": hpevtEfiSecInitWriteErr,
       "hpevtEfiSecInitWriteDenied": hpevtEfiSecInitWriteDenied,
       "hpevtHp-uxDumpWriteError": hpevtHp_uxDumpWriteError,
       "hpevtErrDeadlockResetDetected": hpevtErrDeadlockResetDetected,
       "hpevtMemParityErr": hpevtMemParityErr,
       "hpevtMemDimmLoadOrdErr": hpevtMemDimmLoadOrdErr,
       "hpevtMemRefreshStartError": hpevtMemRefreshStartError,
       "hpevtMemExtBaseboardIncompatible": hpevtMemExtBaseboardIncompatible,
       "hpevtFabricDifferentTopologies": hpevtFabricDifferentTopologies,
       "hpevtFabricInvalidXbc2XbcPort": hpevtFabricInvalidXbc2XbcPort,
       "hpevtFabricGetNeighborInfoError": hpevtFabricGetNeighborInfoError,
       "hpevtXbcRoutingErrorState": hpevtXbcRoutingErrorState,
       "hpevtNoNvmErrLogSpace": hpevtNoNvmErrLogSpace,
       "hpevtXbcPortError": hpevtXbcPortError,
       "hpevtXbcPortRouteAround": hpevtXbcPortRouteAround,
       "hpevtXbcUnexpectedState": hpevtXbcUnexpectedState,
       "hpevtXbcRoutingStateTimeout": hpevtXbcRoutingStateTimeout,
       "hpevtXbcNeighborPortNotRoutable": hpevtXbcNeighborPortNotRoutable,
       "hpevtFabricCcToXbcError": hpevtFabricCcToXbcError,
       "hpevtFabricRouteXbcError": hpevtFabricRouteXbcError,
       "hpevtFabricMaxBrokenLinks": hpevtFabricMaxBrokenLinks,
       "hpevtXbcSemaphoreTakeoverFailed": hpevtXbcSemaphoreTakeoverFailed,
       "hpevtXbcForceUnlockSm4Timeout": hpevtXbcForceUnlockSm4Timeout,
       "hpevtXbcGetGlobalSm4Timeout": hpevtXbcGetGlobalSm4Timeout,
       "hpevtXbcReleaseSm4Timeout": hpevtXbcReleaseSm4Timeout,
       "hpevtMpBatteryFailure": hpevtMpBatteryFailure,
       "hpevtMpSoftwareError": hpevtMpSoftwareError,
       "hpevtMpI2cCommError": hpevtMpI2cCommError,
       "hpevtRomCrcError": hpevtRomCrcError,
       "hpevtIoIdentifyIoBpFailed": hpevtIoIdentifyIoBpFailed,
       "hpevtCpuRevisionMismatch": hpevtCpuRevisionMismatch,
       "hpevtCpuFreqMismatch": hpevtCpuFreqMismatch,
       "hpevtCpuOverclocked": hpevtCpuOverclocked,
       "hpevtCmplxProfilIncoherent": hpevtCmplxProfilIncoherent,
       "hpevtDuplicateCabinet": hpevtDuplicateCabinet,
       "hpevtIdCommandRequired": hpevtIdCommandRequired,
       "hpevtNvramBatteryFail": hpevtNvramBatteryFail,
       "hpevtPartitionTimeoutReset": hpevtPartitionTimeoutReset,
       "hpevtPdhcWatchdogTimedOut": hpevtPdhcWatchdogTimedOut,
       "hpevtAbortPowerupOth": hpevtAbortPowerupOth,
       "hpevtAbortPwrupBps": hpevtAbortPwrupBps,
       "hpevtAbortStartBlowr": hpevtAbortStartBlowr,
       "hpevtAbortStartIofan": hpevtAbortStartIofan,
       "hpevtAcDeleted": hpevtAcDeleted,
       "hpevtBlowrFail": hpevtBlowrFail,
       "hpevtBpsFail48flt": hpevtBpsFail48flt,
       "hpevtBpsFailFanflt": hpevtBpsFailFanflt,
       "hpevtBpsFailOt": hpevtBpsFailOt,
       "hpevtBpsNotRedundant": hpevtBpsNotRedundant,
       "hpevtBpsOvervoltage": hpevtBpsOvervoltage,
       "hpevtBpsUndervoltage": hpevtBpsUndervoltage,
       "hpevtCabFanFail": hpevtCabFanFail,
       "hpevtHkpOvervoltage": hpevtHkpOvervoltage,
       "hpevtHkpUndervoltage": hpevtHkpUndervoltage,
       "hpevtIllegalBpsCfgOrPhaseFlt": hpevtIllegalBpsCfgOrPhaseFlt,
       "hpevtIllegalBpsid": hpevtIllegalBpsid,
       "hpevtInletOvertempHi": hpevtInletOvertempHi,
       "hpevtInletOvertempLo": hpevtInletOvertempLo,
       "hpevtInletOvertempMid": hpevtInletOvertempMid,
       "hpevtIofanFail": hpevtIofanFail,
       "hpevtPowerOverload": hpevtPowerOverload,
       "hpevtShutdownBlowr": hpevtShutdownBlowr,
       "hpevtShutdownIofan": hpevtShutdownIofan,
       "hpevtXucFanFail": hpevtXucFanFail,
       "hpevtCluWatchdogReset": hpevtCluWatchdogReset,
       "hpevtEepromInvalidCksm": hpevtEepromInvalidCksm,
       "hpevtHbpbBoardPowerFault": hpevtHbpbBoardPowerFault,
       "hpevtHiobEepromRdFail": hpevtHiobEepromRdFail,
       "hpevtHiopbEepromRdFail": hpevtHiopbEepromRdFail,
       "hpevtHiopbLpmFltRdFail": hpevtHiopbLpmFltRdFail,
       "hpevtHiopbOvertemp": hpevtHiopbOvertemp,
       "hpevtHiopbPowerFault": hpevtHiopbPowerFault,
       "hpevtHiopbVoltMrgnFail": hpevtHiopbVoltMrgnFail,
       "hpevtSbchEepromRdFail": hpevtSbchEepromRdFail,
       "hpevtUguyEepromRdFail": hpevtUguyEepromRdFail,
       "hpevtSysBkpEepromRdFail": hpevtSysBkpEepromRdFail,
       "hpevtSysBkpI2cRdFail": hpevtSysBkpI2cRdFail,
       "hpevtSysBkpI2cWrFail": hpevtSysBkpI2cWrFail,
       "hpevtSysBkpPowerFault": hpevtSysBkpPowerFault,
       "hpevtSysBkpVoltMrgnFail": hpevtSysBkpVoltMrgnFail,
       "hpevtWriteFruDataFail": hpevtWriteFruDataFail,
       "hpevtCpuFanFail": hpevtCpuFanFail,
       "hpevtCpuFanSlow": hpevtCpuFanSlow,
       "hpevtDnaFanFail": hpevtDnaFanFail,
       "hpevtDnaFanSlow": hpevtDnaFanSlow,
       "hpevtPdhcToSysfwRevMismtch": hpevtPdhcToSysfwRevMismtch,
       "hpevtPdhCtrlrFwMismatch": hpevtPdhCtrlrFwMismatch,
       "hpevtCellPowerFault": hpevtCellPowerFault,
       "hpevtCpuInitNodeError": hpevtCpuInitNodeError,
       "hpevtCpuExecuteCmdError": hpevtCpuExecuteCmdError,
       "hpevtCpuCmdStateInvalid": hpevtCpuCmdStateInvalid,
       "hpevtCpuPalProcError": hpevtCpuPalProcError,
       "hpevtBootCpuLoadingError": hpevtBootCpuLoadingError,
       "hpevtXbcPersistantError": hpevtXbcPersistantError,
       "hpevtXbcLinkTestError": hpevtXbcLinkTestError,
       "hpevtPltfrmStorageReadErr": hpevtPltfrmStorageReadErr,
       "hpevtPltfrmStorageWriteErr": hpevtPltfrmStorageWriteErr,
       "hpevtTreeNodeErrorSequencer": hpevtTreeNodeErrorSequencer,
       "hpevtPartitionVariableError": hpevtPartitionVariableError,
       "hpevtCellRedundtPowerFault": hpevtCellRedundtPowerFault,
       "hpevtPalProcConfigIncompatible": hpevtPalProcConfigIncompatible,
       "hpevtPalGetProcFeaturesFailed": hpevtPalGetProcFeaturesFailed,
       "hpevtPdhcCriticalDebug": hpevtPdhcCriticalDebug,
       "hpevtCluUndefinedCase": hpevtCluUndefinedCase,
       "hpevtCellVoltageMarginUnkn": hpevtCellVoltageMarginUnkn,
       "hpevtPdhcAssertionFailed": hpevtPdhcAssertionFailed,
       "hpevtPdhcFirmwareUnknownErr": hpevtPdhcFirmwareUnknownErr,
       "hpevtPdhcI2cWriteFailed": hpevtPdhcI2cWriteFailed,
       "hpevtPdhcI2cReadFailed": hpevtPdhcI2cReadFailed,
       "hpevtPdhcSmbusWriteFailed": hpevtPdhcSmbusWriteFailed,
       "hpevtPdhcSmbusReadFailed": hpevtPdhcSmbusReadFailed,
       "hpevtFrequencyProgramFailed": hpevtFrequencyProgramFailed,
       "hpevtSysFwFlashUpdateError": hpevtSysFwFlashUpdateError,
       "hpevtPdhcUnexpectedReset": hpevtPdhcUnexpectedReset,
       "hpevtCpuTmpSensorSetupFail": hpevtCpuTmpSensorSetupFail,
       "hpevtCpuModuleThermalert": hpevtCpuModuleThermalert,
       "hpevtPdhcFlashUpdateError": hpevtPdhcFlashUpdateError,
       "hpevtCellTypMismatchWSysfw": hpevtCellTypMismatchWSysfw,
       "hpevtPdhcPdhArbiterTimeout": hpevtPdhcPdhArbiterTimeout,
       "hpevtPdhcGetSm4Timeout": hpevtPdhcGetSm4Timeout,
       "hpevtIpmiBmc2hostMsgFailure": hpevtIpmiBmc2hostMsgFailure,
       "hpevtEfiDebugLevelTokenErr": hpevtEfiDebugLevelTokenErr,
       "hpevtXbcPortNotLandmined": hpevtXbcPortNotLandmined,
       "hpevtFabricValidateError": hpevtFabricValidateError,
       "hpevtFabricISRInvalidBkp": hpevtFabricISRInvalidBkp,
       "hpevtFabricXinWrZeroErrMaskError": hpevtFabricXinWrZeroErrMaskError,
       "hpevtFabricCcPriModeRegRdStatus": hpevtFabricCcPriModeRegRdStatus,
       "hpevtFabricCcPriModeRegRdData": hpevtFabricCcPriModeRegRdData,
       "hpevtFabricCcErrMaskRegRdStatus": hpevtFabricCcErrMaskRegRdStatus,
       "hpevtFabricCcErrMaskRegRdData": hpevtFabricCcErrMaskRegRdData,
       "hpevtFabricXingNeighborPortBad": hpevtFabricXingNeighborPortBad,
       "hpevtFabricISRRdFwdProgErr": hpevtFabricISRRdFwdProgErr,
       "hpevtFabricGetNeighborMaxLinksBroken": hpevtFabricGetNeighborMaxLinksBroken,
       "hpevtPmAssertionFailed": hpevtPmAssertionFailed,
       "hpevtPmFirmwareUnknownErr": hpevtPmFirmwareUnknownErr,
       "hpevtPmCriticalDebug": hpevtPmCriticalDebug,
       "hpevtFabricLinkCorErrTestFailure": hpevtFabricLinkCorErrTestFailure,
       "hpevtInvalidCabinetNumber": hpevtInvalidCabinetNumber,
       "hpevtPdIncompatibleFwRevs": hpevtPdIncompatibleFwRevs,
       "hpevtPmI2cWriteFailed": hpevtPmI2cWriteFailed,
       "hpevtPmI2cReadFailed": hpevtPmI2cReadFailed,
       "hpevtCellInfoError": hpevtCellInfoError,
       "hpevtSlaveConsoleSetupError": hpevtSlaveConsoleSetupError,
       "hpevtRegistryMoveToCoreCellError": hpevtRegistryMoveToCoreCellError,
       "hpevtProfileGroupCCrcError": hpevtProfileGroupCCrcError,
       "hpevtMcCoreCellSelectFail": hpevtMcCoreCellSelectFail,
       "hpevtFabricAssertFabricUtils": hpevtFabricAssertFabricUtils,
       "hpevtSalPmiFwError": hpevtSalPmiFwError,
       "hpevtOlaWrongNumberCells": hpevtOlaWrongNumberCells,
       "hpevtFabricXbcRouteSourceCellPortErr": hpevtFabricXbcRouteSourceCellPortErr,
       "hpevtBootOlaCellIncompatible": hpevtBootOlaCellIncompatible,
       "hpevtBootOlaCellDidNotReachRendezvous": hpevtBootOlaCellDidNotReachRendezvous,
       "hpevtBootOlaCellStillAtBib": hpevtBootOlaCellStillAtBib,
       "hpevtBootOlaCellUnexpectedCellState": hpevtBootOlaCellUnexpectedCellState,
       "hpevtBootOlaCellCantReachAliveCells": hpevtBootOlaCellCantReachAliveCells,
       "hpevtBootMixedCpuCoreFreqInstalled": hpevtBootMixedCpuCoreFreqInstalled,
       "hpevtXinInitIntermittentFailure": hpevtXinInitIntermittentFailure,
       "hpevtPdhErrClearOlaSteeringBit": hpevtPdhErrClearOlaSteeringBit,
       "hpevtBootOlaFailedUpdatePdAddrMap": hpevtBootOlaFailedUpdatePdAddrMap,
       "hpevtBootOlaFailedUpdatePdPdt": hpevtBootOlaFailedUpdatePdPdt,
       "hpevtBootOlaFailedUpdateCellMap": hpevtBootOlaFailedUpdateCellMap,
       "hpevtFabricCc2XbcLinkInitFailed": hpevtFabricCc2XbcLinkInitFailed,
       "hpevtFwVirtualMappingError": hpevtFwVirtualMappingError,
       "hpevtFabricXinInitWriteErr": hpevtFabricXinInitWriteErr,
       "hpevtFabricXinInitReadErr": hpevtFabricXinInitReadErr,
       "hpevtFabricLinkInitIntermittentFailure": hpevtFabricLinkInitIntermittentFailure,
       "hpevtIodiscPciInitnodeError": hpevtIodiscPciInitnodeError,
       "hpevtIodiscPciBusscanError": hpevtIodiscPciBusscanError,
       "hpevtIodiscPciInitbridgeError": hpevtIodiscPciInitbridgeError,
       "hpevtIodiscPciIomapError": hpevtIodiscPciIomapError,
       "hpevtIodiscPciMmiomapError": hpevtIodiscPciMmiomapError,
       "hpevtIodiscSbaInitnodeError": hpevtIodiscSbaInitnodeError,
       "hpevtIodiscSbaDiscoverError": hpevtIodiscSbaDiscoverError,
       "hpevtIodiscSbaResetError": hpevtIodiscSbaResetError,
       "hpevtIodiscIolinkError": hpevtIodiscIolinkError,
       "hpevtIodiscCableError": hpevtIodiscCableError,
       "hpevtIodiscIoChassisPower": hpevtIodiscIoChassisPower,
       "hpevtIodiscLbaInitnodeError": hpevtIodiscLbaInitnodeError,
       "hpevtIodiscLbaWidthError": hpevtIodiscLbaWidthError,
       "hpevtIodiscLbaPhaseError": hpevtIodiscLbaPhaseError,
       "hpevtIodiscLbaClearError": hpevtIodiscLbaClearError,
       "hpevtIodiscLbaLogError": hpevtIodiscLbaLogError,
       "hpevtIodiscLbaDiscoverError": hpevtIodiscLbaDiscoverError,
       "hpevtIodiscLbaConfigError": hpevtIodiscLbaConfigError,
       "hpevtIodiscLbaPciscanError": hpevtIodiscLbaPciscanError,
       "hpevtIodiscLbaPciconfigError": hpevtIodiscLbaPciconfigError,
       "hpevtBootOlaCellErrAccessCmplxProfile": hpevtBootOlaCellErrAccessCmplxProfile,
       "hpevtBootFwRelocMemErr": hpevtBootFwRelocMemErr,
       "hpevtBootOlaCellNotConfigInCmplxProfile": hpevtBootOlaCellNotConfigInCmplxProfile,
       "hpevtOptsNvmAllocError": hpevtOptsNvmAllocError,
       "hpevtBootOlaUpdateRtcFailedOlaCell": hpevtBootOlaUpdateRtcFailedOlaCell,
       "hpevtSalInfoTimeout": hpevtSalInfoTimeout,
       "hpevtPdhIprNotClearedOnCell": hpevtPdhIprNotClearedOnCell,
       "hpevtPdhIprClearAttempts": hpevtPdhIprClearAttempts,
       "hpevtBootOlaUpdateRtcFailedExistingCell": hpevtBootOlaUpdateRtcFailedExistingCell,
       "hpevtMemIncompleteEchelon": hpevtMemIncompleteEchelon,
       "hpevtFabricRdPortStatePortInvalid": hpevtFabricRdPortStatePortInvalid,
       "hpevtFabricWrPortStatePortInvalid": hpevtFabricWrPortStatePortInvalid,
       "hpevtMainBpLpmFlt": hpevtMainBpLpmFlt,
       "hpevtIoBpLpmFlt": hpevtIoBpLpmFlt,
       "hpevtCmplxProfileInitFailed": hpevtCmplxProfileInitFailed,
       "hpevtPalSetProcFeaturesFailed": hpevtPalSetProcFeaturesFailed,
       "hpevtActiveLogNotFound": hpevtActiveLogNotFound,
       "hpevtReachedMaxErrorLogs": hpevtReachedMaxErrorLogs,
       "hpevtOldNoCellToDelete": hpevtOldNoCellToDelete,
       "hpevtBpsOvercurrent": hpevtBpsOvercurrent,
       "hpevtBpsWarnOt": hpevtBpsWarnOt,
       "hpevtErmOutOfHeap": hpevtErmOutOfHeap,
       "hpevtMemDimmUnsupported": hpevtMemDimmUnsupported,
       "hpevtOptsMallocError": hpevtOptsMallocError,
       "hpevtCellHwDegraded": hpevtCellHwDegraded,
       "hpevtNotIntegratingCell": hpevtNotIntegratingCell,
       "hpevtIoContextCorruptErr": hpevtIoContextCorruptErr,
       "hpevtIoRopeFatal": hpevtIoRopeFatal,
       "hpevtIoBusFatal": hpevtIoBusFatal,
       "hpevtIoRopeUnitFatal": hpevtIoRopeUnitFatal,
       "hpevtPdhFlashWriteEnableBitSetNowCleared": hpevtPdhFlashWriteEnableBitSetNowCleared,
       "hpevtFirmwareInitError": hpevtFirmwareInitError,
       "hpevtMcIncompleteCpuSet": hpevtMcIncompleteCpuSet,
       "hpevtMcIncompleteCellSet": hpevtMcIncompleteCellSet,
       "hpevtMcTreeCheckFailed": hpevtMcTreeCheckFailed,
       "hpevtMcRegistryCheckFailed": hpevtMcRegistryCheckFailed,
       "hpevtMcDuringOsMca": hpevtMcDuringOsMca,
       "hpevtMcMemDumpAbandon": hpevtMcMemDumpAbandon,
       "hpevtMcFwTreeNotComplete": hpevtMcFwTreeNotComplete,
       "hpevtAcpiConfigMismatch": hpevtAcpiConfigMismatch,
       "hpevtFabricXinErrOrderStatusClrFailed": hpevtFabricXinErrOrderStatusClrFailed,
       "hpevtFabricAssertFabricInit": hpevtFabricAssertFabricInit,
       "hpevtInvalidPiromData": hpevtInvalidPiromData,
       "hpevtSettingFreqRatiosError": hpevtSettingFreqRatiosError,
       "hpevtOptsBlockCksumError": hpevtOptsBlockCksumError,
       "hpevtFabricColaLocalCcLinkNotInit": hpevtFabricColaLocalCcLinkNotInit,
       "hpevtFabricXinInitDisableWrError": hpevtFabricXinInitDisableWrError,
       "hpevtFabricXinErrMaskUnknownBkp": hpevtFabricXinErrMaskUnknownBkp,
       "hpevtFabricXinWrErrMaskError": hpevtFabricXinWrErrMaskError,
       "hpevtFabricXinRdErrMaskError": hpevtFabricXinRdErrMaskError,
       "hpevtFabricInitCcLinkFailure": hpevtFabricInitCcLinkFailure,
       "hpevtResetCommandError": hpevtResetCommandError,
       "hpevtFabricInitCcLinkDisableErr": hpevtFabricInitCcLinkDisableErr,
       "hpevtFabricSetPortStateGetSm4Err": hpevtFabricSetPortStateGetSm4Err,
       "hpevtFabricSetPortStateRlsSm4Err": hpevtFabricSetPortStateRlsSm4Err,
       "hpevtFabricAssertFabricErr": hpevtFabricAssertFabricErr,
       "hpevtFabricXinLinkAlreadyInit": hpevtFabricXinLinkAlreadyInit,
       "hpevtNoCpuModulesFoundByPdhc": hpevtNoCpuModulesFoundByPdhc,
       "hpevtCpuModCompatMismatch": hpevtCpuModCompatMismatch,
       "hpevtBadCpuModScratchCksum": hpevtBadCpuModScratchCksum,
       "hpevtPdhBatteryLowWarning": hpevtPdhBatteryLowWarning,
       "hpevtFabricRouteXbcCopyRoutingErr": hpevtFabricRouteXbcCopyRoutingErr,
       "hpevtFabricCopyRdBackFailed": hpevtFabricCopyRdBackFailed,
       "hpevtFabricRtgCompleteSm4RlsErr": hpevtFabricRtgCompleteSm4RlsErr,
       "hpevtFabricRtgCompleteWrFwdPrgErr": hpevtFabricRtgCompleteWrFwdPrgErr,
       "hpevtFabricRtgCompleteSm4AccessErr": hpevtFabricRtgCompleteSm4AccessErr,
       "hpevtFabricRtgCompleteTopologyErr": hpevtFabricRtgCompleteTopologyErr,
       "hpevtFabricRouteTraversableCc2CcErr": hpevtFabricRouteTraversableCc2CcErr,
       "hpevtFabricDataRouteTraversableCc2CcErr": hpevtFabricDataRouteTraversableCc2CcErr,
       "hpevtFabricCc2ccTraverseLclXinRdErr": hpevtFabricCc2ccTraverseLclXinRdErr,
       "hpevtFabricCc2ccTraverseRmtXinRdErr": hpevtFabricCc2ccTraverseRmtXinRdErr,
       "hpevtFabricCc2ccTraverseLclNotInit": hpevtFabricCc2ccTraverseLclNotInit,
       "hpevtFabricCc2ccTraverseRmtNotInit": hpevtFabricCc2ccTraverseRmtNotInit,
       "hpevtFabricDisableXinLinkReadErr": hpevtFabricDisableXinLinkReadErr,
       "hpevtFabricXinInitRetryReadErr": hpevtFabricXinInitRetryReadErr,
       "hpevtFabricAssertFabricCc": hpevtFabricAssertFabricCc,
       "hpevtCpuRestricted": hpevtCpuRestricted,
       "hpevtPdhInvalidRtcCleared": hpevtPdhInvalidRtcCleared,
       "hpevtLstNotRun": hpevtLstNotRun,
       "hpevtBootSetCellStateFabricFailure": hpevtBootSetCellStateFabricFailure,
       "hpevtBootResetCellStateFailure": hpevtBootResetCellStateFailure,
       "hpevtMemChipspareDeallocRank": hpevtMemChipspareDeallocRank,
       "hpevtClockFreqError": hpevtClockFreqError,
       "hpevtFabricColaInitTraversableErr": hpevtFabricColaInitTraversableErr,
       "hpevtFabricAttemptFocusedReroute": hpevtFabricAttemptFocusedReroute,
       "hpevtFabricCellRerouteNinfoErr": hpevtFabricCellRerouteNinfoErr,
       "hpevtBootWakeCpuIsCpuDeconfigErr": hpevtBootWakeCpuIsCpuDeconfigErr,
       "hpevtBootWakeCpuGetCountersErr": hpevtBootWakeCpuGetCountersErr,
       "hpevtBootWakeCpuGetStructAddrErr": hpevtBootWakeCpuGetStructAddrErr,
       "hpevtBootCheckCpu4CompletionErr": hpevtBootCheckCpu4CompletionErr,
       "hpevtBootCheckCpuGetStructAddrErr": hpevtBootCheckCpuGetStructAddrErr,
       "hpevtReconfigResetScheduled": hpevtReconfigResetScheduled,
       "hpevtProfileWrongArchType": hpevtProfileWrongArchType,
       "hpevtBootCheckCpuIsDeconfigErr": hpevtBootCheckCpuIsDeconfigErr,
       "hpevtBootCheckCpuGetCountersErr": hpevtBootCheckCpuGetCountersErr,
       "hpevtBootPdMonarchRtnFromSwSetFpErr": hpevtBootPdMonarchRtnFromSwSetFpErr,
       "hpevtBootSlaveRtnFromFwSetFpErr": hpevtBootSlaveRtnFromFwSetFpErr,
       "hpevtBootProblemBranchingToPgzLocation": hpevtBootProblemBranchingToPgzLocation,
       "hpevtBootBadCpuOrder": hpevtBootBadCpuOrder,
       "hpevtBootSlpWakeCntrsStructAddrErr": hpevtBootSlpWakeCntrsStructAddrErr,
       "hpevtBootGetSleepTimeoutStructAddrErr": hpevtBootGetSleepTimeoutStructAddrErr,
       "hpevtBootMoveSlavesDispatcherAddrErr": hpevtBootMoveSlavesDispatcherAddrErr,
       "hpevtBootMoveSlavesCheckSlaveErr": hpevtBootMoveSlavesCheckSlaveErr,
       "hpevtBootMoveSlavesFpSetAddrErr": hpevtBootMoveSlavesFpSetAddrErr,
       "hpevtBootMoveSlavesFpSetErr": hpevtBootMoveSlavesFpSetErr,
       "hpevtBootMoveCellMonarchsStructAddrErr": hpevtBootMoveCellMonarchsStructAddrErr,
       "hpevtBootMoveCellMonarchsCheckSlaveErr": hpevtBootMoveCellMonarchsCheckSlaveErr,
       "hpevtBootMoveCellMonarchsFpSetAddrErr": hpevtBootMoveCellMonarchsFpSetAddrErr,
       "hpevtBootMoveCellMonarchsFpSetErr": hpevtBootMoveCellMonarchsFpSetErr,
       "hpevtBootDualCoreInitFail": hpevtBootDualCoreInitFail,
       "hpevtBootDeconfigCpuModulePair": hpevtBootDeconfigCpuModulePair,
       "hpevtBootVirtualizeDualCoreRegistersFail": hpevtBootVirtualizeDualCoreRegistersFail,
       "hpevtBootVirtualizeDualCoreInterposerFail": hpevtBootVirtualizeDualCoreInterposerFail,
       "hpevtBootInstallPmiHandlerFailed": hpevtBootInstallPmiHandlerFailed,
       "hpevtPdhcCellIncompatable": hpevtPdhcCellIncompatable,
       "hpevtPdhcPdhNotAvailable": hpevtPdhcPdhNotAvailable,
       "hpevtPdhcMponFailed": hpevtPdhcMponFailed,
       "hpevtPdhcDillonResetFailed": hpevtPdhcDillonResetFailed,
       "hpevtPdhcDmdClockFailed": hpevtPdhcDmdClockFailed,
       "hpevtAllCpusDeconfOnCell": hpevtAllCpusDeconfOnCell,
       "hpevtFabricLogRoutingRdErr": hpevtFabricLogRoutingRdErr,
       "hpevtFabricLinkRendezDisableErr": hpevtFabricLinkRendezDisableErr,
       "hpevtAcDeletedA0": hpevtAcDeletedA0,
       "hpevtAcDeletedA1": hpevtAcDeletedA1,
       "hpevtAcDeletedB0": hpevtAcDeletedB0,
       "hpevtAcDeletedB1": hpevtAcDeletedB1,
       "hpevtFabricCc2CcLinkDisableErr": hpevtFabricCc2CcLinkDisableErr,
       "hpevtFabricISREarlyCopyRoutingErr": hpevtFabricISREarlyCopyRoutingErr,
       "hpevtFabricClrLinkInitBitErrMaskRd": hpevtFabricClrLinkInitBitErrMaskRd,
       "hpevtFabricClrLinkInitBitErrMaskWr": hpevtFabricClrLinkInitBitErrMaskWr,
       "hpevtFabricPortPairRdPstatusErr": hpevtFabricPortPairRdPstatusErr,
       "hpevtPdhBatteryPowerLow": hpevtPdhBatteryPowerLow,
       "hpevtNoHandoffToOsMca": hpevtNoHandoffToOsMca,
       "hpevtBootRtnFromSwCantGetCounters": hpevtBootRtnFromSwCantGetCounters,
       "hpevtBootRtnFromSwCpuNotAsleep": hpevtBootRtnFromSwCpuNotAsleep,
       "hpevtBootDeconfigAbsentCantSetCpuState": hpevtBootDeconfigAbsentCantSetCpuState,
       "hpevtNvramBlockTableCorrupt": hpevtNvramBlockTableCorrupt,
       "hpevtBootMoveSlavesSetTimeoutErr": hpevtBootMoveSlavesSetTimeoutErr,
       "hpevtBootReconfigAllCpus": hpevtBootReconfigAllCpus,
       "hpevtBootGetNumcoresFailure": hpevtBootGetNumcoresFailure,
       "hpevtFabricRmtRoutePortTopoErr": hpevtFabricRmtRoutePortTopoErr,
       "hpevtFabricCellRerouteFailure": hpevtFabricCellRerouteFailure,
       "hpevtFabricRdFailedLinksError": hpevtFabricRdFailedLinksError,
       "hpevtFabricWrFailedLinksRdError": hpevtFabricWrFailedLinksRdError,
       "hpevtFabricWrFailedLinksWrError": hpevtFabricWrFailedLinksWrError,
       "hpevtFabricIncFailedLinksRdError": hpevtFabricIncFailedLinksRdError,
       "hpevtFabricIncFailedLinksWrError": hpevtFabricIncFailedLinksWrError,
       "hpevtFabricIncFailedLinksHitLimit": hpevtFabricIncFailedLinksHitLimit,
       "hpevtFabricRtgCompleteRdFldLinksErr": hpevtFabricRtgCompleteRdFldLinksErr,
       "hpevtFabricRtgCompleteWrFldLinksErr": hpevtFabricRtgCompleteWrFldLinksErr,
       "hpevtFabricCellRerouteRdXbcErr": hpevtFabricCellRerouteRdXbcErr,
       "hpevtFabricCellRerouteNbrNotReachable": hpevtFabricCellRerouteNbrNotReachable,
       "hpevtFabricCellRerouteSm4RlsErr": hpevtFabricCellRerouteSm4RlsErr,
       "hpevtFabricRmtRoutePortBcastWrErr": hpevtFabricRmtRoutePortBcastWrErr,
       "hpevtFabricRmtRoutePortRdErr": hpevtFabricRmtRoutePortRdErr,
       "hpevtFabricRmtRoutePortWrErr": hpevtFabricRmtRoutePortWrErr,
       "hpevtIoLinkSubsystemFailed": hpevtIoLinkSubsystemFailed,
       "hpevtIoSbaSubsystemFailed": hpevtIoSbaSubsystemFailed,
       "hpevtIoErrengineError": hpevtIoErrengineError,
       "hpevtIoDiscEeMallocErr": hpevtIoDiscEeMallocErr,
       "hpevtIoDiscEeCreatetreeErr": hpevtIoDiscEeCreatetreeErr,
       "hpevtIoDiscEeAttachserviceErr": hpevtIoDiscEeAttachserviceErr,
       "hpevtIoDiscEeInitErr": hpevtIoDiscEeInitErr,
       "hpevtIoDiscEeInitializationErr": hpevtIoDiscEeInitializationErr,
       "hpevtIoDiscEeContextErr": hpevtIoDiscEeContextErr,
       "hpevtIoDiscCreateSbaNodeErr": hpevtIoDiscCreateSbaNodeErr,
       "hpevtIoDiscSbaAttachserviceErr": hpevtIoDiscSbaAttachserviceErr,
       "hpevtIoDiscSbaInitnodeErr": hpevtIoDiscSbaInitnodeErr,
       "hpevtIoDiscSbaUnknownErr": hpevtIoDiscSbaUnknownErr,
       "hpevtIoDeviceMissing": hpevtIoDeviceMissing,
       "hpevtFabricRmtRoutePortBadReroute": hpevtFabricRmtRoutePortBadReroute,
       "hpevtAgtPredictMemFail": hpevtAgtPredictMemFail,
       "hpevtWinAgtLockedProperty": hpevtWinAgtLockedProperty,
       "hpevtIoPciPowerOverloadErr": hpevtIoPciPowerOverloadErr,
       "hpevtMemSbeSeedingEnabled": hpevtMemSbeSeedingEnabled,
       "hpevtFabricWrFailedLinksTopoErr": hpevtFabricWrFailedLinksTopoErr,
       "hpevtBootErrInitGroupCPaFields": hpevtBootErrInitGroupCPaFields,
       "hpevtFabricAssertFabricHop": hpevtFabricAssertFabricHop,
       "hpevtBootFailedReadingProfileCInIcm": hpevtBootFailedReadingProfileCInIcm,
       "hpevtFabricHaltLinkDisableErr": hpevtFabricHaltLinkDisableErr,
       "hpevtBootGetSpiromGetSiblingErr": hpevtBootGetSpiromGetSiblingErr,
       "hpevtCpuClockRatioMismatch": hpevtCpuClockRatioMismatch,
       "hpevtBootStopBootOverride": hpevtBootStopBootOverride,
       "hpevtVgaBiosRelocFail": hpevtVgaBiosRelocFail,
       "hpevtCompMatrixXsumError": hpevtCompMatrixXsumError,
       "hpevtBootGetDefaultRdrsFailed": hpevtBootGetDefaultRdrsFailed,
       "hpevtBootGetCurrentRdrsFailed": hpevtBootGetCurrentRdrsFailed,
       "hpevtBootReadPrefetchFailed": hpevtBootReadPrefetchFailed,
       "hpevtBootReadZlcoFailed": hpevtBootReadZlcoFailed,
       "hpevtBootUpdateZlcoAndPrefetchFailed": hpevtBootUpdateZlcoAndPrefetchFailed,
       "hpevtBootErrorReadingZlcoFlagInPdProfile": hpevtBootErrorReadingZlcoFlagInPdProfile,
       "hpevtBootFindCoreCellCmplxProfileAcErr": hpevtBootFindCoreCellCmplxProfileAcErr,
       "hpevtBootFindCoreCellConfigSelectErr": hpevtBootFindCoreCellConfigSelectErr,
       "hpevtBootCellLclCantFindViable": hpevtBootCellLclCantFindViable,
       "hpevtBootCellRmtCantFindViable": hpevtBootCellRmtCantFindViable,
       "hpevtBootFindCoreCellNotInRendez": hpevtBootFindCoreCellNotInRendez,
       "hpevtBootFindCoreCellLclNotViable": hpevtBootFindCoreCellLclNotViable,
       "hpevtBootFindCoreCellFabriclessPdErr": hpevtBootFindCoreCellFabriclessPdErr,
       "hpevtRtcAccessError": hpevtRtcAccessError,
       "hpevtBootAccessCellArchErr": hpevtBootAccessCellArchErr,
       "hpevtXbcLogSizeErr": hpevtXbcLogSizeErr,
       "hpevtXbcLogClearErr": hpevtXbcLogClearErr,
       "hpevtIodiscPciLogError": hpevtIodiscPciLogError,
       "hpevtIodiscSbaLogError": hpevtIodiscSbaLogError,
       "hpevtXbcInitMaxRetries": hpevtXbcInitMaxRetries,
       "hpevtWinAgtPredictMemFailWarning": hpevtWinAgtPredictMemFailWarning,
       "hpevtWinAgtPredictMemFailCritical": hpevtWinAgtPredictMemFailCritical,
       "hpevtPciFatalRopeParityErr": hpevtPciFatalRopeParityErr,
       "hpevtPciFatalBusError": hpevtPciFatalBusError,
       "hpevtPciFatalDeviceError": hpevtPciFatalDeviceError,
       "hpevtBootErrorReadingFirstBootToken": hpevtBootErrorReadingFirstBootToken,
       "hpevtBootNonPaCellDetected": hpevtBootNonPaCellDetected,
       "hpevtFabricErrorsXbcClearWrErr": hpevtFabricErrorsXbcClearWrErr,
       "hpevtFabricErrorsXbcClearRdGlblErr": hpevtFabricErrorsXbcClearRdGlblErr,
       "hpevtFabricErrorsXbcClrLoSevErr": hpevtFabricErrorsXbcClrLoSevErr,
       "hpevtFabricErrorsXbcClrHiSevErr": hpevtFabricErrorsXbcClrHiSevErr,
       "hpevtFabricErrorsXbcClearRdPortErr": hpevtFabricErrorsXbcClearRdPortErr,
       "hpevtFabricErrsCsrLogClrRdSlicesErr": hpevtFabricErrsCsrLogClrRdSlicesErr,
       "hpevtFabricErrsCsrLogClrCopyBlk0Err": hpevtFabricErrsCsrLogClrCopyBlk0Err,
       "hpevtFabricErrsCsrLogClrCopyBlk2Err": hpevtFabricErrsCsrLogClrCopyBlk2Err,
       "hpevtFabricXbcLoStateResetErr": hpevtFabricXbcLoStateResetErr,
       "hpevtFabricClrXbcSym01Failure": hpevtFabricClrXbcSym01Failure,
       "hpevtFabricClrXbcIsLoCsrErrErr": hpevtFabricClrXbcIsLoCsrErrErr,
       "hpevtFabricClrXbcRdLoLogStateErr": hpevtFabricClrXbcRdLoLogStateErr,
       "hpevtFabricXbcHiStateResetErr": hpevtFabricXbcHiStateResetErr,
       "hpevtFabricClrXbcIsHiCsrErrErr": hpevtFabricClrXbcIsHiCsrErrErr,
       "hpevtFabricClrXbcRdHiLogStateErr": hpevtFabricClrXbcRdHiLogStateErr,
       "hpevtPlatformCacheHashingError": hpevtPlatformCacheHashingError,
       "hpevtFabricXbcWriteableInvalidCsr": hpevtFabricXbcWriteableInvalidCsr,
       "hpevtMcCellsLostConnection": hpevtMcCellsLostConnection,
       "hpevtBuildErrCellDevTree": hpevtBuildErrCellDevTree,
       "hpevtDcnfgFsbInit": hpevtDcnfgFsbInit,
       "hpevtDcnfgCpuParams": hpevtDcnfgCpuParams,
       "hpevtDcnfgCpuIcache": hpevtDcnfgCpuIcache,
       "hpevtDcnfgCpuDcache": hpevtDcnfgCpuDcache,
       "hpevtDcnfgCpuCacheState": hpevtDcnfgCpuCacheState,
       "hpevtDcnfgCpuCacheMonitor": hpevtDcnfgCpuCacheMonitor,
       "hpevtDcnfgCpuMca": hpevtDcnfgCpuMca,
       "hpevtDcnfgCpuDisableMca": hpevtDcnfgCpuDisableMca,
       "hpevtDcnfgCpuSelfTest": hpevtDcnfgCpuSelfTest,
       "hpevtDcnfgCpuL2Cache": hpevtDcnfgCpuL2Cache,
       "hpevtDcnfgCpuDefValue": hpevtDcnfgCpuDefValue,
       "hpevtDcnfgCpuInReg": hpevtDcnfgCpuInReg,
       "hpevtDcnfgCpuProgReg": hpevtDcnfgCpuProgReg,
       "hpevtNoMemSelfTest": hpevtNoMemSelfTest,
       "hpevtCellLatchOpen": hpevtCellLatchOpen,
       "hpevtDcnfgRightCellLatch": hpevtDcnfgRightCellLatch,
       "hpevtCellLatchSensorBad": hpevtCellLatchSensorBad,
       "hpevtVrmVltFault": hpevtVrmVltFault,
       "hpevtVrmTempFlt": hpevtVrmTempFlt,
       "hpevtVrmFlt": hpevtVrmFlt,
       "hpevtVrmIoVltFlt": hpevtVrmIoVltFlt,
       "hpevtPwrBrickVltFlt": hpevtPwrBrickVltFlt,
       "hpevtVrmBkPlaneTempFlt": hpevtVrmBkPlaneTempFlt,
       "hpevtBkPlanePwrBrickTempFlt": hpevtBkPlanePwrBrickTempFlt,
       "hpevtBkPlanVrmRailFlt": hpevtBkPlanVrmRailFlt,
       "hpevtBkPlanePwrBrkFlt": hpevtBkPlanePwrBrkFlt,
       "hpevtBkPlaneVrmVltFlt": hpevtBkPlaneVrmVltFlt,
       "hpevtBkPlaneVrmTempFlt": hpevtBkPlaneVrmTempFlt,
       "hpevtBkPlaneFlt": hpevtBkPlaneFlt,
       "hpevtMstrMpFailed": hpevtMstrMpFailed,
       "hpevtNvramAlloc": hpevtNvramAlloc,
       "hpevtRtcTimeReg": hpevtRtcTimeReg,
       "hpevtPAAFltMx2": hpevtPAAFltMx2,
       "hpevtAPIopenLnkLocCell": hpevtAPIopenLnkLocCell,
       "hpevtCSRreadUnsuccessTimeOut": hpevtCSRreadUnsuccessTimeOut,
       "hpevtCSRWriteUnsuccess": hpevtCSRWriteUnsuccess,
       "hpevtDataErrEncount": hpevtDataErrEncount,
       "hpevtConfigMaxMemory": hpevtConfigMaxMemory,
       "hpevtFailDelBadPort": hpevtFailDelBadPort,
       "hpevtFailDelBadEdge": hpevtFailDelBadEdge,
       "hpevtCommandMemBuf": hpevtCommandMemBuf,
       "hpevtUnsupprtArflsCsrRouteTravsble": hpevtUnsupprtArflsCsrRouteTravsble,
       "hpevtInvalidPortToTravsble": hpevtInvalidPortToTravsble,
       "hpevtUnbleRdXBCPortNghbr": hpevtUnbleRdXBCPortNghbr,
       "hpevtXBCPortUnexpctNghbrChip": hpevtXBCPortUnexpctNghbrChip,
       "hpevtXBCPortHaveUnxpctNghbrID": hpevtXBCPortHaveUnxpctNghbrID,
       "hpevtXBCHaveUnexpctNghbrPrtConn": hpevtXBCHaveUnexpctNghbrPrtConn,
       "hpevtDataNotFndEdgLst": hpevtDataNotFndEdgLst,
       "hpevtXBCPrtUnxpctNgbrChip": hpevtXBCPrtUnxpctNgbrChip,
       "hpevtXBCtoXBCLnkDwn": hpevtXBCtoXBCLnkDwn,
       "hpevtXBCprtFndErrTravsbl": hpevtXBCprtFndErrTravsbl,
       "hpevtUnblRdLnkCelFabCSR": hpevtUnblRdLnkCelFabCSR,
       "hpevtUblRdXBCrouteTbl": hpevtUblRdXBCrouteTbl,
       "hpevtXBCLnkNotConnCSRTravsbl": hpevtXBCLnkNotConnCSRTravsbl,
       "hpevtErrRdAlrecAlbIdCsr": hpevtErrRdAlrecAlbIdCsr,
       "hpevtCirRoutFndTstXbcCsr": hpevtCirRoutFndTstXbcCsr,
       "hpevtXBCRdErrAlrecAlbIdCsr": hpevtXBCRdErrAlrecAlbIdCsr,
       "hpevtXBC-XBCPrtHavInvldChipCnn": hpevtXBC_XBCPrtHavInvldChipCnn,
       "hpevtArflsXbcRotTravrsblCalBakToBak": hpevtArflsXbcRotTravrsblCalBakToBak,
       "hpevtXBCToXBClnkFndFatErr": hpevtXBCToXBClnkFndFatErr,
       "hpevtUnablRdXbcRotTblEnblMskCsr": hpevtUnablRdXbcRotTblEnblMskCsr,
       "hpevtErrRdXbcRotTablCsr": hpevtErrRdXbcRotTablCsr,
       "hpevtXbcPrtErrRdAlrecAlbIDCsr": hpevtXbcPrtErrRdAlrecAlbIDCsr,
       "hpevtXbcPrtFndUnxpctNgbrChip": hpevtXbcPrtFndUnxpctNgbrChip,
       "hpevtCelPrtPairNotFndGrphDat": hpevtCelPrtPairNotFndGrphDat,
       "hpevtArchFabFndLocCelLnkNotConn": hpevtArchFabFndLocCelLnkNotConn,
       "hpevtXbcErrRdRoutCsr": hpevtXbcErrRdRoutCsr,
       "hpevtXbcUnablRdAlrecAlbIdCsr": hpevtXbcUnablRdAlrecAlbIdCsr,
       "hpevtXbcPrtHasUnxpctNgbrChptype": hpevtXbcPrtHasUnxpctNgbrChptype,
       "hpevtCelToCelLnkHasUnxpctNgbrChpType": hpevtCelToCelLnkHasUnxpctNgbrChpType,
       "hpevtCelPrtPairNotExstGrphDat": hpevtCelPrtPairNotExstGrphDat,
       "hpevtCelToCelLnkConnUnxpctNgbrPrt": hpevtCelToCelLnkConnUnxpctNgbrPrt,
       "hpevtCelToCelLnkConnUnxpctCel": hpevtCelToCelLnkConnUnxpctCel,
       "hpevtEFIDrvrFailLoad": hpevtEFIDrvrFailLoad,
       "hpevtVmRetErrNonCohTbl": hpevtVmRetErrNonCohTbl,
       "hpevtNctTblWrtGlobLnkSelNonCohFail": hpevtNctTblWrtGlobLnkSelNonCohFail,
       "hpevtNctTblFailArfPhs3": hpevtNctTblFailArfPhs3,
       "hpevtPostRndevzFailPrepBckToBckSys": hpevtPostRndevzFailPrepBckToBckSys,
       "hpevtArfPhs4UnablSetNonCohLnk": hpevtArfPhs4UnablSetNonCohLnk,
       "hpevtUnablSetNonCohRout": hpevtUnablSetNonCohRout,
       "hpevtUnableSetCohRoutCel": hpevtUnableSetCohRoutCel,
       "hpevtErrWrtXbcRoutTblEnblMskCsr": hpevtErrWrtXbcRoutTblEnblMskCsr,
       "hpevtVertxRetUnxpctErrNonCohTbl": hpevtVertxRetUnxpctErrNonCohTbl,
       "hpevtWrtSkyGlobLnkSelCohFail": hpevtWrtSkyGlobLnkSelCohFail,
       "hpevtUnablWrtXbcPrtCsr": hpevtUnablWrtXbcPrtCsr,
       "hpevtSysFwUnAccesComplxProf": hpevtSysFwUnAccesComplxProf,
       "hpevtSysFwDetctErrFabInit": hpevtSysFwDetctErrFabInit,
       "hpevtSysFwDetctFailFabInit": hpevtSysFwDetctFailFabInit,
       "hpevtSysFwDetctErrFabOptimz": hpevtSysFwDetctErrFabOptimz,
       "hpevtInPwrUPSFail": hpevtInPwrUPSFail,
       "hpevtUpsRestored": hpevtUpsRestored,
       "hpevtUpsExhausted": hpevtUpsExhausted,
       "hpevtSALFailRedzvsProcs": hpevtSALFailRedzvsProcs,
       "hpevtSALFailClrCECLog": hpevtSALFailClrCECLog,
       "hpevtSysFwUnAccesXBCSemphr": hpevtSysFwUnAccesXBCSemphr,
       "hpevtSysFwDetctErrRelXBCGlobSemphr": hpevtSysFwDetctErrRelXBCGlobSemphr,
       "hpevtSysFwDetctErrOwnXBCGlobSemphr": hpevtSysFwDetctErrOwnXBCGlobSemphr,
       "hpevtErrFormXbcSemphrAddr": hpevtErrFormXbcSemphrAddr,
       "hpevtErrRdXbcGlobSemphr": hpevtErrRdXbcGlobSemphr,
       "hpevtFailGetXbcGlobSemphrAddr": hpevtFailGetXbcGlobSemphrAddr,
       "hpevtFailWrtXbcGlobSemphr": hpevtFailWrtXbcGlobSemphr,
       "hpevtFailRdXbcGlobSemphr": hpevtFailRdXbcGlobSemphr,
       "hpevtFailGetAddrXbcGlobSemphr": hpevtFailGetAddrXbcGlobSemphr,
       "hpevtFailWrtXbcGlobSemphrAfrRls": hpevtFailWrtXbcGlobSemphrAfrRls,
       "hpevtFailRelXbcGlobSemphr": hpevtFailRelXbcGlobSemphr,
       "hpevtFabPhsExeInvlOrdr": hpevtFabPhsExeInvlOrdr,
       "hpevtFabPhsExeInvlOrdrDatExpctPhs": hpevtFabPhsExeInvlOrdrDatExpctPhs,
       "hpevtFailGetAddrXbcToXbcLnk": hpevtFailGetAddrXbcToXbcLnk,
       "hpevtFailOpnFabLnk": hpevtFailOpnFabLnk,
       "hpevtErrWrtXbcRetRout": hpevtErrWrtXbcRetRout,
       "hpevtErrEnblXbcRetRout": hpevtErrEnblXbcRetRout,
       "hpevtFailDisprsRoutAcrssLnk": hpevtFailDisprsRoutAcrssLnk,
       "hpevtErrSetXbcToXbcLnkRoutX": hpevtErrSetXbcToXbcLnkRoutX,
       "hpevtErrRoutRemtside": hpevtErrRoutRemtside,
       "hpevtErrGetAddrRoutRemtXbc": hpevtErrGetAddrRoutRemtXbc,
       "hpevtErrGetNgbrInfo": hpevtErrGetNgbrInfo,
       "hpevtErrFindShrtRout": hpevtErrFindShrtRout,
       "hpevtErrWrtRemtXbcRoutReg": hpevtErrWrtRemtXbcRoutReg,
       "hpevtErrEnblRoutRemtXbc": hpevtErrEnblRoutRemtXbc,
       "hpevtErrWrtRoutRegLocXbc": hpevtErrWrtRoutRegLocXbc,
       "hpevtErrWrtLocXbcRoutRegRchRemtCel": hpevtErrWrtLocXbcRoutRegRchRemtCel,
       "hpevtErrEnblLocXbcRout": hpevtErrEnblLocXbcRout,
       "hpevtSynGrphFailPhs4": hpevtSynGrphFailPhs4,
       "hpevtVmVertxFailSyncGrph": hpevtVmVertxFailSyncGrph,
       "hpevtVmEdgFailFncSyncGrph": hpevtVmEdgFailFncSyncGrph,
       "hpevtUnexpctErrCalVertxMod": hpevtUnexpctErrCalVertxMod,
       "hpevtUnexpctRetVertxModCopCelGrph": hpevtUnexpctRetVertxModCopCelGrph,
       "hpevtChecksumPdtFailed": hpevtChecksumPdtFailed,
       "hpevtChecksumNvmBad": hpevtChecksumNvmBad,
       "hpevtChecksumCalcFailed": hpevtChecksumCalcFailed,
       "hpevtSalandBmcTokenBad": hpevtSalandBmcTokenBad,
       "hpevtBkPlaneCable": hpevtBkPlaneCable,
       "hpevtFparUnusable": hpevtFparUnusable,
       "hpevtFWoutOfNvram": hpevtFWoutOfNvram,
       "hpevtNvramCPUCorrupt": hpevtNvramCPUCorrupt,
       "hpevtNvramIOCorrupt": hpevtNvramIOCorrupt,
       "hpevtNvramLocMemCorrupt": hpevtNvramLocMemCorrupt,
       "hpevtFWInconsistExist": hpevtFWInconsistExist,
       "hpevtFWUnableCreatefParsIO": hpevtFWUnableCreatefParsIO,
       "hpevtFWUnableCreatefParsCLM": hpevtFWUnableCreatefParsCLM,
       "hpevtFWOutOfNvram": hpevtFWOutOfNvram,
       "hpevtFWLbaReconfigFail": hpevtFWLbaReconfigFail,
       "hpevtCpuModuleBadConfig": hpevtCpuModuleBadConfig,
       "hpevtCpuInvalidTerminator": hpevtCpuInvalidTerminator,
       "hpevtInvocationSoftResetCode": hpevtInvocationSoftResetCode,
       "hpevtDataSm4SelfReset": hpevtDataSm4SelfReset,
       "hpevtfParsfailRelseResrce": hpevtfParsfailRelseResrce,
       "hpevtPFMManyErrors": hpevtPFMManyErrors,
       "hpevtPFMOverTempProc": hpevtPFMOverTempProc,
       "hpevtPFMCacheErrorProc": hpevtPFMCacheErrorProc,
       "hpevtPFMCorrecErrorCache": hpevtPFMCorrecErrorCache,
       "hpevtPFMCorrErrSysBus": hpevtPFMCorrErrSysBus,
       "hpevtPFMCorrErrProcBus": hpevtPFMCorrErrProcBus,
       "hpevtPFMErrTagMemProc": hpevtPFMErrTagMemProc,
       "hpevtfParsNotEnableBoot": hpevtfParsNotEnableBoot,
       "hpevtfParsNotRecveOwnShip": hpevtfParsNotRecveOwnShip,
       "hpevtFWErrSetNvramVal": hpevtFWErrSetNvramVal,
       "hpevtUnablWrtXbcPrtRoutTblEnblMsk": hpevtUnablWrtXbcPrtRoutTblEnblMsk,
       "hpevtProcessIntrptUnRecoverble": hpevtProcessIntrptUnRecoverble,
       "hpevtSBASetDevMaskFail": hpevtSBASetDevMaskFail,
       "hpevtLBASlotDevScanErr": hpevtLBASlotDevScanErr,
       "hpevtInadequateMemTofPar": hpevtInadequateMemTofPar,
       "hpevtFailCollVertxInfo": hpevtFailCollVertxInfo,
       "hpevtFailCollVertxFabInfoCall": hpevtFailCollVertxFabInfoCall,
       "hpevtFailFndEdgeProcCall": hpevtFailFndEdgeProcCall,
       "hpevtFailFndEdgProcCall": hpevtFailFndEdgProcCall,
       "hpevtManyEdgEncntProcCall": hpevtManyEdgEncntProcCall,
       "hpevtFailGetAddrProcCall": hpevtFailGetAddrProcCall,
       "hpevtUnexpctStatEncntProcCall": hpevtUnexpctStatEncntProcCall,
       "hpevtUnablGetLnkHlthStatProcCall": hpevtUnablGetLnkHlthStatProcCall,
       "hpevtFabDatFailCrcChk": hpevtFabDatFailCrcChk,
       "hpevtVmCollVertcFailUnexpct": hpevtVmCollVertcFailUnexpct,
       "hpevtUnablGenAlbArfSetCsr": hpevtUnablGenAlbArfSetCsr,
       "hpevtSetDefCsrFailUnexpct": hpevtSetDefCsrFailUnexpct,
       "hpevtEncntErrRout": hpevtEncntErrRout,
       "hpevtEncntErrRoutFab": hpevtEncntErrRoutFab,
       "hpevtErrEncntRoutFabPrvntRoutSel": hpevtErrEncntRoutFabPrvntRoutSel,
       "hpevtInvlPrtRetRoutXbcCcLnk": hpevtInvlPrtRetRoutXbcCcLnk,
       "hpevtErrEncntRoutFabPrvntRoutSelSw": hpevtErrEncntRoutFabPrvntRoutSelSw,
       "hpevtSecndFlshNotProgrmValidImg": hpevtSecndFlshNotProgrmValidImg,
       "hpevtSysBckPlnPwr1p2LDOFault": hpevtSysBckPlnPwr1p2LDOFault,
       "hpevtSysBckPlnPwr2p5LDOFault": hpevtSysBckPlnPwr2p5LDOFault,
       "hpevtSysBckPlnPwr3p3HseFault": hpevtSysBckPlnPwr3p3HseFault,
       "hpevtSysBckPlnPwr12Fault": hpevtSysBckPlnPwr12Fault,
       "hpevtSysBckPlnPwr3p3Fault": hpevtSysBckPlnPwr3p3Fault,
       "hpevtSysBckPlnPwr1p5Fault": hpevtSysBckPlnPwr1p5Fault,
       "hpevtSysBckPlnPwr2p5Fault": hpevtSysBckPlnPwr2p5Fault,
       "hpevtPwrRailPrvInsuffPwrToBckPln": hpevtPwrRailPrvInsuffPwrToBckPln,
       "hpevtRcsNoProvClkBckPln": hpevtRcsNoProvClkBckPln,
       "hpevtHsoFaultOrRemv": hpevtHsoFaultOrRemv,
       "hpevtOpClkNoMtchRcsHso": hpevtOpClkNoMtchRcsHso,
       "hpevtClkMrgnBckPlnFail": hpevtClkMrgnBckPlnFail,
       "hpevtHsoNoRedund": hpevtHsoNoRedund,
       "hpevtHsoInsuff": hpevtHsoInsuff,
       "hpevtFailRdRcsHso": hpevtFailRdRcsHso,
       "hpevtFailWrtRcsHso": hpevtFailWrtRcsHso,
       "hpevtFailRdRpm": hpevtFailRdRpm,
       "hpevtFailWrtRpm": hpevtFailWrtRpm,
       "hpevtFailRdOsp": hpevtFailRdOsp,
       "hpevtFailWrtOsp": hpevtFailWrtOsp,
       "hpevtSbsFaultStrt": hpevtSbsFaultStrt,
       "hpevtFailRdIObckPlnLpm": hpevtFailRdIObckPlnLpm,
       "hpevtFailWrtIOBckPlnLpm": hpevtFailWrtIOBckPlnLpm,
       "hpevtSysSoftViolateWellBhaveRule": hpevtSysSoftViolateWellBhaveRule,
       "hpevtAlbInitPrepUnablRdAlrecConfig": hpevtAlbInitPrepUnablRdAlrecConfig,
       "hpevtfParIsDisbleFrmBoot": hpevtfParIsDisbleFrmBoot,
       "hpevtfParNotInstantiateFW": hpevtfParNotInstantiateFW,
       "hpevtfParNotHaveIOResrc": hpevtfParNotHaveIOResrc,
       "hpevtCPUsDeconfig": hpevtCPUsDeconfig,
       "hpevtCPUsReconfig": hpevtCPUsReconfig,
       "hpevtIOBckPln33VFail": hpevtIOBckPln33VFail,
       "hpevtBckPln5VFail": hpevtBckPln5VFail,
       "hpevtIOBckPlnNeg12VFail": hpevtIOBckPlnNeg12VFail,
       "hpevtIOBckPln12VFail": hpevtIOBckPln12VFail,
       "hpevtIOBckPln15VTempFail": hpevtIOBckPln15VTempFail,
       "hpevtIOBckPln33VTempFail": hpevtIOBckPln33VTempFail,
       "hpevtIOBckPlnNeg12VTempFail": hpevtIOBckPlnNeg12VTempFail,
       "hpevtIOBckPln12VTempFail": hpevtIOBckPln12VTempFail,
       "hpevtLocCelUnablClrLnkOffBit": hpevtLocCelUnablClrLnkOffBit,
       "hpevtArfOlaPreRendezUnablRchCel": hpevtArfOlaPreRendezUnablRchCel,
       "hpevtUnexpctErrSetNctTbl": hpevtUnexpctErrSetNctTbl,
       "hpevtPhs4UnexpctFail": hpevtPhs4UnexpctFail,
       "hpevtUnablSyncGrphCell": hpevtUnablSyncGrphCell,
       "hpevtBitMapUnrchCel": hpevtBitMapUnrchCel,
       "hpevtRetValNctCohTbl": hpevtRetValNctCohTbl,
       "hpevtArfRoutEnblRetErrLocCel": hpevtArfRoutEnblRetErrLocCel,
       "hpevtArfRoutDisRetErrOla": hpevtArfRoutDisRetErrOla,
       "hpevtArfRoutDisRetErrArfPhs4": hpevtArfRoutDisRetErrArfPhs4,
       "hpevtMemAlloctFail": hpevtMemAlloctFail,
       "hpevtMemLockFail": hpevtMemLockFail,
       "hpevtMinProcReqMoreThanAvail": hpevtMinProcReqMoreThanAvail,
       "hpevtVMNotHandlGuestOSPerf": hpevtVMNotHandlGuestOSPerf,
       "hpevtKernlDrvFailLckMem": hpevtKernlDrvFailLckMem,
       "hpevtMMIOmapFndInfoInTble": hpevtMMIOmapFndInfoInTble,
       "hpevtAttmptAddPCImoreThanAllow": hpevtAttmptAddPCImoreThanAllow,
       "hpevtCPUConfigNotSupprt": hpevtCPUConfigNotSupprt,
       "hpevtISAUARTcreatWithoutDatStrct": hpevtISAUARTcreatWithoutDatStrct,
       "hpevtTCGETorIOCTLFail": hpevtTCGETorIOCTLFail,
       "hpevtStatCallPMANFail": hpevtStatCallPMANFail,
       "hpevtVMDrvNotOpen": hpevtVMDrvNotOpen,
       "hpevtVMDrvNotCreatVM": hpevtVMDrvNotCreatVM,
       "hpevtNotAbleCreatNodeForComm": hpevtNotAbleCreatNodeForComm,
       "hpevtVMNotOpen": hpevtVMNotOpen,
       "hpevtVMDrvNotLoad": hpevtVMDrvNotLoad,
       "hpevtCreatThreadPMANFail": hpevtCreatThreadPMANFail,
       "hpevtVMDrvUnableCommVM": hpevtVMDrvUnableCommVM,
       "hpevtConfigUnableToRd": hpevtConfigUnableToRd,
       "hpevtMemAllocFWTblFail": hpevtMemAllocFWTblFail,
       "hpevtDrvUnableBldMapTbl": hpevtDrvUnableBldMapTbl,
       "hpevtVMRebootFail": hpevtVMRebootFail,
       "hpevtSetIntlCohTblRetErr": hpevtSetIntlCohTblRetErr,
       "hpBootStblStoreFlashErr": hpBootStblStoreFlashErr,
       "hpBootStblStoreNvMErr": hpBootStblStoreNvMErr,
       "hpevtFWDetectilleglMemConfig": hpevtFWDetectilleglMemConfig,
       "hpevtSFWFailAllotNVM": hpevtSFWFailAllotNVM,
       "hpevtSFWFailAllotSCRRAM": hpevtSFWFailAllotSCRRAM,
       "hpevtSetIntlCohRetErrArfPhs3": hpevtSetIntlCohRetErrArfPhs3,
       "hpevtErrWrtErrMskAlrecAlTran": hpevtErrWrtErrMskAlrecAlTran,
       "hpevtFwUnexpctIntrnlErrVertx": hpevtFwUnexpctIntrnlErrVertx,
       "hpOsUnsupportedWmixedCpuRevs": hpOsUnsupportedWmixedCpuRevs,
       "hpevtFwUnexpctErrSetLnk": hpevtFwUnexpctErrSetLnk,
       "hpevtFwUnbleWrtSkyGlobLnkSelCoh": hpevtFwUnbleWrtSkyGlobLnkSelCoh,
       "hpOsBootDisabledWmixedCpuKeys": hpOsBootDisabledWmixedCpuKeys,
       "hpevtSysFwErrUpdtLnk": hpevtSysFwErrUpdtLnk,
       "hpevtFabUnablGenSkyCsrAddr": hpevtFabUnablGenSkyCsrAddr,
       "hpevtFwUnablGenSkyCsrAdrr": hpevtFwUnablGenSkyCsrAdrr,
       "hpevtNoOSBootRendez": hpevtNoOSBootRendez,
       "hpevtChksmFailOSBootRendez": hpevtChksmFailOSBootRendez,
       "hpevtSysFWCallPalCopyInfoFail": hpevtSysFWCallPalCopyInfoFail,
       "hpevtSysFWCallPalCopyPalFail": hpevtSysFWCallPalCopyPalFail,
       "hpevtSysFWCallPalCacFlusFail": hpevtSysFWCallPalCacFlusFail,
       "hpevtCellNotInit": hpevtCellNotInit,
       "hpevtFPARsCompBroke": hpevtFPARsCompBroke,
       "hpevtFailGetFPARsSemphr": hpevtFailGetFPARsSemphr,
       "hpevtMorThnOneProcCallCell": hpevtMorThnOneProcCallCell,
       "hpevtFPARsProcFailRendez": hpevtFPARsProcFailRendez,
       "hpevtEncntUnexptErrOLA": hpevtEncntUnexptErrOLA,
       "hpevtMCAOccPriorPreMCA": hpevtMCAOccPriorPreMCA,
       "hpevtMCAInitEvtProc": hpevtMCAInitEvtProc,
       "hpevtUnablFndBadEdg": hpevtUnablFndBadEdg,
       "hpevtUnknEntityDrwPwrBus": hpevtUnknEntityDrwPwrBus,
       "hpevtSoftPartNotBoot": hpevtSoftPartNotBoot,
       "hpevtUnablRotArndBrkLnk": hpevtUnablRotArndBrkLnk,
       "hpevtUnablSetAPERLock": hpevtUnablSetAPERLock,
       "hpevtUncorrtMemEccErrOccr": hpevtUncorrtMemEccErrOccr,
       "hpevtErrRetrvCrssbarLnk": hpevtErrRetrvCrssbarLnk,
       "hpevtUnablRdCrssbar": hpevtUnablRdCrssbar,
       "hpevtUnablEstbshCrssbar": hpevtUnablEstbshCrssbar,
       "hpevtNoRoutLocCrssBar": hpevtNoRoutLocCrssBar,
       "hpevtInvalidTPM": hpevtInvalidTPM,
       "hpevtTPMFailInit": hpevtTPMFailInit,
       "hpevtCpuTempExceedHiThres": hpevtCpuTempExceedHiThres,
       "hpevtSFWDetErrStablStorFlsh": hpevtSFWDetErrStablStorFlsh,
       "hpevtInlckOpenPCIPwr": hpevtInlckOpenPCIPwr,
       "hpevtFaltDetDropRegIO": hpevtFaltDetDropRegIO,
       "hpevtFaltDetDropRegManBckPlne": hpevtFaltDetDropRegManBckPlne,
       "hpevtFaltDetHotswpCoreIO": hpevtFaltDetHotswpCoreIO,
       "hpevtErrRetrvCrssbarChipNmbr": hpevtErrRetrvCrssbarChipNmbr,
       "hpevtCellNotCfgCLMMode": hpevtCellNotCfgCLMMode,
       "hpevttDoblDramInvoke": hpevttDoblDramInvoke,
       "hpevtErrCrssbarCrctByHW": hpevtErrCrssbarCrctByHW,
       "hpevtErrCrssChipBckPln": hpevtErrCrssChipBckPln,
       "hpevtErrCeLLIO": hpevtErrCeLLIO,
       "hpevtMltPltFrmErrCellBckPln": hpevtMltPltFrmErrCellBckPln,
       "hpevtMultPltFrmErrCrssChpBckPln": hpevtMultPltFrmErrCrssChpBckPln,
       "hpevtMultPltFrmErrCeLLIO": hpevtMultPltFrmErrCeLLIO,
       "hpevtServIDNotMatchCab": hpevtServIDNotMatchCab,
       "hpevtDupDimNumDetect": hpevtDupDimNumDetect,
       "hpevtMPLostUPS": hpevtMPLostUPS,
       "hpevtMPGainLanCommUPS": hpevtMPGainLanCommUPS,
       "hpevtUnrecovProcIFAinterptInFW": hpevtUnrecovProcIFAinterptInFW,
       "hpevtUnrecovProcISRinterptInFW": hpevtUnrecovProcISRinterptInFW,
       "hpevtDblChipSpareInvoked": hpevtDblChipSpareInvoked,
       "hpevtExtClkCablRemvFrmCPUCab": hpevtExtClkCablRemvFrmCPUCab,
       "hpevtSysFabEncntLnkErr": hpevtSysFabEncntLnkErr,
       "hpevtFatErrOnCelToFabPrt44I32I1": hpevtFatErrOnCelToFabPrt44I32I1,
       "hpevtSysFWgetFabProblm": hpevtSysFWgetFabProblm,
       "hpevtFatErrCelLnkToFabPrt44I32": hpevtFatErrCelLnkToFabPrt44I32,
       "hpevtSysOSRecovFrmPCIErrL1": hpevtSysOSRecovFrmPCIErrL1,
       "hpevtSysOSRecovFrmPCIErrL2": hpevtSysOSRecovFrmPCIErrL2,
       "hpevtSysOSRecovFrmPCIErrL5": hpevtSysOSRecovFrmPCIErrL5,
       "hpevtReqPwrOnDenied": hpevtReqPwrOnDenied,
       "hpevtBladeFrcPWon": hpevtBladeFrcPWon,
       "hpevtMPNotRecvRespEnclMangr": hpevtMPNotRecvRespEnclMangr,
       "hpevtIntrnlSwErr7193": hpevtIntrnlSwErr7193,
       "hpevtIntrnlSwErr7194": hpevtIntrnlSwErr7194,
       "hpevtIntrnlSwErr7195": hpevtIntrnlSwErr7195,
       "hpevtIntrnlSwErr7196": hpevtIntrnlSwErr7196,
       "hpevtComplxProfNoMtch": hpevtComplxProfNoMtch,
       "hpevtIODevMissCore": hpevtIODevMissCore,
       "hpevtFparUnablNotiCPU": hpevtFparUnablNotiCPU,
       "hpevtFparUnablNotiCpuIOSAPICredir": hpevtFparUnablNotiCpuIOSAPICredir,
       "hpevtOSSetWtchDogTimerToTimeOut": hpevtOSSetWtchDogTimerToTimeOut,
       "hpevtOSShtDwnDueMCA": hpevtOSShtDwnDueMCA,
       "hpevtOSShtDwnDuePanic": hpevtOSShtDwnDuePanic,
       "hpevtCLUFWIncomptblSysType": hpevtCLUFWIncomptblSysType,
       "hpevtOnlnIdentHWProb": hpevtOnlnIdentHWProb,
       "hpevtProcOvTemp": hpevtProcOvTemp,
       "hpevtErrChkFabBootStat": hpevtErrChkFabBootStat,
       "hpevtSysFwUnblClrLnkErrMsk": hpevtSysFwUnblClrLnkErrMsk,
       "hpevtSysFwNotDetLnkAdrr": hpevtSysFwNotDetLnkAdrr,
       "hpevtSysFwUnblTurnBadLnkOff": hpevtSysFwUnblTurnBadLnkOff,
       "hpevtWindWtchDogXpired": hpevtWindWtchDogXpired,
       "hpevtMPCtrlReprtMPBusCommFail": hpevtMPCtrlReprtMPBusCommFail,
       "hpevt12VPCIFailonIOChass": hpevt12VPCIFailonIOChass,
       "hpevtSFWDetFailOptmzFab": hpevtSFWDetFailOptmzFab,
       "hpevtCritFailCellOnline": hpevtCritFailCellOnline,
       "hpevtCellHasIncomptbleHwFW": hpevtCellHasIncomptbleHwFW,
       "hpevtCellFWnotMatchPartFW": hpevtCellFWnotMatchPartFW,
       "hpevtVMSDetctUnrecvrdEvnt": hpevtVMSDetctUnrecvrdEvnt,
       "hpevtBadCellBrdOrBadProcBrd": hpevtBadCellBrdOrBadProcBrd,
       "hpevtCPUDegradErrThirdCache": hpevtCPUDegradErrThirdCache,
       "hpevtROMFailAuthentc": hpevtROMFailAuthentc,
       "hpevtAltrntROMUnblSwap": hpevtAltrntROMUnblSwap,
       "hpevtPciSlotErrDetect": hpevtPciSlotErrDetect,
       "hpevtCCLinkDown": hpevtCCLinkDown,
       "hpevtUnrecovProcIntOccr": hpevtUnrecovProcIntOccr,
       "hpevtElectrncKeyProblm": hpevtElectrncKeyProblm,
       "hpevtBldeInstImproperLoc": hpevtBldeInstImproperLoc,
       "hpevtbldeInstViolateEnclre": hpevtbldeInstViolateEnclre,
       "hpevtsx2000FabRprtUnexpctErr": hpevtsx2000FabRprtUnexpctErr,
       "hpevtOANotServPwrOnReqst": hpevtOANotServPwrOnReqst,
       "hpevtIOBckPlnReprtNonRedundncyPCIPwr": hpevtIOBckPlnReprtNonRedundncyPCIPwr,
       "hpevtUSBStorAttch": hpevtUSBStorAttch,
       "hpevtUSBStorRemoved": hpevtUSBStorRemoved,
       "hpevtMigratSrcNotConnt": hpevtMigratSrcNotConnt,
       "hpevtMigratFail": hpevtMigratFail,
       "hpevtMigratNotSuccess": hpevtMigratNotSuccess,
       "hpevtVMNotAlloctMemForIO": hpevtVMNotAlloctMemForIO,
       "hpevtUnSupprtDimmInPartition": hpevtUnSupprtDimmInPartition,
       "hpevtRuntimeCritShtDwn": hpevtRuntimeCritShtDwn,
       "hpevtPwrExptGreatrPwrBulk": hpevtPwrExptGreatrPwrBulk,
       "hpevtBulkPwrReduncLost": hpevtBulkPwrReduncLost,
       "hpevtACReduncLost": hpevtACReduncLost,
       "hpevtFanCoolNotRedunc": hpevtFanCoolNotRedunc,
       "hpevtFanInsufficientInCoolDomain": hpevtFanInsufficientInCoolDomain,
       "hpevtOSNotUseAllProcs": hpevtOSNotUseAllProcs,
       "hpevtFMPUnexpctRstHasRcv": hpevtFMPUnexpctRstHasRcv,
       "hpIpfEvtDetailStr": hpIpfEvtDetailStr,
       "hpIpf02Events": hpIpf02Events}
)
